# For Development Mode 
export FLASK_ENV=development 

# To install dependencies
pip install -r requirements.txt

# How to make virtual env
python3 -m virtualenv 'give name'

# How to activate env
source 'env name'/bin/activate

# How to deactivate env
deactivate

# For creating requirement.txt file
pip freeze > requirements.txt