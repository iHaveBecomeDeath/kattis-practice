#!/usr/bin/env python3

megabytesPerMonth = int(input())
numberOfMonths = int(input())
usedMegabytes = 0
i = 0

while i < numberOfMonths:
  usedMegabytes += (int(input()))
  i += 1

nextMonthsMegabytes = (megabytesPerMonth * numberOfMonths) - usedMegabytes + megabytesPerMonth

print(nextMonthsMegabytes)