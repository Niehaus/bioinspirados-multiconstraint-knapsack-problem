sudo rm tests/Evaluation/PB1_mean.txt
touch tests/Evaluation/PB1_mean.txt
sudo chmod 777 tests/Evaluation/PB1_mean.txt
echo -e "Geração\tÓtimo\tMédia dos Fitnesses\tDesvio Padrão" >> tests/Evaluation/PB1_mean.txt
python3 main.py instances/PB1.txt tests/Evaluation/PB1_mean.txt 50 85 0.5 0.5

sudo rm tests/Evaluation/PB2_mean.txt
touch tests/Evaluation/PB2_mean.txt
sudo chmod 777 tests/Evaluation/PB2_mean.txt
echo -e "Geração\tÓtimo\tMédia dos Fitnesses\tDesvio Padrão" >> tests/Evaluation/PB2_mean.txt
python3 main.py instances/PB2.txt tests/Evaluation/PB2_mean.txt 50 85 0.5 0.5

sudo rm tests/Evaluation/PB4_mean.txt
touch tests/Evaluation/PB4_mean.txt
sudo chmod 777 tests/Evaluation/PB4_mean.txt
echo -e "Geração\tÓtimo\tMédia dos Fitnesses\tDesvio Padrão" >> tests/Evaluation/PB4_mean.txt
python3 main.py instances/PB4.txt tests/Evaluation/PB4_mean.txt 85 50 0.5 0.5

sudo rm tests/Evaluation/PB5_mean.txt
touch tests/Evaluation/PB5_mean.txt
sudo chmod 777 tests/Evaluation/PB5_mean.txt
echo -e "Geração\tÓtimo\tMédia dos Fitnesses\tDesvio Padrão" >> tests/Evaluation/PB5_mean.txt
python3 main.py instances/PB5.txt tests/Evaluation/PB5_mean.txt 85 50 0.5 0.5

sudo rm tests/Evaluation/PB6_mean.txt
touch tests/Evaluation/PB6_mean.txt
sudo chmod 777 tests/Evaluation/PB6_mean.txt
echo -e "Geração\tÓtimo\tMédia dos Fitnesses\tDesvio Padrão" >> tests/Evaluation/PB6_mean.txt
python3 main.py instances/PB6.txt tests/Evaluation/PB6_mean.txt 100 85 0.5 0.5

sudo rm tests/Evaluation/PB7_mean.txt
touch tests/Evaluation/PB7_mean.txt
sudo chmod 777 tests/Evaluation/PB7_mean.txt
echo -e "Geração\tÓtimo\tMédia dos Fitnesses\tDesvio Padrão" >> tests/Evaluation/PB7_mean.txt
python3 main.py instances/PB7.txt tests/Evaluation/PB7_mean.txt 100 50 0.5 0.5