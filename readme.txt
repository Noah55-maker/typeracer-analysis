run the following lines to complete setup:
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt


to re-enter the virtual environment:
source .venv/bin/activate


to run the program:
python3 fetch.py # fetches, parses, and writes data from typeracerdata.com
python3 graph.py # graphs data from previous step
