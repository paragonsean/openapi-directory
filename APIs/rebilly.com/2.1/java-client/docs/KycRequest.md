

# KycRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTime** | **OffsetDateTime** | Creation date/time. |  [optional] [readonly] |
|**documents** | [**List&lt;CommonKycRequestDocumentsInner&gt;**](CommonKycRequestDocumentsInner.md) | Documents to be requested from customer. |  |
|**expirationTime** | **OffsetDateTime** | Expiration date/time. |  [optional] |
|**id** | **String** | The resource ID. Defaults to UUID v4. |  [optional] [readonly] |
|**redirectUrl** | **URI** | The URL to redirect the customer when an upload is completed. |  [optional] |
|**updatedTime** | **OffsetDateTime** | Latest update date/time. |  [optional] [readonly] |
|**links** | [**List&lt;KycRequestAllOfLinks&gt;**](KycRequestAllOfLinks.md) | The links related to resource. |  [optional] [readonly] |
|**customerId** | **String** | The сustomer&#39;s ID. |  |
|**matchLevel** | **Integer** | The level of strictness for the document matches. |  [optional] |
|**reason** | **String** | Reason for uploading. |  [optional] |



