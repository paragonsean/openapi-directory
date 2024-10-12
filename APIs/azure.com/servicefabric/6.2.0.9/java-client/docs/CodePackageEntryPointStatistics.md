

# CodePackageEntryPointStatistics

Statistics about setup or main entry point  of a code package deployed on a Service Fabric node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationCount** | **String** | Number of times the entry point has run. |  [optional] |
|**activationFailureCount** | **String** | Number of times the entry point failed to run. |  [optional] |
|**continuousActivationFailureCount** | **String** | Number of times the entry point continuously failed to run. |  [optional] |
|**continuousExitFailureCount** | **String** | Number of times the entry point continuously failed to exit gracefully. |  [optional] |
|**exitCount** | **String** | Number of times the entry point finished running. |  [optional] |
|**exitFailureCount** | **String** | Number of times the entry point failed to exit gracefully. |  [optional] |
|**lastActivationTime** | **OffsetDateTime** | The last time (in UTC) when Service Fabric attempted to run the entry point. |  [optional] |
|**lastExitCode** | **String** | The last exit code of the entry point. |  [optional] |
|**lastExitTime** | **OffsetDateTime** | The last time (in UTC) when the entry point finished running. |  [optional] |
|**lastSuccessfulActivationTime** | **OffsetDateTime** | The last time (in UTC) when the entry point ran successfully. |  [optional] |
|**lastSuccessfulExitTime** | **OffsetDateTime** | The last time (in UTC) when the entry point finished running gracefully. |  [optional] |



