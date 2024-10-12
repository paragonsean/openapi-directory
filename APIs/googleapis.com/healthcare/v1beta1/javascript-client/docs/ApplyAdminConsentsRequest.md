# CloudHealthcareApi.ApplyAdminConsentsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**newConsentsList** | [**AdminConsents**](AdminConsents.md) |  | [optional] 
**validateOnly** | **Boolean** | If true, the method only validates Consent resources to make sure they are supported. Otherwise, the method applies the aggregate consent information to update the enforcement model and reindex the FHIR resources. If all Consent resources can be applied successfully, the ApplyAdminConsentsResponse is returned containing the following fields: * &#x60;consent_apply_success&#x60; to indicate the number of Consent resources applied. * &#x60;affected_resources&#x60; to indicate the number of resources that might have had their consent access changed. If, however, one or more Consent resources are unsupported or cannot be applied, the method fails and ApplyAdminConsentsErrorDetail is is returned with details about the unsupported Consent resources. | [optional] 


