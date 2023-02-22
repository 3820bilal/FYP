
# Digital Hardware Generator and Integrator

The aim of this project is to create a framework that can be used to generate and intergrate RTL components. User should be able to connect components from a library of generic RTL components and existing IP blocks to create Digital Hardware.

Here is brief discription of files that how to proceed them

## [create.py](https://github.com/3820bilal/FYP/blob/main/create.py)

This file will create project when run without any argument with the name of 
**Baseboard.sv** (default).

If you are using VS code you can only run file using run button simply or 


To run this project in terminal

```bash
  python .\create.py
```

If you are using ubuntu terminal use
```bash
python3 create.py
```
you can give file the name of your own choice by

```bash
python .\create.py -f filename
```
the above project will add only two inputs **clk** and **reset** in created file.
If you want to add more inputs and outputs in the file use following commands

```bash
python .\create.py -f filename -i enable -o clear -ir None -or [3:0]
```

None is range for input **enable** and **[3:0]** is range for output **clear**
**Note:** If you are using ubuntu terminal then use **./plug.py** and then pass argument

## [plug.py](https://github.com/3820bilal/FYP/blob/main/plug.py)

This file will create the instance of file that is given in argument. (**the file should be available in library**).

To run this file use following commands

argument after **-i** is for instance name 

argument after **-f** is for file name
```bash
python .\plug.py -i instance_name -f filename 
```
**Note:** If you are using ubuntu terminal then use **./plug.py** and then pass argument

## [connect.py](https://github.com/3820bilal/FYP/blob/main/connect.py)

This file will connect the ports of one instance with the ports of another instance.

To run this file use following commands

argument after **-i** is for input instance

argument after **-o** is for output instance 

argument after **-ip** is for ports of input instance

argument after **-op** is for ports of output instance 
```bash
python .\connect.py -i input instance_name -o output instance name -ip input port -op output port
```
you can give **list** of input ports and output ports to connect.

**Note:** If you are using ubuntu terminal then use **./connect.py** and then pass argument
## [adddata.py](https://github.com/3820bilal/FYP/blob/main/adddata.py)

You can add new inputs and outputs using this file.

To add new inputs and outputs use commands that are already used in create.py and pass the name of file in which you want to add ports

```bash
python .\adddata.py -d port name_of_port -f filename 
```
**Note:** If you are using ubuntu terminal then use **./adddata.py** and then pass argument

## [delete.py](https://github.com/3820bilal/FYP/blob/main/delete.py)

This file can delete instance and ports from file. 

To run this file use following commands

To delete ports, you have to use 

argument after **-d** should be port to delete port and  instance to delete instance and then name of port or instance that needs to be deleted 

argument after **-f** is for file name
```bash
python .\delete.py -d port name_of_port -f filename 
```
**Note:** If you are using ubuntu terminal then use **./delete.py** and then pass argument
