#!/bin/sh

ARRAY=( "enron1" "enron2" "enron3" "enron4" "enron5" "enron6" )
BASE_URL="http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/"
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd "$SCRIPTPATH/datasets"
for ELEMENT in ${ARRAY[@]}
do
    FILE=$ELEMENT.tar.gz
    URL="$BASE_URL$FILE"
    FOLDER="$ELEMENT"
    PWD
    rm -rf $FOLDER
    mkdir $FOLDER
    echo "Downloading dataset from $URL into $FOLDER"
    curl --url $URL --output "$FOLDER/$FILE"
done
