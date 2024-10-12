# LgtmApiSpecification.Health

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A description of the status of the service. | [optional] 
**details** | [**{String: Health}**](Health.md) | Details of the health of the service. This contains information about the status of the components on which the service depends. | [optional] 
**status** | **String** | The status of the service. | [optional] 



## Enum: StatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `UP` (value: `"UP"`)

* `DOWN` (value: `"DOWN"`)




