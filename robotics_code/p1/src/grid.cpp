#include "grid.hpp"

namespace dolomiti::interview::p1 {

Grid::Grid(int size) : cells_(size, std::vector<Cell>(size, 0)) {
}
void
Grid::Set(int value, const Position& pos)
{
    cells_[pos.x][pos.y] = value;
}

int
Grid::GetValue(const Position& pos)
{
    return cells_[pos.x][pos.y].value;
}

} // namespace dolomiti::interview::a1

