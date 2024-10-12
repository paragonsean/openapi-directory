# ApiManagementClient.QuotaCounterContract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**QuotaCounterValueContractProperties**](QuotaCounterValueContractProperties.md) |  | [optional] 
**counterKey** | **String** | The Key value of the Counter. Must not be empty. | 
**periodEndTime** | **Date** | The date of the end of Counter Period. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | 
**periodKey** | **String** | Identifier of the Period for which the counter was collected. Must not be empty. | 
**periodStartTime** | **Date** | The date of the start of Counter Period. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | 


