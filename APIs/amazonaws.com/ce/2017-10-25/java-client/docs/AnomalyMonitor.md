

# AnomalyMonitor

This object continuously inspects your account's cost data for anomalies. It's based on <code>MonitorType</code> and <code>MonitorSpecification</code>. The content consists of detailed metadata and the current status of the monitor object. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**monitorArn** | [**String**](String.md) |  |  [optional] |
|**monitorName** | [**String**](String.md) |  |  |
|**creationDate** | [**String**](String.md) |  |  [optional] |
|**lastUpdatedDate** | [**String**](String.md) |  |  [optional] |
|**lastEvaluatedDate** | [**String**](String.md) |  |  [optional] |
|**monitorType** | [**MonitorType**](MonitorType.md) |  |  |
|**monitorDimension** | [**MonitorDimension**](MonitorDimension.md) |  |  [optional] |
|**monitorSpecification** | [**Expression**](Expression.md) |  |  [optional] |
|**dimensionalValueCount** | [**Integer**](Integer.md) |  |  [optional] |



