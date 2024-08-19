from typing import List, Dict
from aiohttp import web

from openapi_server.models.assessed_machine import AssessedMachine
from openapi_server.models.assessed_machine_result_list import AssessedMachineResultList
from openapi_server.models.assessment import Assessment
from openapi_server.models.assessment_options import AssessmentOptions
from openapi_server.models.assessment_options_result_list import AssessmentOptionsResultList
from openapi_server.models.assessment_result_list import AssessmentResultList
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.download_url import DownloadUrl
from openapi_server.models.group import Group
from openapi_server.models.group_result_list import GroupResultList
from openapi_server.models.hyper_v_collector import HyperVCollector
from openapi_server.models.hyper_v_collector_list import HyperVCollectorList
from openapi_server.models.machine import Machine
from openapi_server.models.machine_result_list import MachineResultList
from openapi_server.models.operation_result_list import OperationResultList
from openapi_server.models.project import Project
from openapi_server.models.project_result_list import ProjectResultList
from openapi_server.models.update_group_body import UpdateGroupBody
from openapi_server.models.v_mware_collector import VMwareCollector
from openapi_server.models.v_mware_collector_list import VMwareCollectorList
from openapi_server import util


async def assessed_machines_get(request: web.Request, subscription_id, resource_group_name, project_name, group_name, assessment_name, assessed_machine_name, api_version, accept_language=None) -> web.Response:
    """Get an assessed machine.

    Get an assessed machine with its size &amp; cost estimate that was evaluated in the specified assessment.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param group_name: Unique name of a group within a project.
    :type group_name: str
    :param assessment_name: Unique name of an assessment within a project.
    :type assessment_name: str
    :param assessed_machine_name: Unique name of an assessed machine evaluated as part of an assessment.
    :type assessed_machine_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def assessed_machines_list_by_assessment(request: web.Request, subscription_id, resource_group_name, project_name, group_name, assessment_name, api_version, accept_language=None) -> web.Response:
    """Get assessed machines for assessment.

    Get list of machines that assessed as part of the specified assessment. Returns a json array of objects of type &#39;assessedMachine&#39; as specified in the Models section.  Whenever an assessment is created or updated, it goes under computation. During this phase, the &#39;status&#39; field of Assessment object reports &#39;Computing&#39;. During the period when the assessment is under computation, the list of assessed machines is empty and no assessed machines are returned by this call. 

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param group_name: Unique name of a group within a project.
    :type group_name: str
    :param assessment_name: Unique name of an assessment within a project.
    :type assessment_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def assessments_create(request: web.Request, subscription_id, resource_group_name, project_name, group_name, assessment_name, api_version, accept_language=None, assessment=None) -> web.Response:
    """Create or Update assessment.

    Create a new assessment with the given name and the specified settings. Since name of an assessment in a project is a unique identifier, if an assessment with the name provided already exists, then the existing assessment is updated.  Any PUT operation, resulting in either create or update on an assessment, will cause the assessment to go in a \&quot;InProgress\&quot; state. This will be indicated by the field &#39;computationState&#39; on the Assessment object. During this time no other PUT operation will be allowed on that assessment object, nor will a Delete operation. Once the computation for the assessment is complete, the field &#39;computationState&#39; will be updated to &#39;Ready&#39;, and then other PUT or DELETE operations can happen on the assessment.  When assessment is under computation, any PUT will lead to a 400 - Bad Request error. 

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param group_name: Unique name of a group within a project.
    :type group_name: str
    :param assessment_name: Unique name of an assessment within a project.
    :type assessment_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str
    :param assessment: New or Updated Assessment object.
    :type assessment: dict | bytes

    """
    assessment = Assessment.from_dict(assessment)
    return web.Response(status=200)


async def assessments_delete(request: web.Request, subscription_id, resource_group_name, project_name, group_name, assessment_name, api_version, accept_language=None) -> web.Response:
    """Deletes an assessment from the project.

    Delete an assessment from the project. The machines remain in the assessment. Deleting a non-existent assessment results in a no-operation.  When an assessment is under computation, as indicated by the &#39;computationState&#39; field, it cannot be deleted. Any such attempt will return a 400 - Bad Request. 

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param group_name: Unique name of a group within a project.
    :type group_name: str
    :param assessment_name: Unique name of an assessment within a project.
    :type assessment_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def assessments_get(request: web.Request, subscription_id, resource_group_name, project_name, group_name, assessment_name, api_version, accept_language=None) -> web.Response:
    """Get an assessment.

    Get an existing assessment with the specified name. Returns a json object of type &#39;assessment&#39; as specified in Models section.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param group_name: Unique name of a group within a project.
    :type group_name: str
    :param assessment_name: Unique name of an assessment within a project.
    :type assessment_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def assessments_get_report_download_url(request: web.Request, subscription_id, resource_group_name, project_name, group_name, assessment_name, api_version, accept_language=None) -> web.Response:
    """Get download URL for the assessment report.

    Get the URL for downloading the assessment in a report format.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param group_name: Unique name of a group within a project.
    :type group_name: str
    :param assessment_name: Unique name of an assessment within a project.
    :type assessment_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def assessments_list_by_group(request: web.Request, subscription_id, resource_group_name, project_name, group_name, api_version, accept_language=None) -> web.Response:
    """Get all assessments created for the specified group.

    Get all assessments created for the specified group.  Returns a json array of objects of type &#39;assessment&#39; as specified in Models section. 

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param group_name: Unique name of a group within a project.
    :type group_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def assessments_list_by_project(request: web.Request, subscription_id, resource_group_name, project_name, api_version, accept_language=None) -> web.Response:
    """Get all assessments created in the project.

    Get all assessments created in the project.  Returns a json array of objects of type &#39;assessment&#39; as specified in Models section. 

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def groups_create(request: web.Request, subscription_id, resource_group_name, project_name, group_name, api_version, accept_language=None, group=None) -> web.Response:
    """Create a new group with specified settings.

    Create a new group by sending a json object of type &#39;group&#39; as given in Models section as part of the Request Body. The group name in a project is unique.  This operation is Idempotent. 

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param group_name: Unique name of a group within a project.
    :type group_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str
    :param group: New or Updated Group object.
    :type group: dict | bytes

    """
    group = Group.from_dict(group)
    return web.Response(status=200)


async def groups_delete(request: web.Request, subscription_id, resource_group_name, project_name, group_name, api_version, accept_language=None) -> web.Response:
    """Delete the group

    Delete the group from the project. The machines remain in the project. Deleting a non-existent group results in a no-operation.  A group is an aggregation mechanism for machines in a project. Therefore, deleting group does not delete machines in it. 

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param group_name: Unique name of a group within a project.
    :type group_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def groups_get(request: web.Request, subscription_id, resource_group_name, project_name, group_name, api_version, accept_language=None) -> web.Response:
    """Get a specific group.

    Get information related to a specific group in the project. Returns a json object of type &#39;group&#39; as specified in the models section.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param group_name: Unique name of a group within a project.
    :type group_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def groups_list_by_project(request: web.Request, subscription_id, resource_group_name, project_name, api_version, accept_language=None) -> web.Response:
    """Get all groups

    Get all groups created in the project. Returns a json array of objects of type &#39;group&#39; as specified in the Models section.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def groups_update_machines(request: web.Request, subscription_id, resource_group_name, project_name, group_name, api_version, accept_language=None, group_update_properties=None) -> web.Response:
    """Update machines in group.

    Update machines in group by adding or removing machines.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param group_name: Unique name of a group within a project.
    :type group_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str
    :param group_update_properties: Machines list to be added or removed from group.
    :type group_update_properties: dict | bytes

    """
    group_update_properties = UpdateGroupBody.from_dict(group_update_properties)
    return web.Response(status=200)


async def hyper_v_collectors_create(request: web.Request, subscription_id, resource_group_name, project_name, hyper_v_collector_name, api_version, accept_language=None, collector_body=None) -> web.Response:
    """Create or Update Hyper-V collector.

    Create or Update Hyper-V collector

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param hyper_v_collector_name: Unique name of a Hyper-V collector within a project.
    :type hyper_v_collector_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str
    :param collector_body: New or Updated Hyper-V collector.
    :type collector_body: dict | bytes

    """
    collector_body = HyperVCollector.from_dict(collector_body)
    return web.Response(status=200)


async def hyper_v_collectors_delete(request: web.Request, subscription_id, resource_group_name, project_name, hyper_v_collector_name, api_version, accept_language=None) -> web.Response:
    """Deletes Hyper-V collector from the project.

    Delete a Hyper-V collector from the project.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param hyper_v_collector_name: Unique name of a Hyper-V collector within a project.
    :type hyper_v_collector_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def hyper_v_collectors_get(request: web.Request, subscription_id, resource_group_name, project_name, hyper_v_collector_name, api_version, accept_language=None) -> web.Response:
    """Get a Hyper-V collector.

    Get a Hyper-V collector.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param hyper_v_collector_name: Unique name of a Hyper-V collector within a project.
    :type hyper_v_collector_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def hyper_v_collectors_list_by_project(request: web.Request, subscription_id, resource_group_name, project_name, api_version, accept_language=None) -> web.Response:
    """Get a list of Hyper-V collector.

    Get a list of Hyper-V collector.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def machines_get(request: web.Request, subscription_id, resource_group_name, project_name, machine_name, api_version, accept_language=None) -> web.Response:
    """Get a specific machine.

    Get the machine with the specified name. Returns a json object of type &#39;machine&#39; defined in Models section.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param machine_name: Unique name of a machine in private datacenter.
    :type machine_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def machines_list_by_project(request: web.Request, subscription_id, resource_group_name, project_name, api_version, accept_language=None) -> web.Response:
    """Get all machines in the project

    Get data of all the machines available in the project. Returns a json array of objects of type &#39;machine&#39; defined in Models section.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def operations_list(request: web.Request, ) -> web.Response:
    """Get list of operations supported in the API.

    Get a list of REST API supported by Microsoft.Migrate provider.


    """
    return web.Response(status=200)


async def project_assessment_options(request: web.Request, subscription_id, resource_group_name, project_name, assessment_options_name, api_version, accept_language=None) -> web.Response:
    """Get all available options for the properties of an assessment on a project.

    Get all available options for the properties of an assessment on a project.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param assessment_options_name: Name of the assessment options. The only name accepted in default.
    :type assessment_options_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def project_assessment_options_list(request: web.Request, subscription_id, resource_group_name, project_name, api_version, accept_language=None) -> web.Response:
    """Gets list of all available options for the properties of an assessment on a project.

    Gets list of all available options for the properties of an assessment on a project.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def projects_create(request: web.Request, subscription_id, resource_group_name, project_name, api_version, accept_language=None, project=None) -> web.Response:
    """Create or update project.

    Create a project with specified name. If a project already exists, update it.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str
    :param project: New or Updated project object.
    :type project: dict | bytes

    """
    project = Project.from_dict(project)
    return web.Response(status=200)


async def projects_delete(request: web.Request, subscription_id, resource_group_name, project_name, api_version, accept_language=None) -> web.Response:
    """Delete the project

    Delete the project. Deleting non-existent project is a no-operation.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def projects_get(request: web.Request, subscription_id, resource_group_name, project_name, api_version, accept_language=None) -> web.Response:
    """Get the specified project.

    Get the project with the specified name.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def projects_list(request: web.Request, subscription_id, resource_group_name, api_version, accept_language=None) -> web.Response:
    """Get all projects.

    Get all the projects in the resource group.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def projects_list_by_subscription(request: web.Request, subscription_id, api_version, accept_language=None) -> web.Response:
    """Get all projects.

    Get all the projects in the subscription.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def projects_update(request: web.Request, subscription_id, resource_group_name, project_name, api_version, accept_language=None, project=None) -> web.Response:
    """Update project.

    Update a project with specified name. Supports partial updates, for example only tags can be provided.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str
    :param project: Updated project object.
    :type project: dict | bytes

    """
    project = Project.from_dict(project)
    return web.Response(status=200)


async def v_mware_collectors_create(request: web.Request, subscription_id, resource_group_name, project_name, vm_ware_collector_name, api_version, accept_language=None, collector_body=None) -> web.Response:
    """Create or Update VMware collector.

    Create or Update VMware collector

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param vm_ware_collector_name: Unique name of a VMware collector within a project.
    :type vm_ware_collector_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str
    :param collector_body: New or Updated VMware collector.
    :type collector_body: dict | bytes

    """
    collector_body = VMwareCollector.from_dict(collector_body)
    return web.Response(status=200)


async def v_mware_collectors_delete(request: web.Request, subscription_id, resource_group_name, project_name, vm_ware_collector_name, api_version, accept_language=None) -> web.Response:
    """Deletes VMware collector from the project.

    Delete a VMware collector from the project.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param vm_ware_collector_name: Unique name of a VMware collector within a project.
    :type vm_ware_collector_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def v_mware_collectors_get(request: web.Request, subscription_id, resource_group_name, project_name, vm_ware_collector_name, api_version, accept_language=None) -> web.Response:
    """Get a VMware collector.

    Get a VMware collector.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param vm_ware_collector_name: Unique name of a VMware collector within a project.
    :type vm_ware_collector_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def v_mware_collectors_list_by_project(request: web.Request, subscription_id, resource_group_name, project_name, api_version, accept_language=None) -> web.Response:
    """Get a list of VMware collector.

    Get a list of VMware collector.

    :param subscription_id: Azure Subscription Id in which project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that project is part of.
    :type resource_group_name: str
    :param project_name: Name of the Azure Migrate project.
    :type project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)
