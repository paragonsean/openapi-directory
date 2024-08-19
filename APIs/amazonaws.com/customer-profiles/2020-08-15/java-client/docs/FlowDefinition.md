

# FlowDefinition

The configurations that control how Customer Profiles retrieves data from the source, Amazon AppFlow. Customer Profiles uses this information to create an AppFlow flow on behalf of customers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | [**String**](String.md) |  |  [optional] |
|**flowName** | [**String**](String.md) |  |  |
|**kmsArn** | [**String**](String.md) |  |  |
|**sourceFlowConfig** | [**PutIntegrationRequestFlowDefinitionSourceFlowConfig**](PutIntegrationRequestFlowDefinitionSourceFlowConfig.md) |  |  |
|**tasks** | [**List**](List.md) |  |  |
|**triggerConfig** | [**PutIntegrationRequestFlowDefinitionTriggerConfig**](PutIntegrationRequestFlowDefinitionTriggerConfig.md) |  |  |



