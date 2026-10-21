class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solutions = {}
        for s in strs:
            chars = ''.join(sorted(list(s)))
            if chars not in solutions.keys():
                solutions[chars] = []
            solutions[chars].append(s)
        return [solutions[k] for k in solutions.keys()]
