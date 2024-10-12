

# GetItemInput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tableName** | [**String**](String.md) |  |  |
|**key** | [**Key**](Key.md) |  |  |
|**attributesToGet** | **List&lt;String&gt;** | List of &lt;code&gt;Attribute&lt;/code&gt; names. If attribute names are not specified then all attributes will be returned. If some attributes are not found, they will not appear in the result. |  [optional] |
|**consistentRead** | **Boolean** | If set to &lt;code&gt;true&lt;/code&gt;, then a consistent read is issued. Otherwise eventually-consistent is used. |  [optional] |



