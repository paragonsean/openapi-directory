

# RecipientTransferProperties

Transfer Details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedProductType** | **List&lt;EligibleProductType&gt;** | Type of subscriptions that can be transferred. |  [optional] [readonly] |
|**canceledBy** | **String** | Email Id who user canceled the transfer. |  [optional] [readonly] |
|**creationTime** | **OffsetDateTime** | Transfer creation time. |  [optional] [readonly] |
|**detailedTransferStatus** | [**List&lt;DetailedTransferStatus&gt;**](DetailedTransferStatus.md) | Detailed transfer status. |  [optional] [readonly] |
|**expirationTime** | **OffsetDateTime** | Transfer expiration time. |  [optional] [readonly] |
|**initiatorEmailId** | **String** | Email Id of initiator of transfer. |  [optional] [readonly] |
|**lastModifiedTime** | **OffsetDateTime** | Transfer last modification time. |  [optional] [readonly] |
|**recipientEmailId** | **String** | Email Id of recipient of transfer. |  [optional] [readonly] |
|**transferStatus** | **TransferStatus** |  |  [optional] |



