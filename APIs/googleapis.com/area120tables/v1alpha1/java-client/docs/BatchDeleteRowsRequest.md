

# BatchDeleteRowsRequest

Request message for TablesService.BatchDeleteRows

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**names** | **List&lt;String&gt;** | Required. The names of the rows to delete. All rows must belong to the parent table or else the entire batch will fail. A maximum of 500 rows can be deleted in a batch. Format: tables/{table}/rows/{row} |  [optional] |



