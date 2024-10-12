

# ServiceAccountDelegationInfo

Identity delegation history of an authenticated service account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstPartyPrincipal** | [**FirstPartyPrincipal**](FirstPartyPrincipal.md) |  |  [optional] |
|**principalSubject** | **String** | A string representing the principal_subject associated with the identity. For most identities, the format will be &#x60;principal://iam.googleapis.com/{identity pool name}/subject/{subject)&#x60; except for some GKE identities (GKE_WORKLOAD, FREEFORM, GKE_HUB_WORKLOAD) that are still in the legacy format &#x60;serviceAccount:{identity pool name}[{subject}]&#x60; |  [optional] |
|**thirdPartyPrincipal** | [**ThirdPartyPrincipal**](ThirdPartyPrincipal.md) |  |  [optional] |



