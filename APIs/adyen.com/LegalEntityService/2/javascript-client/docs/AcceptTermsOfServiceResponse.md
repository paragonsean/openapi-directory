# LegalEntityManagementApi.AcceptTermsOfServiceResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptedBy** | **String** | The unique identifier of the user that accepted the Terms of Service. | [optional] 
**id** | **String** | The unique identifier of the Terms of Service acceptance. | [optional] 
**ipAddress** | **String** | The IP address of the user that accepted the Terms of Service. | [optional] 
**language** | **String** | The language used for the Terms of Service document, specified by the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code. Possible value: **en** for English. | [optional] 
**termsOfServiceDocumentId** | **String** | The unique identifier of the Terms of Service document. | [optional] 
**type** | **String** | The type of Terms of Service.  Possible values: *  **adyenForPlatformsManage** *  **adyenIssuing** *  **adyenForPlatformsAdvanced** *  **adyenCapital** *  **adyenAccount** *  **adyenCard** *  **adyenFranchisee** *  **adyenPccr**   | [optional] 



## Enum: TypeEnum


* `adyenAccount` (value: `"adyenAccount"`)

* `adyenCapital` (value: `"adyenCapital"`)

* `adyenCard` (value: `"adyenCard"`)

* `adyenForPlatformsAdvanced` (value: `"adyenForPlatformsAdvanced"`)

* `adyenForPlatformsManage` (value: `"adyenForPlatformsManage"`)

* `adyenFranchisee` (value: `"adyenFranchisee"`)

* `adyenIssuing` (value: `"adyenIssuing"`)

* `adyenPccr` (value: `"adyenPccr"`)




