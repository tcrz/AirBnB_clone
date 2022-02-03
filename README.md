<h1> AirBnB_clone </h1>

The goal of the project is to deploy on your server a simple copy of the AirBnB website.

The AirBnB website operates an online marketplace for travel information and booking services. The Company offers lodging, home-stay, and tourism services via websites and mobile applications. Airbnb serves clients worldwide.

<h2>Files and Directories</h2>

* <b>models</b> directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.

* <b>tests directory</b> will contain all unit tests.

* <b>console.py</b> file is the entry point of our command interpreter.

* <b>models/base_model.py</b> file is the base class of all our models(contained in/models). It contains common elements:

* <b>attributes:</b> id, created_at and updated_at

* <b>methods:</b> save() and to_json()

* <b>models/engine</b> directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py**

<h2> File Storage Engine </h2> 
This involves:
* creating your data model(parent and subclasses)
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)

This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console(CLI) will be a tool to validate this storage engine. This CLI will be used to make operations on Classes involving creating instances, destroying them, amont many other commands. This project uses python library, `cmd` to create an interactive command line interface. Commands performed on classes and instances reflect accordingly on ```file.json```. ecample: ```create BaseModel``` will serialize an instance and save it to ```file.json```

 
 
#### How to start the CLI(Console)
```
$ ./console.py
```
#### How to use it
#### For a detailed description of all tests, run these commands in the CLI:
The help command gives info on how to use each command:

```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update


(hbnb) help create
Creates a new instance of specified, saves it amd prints its id
```

[Example] Run a command:
```
(hbnb) create Amenity
b99ef20a-4de5-4574-9178-e11aee525ff3
```
 

* Other Commands in the CLI may also be executed with this syntax(these commands work similarly to those above):
  * **count:** `<class name>.count()` --counts instances of specified class

  * **update:** `<class name>.update(<id>, <attribute name>, <attribute value>)`
 
  * **show:** `<class name>.show(<id>)`

  * **all:** `<class name>.all()`

  * **destroy:** `<class name>.destroy(<id>)`

  * **update:** `<class name>.update(<id>, <attribute name>, <attribute value>)`

