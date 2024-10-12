

# GetPricesRequestObject


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**utmCampaign** | **String** | Campaign name, represented by the &#x60;utm_campaign&#x60; value in the URL that led to the order. If there is no value, use &#x60;null&#x60; |  [optional] |
|**utmInternalCampaign** | **String** | Internal campaign name, represented by the &#x60;utmi_cp&#x60; value in the URL that led to the order. If there is no value, use &#x60;null&#x60; |  [optional] |
|**utmMedium** | **String** | Medium that indicates what type of traffic the customer originated from, represented by the &#x60;utm_medium&#x60; value in the URL that led to the order. If there is no value, use &#x60;null&#x60; |  [optional] |
|**utmSource** | **String** | Traffic source, indicates where the traffic originated from according to the &#x60;utm_source&#x60; value in the URL that led to the order. If there is no value, use &#x60;null&#x60; |  [optional] |
|**email** | **String** | The customer&#39;s email address. If there is no value, use an empty string |  |
|**items** | [**List&lt;ItemsInner&gt;**](ItemsInner.md) | The list of items that are to be priced by Pricing Hub |  |
|**salesChannel** | **String** | Represents Checkout&#39;s sales channel |  |



