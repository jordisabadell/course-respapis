var express = require("express");
var app = express();

app.get("/", function(req, rest) {
    rest.send("Hello world NodeJS!");
});

app.listen(3000, function() {  //3000 = puerto de ejecución
    console.log("* Running on http://127.0.0.1:3000 (Press CTRL + C to quit)");
});