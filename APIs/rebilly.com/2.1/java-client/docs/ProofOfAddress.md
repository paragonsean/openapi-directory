

# ProofOfAddress


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;ProofOfAddressAllOfLinks&gt;**](ProofOfAddressAllOfLinks.md) | The links related to resource. |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | Creation date/time. |  [optional] [readonly] |
|**documentSubtype** | **KycDocumentSubtypes** | Document subtype submitted for validation. |  [optional] |
|**documentType** | **KycDocumentTypes** | Document type submitted for validation, only identity-proof type is analyzed in an automated manner. |  |
|**fileId** | **String** | Linked file object id. |  [optional] |
|**fileIds** | **List&lt;String&gt;** | Linked file object id&#39;s. |  [optional] |
|**id** | **String** | The resource ID. Defaults to UUID v4. |  [optional] [readonly] |
|**processedTime** | **OffsetDateTime** | Processing date/time. |  [optional] [readonly] |
|**rejectionReason** | [**KycDocumentRejection**](KycDocumentRejection.md) |  |  [optional] |
|**requestId** | **String** | KYC request identifier string. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the validation. |  [readonly] |
|**updatedTime** | **OffsetDateTime** | Latest update date/time. |  [optional] [readonly] |
|**customerId** | **String** | The сustomer&#39;s ID. |  |
|**matchLevel** | **Integer** | The level of strictness for the document matches. |  [optional] |
|**notes** | **String** | Reviewer notes. |  [optional] |
|**reason** | **String** | Reason for uploading. |  [optional] |
|**reviewTime** | **OffsetDateTime** | Date and time of manual review. |  [optional] [readonly] |
|**reviewerId** | **String** | Reviewer&#39;s user ID. |  [optional] [readonly] |
|**reviewerName** | **String** | Reviewer&#39;s first and last name. |  [optional] [readonly] |
|**documentMatches** | [**ProofOfAddressAllOfDocumentMatches**](ProofOfAddressAllOfDocumentMatches.md) |  |  [optional] |
|**parsedData** | [**ProofOfAddressAllOfDocumentMatches**](ProofOfAddressAllOfDocumentMatches.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| IN_PROGRESS | &quot;in-progress&quot; |
| ACCEPTED | &quot;accepted&quot; |
| REJECTED | &quot;rejected&quot; |



