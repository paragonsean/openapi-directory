# ServiceFabricClientApis.ChaosReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chaosParameters** | [**ChaosParameters**](ChaosParameters.md) |  | [optional] 
**continuationToken** | **String** | The continuation token parameter is used to obtain next set of results. The continuation token is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token is not included in the response. | [optional] 
**history** | [**[ChaosEventWrapper]**](ChaosEventWrapper.md) |  | [optional] 
**status** | **String** | Current status of the Chaos run.  - Invalid - Indicates an invalid Chaos status. All Service Fabric enumerations have the invalid type.   The valus is zero. - Running - Indicates that Chaos is not stopped. - Stopped - Indicates that Chaos is not scheduling futher faults. | [optional] 



## Enum: StatusEnum


* `Invalid` (value: `"Invalid"`)

* `Running` (value: `"Running"`)

* `Stopped` (value: `"Stopped"`)




