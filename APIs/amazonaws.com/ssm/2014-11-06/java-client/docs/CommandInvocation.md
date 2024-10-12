

# CommandInvocation

An invocation is a copy of a command sent to a specific managed node. A command can apply to one or more managed nodes. A command invocation applies to one managed node. For example, if a user runs <code>SendCommand</code> against three managed nodes, then a command invocation is created for each requested managed node ID. A command invocation returns status and detail information about a command you ran. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commandId** | [**String**](String.md) |  |  [optional] |
|**instanceId** | [**String**](String.md) |  |  [optional] |
|**instanceName** | [**String**](String.md) |  |  [optional] |
|**comment** | [**String**](String.md) |  |  [optional] |
|**documentName** | [**String**](String.md) |  |  [optional] |
|**documentVersion** | [**String**](String.md) |  |  [optional] |
|**requestedDateTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**status** | [**CommandInvocationStatus**](CommandInvocationStatus.md) |  |  [optional] |
|**statusDetails** | [**String**](String.md) |  |  [optional] |
|**traceOutput** | [**String**](String.md) |  |  [optional] |
|**standardOutputUrl** | [**String**](String.md) |  |  [optional] |
|**standardErrorUrl** | [**String**](String.md) |  |  [optional] |
|**commandPlugins** | [**List**](List.md) |  |  [optional] |
|**serviceRole** | [**String**](String.md) |  |  [optional] |
|**notificationConfig** | [**CommandInvocationNotificationConfig**](CommandInvocationNotificationConfig.md) |  |  [optional] |
|**cloudWatchOutputConfig** | [**CommandCloudWatchOutputConfig**](CommandCloudWatchOutputConfig.md) |  |  [optional] |



