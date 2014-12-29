#CodeZap
CodeZap (inspired from PokeZap in Pokemon) is a small utility application written with love in python v2.7.x for it to work to build a csv file database (well, actually two files, but technically one) to store the information of online judge problems I do, and the keywords I associate with them. 

Read 'How it works?' section below to have a better understanding of it.


##How to write into database?

 1.  Open your command line in the directory and run the command `python writer.py`
 2.  You write ID/Name of the Problem.
 3.  You input the keywords you want to associate with it.
 4.  Click on 'submit' or just press Enter.

##How to read from database? 

Open your command line in the directory and run the command `python reader.py`
Enter ID into the `Search by ID` field to get the results of tags associated with it.
Or
Enter any tag into the `Search by Tag` field to get the associated problem name/IDs.

##How it works? 

This way you can input problems and your favourite keywords into the database.

It builds two csv files - IDWise and TagWise. As the names suggest, IDWise links all keywords to a particular ID (ID could be the name of the problem too), and TagWise associates problems with each keyword(tag) you give.

Say, for example, you've solved two problems and you input them into the database :-

    ID : Problem 1, Keywords you associate : tough, dynamic programming, optimization
    
    ID : Problem 2, Keywords you associate : tough, object oriented programming, arrays

Then, it builds the two files as follows. 

**IDWise** file contains

    Problem 1, tough, dynamic programming, optimizations
    Problem 2, tough, object oriented programming, arrays

**TagWise** file contains

    tough, Problem 1, Problem 2
    dynamic programming, Problem 1
    object oriented programming, Problem 1
    optimizations, Problem 1
    arrays, Problem 1

Now, say in future, you come across a point of time when you're writing code for something you've already done in the past, but don't exactly remember which practice problem or question it was. You open up the Reader app(coming soon) and input the keywords and it'll show you the ID/Names of all the Problems that are related to that keyword.

You can also search a problem by its name to get all its keywords/tags that you've defined.


##Future Work

The following features could be added to the application to make it more convenient and better.

 - Reader scans if tag exists as a substring of any other tag. Also, casing should be ignored while checking.
 - Being able to edit an already filled entry through the application.
 - Making search results in Reader app behave like dynamic links, clicking on which they get inputted into the corresponding boxes and get auto-submitted. Also, this would require a back button, so as to move to previous value.
 - Changing grid system to pack and improving layout, making it more responsive.
 - Ability to have a settings window for the application through which you can browse and select the path where you want to store the two database files.


I'll remove these dependencies and issues whenever I get time.
This project's aim was basically to help 'me' in competitive programming, and also to kinda learn how GUI works in python.


##Author

Bhavul Gauri

