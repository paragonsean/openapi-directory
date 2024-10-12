

# IntegratorCardPayloadResponse

The card details payload, sent to HubSpot by an app in response to a data fetch request when a user visits a CRM record page.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allItemsLinkUrl** | **String** | URL to a page the integrator has built that displays all details for this card. This URL will be displayed to users under a &#x60;See more [x]&#x60; link if there are more than five items in your response, where &#x60;[x]&#x60; is the value of &#x60;itemLabel&#x60;. |  [optional] |
|**cardLabel** | **String** | The label to be used for the &#x60;allItemsLinkUrl&#x60; link (e.g. &#39;See more tickets&#39;). If not provided, this falls back to the card&#39;s title. |  [optional] |
|**responseVersion** | [**ResponseVersionEnum**](#ResponseVersionEnum) |  |  [optional] |
|**sections** | [**List&lt;IntegratorObjectResult&gt;**](IntegratorObjectResult.md) | A list of up to five valid card sub categories. |  [optional] |
|**topLevelActions** | [**TopLevelActions**](TopLevelActions.md) |  |  [optional] |
|**totalCount** | **Integer** | The total number of card properties that will be sent in this response. |  |



## Enum: ResponseVersionEnum

| Name | Value |
|---- | -----|
| V1 | &quot;v1&quot; |
| V3 | &quot;v3&quot; |



