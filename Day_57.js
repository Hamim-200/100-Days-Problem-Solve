var isEmpty = function(obj) {
    let flag = true;
    for(let i in obj){
        flag=false;
    }
    return flag;
    
};