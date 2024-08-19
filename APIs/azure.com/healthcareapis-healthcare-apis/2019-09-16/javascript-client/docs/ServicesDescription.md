# HealthcareApisClient.ServicesDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**ServicesProperties**](ServicesProperties.md) |  | [optional] 
**etag** | **String** | An etag associated with the resource, used for optimistic concurrency when editing it. | [optional] 
**id** | **String** | The resource identifier. | [optional] [readonly] 
**kind** | **String** | The kind of the service. | 
**location** | **String** | The resource location. | 
**name** | **String** | The resource name. | [optional] [readonly] 
**tags** | **{String: String}** | The resource tags. | [optional] 
**type** | **String** | The resource type. | [optional] [readonly] 



## Enum: KindEnum


* `fhir` (value: `"fhir"`)

* `fhir-Stu3` (value: `"fhir-Stu3"`)

* `fhir-R4` (value: `"fhir-R4"`)




