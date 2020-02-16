"""
Write a function that takes in a non-empty list of distinct integers and an integer representing a target sum
as arguments.

If any two numbers in the input array sum up to the target sum,
the function should return them as list.

If no two numbers adds to target sum, the function should return Empty List..
If there are more than two numbers, return any two numbers pair.

For example:
[1, 22, 4, 5, 7] 6 => [1, 5]
x + y = 6
y = 6 - x
"""


def two_number_sum(nums, target_sum):
    hashtable = {}
    for num in nums:
        match = target_sum - num
        if match in hashtable:
            return [match, num]
        else:
            hashtable[num] = True

    return []


def main():
    print(two_number_sum([1, 22, 4, 5, 7], 6))


if __name__ == '__main__':
    main()
