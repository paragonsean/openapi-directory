from typing import List, Dict
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.applications import Applications
from openapi_server.models.configuration import Configuration
from openapi_server.models.configuration_profile import ConfigurationProfile
from openapi_server.models.configuration_profiles import ConfigurationProfiles
from openapi_server.models.create_application_request import CreateApplicationRequest
from openapi_server.models.create_configuration_profile_request import CreateConfigurationProfileRequest
from openapi_server.models.create_deployment_strategy_request import CreateDeploymentStrategyRequest
from openapi_server.models.create_environment_request import CreateEnvironmentRequest
from openapi_server.models.create_extension_association_request import CreateExtensionAssociationRequest
from openapi_server.models.create_extension_request import CreateExtensionRequest
from openapi_server.models.create_hosted_configuration_version_request import CreateHostedConfigurationVersionRequest
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_strategies import DeploymentStrategies
from openapi_server.models.deployment_strategy import DeploymentStrategy
from openapi_server.models.deployments import Deployments
from openapi_server.models.environment import Environment
from openapi_server.models.environments import Environments
from openapi_server.models.extension import Extension
from openapi_server.models.extension_association import ExtensionAssociation
from openapi_server.models.extension_associations import ExtensionAssociations
from openapi_server.models.extensions import Extensions
from openapi_server.models.hosted_configuration_version import HostedConfigurationVersion
from openapi_server.models.hosted_configuration_versions import HostedConfigurationVersions
from openapi_server.models.resource_tags import ResourceTags
from openapi_server.models.start_deployment_request import StartDeploymentRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_application_request import UpdateApplicationRequest
from openapi_server.models.update_configuration_profile_request import UpdateConfigurationProfileRequest
from openapi_server.models.update_deployment_strategy_request import UpdateDeploymentStrategyRequest
from openapi_server.models.update_environment_request import UpdateEnvironmentRequest
from openapi_server.models.update_extension_association_request import UpdateExtensionAssociationRequest
from openapi_server.models.update_extension_request import UpdateExtensionRequest
from openapi_server import util


async def create_application(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_application

    Creates an application. In AppConfig, an application is simply an organizational construct like a folder. This organizational construct has a relationship with some unit of executable code. For example, you could create an application called MyMobileApp to organize and manage configuration data for a mobile application installed by your users.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def create_configuration_profile(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_configuration_profile

    &lt;p&gt;Creates a configuration profile, which is information that enables AppConfig to access the configuration source. Valid configuration sources include the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Configuration data in YAML, JSON, and other formats stored in the AppConfig hosted configuration store&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Configuration data stored as objects in an Amazon Simple Storage Service (Amazon S3) bucket&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Pipelines stored in CodePipeline&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Secrets stored in Secrets Manager&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Standard and secure string parameters stored in Amazon Web Services Systems Manager Parameter Store&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Configuration data in SSM documents stored in the Systems Manager document store&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;A configuration profile includes the following information:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The URI location of the configuration data.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Identity and Access Management (IAM) role that provides access to the configuration data.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A validator for the configuration data. Available validators include either a JSON Schema or an Amazon Web Services Lambda function.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html\&quot;&gt;Create a Configuration and a Configuration Profile&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.&lt;/p&gt;

    :param application_id: The application ID.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateConfigurationProfileRequest.from_dict(body)
    return web.Response(status=200)


async def create_deployment_strategy(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_deployment_strategy

    Creates a deployment strategy that defines important criteria for rolling out your configuration to the designated targets. A deployment strategy includes the overall duration required, a percentage of targets to receive the deployment during each interval, an algorithm that defines how percentage grows, and bake time.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateDeploymentStrategyRequest.from_dict(body)
    return web.Response(status=200)


async def create_environment(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_environment

    Creates an environment. For each application, you define one or more environments. An environment is a deployment group of AppConfig targets, such as applications in a &lt;code&gt;Beta&lt;/code&gt; or &lt;code&gt;Production&lt;/code&gt; environment. You can also define environments for application subcomponents such as the &lt;code&gt;Web&lt;/code&gt;, &lt;code&gt;Mobile&lt;/code&gt; and &lt;code&gt;Back-end&lt;/code&gt; components for your application. You can configure Amazon CloudWatch alarms for each environment. The system monitors alarms during a configuration deployment. If an alarm is triggered, the system rolls back the configuration.

    :param application_id: The application ID.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateEnvironmentRequest.from_dict(body)
    return web.Response(status=200)


async def create_extension(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, latest_version_number=None) -> web.Response:
    """create_extension

    &lt;p&gt;Creates an AppConfig extension. An extension augments your ability to inject logic or behavior at different points during the AppConfig workflow of creating or deploying a configuration.&lt;/p&gt; &lt;p&gt;You can create your own extensions or use the Amazon Web Services authored extensions provided by AppConfig. For most use cases, to create your own extension, you must create an Lambda function to perform any computation and processing defined in the extension. For more information about extensions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html\&quot;&gt;Working with AppConfig extensions&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param latest_version_number: You can omit this field when you create an extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field.
    :type latest_version_number: int

    """
    body = CreateExtensionRequest.from_dict(body)
    return web.Response(status=200)


async def create_extension_association(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_extension_association

    When you create an extension or configure an Amazon Web Services authored extension, you associate the extension with an AppConfig application, environment, or configuration profile. For example, you can choose to run the &lt;code&gt;AppConfig deployment events to Amazon SNS&lt;/code&gt; Amazon Web Services authored extension and receive notifications on an Amazon SNS topic anytime a configuration deployment is started for a specific application. Defining which extension to associate with an AppConfig resource is called an &lt;i&gt;extension association&lt;/i&gt;. An extension association is a specified relationship between an extension and an AppConfig resource, such as an application or a configuration profile. For more information about extensions and associations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html\&quot;&gt;Working with AppConfig extensions&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateExtensionAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def create_hosted_configuration_version(request: web.Request, application_id, configuration_profile_id, content_type, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, description=None, latest_version_number=None, version_label=None) -> web.Response:
    """create_hosted_configuration_version

    Creates a new configuration in the AppConfig hosted configuration store.

    :param application_id: The application ID.
    :type application_id: str
    :param configuration_profile_id: The configuration profile ID.
    :type configuration_profile_id: str
    :param content_type: A standard MIME type describing the format of the configuration content. For more information, see &lt;a href&#x3D;\&quot;https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17\&quot;&gt;Content-Type&lt;/a&gt;.
    :type content_type: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param description: A description of the configuration.
    :type description: str
    :param latest_version_number: An optional locking token used to prevent race conditions from overwriting configuration updates when creating a new version. To ensure your data is not overwritten when creating multiple hosted configuration versions in rapid succession, specify the version number of the latest hosted configuration version.
    :type latest_version_number: int
    :param version_label: An optional, user-defined label for the AppConfig hosted configuration version. This value must contain at least one non-numeric character. For example, \&quot;v2.2.0\&quot;.
    :type version_label: str

    """
    body = CreateHostedConfigurationVersionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_application(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_application

    Deletes an application. Deleting an application does not delete a configuration from a host.

    :param application_id: The ID of the application to delete.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_configuration_profile(request: web.Request, application_id, configuration_profile_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_configuration_profile

    Deletes a configuration profile. Deleting a configuration profile does not delete a configuration from a host.

    :param application_id: The application ID that includes the configuration profile you want to delete.
    :type application_id: str
    :param configuration_profile_id: The ID of the configuration profile you want to delete.
    :type configuration_profile_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_deployment_strategy(request: web.Request, deployment_strategy_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_deployment_strategy

    Deletes a deployment strategy. Deleting a deployment strategy does not delete a configuration from a host.

    :param deployment_strategy_id: The ID of the deployment strategy you want to delete.
    :type deployment_strategy_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_environment(request: web.Request, application_id, environment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_environment

    Deletes an environment. Deleting an environment does not delete a configuration from a host.

    :param application_id: The application ID that includes the environment that you want to delete.
    :type application_id: str
    :param environment_id: The ID of the environment that you want to delete.
    :type environment_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_extension(request: web.Request, extension_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version=None) -> web.Response:
    """delete_extension

    Deletes an AppConfig extension. You must delete all associations to an extension before you delete the extension.

    :param extension_identifier: The name, ID, or Amazon Resource Name (ARN) of the extension you want to delete.
    :type extension_identifier: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version: A specific version of an extension to delete. If omitted, the highest version is deleted.
    :type version: int

    """
    return web.Response(status=200)


async def delete_extension_association(request: web.Request, extension_association_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_extension_association

    Deletes an extension association. This action doesn&#39;t delete extensions defined in the association.

    :param extension_association_id: The ID of the extension association to delete.
    :type extension_association_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_hosted_configuration_version(request: web.Request, application_id, configuration_profile_id, version_number, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_hosted_configuration_version

    Deletes a version of a configuration from the AppConfig hosted configuration store.

    :param application_id: The application ID.
    :type application_id: str
    :param configuration_profile_id: The configuration profile ID.
    :type configuration_profile_id: str
    :param version_number: The versions number to delete.
    :type version_number: int
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_application(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_application

    Retrieves information about an application.

    :param application_id: The ID of the application you want to get.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_configuration(request: web.Request, application, environment, configuration, client_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_configuration_version=None) -> web.Response:
    """get_configuration

    &lt;p&gt;(Deprecated) Retrieves the latest deployed configuration.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Note the following important information.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This API action is deprecated. Calls to receive configuration data should use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.html\&quot;&gt;StartConfigurationSession&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html\&quot;&gt;GetLatestConfiguration&lt;/a&gt; APIs instead. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GetConfiguration&lt;/code&gt; is a priced call. For more information, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/systems-manager/pricing/\&quot;&gt;Pricing&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/important&gt;

    :param application: The application to get. Specify either the application name or the application ID.
    :type application: str
    :param environment: The environment to get. Specify either the environment name or the environment ID.
    :type environment: str
    :param configuration: The configuration to get. Specify either the configuration name or the configuration ID.
    :type configuration: str
    :param client_id: The clientId parameter in the following command is a unique, user-specified ID to identify the client for the configuration. This ID enables AppConfig to deploy the configuration in intervals, as defined in the deployment strategy. 
    :type client_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param client_configuration_version: &lt;p&gt;The configuration version returned in the most recent &lt;code&gt;GetConfiguration&lt;/code&gt; response.&lt;/p&gt; &lt;important&gt; &lt;p&gt;AppConfig uses the value of the &lt;code&gt;ClientConfigurationVersion&lt;/code&gt; parameter to identify the configuration version on your clients. If you don’t send &lt;code&gt;ClientConfigurationVersion&lt;/code&gt; with each call to &lt;code&gt;GetConfiguration&lt;/code&gt;, your clients receive the current configuration. You are charged each time your clients receive a configuration.&lt;/p&gt; &lt;p&gt;To avoid excess charges, we recommend you use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/StartConfigurationSession.html\&quot;&gt;StartConfigurationSession&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/GetLatestConfiguration.html\&quot;&gt;GetLatestConfiguration&lt;/a&gt; APIs, which track the client configuration version on your behalf. If you choose to continue using &lt;code&gt;GetConfiguration&lt;/code&gt;, we recommend that you include the &lt;code&gt;ClientConfigurationVersion&lt;/code&gt; value with every call to &lt;code&gt;GetConfiguration&lt;/code&gt;. The value to use for &lt;code&gt;ClientConfigurationVersion&lt;/code&gt; comes from the &lt;code&gt;ConfigurationVersion&lt;/code&gt; attribute returned by &lt;code&gt;GetConfiguration&lt;/code&gt; when there is new or updated data, and should be saved for subsequent calls to &lt;code&gt;GetConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about working with configurations, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration.html\&quot;&gt;Retrieving the Configuration&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.&lt;/p&gt;
    :type client_configuration_version: str

    """
    return web.Response(status=200)


async def get_configuration_profile(request: web.Request, application_id, configuration_profile_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_configuration_profile

    Retrieves information about a configuration profile.

    :param application_id: The ID of the application that includes the configuration profile you want to get.
    :type application_id: str
    :param configuration_profile_id: The ID of the configuration profile that you want to get.
    :type configuration_profile_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_deployment(request: web.Request, application_id, environment_id, deployment_number, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_deployment

    Retrieves information about a configuration deployment.

    :param application_id: The ID of the application that includes the deployment you want to get. 
    :type application_id: str
    :param environment_id: The ID of the environment that includes the deployment you want to get. 
    :type environment_id: str
    :param deployment_number: The sequence number of the deployment.
    :type deployment_number: int
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_deployment_strategy(request: web.Request, deployment_strategy_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_deployment_strategy

    Retrieves information about a deployment strategy. A deployment strategy defines important criteria for rolling out your configuration to the designated targets. A deployment strategy includes the overall duration required, a percentage of targets to receive the deployment during each interval, an algorithm that defines how percentage grows, and bake time.

    :param deployment_strategy_id: The ID of the deployment strategy to get.
    :type deployment_strategy_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_environment(request: web.Request, application_id, environment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_environment

    Retrieves information about an environment. An environment is a deployment group of AppConfig applications, such as applications in a &lt;code&gt;Production&lt;/code&gt; environment or in an &lt;code&gt;EU_Region&lt;/code&gt; environment. Each configuration deployment targets an environment. You can enable one or more Amazon CloudWatch alarms for an environment. If an alarm is triggered during a deployment, AppConfig roles back the configuration.

    :param application_id: The ID of the application that includes the environment you want to get.
    :type application_id: str
    :param environment_id: The ID of the environment that you want to get.
    :type environment_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_extension(request: web.Request, extension_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, version_number=None) -> web.Response:
    """get_extension

    Returns information about an AppConfig extension.

    :param extension_identifier: The name, the ID, or the Amazon Resource Name (ARN) of the extension.
    :type extension_identifier: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param version_number: The extension version number. If no version number was defined, AppConfig uses the highest version.
    :type version_number: int

    """
    return web.Response(status=200)


async def get_extension_association(request: web.Request, extension_association_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_extension_association

    Returns information about an AppConfig extension association. For more information about extensions and associations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html\&quot;&gt;Working with AppConfig extensions&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.

    :param extension_association_id: The extension association ID to get.
    :type extension_association_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_hosted_configuration_version(request: web.Request, application_id, configuration_profile_id, version_number, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_hosted_configuration_version

    Retrieves information about a specific configuration version.

    :param application_id: The application ID.
    :type application_id: str
    :param configuration_profile_id: The configuration profile ID.
    :type configuration_profile_id: str
    :param version_number: The version.
    :type version_number: int
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_applications(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_applications

    Lists all applications in your Amazon Web Services account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
    :type max_results: int
    :param next_token: A token to start the list. Next token is a pagination token generated by AppConfig to describe what page the previous List call ended on. For the first List request, the nextToken should not be set. On subsequent calls, the nextToken parameter should be set to the previous responses nextToken value. Use this token to get the next set of results. 
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_configuration_profiles(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, type=None, max_results2=None, next_token2=None) -> web.Response:
    """list_configuration_profiles

    Lists the configuration profiles for an application.

    :param application_id: The application ID.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
    :type max_results: int
    :param next_token: A token to start the list. Use this token to get the next set of results.
    :type next_token: str
    :param type: A filter based on the type of configurations that the configuration profile contains. A configuration can be a feature flag or a freeform configuration.
    :type type: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_deployment_strategies(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_deployment_strategies

    Lists deployment strategies.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
    :type max_results: int
    :param next_token: A token to start the list. Use this token to get the next set of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_deployments(request: web.Request, application_id, environment_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_deployments

    Lists the deployments for an environment in descending deployment number order.

    :param application_id: The application ID.
    :type application_id: str
    :param environment_id: The environment ID.
    :type environment_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of items that may be returned for this call. If there are items that have not yet been returned, the response will include a non-null &lt;code&gt;NextToken&lt;/code&gt; that you can provide in a subsequent call to get the next set of results.
    :type max_results: int
    :param next_token: The token returned by a prior call to this operation indicating the next set of results to be returned. If not specified, the operation will return the first set of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_environments(request: web.Request, application_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_environments

    Lists the environments for an application.

    :param application_id: The application ID.
    :type application_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
    :type max_results: int
    :param next_token: A token to start the list. Use this token to get the next set of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_extension_associations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, resource_identifier=None, extension_identifier=None, extension_version_number=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_extension_associations

    Lists all AppConfig extension associations in the account. For more information about extensions and associations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html\&quot;&gt;Working with AppConfig extensions&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param resource_identifier: The ARN of an application, configuration profile, or environment.
    :type resource_identifier: str
    :param extension_identifier: The name, the ID, or the Amazon Resource Name (ARN) of the extension.
    :type extension_identifier: str
    :param extension_version_number: The version number for the extension defined in the association.
    :type extension_version_number: int
    :param max_results: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
    :type max_results: int
    :param next_token: A token to start the list. Use this token to get the next set of results or pass null to get the first set of results. 
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_extensions(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, name=None, max_results2=None, next_token2=None) -> web.Response:
    """list_extensions

    Lists all custom and Amazon Web Services authored AppConfig extensions in the account. For more information about extensions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html\&quot;&gt;Working with AppConfig extensions&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
    :type max_results: int
    :param next_token: A token to start the list. Use this token to get the next set of results. 
    :type next_token: str
    :param name: The extension name.
    :type name: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_hosted_configuration_versions(request: web.Request, application_id, configuration_profile_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, version_label=None, max_results2=None, next_token2=None) -> web.Response:
    """list_hosted_configuration_versions

    Lists configurations stored in the AppConfig hosted configuration store by version.

    :param application_id: The application ID.
    :type application_id: str
    :param configuration_profile_id: The configuration profile ID.
    :type configuration_profile_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
    :type max_results: int
    :param next_token: A token to start the list. Use this token to get the next set of results. 
    :type next_token: str
    :param version_label: An optional filter that can be used to specify the version label of an AppConfig hosted configuration version. This parameter supports filtering by prefix using a wildcard, for example \&quot;v2*\&quot;. If you don&#39;t specify an asterisk at the end of the value, only an exact match is returned.
    :type version_label: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Retrieves the list of key-value tags assigned to the resource.

    :param resource_arn: The resource ARN.
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def start_deployment(request: web.Request, application_id, environment_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_deployment

    Starts a deployment.

    :param application_id: The application ID.
    :type application_id: str
    :param environment_id: The environment ID.
    :type environment_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartDeploymentRequest.from_dict(body)
    return web.Response(status=200)


async def stop_deployment(request: web.Request, application_id, environment_id, deployment_number, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_deployment

    Stops a deployment. This API action works only on deployments that have a status of &lt;code&gt;DEPLOYING&lt;/code&gt;. This action moves the deployment to a status of &lt;code&gt;ROLLED_BACK&lt;/code&gt;.

    :param application_id: The application ID.
    :type application_id: str
    :param environment_id: The environment ID.
    :type environment_id: str
    :param deployment_number: The sequence number of the deployment.
    :type deployment_number: int
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Assigns metadata to an AppConfig resource. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define. You can specify a maximum of 50 tags for a resource.

    :param resource_arn: The ARN of the resource for which to retrieve tags.
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Deletes a tag key and value from an AppConfig resource.

    :param resource_arn: The ARN of the resource for which to remove tags.
    :type resource_arn: str
    :param tag_keys: The tag keys to delete.
    :type tag_keys: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def update_application(request: web.Request, application_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_application

    Updates an application.

    :param application_id: The application ID.
    :type application_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def update_configuration_profile(request: web.Request, application_id, configuration_profile_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_configuration_profile

    Updates a configuration profile.

    :param application_id: The application ID.
    :type application_id: str
    :param configuration_profile_id: The ID of the configuration profile.
    :type configuration_profile_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateConfigurationProfileRequest.from_dict(body)
    return web.Response(status=200)


async def update_deployment_strategy(request: web.Request, deployment_strategy_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_deployment_strategy

    Updates a deployment strategy.

    :param deployment_strategy_id: The deployment strategy ID.
    :type deployment_strategy_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateDeploymentStrategyRequest.from_dict(body)
    return web.Response(status=200)


async def update_environment(request: web.Request, application_id, environment_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_environment

    Updates an environment.

    :param application_id: The application ID.
    :type application_id: str
    :param environment_id: The environment ID.
    :type environment_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateEnvironmentRequest.from_dict(body)
    return web.Response(status=200)


async def update_extension(request: web.Request, extension_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_extension

    Updates an AppConfig extension. For more information about extensions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html\&quot;&gt;Working with AppConfig extensions&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.

    :param extension_identifier: The name, the ID, or the Amazon Resource Name (ARN) of the extension.
    :type extension_identifier: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateExtensionRequest.from_dict(body)
    return web.Response(status=200)


async def update_extension_association(request: web.Request, extension_association_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_extension_association

    Updates an association. For more information about extensions and associations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html\&quot;&gt;Working with AppConfig extensions&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.

    :param extension_association_id: The system-generated ID for the association.
    :type extension_association_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateExtensionAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def validate_configuration(request: web.Request, application_id, configuration_profile_id, configuration_version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """validate_configuration

    Uses the validators in a configuration profile to validate a configuration.

    :param application_id: The application ID.
    :type application_id: str
    :param configuration_profile_id: The configuration profile ID.
    :type configuration_profile_id: str
    :param configuration_version: The version of the configuration to validate.
    :type configuration_version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)
