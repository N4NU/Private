main = print $ diff 100
 
diff :: Int->Int
diff a = addsq a -sqadd a

sqadd :: Int->Int
sqadd a = add sq a

addsq :: Int->Int
addsq a = sq $ add (\x -> x)  a

add :: (Int->Int)->Int->Int
add f 0 = 0
add f a  = f a + add f (a-1)

sq a = a * a