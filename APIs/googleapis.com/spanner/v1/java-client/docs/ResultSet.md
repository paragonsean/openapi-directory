

# ResultSet

Results from Read or ExecuteSql.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metadata** | [**ResultSetMetadata**](ResultSetMetadata.md) |  |  [optional] |
|**rows** | **List&lt;List&lt;Object&gt;&gt;** | Each element in &#x60;rows&#x60; is a row whose format is defined by metadata.row_type. The ith element in each row matches the ith field in metadata.row_type. Elements are encoded based on type as described here. |  [optional] |
|**stats** | [**ResultSetStats**](ResultSetStats.md) |  |  [optional] |



