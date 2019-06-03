.PHONY=test prepare debug converge

test:
	molecule test

prepare:
	molecule prepare

debug:
	molecule --debug converge

converge:
	molecule converge
