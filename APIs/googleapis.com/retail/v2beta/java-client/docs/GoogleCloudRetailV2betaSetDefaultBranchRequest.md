

# GoogleCloudRetailV2betaSetDefaultBranchRequest

Request message to set a specified branch as new default_branch.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**branchId** | **String** | The final component of the resource name of a branch. This field must be one of \&quot;0\&quot;, \&quot;1\&quot; or \&quot;2\&quot;. Otherwise, an INVALID_ARGUMENT error is returned. If there are no sufficient active products in the targeted branch and force is not set, a FAILED_PRECONDITION error is returned. |  [optional] |
|**force** | **Boolean** | If set to true, it permits switching to a branch with branch_id even if it has no sufficient active products. |  [optional] |
|**note** | **String** | Some note on this request, this can be retrieved by CatalogService.GetDefaultBranch before next valid default branch set occurs. This field must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is returned. |  [optional] |



