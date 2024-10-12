# ConnectorsApi.CustomConnector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeConnectorVersions** | **[String]** | Optional. Active connector versions. | [optional] 
**createTime** | **String** | Output only. Created time. | [optional] [readonly] 
**customConnectorType** | **String** | Required. Type of the custom connector. | [optional] 
**description** | **String** | Optional. Description of the resource. | [optional] 
**displayName** | **String** | Optional. Display name. | [optional] 
**labels** | **{String: String}** | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources | [optional] 
**logo** | **String** | Optional. Logo of the resource. | [optional] 
**name** | **String** | Identifier. Resource name of the CustomConnector. Format: projects/{project}/locations/{location}/customConnectors/{connector} | [optional] 
**updateTime** | **String** | Output only. Updated time. | [optional] [readonly] 



## Enum: CustomConnectorTypeEnum


* `CUSTOM_CONNECTOR_TYPE_UNSPECIFIED` (value: `"CUSTOM_CONNECTOR_TYPE_UNSPECIFIED"`)

* `OPEN_API` (value: `"OPEN_API"`)

* `PROTO` (value: `"PROTO"`)




