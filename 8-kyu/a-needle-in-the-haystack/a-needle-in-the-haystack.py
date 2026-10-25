def find_needle(haystack):
    for n in range(len(haystack)):
        if haystack[n] == "needle":
            return (f"found the needle at position {n}")
    # your code here