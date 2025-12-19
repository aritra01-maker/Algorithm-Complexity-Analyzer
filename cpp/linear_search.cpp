#include <bits/stdc++.h>
#include "timer.hpp"
using namespace std;

void linear_search(int n)
{
    vector<int> a(n);
    for(int i = 0; i < n; i++)
        a[i] = i;

    int target = n - 1;
    for(int i = 0; i < n; i++)
        if(a[i] == target) break;
}

int main()
{
    ofstream file("../data/timings.csv", ios::app);

    for(int k = 10; k <= 20; k++)
    {
        int n = 1 << k;
        double total = 0;

        for(int i = 0; i < 5; i++)
            total += measure_time(linear_search, n);

        file << "linear," << n << "," << total/5 << "\n";
        cout << "Linear n=" << n << " done\n";
    }
}
