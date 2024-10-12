from typing import List, Dict
from aiohttp import web

from openapi_server.models.abort_environment_update_message import AbortEnvironmentUpdateMessage
from openapi_server.models.application_description_message import ApplicationDescriptionMessage
from openapi_server.models.application_descriptions_message import ApplicationDescriptionsMessage
from openapi_server.models.application_resource_lifecycle_description_message import ApplicationResourceLifecycleDescriptionMessage
from openapi_server.models.application_version_description_message import ApplicationVersionDescriptionMessage
from openapi_server.models.application_version_descriptions_message import ApplicationVersionDescriptionsMessage
from openapi_server.models.apply_environment_managed_action_request import ApplyEnvironmentManagedActionRequest
from openapi_server.models.apply_environment_managed_action_result import ApplyEnvironmentManagedActionResult
from openapi_server.models.associate_environment_operations_role_message import AssociateEnvironmentOperationsRoleMessage
from openapi_server.models.check_dns_availability_message import CheckDNSAvailabilityMessage
from openapi_server.models.check_dns_availability_result_message import CheckDNSAvailabilityResultMessage
from openapi_server.models.compose_environments_message import ComposeEnvironmentsMessage
from openapi_server.models.configuration_option_setting import ConfigurationOptionSetting
from openapi_server.models.configuration_options_description import ConfigurationOptionsDescription
from openapi_server.models.configuration_settings_description import ConfigurationSettingsDescription
from openapi_server.models.configuration_settings_descriptions import ConfigurationSettingsDescriptions
from openapi_server.models.configuration_settings_validation_messages import ConfigurationSettingsValidationMessages
from openapi_server.models.create_application_message import CreateApplicationMessage
from openapi_server.models.create_application_version_message import CreateApplicationVersionMessage
from openapi_server.models.create_configuration_template_message import CreateConfigurationTemplateMessage
from openapi_server.models.create_environment_message import CreateEnvironmentMessage
from openapi_server.models.create_platform_version_request import CreatePlatformVersionRequest
from openapi_server.models.create_platform_version_result import CreatePlatformVersionResult
from openapi_server.models.create_storage_location_result_message import CreateStorageLocationResultMessage
from openapi_server.models.delete_application_message import DeleteApplicationMessage
from openapi_server.models.delete_application_version_message import DeleteApplicationVersionMessage
from openapi_server.models.delete_configuration_template_message import DeleteConfigurationTemplateMessage
from openapi_server.models.delete_environment_configuration_message import DeleteEnvironmentConfigurationMessage
from openapi_server.models.delete_platform_version_request import DeletePlatformVersionRequest
from openapi_server.models.delete_platform_version_result import DeletePlatformVersionResult
from openapi_server.models.describe_account_attributes_result import DescribeAccountAttributesResult
from openapi_server.models.describe_application_versions_message import DescribeApplicationVersionsMessage
from openapi_server.models.describe_applications_message import DescribeApplicationsMessage
from openapi_server.models.describe_configuration_options_message import DescribeConfigurationOptionsMessage
from openapi_server.models.describe_configuration_settings_message import DescribeConfigurationSettingsMessage
from openapi_server.models.describe_environment_health_request import DescribeEnvironmentHealthRequest
from openapi_server.models.describe_environment_health_result import DescribeEnvironmentHealthResult
from openapi_server.models.describe_environment_managed_action_history_request import DescribeEnvironmentManagedActionHistoryRequest
from openapi_server.models.describe_environment_managed_action_history_result import DescribeEnvironmentManagedActionHistoryResult
from openapi_server.models.describe_environment_managed_actions_request import DescribeEnvironmentManagedActionsRequest
from openapi_server.models.describe_environment_managed_actions_result import DescribeEnvironmentManagedActionsResult
from openapi_server.models.describe_environment_resources_message import DescribeEnvironmentResourcesMessage
from openapi_server.models.describe_environments_message import DescribeEnvironmentsMessage
from openapi_server.models.describe_events_message import DescribeEventsMessage
from openapi_server.models.describe_instances_health_request import DescribeInstancesHealthRequest
from openapi_server.models.describe_instances_health_result import DescribeInstancesHealthResult
from openapi_server.models.describe_platform_version_request import DescribePlatformVersionRequest
from openapi_server.models.describe_platform_version_result import DescribePlatformVersionResult
from openapi_server.models.disassociate_environment_operations_role_message import DisassociateEnvironmentOperationsRoleMessage
from openapi_server.models.environment_description import EnvironmentDescription
from openapi_server.models.environment_descriptions_message import EnvironmentDescriptionsMessage
from openapi_server.models.environment_health_attribute import EnvironmentHealthAttribute
from openapi_server.models.environment_resource_descriptions_message import EnvironmentResourceDescriptionsMessage
from openapi_server.models.event_descriptions_message import EventDescriptionsMessage
from openapi_server.models.get_create_application_resource_lifecycle_config_parameter import GETCreateApplicationResourceLifecycleConfigParameter
from openapi_server.models.get_create_application_version_build_configuration_parameter import GETCreateApplicationVersionBuildConfigurationParameter
from openapi_server.models.get_create_application_version_source_build_information_parameter import GETCreateApplicationVersionSourceBuildInformationParameter
from openapi_server.models.get_create_application_version_source_bundle_parameter import GETCreateApplicationVersionSourceBundleParameter
from openapi_server.models.get_create_configuration_template_source_configuration_parameter import GETCreateConfigurationTemplateSourceConfigurationParameter
from openapi_server.models.get_create_environment_tier_parameter import GETCreateEnvironmentTierParameter
from openapi_server.models.instances_health_attribute import InstancesHealthAttribute
from openapi_server.models.list_available_solution_stacks_result_message import ListAvailableSolutionStacksResultMessage
from openapi_server.models.list_platform_branches_request import ListPlatformBranchesRequest
from openapi_server.models.list_platform_branches_result import ListPlatformBranchesResult
from openapi_server.models.list_platform_versions_request import ListPlatformVersionsRequest
from openapi_server.models.list_platform_versions_result import ListPlatformVersionsResult
from openapi_server.models.list_tags_for_resource_message import ListTagsForResourceMessage
from openapi_server.models.option_specification import OptionSpecification
from openapi_server.models.platform_filter import PlatformFilter
from openapi_server.models.rebuild_environment_message import RebuildEnvironmentMessage
from openapi_server.models.request_environment_info_message import RequestEnvironmentInfoMessage
from openapi_server.models.resource_tags_description_message import ResourceTagsDescriptionMessage
from openapi_server.models.restart_app_server_message import RestartAppServerMessage
from openapi_server.models.retrieve_environment_info_message import RetrieveEnvironmentInfoMessage
from openapi_server.models.retrieve_environment_info_result_message import RetrieveEnvironmentInfoResultMessage
from openapi_server.models.search_filter import SearchFilter
from openapi_server.models.swap_environment_cnames_message import SwapEnvironmentCNAMEsMessage
from openapi_server.models.tag import Tag
from openapi_server.models.terminate_environment_message import TerminateEnvironmentMessage
from openapi_server.models.update_application_message import UpdateApplicationMessage
from openapi_server.models.update_application_resource_lifecycle_message import UpdateApplicationResourceLifecycleMessage
from openapi_server.models.update_application_version_message import UpdateApplicationVersionMessage
from openapi_server.models.update_configuration_template_message import UpdateConfigurationTemplateMessage
from openapi_server.models.update_environment_message import UpdateEnvironmentMessage
from openapi_server.models.update_tags_for_resource_message import UpdateTagsForResourceMessage
from openapi_server.models.validate_configuration_settings_message import ValidateConfigurationSettingsMessage
from openapi_server import util


async def g_et_abort_environment_update(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, environment_id=None, environment_name=None) -> web.Response:
    """g_et_abort_environment_update

    Cancels in-progress environment configuration update or application version deployment.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param environment_id: This specifies the ID of the environment with the in-progress update that you want to cancel.
    :type environment_id: str
    :param environment_name: This specifies the name of the environment with the in-progress update that you want to cancel.
    :type environment_name: str

    """
    return web.Response(status=200)


async def g_et_apply_environment_managed_action(request: web.Request, action_id, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, environment_name=None, environment_id=None) -> web.Response:
    """g_et_apply_environment_managed_action

    Applies a scheduled managed action immediately. A managed action can be applied only if its status is &lt;code&gt;Scheduled&lt;/code&gt;. Get the status and action ID of a managed action with &lt;a&gt;DescribeEnvironmentManagedActions&lt;/a&gt;.

    :param action_id: The action ID of the scheduled managed action to execute.
    :type action_id: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param environment_name: The name of the target environment.
    :type environment_name: str
    :param environment_id: The environment ID of the target environment.
    :type environment_id: str

    """
    return web.Response(status=200)


async def g_et_associate_environment_operations_role(request: web.Request, environment_name, operations_role, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_associate_environment_operations_role

    Add or change the operations role used by an environment. After this call is made, Elastic Beanstalk uses the associated operations role for permissions to downstream services during subsequent calls acting on this environment. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/iam-operationsrole.html\&quot;&gt;Operations roles&lt;/a&gt; in the &lt;i&gt;AWS Elastic Beanstalk Developer Guide&lt;/i&gt;.

    :param environment_name: The name of the environment to which to set the operations role.
    :type environment_name: str
    :param operations_role: The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment&#39;s operations role.
    :type operations_role: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_check_dns_availability(request: web.Request, cname_prefix, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_check_dns_availability

    Checks if the specified CNAME is available.

    :param cname_prefix: The prefix used when this CNAME is reserved.
    :type cname_prefix: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_compose_environments(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, application_name=None, group_name=None, version_labels=None) -> web.Response:
    """g_et_compose_environments

    Create or update a group of environments that each run a separate component of a single application. Takes a list of version labels that specify application source bundles for each of the environments to create or update. The name of each environment and other required information must be included in the source bundles in an environment manifest named &lt;code&gt;env.yaml&lt;/code&gt;. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-mgmt-compose.html\&quot;&gt;Compose Environments&lt;/a&gt; for details.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param application_name: The name of the application to which the specified source bundles belong.
    :type application_name: str
    :param group_name: The name of the group to which the target environments belong. Specify a group name only if the environment name defined in each target environment&#39;s manifest ends with a + (plus) character. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html\&quot;&gt;Environment Manifest (env.yaml)&lt;/a&gt; for details.
    :type group_name: str
    :param version_labels: A list of version labels, specifying one or more application source bundles that belong to the target application. Each source bundle must include an environment manifest that specifies the name of the environment and the name of the solution stack to use, and optionally can specify environment links to create.
    :type version_labels: List[str]

    """
    return web.Response(status=200)


async def g_et_create_application(request: web.Request, application_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, description=None, resource_lifecycle_config=None, tags=None) -> web.Response:
    """g_et_create_application

    Creates an application that has one configuration template named &lt;code&gt;default&lt;/code&gt; and no application versions.

    :param application_name: The name of the application. Must be unique within your account.
    :type application_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param description: Your description of the application.
    :type description: str
    :param resource_lifecycle_config: Specifies an application resource lifecycle configuration to prevent your application from accumulating too many versions.
    :type resource_lifecycle_config: dict | bytes
    :param tags: &lt;p&gt;Specifies the tags applied to the application.&lt;/p&gt; &lt;p&gt;Elastic Beanstalk applies these tags only to the application. Environments that you create in the application don&#39;t inherit the tags.&lt;/p&gt;
    :type tags: list | bytes

    """
    resource_lifecycle_config = .from_dict(resource_lifecycle_config)
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_application_version(request: web.Request, application_name, version_label, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, description=None, source_build_information=None, source_bundle=None, build_configuration=None, auto_create_application=None, process=None, tags=None) -> web.Response:
    """g_et_create_application_version

    &lt;p&gt;Creates an application version for the specified application. You can create an application version from a source bundle in Amazon S3, a commit in AWS CodeCommit, or the output of an AWS CodeBuild build as follows:&lt;/p&gt; &lt;p&gt;Specify a commit in an AWS CodeCommit repository with &lt;code&gt;SourceBuildInformation&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Specify a build in an AWS CodeBuild with &lt;code&gt;SourceBuildInformation&lt;/code&gt; and &lt;code&gt;BuildConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Specify a source bundle in S3 with &lt;code&gt;SourceBundle&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Omit both &lt;code&gt;SourceBuildInformation&lt;/code&gt; and &lt;code&gt;SourceBundle&lt;/code&gt; to use the default sample application.&lt;/p&gt; &lt;note&gt; &lt;p&gt;After you create an application version with a specified Amazon S3 bucket and key location, you can&#39;t change that Amazon S3 location. If you change the Amazon S3 location, you receive an exception when you attempt to launch an environment from the application version.&lt;/p&gt; &lt;/note&gt;

    :param application_name:  The name of the application. If no application is found with this name, and &lt;code&gt;AutoCreateApplication&lt;/code&gt; is &lt;code&gt;false&lt;/code&gt;, returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error. 
    :type application_name: str
    :param version_label: &lt;p&gt;A label identifying this version.&lt;/p&gt; &lt;p&gt;Constraint: Must be unique per application. If an application version already exists with this label for the specified application, AWS Elastic Beanstalk returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error. &lt;/p&gt;
    :type version_label: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param description: A description of this application version.
    :type description: str
    :param source_build_information: Specify a commit in an AWS CodeCommit Git repository to use as the source code for the application version.
    :type source_build_information: dict | bytes
    :param source_bundle: &lt;p&gt;The Amazon S3 bucket and key that identify the location of the source bundle for this version.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The Amazon S3 bucket must be in the same region as the environment.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Specify a source bundle in S3 or a commit in an AWS CodeCommit repository (with &lt;code&gt;SourceBuildInformation&lt;/code&gt;), but not both. If neither &lt;code&gt;SourceBundle&lt;/code&gt; nor &lt;code&gt;SourceBuildInformation&lt;/code&gt; are provided, Elastic Beanstalk uses a sample application.&lt;/p&gt;
    :type source_bundle: dict | bytes
    :param build_configuration: Settings for an AWS CodeBuild build.
    :type build_configuration: dict | bytes
    :param auto_create_application: Set to &lt;code&gt;true&lt;/code&gt; to create an application with the specified name if it doesn&#39;t already exist.
    :type auto_create_application: bool
    :param process: &lt;p&gt;Pre-processes and validates the environment manifest (&lt;code&gt;env.yaml&lt;/code&gt;) and configuration files (&lt;code&gt;*.config&lt;/code&gt; files in the &lt;code&gt;.ebextensions&lt;/code&gt; folder) in the source bundle. Validating configuration files can identify issues prior to deploying the application version to an environment.&lt;/p&gt; &lt;p&gt;You must turn processing on for application versions that you create using AWS CodeBuild or AWS CodeCommit. For application versions built from a source bundle in Amazon S3, processing is optional.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;Process&lt;/code&gt; option validates Elastic Beanstalk configuration files. It doesn&#39;t validate your application&#39;s configuration files, like proxy server or Docker configuration.&lt;/p&gt; &lt;/note&gt;
    :type process: bool
    :param tags: &lt;p&gt;Specifies the tags applied to the application version.&lt;/p&gt; &lt;p&gt;Elastic Beanstalk applies these tags only to the application version. Environments that use the application version don&#39;t inherit the tags.&lt;/p&gt;
    :type tags: list | bytes

    """
    source_build_information = .from_dict(source_build_information)
    source_bundle = .from_dict(source_bundle)
    build_configuration = .from_dict(build_configuration)
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_configuration_template(request: web.Request, application_name, template_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, solution_stack_name=None, platform_arn=None, source_configuration=None, environment_id=None, description=None, option_settings=None, tags=None) -> web.Response:
    """g_et_create_configuration_template

    &lt;p&gt;Creates an AWS Elastic Beanstalk configuration template, associated with a specific Elastic Beanstalk application. You define application configuration settings in a configuration template. You can then use the configuration template to deploy different versions of the application with the same configuration settings.&lt;/p&gt; &lt;p&gt;Templates aren&#39;t associated with any environment. The &lt;code&gt;EnvironmentName&lt;/code&gt; response element is always &lt;code&gt;null&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Related Topics&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeConfigurationOptions&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeConfigurationSettings&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListAvailableSolutionStacks&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param application_name: The name of the Elastic Beanstalk application to associate with this configuration template.
    :type application_name: str
    :param template_name: &lt;p&gt;The name of the configuration template.&lt;/p&gt; &lt;p&gt;Constraint: This name must be unique per application.&lt;/p&gt;
    :type template_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param solution_stack_name: &lt;p&gt;The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, &lt;code&gt;64bit Amazon Linux 2013.09 running Tomcat 7 Java 7&lt;/code&gt;. A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html\&quot;&gt;Supported Platforms&lt;/a&gt; in the &lt;i&gt;AWS Elastic Beanstalk Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You must specify &lt;code&gt;SolutionStackName&lt;/code&gt; if you don&#39;t specify &lt;code&gt;PlatformArn&lt;/code&gt;, &lt;code&gt;EnvironmentId&lt;/code&gt;, or &lt;code&gt;SourceConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks.html\&quot;&gt; &lt;code&gt;ListAvailableSolutionStacks&lt;/code&gt; &lt;/a&gt; API to obtain a list of available solution stacks.&lt;/p&gt;
    :type solution_stack_name: str
    :param platform_arn: &lt;p&gt;The Amazon Resource Name (ARN) of the custom platform. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html\&quot;&gt; Custom Platforms&lt;/a&gt; in the &lt;i&gt;AWS Elastic Beanstalk Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you specify &lt;code&gt;PlatformArn&lt;/code&gt;, then don&#39;t specify &lt;code&gt;SolutionStackName&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;
    :type platform_arn: str
    :param source_configuration: &lt;p&gt;An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.&lt;/p&gt; &lt;p&gt;Values specified in &lt;code&gt;OptionSettings&lt;/code&gt; override any values obtained from the &lt;code&gt;SourceConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You must specify &lt;code&gt;SourceConfiguration&lt;/code&gt; if you don&#39;t specify &lt;code&gt;PlatformArn&lt;/code&gt;, &lt;code&gt;EnvironmentId&lt;/code&gt;, or &lt;code&gt;SolutionStackName&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name.&lt;/p&gt;
    :type source_configuration: dict | bytes
    :param environment_id: The ID of an environment whose settings you want to use to create the configuration template. You must specify &lt;code&gt;EnvironmentId&lt;/code&gt; if you don&#39;t specify &lt;code&gt;PlatformArn&lt;/code&gt;, &lt;code&gt;SolutionStackName&lt;/code&gt;, or &lt;code&gt;SourceConfiguration&lt;/code&gt;.
    :type environment_id: str
    :param description: An optional description for this configuration.
    :type description: str
    :param option_settings: Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html\&quot;&gt;Option Values&lt;/a&gt; in the &lt;i&gt;AWS Elastic Beanstalk Developer Guide&lt;/i&gt;.
    :type option_settings: list | bytes
    :param tags: Specifies the tags applied to the configuration template.
    :type tags: list | bytes

    """
    source_configuration = .from_dict(source_configuration)
    option_settings = [ConfigurationOptionSetting.from_dict(d) for d in option_settings]
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_environment(request: web.Request, application_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, environment_name=None, group_name=None, description=None, cname_prefix=None, tier=None, tags=None, version_label=None, template_name=None, solution_stack_name=None, platform_arn=None, option_settings=None, options_to_remove=None, operations_role=None) -> web.Response:
    """g_et_create_environment

    Launches an AWS Elastic Beanstalk environment for the specified application using the specified configuration.

    :param application_name: The name of the application that is associated with this environment.
    :type application_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param environment_name: &lt;p&gt;A unique name for the environment.&lt;/p&gt; &lt;p&gt;Constraint: Must be from 4 to 40 characters in length. The name can contain only letters, numbers, and hyphens. It can&#39;t start or end with a hyphen. This name must be unique within a region in your account. If the specified name already exists in the region, Elastic Beanstalk returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error. &lt;/p&gt; &lt;p&gt;If you don&#39;t specify the &lt;code&gt;CNAMEPrefix&lt;/code&gt; parameter, the environment name becomes part of the CNAME, and therefore part of the visible URL for your application.&lt;/p&gt;
    :type environment_name: str
    :param group_name: The name of the group to which the target environment belongs. Specify a group name only if the environment&#39;s name is specified in an environment manifest and not with the environment name parameter. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html\&quot;&gt;Environment Manifest (env.yaml)&lt;/a&gt; for details.
    :type group_name: str
    :param description: Your description for this environment.
    :type description: str
    :param cname_prefix: If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.
    :type cname_prefix: str
    :param tier: Specifies the tier to use in creating this environment. The environment tier that you choose determines whether Elastic Beanstalk provisions resources to support a web application that handles HTTP(S) requests or a web application that handles background-processing tasks.
    :type tier: dict | bytes
    :param tags: Specifies the tags applied to resources in the environment.
    :type tags: list | bytes
    :param version_label: &lt;p&gt;The name of the application version to deploy.&lt;/p&gt; &lt;p&gt;Default: If not specified, Elastic Beanstalk attempts to deploy the sample application.&lt;/p&gt;
    :type version_label: str
    :param template_name: &lt;p&gt;The name of the Elastic Beanstalk configuration template to use with the environment.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you specify &lt;code&gt;TemplateName&lt;/code&gt;, then don&#39;t specify &lt;code&gt;SolutionStackName&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;
    :type template_name: str
    :param solution_stack_name: &lt;p&gt;The name of an Elastic Beanstalk solution stack (platform version) to use with the environment. If specified, Elastic Beanstalk sets the configuration values to the default values associated with the specified solution stack. For a list of current solution stacks, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html\&quot;&gt;Elastic Beanstalk Supported Platforms&lt;/a&gt; in the &lt;i&gt;AWS Elastic Beanstalk Platforms&lt;/i&gt; guide.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you specify &lt;code&gt;SolutionStackName&lt;/code&gt;, don&#39;t specify &lt;code&gt;PlatformArn&lt;/code&gt; or &lt;code&gt;TemplateName&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;
    :type solution_stack_name: str
    :param platform_arn: &lt;p&gt;The Amazon Resource Name (ARN) of the custom platform to use with the environment. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html\&quot;&gt;Custom Platforms&lt;/a&gt; in the &lt;i&gt;AWS Elastic Beanstalk Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you specify &lt;code&gt;PlatformArn&lt;/code&gt;, don&#39;t specify &lt;code&gt;SolutionStackName&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;
    :type platform_arn: str
    :param option_settings: If specified, AWS Elastic Beanstalk sets the specified configuration options to the requested value in the configuration set for the new environment. These override the values obtained from the solution stack or the configuration template.
    :type option_settings: list | bytes
    :param options_to_remove: A list of custom user-defined configuration options to remove from the configuration set for this new environment.
    :type options_to_remove: list | bytes
    :param operations_role: The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment&#39;s operations role. If specified, Elastic Beanstalk uses the operations role for permissions to downstream services during this call and during subsequent calls acting on this environment. To specify an operations role, you must have the &lt;code&gt;iam:PassRole&lt;/code&gt; permission for the role. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/iam-operationsrole.html\&quot;&gt;Operations roles&lt;/a&gt; in the &lt;i&gt;AWS Elastic Beanstalk Developer Guide&lt;/i&gt;.
    :type operations_role: str

    """
    tier = .from_dict(tier)
    tags = [Tag.from_dict(d) for d in tags]
    option_settings = [ConfigurationOptionSetting.from_dict(d) for d in option_settings]
    options_to_remove = [OptionSpecification.from_dict(d) for d in options_to_remove]
    return web.Response(status=200)


async def g_et_create_platform_version(request: web.Request, platform_name, platform_version, platform_definition_bundle, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, environment_name=None, option_settings=None, tags=None) -> web.Response:
    """g_et_create_platform_version

    Create a new version of your custom platform.

    :param platform_name: The name of your custom platform.
    :type platform_name: str
    :param platform_version: The number, such as 1.0.2, for the new platform version.
    :type platform_version: str
    :param platform_definition_bundle: The location of the platform definition archive in Amazon S3.
    :type platform_definition_bundle: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param environment_name: The name of the builder environment.
    :type environment_name: str
    :param option_settings: The configuration option settings to apply to the builder environment.
    :type option_settings: list | bytes
    :param tags: &lt;p&gt;Specifies the tags applied to the new platform version.&lt;/p&gt; &lt;p&gt;Elastic Beanstalk applies these tags only to the platform version. Environments that you create using the platform version don&#39;t inherit the tags.&lt;/p&gt;
    :type tags: list | bytes

    """
    platform_definition_bundle = .from_dict(platform_definition_bundle)
    option_settings = [ConfigurationOptionSetting.from_dict(d) for d in option_settings]
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_storage_location(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_storage_location

    Creates a bucket in Amazon S3 to store application versions, logs, and other files used by Elastic Beanstalk environments. The Elastic Beanstalk console and EB CLI call this API the first time you create an environment in a region. If the storage location already exists, &lt;code&gt;CreateStorageLocation&lt;/code&gt; still returns the bucket name but does not create a new bucket.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_delete_application(request: web.Request, application_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, terminate_env_by_force=None) -> web.Response:
    """g_et_delete_application

    &lt;p&gt;Deletes the specified application along with all associated versions and configurations. The application versions will not be deleted from your Amazon S3 bucket.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot delete an application that has a running environment.&lt;/p&gt; &lt;/note&gt;

    :param application_name: The name of the application to delete.
    :type application_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param terminate_env_by_force: When set to true, running environments will be terminated before deleting the application.
    :type terminate_env_by_force: bool

    """
    return web.Response(status=200)


async def g_et_delete_application_version(request: web.Request, application_name, version_label, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, delete_source_bundle=None) -> web.Response:
    """g_et_delete_application_version

    &lt;p&gt;Deletes the specified version from the specified application.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot delete an application version that is associated with a running environment.&lt;/p&gt; &lt;/note&gt;

    :param application_name: The name of the application to which the version belongs.
    :type application_name: str
    :param version_label: The label of the version to delete.
    :type version_label: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param delete_source_bundle: Set to &lt;code&gt;true&lt;/code&gt; to delete the source bundle from your storage bucket. Otherwise, the application version is deleted only from Elastic Beanstalk and the source bundle remains in Amazon S3.
    :type delete_source_bundle: bool

    """
    return web.Response(status=200)


async def g_et_delete_configuration_template(request: web.Request, application_name, template_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_configuration_template

    &lt;p&gt;Deletes the specified configuration template.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you launch an environment using a configuration template, the environment gets a copy of the template. You can delete or modify the environment&#39;s copy of the template without affecting the running environment.&lt;/p&gt; &lt;/note&gt;

    :param application_name: The name of the application to delete the configuration template from.
    :type application_name: str
    :param template_name: The name of the configuration template to delete.
    :type template_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_delete_environment_configuration(request: web.Request, application_name, environment_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_environment_configuration

    &lt;p&gt;Deletes the draft configuration associated with the running environment.&lt;/p&gt; &lt;p&gt;Updating a running environment with any configuration changes creates a draft configuration set. You can get the draft configuration using &lt;a&gt;DescribeConfigurationSettings&lt;/a&gt; while the update is in progress or if the update fails. The &lt;code&gt;DeploymentStatus&lt;/code&gt; for the draft configuration indicates whether the deployment is in process or has failed. The draft configuration remains in existence until it is deleted with this action.&lt;/p&gt;

    :param application_name: The name of the application the environment is associated with.
    :type application_name: str
    :param environment_name: The name of the environment to delete the draft configuration from.
    :type environment_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_delete_platform_version(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, platform_arn=None) -> web.Response:
    """g_et_delete_platform_version

    Deletes the specified version of a custom platform.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param platform_arn: The ARN of the version of the custom platform.
    :type platform_arn: str

    """
    return web.Response(status=200)


async def g_et_describe_account_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_account_attributes

    &lt;p&gt;Returns attributes related to AWS Elastic Beanstalk that are associated with the calling AWS account.&lt;/p&gt; &lt;p&gt;The result currently has one set of attributes—resource quotas.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_describe_application_versions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, application_name=None, version_labels=None, max_records=None, next_token=None) -> web.Response:
    """g_et_describe_application_versions

    Retrieve a list of application versions.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param application_name: Specify an application name to show only application versions for that application.
    :type application_name: str
    :param version_labels: Specify a version label to show a specific application version.
    :type version_labels: List[str]
    :param max_records: &lt;p&gt;For a paginated request. Specify a maximum number of application versions to include in each response.&lt;/p&gt; &lt;p&gt;If no &lt;code&gt;MaxRecords&lt;/code&gt; is specified, all available application versions are retrieved in a single response.&lt;/p&gt;
    :type max_records: int
    :param next_token: &lt;p&gt;For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.&lt;/p&gt; &lt;p&gt;If no &lt;code&gt;NextToken&lt;/code&gt; is specified, the first page is retrieved.&lt;/p&gt;
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_describe_applications(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, application_names=None) -> web.Response:
    """g_et_describe_applications

    Returns the descriptions of existing applications.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param application_names: If specified, AWS Elastic Beanstalk restricts the returned descriptions to only include those with the specified names.
    :type application_names: List[str]

    """
    return web.Response(status=200)


async def g_et_describe_configuration_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, application_name=None, template_name=None, environment_name=None, solution_stack_name=None, platform_arn=None, options=None) -> web.Response:
    """g_et_describe_configuration_options

    Describes the configuration options that are used in a particular configuration template or environment, or that a specified solution stack defines. The description includes the values the options, their default values, and an indication of the required action on a running environment if an option value is changed.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param application_name: The name of the application associated with the configuration template or environment. Only needed if you want to describe the configuration options associated with either the configuration template or environment.
    :type application_name: str
    :param template_name: The name of the configuration template whose configuration options you want to describe.
    :type template_name: str
    :param environment_name: The name of the environment whose configuration options you want to describe.
    :type environment_name: str
    :param solution_stack_name: The name of the solution stack whose configuration options you want to describe.
    :type solution_stack_name: str
    :param platform_arn: The ARN of the custom platform.
    :type platform_arn: str
    :param options: If specified, restricts the descriptions to only the specified options.
    :type options: list | bytes

    """
    options = [OptionSpecification.from_dict(d) for d in options]
    return web.Response(status=200)


async def g_et_describe_configuration_settings(request: web.Request, application_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, template_name=None, environment_name=None) -> web.Response:
    """g_et_describe_configuration_settings

    &lt;p&gt;Returns a description of the settings for the specified configuration set, that is, either a configuration template or the configuration set associated with a running environment.&lt;/p&gt; &lt;p&gt;When describing the settings for the configuration set associated with a running environment, it is possible to receive two sets of setting descriptions. One is the deployed configuration set, and the other is a draft configuration of an environment that is either in the process of deployment or that failed to deploy.&lt;/p&gt; &lt;p&gt;Related Topics&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteEnvironmentConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param application_name: The application for the environment or configuration template.
    :type application_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param template_name: &lt;p&gt;The name of the configuration template to describe.&lt;/p&gt; &lt;p&gt; Conditional: You must specify either this parameter or an EnvironmentName, but not both. If you specify both, AWS Elastic Beanstalk returns an &lt;code&gt;InvalidParameterCombination&lt;/code&gt; error. If you do not specify either, AWS Elastic Beanstalk returns a &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type template_name: str
    :param environment_name: &lt;p&gt;The name of the environment to describe.&lt;/p&gt; &lt;p&gt; Condition: You must specify either this or a TemplateName, but not both. If you specify both, AWS Elastic Beanstalk returns an &lt;code&gt;InvalidParameterCombination&lt;/code&gt; error. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type environment_name: str

    """
    return web.Response(status=200)


async def g_et_describe_environment_health(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, environment_name=None, environment_id=None, attribute_names=None) -> web.Response:
    """g_et_describe_environment_health

    Returns information about the overall health of the specified environment. The &lt;b&gt;DescribeEnvironmentHealth&lt;/b&gt; operation is only available with AWS Elastic Beanstalk Enhanced Health.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param environment_name: &lt;p&gt;Specify the environment by name.&lt;/p&gt; &lt;p&gt;You must specify either this or an EnvironmentName, or both.&lt;/p&gt;
    :type environment_name: str
    :param environment_id: &lt;p&gt;Specify the environment by ID.&lt;/p&gt; &lt;p&gt;You must specify either this or an EnvironmentName, or both.&lt;/p&gt;
    :type environment_id: str
    :param attribute_names: Specify the response elements to return. To retrieve all attributes, set to &lt;code&gt;All&lt;/code&gt;. If no attribute names are specified, returns the name of the environment.
    :type attribute_names: list | bytes

    """
    attribute_names = [EnvironmentHealthAttribute.from_dict(d) for d in attribute_names]
    return web.Response(status=200)


async def g_et_describe_environment_managed_action_history(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, environment_id=None, environment_name=None, next_token=None, max_items=None) -> web.Response:
    """g_et_describe_environment_managed_action_history

    Lists an environment&#39;s completed and failed managed actions.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param environment_id: The environment ID of the target environment.
    :type environment_id: str
    :param environment_name: The name of the target environment.
    :type environment_name: str
    :param next_token: The pagination token returned by a previous request.
    :type next_token: str
    :param max_items: The maximum number of items to return for a single request.
    :type max_items: int

    """
    return web.Response(status=200)


async def g_et_describe_environment_managed_actions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, environment_name=None, environment_id=None, status=None) -> web.Response:
    """g_et_describe_environment_managed_actions

    Lists an environment&#39;s upcoming and in-progress managed actions.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param environment_name: The name of the target environment.
    :type environment_name: str
    :param environment_id: The environment ID of the target environment.
    :type environment_id: str
    :param status: To show only actions with a particular status, specify a status.
    :type status: str

    """
    return web.Response(status=200)


async def g_et_describe_environment_resources(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, environment_id=None, environment_name=None) -> web.Response:
    """g_et_describe_environment_resources

    Returns AWS resources for this environment.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param environment_id: &lt;p&gt;The ID of the environment to retrieve AWS resource usage data.&lt;/p&gt; &lt;p&gt; Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type environment_id: str
    :param environment_name: &lt;p&gt;The name of the environment to retrieve AWS resource usage data.&lt;/p&gt; &lt;p&gt; Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type environment_name: str

    """
    return web.Response(status=200)


async def g_et_describe_environments(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, application_name=None, version_label=None, environment_ids=None, environment_names=None, include_deleted=None, included_deleted_back_to=None, max_records=None, next_token=None) -> web.Response:
    """g_et_describe_environments

    Returns descriptions for existing environments.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param application_name: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application.
    :type application_name: str
    :param version_label: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application version.
    :type version_label: str
    :param environment_ids: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified IDs.
    :type environment_ids: List[str]
    :param environment_names: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified names.
    :type environment_names: List[str]
    :param include_deleted: &lt;p&gt;Indicates whether to include deleted environments:&lt;/p&gt; &lt;p&gt; &lt;code&gt;true&lt;/code&gt;: Environments that have been deleted after &lt;code&gt;IncludedDeletedBackTo&lt;/code&gt; are displayed.&lt;/p&gt; &lt;p&gt; &lt;code&gt;false&lt;/code&gt;: Do not include deleted environments.&lt;/p&gt;
    :type include_deleted: bool
    :param included_deleted_back_to:  If specified when &lt;code&gt;IncludeDeleted&lt;/code&gt; is set to &lt;code&gt;true&lt;/code&gt;, then environments deleted after this date are displayed. 
    :type included_deleted_back_to: str
    :param max_records: &lt;p&gt;For a paginated request. Specify a maximum number of environments to include in each response.&lt;/p&gt; &lt;p&gt;If no &lt;code&gt;MaxRecords&lt;/code&gt; is specified, all available environments are retrieved in a single response.&lt;/p&gt;
    :type max_records: int
    :param next_token: &lt;p&gt;For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.&lt;/p&gt; &lt;p&gt;If no &lt;code&gt;NextToken&lt;/code&gt; is specified, the first page is retrieved.&lt;/p&gt;
    :type next_token: str

    """
    included_deleted_back_to = util.deserialize_datetime(included_deleted_back_to)
    return web.Response(status=200)


async def g_et_describe_events(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, application_name=None, version_label=None, template_name=None, environment_id=None, environment_name=None, platform_arn=None, request_id=None, severity=None, start_time=None, end_time=None, max_records=None, next_token=None) -> web.Response:
    """g_et_describe_events

    &lt;p&gt;Returns list of event descriptions matching criteria up to the last 6 weeks.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action returns the most recent 1,000 events from the specified &lt;code&gt;NextToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param application_name: If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those associated with this application.
    :type application_name: str
    :param version_label: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this application version.
    :type version_label: str
    :param template_name: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that are associated with this environment configuration.
    :type template_name: str
    :param environment_id: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.
    :type environment_id: str
    :param environment_name: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.
    :type environment_name: str
    :param platform_arn: The ARN of a custom platform version. If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this custom platform version.
    :type platform_arn: str
    :param request_id: If specified, AWS Elastic Beanstalk restricts the described events to include only those associated with this request ID.
    :type request_id: str
    :param severity: If specified, limits the events returned from this call to include only those with the specified severity or higher.
    :type severity: str
    :param start_time: If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur on or after this time.
    :type start_time: str
    :param end_time:  If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur up to, but not including, the &lt;code&gt;EndTime&lt;/code&gt;. 
    :type end_time: str
    :param max_records: Specifies the maximum number of events that can be returned, beginning with the most recent event.
    :type max_records: int
    :param next_token: Pagination token. If specified, the events return the next batch of results.
    :type next_token: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def g_et_describe_instances_health(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, environment_name=None, environment_id=None, attribute_names=None, next_token=None) -> web.Response:
    """g_et_describe_instances_health

    Retrieves detailed information about the health of instances in your AWS Elastic Beanstalk. This operation requires &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced.html\&quot;&gt;enhanced health reporting&lt;/a&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param environment_name: Specify the AWS Elastic Beanstalk environment by name.
    :type environment_name: str
    :param environment_id: Specify the AWS Elastic Beanstalk environment by ID.
    :type environment_id: str
    :param attribute_names: Specifies the response elements you wish to receive. To retrieve all attributes, set to &lt;code&gt;All&lt;/code&gt;. If no attribute names are specified, returns a list of instances.
    :type attribute_names: list | bytes
    :param next_token: Specify the pagination token returned by a previous call.
    :type next_token: str

    """
    attribute_names = [InstancesHealthAttribute.from_dict(d) for d in attribute_names]
    return web.Response(status=200)


async def g_et_describe_platform_version(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, platform_arn=None) -> web.Response:
    """g_et_describe_platform_version

    &lt;p&gt;Describes a platform version. Provides full details. Compare to &lt;a&gt;ListPlatformVersions&lt;/a&gt;, which provides summary information about a list of platform versions.&lt;/p&gt; &lt;p&gt;For definitions of platform version and other platform-related terms, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html\&quot;&gt;AWS Elastic Beanstalk Platforms Glossary&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param platform_arn: The ARN of the platform version.
    :type platform_arn: str

    """
    return web.Response(status=200)


async def g_et_disassociate_environment_operations_role(request: web.Request, environment_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_disassociate_environment_operations_role

    Disassociate the operations role from an environment. After this call is made, Elastic Beanstalk uses the caller&#39;s permissions for permissions to downstream services during subsequent calls acting on this environment. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/iam-operationsrole.html\&quot;&gt;Operations roles&lt;/a&gt; in the &lt;i&gt;AWS Elastic Beanstalk Developer Guide&lt;/i&gt;.

    :param environment_name: The name of the environment from which to disassociate the operations role.
    :type environment_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_list_available_solution_stacks(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_list_available_solution_stacks

    Returns a list of the available solution stack names, with the public version first and then in reverse chronological order.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_list_platform_branches(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, filters=None, max_records=None, next_token=None) -> web.Response:
    """g_et_list_platform_branches

    &lt;p&gt;Lists the platform branches available for your account in an AWS Region. Provides summary information about each platform branch.&lt;/p&gt; &lt;p&gt;For definitions of platform branch and other platform-related terms, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html\&quot;&gt;AWS Elastic Beanstalk Platforms Glossary&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param filters: &lt;p&gt;Criteria for restricting the resulting list of platform branches. The filter is evaluated as a logical conjunction (AND) of the separate &lt;code&gt;SearchFilter&lt;/code&gt; terms.&lt;/p&gt; &lt;p&gt;The following list shows valid attribute values for each of the &lt;code&gt;SearchFilter&lt;/code&gt; terms. Most operators take a single value. The &lt;code&gt;in&lt;/code&gt; and &lt;code&gt;not_in&lt;/code&gt; operators can take multiple values.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Attribute &#x3D; BranchName&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Operator&lt;/code&gt;: &lt;code&gt;&#x3D;&lt;/code&gt; | &lt;code&gt;!&#x3D;&lt;/code&gt; | &lt;code&gt;begins_with&lt;/code&gt; | &lt;code&gt;ends_with&lt;/code&gt; | &lt;code&gt;contains&lt;/code&gt; | &lt;code&gt;in&lt;/code&gt; | &lt;code&gt;not_in&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Attribute &#x3D; LifecycleState&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Operator&lt;/code&gt;: &lt;code&gt;&#x3D;&lt;/code&gt; | &lt;code&gt;!&#x3D;&lt;/code&gt; | &lt;code&gt;in&lt;/code&gt; | &lt;code&gt;not_in&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Values&lt;/code&gt;: &lt;code&gt;beta&lt;/code&gt; | &lt;code&gt;supported&lt;/code&gt; | &lt;code&gt;deprecated&lt;/code&gt; | &lt;code&gt;retired&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Attribute &#x3D; PlatformName&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Operator&lt;/code&gt;: &lt;code&gt;&#x3D;&lt;/code&gt; | &lt;code&gt;!&#x3D;&lt;/code&gt; | &lt;code&gt;begins_with&lt;/code&gt; | &lt;code&gt;ends_with&lt;/code&gt; | &lt;code&gt;contains&lt;/code&gt; | &lt;code&gt;in&lt;/code&gt; | &lt;code&gt;not_in&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Attribute &#x3D; TierType&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Operator&lt;/code&gt;: &lt;code&gt;&#x3D;&lt;/code&gt; | &lt;code&gt;!&#x3D;&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Values&lt;/code&gt;: &lt;code&gt;WebServer/Standard&lt;/code&gt; | &lt;code&gt;Worker/SQS/HTTP&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Array size: limited to 10 &lt;code&gt;SearchFilter&lt;/code&gt; objects.&lt;/p&gt; &lt;p&gt;Within each &lt;code&gt;SearchFilter&lt;/code&gt; item, the &lt;code&gt;Values&lt;/code&gt; array is limited to 10 items.&lt;/p&gt;
    :type filters: list | bytes
    :param max_records: The maximum number of platform branch values returned in one call.
    :type max_records: int
    :param next_token: &lt;p&gt;For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.&lt;/p&gt; &lt;p&gt;If no &lt;code&gt;NextToken&lt;/code&gt; is specified, the first page is retrieved.&lt;/p&gt;
    :type next_token: str

    """
    filters = [SearchFilter.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_list_platform_versions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, filters=None, max_records=None, next_token=None) -> web.Response:
    """g_et_list_platform_versions

    &lt;p&gt;Lists the platform versions available for your account in an AWS Region. Provides summary information about each platform version. Compare to &lt;a&gt;DescribePlatformVersion&lt;/a&gt;, which provides full details about a single platform version.&lt;/p&gt; &lt;p&gt;For definitions of platform version and other platform-related terms, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html\&quot;&gt;AWS Elastic Beanstalk Platforms Glossary&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param filters: Criteria for restricting the resulting list of platform versions. The filter is interpreted as a logical conjunction (AND) of the separate &lt;code&gt;PlatformFilter&lt;/code&gt; terms.
    :type filters: list | bytes
    :param max_records: The maximum number of platform version values returned in one call.
    :type max_records: int
    :param next_token: &lt;p&gt;For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.&lt;/p&gt; &lt;p&gt;If no &lt;code&gt;NextToken&lt;/code&gt; is specified, the first page is retrieved.&lt;/p&gt;
    :type next_token: str

    """
    filters = [PlatformFilter.from_dict(d) for d in filters]
    return web.Response(status=200)


async def g_et_list_tags_for_resource(request: web.Request, resource_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_list_tags_for_resource

    &lt;p&gt;Return the tags applied to an AWS Elastic Beanstalk resource. The response contains a list of tag key-value pairs.&lt;/p&gt; &lt;p&gt;Elastic Beanstalk supports tagging of all of its resources. For details about resource tagging, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-tagging-resources.html\&quot;&gt;Tagging Application Resources&lt;/a&gt;.&lt;/p&gt;

    :param resource_arn: &lt;p&gt;The Amazon Resource Name (ARN) of the resouce for which a tag list is requested.&lt;/p&gt; &lt;p&gt;Must be the ARN of an Elastic Beanstalk resource.&lt;/p&gt;
    :type resource_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_rebuild_environment(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, environment_id=None, environment_name=None) -> web.Response:
    """g_et_rebuild_environment

    Deletes and recreates all of the AWS resources (for example: the Auto Scaling group, load balancer, etc.) for a specified environment and forces a restart.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param environment_id: &lt;p&gt;The ID of the environment to rebuild.&lt;/p&gt; &lt;p&gt; Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type environment_id: str
    :param environment_name: &lt;p&gt;The name of the environment to rebuild.&lt;/p&gt; &lt;p&gt; Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type environment_name: str

    """
    return web.Response(status=200)


async def g_et_request_environment_info(request: web.Request, info_type, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, environment_id=None, environment_name=None) -> web.Response:
    """g_et_request_environment_info

    &lt;p&gt;Initiates a request to compile the specified type of information of the deployed environment.&lt;/p&gt; &lt;p&gt; Setting the &lt;code&gt;InfoType&lt;/code&gt; to &lt;code&gt;tail&lt;/code&gt; compiles the last lines from the application server log files of every Amazon EC2 instance in your environment. &lt;/p&gt; &lt;p&gt; Setting the &lt;code&gt;InfoType&lt;/code&gt; to &lt;code&gt;bundle&lt;/code&gt; compresses the application server log files for every Amazon EC2 instance into a &lt;code&gt;.zip&lt;/code&gt; file. Legacy and .NET containers do not support bundle logs. &lt;/p&gt; &lt;p&gt; Use &lt;a&gt;RetrieveEnvironmentInfo&lt;/a&gt; to obtain the set of logs. &lt;/p&gt; &lt;p&gt;Related Topics&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;RetrieveEnvironmentInfo&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param info_type: The type of information to request.
    :type info_type: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param environment_id: &lt;p&gt;The ID of the environment of the requested data.&lt;/p&gt; &lt;p&gt;If no such environment is found, &lt;code&gt;RequestEnvironmentInfo&lt;/code&gt; returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error. &lt;/p&gt; &lt;p&gt;Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type environment_id: str
    :param environment_name: &lt;p&gt;The name of the environment of the requested data.&lt;/p&gt; &lt;p&gt;If no such environment is found, &lt;code&gt;RequestEnvironmentInfo&lt;/code&gt; returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error. &lt;/p&gt; &lt;p&gt;Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type environment_name: str

    """
    return web.Response(status=200)


async def g_et_restart_app_server(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, environment_id=None, environment_name=None) -> web.Response:
    """g_et_restart_app_server

    Causes the environment to restart the application container server running on each Amazon EC2 instance.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param environment_id: &lt;p&gt;The ID of the environment to restart the server for.&lt;/p&gt; &lt;p&gt; Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type environment_id: str
    :param environment_name: &lt;p&gt;The name of the environment to restart the server for.&lt;/p&gt; &lt;p&gt; Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type environment_name: str

    """
    return web.Response(status=200)


async def g_et_retrieve_environment_info(request: web.Request, info_type, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, environment_id=None, environment_name=None) -> web.Response:
    """g_et_retrieve_environment_info

    &lt;p&gt;Retrieves the compiled information from a &lt;a&gt;RequestEnvironmentInfo&lt;/a&gt; request.&lt;/p&gt; &lt;p&gt;Related Topics&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;RequestEnvironmentInfo&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param info_type: The type of information to retrieve.
    :type info_type: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param environment_id: &lt;p&gt;The ID of the data&#39;s environment.&lt;/p&gt; &lt;p&gt;If no such environment is found, returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error.&lt;/p&gt;
    :type environment_id: str
    :param environment_name: &lt;p&gt;The name of the data&#39;s environment.&lt;/p&gt; &lt;p&gt; If no such environment is found, returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error. &lt;/p&gt; &lt;p&gt; Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type environment_name: str

    """
    return web.Response(status=200)


async def g_et_swap_environment_cnames(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, source_environment_id=None, source_environment_name=None, destination_environment_id=None, destination_environment_name=None) -> web.Response:
    """g_et_swap_environment_cnames

    Swaps the CNAMEs of two environments.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param source_environment_id: &lt;p&gt;The ID of the source environment.&lt;/p&gt; &lt;p&gt; Condition: You must specify at least the &lt;code&gt;SourceEnvironmentID&lt;/code&gt; or the &lt;code&gt;SourceEnvironmentName&lt;/code&gt;. You may also specify both. If you specify the &lt;code&gt;SourceEnvironmentId&lt;/code&gt;, you must specify the &lt;code&gt;DestinationEnvironmentId&lt;/code&gt;. &lt;/p&gt;
    :type source_environment_id: str
    :param source_environment_name: &lt;p&gt;The name of the source environment.&lt;/p&gt; &lt;p&gt; Condition: You must specify at least the &lt;code&gt;SourceEnvironmentID&lt;/code&gt; or the &lt;code&gt;SourceEnvironmentName&lt;/code&gt;. You may also specify both. If you specify the &lt;code&gt;SourceEnvironmentName&lt;/code&gt;, you must specify the &lt;code&gt;DestinationEnvironmentName&lt;/code&gt;. &lt;/p&gt;
    :type source_environment_name: str
    :param destination_environment_id: &lt;p&gt;The ID of the destination environment.&lt;/p&gt; &lt;p&gt; Condition: You must specify at least the &lt;code&gt;DestinationEnvironmentID&lt;/code&gt; or the &lt;code&gt;DestinationEnvironmentName&lt;/code&gt;. You may also specify both. You must specify the &lt;code&gt;SourceEnvironmentId&lt;/code&gt; with the &lt;code&gt;DestinationEnvironmentId&lt;/code&gt;. &lt;/p&gt;
    :type destination_environment_id: str
    :param destination_environment_name: &lt;p&gt;The name of the destination environment.&lt;/p&gt; &lt;p&gt; Condition: You must specify at least the &lt;code&gt;DestinationEnvironmentID&lt;/code&gt; or the &lt;code&gt;DestinationEnvironmentName&lt;/code&gt;. You may also specify both. You must specify the &lt;code&gt;SourceEnvironmentName&lt;/code&gt; with the &lt;code&gt;DestinationEnvironmentName&lt;/code&gt;. &lt;/p&gt;
    :type destination_environment_name: str

    """
    return web.Response(status=200)


async def g_et_terminate_environment(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, environment_id=None, environment_name=None, terminate_resources=None, force_terminate=None) -> web.Response:
    """g_et_terminate_environment

    Terminates the specified environment.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param environment_id: &lt;p&gt;The ID of the environment to terminate.&lt;/p&gt; &lt;p&gt; Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type environment_id: str
    :param environment_name: &lt;p&gt;The name of the environment to terminate.&lt;/p&gt; &lt;p&gt; Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type environment_name: str
    :param terminate_resources: &lt;p&gt;Indicates whether the associated AWS resources should shut down when the environment is terminated:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;true&lt;/code&gt;: The specified environment as well as the associated AWS resources, such as Auto Scaling group and LoadBalancer, are terminated.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;false&lt;/code&gt;: AWS Elastic Beanstalk resource management is removed from the environment, but the AWS resources continue to operate.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/ug/\&quot;&gt; AWS Elastic Beanstalk User Guide. &lt;/a&gt; &lt;/p&gt; &lt;p&gt; Default: &lt;code&gt;true&lt;/code&gt; &lt;/p&gt; &lt;p&gt; Valid Values: &lt;code&gt;true&lt;/code&gt; | &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type terminate_resources: bool
    :param force_terminate: Terminates the target environment even if another environment in the same group is dependent on it.
    :type force_terminate: bool

    """
    return web.Response(status=200)


async def g_et_update_application(request: web.Request, application_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, description=None) -> web.Response:
    """g_et_update_application

    &lt;p&gt;Updates the specified application to have the specified properties.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If a property (for example, &lt;code&gt;description&lt;/code&gt;) is not provided, the value remains unchanged. To clear these properties, specify an empty string.&lt;/p&gt; &lt;/note&gt;

    :param application_name: The name of the application to update. If no such application is found, &lt;code&gt;UpdateApplication&lt;/code&gt; returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error. 
    :type application_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param description: &lt;p&gt;A new description for the application.&lt;/p&gt; &lt;p&gt;Default: If not specified, AWS Elastic Beanstalk does not update the description.&lt;/p&gt;
    :type description: str

    """
    return web.Response(status=200)


async def g_et_update_application_resource_lifecycle(request: web.Request, application_name, resource_lifecycle_config, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_update_application_resource_lifecycle

    Modifies lifecycle settings for an application.

    :param application_name: The name of the application.
    :type application_name: str
    :param resource_lifecycle_config: The lifecycle configuration.
    :type resource_lifecycle_config: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    resource_lifecycle_config = .from_dict(resource_lifecycle_config)
    return web.Response(status=200)


async def g_et_update_application_version(request: web.Request, application_name, version_label, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, description=None) -> web.Response:
    """g_et_update_application_version

    &lt;p&gt;Updates the specified application version to have the specified properties.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If a property (for example, &lt;code&gt;description&lt;/code&gt;) is not provided, the value remains unchanged. To clear properties, specify an empty string.&lt;/p&gt; &lt;/note&gt;

    :param application_name: &lt;p&gt;The name of the application associated with this version.&lt;/p&gt; &lt;p&gt; If no application is found with this name, &lt;code&gt;UpdateApplication&lt;/code&gt; returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error.&lt;/p&gt;
    :type application_name: str
    :param version_label: &lt;p&gt;The name of the version to update.&lt;/p&gt; &lt;p&gt;If no application version is found with this label, &lt;code&gt;UpdateApplication&lt;/code&gt; returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error. &lt;/p&gt;
    :type version_label: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param description: A new description for this version.
    :type description: str

    """
    return web.Response(status=200)


async def g_et_update_configuration_template(request: web.Request, application_name, template_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, description=None, option_settings=None, options_to_remove=None) -> web.Response:
    """g_et_update_configuration_template

    &lt;p&gt;Updates the specified configuration template to have the specified properties or configuration option values.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If a property (for example, &lt;code&gt;ApplicationName&lt;/code&gt;) is not provided, its value remains unchanged. To clear such properties, specify an empty string.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Related Topics&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeConfigurationOptions&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param application_name: &lt;p&gt;The name of the application associated with the configuration template to update.&lt;/p&gt; &lt;p&gt; If no application is found with this name, &lt;code&gt;UpdateConfigurationTemplate&lt;/code&gt; returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error. &lt;/p&gt;
    :type application_name: str
    :param template_name: &lt;p&gt;The name of the configuration template to update.&lt;/p&gt; &lt;p&gt; If no configuration template is found with this name, &lt;code&gt;UpdateConfigurationTemplate&lt;/code&gt; returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error. &lt;/p&gt;
    :type template_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param description: A new description for the configuration.
    :type description: str
    :param option_settings: A list of configuration option settings to update with the new specified option value.
    :type option_settings: list | bytes
    :param options_to_remove: &lt;p&gt;A list of configuration options to remove from the configuration set.&lt;/p&gt; &lt;p&gt; Constraint: You can remove only &lt;code&gt;UserDefined&lt;/code&gt; configuration options. &lt;/p&gt;
    :type options_to_remove: list | bytes

    """
    option_settings = [ConfigurationOptionSetting.from_dict(d) for d in option_settings]
    options_to_remove = [OptionSpecification.from_dict(d) for d in options_to_remove]
    return web.Response(status=200)


async def g_et_update_environment(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, application_name=None, environment_id=None, environment_name=None, group_name=None, description=None, tier=None, version_label=None, template_name=None, solution_stack_name=None, platform_arn=None, option_settings=None, options_to_remove=None) -> web.Response:
    """g_et_update_environment

    &lt;p&gt;Updates the environment description, deploys a new application version, updates the configuration settings to an entirely new configuration template, or updates select configuration option values in the running environment.&lt;/p&gt; &lt;p&gt; Attempting to update both the release and configuration is not allowed and AWS Elastic Beanstalk returns an &lt;code&gt;InvalidParameterCombination&lt;/code&gt; error. &lt;/p&gt; &lt;p&gt; When updating the configuration settings to a new template or individual settings, a draft configuration is created and &lt;a&gt;DescribeConfigurationSettings&lt;/a&gt; for this environment returns two setting descriptions with different &lt;code&gt;DeploymentStatus&lt;/code&gt; values. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param application_name: The name of the application with which the environment is associated.
    :type application_name: str
    :param environment_id: &lt;p&gt;The ID of the environment to update.&lt;/p&gt; &lt;p&gt;If no environment with this ID exists, AWS Elastic Beanstalk returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type environment_id: str
    :param environment_name: &lt;p&gt;The name of the environment to update. If no environment with this name exists, AWS Elastic Beanstalk returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error. &lt;/p&gt; &lt;p&gt;Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns &lt;code&gt;MissingRequiredParameter&lt;/code&gt; error. &lt;/p&gt;
    :type environment_name: str
    :param group_name: The name of the group to which the target environment belongs. Specify a group name only if the environment&#39;s name is specified in an environment manifest and not with the environment name or environment ID parameters. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html\&quot;&gt;Environment Manifest (env.yaml)&lt;/a&gt; for details.
    :type group_name: str
    :param description: If this parameter is specified, AWS Elastic Beanstalk updates the description of this environment.
    :type description: str
    :param tier: &lt;p&gt;This specifies the tier to use to update the environment.&lt;/p&gt; &lt;p&gt;Condition: At this time, if you change the tier version, name, or type, AWS Elastic Beanstalk returns &lt;code&gt;InvalidParameterValue&lt;/code&gt; error. &lt;/p&gt;
    :type tier: dict | bytes
    :param version_label: If this parameter is specified, AWS Elastic Beanstalk deploys the named application version to the environment. If no such application version is found, returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error. 
    :type version_label: str
    :param template_name: If this parameter is specified, AWS Elastic Beanstalk deploys this configuration template to the environment. If no such configuration template is found, AWS Elastic Beanstalk returns an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error. 
    :type template_name: str
    :param solution_stack_name: This specifies the platform version that the environment will run after the environment is updated.
    :type solution_stack_name: str
    :param platform_arn: The ARN of the platform, if used.
    :type platform_arn: str
    :param option_settings: If specified, AWS Elastic Beanstalk updates the configuration set associated with the running environment and sets the specified configuration options to the requested value.
    :type option_settings: list | bytes
    :param options_to_remove: A list of custom user-defined configuration options to remove from the configuration set for this environment.
    :type options_to_remove: list | bytes

    """
    tier = .from_dict(tier)
    option_settings = [ConfigurationOptionSetting.from_dict(d) for d in option_settings]
    options_to_remove = [OptionSpecification.from_dict(d) for d in options_to_remove]
    return web.Response(status=200)


async def g_et_update_tags_for_resource(request: web.Request, resource_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags_to_add=None, tags_to_remove=None) -> web.Response:
    """g_et_update_tags_for_resource

    &lt;p&gt;Update the list of tags applied to an AWS Elastic Beanstalk resource. Two lists can be passed: &lt;code&gt;TagsToAdd&lt;/code&gt; for tags to add or update, and &lt;code&gt;TagsToRemove&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Elastic Beanstalk supports tagging of all of its resources. For details about resource tagging, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-tagging-resources.html\&quot;&gt;Tagging Application Resources&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you create a custom IAM user policy to control permission to this operation, specify one of the following two virtual actions (or both) instead of the API operation name:&lt;/p&gt; &lt;dl&gt; &lt;dt&gt;elasticbeanstalk:AddTags&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Controls permission to call &lt;code&gt;UpdateTagsForResource&lt;/code&gt; and pass a list of tags to add in the &lt;code&gt;TagsToAdd&lt;/code&gt; parameter.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;elasticbeanstalk:RemoveTags&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Controls permission to call &lt;code&gt;UpdateTagsForResource&lt;/code&gt; and pass a list of tag keys to remove in the &lt;code&gt;TagsToRemove&lt;/code&gt; parameter.&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt; &lt;p&gt;For details about creating a custom user policy, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#AWSHowTo.iam.policies\&quot;&gt;Creating a Custom User Policy&lt;/a&gt;.&lt;/p&gt;

    :param resource_arn: &lt;p&gt;The Amazon Resource Name (ARN) of the resouce to be updated.&lt;/p&gt; &lt;p&gt;Must be the ARN of an Elastic Beanstalk resource.&lt;/p&gt;
    :type resource_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param tags_to_add: &lt;p&gt;A list of tags to add or update. If a key of an existing tag is added, the tag&#39;s value is updated.&lt;/p&gt; &lt;p&gt;Specify at least one of these parameters: &lt;code&gt;TagsToAdd&lt;/code&gt;, &lt;code&gt;TagsToRemove&lt;/code&gt;.&lt;/p&gt;
    :type tags_to_add: list | bytes
    :param tags_to_remove: &lt;p&gt;A list of tag keys to remove. If a tag key doesn&#39;t exist, it is silently ignored.&lt;/p&gt; &lt;p&gt;Specify at least one of these parameters: &lt;code&gt;TagsToAdd&lt;/code&gt;, &lt;code&gt;TagsToRemove&lt;/code&gt;.&lt;/p&gt;
    :type tags_to_remove: List[str]

    """
    tags_to_add = [Tag.from_dict(d) for d in tags_to_add]
    return web.Response(status=200)


async def g_et_validate_configuration_settings(request: web.Request, application_name, option_settings, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, template_name=None, environment_name=None) -> web.Response:
    """g_et_validate_configuration_settings

    &lt;p&gt;Takes a set of configuration settings and either a configuration template or environment, and determines whether those values are valid.&lt;/p&gt; &lt;p&gt;This action returns a list of messages indicating any errors or warnings associated with the selection of option values.&lt;/p&gt;

    :param application_name: The name of the application that the configuration template or environment belongs to.
    :type application_name: str
    :param option_settings: A list of the options and desired values to evaluate.
    :type option_settings: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param template_name: &lt;p&gt;The name of the configuration template to validate the settings against.&lt;/p&gt; &lt;p&gt;Condition: You cannot specify both this and an environment name.&lt;/p&gt;
    :type template_name: str
    :param environment_name: &lt;p&gt;The name of the environment to validate the settings against.&lt;/p&gt; &lt;p&gt;Condition: You cannot specify both this and a configuration template name.&lt;/p&gt;
    :type environment_name: str

    """
    option_settings = [ConfigurationOptionSetting.from_dict(d) for d in option_settings]
    return web.Response(status=200)


async def p_ost_abort_environment_update(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_abort_environment_update

    Cancels in-progress environment configuration update or application version deployment.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = AbortEnvironmentUpdateMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_apply_environment_managed_action(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_apply_environment_managed_action

    Applies a scheduled managed action immediately. A managed action can be applied only if its status is &lt;code&gt;Scheduled&lt;/code&gt;. Get the status and action ID of a managed action with &lt;a&gt;DescribeEnvironmentManagedActions&lt;/a&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ApplyEnvironmentManagedActionRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_associate_environment_operations_role(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_associate_environment_operations_role

    Add or change the operations role used by an environment. After this call is made, Elastic Beanstalk uses the associated operations role for permissions to downstream services during subsequent calls acting on this environment. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/iam-operationsrole.html\&quot;&gt;Operations roles&lt;/a&gt; in the &lt;i&gt;AWS Elastic Beanstalk Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = AssociateEnvironmentOperationsRoleMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_check_dns_availability(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_check_dns_availability

    Checks if the specified CNAME is available.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CheckDNSAvailabilityMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_compose_environments(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_compose_environments

    Create or update a group of environments that each run a separate component of a single application. Takes a list of version labels that specify application source bundles for each of the environments to create or update. The name of each environment and other required information must be included in the source bundles in an environment manifest named &lt;code&gt;env.yaml&lt;/code&gt;. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-mgmt-compose.html\&quot;&gt;Compose Environments&lt;/a&gt; for details.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ComposeEnvironmentsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_application(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_application

    Creates an application that has one configuration template named &lt;code&gt;default&lt;/code&gt; and no application versions.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CreateApplicationMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_application_version(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_application_version

    &lt;p&gt;Creates an application version for the specified application. You can create an application version from a source bundle in Amazon S3, a commit in AWS CodeCommit, or the output of an AWS CodeBuild build as follows:&lt;/p&gt; &lt;p&gt;Specify a commit in an AWS CodeCommit repository with &lt;code&gt;SourceBuildInformation&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Specify a build in an AWS CodeBuild with &lt;code&gt;SourceBuildInformation&lt;/code&gt; and &lt;code&gt;BuildConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Specify a source bundle in S3 with &lt;code&gt;SourceBundle&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Omit both &lt;code&gt;SourceBuildInformation&lt;/code&gt; and &lt;code&gt;SourceBundle&lt;/code&gt; to use the default sample application.&lt;/p&gt; &lt;note&gt; &lt;p&gt;After you create an application version with a specified Amazon S3 bucket and key location, you can&#39;t change that Amazon S3 location. If you change the Amazon S3 location, you receive an exception when you attempt to launch an environment from the application version.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CreateApplicationVersionMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_configuration_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_configuration_template

    &lt;p&gt;Creates an AWS Elastic Beanstalk configuration template, associated with a specific Elastic Beanstalk application. You define application configuration settings in a configuration template. You can then use the configuration template to deploy different versions of the application with the same configuration settings.&lt;/p&gt; &lt;p&gt;Templates aren&#39;t associated with any environment. The &lt;code&gt;EnvironmentName&lt;/code&gt; response element is always &lt;code&gt;null&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Related Topics&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeConfigurationOptions&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeConfigurationSettings&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListAvailableSolutionStacks&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CreateConfigurationTemplateMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_environment(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_environment

    Launches an AWS Elastic Beanstalk environment for the specified application using the specified configuration.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CreateEnvironmentMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_platform_version(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_platform_version

    Create a new version of your custom platform.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CreatePlatformVersionRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_storage_location(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_create_storage_location

    Creates a bucket in Amazon S3 to store application versions, logs, and other files used by Elastic Beanstalk environments. The Elastic Beanstalk console and EB CLI call this API the first time you create an environment in a region. If the storage location already exists, &lt;code&gt;CreateStorageLocation&lt;/code&gt; still returns the bucket name but does not create a new bucket.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def p_ost_delete_application(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_application

    &lt;p&gt;Deletes the specified application along with all associated versions and configurations. The application versions will not be deleted from your Amazon S3 bucket.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot delete an application that has a running environment.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteApplicationMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_application_version(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_application_version

    &lt;p&gt;Deletes the specified version from the specified application.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot delete an application version that is associated with a running environment.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteApplicationVersionMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_configuration_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_configuration_template

    &lt;p&gt;Deletes the specified configuration template.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you launch an environment using a configuration template, the environment gets a copy of the template. You can delete or modify the environment&#39;s copy of the template without affecting the running environment.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteConfigurationTemplateMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_environment_configuration(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_environment_configuration

    &lt;p&gt;Deletes the draft configuration associated with the running environment.&lt;/p&gt; &lt;p&gt;Updating a running environment with any configuration changes creates a draft configuration set. You can get the draft configuration using &lt;a&gt;DescribeConfigurationSettings&lt;/a&gt; while the update is in progress or if the update fails. The &lt;code&gt;DeploymentStatus&lt;/code&gt; for the draft configuration indicates whether the deployment is in process or has failed. The draft configuration remains in existence until it is deleted with this action.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteEnvironmentConfigurationMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_platform_version(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_platform_version

    Deletes the specified version of a custom platform.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeletePlatformVersionRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_account_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_describe_account_attributes

    &lt;p&gt;Returns attributes related to AWS Elastic Beanstalk that are associated with the calling AWS account.&lt;/p&gt; &lt;p&gt;The result currently has one set of attributes—resource quotas.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def p_ost_describe_application_versions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_application_versions

    Retrieve a list of application versions.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeApplicationVersionsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_applications(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_applications

    Returns the descriptions of existing applications.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeApplicationsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_configuration_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_configuration_options

    Describes the configuration options that are used in a particular configuration template or environment, or that a specified solution stack defines. The description includes the values the options, their default values, and an indication of the required action on a running environment if an option value is changed.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeConfigurationOptionsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_configuration_settings(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_configuration_settings

    &lt;p&gt;Returns a description of the settings for the specified configuration set, that is, either a configuration template or the configuration set associated with a running environment.&lt;/p&gt; &lt;p&gt;When describing the settings for the configuration set associated with a running environment, it is possible to receive two sets of setting descriptions. One is the deployed configuration set, and the other is a draft configuration of an environment that is either in the process of deployment or that failed to deploy.&lt;/p&gt; &lt;p&gt;Related Topics&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteEnvironmentConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeConfigurationSettingsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_environment_health(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_environment_health

    Returns information about the overall health of the specified environment. The &lt;b&gt;DescribeEnvironmentHealth&lt;/b&gt; operation is only available with AWS Elastic Beanstalk Enhanced Health.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeEnvironmentHealthRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_environment_managed_action_history(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_items=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_environment_managed_action_history

    Lists an environment&#39;s completed and failed managed actions.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param max_items: Pagination limit
    :type max_items: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeEnvironmentManagedActionHistoryRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_environment_managed_actions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_environment_managed_actions

    Lists an environment&#39;s upcoming and in-progress managed actions.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeEnvironmentManagedActionsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_environment_resources(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_environment_resources

    Returns AWS resources for this environment.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeEnvironmentResourcesMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_environments(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_environments

    Returns descriptions for existing environments.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeEnvironmentsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_events(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_events

    &lt;p&gt;Returns list of event descriptions matching criteria up to the last 6 weeks.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This action returns the most recent 1,000 events from the specified &lt;code&gt;NextToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param max_records: Pagination limit
    :type max_records: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeEventsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_instances_health(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_instances_health

    Retrieves detailed information about the health of instances in your AWS Elastic Beanstalk. This operation requires &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced.html\&quot;&gt;enhanced health reporting&lt;/a&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeInstancesHealthRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_platform_version(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_platform_version

    &lt;p&gt;Describes a platform version. Provides full details. Compare to &lt;a&gt;ListPlatformVersions&lt;/a&gt;, which provides summary information about a list of platform versions.&lt;/p&gt; &lt;p&gt;For definitions of platform version and other platform-related terms, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html\&quot;&gt;AWS Elastic Beanstalk Platforms Glossary&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribePlatformVersionRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_disassociate_environment_operations_role(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_disassociate_environment_operations_role

    Disassociate the operations role from an environment. After this call is made, Elastic Beanstalk uses the caller&#39;s permissions for permissions to downstream services during subsequent calls acting on this environment. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/iam-operationsrole.html\&quot;&gt;Operations roles&lt;/a&gt; in the &lt;i&gt;AWS Elastic Beanstalk Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DisassociateEnvironmentOperationsRoleMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_available_solution_stacks(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_list_available_solution_stacks

    Returns a list of the available solution stack names, with the public version first and then in reverse chronological order.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def p_ost_list_platform_branches(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_platform_branches

    &lt;p&gt;Lists the platform branches available for your account in an AWS Region. Provides summary information about each platform branch.&lt;/p&gt; &lt;p&gt;For definitions of platform branch and other platform-related terms, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html\&quot;&gt;AWS Elastic Beanstalk Platforms Glossary&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param max_records: Pagination limit
    :type max_records: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListPlatformBranchesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_platform_versions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_platform_versions

    &lt;p&gt;Lists the platform versions available for your account in an AWS Region. Provides summary information about each platform version. Compare to &lt;a&gt;DescribePlatformVersion&lt;/a&gt;, which provides full details about a single platform version.&lt;/p&gt; &lt;p&gt;For definitions of platform version and other platform-related terms, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html\&quot;&gt;AWS Elastic Beanstalk Platforms Glossary&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param max_records: Pagination limit
    :type max_records: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListPlatformVersionsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_tags_for_resource(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_list_tags_for_resource

    &lt;p&gt;Return the tags applied to an AWS Elastic Beanstalk resource. The response contains a list of tag key-value pairs.&lt;/p&gt; &lt;p&gt;Elastic Beanstalk supports tagging of all of its resources. For details about resource tagging, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-tagging-resources.html\&quot;&gt;Tagging Application Resources&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ListTagsForResourceMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_rebuild_environment(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_rebuild_environment

    Deletes and recreates all of the AWS resources (for example: the Auto Scaling group, load balancer, etc.) for a specified environment and forces a restart.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = RebuildEnvironmentMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_request_environment_info(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_request_environment_info

    &lt;p&gt;Initiates a request to compile the specified type of information of the deployed environment.&lt;/p&gt; &lt;p&gt; Setting the &lt;code&gt;InfoType&lt;/code&gt; to &lt;code&gt;tail&lt;/code&gt; compiles the last lines from the application server log files of every Amazon EC2 instance in your environment. &lt;/p&gt; &lt;p&gt; Setting the &lt;code&gt;InfoType&lt;/code&gt; to &lt;code&gt;bundle&lt;/code&gt; compresses the application server log files for every Amazon EC2 instance into a &lt;code&gt;.zip&lt;/code&gt; file. Legacy and .NET containers do not support bundle logs. &lt;/p&gt; &lt;p&gt; Use &lt;a&gt;RetrieveEnvironmentInfo&lt;/a&gt; to obtain the set of logs. &lt;/p&gt; &lt;p&gt;Related Topics&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;RetrieveEnvironmentInfo&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = RequestEnvironmentInfoMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_restart_app_server(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_restart_app_server

    Causes the environment to restart the application container server running on each Amazon EC2 instance.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = RestartAppServerMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_retrieve_environment_info(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_retrieve_environment_info

    &lt;p&gt;Retrieves the compiled information from a &lt;a&gt;RequestEnvironmentInfo&lt;/a&gt; request.&lt;/p&gt; &lt;p&gt;Related Topics&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;RequestEnvironmentInfo&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = RetrieveEnvironmentInfoMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_swap_environment_cnames(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_swap_environment_cnames

    Swaps the CNAMEs of two environments.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = SwapEnvironmentCNAMEsMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_terminate_environment(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_terminate_environment

    Terminates the specified environment.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = TerminateEnvironmentMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_application(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_application

    &lt;p&gt;Updates the specified application to have the specified properties.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If a property (for example, &lt;code&gt;description&lt;/code&gt;) is not provided, the value remains unchanged. To clear these properties, specify an empty string.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateApplicationMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_application_resource_lifecycle(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_application_resource_lifecycle

    Modifies lifecycle settings for an application.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateApplicationResourceLifecycleMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_application_version(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_application_version

    &lt;p&gt;Updates the specified application version to have the specified properties.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If a property (for example, &lt;code&gt;description&lt;/code&gt;) is not provided, the value remains unchanged. To clear properties, specify an empty string.&lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateApplicationVersionMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_configuration_template(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_configuration_template

    &lt;p&gt;Updates the specified configuration template to have the specified properties or configuration option values.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If a property (for example, &lt;code&gt;ApplicationName&lt;/code&gt;) is not provided, its value remains unchanged. To clear such properties, specify an empty string.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Related Topics&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeConfigurationOptions&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateConfigurationTemplateMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_environment(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_environment

    &lt;p&gt;Updates the environment description, deploys a new application version, updates the configuration settings to an entirely new configuration template, or updates select configuration option values in the running environment.&lt;/p&gt; &lt;p&gt; Attempting to update both the release and configuration is not allowed and AWS Elastic Beanstalk returns an &lt;code&gt;InvalidParameterCombination&lt;/code&gt; error. &lt;/p&gt; &lt;p&gt; When updating the configuration settings to a new template or individual settings, a draft configuration is created and &lt;a&gt;DescribeConfigurationSettings&lt;/a&gt; for this environment returns two setting descriptions with different &lt;code&gt;DeploymentStatus&lt;/code&gt; values. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateEnvironmentMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_tags_for_resource(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_tags_for_resource

    &lt;p&gt;Update the list of tags applied to an AWS Elastic Beanstalk resource. Two lists can be passed: &lt;code&gt;TagsToAdd&lt;/code&gt; for tags to add or update, and &lt;code&gt;TagsToRemove&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Elastic Beanstalk supports tagging of all of its resources. For details about resource tagging, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-tagging-resources.html\&quot;&gt;Tagging Application Resources&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you create a custom IAM user policy to control permission to this operation, specify one of the following two virtual actions (or both) instead of the API operation name:&lt;/p&gt; &lt;dl&gt; &lt;dt&gt;elasticbeanstalk:AddTags&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Controls permission to call &lt;code&gt;UpdateTagsForResource&lt;/code&gt; and pass a list of tags to add in the &lt;code&gt;TagsToAdd&lt;/code&gt; parameter.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;elasticbeanstalk:RemoveTags&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Controls permission to call &lt;code&gt;UpdateTagsForResource&lt;/code&gt; and pass a list of tag keys to remove in the &lt;code&gt;TagsToRemove&lt;/code&gt; parameter.&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt; &lt;p&gt;For details about creating a custom user policy, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#AWSHowTo.iam.policies\&quot;&gt;Creating a Custom User Policy&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateTagsForResourceMessage.from_dict(body)
    return web.Response(status=200)


async def p_ost_validate_configuration_settings(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_validate_configuration_settings

    &lt;p&gt;Takes a set of configuration settings and either a configuration template or environment, and determines whether those values are valid.&lt;/p&gt; &lt;p&gt;This action returns a list of messages indicating any errors or warnings associated with the selection of option values.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ValidateConfigurationSettingsMessage.from_dict(body)
    return web.Response(status=200)
