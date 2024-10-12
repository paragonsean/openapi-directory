

# GoogleCloudApigeeV1AppGroupApp

Response for [GetAppGroupApp].[AppGroupApps.GetAppGroupApp], [CreateAppGroupAppRequest].[AppGroupApp.CreateAppGroupAppRequest] and [DeleteAppGroupApp].[AppGroupApp.DeleteAppGroupApp]

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiProducts** | **List&lt;String&gt;** | List of API products associated with the AppGroup app. |  [optional] |
|**appGroup** | **String** | Immutable. Name of the parent AppGroup whose resource name format is of syntax (organizations/_*_/appgroups/_*). |  [optional] |
|**appId** | **String** | Immutable. ID of the AppGroup app. |  [optional] |
|**attributes** | [**List&lt;GoogleCloudApigeeV1Attribute&gt;**](GoogleCloudApigeeV1Attribute.md) | List of attributes for the AppGroup app. |  [optional] |
|**callbackUrl** | **String** | Callback URL used by OAuth 2.0 authorization servers to communicate authorization codes back to AppGroup apps. |  [optional] |
|**createdAt** | **String** | Output only. Time the AppGroup app was created in milliseconds since epoch. |  [optional] [readonly] |
|**credentials** | [**List&lt;GoogleCloudApigeeV1Credential&gt;**](GoogleCloudApigeeV1Credential.md) | Output only. Set of credentials for the AppGroup app consisting of the consumer key/secret pairs associated with the API products. |  [optional] [readonly] |
|**keyExpiresIn** | **String** | Immutable. Expiration time, in seconds, for the consumer key that is generated for the AppGroup app. If not set or left to the default value of &#x60;-1&#x60;, the API key never expires. The expiration time can&#39;t be updated after it is set. |  [optional] |
|**lastModifiedAt** | **String** | Output only. Time the AppGroup app was modified in milliseconds since epoch. |  [optional] [readonly] |
|**name** | **String** | Immutable. Name of the AppGroup app whose resource name format is of syntax (organizations/_*_/appgroups/_*_/apps/_*). |  [optional] |
|**scopes** | **List&lt;String&gt;** | Scopes to apply to the AppGroup app. The specified scopes must already exist for the API product that you associate with the AppGroup app. |  [optional] |
|**status** | **String** | Status of the App. Valid values include &#x60;approved&#x60; or &#x60;revoked&#x60;. |  [optional] |



