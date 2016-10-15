// var fs = require('fs')

// const filePath = './test.csv'

// fs.readFile(filePath, 'utf8', function(err, data) {
//     if (err) {
//         throw err
//     } else {
//         console.log(' - ', data); 
//     }
// })

var count = 0
var snapshots = []

var lr = require('readline').createInterface({
    input: require('fs').createReadStream('./test.csv')
})

lr.on('line', function(line) {
    if (count > 0) {
        snapshots.push(line.split(','))
    }
    count++
    // console.log(' - ', line)
})

lr.on('close', function() {
    // console.log(snapshots)
    
    // console.log(snapshots[1][2])

    var x = (snapshots[1][2] - snapshots[1][1])/snapshots[0][2] - 1
    console.log(x)
})


