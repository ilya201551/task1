# Task1

**loader.py:**
  - loads the required json file and returns the dictionary.

**merger.py:**
  - returns a combined dictionary .
  
**sever.py:**
  - the **save()** method of Saver class checks the format and calls the save method of one of the classes(JsonSaver/XmlSaver) to return the result in the desired format.

**main.py:**
  - parses the arguments and calls **save()** method of Saver class.
