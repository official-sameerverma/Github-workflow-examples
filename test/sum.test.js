const sum = require('../index')

test(' add 2 +3 equals to 5 ', ()=>{
    expect(sum(2,3)).toBe(5)
})

test(' add negative numbers  ', ()=>{
    expect(sum(-2, -3)).toBe(-5)
})