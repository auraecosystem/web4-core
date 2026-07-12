# Terminal 1: Start the demo store
cd demo/store
pip install -r requirements.txt
python app.py
# Visit: http://localhost:8000

# Terminal 2: Start the delegation UI
cd demo/delegation-ui
pip install -r requirements.txt
python app.py
# Visit: http://localhost:8000
# To view the text narrative files created by the script:
cat public/narratives/adversarial_summary.json
# or check the local markdown files
cat docs/NARRATIVE_SYSTEM.md
