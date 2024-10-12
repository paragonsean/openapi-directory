# LegalEntityManagementApi.TermsOfServiceAcceptanceInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptedBy** | **String** | The unique identifier of the user that accepted the Terms of Service. | [optional] 
**acceptedFor** | **String** | The unique identifier of the legal entity for which the Terms of Service are accepted. | [optional] 
**createdAt** | **Date** | The date when the Terms of Service were accepted. | [optional] 
**id** | **String** | An Adyen-generated reference for the accepted Terms of Service. | [optional] 
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




