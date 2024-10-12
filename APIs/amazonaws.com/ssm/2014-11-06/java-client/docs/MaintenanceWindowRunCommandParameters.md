

# MaintenanceWindowRunCommandParameters

<p>The parameters for a <code>RUN_COMMAND</code> task type.</p> <p>For information about specifying and updating task parameters, see <a>RegisterTaskWithMaintenanceWindow</a> and <a>UpdateMaintenanceWindowTask</a>.</p> <note> <p> <code>LoggingInfo</code> has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the <code>OutputS3BucketName</code> and <code>OutputS3KeyPrefix</code> options in the <code>TaskInvocationParameters</code> structure. For information about how Amazon Web Services Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> <p> <code>TaskParameters</code> has been deprecated. To specify parameters to pass to a task when it runs, instead use the <code>Parameters</code> option in the <code>TaskInvocationParameters</code> structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> <p>For <code>RUN_COMMAND</code> tasks, Systems Manager uses specified values for <code>TaskParameters</code> and <code>LoggingInfo</code> only if no values are specified for <code>TaskInvocationParameters</code>. </p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comment** | [**String**](String.md) |  |  [optional] |
|**cloudWatchOutputConfig** | [**CloudWatchOutputConfig**](CloudWatchOutputConfig.md) |  |  [optional] |
|**documentHash** | [**String**](String.md) |  |  [optional] |
|**documentHashType** | [**DocumentHashType**](DocumentHashType.md) |  |  [optional] |
|**documentVersion** | [**String**](String.md) |  |  [optional] |
|**notificationConfig** | [**MaintenanceWindowRunCommandParametersNotificationConfig**](MaintenanceWindowRunCommandParametersNotificationConfig.md) |  |  [optional] |
|**outputS3BucketName** | [**String**](String.md) |  |  [optional] |
|**outputS3KeyPrefix** | [**String**](String.md) |  |  [optional] |
|**parameters** | [**Map**](Map.md) |  |  [optional] |
|**serviceRoleArn** | [**String**](String.md) |  |  [optional] |
|**timeoutSeconds** | [**Integer**](Integer.md) |  |  [optional] |



