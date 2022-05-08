from typing import List


def insertion_sort(target_list: List, reverse: bool = False) -> List:
    length = len(target_list)

    def should_switch(current_value, new_value):
        if reverse:
            return current_value > new_value
        return new_value > current_value

    for head in range(1, length):
        current_value = target_list[head]
        new_head = head - 1
        while new_head >= 0 and should_switch(current_value, target_list[new_head]):
            # Shift over
            target_list[new_head + 1] = target_list[new_head]
            new_head -= 1
        target_list[new_head + 1] = current_value
    return target_list
