# https://stackoverflow.com/questions/51049663/python3-6-error-modulenotfounderror-no-module-named-src

export PYTHONPATH="$PYTHONPATH:$PWD"

nodemon --exec python src/main.py
