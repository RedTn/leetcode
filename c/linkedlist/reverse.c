
// REFERENCE
// struct list {
//     struct list *next;
//     struct list *prev;
// };
//
// A doubly-linked list which is NULL terminated at either end.

// Reverse a doubly-linked list, NULL terminated at either end, in place. Return the new head of the list.
struct list *reverse(struct list *head) {
    while(head->next != NULL) {
        struct list *temp = head->next;
        head->next = head->prev;
        head->prev = temp;
        head = temp;
    }
    head->next = head->prev;
    head->prev = NULL;
    return head;
}