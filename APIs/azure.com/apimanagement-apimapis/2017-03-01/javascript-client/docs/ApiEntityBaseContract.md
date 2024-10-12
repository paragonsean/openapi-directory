# ApiManagementClient.ApiEntityBaseContract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiRevision** | **String** | Describes the Revision of the Api. If no value is provided, default revision 1 is created | [optional] 
**apiVersion** | **String** | Indicates the Version identifier of the API if the API is versioned | [optional] 
**apiVersionSetId** | **String** | A resource identifier for the related ApiVersionSet. | [optional] 
**authenticationSettings** | [**ApiContractPropertiesAllOfAuthenticationSettings**](ApiContractPropertiesAllOfAuthenticationSettings.md) |  | [optional] 
**description** | **String** | Description of the API. May include HTML formatting tags. | [optional] 
**isCurrent** | **Boolean** | Indicates if API revision is current api revision. | [optional] [readonly] 
**isOnline** | **Boolean** | Indicates if API revision is accessible via the gateway. | [optional] [readonly] 
**subscriptionKeyParameterNames** | [**ApiEntityBaseContractSubscriptionKeyParameterNames**](ApiEntityBaseContractSubscriptionKeyParameterNames.md) |  | [optional] 
**type** | **String** | Type of API. | [optional] 



## Enum: TypeEnum


* `http` (value: `"http"`)

* `soap` (value: `"soap"`)




