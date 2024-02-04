1. Interpolation search is more efficient on uniformly distributed data. Interpolation search
    also takes into account the values of each element to adapt to any sorted values instead of always
    using the midway point to decide where to search next.

2. Interpolation search may perform less efficiently when the data is not uniformly distributed
    as interpolation search relies on the fact that the difference between a value and the next value
    stays relatively constant. If the difference between values is not constant through out the data set,
    then the calculated position may deviate from the actual desired position leading to a longer search time.

3. The part of the code affected would be the pos variable. 

4. If the data is unsorted, then interpolation and binary search will not work properly
    but linear search will.

5. If the dataset is small and if the key that we are looking for is near the start of the dataset, then
    linear search will outperform both interpolation and binary search. 

6. Create base cases for the first few data values before starting the normal process of binary or interpolation
   search. If the data is given unsorted, then consider finding a way to sort the data set first before searching.



