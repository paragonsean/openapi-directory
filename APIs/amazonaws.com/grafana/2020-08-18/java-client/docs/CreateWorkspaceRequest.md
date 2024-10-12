

# CreateWorkspaceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountAccessType** | [**AccountAccessTypeEnum**](#AccountAccessTypeEnum) | Specifies whether the workspace can access Amazon Web Services resources in this Amazon Web Services account only, or whether it can also access Amazon Web Services resources in other accounts in the same organization. If you specify &lt;code&gt;ORGANIZATION&lt;/code&gt;, you must specify which organizational units the workspace can access in the &lt;code&gt;workspaceOrganizationalUnits&lt;/code&gt; parameter. |  |
|**authenticationProviders** | **List&lt;AuthenticationProviderTypes&gt;** | Specifies whether this workspace uses SAML 2.0, IAM Identity Center (successor to Single Sign-On), or both to authenticate users for using the Grafana console within a workspace. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG.html\&quot;&gt;User authentication in Amazon Managed Grafana&lt;/a&gt;. |  |
|**clientToken** | **String** | A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request. |  [optional] |
|**_configuration** | **String** | The configuration string for the workspace that you create. For more information about the format and configuration options available, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html\&quot;&gt;Working in your Grafana workspace&lt;/a&gt;. |  [optional] |
|**grafanaVersion** | **String** | &lt;p&gt;Specifies the version of Grafana to support in the new workspace.&lt;/p&gt; &lt;p&gt;To get a list of supported version, use the &lt;code&gt;ListVersions&lt;/code&gt; operation.&lt;/p&gt; |  [optional] |
|**networkAccessControl** | [**CreateWorkspaceRequestNetworkAccessControl**](CreateWorkspaceRequestNetworkAccessControl.md) |  |  [optional] |
|**organizationRoleName** | **String** | The name of an IAM role that already exists to use with Organizations to access Amazon Web Services data sources and notification channels in other accounts in an organization. |  [optional] |
|**permissionType** | [**PermissionTypeEnum**](#PermissionTypeEnum) | &lt;p&gt;When creating a workspace through the Amazon Web Services API, CLI or Amazon Web Services CloudFormation, you must manage IAM roles and provision the permissions that the workspace needs to use Amazon Web Services data sources and notification channels.&lt;/p&gt; &lt;p&gt;You must also specify a &lt;code&gt;workspaceRoleArn&lt;/code&gt; for a role that you will manage for the workspace to use when accessing those datasources and notification channels.&lt;/p&gt; &lt;p&gt;The ability for Amazon Managed Grafana to create and update IAM roles on behalf of the user is supported only in the Amazon Managed Grafana console, where this value may be set to &lt;code&gt;SERVICE_MANAGED&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Use only the &lt;code&gt;CUSTOMER_MANAGED&lt;/code&gt; permission type when creating a workspace with the API, CLI or Amazon Web Services CloudFormation. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html\&quot;&gt;Amazon Managed Grafana permissions and policies for Amazon Web Services data sources and notification channels&lt;/a&gt;.&lt;/p&gt; |  |
|**stackSetName** | **String** | The name of the CloudFormation stack set to use to generate IAM roles to be used for this workspace. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The list of tags associated with the workspace. |  [optional] |
|**vpcConfiguration** | [**CreateWorkspaceRequestVpcConfiguration**](CreateWorkspaceRequestVpcConfiguration.md) |  |  [optional] |
|**workspaceDataSources** | **List&lt;DataSourceType&gt;** | This parameter is for internal use only, and should not be used. |  [optional] |
|**workspaceDescription** | **String** | &lt;p&gt;A description for the workspace. This is used only to help you identify this workspace.&lt;/p&gt; &lt;p&gt;Pattern: &lt;code&gt;^[\\\\p{L}\\\\p{Z}\\\\p{N}\\\\p{P}]{0,2048}$&lt;/code&gt; &lt;/p&gt; |  [optional] |
|**workspaceName** | **String** | The name for the workspace. It does not have to be unique. |  [optional] |
|**workspaceNotificationDestinations** | **List&lt;NotificationDestinationType&gt;** | Specify the Amazon Web Services notification channels that you plan to use in this workspace. Specifying these data sources here enables Amazon Managed Grafana to create IAM roles and permissions that allow Amazon Managed Grafana to use these channels. |  [optional] |
|**workspaceOrganizationalUnits** | **List&lt;String&gt;** | Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization. |  [optional] |
|**workspaceRoleArn** | **String** | Specified the IAM role that grants permissions to the Amazon Web Services resources that the workspace will view data from, including both data sources and notification channels. You are responsible for managing the permissions for this role as new data sources or notification channels are added.  |  [optional] |



## Enum: AccountAccessTypeEnum

| Name | Value |
|---- | -----|
| CURRENT_ACCOUNT | &quot;CURRENT_ACCOUNT&quot; |
| ORGANIZATION | &quot;ORGANIZATION&quot; |



## Enum: PermissionTypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER_MANAGED | &quot;CUSTOMER_MANAGED&quot; |
| SERVICE_MANAGED | &quot;SERVICE_MANAGED&quot; |



