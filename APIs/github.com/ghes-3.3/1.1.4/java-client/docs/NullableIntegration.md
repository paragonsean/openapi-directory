

# NullableIntegration

GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** |  |  [optional] |
|**clientSecret** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  |
|**description** | **String** |  |  |
|**events** | **List&lt;String&gt;** | The list of events for the GitHub app |  |
|**externalUrl** | **URI** |  |  |
|**htmlUrl** | **URI** |  |  |
|**id** | **Integer** | Unique identifier of the GitHub app |  |
|**installationsCount** | **Integer** | The number of installations associated with the GitHub app |  [optional] |
|**name** | **String** | The name of the GitHub app |  |
|**nodeId** | **String** |  |  |
|**owner** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |
|**pem** | **String** |  |  [optional] |
|**permissions** | **IntegrationPermissions** |  |  |
|**slug** | **String** | The slug name of the GitHub app |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  |
|**webhookSecret** | **String** |  |  [optional] |



