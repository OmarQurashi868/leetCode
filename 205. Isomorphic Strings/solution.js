/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var isIsomorphic = function (s, t) {
    let map1 = {};
    let map2 = {};
    let newS = [];
    let newT = [];

    let count = 0;
    for (let i = 0; i < s.length; i++) {
        if (!map1[s[i]]) {
            map1[s[i]] = count;
            count++;
        }
    }
    for (let i = 0; i < s.length; i++) {
        newS.push(map1[s[i]]);
    }

    count = 0;
    for (let i = 0; i < t.length; i++) {
        if (!map2[t[i]]) {
            map2[t[i]] = count;
            count++;
        }
    }
    for (let i = 0; i < t.length; i++) {
        newT.push(map2[t[i]]);
    }

    for (let i = 0; i < newS.length; i++) {
        if (newS[i] != newT[i]) return false;
    }
    return true;
};