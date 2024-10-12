# AmazonCognitoIdentityProvider.CreateUserPoolClientRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**userPoolId** | **String** |  | 
**clientName** | **String** |  | 
**generateSecret** | **Boolean** |  | [optional] 
**refreshTokenValidity** | **Number** |  | [optional] 
**accessTokenValidity** | **Number** |  | [optional] 
**idTokenValidity** | **Number** |  | [optional] 
**tokenValidityUnits** | [**CreateUserPoolClientRequestTokenValidityUnits**](CreateUserPoolClientRequestTokenValidityUnits.md) |  | [optional] 
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
**analyticsConfiguration** | [**CreateUserPoolClientRequestAnalyticsConfiguration**](CreateUserPoolClientRequestAnalyticsConfiguration.md) |  | [optional] 
**preventUserExistenceErrors** | [**PreventUserExistenceErrorTypes**](PreventUserExistenceErrorTypes.md) |  | [optional] 
**enableTokenRevocation** | **Boolean** |  | [optional] 
**enablePropagateAdditionalUserContextData** | **Boolean** |  | [optional] 
**authSessionValidity** | **Number** |  | [optional] 


