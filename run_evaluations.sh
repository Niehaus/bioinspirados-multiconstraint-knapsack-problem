sudo rm tests/Evaluation/PB1_mean_final.txt
touch tests/Evaluation/PB1_mean_final.txt
sudo chmod 777 tests/Evaluation/PB1_mean_final.txt
echo -e "Geração\tÓtimo\tMédia dos Fitnesses\tDesvio Padrão" >> tests/Evaluation/PB1_mean_final.txt
python3 m2.py instances/PB1.txt tests/Evaluation/PB1_mean_final.txt 50 85 0.5 0.5

sudo rm tests/Evaluation/PB2_mean_final.txt
touch tests/Evaluation/PB2_mean_final.txt
sudo chmod 777 tests/Evaluation/PB2_mean_final.txt
echo -e "Geração\tÓtimo\tMédia dos Fitnesses\tDesvio Padrão" >> tests/Evaluation/PB2_mean_final.txt
python3 m2.py instances/PB2.txt tests/Evaluation/PB2_mean_final.txt 100 50 0.5 0.5

sudo rm tests/Evaluation/PB4_mean_final.txt
touch tests/Evaluation/PB4_mean_final.txt
sudo chmod 777 tests/Evaluation/PB4_mean_final.txt
echo -e "Geração\tÓtimo\tMédia dos Fitnesses\tDesvio Padrão" >> tests/Evaluation/PB4_mean_final.txt
python3 m2.py instances/PB4.txt tests/Evaluation/PB4_mean_final.txt 50 100 0.5 1.25

sudo rm tests/Evaluation/PB5_mean_final.txt
touch tests/Evaluation/PB5_mean_final.txt
sudo chmod 777 tests/Evaluation/PB5_mean_final.txt
echo -e "Geração\tÓtimo\tMédia dos Fitnesses\tDesvio Padrão" >> tests/Evaluation/PB5_mean_final.txt
python3 m2.py instances/PB5.txt tests/Evaluation/PB5_mean_final.txt 100 85 0.5 0.5

sudo rm tests/Evaluation/PB6_mean_final.txt
touch tests/Evaluation/PB6_mean_final.txt
sudo chmod 777 tests/Evaluation/PB6_mean_final.txt
echo -e "Geração\tÓtimo\tMédia dos Fitnesses\tDesvio Padrão" >> tests/Evaluation/PB6_mean_final.txt
python3 m2.py instances/PB6.txt tests/Evaluation/PB6_mean_final.txt 100 100 1 1

sudo rm tests/Evaluation/PB7_mean_final.txt
touch tests/Evaluation/PB7_mean_final.txt
sudo chmod 777 tests/Evaluation/PB7_mean_final.txt
echo -e "Geração\tÓtimo\tMédia dos Fitnesses\tDesvio Padrão" >> tests/Evaluation/PB7_mean_final.txt
python3 m2.py instances/PB7.txt tests/Evaluation/PB7_mean_final.txt 100 50 0.5 0.5