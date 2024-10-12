

# FeatureTemplateSection


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configId** | **String** | Unique identifier of configuration associated with the vertical pack. Required for cloning |  |
|**description** | **String** | Verbal description of template features, belonging to domain area, etc. |  |
|**id** | **String** | Unique document identifier. Can be up to 36 alphanumeric characters |  |
|**isFree** | **Boolean** | Shows whether Vertical pack is free or requires subscription |  |
|**language** | **String** | The language supported by the vertical pack |  |
|**name** | **String** | Name of the vertical pack |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the vertical pack, can be either \&quot;vertical-pack\&quot; or \&quot;language-default\&quot; |  |
|**version** | **String** | Version of the vertical pack, for versioning purposes. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LANGUAGE_DEFAULT | &quot;language-default&quot; |
| VERTICAL_PACK | &quot;vertical-pack&quot; |



