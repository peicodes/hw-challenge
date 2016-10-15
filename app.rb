=begin
require 'csv'

snapshots=[]
CSV.foreach("./test.csv",{:headers=>:first_row}) do |row|
  snapshots << {
    year: row[0].to_i,
    cash_flow: row[1].to_f,
    market_value: row[2].to_f
  }
end
# 0.045
x=1

result = snapshots.each_with_index.inject(0) do |sum, (snapshot, index)|
  sum + snapshot[:cash_flow]*(1+x)**(snapshots.length-index-1)
end

puts result

=end


def expand(exponent, result)
  coef = []
  (0..exponent).each do |i|
    coef << combo(result, i)
  end


  coef[0] = coef[0] - combo(exponent, exponent)
  coef[1] -= 1

  puts coef

  evaluate(0.0, coef)
end

def combo (n, k)
  fact(n.to_f)/(fact(k.to_f)*(fact(n.to_f-k.to_f)))
end

def fact(x)
  (1..x).reduce(:*) || 1
end

def evaluate(x, coef)
  coef.map.with_index { |k, power| k * (x**power) }.reduce(0, :+)
end

expand(4,4)
