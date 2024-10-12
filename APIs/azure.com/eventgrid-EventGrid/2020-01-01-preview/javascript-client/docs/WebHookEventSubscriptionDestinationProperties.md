# EventGridManagementClient.WebHookEventSubscriptionDestinationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureActiveDirectoryApplicationIdOrUri** | **String** | The Azure Active Directory Application ID or URI to get the access token that will be included as the bearer token in delivery requests. | [optional] 
**azureActiveDirectoryTenantId** | **String** | The Azure Active Directory Tenant ID to get the access token that will be included as the bearer token in delivery requests. | [optional] 
**endpointBaseUrl** | **String** | The base URL that represents the endpoint of the destination of an event subscription. | [optional] [readonly] 
**endpointUrl** | **String** | The URL that represents the endpoint of the destination of an event subscription. | [optional] 
**maxEventsPerBatch** | **Number** | Maximum number of events per batch. | [optional] 
**preferredBatchSizeInKilobytes** | **Number** | Preferred batch size in Kilobytes. | [optional] 


