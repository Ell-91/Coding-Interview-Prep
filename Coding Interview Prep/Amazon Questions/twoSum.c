#include<stdio.h>
#include<stdlib.h>      //Standard header to use malloc and calloc

//take in the integer array, take in the size of the array and we need to know our integer target value
int* twoSum(int* nums, int numsSize, int target, int* returnSize); //function signature or prototype 

int main(){
  int arr[] = {2,7,11,15};
  int return_size, target = 9;
  int *p = NULL;
  free(p);

  //to get the total number of elements    sizeof(arr)/sizeof(arr[0])
  //address of the return size      &return_size
  p = twoSum(arr, sizeof(arr)/sizeof(arr[0]), target, &return_size  );
  return p;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
  int i, j;
  int *return_arr = (int*)malloc(2 * sizeof(int));   //returning two numbers int is 4 bytes (2*2)

  //If j = 0 then we would use the same number twice which we are not supposed to do, so we do j = i + 1
  //choose 1st number and the combination of the other numbers
  for(i = 0; i < numsSize; i++){
    for(j = i + 1; j < numsSize; j++){
      if(nums[i] + nums[j] == target){
        *returnSize = 2;
        return_arr[0] = i;
        return_arr[1] = j;
        return return_arr;
      }
    }
  }
  //Didn't find the target
  *returnSize = 0;
  free(return_arr);
  return NULL;
}