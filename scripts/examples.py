#lazy evaluation
sum(x*x for x in range(10))
#iter tools
#zip

it.izip('abc', 'def')

list(it.izip('abc', 'def'))
list.(it.slice(iter(range(10), None, 8,2))