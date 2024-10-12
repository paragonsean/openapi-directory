

# User

A Cloud SQL user resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dualPasswordType** | [**DualPasswordTypeEnum**](#DualPasswordTypeEnum) | Dual password status for the user. |  [optional] |
|**etag** | **String** | This field is deprecated and will be removed from a future version of the API. |  [optional] |
|**host** | **String** | Optional. The host from which the user can connect. For &#x60;insert&#x60; operations, host defaults to an empty string. For &#x60;update&#x60; operations, host is specified as part of the request URL. The host name cannot be updated after insertion. For a MySQL instance, it&#39;s required; for a PostgreSQL or SQL Server instance, it&#39;s optional. |  [optional] |
|**instance** | **String** | The name of the Cloud SQL instance. This does not include the project ID. Can be omitted for *update* because it is already specified on the URL. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#user&#x60;. |  [optional] |
|**name** | **String** | The name of the user in the Cloud SQL instance. Can be omitted for &#x60;update&#x60; because it is already specified in the URL. |  [optional] |
|**password** | **String** | The password for the user. |  [optional] |
|**passwordPolicy** | [**UserPasswordValidationPolicy**](UserPasswordValidationPolicy.md) |  |  [optional] |
|**project** | **String** | The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable. Can be omitted for *update* because it is already specified on the URL. |  [optional] |
|**sqlserverUserDetails** | [**SqlServerUserDetails**](SqlServerUserDetails.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The user type. It determines the method to authenticate the user during login. The default is the database&#39;s built-in user type. |  [optional] |



## Enum: DualPasswordTypeEnum

| Name | Value |
|---- | -----|
| DUAL_PASSWORD_TYPE_UNSPECIFIED | &quot;DUAL_PASSWORD_TYPE_UNSPECIFIED&quot; |
| NO_MODIFY_DUAL_PASSWORD | &quot;NO_MODIFY_DUAL_PASSWORD&quot; |
| NO_DUAL_PASSWORD | &quot;NO_DUAL_PASSWORD&quot; |
| DUAL_PASSWORD | &quot;DUAL_PASSWORD&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BUILT_IN | &quot;BUILT_IN&quot; |
| CLOUD_IAM_USER | &quot;CLOUD_IAM_USER&quot; |
| CLOUD_IAM_SERVICE_ACCOUNT | &quot;CLOUD_IAM_SERVICE_ACCOUNT&quot; |
| CLOUD_IAM_GROUP | &quot;CLOUD_IAM_GROUP&quot; |
| CLOUD_IAM_GROUP_USER | &quot;CLOUD_IAM_GROUP_USER&quot; |
| CLOUD_IAM_GROUP_SERVICE_ACCOUNT | &quot;CLOUD_IAM_GROUP_SERVICE_ACCOUNT&quot; |



