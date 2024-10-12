

# Connector


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authOnly** | **Boolean** | Indicates whether a connector only supports authentication. In this case the connector is not mapped to a Unified API, but can be used with the Proxy API |  [optional] [readonly] |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) | Type of authorization used by the connector |  [optional] [readonly] |
|**blindMapped** | **Boolean** | Set to &#x60;true&#x60; when connector was implemented from downstream docs only and without API access. This state indicates that integration will require Apideck support, and access to downstream API to validate mapping quality. |  [optional] [readonly] |
|**configurableResources** | **List&lt;String&gt;** | List of resources that have settings that can be configured. |  [optional] |
|**customScopes** | **Boolean** | Set to &#x60;true&#x60; when connector allows the definition of custom scopes. |  [optional] [readonly] |
|**description** | **String** | A description of the object. |  [optional] |
|**docs** | [**List&lt;ConnectorDoc&gt;**](ConnectorDoc.md) |  |  [optional] |
|**freeTrialAvailable** | **Boolean** | Set to &#x60;true&#x60; when the connector offers a free trial. Use &#x60;signup_url&#x60; to sign up for a free trial |  [optional] |
|**hasSandboxCredentials** | **Boolean** | Indicates whether Apideck Sandbox OAuth credentials are available. |  [optional] |
|**iconUrl** | **URI** | Link to a small square icon for the connector. |  [optional] |
|**id** | **String** | ID of the connector. |  [optional] [readonly] |
|**logoUrl** | **URI** | Link to the full logo for the connector. |  [optional] |
|**name** | **String** | Name of the connector. |  [optional] |
|**oauthCredentialsSource** | [**OauthCredentialsSourceEnum**](#OauthCredentialsSourceEnum) | Location of the OAuth client credentials. For most connectors the OAuth client credentials are stored on integration and managed by the application owner. For others they are stored on connection and managed by the consumer in Vault. |  [optional] [readonly] |
|**oauthGrantType** | [**OauthGrantTypeEnum**](#OauthGrantTypeEnum) | OAuth grant type used by the connector. More info: https://oauth.net/2/grant-types |  [optional] [readonly] |
|**oauthScopes** | [**List&lt;ConnectorOauthScopesInner&gt;**](ConnectorOauthScopesInner.md) | List of OAuth Scopes available for this connector. |  [optional] |
|**partnerSignupUrl** | **URI** | Link to the connector&#39;s partner program signup page. |  [optional] |
|**schemaSupport** | [**SchemaSupport**](SchemaSupport.md) |  |  [optional] |
|**serviceId** | **String** | Service provider identifier |  [optional] |
|**settings** | [**List&lt;ConnectorSetting&gt;**](ConnectorSetting.md) |  |  [optional] |
|**signupUrl** | **URI** | Link to the connector&#39;s signup page. |  [optional] |
|**status** | **ConnectorStatus** |  |  [optional] |
|**supportedEvents** | [**List&lt;ConnectorEvent&gt;**](ConnectorEvent.md) | List of events that are supported on the connector across all Unified APIs. |  [optional] |
|**supportedResources** | [**List&lt;LinkedConnectorResource&gt;**](LinkedConnectorResource.md) | List of resources that are supported on the connector. |  [optional] |
|**tlsSupport** | [**ConnectorTlsSupport**](ConnectorTlsSupport.md) |  |  [optional] |
|**unifiedApis** | [**List&lt;ConnectorUnifiedApisInner&gt;**](ConnectorUnifiedApisInner.md) | List of Unified APIs that feature this connector. |  [optional] |
|**webhookSupport** | [**WebhookSupport**](WebhookSupport.md) |  |  [optional] |
|**websiteUrl** | **URI** | Link to the connector&#39;s website. |  [optional] |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| OAUTH2 | &quot;oauth2&quot; |
| API_KEY | &quot;apiKey&quot; |
| BASIC | &quot;basic&quot; |
| CUSTOM | &quot;custom&quot; |
| NONE | &quot;none&quot; |



## Enum: OauthCredentialsSourceEnum

| Name | Value |
|---- | -----|
| INTEGRATION | &quot;integration&quot; |
| CONNECTION | &quot;connection&quot; |



## Enum: OauthGrantTypeEnum

| Name | Value |
|---- | -----|
| AUTHORIZATION_CODE | &quot;authorization_code&quot; |
| CLIENT_CREDENTIALS | &quot;client_credentials&quot; |
| PASSWORD | &quot;password&quot; |



