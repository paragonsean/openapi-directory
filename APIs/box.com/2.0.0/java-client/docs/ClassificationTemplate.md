

# ClassificationTemplate

A metadata template that holds the security classifications defined by an enterprise.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copyInstanceOnItemCopy** | **Boolean** | Classifications are always copied along when the file or folder is copied. |  [optional] |
|**displayName** | [**DisplayNameEnum**](#DisplayNameEnum) | The name of this template as shown in web and mobile interfaces. |  [optional] |
|**fields** | [**List&lt;ClassificationTemplateFieldsInner&gt;**](ClassificationTemplateFieldsInner.md) | A list of fields for this classification template. This includes only one field, the &#x60;Box__Security__Classification__Key&#x60;, which defines the different classifications available in this enterprise. |  [optional] |
|**hidden** | **Boolean** | This template is always available in web and mobile interfaces. |  [optional] |
|**id** | **String** | The ID of the classification template. |  [optional] |
|**scope** | **String** | The scope of the classification template. This is in the format &#x60;enterprise_{id}&#x60; where the &#x60;id&#x60; is the enterprise ID. |  [optional] |
|**templateKey** | [**TemplateKeyEnum**](#TemplateKeyEnum) | &#x60;securityClassification-6VMVochwUWo&#x60; |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | &#x60;metadata_template&#x60; |  |



## Enum: DisplayNameEnum

| Name | Value |
|---- | -----|
| CLASSIFICATION | &quot;Classification&quot; |



## Enum: TemplateKeyEnum

| Name | Value |
|---- | -----|
| SECURITY_CLASSIFICATION_6_VM_VOCHW_UWO | &quot;securityClassification-6VMVochwUWo&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| METADATA_TEMPLATE | &quot;metadata_template&quot; |



