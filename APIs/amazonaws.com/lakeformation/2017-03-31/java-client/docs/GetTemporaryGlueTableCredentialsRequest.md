

# GetTemporaryGlueTableCredentialsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tableArn** | **String** | The ARN identifying a table in the Data Catalog for the temporary credentials request. |  |
|**permissions** | **List&lt;Permission&gt;** | Filters the request based on the user having been granted a list of specified permissions on the requested resource(s). |  [optional] |
|**durationSeconds** | **Integer** | The time period, between 900 and 21,600 seconds, for the timeout of the temporary credentials. |  [optional] |
|**auditContext** | [**GetTemporaryGluePartitionCredentialsRequestAuditContext**](GetTemporaryGluePartitionCredentialsRequestAuditContext.md) |  |  [optional] |
|**supportedPermissionTypes** | **List&lt;PermissionType&gt;** | A list of supported permission types for the table. Valid values are &lt;code&gt;COLUMN_PERMISSION&lt;/code&gt; and &lt;code&gt;CELL_FILTER_PERMISSION&lt;/code&gt;. |  [optional] |



