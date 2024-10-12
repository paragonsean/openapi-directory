

# ClassificationTemplateFieldsInner

The metadata template field that represents the available classifications.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | [**DisplayNameEnum**](#DisplayNameEnum) | &#x60;Classification&#x60; |  [optional] |
|**hidden** | **Boolean** | Classifications are always visible to web and mobile users. |  [optional] |
|**id** | **String** | The unique ID of the field. |  [optional] |
|**key** | [**KeyEnum**](#KeyEnum) | &#x60;Box__Security__Classification__Key&#x60; |  [optional] |
|**options** | [**List&lt;ClassificationTemplateFieldsInnerOptionsInner&gt;**](ClassificationTemplateFieldsInnerOptionsInner.md) | A list of classifications available in this enterprise. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | &#x60;enum&#x60; |  [optional] |



## Enum: DisplayNameEnum

| Name | Value |
|---- | -----|
| CLASSIFICATION | &quot;Classification&quot; |



## Enum: KeyEnum

| Name | Value |
|---- | -----|
| BOX__SECURITY__CLASSIFICATION__KEY | &quot;Box__Security__Classification__Key&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ENUM | &quot;enum&quot; |



