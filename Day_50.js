function memoize(fn) {
    fn.cache = {};
    return function(...args) {
      const key = JSON.stringify(args);
      if (key in fn.cache) {
        return fn.cache[key];
      }
      const result = fn(...args);
      fn.cache[key] = result;
      return result;
    }
  }
  