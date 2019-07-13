#!/bin/sh -xe

run_test() {
	datetime=$1
	expect="$2"
	
	date --set="$datetime"
	[ "$(./homework.sh)" = "$expect" ]
}

run_test 5:00 "Доброй ночи!"
run_test 6:00 "Доброго утра!"
run_test 5:59:59 "Доброй ночи!"


