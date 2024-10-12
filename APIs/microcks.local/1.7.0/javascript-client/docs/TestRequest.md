# MicrocksApiV17.TestRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filteredOperations** | **[String]** | A restriction on service operations to test | [optional] 
**operationHeaders** | **{String: [HeaderDTO]}** | Specification of additional headers for a Service/API operations. Keys are operation name or \&quot;globals\&quot; (if header applies to all), values are Header objects DTO. | [optional] 
**runnerType** | [**TestRunnerType**](TestRunnerType.md) |  | 
**secretName** | **String** | The name of Secret to use for connecting the test endpoint | [optional] 
**serviceId** | **String** | Unique identifier of service to test | 
**testEndpoint** | **String** | Endpoint to test for this service | 
**timeout** | **Number** | The maximum time (in milliseconds) to wait for this test ends | 


