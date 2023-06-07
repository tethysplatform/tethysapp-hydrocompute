from tethys_sdk.base import TethysAppBase


class Hydrocompute(TethysAppBase):
    """
    Tethys app class for HydroCompute.
    """
    name = 'HydroLang and HydroCompute Demonstration'
    description = 'This application demonstrates the capabilities of HydroLang and HydroCompute, ' \
                  'powerful JavaScript libraries developed by the University of Iowa ' \
                  'Hydro- informatics Lab. Launch to learn more.'
    package = 'hydrocompute'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/sticker_uihilab2_white.png'
    root_url = 'uihi'
    color = '#ffd700'
    tags = '"Hydrology","Compute","Hydrologic Modeling","JavaScript"'
    enable_feedback = False
    feedback_emails = []
