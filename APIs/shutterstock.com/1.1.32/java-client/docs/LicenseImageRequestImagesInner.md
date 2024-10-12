

# LicenseImageRequestImagesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authCookie** | [**Cookie**](Cookie.md) |  |  [optional] |
|**customDimensions** | [**CustomSizeDimensions**](CustomSizeDimensions.md) |  |  [optional] |
|**editorialAcknowledgement** | **Boolean** | Set to true to acknowledge the editorial agreement |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | (Deprecated) Image format to download |  [optional] |
|**imageId** | **String** | Image ID |  |
|**metadata** | **Object** | Additional information for license requests for enterprise accounts and API subscriptions, 4 fields maximum; which fields are required is set by the account holder |  [optional] |
|**price** | **BigDecimal** | For revenue-sharing transactions, the final cost to the end customer as a floating-point number in the transaction currency, such as 12.34 |  [optional] |
|**searchId** | **String** | ID of the search that led to this licensing transaction |  [optional] |
|**showModal** | **Boolean** | (Deprecated) |  [optional] |
|**size** | [**SizeEnum**](#SizeEnum) | Image size to download |  [optional] |
|**subscriptionId** | **String** | ID of the subscription to use for the download. |  [optional] |
|**verificationCode** | **String** | (Deprecated) |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| EPS | &quot;eps&quot; |



## Enum: SizeEnum

| Name | Value |
|---- | -----|
| VECTOR | &quot;vector&quot; |



