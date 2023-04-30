# Install
* `conda create --name <env> --file requirements.txt`
* Create `openai-api-key.txt` with your openai key
* Create `wanikani-api-key.txt` with your wanikani api token
* Make a google cloud account, make a project, activate text to speech, do some cli stuff to activate it. It was complicated...

# Run
* Wanikani api test: `python3 wani-test.py`
* Program that asks user to input some vocab then creates some sentences using them: `python3 integrated_test.py`