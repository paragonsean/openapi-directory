

# PullURIResponseDocDetails

Issuer can add meta content specific to document here.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**DOB** | **String** | The date of birth if sent in the original request. |  |
|**dataContent** | **String** | Enclose the base64 byte encoded certificate metadata in XML format. The DataContent element should be sent only if the original request contains format attribute as “xml” or “both”. |  |
|**digiLockerId** | **String** | A unique 36 character DigiLocker Id as sent in the original request. |  |
|**docContent** | **String** | Enclose the Base64 byte encoded contents of PDF file in this element. |  |
|**docType** | **String** | The document type sent in the original request. |  |
|**fullName** | **String** | The full name if sent in the original request. |  |
|**UDF1** | **String** | Search parameters sent in the original request. |  |
|**UDF2** | **String** | Search parameters sent in the original request. |  |
|**UID** | **String** | The Aadhaar number if sent in the original request. |  |
|**URI** | **String** | URI corresponding to the search criteria that identifies the document uniquely. |  |



