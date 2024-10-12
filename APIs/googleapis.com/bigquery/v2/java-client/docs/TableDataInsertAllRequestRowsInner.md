

# TableDataInsertAllRequestRowsInner

Data for a single insertion row.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**insertId** | **String** | Insertion ID for best-effort deduplication. This feature is not recommended, and users seeking stronger insertion semantics are encouraged to use other mechanisms such as the BigQuery Write API. |  [optional] |
|**json** | **Map&lt;String, Object&gt;** | Represents a single JSON object. |  [optional] |



