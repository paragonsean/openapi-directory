# CrmCards.IntegratorCardPayloadResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allItemsLinkUrl** | **String** | URL to a page the integrator has built that displays all details for this card. This URL will be displayed to users under a &#x60;See more [x]&#x60; link if there are more than five items in your response, where &#x60;[x]&#x60; is the value of &#x60;itemLabel&#x60;. | [optional] 
**cardLabel** | **String** | The label to be used for the &#x60;allItemsLinkUrl&#x60; link (e.g. &#39;See more tickets&#39;). If not provided, this falls back to the card&#39;s title. | [optional] 
**responseVersion** | **String** |  | [optional] 
**sections** | [**[IntegratorObjectResult]**](IntegratorObjectResult.md) | A list of up to five valid card sub categories. | [optional] 
**topLevelActions** | [**TopLevelActions**](TopLevelActions.md) |  | [optional] 
**totalCount** | **Number** | The total number of card properties that will be sent in this response. | 



## Enum: ResponseVersionEnum


* `v1` (value: `"v1"`)

* `v3` (value: `"v3"`)




