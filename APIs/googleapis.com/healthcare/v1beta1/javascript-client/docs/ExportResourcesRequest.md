# CloudHealthcareApi.ExportResourcesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**since** | **String** | If provided, only resources updated after this time are exported. The time uses the format YYYY-MM-DDThh:mm:ss.sss+zz:zz. For example, &#x60;2015-02-07T13:28:17.239+02:00&#x60; or &#x60;2017-01-01T00:00:00Z&#x60;. The time must be specified to the second and include a time zone. | [optional] 
**type** | **String** | String of comma-delimited FHIR resource types. If provided, only resources of the specified resource type(s) are exported. | [optional] 
**bigqueryDestination** | [**GoogleCloudHealthcareV1beta1FhirBigQueryDestination**](GoogleCloudHealthcareV1beta1FhirBigQueryDestination.md) |  | [optional] 
**gcsDestination** | [**GoogleCloudHealthcareV1beta1FhirGcsDestination**](GoogleCloudHealthcareV1beta1FhirGcsDestination.md) |  | [optional] 


