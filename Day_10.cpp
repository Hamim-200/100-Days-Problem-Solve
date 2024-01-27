// class Solution {
// public:
//     ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
//         ListNode* returnNode = new ListNode(INT_MIN);
//         ListNode* headNode = returnNode;

//         while (l1 != NULL && l2!=NULL){
//             if(l1->val <= l2->val){
//                 returnNode->next = l1;
//                 l1 = l1->next;
//             }
//             else{
//                 returnNode->next = l2;
//                 l2 = l2->next;
//             }
//             returnNode = returnNode->next;
//         }

//         if(l1==NULL){
//             returnNode->next = l2;
//         }
//         else if(l2==NULL){
//             returnNode->next = l1;
//         }
//         return headNode->next;
//     }
// };