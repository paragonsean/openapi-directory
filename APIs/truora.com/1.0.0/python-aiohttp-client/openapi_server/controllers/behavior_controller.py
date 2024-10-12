from typing import List, Dict
from aiohttp import web

from openapi_server.models.behaviour_output import BehaviourOutput
from openapi_server.models.error import Error
from openapi_server import util


async def report_behavior(request: web.Request, birth_date, country, document_id, document_type, email, feedback_date, first_name, last_name, reason, phone_number=None) -> web.Response:
    """Report Behavior

    Creates a behavior item to report employee conducts that do not or might not be included in their background check. This report includes both possitive and negative behaviors and sorts them by severity.  ### Reasons to report a person  &lt;table&gt;   &lt;tr&gt;     &lt;td style&#x3D;\&quot;width: 100px\&quot;&gt;&lt;center&gt;&lt;b&gt;Very High&lt;/b&gt;&lt;br&gt;(Score: 1)&lt;/td&gt;     &lt;td&gt;Rape, Drug Dealing, Sexual Harassment&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;High&lt;/b&gt;&lt;br&gt;(Score: 0.8)&lt;/td&gt;     &lt;td&gt;Theft, Fights, Aggressive Behaviour, Identity Fraud, Drunk, Drug Possession&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Medium&lt;/b&gt;&lt;br&gt;(Score: 0.6)&lt;/td&gt;     &lt;td&gt;Absences&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Low&lt;/b&gt;&lt;br&gt;(Score: 0.4)&lt;/td&gt;     &lt;td&gt;Tardiness, Confidentiality Breach&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;None&lt;/b&gt;&lt;br&gt;(Score: 0)&lt;/td&gt;     &lt;td&gt;Good Reputation&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Unknown&lt;/b&gt;&lt;/td&gt;     &lt;td&gt;No information&lt;/td&gt;   &lt;/tr&gt; &lt;/table&gt;  **NOTE:** If the reason of your report is not here, please contact Truora support team. 

    :param birth_date: Birth date of reported person
    :type birth_date: str
    :param country: Document country
    :type country: str
    :param document_id: Person document ID
    :type document_id: str
    :param document_type: Document type associated with the background check
    :type document_type: str
    :param email: Reported person e-mail
    :type email: str
    :param feedback_date: Behavior report date
    :type feedback_date: str
    :param first_name: Person first name
    :type first_name: str
    :param last_name: Person last name
    :type last_name: str
    :param reason: Report reason
    :type reason: str
    :param phone_number: Phone number of the reported person
    :type phone_number: str

    """
    birth_date = util.deserialize_datetime(birth_date)
    feedback_date = util.deserialize_datetime(feedback_date)
    return web.Response(status=200)
