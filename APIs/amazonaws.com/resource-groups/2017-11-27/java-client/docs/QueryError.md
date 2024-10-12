

# QueryError

A two-part error structure that can occur in <code>ListGroupResources</code> or <code>SearchResources</code> operations on CloudFront stack-based queries. The error occurs if the CloudFront stack on which the query is based either does not exist, or has a status that renders the stack inactive. A <code>QueryError</code> occurrence does not necessarily mean that Resource Groups could not complete the operation, but the resulting group might have no member resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorCode** | [**QueryErrorCode**](QueryErrorCode.md) |  |  [optional] |
|**message** | [**String**](String.md) |  |  [optional] |



