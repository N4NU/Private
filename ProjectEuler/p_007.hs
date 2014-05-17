main = print $  prime !! 10000

prime :: [Int]
prime = 2 : prime_make [3, 5 .. ]

prime_make :: [Int] -> [Int]
prime_make (p:xs) = p : prime_make[x | x <- xs, x `mod` p /= 0]