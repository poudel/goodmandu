from rest_framework.renderers import BrowsableAPIRenderer as OriginalBrowsableAPIRenderer


class BrowsableAPIRenderer(OriginalBrowsableAPIRenderer):

    def get_context(self, *args):
        ctx = super().get_context(*args)
        ctx.update({
            "post_form": None,
            "put_form": None,
        })
        return ctx
