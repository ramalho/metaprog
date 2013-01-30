exports.recursivo = function recursivo(n) {
  return n < 2 ? 1 : n * recursivo(n-1);
};
exports.iterativo = function (n) {
  var res = n;
  while (--n > 1) res *= n;
  return res;
};
