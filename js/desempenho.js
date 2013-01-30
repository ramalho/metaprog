var Benchmark = require('benchmark');
var fatorial = require('./fatorial');
require('./memorar');

var suite = new Benchmark.Suite;
var lista = [7, 1, 5, 3, 9, 15, 11, 21, 13, 17, 19];

suite.add('recursivo -> 21!', function() {
  fatorial.recursivo(21);
})
.add('iterativo -> 21!', function() {
  fatorial.iterativo(21);
})
.add('recursivo -> 2!...21!', function() {
  for (var i=0; i<lista.length; i++)
    fatorial.recursivo(lista[i]);
})
.add('iterativo -> 2!...21!', function() {
  for (var i=0; i<lista.length; i++)
    fatorial.iterativo(lista[i]);
})
// add listeners
.on('cycle', function(event) {
  console.log(String(event.target));
})
// run async
.run({ 'async': true });
