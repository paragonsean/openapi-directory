

# Device


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** |  |  |
|**attributes** | **Map&lt;String, Map&lt;String, Object&gt;&gt;** | Each key is &lt;FunctionalityClass&gt;@&lt;Endpoint&gt; |  [optional] |
|**propertyClass** | **String** |  |  |
|**functionalities** | [**Set&lt;FunctionalityItem&gt;**](FunctionalityItem.md) |  |  [readonly] |
|**isOnline** | **Boolean** |  |  [readonly] |
|**manufacturer** | **String** |  |  [optional] [readonly] |
|**metadata** | **Map&lt;String, Object&gt;** | Keys are limited to the same format as tags (up to 21 characters, [a-z0-9], starting with [a-z]). Values can be any JSON value. |  [optional] |
|**model** | **String** |  |  [optional] [readonly] |
|**name** | **String** | Name of the device. User defined. |  [optional] |
|**place** | **String** | Unique identifier of the *Place* |  |
|**protocol** | **String** |  |  [optional] |
|**tags** | **Set&lt;String&gt;** |  |  |



