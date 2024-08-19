

# OauthConnection

When a user authorizes your OAuth application, an OAuth Connection object is created.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp when the OAuth Connection was created. |  |
|**groupId** | **String** | The identifier of the Group that has authorized your OAuth application. |  |
|**id** | **String** | The OAuth Connection&#39;s identifier. |  |
|**status** | [**StatusEnum**](#StatusEnum) | Whether the connection is active. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;oauth_connection&#x60;. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| OAUTH_CONNECTION | &quot;oauth_connection&quot; |



