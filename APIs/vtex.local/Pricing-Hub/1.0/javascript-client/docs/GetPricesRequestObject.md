# PricingHub.GetPricesRequestObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**utmCampaign** | **String** | Campaign name, represented by the &#x60;utm_campaign&#x60; value in the URL that led to the order. If there is no value, use &#x60;null&#x60; | [optional] [default to &#39;summer&#39;]
**utmInternalCampaign** | **String** | Internal campaign name, represented by the &#x60;utmi_cp&#x60; value in the URL that led to the order. If there is no value, use &#x60;null&#x60; | [optional] [default to &#39;sale&#39;]
**utmMedium** | **String** | Medium that indicates what type of traffic the customer originated from, represented by the &#x60;utm_medium&#x60; value in the URL that led to the order. If there is no value, use &#x60;null&#x60; | [optional] [default to &#39;social&#39;]
**utmSource** | **String** | Traffic source, indicates where the traffic originated from according to the &#x60;utm_source&#x60; value in the URL that led to the order. If there is no value, use &#x60;null&#x60; | [optional] [default to &#39;facebook&#39;]
**email** | **String** | The customer&#39;s email address. If there is no value, use an empty string | [default to &#39;customer@email.com&#39;]
**items** | [**[ItemsInner]**](ItemsInner.md) | The list of items that are to be priced by Pricing Hub | 
**salesChannel** | **String** | Represents Checkout&#39;s sales channel | [default to &#39;1&#39;]


