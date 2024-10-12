

# NiResponseXmlStandard

Standard

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callerIdentity** | [**NiResponseXmlStandardCallerIdentity**](NiResponseXmlStandardCallerIdentity.md) |  |  [optional] |
|**currentCarrier** | [**NiCurrentCarrierProperties**](NiCurrentCarrierProperties.md) |  |  [optional] |
|**error** | [**NiResponseXmlBasicError**](NiResponseXmlBasicError.md) |  |  [optional] |
|**internationalFormatNumber** | **String** | The &#x60;number&#x60; in your request in international format. |  [optional] |
|**localNumber** | [**NiResponseXmlBasicLocalNumber**](NiResponseXmlBasicLocalNumber.md) |  |  [optional] |
|**originalCarrier** | [**NiInitialCarrierProperties**](NiInitialCarrierProperties.md) |  |  [optional] |
|**ported** | [**NiResponseXmlStandardPorted**](NiResponseXmlStandardPorted.md) |  |  [optional] |
|**remainingBalance** | **String** | Your account balance in EUR after this request. |  [optional] |
|**requestId** | **String** | The unique identifier for your request. This is a alphanumeric string up to 40 characters. |  [optional] |
|**requestPrice** | **String** | If there is an internal lookup error, the &#x60;refund_price&#x60; will reflect the lookup price. If &#x60;cnam&#x60; is requested for a non-US number the &#x60;refund_price&#x60; will reflect the &#x60;cnam&#x60; price. If both of these conditions occur, &#x60;refund_price&#x60; is the sum of the lookup price and &#x60;cnam&#x60; price. |  [optional] |



