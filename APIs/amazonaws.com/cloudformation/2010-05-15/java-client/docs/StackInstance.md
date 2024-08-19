

# StackInstance

An CloudFormation stack, in a specific account and Region, that's part of a stack set operation. A stack instance is a reference to an attempted or actual stack in a given account within a given Region. A stack instance can exist without a stack—for example, if the stack couldn't be created for some reason. A stack instance is associated with only one stack set. Each stack instance contains the ID of its associated stack set, in addition to the ID of the actual stack and the stack status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stackSetId** | [**String**](String.md) |  |  [optional] |
|**region** | [**String**](String.md) |  |  [optional] |
|**account** | [**String**](String.md) |  |  [optional] |
|**stackId** | [**String**](String.md) |  |  [optional] |
|**parameterOverrides** | [**List**](List.md) |  |  [optional] |
|**status** | [**StackInstanceStatus**](StackInstanceStatus.md) |  |  [optional] |
|**stackInstanceStatus** | [**StackInstanceStackInstanceStatus**](StackInstanceStackInstanceStatus.md) |  |  [optional] |
|**statusReason** | [**String**](String.md) |  |  [optional] |
|**organizationalUnitId** | [**String**](String.md) |  |  [optional] |
|**driftStatus** | [**StackDriftStatus**](StackDriftStatus.md) |  |  [optional] |
|**lastDriftCheckTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastOperationId** | [**String**](String.md) |  |  [optional] |



