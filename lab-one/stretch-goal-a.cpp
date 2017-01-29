// Jon
// stretch goal part a

#include <string.h>
#include <iostream>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctime>

using namespace std;

int main() {

  // Get the hostname using gethostname()
  char hostName[128];
  int hostNameLength = 128;
  gethostname(hostName, hostNameLength);

  int maximumValue;

  // Set the maximum value according to which platform the program is running on
  if (strcmp(hostName, "hopper.cluster.earlham.edu") == 0) {
    maximumValue = 45000;
  } else if (strcmp(hostName, "eccs-home") == 0) {
    maximumValue = 55000;
  } else if (strcmp(hostName, "snyder") == 0) {
    maximumValue = 50000;
  } else maximumValue = 1000;

  // Initialize array
  char Array[maximumValue][maximumValue];

  // Column major traversal
  clock_t colStart = clock();         // Initialize timer for Column Major Traversal
  for(int j = 0; j < maximumValue; j++) {
    for(int i = 0; i < maximumValue; i++) {
      Array[i][j] = 'C';
      // cout << Array[i][j];
    }
  }
  // Find run time for column major traversal
  double colTime = static_cast<double>(clock() - colStart) / CLOCKS_PER_SEC;

  // Row major traversal
  clock_t rowStart = clock();         // Initialize timer for Row Major Traversal
  for(int i = 0; i < maximumValue; i++) {
    for(int j = 0; j < maximumValue; j++) {
      Array[i][j] = 'R';
      // cout << Array[i][j];
    }
  }
  // Find run time for row major traversal
  double rowTime = static_cast<double>(clock() - rowStart) / CLOCKS_PER_SEC;

  cout << "The maximum value is: " << maximumValue;
  cout << "Row Major traversal takes: " << rowTime;
  cout << "\nColumn Major traversal takes: " << colTime << endl;

  return 0;

}
