# Upgrade pip
pip install -U pip

# Install libraries
pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

# Set CUDA environments
export CUDA_VER=11.4
export PATH=/usr/local/cuda-$CUDA_VER/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-$CUDA_VER/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export CUDA_HOME=/usr/local/cuda-$CUDA_VER
echo "**********"
echo "Setup CUDA_VER $CUDA_VER completed"
echo "**********"

