#include <iostream>
#include <set>

int main()
{
    std::set<double>powers;
    for (auto a = 2; a <= 100; ++a) 
        for (auto b = 2; b <= 100; ++b)
            value.insert(std::pow(a, b));

    std::cout << "Solution: " << value.size();
    return 0;
}
