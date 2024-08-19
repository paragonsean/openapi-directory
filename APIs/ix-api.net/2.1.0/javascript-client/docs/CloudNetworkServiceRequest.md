# IxApi.CloudNetworkServiceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAccount** | **String** | An account requires billing_information to be used as a &#x60;billing_account&#x60;. | 
**capacity** | **Number** | The capacity of the service in Mbps. When null, the maximum capacity will be used. | [optional] 
**cloudKey** | **String** |  | 
**consumingAccount** | **String** | The &#x60;id&#x60; of the account consuming a service.  Used to be &#x60;owning_customer&#x60;.  | 
**contractRef** | **String** | A reference to a contract. If no specific contract is used, a default MAY be chosen by the implementer.  | [optional] 
**externalRef** | **String** | Reference field, free to use for the API user. | [optional] 
**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  | 
**productOffering** | **String** |  | 
**purchaseOrder** | **String** | Purchase Order ID which will be displayed on the invoice.  | [optional] [default to &#39;&#39;]
**type** | **String** |  | 


