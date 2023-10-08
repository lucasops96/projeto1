from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from authors.forms import LoginForm, RegisterForm
from authors.forms.recipe_form import AuthorRecipeForm
from recipes.models import Recipe


def register_view(request):
    register_form_data = request.session.get('register_form_data',None)
    form = RegisterForm(register_form_data)

    return render(request,'authors/pages/register_view.html',{
        'form':form,
        'form_action':reverse('authors:register_create'),
    })


def register_create(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request,'Your user is created, please login.')

        del(request.session['register_form_data'])
        return redirect(reverse('authors:login'))

    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render(request,'authors/pages/login.html',{
        'form': form,
        'form_action':reverse('authors:login_create'),
    })

def login_create(request):
    if not request.POST:
        raise Http404()
    
    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user =  authenticate(
            username=form.cleaned_data.get('username',''),
            password=form.cleaned_data.get('password',''),
        )

        if authenticated_user is not None:
            messages.success(request,'Your are logged in.')
            login(request,authenticated_user)
        else:
            messages.error(request,'Invalid credentils')
    else:
        messages.error(request,'Invalid username or password')
    
    return redirect(reverse('authors:dashboard'))


@login_required(login_url='authors:login',redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        messages.error(request, 'Invalid logout request')
        return redirect(reverse('authors:login'))
    
    if request.POST.get('username') != request.user.username:
        messages.error(request, 'Invalid logout user')
        return redirect(reverse('authors:login'))
    
    messages.success(request, 'Logged out successfully')
    logout(request)
    return redirect(reverse('authors:login'))

@login_required(login_url='authors:login',redirect_field_name='next')
def dashboard(request):
    recipes = Recipe.objects.filter(
        is_published=False,
        author=request.user
    )
    
    return render(request,'authors/pages/dashboard.html',context={
        'recipes':recipes,
    })


# @login_required(login_url='authors:login',redirect_field_name='next')
# def dashboard_recipe_edit(request,id):
#     recipe = Recipe.objects.filter(
#         pk=id,
#         is_published=False,
#         author=request.user
#     ).first()

#     if not recipe:
#         raise Http404()
    
#     form = AuthorRecipeForm(
#         request.POST or None,
#         files=request.FILES or None,
#         instance=recipe
#     )

#     if form.is_valid():
#         # Agora, o form é válido e eu posso tentar salvar
#         recipe = form.save(commit=False)

#         recipe.author = request.user
#         recipe.preparation_steps_is_hmtl = False
#         recipe.is_published = False

#         recipe.save()

#         messages.success(request,'Sua receita foi salva com sucesso!')
#         return redirect(reverse('authors:dashboard_recipe_edit',args=(id,)))
        
    
#     return render(request,'authors/pages/dashboard_recipe.html',context={
#         'form':form
#     })


# @login_required(login_url='authors:login',redirect_field_name='next')
# def dashboard_recipe_new(request):
#     form = AuthorRecipeForm(
#         request.POST or None,
#         files=request.FILES or None,
#     )

#     if form.is_valid():
#         recipe: Recipe = form.save(commit=False)

#         recipe.author = request.user
#         #Fiz está linha para atribuir o slug da receita criada antes do instrutor ensinar de como usar slugfy no model de Recipe.
#         #recipe.slug = recipe.title.lower().replace(' ','-')
#         recipe.preparation_steps_is_hmtl = False
#         recipe.is_published = False

#         recipe.save()

#         messages.success(request,'Salvo com sucesso!')
#         return redirect(
#             reverse('authors:dashboard_recipe_edit',args=(recipe.id,))
#         )



#     return render(request,'authors/pages/dashboard_recipe.html',context={
#         'form':form,
#         'form_action':reverse('authors:dashboard_recipe_new')
#     })

# @login_required(login_url='authors:login',redirect_field_name='next')
# def dashboard_recipe_delete(request):
#     if not request.POST:
#         raise Http404()
    
#     POST = request.POST
#     id = POST.get('id')
    
#     recipe = Recipe.objects.filter(
#         pk=id,
#         is_published=False,
#         author=request.user
#     ).first()

#     if not recipe:
#         raise Http404()
    
#     recipe.delete()
#     messages.success(request,'Deleted successfully')
#     return redirect(reverse('authors:dashboard'))