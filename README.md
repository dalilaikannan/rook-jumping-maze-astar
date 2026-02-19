# Rook Jumping Maze Solver (A* Search) ♖

An implementation of the A* search algorithm to solve the Rook Jumping Maze (RJM) problem, with a planned GUI for interactive visualization.
This project demonstrates heuristic search and efficient pathfinding using priority queues.

🧠 **Problem Description**

The Rook Jumping Maze is an n × n grid where:

  - Each cell contains a number k
  - From that cell, you must move exactly k spaces

Movement is restricted to:
  - Up
  - Down
  - Left
  - Right

🚀 **Algorithm**

This solver uses A* search : f(n)=g(n)+h(n)

Where:
  - g(n) = number of jumps taken so far (aka the total cost, each jump constitutes a cost of 1)
  - h(n) = Manhattan distance heuristic
  - f(n) = estimated total cost


🧩 **Features**
  - A* search implementation
  - Manhattan distance heuristic
  - Priority queue optimization
  - Edge case handling (start = goal)
  - GUI visualization (in progress)


**To Run**
    - python rjm_solver.py
