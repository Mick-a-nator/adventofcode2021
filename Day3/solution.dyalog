⍝ Some segments of a solution, but not complete
data ← ⊃⎕nget'~/workspace/adventofcode-2021/Day3/input_day3.txt'1
toNum ← 48-⍨⎕ucs
gamma ← {(2÷⍨≢⍵)>⊃+/toNum¨⍵}
