

# Payee


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderName** | **String** | The name on the payee bank account. |  [optional] |
|**accountName** | **String** | The alias attributed to the payee, usually set by the user when creating the payee. |  [optional] |
|**accountNumber** | **String** | The Account Number of the account if currency is GBP. |  [optional] |
|**bic** | **String** | The BIC of the account if currency is EUR. |  [optional] |
|**createdBy** | [**CreatedByEnum**](#CreatedByEnum) | The creation source of the payee. |  [optional] |
|**currency** | [**Currency**](Currency.md) |  |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date the payee was created. ISO Date Time. |  [optional] |
|**iban** | **String** | The IBAN of the account if currency is EUR. |  [optional] |
|**id** | **Long** | Identifier for the fire.com payee bank account (assigned by fire.com). |  [optional] |
|**nsc** | **String** | The Sort Code of the account if currency is GBP. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the payee. Only payees in LIVE status can be selected as a destination account for an outgoing payment.   * &#39;CREATED&#39; - The payee has been set-up via Bank Transfer Received, Direct Debit, or Open Banking. This payee must be converted to LIVE status to select as a destination account for an outgoing payment.   * &#39;LIVE&#39; - The payee can be selected as a destination account for an outgoing payment.   * &#39;CLOSED&#39;   * &#39;ARCHIVED&#39; - The payee has been deleted and must be added again to be selected as a destination account for an outgoing payment.  |  [optional] |



## Enum: CreatedByEnum

| Name | Value |
|---- | -----|
| CUSTOMER | &quot;CUSTOMER&quot; |
| LODGEMENT | &quot;LODGEMENT&quot; |
| DIRECT_DEBIT | &quot;DIRECT DEBIT&quot; |
| OPEN_BANKING | &quot;OPEN BANKING&quot; |
| FIRE_OPEN_PAYMENT | &quot;FIRE OPEN PAYMENT&quot; |
| FIRE_DIRECT | &quot;FIRE DIRECT&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;CREATED&quot; |
| LIVE | &quot;LIVE&quot; |
| CLOSED | &quot;CLOSED&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |



