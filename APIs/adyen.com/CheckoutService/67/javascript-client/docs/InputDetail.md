# AdyenCheckoutApi.InputDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | **{String: String}** | Configuration parameters for the required input. | [optional] 
**details** | [**[SubInputDetail]**](SubInputDetail.md) | Input details can also be provided recursively. | [optional] 
**inputDetails** | [**[SubInputDetail]**](SubInputDetail.md) | Input details can also be provided recursively (deprecated). | [optional] 
**itemSearchUrl** | **String** | In case of a select, the URL from which to query the items. | [optional] 
**items** | [**[Item]**](Item.md) | In case of a select, the items to choose from. | [optional] 
**key** | **String** | The value to provide in the result. | [optional] 
**optional** | **Boolean** | True if this input value is optional. | [optional] 
**type** | **String** | The type of the required input. | [optional] 
**value** | **String** | The value can be pre-filled, if available. | [optional] 


