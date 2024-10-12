

# ComplianceNote

ComplianceNote encapsulates all information about a specific compliance check.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cisBenchmark** | [**CisBenchmark**](CisBenchmark.md) |  |  [optional] |
|**description** | **String** | A description about this compliance check. |  [optional] |
|**rationale** | **String** | A rationale for the existence of this compliance check. |  [optional] |
|**remediation** | **String** | A description of remediation steps if the compliance check fails. |  [optional] |
|**scanInstructions** | **byte[]** | Serialized scan instructions with a predefined format. |  [optional] |
|**title** | **String** | The title that identifies this compliance check. |  [optional] |
|**version** | [**List&lt;ComplianceVersion&gt;**](ComplianceVersion.md) | The OS and config versions the benchmark applies to. |  [optional] |



