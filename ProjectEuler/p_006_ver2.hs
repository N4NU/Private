main = print $ diff 100

diff :: Int->Int
diff a = addsq a -sqadd a

sqadd :: Int->Int
sqadd a = add 2 a

addsq :: Int->Int
addsq a = power (*) (add 1 a) 2 1

add :: Int->Int->Int
add n 0 = 0
add n m = power (*) m n 1 + add n (m-1)

power :: Integral a => (t -> t -> t) -> t -> a -> t -> t
power _ _ 0 e = e
power f a n e = power f (f a a) (div n 2) (if odd n then f a e else e)