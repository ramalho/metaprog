Function.prototype.memorado = function(key){
  this._values = this._values || {};
  return this._values[key] !== undefined ?
    this._values[key] :
    this._values[key] = this.apply(this, arguments);
};

Function.prototype.memorar = function(){
  var fn = this;
  return function(){
    return fn.memorado.apply(fn, arguments);
  };
};
