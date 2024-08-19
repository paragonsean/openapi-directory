# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="Aviation Radiation API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Aviation Radiation API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Our atmosphere protects us from a hostile space radiation environment comprising high energy particles of solar and intergalactic origin. Solar radiation is significant during unpredictable and short lived solar flares and coronal mass ejections (CMEs); however, galactic cosmic radiation (GCR) is omnipresent. The GCR intensity varies with latitude, longitude, and time due to effects of solar activity on the interplanetary magnetic field, as well as the Earth&#39;s magnetic field. Space radiation collides with gases in the atmosphere, leading to a complex shower of high energy radiation, the intensity and composition of which varies spatially and temporally. Excessive exposure to radiation can damage DNA and lead to long-term health effects such as an increased risk of cancer.  &lt;br&gt;&lt;br&gt; Resulting radiation levels at commercial aircraft altitudes are greater than at sea level. Aircrew are classified as radiation workers in some countries; however, planning to limit their exposure, and monitoring, is generally lacking. Both real-time measurements and predictive models of radiation in the atmosphere are important to mitigate the radiation risk to crew. &lt;br&gt;&lt;br&gt; We host a RESTful API to models of cosmic ray induced ionising radiation in the atmosphere.  The CARI7 and PARMA endpoints use models developed by the US Federal Aviation Administration and the Japan Atomic Energy Agency to  calculate cosmic radiation doses at a point.  The Route Dose API calculates the same quantities along a great circle route between two airports using CARI7. &lt;br&gt;&lt;br&gt; API requests must contain a key \&quot;API-Key\&quot; in the header (see code samples). Obtain a key from  &lt;a href&#x3D;&#39;https://developer.amentum.io&#39;&gt;here&lt;/a&gt;. &lt;br&gt;&lt;br&gt;  Help us improve the quality of our web APIs by completing our 2 minute survey &lt;a href&#x3D;\&quot;https://www.surveymonkey.com/r/CTDTRBN\&quot;&gt;here&lt;/a&gt;.&lt;br&gt;&lt;br&gt; Amentum Pty Ltd is not responsible nor liable for any loss or damage of any sort incurred as a result of using the API. &lt;br&gt;&lt;br&gt; Copyright &lt;a href&#x3D;&#39;https://amentum.space&#39;&gt;Amentum Pty Ltd&lt;/a&gt; 2022. 
    """
)

