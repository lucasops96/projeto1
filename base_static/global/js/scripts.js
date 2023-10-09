
(()=>{
    const forms = document.querySelectorAll('.form-delete')

    for(const form of forms){
        form.addEventListener('submit',function(e){
            e.preventDefault();

            const confirmed = confirm('Are you sure?');

            if(confirmed){
                form.submit();
            }
        })
    }
})()


(()=>{
    const buttonCloseMenu = document.querySelector('.button-close-menu')
    const buttonShowMenu = document.querySelector('.button-show-menu')
    const menuContainer = document.querySelector('.menu-container')
})()
    


