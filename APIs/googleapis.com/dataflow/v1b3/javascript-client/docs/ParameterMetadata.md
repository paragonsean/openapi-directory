# DataflowApi.ParameterMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customMetadata** | **{String: String}** | Optional. Additional metadata for describing this parameter. | [optional] 
**defaultValue** | **String** | Optional. The default values will pre-populate the parameter with the given value from the proto. If default_value is left empty, the parameter will be populated with a default of the relevant type, e.g. false for a boolean. | [optional] 
**enumOptions** | [**[ParameterMetadataEnumOption]**](ParameterMetadataEnumOption.md) | Optional. The options shown when ENUM ParameterType is specified. | [optional] 
**groupName** | **String** | Optional. Specifies a group name for this parameter to be rendered under. Group header text will be rendered exactly as specified in this field. Only considered when parent_name is NOT provided. | [optional] 
**helpText** | **String** | Required. The help text to display for the parameter. | [optional] 
**hiddenUi** | **Boolean** | Optional. Whether the parameter should be hidden in the UI. | [optional] 
**isOptional** | **Boolean** | Optional. Whether the parameter is optional. Defaults to false. | [optional] 
**label** | **String** | Required. The label to display for the parameter. | [optional] 
**name** | **String** | Required. The name of the parameter. | [optional] 
**paramType** | **String** | Optional. The type of the parameter. Used for selecting input picker. | [optional] 
**parentName** | **String** | Optional. Specifies the name of the parent parameter. Used in conjunction with &#39;parent_trigger_values&#39; to make this parameter conditional (will only be rendered conditionally). Should be mappable to a ParameterMetadata.name field. | [optional] 
**parentTriggerValues** | **[String]** | Optional. The value(s) of the &#39;parent_name&#39; parameter which will trigger this parameter to be shown. If left empty, ANY non-empty value in parent_name will trigger this parameter to be shown. Only considered when this parameter is conditional (when &#39;parent_name&#39; has been provided). | [optional] 
**regexes** | **[String]** | Optional. Regexes that the parameter must match. | [optional] 



## Enum: ParamTypeEnum


* `DEFAULT` (value: `"DEFAULT"`)

* `TEXT` (value: `"TEXT"`)

* `GCS_READ_BUCKET` (value: `"GCS_READ_BUCKET"`)

* `GCS_WRITE_BUCKET` (value: `"GCS_WRITE_BUCKET"`)

* `GCS_READ_FILE` (value: `"GCS_READ_FILE"`)

* `GCS_WRITE_FILE` (value: `"GCS_WRITE_FILE"`)

* `GCS_READ_FOLDER` (value: `"GCS_READ_FOLDER"`)

* `GCS_WRITE_FOLDER` (value: `"GCS_WRITE_FOLDER"`)

* `PUBSUB_TOPIC` (value: `"PUBSUB_TOPIC"`)

* `PUBSUB_SUBSCRIPTION` (value: `"PUBSUB_SUBSCRIPTION"`)

* `BIGQUERY_TABLE` (value: `"BIGQUERY_TABLE"`)

* `JAVASCRIPT_UDF_FILE` (value: `"JAVASCRIPT_UDF_FILE"`)

* `SERVICE_ACCOUNT` (value: `"SERVICE_ACCOUNT"`)

* `MACHINE_TYPE` (value: `"MACHINE_TYPE"`)

* `KMS_KEY_NAME` (value: `"KMS_KEY_NAME"`)

* `WORKER_REGION` (value: `"WORKER_REGION"`)

* `WORKER_ZONE` (value: `"WORKER_ZONE"`)

* `BOOLEAN` (value: `"BOOLEAN"`)

* `ENUM` (value: `"ENUM"`)

* `NUMBER` (value: `"NUMBER"`)




