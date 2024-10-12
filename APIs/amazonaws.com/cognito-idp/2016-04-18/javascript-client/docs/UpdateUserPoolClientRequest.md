# AmazonCognitoIdentityProvider.UpdateUserPoolClientRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**userPoolId** | **String** |  | 
**clientId** | **String** |  | 
**clientName** | **String** |  | [optional] 
**refreshTokenValidity** | **Number** |  | [optional] 
**accessTokenValidity** | **Number** |  | [optional] 
**idTokenValidity** | **Number** |  | [optional] 
**tokenValidityUnits** | [**UpdateUserPoolClientRequestTokenValidityUnits**](UpdateUserPoolClientRequestTokenValidityUnits.md) |  | [optional] 
**readAttributes** | **Array** |  | [optional] 
**writeAttributes** | **Array** |  | [optional] 
**explicitAuthFlows** | **Array** |  | [optional] 
**supportedIdentityProviders** | **Array** |  | [optional] 
**callbackURLs** | **Array** |  | [optional] 
**logoutURLs** | **Array** |  | [optional] 
**defaultRedirectURI** | **String** |  | [optional] 
**allowedOAuthFlows** | **Array** |  | [optional] 
**allowedOAuthScopes** | **Array** |  | [optional] 
**allowedOAuthFlowsUserPoolClient** | **Boolean** |  | [optional] 
**analyticsConfiguration** | [**UpdateUserPoolClientRequestAnalyticsConfiguration**](UpdateUserPoolClientRequestAnalyticsConfiguration.md) |  | [optional] 
**preventUserExistenceErrors** | [**PreventUserExistenceErrorTypes**](PreventUserExistenceErrorTypes.md) |  | [optional] 
**enableTokenRevocation** | **Boolean** |  | [optional] 
**enablePropagateAdditionalUserContextData** | **Boolean** |  | [optional] 
**authSessionValidity** | **Number** |  | [optional] 


