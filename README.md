# HiCu-ICD-codes

The Original setup was however i had to make edits to my local machine 

Install the following packages to run the code in this repository:

    gensim==4.1.2
    nltk==3.5
    numpy==1.18.1
    pandas==1.0.0
    scikit_learn==1.1.1
    scipy==1.4.1
    torch==1.7.1
    tqdm==4.62.3
    transformers==4.5.1

pip install -r requirements.txt

I used these to overcome issues with dependencies being out of date 

gensim==4.1.2
nltk==3.5
numpy==1.24.4      # originally specified as 1.18.1, but 1.24.4 is compatible with gensim and works fine
pandas==1.0.0
scikit_learn==1.1.1
scipy==1.10.1       # installed with gensim
torch==1.7.1
tqdm==4.62.3
transformers==4.5.1
Note: numpy==1.18.1 was initially requested but replaced by 1.24.4 automatically during gensim installation. This is OK unless you see runtime errors — if needed, you can lock it back to 1.18.1.

Create and activate a virtual environment 

python -m venv hicu-env
hicu-env\Scripts\activate

cd into the HiCu-ICD-main

Install dependencies 

pip install -r requirements.txt

OR 

Can do them manually (optional) 

pip install numpy==1.24.4
pip install gensim==4.1.2
pip install nltk==3.5
pip install pandas==1.0.0
pip install scikit_learn==1.1.1
pip install scipy==1.10.1
pip install torch==1.7.1
pip install tqdm==4.62.3
pip install transformers==4.5.1

🔹 Python and Package Versions Used

    Python: 3.8.10

    Key Packages:

numpy==1.24.4
gensim==4.1.2
nltk==3.5
pandas==1.0.0
scikit_learn==1.1.1
scipy==1.10.1
torch==1.7.1
tqdm==4.62.3
transformers==4.5.1
