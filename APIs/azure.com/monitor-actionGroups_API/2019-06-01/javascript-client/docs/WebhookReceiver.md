# AzureActionGroups.WebhookReceiver

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifierUri** | **String** | Indicates the identifier uri for aad auth. | [optional] 
**name** | **String** | The name of the webhook receiver. Names must be unique across all receivers within an action group. | 
**objectId** | **String** | Indicates the webhook app object Id for aad auth. | [optional] 
**serviceUri** | **String** | The URI where webhooks should be sent. | 
**tenantId** | **String** | Indicates the tenant id for aad auth. | [optional] 
**useAadAuth** | **Boolean** | Indicates whether or not use AAD authentication. | [optional] [default to false]
**useCommonAlertSchema** | **Boolean** | Indicates whether to use common alert schema. | 


