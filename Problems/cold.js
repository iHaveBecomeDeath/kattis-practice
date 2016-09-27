var n = readline();
var temps = readline().split(' ');
var coldTemps = temps.filter(v => {return v < 0});
print(coldTemps.length);
