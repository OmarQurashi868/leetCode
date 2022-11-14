/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
function uncommonFromSentences(s1, s2) {
  const words1 = s1.split(" ");
  const words2 = s2.split(" ");
  let count = {};
  let out = [];
  for (const word of words1) {
    count[word] = count[word] ? count[word] + 1 : 1;
  }
  for (const word of words2) {
    count[word] = count[word] ? count[word] + 1 : 1;
  }
  for (let word in count) {
    if (count[word] == 1) {
      out.push(word);
    }
  }
  return out;
}
