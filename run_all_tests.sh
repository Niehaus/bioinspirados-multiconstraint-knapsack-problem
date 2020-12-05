tests=(1)
instances=("PB1" "PB2" "PB4" "PB5" "PB6" "PB7")

for t in "${tests[@]}"
do
	for i in "${instances[@]}"
	do
		echo "<< TESTE $t $i >>"
		./ant_system_sh.sh instances/$i.txt tests/Calibration/$i/test_$t.txt
	done
done