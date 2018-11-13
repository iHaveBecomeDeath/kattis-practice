
function candles_for_row(input_line) {
  var input = input_line.split(' ');
  function iterate_days(num, sum) {
    sum += num + 1;
    num--;
    if (num > 0) {
      sum = iterate_days(num, sum);
    }
    return sum;
  }

  var sum_outer = 0;
  return `${input[0]} ${iterate_days(parseInt(input[1]), sum_outer)}`;
}

for (var i = 0; i < readline(); i++) {
  print(candles_for_row(readline()));
}
