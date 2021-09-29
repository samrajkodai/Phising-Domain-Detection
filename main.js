
var count=0;
function as()
{
setTimeout("color()",10000);
}
function color()
{
var a =new 
Array("#61EDFF80","#89FF6180","#FF71D780","#5F15FFC6","pink","green","#FF103CC6");
if(count<=10)
{
document.body.style.backgroundColor=a[count++];
setTimeout("color()",10000);
}
else
{
count=0;
as();
}
}
