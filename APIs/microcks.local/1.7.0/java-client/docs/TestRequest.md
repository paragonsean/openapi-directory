

# TestRequest

Test request is a minimalist wrapper for requesting the launch of a new test

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filteredOperations** | **List&lt;String&gt;** | A restriction on service operations to test |  [optional] |
|**operationHeaders** | **Map&lt;String, List&lt;HeaderDTO&gt;&gt;** | Specification of additional headers for a Service/API operations. Keys are operation name or \&quot;globals\&quot; (if header applies to all), values are Header objects DTO. |  [optional] |
|**runnerType** | **TestRunnerType** |  |  |
|**secretName** | **String** | The name of Secret to use for connecting the test endpoint |  [optional] |
|**serviceId** | **String** | Unique identifier of service to test |  |
|**testEndpoint** | **String** | Endpoint to test for this service |  |
|**timeout** | **Integer** | The maximum time (in milliseconds) to wait for this test ends |  |



