import System.IO
import System.IO.Error
import Data.Function

readIn :: IO [String]
readIn = do
    content <- readFile "input_day1.txt"
    return (lines content)

toInt :: String -> Int
toInt str = read str :: Int

chunk :: Int -> [a] -> [[a]]
chunk n xs =  
    if   length chunk' < n then []
    else (chunk' : chunk n (tail xs))
        where chunk' = take n xs

increase :: [Int] -> Bool
increase [a, b] = b > a
increase _ = False

solve :: [String] -> IO ()
solve nums = nums 
    & (map toInt) 
    & (chunk 2)
    & (map increase)
    & (sum . (map fromEnum))
    & (putStrLn . show)

part1 :: IO ()
part1 = readIn >>= solve


main = part1
