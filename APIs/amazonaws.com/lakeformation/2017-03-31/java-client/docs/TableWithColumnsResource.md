

# TableWithColumnsResource

<p>A structure for a table with columns object. This object is only used when granting a SELECT permission.</p> <p>This object must take a value for at least one of <code>ColumnsNames</code>, <code>ColumnsIndexes</code>, or <code>ColumnsWildcard</code>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catalogId** | [**String**](String.md) |  |  [optional] |
|**databaseName** | [**String**](String.md) |  |  |
|**name** | [**String**](String.md) |  |  |
|**columnNames** | [**List**](List.md) |  |  [optional] |
|**columnWildcard** | [**TableWithColumnsResourceColumnWildcard**](TableWithColumnsResourceColumnWildcard.md) |  |  [optional] |



