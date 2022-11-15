/**
 * @param {number[]} nums
 * @return {number}
 */
 var pivotIndex = function (nums) {
    for (let i = 0; i < nums.length; i++) {
        if (checkPivotIndex(nums, i)) {
            return i;
        }
    }
    return -1;
};

const checkPivotIndex = (nums, limit) => {
    let leftSum = 0;
    let rightSum = 0;
    for (let i = 0; i < limit; i++) {
        if (i != limit) leftSum += nums[i]
    }
    for (let i = limit; i < nums.length; i++) {
        if (i != limit) rightSum += nums[i]

    }
    return leftSum == rightSum;
}