/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

 function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let out = new ListNode();
    let nodeOut = out;
    let node1 = l1;
    let node2 = l2;
    while (node1 || node2) {
        nodeOut.val += (node1?.val || 0) + (node2?.val || 0);

        node1 = node1?.next || null;
        node2 = node2?.next || null;
        if (!node1 && !node2 && nodeOut.val < 10) break;

        nodeOut.next = new ListNode();
        if (nodeOut.val >= 10) {
            nodeOut.val -= 10;
            nodeOut.next.val += 1;
        }

        nodeOut = nodeOut.next;
    }
    return out
};