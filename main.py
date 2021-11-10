# pc performance respect to hardware
from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
from fuzzy_system.fuzzy_system import FuzzySystem

cpu_temps = FuzzyInputVariable('CPU Temperature', 0, 105, 100)
cpu_temps.add_triangular('Cold', 0, 25, 40)
cpu_temps.add_trapezoidal('Medium', 30, 50, 70, 85)
cpu_temps.add_triangular('Hot', 85, 95, 105)

utilize = FuzzyInputVariable('CPU Utilization', 0, 100, 100)
utilize.add_triangular('Low', 0, 15, 30)
utilize.add_trapezoidal('Normal', 25, 35, 50, 65)
utilize.add_trapezoidal('High', 60, 75, 90, 100)

cpu_speed = FuzzyOutputVariable('CPU Speed', 0, 100, 100)
cpu_speed.add_triangular('Slow', 5, 15, 30)
cpu_speed.add_trapezoidal('Moderate', 30, 45, 65, 75)
cpu_speed.add_triangular('Fast', 70, 85, 100)

cpu_fan_speed = FuzzyOutputVariable('CPU Fan', 0, 100, 100)
cpu_fan_speed.add_triangular('Slow', 0, 15, 35)
cpu_fan_speed.add_trapezoidal('Medium', 30, 50, 65, 80)
# cpu_fan_speed.add_triangular('Fast', 85, 90, 100)
cpu_fan_speed.add_trapezoidal('Fast', 85, 90, 95, 100)

system = FuzzySystem()
system.add_input_variable(cpu_temps)
system.add_input_variable(utilize)
system.add_output_variable(cpu_speed)
system.add_output_variable(cpu_fan_speed)

system.add_rule(
		{ 'CPU Temperature':'Cold',
			'CPU Utilization':'Low' },
		{ 'CPU Speed':'Fast', 'CPU Fan':'Slow'})

system.add_rule(
		{ 'CPU Temperature':'Cold',
			'CPU Utilization':'Normal' },
		{ 'CPU Speed':'Fast', 'CPU Fan': 'Slow'})

system.add_rule(
		{ 'CPU Temperature':'Cold',
			'CPU Utilization':'High' },
		{ 'CPU Speed':'Slow', 'CPU Fan':'Medium'})

system.add_rule(
		{ 'CPU Temperature':'Medium',
			'CPU Utilization':'Low' },
		{ 'CPU Speed':'Fast', 'CPU Fan': 'Slow'})

system.add_rule(
		{ 'CPU Temperature':'Medium',
			'CPU Utilization':'Normal' },
		{ 'CPU Speed':'Moderate', 'CPU Fan':'Medium'})

system.add_rule(
		{ 'CPU Temperature':'Medium',
			'CPU Utilization':'High' },
		{ 'CPU Speed':'Slow', 'CPU Fan': 'Fast'})

system.add_rule(
		{ 'CPU Temperature':'Hot',
			'CPU Utilization':'Low' },
		{ 'CPU Speed':'Moderate', 'CPU Fan': 'Medium'})

system.add_rule(
		{ 'CPU Temperature':'Hot',
			'CPU Utilization':'Normal' },
		{ 'CPU Speed':'Slow', 'CPU Fan': 'Fast'})

system.add_rule(
		{ 'CPU Temperature':'Hot',
			'CPU Utilization':'High' },
		{ 'CPU Speed':'Slow', 'CPU Fan': 'Fast'})

result = system.evaluate_output({
				'CPU Temperature':50,
				'CPU Utilization':40  })
# print(result.values())
print(f"The current CPU speed percentage is: {round(result['CPU Speed'], 3)} \nCPU Fan speed is: {round(result['CPU Fan'], 3)}")

# system.plot_system()

