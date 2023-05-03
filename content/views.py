from django.shortcuts import render, redirect

from content.models import Blog


def blog_list(request):
    blog = Blog.objects.all()
    # blog = Blog.objects.get(pk=product_id)
    context = {
        'blog': blog,
    }
    # if request.method == 'POST':
    #     if 'add_comment' in request.POST:
    #         name = request.POST['comment']
    #         comment = Comment(
    #             name=name,
    #             product=product,
    #             user=request.user
    #         )
    #         comment.save()
    #         return redirect('product_details', product_id=product_id)
    return render(request, 'blog/blog.html', context=context)


def blog_single(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog-single.html', context=context)

