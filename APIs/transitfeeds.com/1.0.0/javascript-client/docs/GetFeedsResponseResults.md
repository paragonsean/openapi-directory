# TransitFeedsApi.GetFeedsResponseResults

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feeds** | [**[Feed]**](Feed.md) | An array of zero or more feeds. | [optional] 
**input** | **String** | If the status value is &#x60;MISSINGINPUT&#x60; or &#x60;INVALIDINPUT&#x60;, this field contains the name of the offending field. | [optional] 
**limit** | **Number** | The maximum number of feeds that can be returned in this response. If the final page is being requested then this number may be larger than the number of feeds returned in &#x60;feeds&#x60;.  | [optional] 
**numPages** | **Number** | The number of pages available, based on the &#x60;total&#x60; and &#x60;limit&#x60;. | [optional] 
**page** | **Number** | The page number being requested, based on the maximum number than can be returned from in &#x60;limit&#x60;. | [optional] 
**total** | **Number** | The total number of feeds found based on the request input. Note that this number may be larger than the number of feeds returned in &#x60;feeds&#x60;, based on the values for &#x60;limit&#x60; and &#x60;page&#x60;.  | [optional] 


