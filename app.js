var csv = require('csv-parser')
var fs = require('fs')
var arrYear=[];
var arrCash=[];
var arrMValue=[];
var finalVal=0;
var xVal=0;


fs.createReadStream('test.csv')
  .pipe(csv())
  .on('data', function (data) {
    arrYear.push(data.year);
    arrCash.push(data.cash_flow);
    arrMValue.push(data.market_value);
  }).on('end', function () {

  	while(Math.abs(finalVal-arrMValue[arrYear.length-1]) != 0.1){
	  	for (var i=0; i<(arrYear.length-1); i++){
	  		console.log(finalVal);
	  		finalVal += arrCash[i]*(1+xVal)^(arrYear.length-(arrYear[i]-1));
	   	}
	  	xVal+=0.001;
	  }
	  console.log(xVal);
  })




  // snapshot[0].cash_flow * (1 + x) ^ (n - 1) + snapshot[1].cash_flow * (1 + x) ^ (n - 2) + ...snapshot[n-2].cash_flow * (1 + x) ^ 1 = snapshot[n-1].market_value