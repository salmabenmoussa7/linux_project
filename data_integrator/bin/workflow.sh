#!/bin/bash

FILE=../../raw_data.csv
dt=$(date +%Y-%m-%d-%H-%M-%S)

if test -f "$FILE"; then
  echo "$FILE exists. Launching integration"
  bash run.sh
  echo "Data integration succeeded"
  # Vérifie si le répertoire d'archive existe, sinon le créer
  if [ ! -d "../../archived/raw" ]; then
    mkdir -p ../../archived/raw
  fi
  mv $FILE ../../archived/raw/raw_data_$dt.csv
else
  echo "No raw file detected"
fi
