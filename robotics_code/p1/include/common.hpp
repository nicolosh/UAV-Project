#ifndef INTERVIEW_COMMON_HPP
#define INTERVIEW_COMMON_HPP

#include <string>
#include <vector>

namespace dolomiti::interview::p1 {

class Grid;

enum class Move : char
{
    RIGHT = 'R',
    LEFT = 'L',
    UP = 'U',
    DOWN = 'D'
};

struct Position
{
    Position(int x, int y) : x(x), y(y) {};
    int x{ 0 };
    int y{ 0 };
};

Position EstimateFinalPosition(const Position &, const std::vector<Move> &, const Grid&);
bool DoPathsCollide(const Position &, const Position &,
                    const std::vector<Move> &, const std::vector<Move> &, const Grid&);
bool CanReachDestination(const Position &, const std::vector<Move> &, const Grid&);

std::vector<Move> GetMoves(const std::string&);

}  // namespace dolomiti::interview::a1

#endif  // INTERVIEW_COMMON_HPP
