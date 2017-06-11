function getChildrenByTagName(node, tagname){
    var children = new Array();
    for (var i = 0; i < node.childNodes.length; i++){
        if (node.childNodes[i].tagName == tagname){
            children[children.length] = node.childNodes[i];
        }
    }
    return children;
}
function sortTable(colNum){
    var MAX_SCORE = 100000;
    var tb = document.getElementById("scoreTable");
    var tbod = getChildrenByTagName(document.getElementById("scoreTable"), "TBODY");
    if (!tbod || tbod.length != 1){
        alert("Sorting Error");
        return;
    }
    var trows = getChildrenByTagName(tbod[0], "TR");
    var allRows = new Array();
    var numShooters = trows.length;
    for (var i = 1; i < numShooters; i++){
        var sortObj = new Object();
        var tds = getChildrenByTagName(trows[i], "TD");
        if (isNaN(tds[colNum].innerHTML)){
            sortObj.sortVal = MAX_SCORE++;
        } else {
            sortObj.sortVal = parseFloat(tds[colNum].innerHTML);
        }
        sortObj.row = tbod[0].removeChild(trows[i]);
        allRows[allRows.length] = sortObj;
    }
    var tmp;
    for (var t = 0; t < allRows.length - 1; t++){
        for (var b = allRows.length - 1; b > t; b--){
            if (allRows[b].sortVal < allRows[t].sortVal){
                tmp = allRows[b];
                allRows[b] = allRows[t];
                allRows[t] = tmp;
            }
        }
    }
    for (var x = 0; x < allRows.length; x++){
        tbod[0].appendChild(allRows[x].row);
    }
}
function showAdjScore(evt){
    evt = (evt) ? evt : document.parentWindow.event;
    var theBox = document.createElement("DIV");
    theBox.id = this.id + "_adjscorebox";
    theBox.className = "scorebox";
    theBox.innerHTML = "some text";
    document.body.appendChild(theBox);
    theBox.style.left = evt.clientX;
    theBox.style.top = evt.clientY;
    this.scoreBox = theBox;
}
function closeAdjScore(evt){
    var theEl = document.getElementById(this.id + "_adjscorebox");
    if (theEl)
        document.body.removeChild(theEl);
}
