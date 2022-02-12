#!/bin/bash

echo "infinite loop"

while true
do
    echo '...... docker exec -it ${ID} /bin/bash ......'
    echo '...... get into run `runner.sh` and `python3 hello.py` .....'
    echo '...... sleep 5 ......'
    sleep 5
done


