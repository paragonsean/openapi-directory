# CloudHealthcareApi.ApplyConsentsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patientScope** | [**PatientScope**](PatientScope.md) |  | [optional] 
**timeRange** | [**TimeRange**](TimeRange.md) |  | [optional] 
**validateOnly** | **Boolean** | Optional. If true, the method only validates Consent resources to make sure they are supported. When the operation completes, ApplyConsentsResponse is returned where &#x60;consent_apply_success&#x60; and &#x60;consent_apply_failure&#x60; indicate supported and unsupported (or invalid) Consent resources, respectively. Otherwise, the method propagates the aggregate consensual information to the patient&#39;s resources. Upon success, &#x60;affected_resources&#x60; in the ApplyConsentsResponse indicates the number of resources that may have consensual access changed. | [optional] 


