# PosTerminalManagementApi.Store

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) | The address of the store. | [optional] 
**description** | **String** | The description of the store. | [optional] 
**inStoreTerminals** | **[String]** | The list of terminals assigned to the store. | [optional] 
**merchantAccountCode** | **String** | The code of the merchant account. | [optional] 
**status** | **String** | The status of the store:  - &#x60;PreActive&#x60;: the store has been created, but not yet activated.   - &#x60;Active&#x60;: the store has been activated. This means you can process payments for this store.   - &#x60;Inactive&#x60;: the store is currently not active.   - &#x60;InactiveWithModifications&#x60;: the store is currently not active, but payment modifications such as refunds are possible.   - &#x60;Closed&#x60;: the store has been closed.  | [optional] 
**store** | **String** | The code of the store. | 


