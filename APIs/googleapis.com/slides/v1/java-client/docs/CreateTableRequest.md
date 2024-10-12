

# CreateTableRequest

Creates a new table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columns** | **Integer** | Number of columns in the table. |  [optional] |
|**elementProperties** | [**PageElementProperties**](PageElementProperties.md) |  |  [optional] |
|**objectId** | **String** | A user-supplied object ID. If you specify an ID, it must be unique among all pages and page elements in the presentation. The ID must start with an alphanumeric character or an underscore (matches regex &#x60;[a-zA-Z0-9_]&#x60;); remaining characters may include those as well as a hyphen or colon (matches regex &#x60;[a-zA-Z0-9_-:]&#x60;). The length of the ID must not be less than 5 or greater than 50. If you don&#39;t specify an ID, a unique one is generated. |  [optional] |
|**rows** | **Integer** | Number of rows in the table. |  [optional] |



