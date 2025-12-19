#include <bits/stdc++.h>
#include "timer.hpp"
using namespace std;

void bubble_sort(int n)
{//O(n^2)time complexity
    vector<int> a(n);
    for(int i = 0; i < n; i++)
        a[i] = rand();

    for(int i = 0; i < n; i++)
        for(int j = 0; j < n - i - 1; j++)
            if(a[j] > a[j+1])
                swap(a[j], a[j+1]);
}

int main()
{
    ofstream file("../data/timings.csv", ios::app);

    for(int k = 10; k <= 16; k++)
    {
        int n = 1 << k;
        double total = 0;

        for(int i = 0; i < 5; i++)
            total += measure_time(bubble_sort, n);

        file << "bubble," << n << "," << total/5 << "\n";
        cout << "Bubble n=" << n << " done\n";
    }
}
/*
Research reasoning

->n = 2^k → geometric growth

->Run 5 times → noise reduction

->Average runtime recorded
*/