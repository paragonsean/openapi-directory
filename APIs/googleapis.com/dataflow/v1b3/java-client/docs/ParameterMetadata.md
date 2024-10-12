

# ParameterMetadata

Metadata for a specific parameter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customMetadata** | **Map&lt;String, String&gt;** | Optional. Additional metadata for describing this parameter. |  [optional] |
|**defaultValue** | **String** | Optional. The default values will pre-populate the parameter with the given value from the proto. If default_value is left empty, the parameter will be populated with a default of the relevant type, e.g. false for a boolean. |  [optional] |
|**enumOptions** | [**List&lt;ParameterMetadataEnumOption&gt;**](ParameterMetadataEnumOption.md) | Optional. The options shown when ENUM ParameterType is specified. |  [optional] |
|**groupName** | **String** | Optional. Specifies a group name for this parameter to be rendered under. Group header text will be rendered exactly as specified in this field. Only considered when parent_name is NOT provided. |  [optional] |
|**helpText** | **String** | Required. The help text to display for the parameter. |  [optional] |
|**hiddenUi** | **Boolean** | Optional. Whether the parameter should be hidden in the UI. |  [optional] |
|**isOptional** | **Boolean** | Optional. Whether the parameter is optional. Defaults to false. |  [optional] |
|**label** | **String** | Required. The label to display for the parameter. |  [optional] |
|**name** | **String** | Required. The name of the parameter. |  [optional] |
|**paramType** | [**ParamTypeEnum**](#ParamTypeEnum) | Optional. The type of the parameter. Used for selecting input picker. |  [optional] |
|**parentName** | **String** | Optional. Specifies the name of the parent parameter. Used in conjunction with &#39;parent_trigger_values&#39; to make this parameter conditional (will only be rendered conditionally). Should be mappable to a ParameterMetadata.name field. |  [optional] |
|**parentTriggerValues** | **List&lt;String&gt;** | Optional. The value(s) of the &#39;parent_name&#39; parameter which will trigger this parameter to be shown. If left empty, ANY non-empty value in parent_name will trigger this parameter to be shown. Only considered when this parameter is conditional (when &#39;parent_name&#39; has been provided). |  [optional] |
|**regexes** | **List&lt;String&gt;** | Optional. Regexes that the parameter must match. |  [optional] |



## Enum: ParamTypeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;DEFAULT&quot; |
| TEXT | &quot;TEXT&quot; |
| GCS_READ_BUCKET | &quot;GCS_READ_BUCKET&quot; |
| GCS_WRITE_BUCKET | &quot;GCS_WRITE_BUCKET&quot; |
| GCS_READ_FILE | &quot;GCS_READ_FILE&quot; |
| GCS_WRITE_FILE | &quot;GCS_WRITE_FILE&quot; |
| GCS_READ_FOLDER | &quot;GCS_READ_FOLDER&quot; |
| GCS_WRITE_FOLDER | &quot;GCS_WRITE_FOLDER&quot; |
| PUBSUB_TOPIC | &quot;PUBSUB_TOPIC&quot; |
| PUBSUB_SUBSCRIPTION | &quot;PUBSUB_SUBSCRIPTION&quot; |
| BIGQUERY_TABLE | &quot;BIGQUERY_TABLE&quot; |
| JAVASCRIPT_UDF_FILE | &quot;JAVASCRIPT_UDF_FILE&quot; |
| SERVICE_ACCOUNT | &quot;SERVICE_ACCOUNT&quot; |
| MACHINE_TYPE | &quot;MACHINE_TYPE&quot; |
| KMS_KEY_NAME | &quot;KMS_KEY_NAME&quot; |
| WORKER_REGION | &quot;WORKER_REGION&quot; |
| WORKER_ZONE | &quot;WORKER_ZONE&quot; |
| BOOLEAN | &quot;BOOLEAN&quot; |
| ENUM | &quot;ENUM&quot; |
| NUMBER | &quot;NUMBER&quot; |



