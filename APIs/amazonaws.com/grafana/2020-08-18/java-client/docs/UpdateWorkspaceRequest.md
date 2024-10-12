

# UpdateWorkspaceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountAccessType** | [**AccountAccessTypeEnum**](#AccountAccessTypeEnum) | Specifies whether the workspace can access Amazon Web Services resources in this Amazon Web Services account only, or whether it can also access Amazon Web Services resources in other accounts in the same organization. If you specify &lt;code&gt;ORGANIZATION&lt;/code&gt;, you must specify which organizational units the workspace can access in the &lt;code&gt;workspaceOrganizationalUnits&lt;/code&gt; parameter. |  [optional] |
|**networkAccessControl** | [**CreateWorkspaceRequestNetworkAccessControl**](CreateWorkspaceRequestNetworkAccessControl.md) |  |  [optional] |
|**organizationRoleName** | **String** | The name of an IAM role that already exists to use to access resources through Organizations. This can only be used with a workspace that has the &lt;code&gt;permissionType&lt;/code&gt; set to &lt;code&gt;CUSTOMER_MANAGED&lt;/code&gt;. |  [optional] |
|**permissionType** | [**PermissionTypeEnum**](#PermissionTypeEnum) | &lt;p&gt;Use this parameter if you want to change a workspace from &lt;code&gt;SERVICE_MANAGED&lt;/code&gt; to &lt;code&gt;CUSTOMER_MANAGED&lt;/code&gt;. This allows you to manage the permissions that the workspace uses to access datasources and notification channels. If the workspace is in a member Amazon Web Services account of an organization, and that account is not a delegated administrator account, and you want the workspace to access data sources in other Amazon Web Services accounts in the organization, you must choose &lt;code&gt;CUSTOMER_MANAGED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you specify this as &lt;code&gt;CUSTOMER_MANAGED&lt;/code&gt;, you must also specify a &lt;code&gt;workspaceRoleArn&lt;/code&gt; that the workspace will use for accessing Amazon Web Services resources.&lt;/p&gt; &lt;p&gt;For more information on the role and permissions needed, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html\&quot;&gt;Amazon Managed Grafana permissions and policies for Amazon Web Services data sources and notification channels&lt;/a&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;Do not use this to convert a &lt;code&gt;CUSTOMER_MANAGED&lt;/code&gt; workspace to &lt;code&gt;SERVICE_MANAGED&lt;/code&gt;. Do not include this parameter if you want to leave the workspace as &lt;code&gt;SERVICE_MANAGED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can convert a &lt;code&gt;CUSTOMER_MANAGED&lt;/code&gt; workspace to &lt;code&gt;SERVICE_MANAGED&lt;/code&gt; using the Amazon Managed Grafana console. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/userguide/AMG-datasource-and-notification.html\&quot;&gt;Managing permissions for data sources and notification channels&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; |  [optional] |
|**removeNetworkAccessConfiguration** | **Boolean** | &lt;p&gt;Whether to remove the network access configuration from the workspace.&lt;/p&gt; &lt;p&gt;Setting this to &lt;code&gt;true&lt;/code&gt; and providing a &lt;code&gt;networkAccessControl&lt;/code&gt; to set will return an error.&lt;/p&gt; &lt;p&gt;If you remove this configuration by setting this to &lt;code&gt;true&lt;/code&gt;, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.&lt;/p&gt; |  [optional] |
|**removeVpcConfiguration** | **Boolean** | &lt;p&gt;Whether to remove the VPC configuration from the workspace.&lt;/p&gt; &lt;p&gt;Setting this to &lt;code&gt;true&lt;/code&gt; and providing a &lt;code&gt;vpcConfiguration&lt;/code&gt; to set will return an error.&lt;/p&gt; |  [optional] |
|**stackSetName** | **String** | The name of the CloudFormation stack set to use to generate IAM roles to be used for this workspace. |  [optional] |
|**vpcConfiguration** | [**CreateWorkspaceRequestVpcConfiguration**](CreateWorkspaceRequestVpcConfiguration.md) |  |  [optional] |
|**workspaceDataSources** | **List&lt;DataSourceType&gt;** | This parameter is for internal use only, and should not be used. |  [optional] |
|**workspaceDescription** | **String** | A description for the workspace. This is used only to help you identify this workspace. |  [optional] |
|**workspaceName** | **String** | A new name for the workspace to update. |  [optional] |
|**workspaceNotificationDestinations** | **List&lt;NotificationDestinationType&gt;** | Specify the Amazon Web Services notification channels that you plan to use in this workspace. Specifying these data sources here enables Amazon Managed Grafana to create IAM roles and permissions that allow Amazon Managed Grafana to use these channels. |  [optional] |
|**workspaceOrganizationalUnits** | **List&lt;String&gt;** | Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization. |  [optional] |
|**workspaceRoleArn** | **String** | Specifies an IAM role that grants permissions to Amazon Web Services resources that the workspace accesses, such as data sources and notification channels. If this workspace has &lt;code&gt;permissionType&lt;/code&gt; &lt;code&gt;CUSTOMER_MANAGED&lt;/code&gt;, then this role is required. |  [optional] |



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



