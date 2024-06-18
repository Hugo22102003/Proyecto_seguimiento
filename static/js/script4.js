const selectBox = document.querySelector('.select-box');
const selecOption = document.querySelector('.select-option');
const soValue = document.querySelector('#soValue');
const optionSearch = document.querySelector('#optionSearch');
const options = document.querySelector('.options');
const optionlist = document.querySelectorAll('.options li');

selecOption.addEventListener('click', function() {
    selectBox.classList.toggle('active');
});

optionlist.forEach(function(optionlistSingle){
    optionlistSingle.addEventListener('click', function(){
        text = this.textContent;
        soValue.value = text;
        selectBox.classList.remove('active')
    })
});

optionSearch.addEventListener('keyup', function(){
    var filter, i, li
    filter = optionSearch.value.toUpperCase();
    li = options.getElementsByTagName('li');
    for(i = 0; i < li.length; i++){
        liCount = li[i];
        textValue = liCount.textContent ||  liCount.innerText;
        if(textValue.toUpperCase().indexOf(filter) > -1){
            li[i].style.display = '';
        }else{
            li[i].style.display = 'none';
        }
    }

})