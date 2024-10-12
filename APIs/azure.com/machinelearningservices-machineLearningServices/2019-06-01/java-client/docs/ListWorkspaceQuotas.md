

# ListWorkspaceQuotas

The List WorkspaceQuotasByVMFamily operation response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextLink** | **String** | The URI to fetch the next page of workspace quota information by VM Family. Call ListNext() with this to fetch the next page of Workspace Quota information. |  [optional] [readonly] |
|**value** | [**List&lt;ResourceQuota&gt;**](ResourceQuota.md) | The list of Workspace Quotas by VM Family |  [optional] [readonly] |



