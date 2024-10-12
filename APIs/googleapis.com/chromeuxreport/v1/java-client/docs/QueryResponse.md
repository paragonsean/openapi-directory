

# QueryResponse

Response payload sent back to a physical web client. This response contains the record found based on the identiers present in a `QueryRequest`. The returned response will have a record, and sometimes details on normalization actions taken on the request that were necessary to make the request successful.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**record** | [**Record**](Record.md) |  |  [optional] |
|**urlNormalizationDetails** | [**UrlNormalization**](UrlNormalization.md) |  |  [optional] |



