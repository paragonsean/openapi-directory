

# TestResult

Represents the result of a Service or API test run by Microcks. Tests are related to a service and made of multiple test cases corresponding to each operations / actions composing service. Tests are run against a specific endpoint named testedEndpoint. It holds global markers telling if test still ran, is a success, how many times is has taken and so on ...

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**elapsedTime** | **BigDecimal** | Elapsed time in milliseconds since test beginning |  [optional] |
|**id** | **String** | Unique identifier of TestResult |  |
|**inProgress** | **Boolean** | Flag telling is test is still in progress |  |
|**operationHeaders** | **Map&lt;String, List&lt;HeaderDTO&gt;&gt;** | Specification of additional headers for a Service/API operations. Keys are operation name or \&quot;globals\&quot; (if header applies to all), values are Header objects DTO. |  [optional] |
|**runnerType** | **TestRunnerType** |  |  |
|**secretRef** | [**SecretRef**](SecretRef.md) |  |  [optional] |
|**serviceId** | **String** | Unique identifier of service tested |  |
|**success** | **Boolean** | Flag telling if test is a success |  |
|**testCaseResults** | [**List&lt;TestCaseResult&gt;**](TestCaseResult.md) | TestCase results associated to this test |  [optional] |
|**testDate** | **Long** | Timestamp of creation date of this service |  |
|**testNumber** | **BigDecimal** | Incremental number for tracking number of tests of a service |  |
|**testedEndpoint** | **String** | Endpoint used during test |  |
|**timeout** | **Integer** | The maximum time (in milliseconds) to wait for this test ends |  [optional] |
|**version** | **BigDecimal** | Revision number of this test |  |



