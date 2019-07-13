#!/bin/sh

time_of_day() {
	hour=$1
	if [ -z "$hour" ]; then
		echo "Error! empty arg for time_of_day() func" >&2
		return 1
	fi
	if [ 0 -gt "$hour" ] || [ "$hour" -gt 23 ]; then
		echo "Error! arg not in [0, 23]" >&2
		return 2
	fi
	if [ "$hour" -le 5 ] || [ "$hour" -gt 22 ]; then
	    echo "Доброй ночи!"
	elif [ "$hour" -le 12 ]; then
	    echo "Доброго утра!"
	elif [ "$hour" -le 17 ]; then
	    echo "Добрый день!"
	elif [ "$hour" -le 22 ]; then
	    echo "Добрый вечер!"
	else
	    return 1
	fi

}

run_tests() {
	set -x -e
	[ "$(time_of_day 10)" = "Доброго утра!" ]
	[ "$(time_of_day 0)" = "Доброй ночи!" ]
	! time_of_day -
	! time_of_day 25
	! time_of_day -1
	! time_of_day
}

main() {
	x=`date +%H`
	time_of_day $x
}

if [ "$1" = "--test" ]; then
	run_tests
else
	main
fi


