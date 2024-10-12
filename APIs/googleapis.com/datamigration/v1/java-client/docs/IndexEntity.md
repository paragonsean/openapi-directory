

# IndexEntity

Index is not used as an independent entity, it is retrieved as part of a Table entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customFeatures** | **Map&lt;String, Object&gt;** | Custom engine specific features. |  [optional] |
|**name** | **String** | The name of the index. |  [optional] |
|**tableColumns** | **List&lt;String&gt;** | Table columns used as part of the Index, for example B-TREE index should list the columns which constitutes the index. |  [optional] |
|**type** | **String** | Type of index, for example B-TREE. |  [optional] |
|**unique** | **Boolean** | Boolean value indicating whether the index is unique. |  [optional] |



