const year=2023;
const month=prompt("Mês (0=Janeiro):");
const weekdays="DSTQQSS";

var mday=new Date(year,month,1);
var cabe=[];
while (mday.getMonth() === Number(month)) {
    cabe.push(weekdays[mday.getDay()]);
    mday.setDate(mday.getDate()+1);
}
console.log(cabe)
