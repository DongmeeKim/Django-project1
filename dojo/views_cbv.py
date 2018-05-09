from django.http import HttpResponse
from django.views.generic import View, TemplateView



class PostListView1(View):
    def get(help, request):
        name = '공유'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
        <h1> ASK Django </h1>

        <p> {name} </p>

        <p> 여러분의 파이썬 & 장고 페이스메이커가 되겠습니다. </p> 

        '''


post_list1 = PostListView1.as_view()


class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'


post_list2 = PostListView2.as_view()