# NumberInsightApi.GetNumberInsightAsync200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorText** | **String** | The status description of your request. Note: This field is equivalent to &#x60;status_message&#x60; field in the other endpoints | [optional] 
**number** | **String** | The &#x60;number&#x60; in your request | [optional] 
**remainingBalance** | **String** | Your account balance in EUR after this request. | [optional] 
**requestId** | **String** | The unique identifier for your request. This is a alphanumeric string up to 40 characters. | [optional] 
**requestPrice** | **String** | If there is an internal lookup error, the &#x60;refund_price&#x60; will reflect the lookup price. If &#x60;cnam&#x60; is requested for a non-US number the &#x60;refund_price&#x60; will reflect the &#x60;cnam&#x60; price. If both of these conditions occur, &#x60;refund_price&#x60; is the sum of the lookup price and &#x60;cnam&#x60; price. | [optional] 
**status** | [**NiStandardAdvancedStatus**](NiStandardAdvancedStatus.md) |  | [optional] 


