

# AccessPolicy

`AccessPolicy` is a container for `AccessLevels` (which define the necessary attributes to use Google Cloud services) and `ServicePerimeters` (which define regions of services able to freely pass data within a perimeter). An access policy is globally visible within an organization, and the restrictions it specifies apply to all projects within an organization.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Output only. Resource name of the &#x60;AccessPolicy&#x60;. Format: &#x60;accessPolicies/{policy_id}&#x60; |  [optional] |
|**parent** | **String** | Required. The parent of this &#x60;AccessPolicy&#x60; in the Cloud Resource Hierarchy. Currently immutable once created. Format: &#x60;organizations/{organization_id}&#x60; |  [optional] |
|**title** | **String** | Required. Human readable title. Does not affect behavior. |  [optional] |



