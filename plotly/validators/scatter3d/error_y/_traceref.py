import _plotly_utils.basevalidators


class TracerefValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self,
        plotly_name='traceref',
        parent_name='scatter3d.error_y',
        **kwargs
    ):
        super(TracerefValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            min=0,
            role='info',
            **kwargs
        )