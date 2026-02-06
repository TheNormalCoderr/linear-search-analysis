#include <iostream>
#include <iomanip>
#include <vector>
#include <chrono>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <unordered_set>

using namespace std;
using namespace std::chrono;

/* Linear Search */
int linearSearch(const vector<int> &arr, int key)
{
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] == key)
            return i;
    }
    return -1;
}

int main()
{
    /* ================= USER CONTROLS ================= */

    const int START_SIZE = 1000;
    const int MAX_SIZE = 500000;
    const int STEP_SIZE = 10000;
    const int TRIALS = 3000;
    const int keyMultiplier = 2;
    srand(time(NULL));

    /* ================= OUTPUT FILE ================= */

    ofstream fout("linear_search_analysis.txt");
    fout << "ArraySize\tHit%\tMiss%\tAvgTime_us\tAvgIndexFound\n";

    /* ================= TERMINAL HEADER ================= */

    cout << left
         << setw(12) << "ArraySize"
         << setw(12) << "Duplicates"
         << setw(10) << "Hit(%)"
         << setw(10) << "Miss(%)"
         << setw(15) << "AvgTime(us)"
         << setw(15) << "AvgIndex"
         << endl;

    cout << string(74, '-') << endl;

    /* ================= MAIN ANALYSIS ================= */

    for (int size = START_SIZE; size <= MAX_SIZE; size += STEP_SIZE)
    {
        vector<int> arr(size);
        unordered_set<int> uniqueValues;

        /* Fill array with random values */
        for (int i = 0; i < size; i++)
        {
            arr[i] = rand() % size;
            uniqueValues.insert(arr[i]);
        }

        double duplicates = size - uniqueValues.size();

        int hits = 0, misses = 0;
        long long indexSum = 0;

        auto start = high_resolution_clock::now();

        for (int i = 0; i < TRIALS; i++)
        {
            int key = rand() % (keyMultiplier * size);

            int idx = linearSearch(arr, key);
            if (idx != -1)
            {
                hits++;
                indexSum += idx;
            }
            else
            {
                misses++;
            }
        }

        auto end = high_resolution_clock::now();

        double totalTimeUs =
            duration<double, micro>(end - start).count();

        double avgTimeUs = totalTimeUs / TRIALS;
        double hitPerc = (hits * 100.0) / TRIALS;
        double missPerc = (misses * 100.0) / TRIALS;

        double avgIndex =
            (hits > 0) ? (double)indexSum / hits : -1.0;

        /* ===== FILE OUTPUT (UNCHANGED) ===== */
        fout << size << "\t"
             << fixed << setprecision(2)
             << hitPerc << "\t"
             << missPerc << "\t"
             << avgTimeUs << "\t"
             << avgIndex << "\n";

        /* ===== TERMINAL OUTPUT ===== */
        cout << "\n========================================\n";
        cout << "Array Size        : " << size << endl;
        cout << "----------------------------------------\n";
        cout << fixed << setprecision(2);
        cout << "Duplicates (%)    : " << (duplicates / size) * 100 << endl;
        cout << "Hit Percentage    : " << hitPerc << endl;
        cout << "Miss Percentage   : " << missPerc << endl;
        cout << "Avg Time (us)     : " << avgTimeUs << endl;
        cout << "Avg Index Found   : " << avgIndex << endl;
        cout << "========================================\n";
    }

    fout.close();

    cout << "\nAnalysis complete." << endl;
    cout << "Output written to linear_search_analysis.txt" << endl;

    return 0;
}