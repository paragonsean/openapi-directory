

# ThreeDSecure


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource. |  [optional] [readonly] |
|**amount** | **Double** | Transaction amount. |  |
|**cavv** | **String** | The 3D Secure entry cardholder authentication verification value. |  [optional] |
|**createdTime** | **OffsetDateTime** | The 3D Secure entry created time. |  [optional] [readonly] |
|**currency** | **String** | ISO 4217 alphabetic currency code. |  |
|**customerId** | **String** | Related customer ID. |  |
|**eci** | **Integer** | The 3D Secure entry electronic commerce indicator. |  [optional] |
|**enrolled** | [**EnrolledEnum**](#EnrolledEnum) | Is the cardholder enrolled in 3DSecure. |  |
|**enrollmentEci** | **String** | The 3D Secure entry enrollment eci. |  |
|**gatewayAccountId** | **String** | Related gateway account ID. |  |
|**id** | **String** | The 3D Secure entry identifier string. |  [optional] [readonly] |
|**payerAuthResponseStatus** | [**PayerAuthResponseStatusEnum**](#PayerAuthResponseStatusEnum) | The 3D Secure entry Auth Response Status. |  [optional] |
|**paymentCardId** | **String** | Related payment card ID. |  |
|**signatureVerification** | [**SignatureVerificationEnum**](#SignatureVerificationEnum) | If signature was verified. |  [optional] |
|**websiteId** | **String** | Related Website ID. |  |
|**xid** | **String** | The 3D Secure entry transaction Id. |  [optional] |



## Enum: EnrolledEnum

| Name | Value |
|---- | -----|
| Y | &quot;Y&quot; |
| N | &quot;N&quot; |
| U | &quot;U&quot; |



## Enum: PayerAuthResponseStatusEnum

| Name | Value |
|---- | -----|
| Y | &quot;Y&quot; |
| N | &quot;N&quot; |
| U | &quot;U&quot; |
| A | &quot;A&quot; |



## Enum: SignatureVerificationEnum

| Name | Value |
|---- | -----|
| Y | &quot;Y&quot; |
| N | &quot;N&quot; |



