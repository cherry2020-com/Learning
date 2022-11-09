function removeAllSpaces(stringValue){
    stringValue = stringValue.trim();
    while(stringValue.indexOf(" ") != -1){
        stringValue = stringValue.replace(" ", "");
    }
    return stringValue;
}

let  items = [];

materialColumn = ['   thanks jsjdoi   we12323    ', 'fdjk jewri%kjdsfj  jdsljf ', '  jfd kjdsf   '];
quantityColumn = [' jjkfd we234324  ',' djkf ','dfda  '];
for(let index=0; index < materialColumn.length; index++){
    let row = [];
    row.push( removeAllSpaces(materialColumn[index]));
    row.push( removeAllSpaces(quantityColumn[index])); 
    items.push(row);
}
// return items;

console.log(items);