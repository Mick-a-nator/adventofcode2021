import System.IO
import Data.Function
import Data.Char

readIn :: IO [String]
readIn = do
    content <- readFile "input_day3.txt"
    return (lines content)

toBits :: [Char] -> [Int]
toBits = map digitToInt

transpose :: [[a]] -> [[a]]
transpose ([]:_) = []
transpose x = (map head x) : transpose (map tail x)

type Count = Int
countSumReducer :: (Count, Int) -> Int -> (Count, Int)
countSumReducer (c, s) nxt = (c + 1, s + nxt)

solve :: [String] -> IO ()
solve nums = nums 
    & (map toBits)
    & transpose 
    & (map (foldl countSumReducer (0, 0))) 
    & (map (\(c, s) -> if s > (div c 2) then 1 else 0)) 
    & (foldl (\acc x -> acc * 2 + x) 0)
    & show 
    & putStrLn

main = do
    input <- readIn
    solve input
