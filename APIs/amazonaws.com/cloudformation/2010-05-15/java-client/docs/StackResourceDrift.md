

# StackResourceDrift

<p>Contains the drift information for a resource that has been checked for drift. This includes actual and expected property values for resources in which CloudFormation has detected drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information, see <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html\">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Resources that don't currently support drift detection can't be checked. For a list of resources that support drift detection, see <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html\">Resources that Support Drift Detection</a>.</p> <p>Use <a>DetectStackResourceDrift</a> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all resources in a given stack that support drift detection.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stackId** | [**String**](String.md) |  |  |
|**logicalResourceId** | [**String**](String.md) |  |  |
|**physicalResourceId** | [**String**](String.md) |  |  [optional] |
|**physicalResourceIdContext** | [**List**](List.md) |  |  [optional] |
|**resourceType** | [**String**](String.md) |  |  |
|**expectedProperties** | [**String**](String.md) |  |  [optional] |
|**actualProperties** | [**String**](String.md) |  |  [optional] |
|**propertyDifferences** | [**List**](List.md) |  |  [optional] |
|**stackResourceDriftStatus** | [**StackResourceDriftStatus**](StackResourceDriftStatus.md) |  |  |
|**timestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**moduleInfo** | [**ResourceChangeModuleInfo**](ResourceChangeModuleInfo.md) |  |  [optional] |



