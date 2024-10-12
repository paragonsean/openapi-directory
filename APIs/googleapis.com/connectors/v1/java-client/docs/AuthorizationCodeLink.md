

# AuthorizationCodeLink

This configuration captures the details required to render an authorization link for the OAuth Authorization Code Flow.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | The client ID assigned to the Google Cloud Connectors OAuth app for the connector data source. |  [optional] |
|**enablePkce** | **Boolean** | Whether to enable PKCE for the auth code flow. |  [optional] |
|**scopes** | **List&lt;String&gt;** | The scopes for which the user will authorize Google Cloud Connectors on the connector data source. |  [optional] |
|**uri** | **String** | The base URI the user must click to trigger the authorization code login flow. |  [optional] |



