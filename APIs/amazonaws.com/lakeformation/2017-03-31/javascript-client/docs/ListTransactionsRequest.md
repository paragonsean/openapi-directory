# AwsLakeFormation.ListTransactionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalogId** | **String** | The catalog for which to list transactions. Defaults to the account ID of the caller. | [optional] 
**statusFilter** | **String** |  A filter indicating the status of transactions to return. Options are ALL | COMPLETED | COMMITTED | ABORTED | ACTIVE. The default is &lt;code&gt;ALL&lt;/code&gt;. | [optional] 
**maxResults** | **Number** | The maximum number of transactions to return in a single call. | [optional] 
**nextToken** | **String** | A continuation token if this is not the first call to retrieve transactions. | [optional] 



## Enum: StatusFilterEnum


* `ALL` (value: `"ALL"`)

* `COMPLETED` (value: `"COMPLETED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `COMMITTED` (value: `"COMMITTED"`)

* `ABORTED` (value: `"ABORTED"`)




