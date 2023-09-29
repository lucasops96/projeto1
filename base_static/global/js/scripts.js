function my_scope(){
    const forms = document.querySelectorAll('.form-delete')

    console.log(forms)
    for(const form of forms){
        form.addEventListener('submit',function(e){
            e.preventDefault();

            const confirmed = confirm('Are you sure?');

            if(confirmed){
                form.submit();
            }
        })
    }
}

my_scope();