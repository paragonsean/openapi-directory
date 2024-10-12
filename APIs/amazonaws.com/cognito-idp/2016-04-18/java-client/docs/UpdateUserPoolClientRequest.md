

# UpdateUserPoolClientRequest

Represents the request to update the user pool client.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**userPoolId** | [**String**](String.md) |  |  |
|**clientId** | [**String**](String.md) |  |  |
|**clientName** | [**String**](String.md) |  |  [optional] |
|**refreshTokenValidity** | [**Integer**](Integer.md) |  |  [optional] |
|**accessTokenValidity** | [**Integer**](Integer.md) |  |  [optional] |
|**idTokenValidity** | [**Integer**](Integer.md) |  |  [optional] |
|**tokenValidityUnits** | [**UpdateUserPoolClientRequestTokenValidityUnits**](UpdateUserPoolClientRequestTokenValidityUnits.md) |  |  [optional] |
|**readAttributes** | [**List**](List.md) |  |  [optional] |
|**writeAttributes** | [**List**](List.md) |  |  [optional] |
|**explicitAuthFlows** | [**List**](List.md) |  |  [optional] |
|**supportedIdentityProviders** | [**List**](List.md) |  |  [optional] |
|**callbackURLs** | [**List**](List.md) |  |  [optional] |
|**logoutURLs** | [**List**](List.md) |  |  [optional] |
|**defaultRedirectURI** | [**String**](String.md) |  |  [optional] |
|**allowedOAuthFlows** | [**List**](List.md) |  |  [optional] |
|**allowedOAuthScopes** | [**List**](List.md) |  |  [optional] |
|**allowedOAuthFlowsUserPoolClient** | [**Boolean**](Boolean.md) |  |  [optional] |
|**analyticsConfiguration** | [**UpdateUserPoolClientRequestAnalyticsConfiguration**](UpdateUserPoolClientRequestAnalyticsConfiguration.md) |  |  [optional] |
|**preventUserExistenceErrors** | [**PreventUserExistenceErrorTypes**](PreventUserExistenceErrorTypes.md) |  |  [optional] |
|**enableTokenRevocation** | [**Boolean**](Boolean.md) |  |  [optional] |
|**enablePropagateAdditionalUserContextData** | [**Boolean**](Boolean.md) |  |  [optional] |
|**authSessionValidity** | [**Integer**](Integer.md) |  |  [optional] |



