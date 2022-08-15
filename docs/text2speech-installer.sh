#! /bin/bash

echo '--- A PARTIÇÃO DO CARTÃO SD COMO EXTENSÃO DO FYLE SYSTEM ESTA EM MONTADA EM /media/sdcard? ---' 
echo -n '[y/n]:'
read option1

echo '--- A PARTIÇÃO DO CARTÃO SD CONFIGURADA COMO ÁREA DE TROCA (SWAP) ESTÁ ATIVADA? ---'
echo -n '[y/n]:'
read option2

echo "$option1"
echo "$option2"

if [ "${option1,}" = "n" ] && [ "${option2,}" = "n" ]
then
    echo '--- POR FAVOR, MONTE A PARTIÇÃO DO CARTÃO SD EM /media/sdcard, ATIVE A ÁREA DE TROCA (SWAP), E EXECUTE O SCRIPT NOVAMENTE ---' 
elif [ "${option1,}" = "n" ]
then
    echo '--- POR FAVOR, MONTE A PARTIÇÃO DO CARTÃO SD EM /media/sdcard E EXECUTE O SCRIPT NOVAMENTE ---'
elif [ "${option2,}" = "n" ]
then
    echo '--- POR FAVOR, ATIVE A ÁREA DE TROCA (SWAP) E EXECUTE O SCRIPT NOVAMENTE ---'
elif [ "${option1,}" = "y" ] && [ "${option2,}" = "y" ] 
then
    #echo 'Defina o python'
    echo '--- AS INSTALAÇÕES NECESSÁRIAS SERÃO EXECUTADAS ---'
    
    echo '--- ATUALIZANDO/INSTALANDO OS PACOTES/PROGRAMAS DISPONÍVEIS ---'
    sudo iwconfig wlan0 power off
    sudo apt-get update
    
    echo '--- ATUALIZANDO O SISTEMA ---'
    sudo apt-mark hold linux-image-4.14.0-qcomlt-arm64
    sudo apt-get dist-upgrade
    
    echo '--- INSTALANDO BIBLIOTECAS NECESSARIAS PARA INSTALAR O OPENCV ---'
    sudo apt-get install build-essential cmake pkg-config -y
    sudo apt-get install libjpeg-dev libtiff5-dev libpng-dev -y
    sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
    sudo apt-get install libxvidcore-dev libx264-dev -y
    sudo apt-get install libgtk2.0-dev libgtk-3-dev -y
    sudo apt-get install libatlas-base-dev gfortran -y
    sudo apt-get install hdf5* libhdf5* -y
    sudo apt-get install v4l-utils -y 
    sudo apt-get install python3-pip -y

    echo '--- INSTALANDO NUMPY PARA O PYTHON3 ---'
    sudo python3 -m pip install numpy
    
    echo '--- INSTALANDO O OPENCV ---'
    sudo apt-get install python3-opencv -y
    
    echo '--- OPENCV INSTALADO ---'

    echo '--- INSTALANDO O TEXT2SPEECH ---'

    echo '--- INSTALANDO BIBLIOTECAS E FRAMEWORKS NECESSÁRIAS ---'

    sudo apt-get install tesseract-ocr libtesseract-dev espeak -y
    sudo apt-get install mpg321 -y
    sudo python3 -m pip install pytesseract
    sudo python3 -m pip install Pillow numpy scipy gTTS pyttsx3
    sudo git clone https://github.com/BoseCorp/py-googletrans.git
    cd ./py-googletrans
    sudo python3 setup.py install
    docs/install_traineddata_tesseract.sh

    echo '--- TEXT2SPEECH INSTALADO ---'
fi