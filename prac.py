from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
from fuzzy_system.fuzzy_system import FuzzySystem

con_error = FuzzyInputVariable("Contour Error", -6, 6, 100)
con_error.add_trapezoidal("NL", -6, -6, -4.5, -3)
con_error.add_triangular("NM", -4.5, -3, -1.5)
con_error.add_triangular("NS", -3, -1.5, 0)
con_error.add_triangular("ZR", -1.5, 0, 1.5)
con_error.add_triangular("PS", 0, 1.5, 3)
con_error.add_triangular("PM", 1.5, 3, 4.5)
con_error.add_trapezoidal("PL", 3, 4.5, 6, 6)

con_error_change = FuzzyInputVariable("Contour error Change", -0.9, 0.9, 100)
con_error_change.add_trapezoidal("NL", -0.9, -0.9, -0.675, -0.45)
con_error_change.add_triangular("NM", -0.675, -0.45, -0.225)
con_error_change.add_triangular("NS", -0.45, -0.225, 0)
con_error_change.add_triangular("ZR", -0.225, 0, 0.225)
con_error_change.add_triangular("PS", 0, 0.225, 0.45)
con_error_change.add_triangular("PM", 0.225, 0.45, 0.675)
con_error_change.add_trapezoidal("PL", 0.45, 0.675, 0.9, 0.9)

ctrl_act = FuzzyOutputVariable("Control Action", -61, 61, 100)
ctrl_act.add_triangular("NL", -61, -60, -59)
ctrl_act.add_triangular("NM", -41, -40, -39)
ctrl_act.add_triangular("NS", -21, -20, -19)
ctrl_act.add_triangular("ZR", -1, 0, 1)
ctrl_act.add_triangular("PS", 19, 20, 21)
ctrl_act.add_triangular("PM", 39, 40, 41)
ctrl_act.add_triangular("PL", 59, 60, 61)

system = FuzzySystem()
system.add_input_variable(con_error)
system.add_input_variable(con_error_change)
system.add_output_variable(ctrl_act)




system.add_rule(
		{ 'Contour Error':'NL',
			'Contour error Change':'NL' },
		{ 'Control Action':'NL'})
system.add_rule(
		{ 'Contour Error':'NL',
			'Contour error Change':'NM' },
		{ 'Control Action':'NL'})
system.add_rule(
		{ 'Contour Error':'NL',
			'Contour error Change':'NS' },
		{ 'Control Action':'NL'})
system.add_rule(
		{ 'Contour Error':'NL',
			'Contour error Change':'ZR' },
		{ 'Control Action':'NL'})
system.add_rule(
		{ 'Contour Error':'NL',
			'Contour error Change':'PS' },
		{ 'Control Action':'NL'})
system.add_rule(
		{ 'Contour Error':'NL',
			'Contour error Change':'PM' },
		{ 'Control Action':'NL'})
system.add_rule(
		{ 'Contour Error':'NL',
			'Contour error Change':'PL' },
		{ 'Control Action':'NL'})



system.add_rule(
		{ 'Contour Error':'NM',
			'Contour error Change':'NL' },
		{ 'Control Action':'NL'})
system.add_rule(
		{ 'Contour Error':'NM',
			'Contour error Change':'NM' },
		{ 'Control Action':'NL'})
system.add_rule(
		{ 'Contour Error':'NM',
			'Contour error Change':'NS' },
		{ 'Control Action':'NM'})
system.add_rule(
		{ 'Contour Error':'NM',
			'Contour error Change':'ZR' },
		{ 'Control Action':'NM'})
system.add_rule(
		{ 'Contour Error':'NM',
			'Contour error Change':'PS' },
		{ 'Control Action':'NS'})
system.add_rule(
		{ 'Contour Error':'NM',
			'Contour error Change':'PM' },
		{ 'Control Action':'NS'})
system.add_rule(
		{ 'Contour Error':'NM',
			'Contour error Change':'PL' },
		{ 'Control Action':'NS'})



system.add_rule(
		{ 'Contour Error':'NS',
			'Contour error Change':'NL' },
		{ 'Control Action':'NL'})
system.add_rule(
		{ 'Contour Error':'NS',
			'Contour error Change':'NM' },
		{ 'Control Action':'NM'})
system.add_rule(
		{ 'Contour Error':'NS',
			'Contour error Change':'NS' },
		{ 'Control Action':'NM'})
system.add_rule(
		{ 'Contour Error':'NS',
			'Contour error Change':'ZR' },
		{ 'Control Action':'NS'})
system.add_rule(
		{ 'Contour Error':'NS',
			'Contour error Change':'PS' },
		{ 'Control Action':'NS'})
system.add_rule(
		{ 'Contour Error':'NS',
			'Contour error Change':'PM' },
		{ 'Control Action':'NS'})
system.add_rule(
		{ 'Contour Error':'NS',
			'Contour error Change':'PL' },
		{ 'Control Action':'ZR'})



system.add_rule(
		{ 'Contour Error':'ZR',
			'Contour error Change':'NL' },
		{ 'Control Action':'ZR'})
system.add_rule(
		{ 'Contour Error':'ZR',
			'Contour error Change':'NM' },
		{ 'Control Action':'ZR'})
system.add_rule(
		{ 'Contour Error':'ZR',
			'Contour error Change':'NS' },
		{ 'Control Action':'ZR'})
system.add_rule(
		{ 'Contour Error':'ZR',
			'Contour error Change':'ZR' },
		{ 'Control Action':'ZR'})
system.add_rule(
		{ 'Contour Error':'ZR',
			'Contour error Change':'PS' },
		{ 'Control Action':'ZR'})
system.add_rule(
		{ 'Contour Error':'ZR',
			'Contour error Change':'PM' },
		{ 'Control Action':'ZR'})
system.add_rule(
		{ 'Contour Error':'ZR',
			'Contour error Change':'PL' },
		{ 'Control Action':'ZR'})


system.add_rule(
		{ 'Contour Error':'PS',
			'Contour error Change':'NL' },
		{ 'Control Action':'ZR'})
system.add_rule(
		{ 'Contour Error':'PS',
			'Contour error Change':'NM' },
		{ 'Control Action':'PS'})
system.add_rule(
		{ 'Contour Error':'PS',
			'Contour error Change':'NS' },
		{ 'Control Action':'PS'})
system.add_rule(
		{ 'Contour Error':'PS',
			'Contour error Change':'ZR' },
		{ 'Control Action':'PS'})
system.add_rule(
		{ 'Contour Error':'PS',
			'Contour error Change':'PS' },
		{ 'Control Action':'PM'})
system.add_rule(
		{ 'Contour Error':'PS',
			'Contour error Change':'PM' },
		{ 'Control Action':'PM'})
system.add_rule(
		{ 'Contour Error':'PS',
			'Contour error Change':'PL' },
		{ 'Control Action':'PL'})



system.add_rule(
		{ 'Contour Error':'PM',
			'Contour error Change':'NL' },
		{ 'Control Action':'PS'})
system.add_rule(
		{ 'Contour Error':'PM',
			'Contour error Change':'NM' },
		{ 'Control Action':'PS'})
system.add_rule(
		{ 'Contour Error':'PM',
			'Contour error Change':'NS' },
		{ 'Control Action':'PS'})
system.add_rule(
		{ 'Contour Error':'PM',
			'Contour error Change':'ZR' },
		{ 'Control Action':'PM'})
system.add_rule(
		{ 'Contour Error':'PM',
			'Contour error Change':'PS' },
		{ 'Control Action':'PM'})
system.add_rule(
		{ 'Contour Error':'PM',
			'Contour error Change':'PM' },
		{ 'Control Action':'PL'})
system.add_rule(
		{ 'Contour Error':'PM',
			'Contour error Change':'PL' },
		{ 'Control Action':'PL'})



system.add_rule(
		{ 'Contour Error':'PL',
			'Contour error Change':'NL' },
		{ 'Control Action':'PL'})
system.add_rule(
		{ 'Contour Error':'PL',
			'Contour error Change':'NM' },
		{ 'Control Action':'PL'})
system.add_rule(
		{ 'Contour Error':'PL',
			'Contour error Change':'NS' },
		{ 'Control Action':'PL'})
system.add_rule(
		{ 'Contour Error':'PL',
			'Contour error Change':'ZR' },
		{ 'Control Action':'PL'})
system.add_rule(
		{ 'Contour Error':'PL',
			'Contour error Change':'PS' },
		{ 'Control Action':'PL'})
system.add_rule(
		{ 'Contour Error':'PL',
			'Contour error Change':'PM' },
		{ 'Control Action':'PL'})
system.add_rule(
		{ 'Contour Error':'PL',
			'Contour error Change':'PL' },
		{ 'Control Action':'PL'})

result = system.evaluate_output({
				'Contour Error':-6,
				'Contour error Change':-0.89 })


# print(result.values())

print(f"\nControl Action is: {round(result['Control Action'], 3)}")
# print(f"the new outputs are : {result.keys()} and keys are: {result.values()}")


system.plot_system()