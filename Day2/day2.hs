import System.IO
import Data.Function

readIn :: IO [String]
readIn = do
    content <- readFile "input_day2.txt"
    return (lines content)

data Direction = Forward | Up | Down 
    deriving Show

parseDirection :: String -> Maybe Direction
parseDirection "forward" = Just Forward
parseDirection "up" = Just Up
parseDirection "down" = Just Down
parseDirection _ = Nothing

data Command = Command
    { direction :: Direction
    , distance :: Int
    } deriving Show

parseCommand :: [String] -> Maybe Command
parseCommand [dir, dist] = do 
    direction <- parseDirection dir
    return (Command (direction) (read dist :: Int))

move :: (Int, Int) -> Maybe Command -> (Int, Int)
move prev Nothing = prev
move (x, y) (Just (Command Forward n)) = (x + n, y)
move (x, y) (Just (Command Up n)) = (x, y - n)
move (x, y) (Just (Command Down n)) = (x, y + n)

tupProd (a, b) = a * b

solve :: [String] -> IO ()
solve = putStrLn . show . tupProd . (foldl move (0, 0)) . (map parseCommand) . (map words)

main = readIn >>= solve
