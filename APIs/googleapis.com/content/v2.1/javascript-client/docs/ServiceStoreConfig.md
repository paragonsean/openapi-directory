# ContentApiForShopping.ServiceStoreConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cutoffConfig** | [**ServiceStoreConfigCutoffConfig**](ServiceStoreConfigCutoffConfig.md) |  | [optional] 
**serviceRadius** | [**Distance**](Distance.md) |  | [optional] 
**storeCodes** | **[String]** | A list of store codes that provide local delivery. If empty, then &#x60;store_service_type&#x60; must be &#x60;all_stores&#x60;, or an error is thrown. If not empty, then &#x60;store_service_type&#x60; must be &#x60;selected_stores&#x60;, or an error is thrown. | [optional] 
**storeServiceType** | **String** | Indicates whether all stores listed by this merchant provide local delivery or not. Acceptable values are &#x60;all stores&#x60; and &#x60;selected stores&#x60; | [optional] 


