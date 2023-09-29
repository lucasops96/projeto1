from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from authors.forms.recipe_form import AuthorRecipeForm
from recipes.models import Recipe


class DashboardRecipe(View):
    def get(self, request, id):
        recipe = Recipe.objects.filter(
            pk=id,
            is_published=False,
            author=request.user
        ).first()

        if not recipe:
            raise Http404()
        
        form = AuthorRecipeForm(
            request.POST or None,
            files=request.FILES or None,
            instance=recipe
        )

        if form.is_valid():
            # Agora, o form é válido e eu posso tentar salvar
            recipe = form.save(commit=False)

            recipe.author = request.user
            recipe.preparation_steps_is_hmtl = False
            recipe.is_published = False

            recipe.save()

            messages.success(request,'Sua receita foi salva com sucesso!')
            return redirect(reverse('authors:dashboard_recipe_edit',args=(id,)))
            
        
        return render(request,'authors/pages/dashboard_recipe.html',context={
            'form':form
        })