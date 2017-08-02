# Directory to download the pretrained models to.
PRETRAINED_MODELS_DIR="/Users/az/Desktop/projects/modemo/tf/skip_thoughts/pretrained/"

mkdir -p ${PRETRAINED_MODELS_DIR}
cd ${PRETRAINED_MODELS_DIR}

# Download and extract the unidirectional model.
wget "http://download.tensorflow.org/models/skip_thoughts_uni_2017_02_02.tar.gz"
tar -xvf skip_thoughts_uni_2017_02_02.tar.gz
rm skip_thoughts_uni_2017_02_02.tar.gz

# Download and extract the bidirectional model.
wget "http://download.tensorflow.org/models/skip_thoughts_bi_2017_02_16.tar.gz"
tar -xvf skip_thoughts_bi_2017_02_16.tar.gz
rm skip_thoughts_bi_2017_02_16.tar.gz