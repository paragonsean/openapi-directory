

# PutDomainPermissionsPolicyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domain** | **String** |  The name of the domain on which to set the resource policy.  |  |
|**domainOwner** | **String** |  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.  |  [optional] |
|**policyRevision** | **String** |  The current revision of the resource policy to be set. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain&#39;s resource policy.  |  [optional] |
|**policyDocument** | **String** |  A valid displayable JSON Aspen policy string to be set as the access control resource policy on the provided domain.  |  |



