class Solution:

    def generateParenthesis(self, n: int) -> list[str]:
        def generate(p, left, right):
            if right == 0:
                return [p]
            return (generate(p + '(', left - 1, right) if left > 0 else []) + (
                generate(p + ')', left, right - 1) if right > left else []
            )

        return generate('', n, n)