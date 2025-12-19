#ifndef TIMER_HPP
#define TIMER_HPP

#include <chrono>

inline double measure_time(void (*func)(int), int n) {
    auto start = std::chrono::high_resolution_clock::now();
    func(n);
    auto end = std::chrono::high_resolution_clock::now();
    return std::chrono::duration<double, std::micro>(end - start).count();
}

#endif
