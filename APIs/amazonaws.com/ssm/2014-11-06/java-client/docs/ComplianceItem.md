

# ComplianceItem

Information about the compliance as defined by the resource type. For example, for a patch resource type, <code>Items</code> includes information about the PatchSeverity, Classification, and so on.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**complianceType** | [**String**](String.md) |  |  [optional] |
|**resourceType** | [**String**](String.md) |  |  [optional] |
|**resourceId** | [**String**](String.md) |  |  [optional] |
|**id** | [**String**](String.md) |  |  [optional] |
|**title** | [**String**](String.md) |  |  [optional] |
|**status** | [**ComplianceStatus**](ComplianceStatus.md) |  |  [optional] |
|**severity** | [**ComplianceSeverity**](ComplianceSeverity.md) |  |  [optional] |
|**executionSummary** | [**ComplianceItemExecutionSummary**](ComplianceItemExecutionSummary.md) |  |  [optional] |
|**details** | [**Map**](Map.md) |  |  [optional] |



