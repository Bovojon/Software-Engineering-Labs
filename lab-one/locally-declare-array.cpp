// Jon
// jon-lab1
// locally declare array

#include <iostream>
#include <ctime>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main() {

  // Initialize a new empty 2-dimensional array of characters
  char Array[3000][3000] = {""};

  // Column major traversal
  clock_t colStart = clock();         // Initialize timer for Column Major Traversal
  for(int j = 0; j < 3000; j++) {
    for(int i = 0; i < 3000; i++) {
      Array[i][j] = 'C';
      // cout << Array[i][j];
    }
  }
  // Find run time for column major traversal
  double colTime = static_cast<double>(clock() - colStart) / CLOCKS_PER_SEC;

  // Row major traversal
  clock_t rowStart = clock();         // Initialize timer for Row Major Traversal
  for(int i = 0; i < 3000; i++) {
    for(int j = 0; j < 3000; j++) {
      Array[i][j] = 'R';
      // cout << Array[i][j];
    }
  }
  // Find run time for row major traversal
  double rowTime = static_cast<double>(clock() - rowStart) / CLOCKS_PER_SEC;

  cout << "Row Major traversal takes: " << rowTime;
  cout << "\nColumn Major traversal takes: " << colTime << endl;

  return 0;
}
