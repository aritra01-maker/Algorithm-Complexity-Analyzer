#include <bits/stdc++.h>
#include "timer.hpp"
using namespace std;

void merge_sort_util(vector<int>& a, int l, int r)
{
    if(l >= r) return;
    int m = (l + r) / 2;
    merge_sort_util(a, l, m);
    merge_sort_util(a, m+1, r);
    inplace_merge(a.begin()+l, a.begin()+m+1, a.begin()+r+1);
}

void merge_sort(int n)
{
    vector<int> a(n);
    for(int i = 0; i < n; i++)
        a[i] = rand();

    merge_sort_util(a, 0, n-1);
}

int main()
{
    ofstream file("../data/timings.csv", ios::app);

    for(int k = 10; k <= 18; k++)
    {
        int n = 1 << k;
        double total = 0;

        for(int i = 0; i < 5; i++)
            total += measure_time(merge_sort, n);

        file << "merge," << n << "," << total/5 << "\n";
        cout << "Merge n=" << n << " done\n";
    }
}
