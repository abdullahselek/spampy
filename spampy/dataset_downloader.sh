#!/bin/bash

ARRAY=("enron1" "enron2" "enron3" "enron4" "enron5" "enron6")
BASE_URL="http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/"
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd "$SCRIPTPATH/datasets"
rm -rf enron
mkdir enron
cd enron
for ELEMENT in ${ARRAY[@]}
do
    FILE=$ELEMENT.tar.gz
    URL="$BASE_URL$FILE"
    FOLDER="$ELEMENT"
    echo "Downloading dataset from $URL into $FOLDER"
    curl -L -o "$FILE" $URL
    tar zxf "$FILE"
    rm -rf "$FILE"
    rm "$FOLDER/Summary.txt"
done
