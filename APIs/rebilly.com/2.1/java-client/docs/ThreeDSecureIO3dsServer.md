

# ThreeDSecureIO3dsServer

ThreeDSecureIO3dsServer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **ThreeDSecureServerName** |  |  |
|**merchantAcquirerBinMastercard** | **String** | Mastercard Acquirer BIN. |  |
|**merchantAcquirerBinVisa** | **String** | Visa Acquirer BIN. |  |
|**merchantCountry** | **String** | Merchant Country ISO Alpha-2 Code. |  |
|**merchantId** | **String** | Merchant Id. |  |
|**merchantName** | **String** | Merchant Name. |  |
|**merchantUrl** | **String** | Merchant URL. |  |
|**transactionType** | [**TransactionTypeEnum**](#TransactionTypeEnum) | 01 - Goods/Service Purchase 03 - Check Acceptance 10 - Account Funding 11 - Quasi-Cash Transaction 28 - Prepaid Activation and Load  Identifies the type of transaction being authenticated.  |  [optional] |
|**v1** | **Boolean** | Value determines if requests can use version 1 of 3DS. In case both v1 and v2 are enabled it will prefer v2. If v2 is not supported for the issuer, it will coalesce to v1.  |  [optional] |
|**v2** | **Boolean** | Value determines if requests will attempt version 2 of 3DS. In case both v1 and v2 are enabled it will prefer v2. If v2 is not supported for the issuer, it will coalesce to v1.  |  [optional] |



## Enum: TransactionTypeEnum

| Name | Value |
|---- | -----|
| _01 | &quot;01&quot; |
| _03 | &quot;03&quot; |
| _10 | &quot;10&quot; |
| _11 | &quot;11&quot; |
| _28 | &quot;28&quot; |



