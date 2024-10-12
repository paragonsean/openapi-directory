

# QueryInput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tableName** | [**String**](String.md) |  |  |
|**attributesToGet** | **List&lt;String&gt;** | List of &lt;code&gt;Attribute&lt;/code&gt; names. If attribute names are not specified then all attributes will be returned. If some attributes are not found, they will not appear in the result. |  [optional] |
|**limit** | [**Integer**](Integer.md) |  |  [optional] |
|**consistentRead** | **Boolean** | If set to &lt;code&gt;true&lt;/code&gt;, then a consistent read is issued. Otherwise eventually-consistent is used. |  [optional] |
|**count** | [**Boolean**](Boolean.md) |  |  [optional] |
|**hashKeyValue** | [**QueryInputHashKeyValue**](QueryInputHashKeyValue.md) |  |  |
|**rangeKeyCondition** | [**QueryInputRangeKeyCondition**](QueryInputRangeKeyCondition.md) |  |  [optional] |
|**scanIndexForward** | [**Boolean**](Boolean.md) |  |  [optional] |
|**exclusiveStartKey** | [**QueryInputExclusiveStartKey**](QueryInputExclusiveStartKey.md) |  |  [optional] |



