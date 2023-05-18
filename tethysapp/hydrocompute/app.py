from tethys_sdk.base import TethysAppBase


class Hydrocompute(TethysAppBase):
    """
    Tethys app class for HydroCompute.
    """

    name = 'HydroCompute'
    description = 'Tethys app that demonstrates the capabilities of the HydroCompute library'
    package = 'hydrocompute'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'hydrocompute'
    color = '#f39c12'
    tags = ''
    enable_feedback = False
    feedback_emails = []