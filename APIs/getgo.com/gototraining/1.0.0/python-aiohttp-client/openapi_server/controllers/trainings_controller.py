from typing import List, Dict
from aiohttp import web

from openapi_server.models.host_url import HostUrl
from openapi_server.models.notified_parties import NotifiedParties
from openapi_server.models.organizer import Organizer
from openapi_server.models.registration_settings import RegistrationSettings
from openapi_server.models.training import Training
from openapi_server.models.training_name_description import TrainingNameDescription
from openapi_server.models.training_organizers import TrainingOrganizers
from openapi_server.models.training_req_create import TrainingReqCreate
from openapi_server.models.training_times import TrainingTimes
from openapi_server import util


async def cancel_training(request: web.Request, authorization, organizer_key, training_key) -> web.Response:
    """Delete Training

    Deletes a scheduled or completed training. For scheduled trainings, it deletes all scheduled sessions of the training. For completed trainings, the sessions remain in the database. No email is sent to organizers or registrants, but when participants attempt to start or join the training, they are directed to a page that states: Training Not Found: The training you are trying to join is no longer available.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param training_key: The key of the training
    :type training_key: int

    """
    return web.Response(status=200)


async def get_all_trainings(request: web.Request, authorization, organizer_key) -> web.Response:
    """Get Trainings

    This call retrieves information on all scheduled trainings for a given organizer. The trainings are returned in the order in which they were created. Completed trainings are not included; ongoing trainings with past sessions are included along with the past sessions. If the organizer does not have any scheduled trainings, the response will be empty.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int

    """
    return web.Response(status=200)


async def get_manage_training_url(request: web.Request, authorization, organizer_key, training_key) -> web.Response:
    """Get Management URL for Training

    A request for a direct URL to the admin portal for a specific training. The request identifies the organizer and the training; the response provides a link the organizer can use to manage or launch the training in the admin portal. The training organizer will be required to log in. You can schedule and manage the training (e.g., add tests, polls and training materials) from the URL provided in the response.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param training_key: The key of the training
    :type training_key: int

    """
    return web.Response(status=200)


async def get_organisers_for_training(request: web.Request, authorization, organizer_key, training_key) -> web.Response:
    """Get Training Organizers

    Retrieves organizer details for a specific training. This is only applicable to multi-user accounts with sharing enabled (co-organizers).

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param training_key: The key of the training
    :type training_key: int

    """
    return web.Response(status=200)


async def get_start_url(request: web.Request, authorization, organizer_key, training_key) -> web.Response:
    """Get Start Url

    Returns a URL that can be used to start a training. When this URL is opened in a web browser, the GoToTraining client will be downloaded and launched and the training will start after the organizer logs in with its credentials.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param training_key: The key of the training
    :type training_key: int

    """
    return web.Response(status=200)


async def get_training(request: web.Request, authorization, organizer_key, training_key) -> web.Response:
    """Get Training

    Uses the organizer key and training key to retrieve information on a scheduled training.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param training_key: The key of the training
    :type training_key: int

    """
    return web.Response(status=200)


async def schedule_training(request: web.Request, authorization, organizer_key, body) -> web.Response:
    """Create Training

    Schedules a training of one or more sessions. The call requires a training&#39;s name, at least one start and end time, and optionally may include additional sessions, a description, additional organizers (presenters), and registration settings. You can only add organizers to a training if you have a multi-user account. Once a training has been created with this method, you can accept registrations to the training. Registration is for the entire training - all sessions. (The GoToTraining admin site enables you to create trainings that allow participants to register for individual sessions as well as automatically create weekly or monthly events.) Registration settings controls whether you allow web registration for this training, and whether a confirmation email is sent to the registrant following registration. Disabling the confirmation email is an API-only setting. If the user registers through the GoToTraining website, a confirmation email is sent. If the user is manually approved by the training administrator through the GoToTraining web site, the confirmation email is sent. It is recommended that you disable web registration if you disable confirmation emails. The response contains a trainingKey for the scheduled training.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param body: The details of the training to create
    :type body: dict | bytes

    """
    body = TrainingReqCreate.from_dict(body)
    return web.Response(status=200)


async def start_training(request: web.Request, authorization, training_key) -> web.Response:
    """Start Training

    Returns a URL that can be used to start a training. When this URL is opened in a web browser, the GoToTraining client will be downloaded and launched and the training will start. A login of the organizer is not required.

    :param authorization: Access token
    :type authorization: str
    :param training_key: The key of the training
    :type training_key: int

    """
    return web.Response(status=200)


async def update_organisers_for_training(request: web.Request, authorization, organizer_key, training_key, body) -> web.Response:
    """Update Training Organizers

    Replaces the co-organizers for a specific training. The scheduling organizer cannot be unassigned. Organizers will be notified via email if the notifyOrganizers parameter is set to true. Replaced organizers are not notified. This method is only applicable to multi-user accounts with sharing enabled (co-organizers).

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param training_key: The key of the training
    :type training_key: int
    :param body: The details of the training to create
    :type body: dict | bytes

    """
    body = TrainingOrganizers.from_dict(body)
    return web.Response(status=200)


async def update_registration_settings_for_training(request: web.Request, authorization, organizer_key, training_key, body) -> web.Response:
    """Update Training Registration Settings

    An API request to automatically enable or disable web registrations and confirmation emails to registrants.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param training_key: The key of the training
    :type training_key: int
    :param body: The new registration settings for the training
    :type body: dict | bytes

    """
    body = RegistrationSettings.from_dict(body)
    return web.Response(status=200)


async def update_training_name_description(request: web.Request, authorization, organizer_key, training_key, body) -> web.Response:
    """Update Training Name and Description

    Request to update a scheduled training name and description.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param training_key: The key of the training
    :type training_key: int
    :param body: The new name and description for the training
    :type body: dict | bytes

    """
    body = TrainingNameDescription.from_dict(body)
    return web.Response(status=200)


async def update_training_times(request: web.Request, authorization, organizer_key, training_key, body) -> web.Response:
    """Update Training Times

     A request to update a scheduled training&#39;s start and end times. If the request contains &#39;notifyTrainers &#x3D; true&#39; and &#39;notifyRegistrants &#x3D; true&#39;, both organizers and registrants are notified. The response provides the number of notified trainers and registrants.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param training_key: The key of the training
    :type training_key: int
    :param body: The new start and end times for the scheduled training
    :type body: dict | bytes

    """
    body = TrainingTimes.from_dict(body)
    return web.Response(status=200)
