# CheckoutApi.AddCoupons200ResponseMarketingData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon** | **String** | Sending an existing coupon code in this field will return the corresponding discount in the purchase. Use the [cart simulation](https://developers.vtex.com/vtex-rest-api/reference/orderform#orderformsimulation) request to check which coupons might apply before placing the order. | [optional] [default to &#39;free-shipping&#39;]
**utmCampaign** | **String** | UTM campaign. | [optional] [default to &#39;Black friday&#39;]
**utmMedium** | **String** | UTM medium. | [optional] [default to &#39;CPC&#39;]
**utmSource** | **String** | UTM source. | [optional] [default to &#39;Facebook&#39;]
**utmiCampaign** | **String** | utmi_campaign (internal utm). | [optional] [default to &#39;utmi_campaign-exmaple&#39;]
**utmiPage** | **String** | utmi_page (internal utm). | [optional] [default to &#39;utmi_page-example&#39;]
**utmiPart** | **String** | utmi_part (internal utm). | [optional] [default to &#39;utmi_part-exmaple&#39;]


