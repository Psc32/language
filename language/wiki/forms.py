from django import forms
from wiki.models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length= 128, label='类别名称', help_text='请输入类别名称')
    
    class Meta:
        model =Category
        fields = ('name',)
        
        
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length = 128, label='页面标题', help_text = '请输入页面标题')
    url = forms.URLField(max_length = 128, label = '页面网址', help_text = '请输入页面网址')
    
    
    class Meta:
        model = Page
        exclude = ('category', 'views') 


    def clean(self):
        cleanedData = self.cleaned_data
        url = cleanedData.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleanedData['url'] = url
        return cleanedData       