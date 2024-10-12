

# DeleteResourcePolicyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**policyName** | **String** | The name of the resource policy to delete. |  |
|**policyRevisionId** | **String** | Specifies a specific policy revision to delete. Provide a &lt;code&gt;PolicyRevisionId&lt;/code&gt; to ensure an atomic delete operation. If the provided revision id does not match the latest policy revision id, an &lt;code&gt;InvalidPolicyRevisionIdException&lt;/code&gt; exception is returned.  |  [optional] |



