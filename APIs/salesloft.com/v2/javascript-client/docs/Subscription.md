# SalesLoftPlatform.Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callbackToken** | **String** | SalesLoft will include this token in the webhook event payload when calling your callback_url. It is strongly encouraged for your handler to verify this value in order to ensure the request came from SalesLoft. | [optional] 
**callbackUrl** | **String** | URL for your callback handler | [optional] 
**enabled** | **Boolean** | Is the Webhook Subscription enabled or not | [optional] 
**eventType** | **String** | Type of event the subscription is for | [optional] 
**id** | **Number** | ID for the Webhook Subscription | [optional] 
**tenantId** | **Number** | ID for the tenant to which user is assigned | [optional] 
**userGuid** | **String** | UUID of the user the token is associated with | [optional] 


