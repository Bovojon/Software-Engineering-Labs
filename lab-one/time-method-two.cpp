// Jon
// jon-lab1
// timing method 2
#include <iostream>
#include <ctime>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

// Initialize a new empty 2-dimensional array of characters
char Array[1000][1000] = {""};

int main() {

  // Column major traversal
  double finalColtime;
  for(int j = 0; j < 1000; j++) {
    for(int i = 0; i < 1000; i++) {
      clock_t colStart = clock();         // Initialize timer for Column Major Traversal
      Array[i][j] = 'C';
      // Find run time for column major traversal
      double colTime = static_cast<double>(clock() - colStart) / CLOCKS_PER_SEC;
      finalColtime += colTime;
      // cout << Array[i][j];
    }
  }

  // Row major traversal
  double finalRowtime;
  for(int i = 0; i < 1000; i++) {
    for(int j = 0; j < 1000; j++) {
      clock_t rowStart = clock();         // Initialize timer for Row Major Traversal
      Array[i][j] = 'R';
      // Find run time for row major traversal
      double rowTime = static_cast<double>(clock() - rowStart) / CLOCKS_PER_SEC;
      finalRowtime += rowTime;
      // cout << Array[i][j];
    }
  }

  cout << "Row Major traversal takes: " << finalRowtime;
  cout << "\nColumn Major traversal takes: " << finalColtime << endl;

  return 0;
}
