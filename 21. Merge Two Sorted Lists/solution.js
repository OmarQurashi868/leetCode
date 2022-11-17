/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
 var mergeTwoLists = function (list1, list2) {
    if (!list1 && !list2) {
        return list1;
    }
    let out = new ListNode();
    let curOut = out;
    let cur1 = list1;
    let cur2 = list2;
    while (cur1 || cur2) {
        if (!cur1 && !cur2) break;
        if (cur1 && cur2) {
            if (cur1?.val <= cur2?.val) {
                curOut.val = cur1.val;
                cur1 = cur1.next;
            } else {
                curOut.val = cur2.val;
                cur2 = cur2.next;
            }
        } else if (cur1) {
            curOut.val = cur1.val;
            cur1 = cur1.next;
        } else if (cur2) {
            curOut.val = cur2.val;
            cur2 = cur2.next;
        }
        if (cur1 || cur2) {
            curOut.next = new ListNode();
            curOut = curOut.next;
        }
    }
    return out;
};