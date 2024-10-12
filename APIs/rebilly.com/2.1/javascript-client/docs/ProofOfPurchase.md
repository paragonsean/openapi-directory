# RebillyRestApi.ProofOfPurchase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[CommonKycDocumentLinksInner]**](CommonKycDocumentLinksInner.md) | The links related to resource. | [optional] [readonly] 
**createdTime** | **Date** | Creation date/time. | [optional] [readonly] 
**documentSubtype** | [**KycDocumentSubtypes**](KycDocumentSubtypes.md) | Document subtype submitted for validation. | [optional] 
**documentType** | [**KycDocumentTypes**](KycDocumentTypes.md) | Document type submitted for validation, only identity-proof type is analyzed in an automated manner. | 
**fileId** | **String** | Linked file object id. | [optional] 
**fileIds** | **[String]** | Linked file object id&#39;s. | [optional] 
**id** | **String** | The resource ID. Defaults to UUID v4. | [optional] [readonly] 
**processedTime** | **Date** | Processing date/time. | [optional] [readonly] 
**rejectionReason** | [**KycDocumentRejection**](KycDocumentRejection.md) |  | [optional] 
**requestId** | **String** | KYC request identifier string. | [optional] [readonly] 
**status** | **String** | Status of the validation. | [readonly] 
**updatedTime** | **Date** | Latest update date/time. | [optional] [readonly] 
**customerId** | **String** | The сustomer&#39;s ID. | 
**matchLevel** | **Number** | The level of strictness for the document matches. | [optional] 
**notes** | **String** | Reviewer notes. | [optional] 
**reason** | **String** | Reason for uploading. | [optional] 
**reviewTime** | **Date** | Date and time of manual review. | [optional] [readonly] 
**reviewerId** | **String** | Reviewer&#39;s user ID. | [optional] [readonly] 
**reviewerName** | **String** | Reviewer&#39;s first and last name. | [optional] [readonly] 



## Enum: StatusEnum


* `pending` (value: `"pending"`)

* `in-progress` (value: `"in-progress"`)

* `accepted` (value: `"accepted"`)

* `rejected` (value: `"rejected"`)




