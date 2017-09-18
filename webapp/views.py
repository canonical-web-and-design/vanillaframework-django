from django.views.generic import TemplateView


class YamlView(TemplateView):
    """
    Load the given data.yaml file render it to a page.

    The Yaml file location can be included by importing settings:
    ```
    from django.conf import settings
    settings.YAML_PATH
    ```
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """
        Set context data which can be accessed in templates.

        `context['message']` can be printed in template with `{{ message }}`
        """
        context = super().get_context_data(**kwargs)
        context['message'] = "Hello world!"
        return context
