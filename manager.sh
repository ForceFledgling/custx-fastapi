#!/bin/bash

function init {
    # Create a directory for migration files
    python3 -m alembic revision --autogenerate -m "Init"
    python3 -m alembic upgrade head
}

function revision {
    python3 -m alembic revision --autogenerate -m "$2"
}

function migrate {
    # Run the migration
    python3 -m alembic upgrade head
}

function run {
    # Run the autocorrect script
    python3 -m app --reload
}

function start {
    # Start screen session for the autocorrect script
    screen -dmS custx python3 -m app --reload
    echo "Screen session for autocorrect started."
}

function stop {
    # Stop screen session for the autocorrect script
    screen -XS custx quit
    echo "Screen session for autocorrect stopped."
}

if [ -z "$1" ]; then
    # If no argument is passed, do not run the script
    echo "Use case: ./manager.sh start/stop"
    exit
else
    # If an argument is passed, run the script
    actions=("init" "revision" "migrate" "run" "start" "stop")
    action=$1
    if [[ ${actions[*]} =~ $action ]]; then
        if [ -z "$2" ]; then
            $action
        else
            $action $2
        fi
    else
        # If the argument is not valid, do not run the script
        echo "Actipn '$actions' not found."
    fi
fi