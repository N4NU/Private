def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)


def modinv(e, pn):
    (inv, q, gcd_val) = egcd(e, pn)
    return inv % pn

# e * x ≡ 1 (mod (p-1)*(q-1))
# x = modinv(e, pn)

e = input('e:')
p = input('p:')
q = input('q:')

pn = (p-1)*(q-1)

print (hex(modinv(e, pn)))
