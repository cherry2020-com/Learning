// var re = /\w+\s/g;  // \w 匹配一个单字字符（字母、数字或者下划线）。等价于 [A-Za-z0-9_]。 \s 匹配空白字符
// var re1 = /\w+\s+\w+/g;
// const re2 = /<(img)\s+\w+.*?>/g;
// var str = "<img     testfor> eroi23 fee fi fo fum ";
// var myArray = str.match(re);
// var myArray1 = str.match(re1);
// var myArray2 = str.match(re2);
// console.log(myArray);
// console.log(myArray1);
// console.log(myArray2);



// // 测试: 可以验证并提取出带名字的Email地址：
// var
//     i,
//     re = /^[\w|.]+\@\w+\.(\w+)$/;
//     re1 = /^[\w+\.]+\@\w+\.(com|org)$/;
//     success = true,
//     should_pass = ['someone@gmail.com', 'bill.gates@microsoft.com', 'tom@voyager.org', 'bob2015@163.com'],
//     should_fail = ['test#gmail.com', 'bill@microsoft', 'bill%gates@ms.com', '@voyager.org'];
// for (i = 0; i < should_pass.length; i++) {
//     if (!re.test(should_pass[i])) {
//         console.log('测试失败: ' + should_pass[i]);
//         success = false;
//         break;
//     }
// }
// for (i = 0; i < should_fail.length; i++) {
//     if (re.test(should_fail[i])) {
//         console.log('测试失败: ' + should_fail[i]);
//         success = false;
//         break;
//     }
// }
// if (success) {
//     console.log('测试通过!');
// }

// 测试: 可以验证并提取出带名字的Email地址：
// \w 匹配一个单字字符（字母、数字或者下划线）。等价于 [A-Za-z0-9_]。 \s 匹配空白字符
// \s sapce
// \w word
var re = /^\<(\w+\s+\w+)\>+\s+(\w+\@\w+\.\w+)$/;  //括号代表分组
// var re = /^\<([\w\s\w]+)\>+\s+(\w+\@\w+\.org|com)$/;
var r = re.exec('<Tom Paris> tom@voyager.org');
if (r === null || r.toString() !== ['<Tom Paris> tom@voyager.org', 'Tom Paris', 'tom@voyager.org'].toString()) {
    console.log(r)
    console.log('测试失败!');
}
else {
    console.log(r)
    console.log('测试成功!');
}