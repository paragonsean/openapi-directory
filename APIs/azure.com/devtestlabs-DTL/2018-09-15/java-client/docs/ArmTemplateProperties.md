

# ArmTemplateProperties

Properties of an Azure Resource Manager template.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contents** | **Object** | The contents of the ARM template. |  [optional] [readonly] |
|**createdDate** | **OffsetDateTime** | The creation date of the armTemplate. |  [optional] [readonly] |
|**description** | **String** | The description of the ARM template. |  [optional] [readonly] |
|**displayName** | **String** | The display name of the ARM template. |  [optional] [readonly] |
|**enabled** | **Boolean** | Whether or not ARM template is enabled for use by lab user. |  [optional] [readonly] |
|**icon** | **String** | The URI to the icon of the ARM template. |  [optional] [readonly] |
|**parametersValueFilesInfo** | [**List&lt;ParametersValueFileInfo&gt;**](ParametersValueFileInfo.md) | File name and parameter values information from all azuredeploy.*.parameters.json for the ARM template. |  [optional] [readonly] |
|**publisher** | **String** | The publisher of the ARM template. |  [optional] [readonly] |



