/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
 var findPoisonedDuration = function (timeSeries, duration) {
    let totalTime = 0;
    for (let i = 0; i < timeSeries.length; i++) {
        if (timeSeries[i + 1] - timeSeries[i] < duration) {
            totalTime += timeSeries[i + 1] - timeSeries[i];
        } else {
            totalTime += duration;
        }
    }
    return totalTime;
};