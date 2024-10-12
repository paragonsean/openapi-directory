

# PostPaymentsCrossBorderCreditTransfersConsentsParamsBodyRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aspspId** | **String** | Identification of ASPSP |  |
|**flags** | [**List&lt;FlagsEnum&gt;**](#List&lt;FlagsEnum&gt;) | Request information flags which can influence the behaviour or returned data |  [optional] |
|**merchant** | [**Merchant**](Merchant.md) |  |  [optional] |
|**tppRedirectURI** | **String** | Call back uri |  |
|**xRequestId** | **String** | Request id given by the client |  |



## Enum: List&lt;FlagsEnum&gt;

| Name | Value |
|---- | -----|
| RETURN_RAW_CONSENT | &quot;Return.Raw.Consent&quot; |



