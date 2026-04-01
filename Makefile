.PHONY: install data dashboard clean

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

data:
	python src/data_generator.py
	python src/data_preprocessing.py

dashboard:
	streamlit run dashboard/app.py

clean:
	rm -rf __pycache__ src/__pycache__ dashboard/__pycache__
	rm -rf venv/
	rm -rf data/*.csv
	rm -rf notebooks/*.ipynb
