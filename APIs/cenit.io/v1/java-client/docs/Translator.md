

# Translator


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customDataType** | [**DataType**](DataType.md) |  |  [optional] |
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**namespace** | [**Namespace**](Namespace.md) |  |  [optional] |
|**sourceDataType** | [**DataType**](DataType.md) |  |  [optional] |
|**style** | [**StyleEnum**](#StyleEnum) |  |  [optional] |
|**targetDataType** | [**DataType**](DataType.md) |  |  [optional] |
|**transformation** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: StyleEnum

| Name | Value |
|---- | -----|
| RUBY | &quot;Ruby&quot; |
| LIQUID | &quot;Liquid&quot; |
| XSLT | &quot;xslt&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMPORT | &quot;Import&quot; |
| EXPORT | &quot;Export&quot; |
| CONVERT | &quot;Convert&quot; |
| UPDATE | &quot;Update&quot; |



