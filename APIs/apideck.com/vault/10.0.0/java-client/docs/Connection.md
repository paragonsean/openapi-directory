

# Connection


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authType** | **AuthType** |  |  [optional] |
|**authorizeUrl** | **String** | The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector&#39;s UI. Before you can use this URI, you must add &#x60;redirect_uri&#x60; as a query parameter to the &#x60;authorize_url&#x60;. Be sure to URL encode the &#x60;redirect_uri&#x60; part. Your users will be redirected to this &#x60;redirect_uri&#x60; after they granted access to your app in the connector&#39;s UI. |  [optional] [readonly] |
|**configurableResources** | **List&lt;String&gt;** |  |  [optional] [readonly] |
|**_configuration** | [**List&lt;ConnectionConfigurationInner&gt;**](ConnectionConfigurationInner.md) |  |  [optional] |
|**createdAt** | **BigDecimal** |  |  [optional] [readonly] |
|**customMappings** | [**List&lt;CustomMapping&gt;**](CustomMapping.md) | List of custom mappings configured for this connection |  [optional] |
|**enabled** | **Boolean** | Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API. |  [optional] |
|**formFields** | [**List&lt;FormField&gt;**](FormField.md) | The settings that are wanted to create a connection. |  [optional] [readonly] |
|**hasGuide** | **Boolean** | Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection). |  [optional] [readonly] |
|**icon** | **String** | A visual icon of the connection, that will be shown in the Vault |  [optional] [readonly] |
|**id** | **String** | The unique identifier of the connection. |  [optional] [readonly] |
|**integrationState** | **IntegrationState** |  |  [optional] |
|**logo** | **String** | The logo of the connection, that will be shown in the Vault |  [optional] [readonly] |
|**metadata** | **Map&lt;String, Object&gt;** | Attach your own consumer specific metadata |  [optional] |
|**name** | **String** | The name of the connection |  [optional] [readonly] |
|**oauthGrantType** | **OAuthGrantType** |  |  [optional] |
|**resourceSchemaSupport** | **List&lt;String&gt;** |  |  [optional] [readonly] |
|**resourceSettingsSupport** | **List&lt;String&gt;** |  |  [optional] [readonly] |
|**revokeUrl** | **String** | The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add &#x60;redirect_uri&#x60; as a query parameter. Your users will be redirected to this &#x60;redirect_uri&#x60; after they granted access to your app in the connector&#39;s UI. |  [optional] [readonly] |
|**schemaSupport** | **Boolean** |  |  [optional] [readonly] |
|**serviceId** | **String** | The ID of the service this connection belongs to. |  [optional] [readonly] |
|**settings** | **Map&lt;String, Object&gt;** | Connection settings. Values will persist to &#x60;form_fields&#x60; with corresponding id |  [optional] |
|**settingsRequiredForAuthorization** | **List&lt;String&gt;** | List of settings that are required to be configured on integration before authorization can occur |  [optional] [readonly] |
|**state** | **ConnectionState** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the connection. |  [optional] [readonly] |
|**subscriptions** | [**List&lt;WebhookSubscription&gt;**](WebhookSubscription.md) |  |  [optional] [readonly] |
|**tagLine** | **String** |  |  [optional] [readonly] |
|**unifiedApi** | **String** | The unified API category where the connection belongs to. |  [optional] [readonly] |
|**updatedAt** | **BigDecimal** |  |  [optional] [readonly] |
|**validationSupport** | **Boolean** |  |  [optional] [readonly] |
|**website** | **String** | The website URL of the connection |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| LIVE | &quot;live&quot; |
| UPCOMING | &quot;upcoming&quot; |
| REQUESTED | &quot;requested&quot; |



