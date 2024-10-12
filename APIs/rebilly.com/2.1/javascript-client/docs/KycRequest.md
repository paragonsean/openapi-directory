# RebillyRestApi.KycRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdTime** | **Date** | Creation date/time. | [optional] [readonly] 
**documents** | [**[CommonKycRequestDocumentsInner]**](CommonKycRequestDocumentsInner.md) | Documents to be requested from customer. | 
**expirationTime** | **Date** | Expiration date/time. | [optional] 
**id** | **String** | The resource ID. Defaults to UUID v4. | [optional] [readonly] 
**redirectUrl** | **String** | The URL to redirect the customer when an upload is completed. | [optional] 
**updatedTime** | **Date** | Latest update date/time. | [optional] [readonly] 
**links** | [**[KycRequestAllOfLinks]**](KycRequestAllOfLinks.md) | The links related to resource. | [optional] [readonly] 
**customerId** | **String** | The сustomer&#39;s ID. | 
**matchLevel** | **Number** | The level of strictness for the document matches. | [optional] 
**reason** | **String** | Reason for uploading. | [optional] 


