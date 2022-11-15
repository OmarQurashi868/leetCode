/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
 var shuffle = function(nums, n) {
    let out = [];
    for (let i = 0; i <n; i++) {
        out.push(nums[i]);
        out.push(nums[i+n]);
    }
    return out;
};