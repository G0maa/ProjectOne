# ProjectOne

This is my first ever project.
It fouces on helping students make their academic schedules.

That way you can have your schecule ready before the official registration
of your institution starts, which will (hopefully) save you some time,
and make you register the subjects you want without them getting full.

## How to run it?

Easily clone (or download) it and compile it using any c++ ?compiler?,
then run the program, after finsihing choosing your lectures,
you should run the python script which will add it to the .xlsx spreadsheet.
BUT you should install openpyxl module first.

```bash
pip install openpyxl
```
The program is now finished, there are few suggested updates
but the current version is fully funcationing.

## I got it to run, now what?

Input is a bit tricky:

Subject_name Subject_code Subject_units
Subject_day subject_periods Subject_group
```
MngPrnc BSC213 1
5 7-8 1
4 7-8 2
5 7-8 3
4 7-8 4
0
```
if there's 2 lecture in the same group you will have to add them after each other:
```
DS INF210 3
1 1-2 1
4 4-6 1
2 1-2 2
4 1-3 2
0
```

You can't "connect" more than 2 lectures together.
Rest of the program should (hopefully) be easy to use.

Mistaken input in many functions isn't monitored.

## Pros/Cons:

+ Obviously you can input lecture to register them.
+ You can have up to 2 lectures in the same group (Lecture + Section).
+ Collision will be dealt by the program and you will know that there's a collision.
+ You can review/delete the subjects you have registered.
+ The output will be shown in a speradsheet.
+ Personally I consider it a bit versatile as it can be used in many other institutions (hopefully).

- Input too long, might take up to 20 mins, but is used by everyone so only one person will have to write it.
- You can't change input after entering it in the program.
- I consider it hard to use/unclear.
- No use of DS or OOP. 
- Personally the code isn't well designed, bad flow.
- No monitoring for mistaken.
- You can only "connect" two lectures together.

It does its job, but will take sometime for you to write the input, and to get used to the command line interface.

## Useless stuff:

I'd say this is an easy project for first year CS students,
and can be improved in many ways:

+ C++ makes it 10x harder.
+ A better way to input:
    Think of either reading from your institution .xlsx tables,
    I ((think)) your institution should have a formatted input similar
    to what I have here in their regeisteration system, so try to ask for it.
+ A better way to store input.
+ Magic() function to create every possible table, which is actually better
than letting user choose every subject, unless threres 100+ tables or so.

 I think it took me about 30 horus to program it? give or take 5.
 You can probably make similar program if you take CS50x and do a bit of Problem solving.
