"""
In order to implement the post_processor you need to follow these steps:
- Step 1 Configuration: In order to configure the post_processor you need just one document
  processed through Document AI. Open the configuration GUI calling run_GUI.py from the command
  line and set the 'path' flag: 'python run_GUI.py --path /your/path/to/DocumentAI/output'
- Step 2: open the configuration file that it's created after you pressed save in the configuration GUI
- Step 3: run the post processor on one (a) or multiple (b) documents processed through Document AI
"""

from dai_post_processor import post_processor as pp
import json
import os

# Step 2
with open("data/config.json") as json_file:
    config_dict = json.load(json_file)

# (a) Apply post-processor to single document

path = "/Users/Niolo/OneDrive - Alma Mater Studiorum Università di Bologna/Work/DocumentAI/WB/3466828248682961428/0"
doc_ai2 = pp.open_doc_ai(path)

doc2 = pp.DocumentClass(doc_ai2, config_dict)
a = doc2.create_json()

# (b) Apply post-processor to multiple documents

path = "/Users/Niolo/OneDrive - Alma Mater Studiorum Università di Bologna/Work/DocumentAI/WB"
file_list = os.listdir(path)
file_list = [file for file in file_list if not file.startswith('.')]
for file in file_list:
    try:
        doc_ai, title = pp.open_doc_ai("{}/{}/0".format(path, file), return_title=True)
        doc2 = pp.DocumentClass(doc_ai, config_dict)
        a = doc2.create_json(file_name=title)
    except Exception as e:
        print(e)

