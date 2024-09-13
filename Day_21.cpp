// class Solution {
// public:
//     int maxArea(vector<int>& height) {
//         int left = 0;
//         int right = height.size() - 1;

//         int curr = 0;
//         int result = 0;

//         while (left < right) {
//             curr = (right - left) * min(height[left], height[right]);
//             result = max(result, curr);

//             if (height[left] <= height[right]) {
//                 left++;
//             } else {
//                 right--;
//             }
//         }
//         return result;
        
//     }
// };