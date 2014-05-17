import Data.Char

main = print $ p_16

p_16 = sum k
  where
        s = show $ power (*) 2 1000 1
        k = map digitToInt s

power :: Integral a => (t -> t -> t) -> t -> a -> t -> t
power _ _ 0 e = e
power f a n e = power f (f a a) (div n 2) (if odd n then f a e else e)