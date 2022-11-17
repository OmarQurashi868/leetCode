/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
 var reverseList = function (head) {
    if (!head) return head;
    let cur = head;
    let out = new ListNode(cur.val, null);
    cur = cur.next;
    while (cur) {
        out = new ListNode(cur.val, out);
        cur = cur.next;
    }
    return out;
};