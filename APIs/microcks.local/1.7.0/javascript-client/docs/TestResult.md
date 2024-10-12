# MicrocksApiV17.TestResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsedTime** | **Number** | Elapsed time in milliseconds since test beginning | [optional] 
**id** | **String** | Unique identifier of TestResult | 
**inProgress** | **Boolean** | Flag telling is test is still in progress | 
**operationHeaders** | **{String: [HeaderDTO]}** | Specification of additional headers for a Service/API operations. Keys are operation name or \&quot;globals\&quot; (if header applies to all), values are Header objects DTO. | [optional] 
**runnerType** | [**TestRunnerType**](TestRunnerType.md) |  | 
**secretRef** | [**SecretRef**](SecretRef.md) |  | [optional] 
**serviceId** | **String** | Unique identifier of service tested | 
**success** | **Boolean** | Flag telling if test is a success | 
**testCaseResults** | [**[TestCaseResult]**](TestCaseResult.md) | TestCase results associated to this test | [optional] 
**testDate** | **Number** | Timestamp of creation date of this service | 
**testNumber** | **Number** | Incremental number for tracking number of tests of a service | 
**testedEndpoint** | **String** | Endpoint used during test | 
**timeout** | **Number** | The maximum time (in milliseconds) to wait for this test ends | [optional] 
**version** | **Number** | Revision number of this test | 


