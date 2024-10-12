

# ComplianceVersion

Describes the CIS benchmark version that is applicable to a given OS and os version.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**benchmarkDocument** | **String** | The name of the document that defines this benchmark, e.g. \&quot;CIS Container-Optimized OS\&quot;. |  [optional] |
|**cpeUri** | **String** | The CPE URI (https://cpe.mitre.org/specification/) this benchmark is applicable to. |  [optional] |
|**version** | **String** | The version of the benchmark. This is set to the version of the OS-specific CIS document the benchmark is defined in. |  [optional] |



