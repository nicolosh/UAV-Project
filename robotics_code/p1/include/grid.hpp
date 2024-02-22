#pragma once
#ifndef INTERVIEW_GRID_HPP
#define INTERVIEW_GRID_HPP

#include "common.hpp"

namespace dolomiti::interview::p1 {

class Grid
{
public:
    explicit Grid(int size);

    void Set(int value, const Position& pos);
    int GetValue(const Position& pos);

private:
    struct Cell
    {
        Cell(int v) : value(v){};
        Cell() : value(0){};

        int value;
    };

    std::vector<std::vector<Cell>> cells_;
};

}  // namespace dolomiti::interview::a1

#endif  // INTERVIEW_GRID_HPP
