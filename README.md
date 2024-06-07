# Conway's Game of Life

## Description
Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. The game is a zero-player game, meaning that its evolution is determined by its **initial state**, requiring no further input. My project implements this game using Python.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Structure](#structure)
3. [Testing](#testing)
4. [Contributing](#contributing)
5. [Contact Information](#contact-information)

## Installation
To run this project, you'll need Python (my version is **3.9.13**) installed on your machine. You can download Python from [here](https://www.python.org/).

Also you need to have the following Python modules:

| Module | Version |
|:-------|:-------:|
|`numpy`| **1.21.5**|
|`pygame`| **2.5.2**|

## Usage
To run the Conway's Game of Life, open the `main.py` file and execute in the editor of your preference or in the console with the following commands:

```bash
cd your_directory
python main.py
```

## Structure
The project structure is:

| Name | Type | Purpose |
|:-----|:-----|:--------|
| `main` | `.py` | Executable |
| **Initial_states** | **Directory** | Contains `.py` files with the different initial states |
| **Testings** | **Directory** | Contains `.ipynb` files with the function testings |

Then you need to choose one of the *initial states* that are predefined.

## Testing
There are two testing files (included in the Testing directory):
1. `Creating_functions.ipynb`: to explore the logic functions.
2. `Creating_drawings.ipynb`: to explore how to draw the cells and grid in Pygame.

## Contact Information
For any questions or feedback, please reach out to edgarruiztovar@gmail.com.