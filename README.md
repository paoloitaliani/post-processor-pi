**post-processor-pi** is a Python module that exploits the output of Document AI (tool available 
on GCP) to create a JSON file that stores the text contained in a document in an organized way, so 
that it reflects its original structure. To work with different types of 
documents having different structures, post-processor-pi has to be configured using the GUI
that I developed.

Installation
------------

The easiest way to install post-processor-pi is using pip:

    pip install post-processor-pi

Documentation
------------

As I mentioned above in order to implement the post-processor we need to configure it first and this
can be done using the Configuration GUI that I developed. 

### Configuration GUI 

In order to start the Configuration GUI we need an example corresponding to the output of Document
AI for one document. Below you can find the code example that enables you to start the Configuration
GUI.

```python
from dai_post_processor import post_processor as pp

# Open one example from Document AI output
path = "your/path/to/DocumentAI/example"
doc_ai = pp.open_doc_ai(path)

# Start Configuration GUI
mywin = pp.configGUI(doc_ai)
mywin.start()
```

After running the above instructions the GUI should open.

#### Configuration GUI Tuning

The Configuration GUI consists of two windows:

1) **Main**: here you can find the essential instructions that are needed to
 configure post-processor-pi.
    - **Select text of interest**: in this section you can select the portion
    of the pages in the documents you're interested in. In the **Page number** 
    field you can provide the page number of the Document example you want to open.
    I you press the **Draw Box** button a new window will open, and here you can
    select the portion of the page drawing a rectangle. All the text outside this
    rectangle will be ignored for all pages and documents. Below you have a demo.
    
    
    