

# CreateAssociationBatchRequestEntry

Describes the association of a Amazon Web Services Systems Manager document (SSM document) and a managed node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  |
|**instanceId** | [**String**](String.md) |  |  [optional] |
|**parameters** | [**Map**](Map.md) |  |  [optional] |
|**automationTargetParameterName** | [**String**](String.md) |  |  [optional] |
|**documentVersion** | [**String**](String.md) |  |  [optional] |
|**targets** | [**List**](List.md) |  |  [optional] |
|**scheduleExpression** | [**String**](String.md) |  |  [optional] |
|**outputLocation** | [**UpdateAssociationRequestOutputLocation**](UpdateAssociationRequestOutputLocation.md) |  |  [optional] |
|**associationName** | [**String**](String.md) |  |  [optional] |
|**maxErrors** | [**String**](String.md) |  |  [optional] |
|**maxConcurrency** | [**String**](String.md) |  |  [optional] |
|**complianceSeverity** | [**AssociationComplianceSeverity**](AssociationComplianceSeverity.md) |  |  [optional] |
|**syncCompliance** | [**AssociationSyncCompliance**](AssociationSyncCompliance.md) |  |  [optional] |
|**applyOnlyAtCronInterval** | [**Boolean**](Boolean.md) |  |  [optional] |
|**calendarNames** | [**List**](List.md) |  |  [optional] |
|**targetLocations** | [**List**](List.md) |  |  [optional] |
|**scheduleOffset** | [**Integer**](Integer.md) |  |  [optional] |
|**targetMaps** | [**List**](List.md) |  |  [optional] |
|**alarmConfiguration** | [**AlarmConfiguration**](AlarmConfiguration.md) |  |  [optional] |



