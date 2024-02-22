#include <iostream>
#include <string>
#include <vector>

#include "common.hpp"
#include "grid.hpp"

using namespace dolomiti::interview::p1;

int
main(int argc, char **argv)
{
    Grid grid(10);
    std::cout << "Welcome to Move the robot\n"
                 "To start with, insert the robot' starting position\n";
    int x;
    int y;
    std::cout << "X: ";
    std::cin >> x;
    std::cout << "Y: ";
    std::cin >> y;

    std::string moves_str;
    std::cout << "Insert the moves the robot should perform";
    std::cin >> moves_str;

    Position initial(x, y);
    std::vector<Move> moves = GetMoves(moves_str);
    auto final_position = EstimateFinalPosition(initial, moves, grid);

    std::cout << "The robot's final position is : " << final_position.x << ", "
              << final_position.y;

    return 0;
}
