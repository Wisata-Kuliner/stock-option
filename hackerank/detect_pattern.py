def detect_pattern(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    for idx, (let_1, let_2) in enumerate(zip(s1, s2)):
        for let_1_inner, let_2_inner in zip(s1[idx:], s2[idx:]):
            if (let_1_inner == let_1) != (let_2_inner == let_2):
                return False
    return True

if __name__ == "__main__":
    print(detect_pattern("bcd", "abd"))