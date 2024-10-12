

# FundingAudit


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** | The amount funded |  [optional] |
|**currency** | **String** | The currency of the funding |  [optional] |
|**dateTime** | **OffsetDateTime** |  |  [optional] |
|**events** | [**List&lt;FundingEvent&gt;**](FundingEvent.md) |  |  [optional] |
|**fundingAccountName** | **String** |  |  [optional] |
|**fundingType** | **String** | Funding type. One of the following values: ACH, WIRE, EMBEDDED, BANK_TRANSFER |  [optional] |
|**sourceAccountName** | **String** |  |  [optional] |
|**status** | **String** | Status of the funding. One of the following values: PENDING, FAILED, CREDIT, DEBIT |  [optional] |
|**topupType** | **String** | Type of top up. One of the following values: AUTOMATIC, MANUAL |  [optional] |



