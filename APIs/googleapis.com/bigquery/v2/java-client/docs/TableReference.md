

# TableReference


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datasetId** | **String** | Required. The ID of the dataset containing this table. |  [optional] |
|**projectId** | **String** | Required. The ID of the project containing this table. |  [optional] |
|**tableId** | **String** | Required. The ID of the table. The ID can contain Unicode characters in category L (letter), M (mark), N (number), Pc (connector, including underscore), Pd (dash), and Zs (space). For more information, see [General Category](https://wikipedia.org/wiki/Unicode_character_property#General_Category). The maximum length is 1,024 characters. Certain operations allow suffixing of the table ID with a partition decorator, such as &#x60;sample_table$20190123&#x60;. |  [optional] |



