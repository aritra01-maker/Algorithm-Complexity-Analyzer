#include <bits/stdc++.h>
#include "timer.hpp"
using namespace std;

void binary_search_algo(int n)
{//O(logn) time complexity.
    vector<int> a(n);
    for(int i = 0; i < n; i++)
        a[i] = i;

    int target = n - 1;
    binary_search(a.begin(), a.end(), target);
}

int main()
{
    ofstream file("../data/timings.csv", ios::app);

    for(int k = 10; k <= 24; k++)
    {
        int n = 1 << k;
        double total = 0;

        for(int i = 0; i < 5; i++)
            total += measure_time(binary_search_algo, n);

        file << "binary," << n << "," << total/5 << "\n";
        cout << "Binary n=" << n << " done\n";
    }
}
