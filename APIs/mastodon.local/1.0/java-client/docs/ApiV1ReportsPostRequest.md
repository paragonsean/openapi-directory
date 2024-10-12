

# ApiV1ReportsPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | ID of the account to report |  |
|**comment** | **String** | Reason for the report (default max 1000 characters) |  [optional] |
|**forward** | **Boolean** | If the account is remote, should the report be forwarded to the remote admin? |  [optional] |
|**statusIds** | **List&lt;String&gt;** | Array of Statuses to attach to the report, for context |  [optional] |



