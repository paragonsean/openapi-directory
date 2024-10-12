

# Transaction

A transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **byte[]** | &#x60;id&#x60; may be used to identify the transaction in subsequent Read, ExecuteSql, Commit, or Rollback calls. Single-use read-only transactions do not have IDs, because single-use transactions do not support multiple requests. |  [optional] |
|**readTimestamp** | **String** | For snapshot read-only transactions, the read timestamp chosen for the transaction. Not returned by default: see TransactionOptions.ReadOnly.return_read_timestamp. A timestamp in RFC3339 UTC \\\&quot;Zulu\\\&quot; format, accurate to nanoseconds. Example: &#x60;\&quot;2014-10-02T15:01:23.045123456Z\&quot;&#x60;. |  [optional] |



