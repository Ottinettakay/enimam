def skip_numbers_greater_than_target(numbers, target):
    result = []
    for num in numbers:
        if num <= target:
            result.append(num)
    return result
