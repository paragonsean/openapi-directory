

# CreateOrganizationSamlRoleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**networks** | [**List&lt;CreateOrganizationSamlRoleRequestNetworksInner&gt;**](CreateOrganizationSamlRoleRequestNetworksInner.md) | The list of networks that the SAML administrator has privileges on |  [optional] |
|**orgAccess** | [**OrgAccessEnum**](#OrgAccessEnum) | The privilege of the SAML administrator on the organization. Can be one of &#39;none&#39;, &#39;read-only&#39;, &#39;full&#39; or &#39;enterprise&#39; |  |
|**role** | **String** | The role of the SAML administrator |  |
|**tags** | [**List&lt;CreateOrganizationSamlRoleRequestTagsInner&gt;**](CreateOrganizationSamlRoleRequestTagsInner.md) | The list of tags that the SAML administrator has privleges on |  [optional] |



## Enum: OrgAccessEnum

| Name | Value |
|---- | -----|
| ENTERPRISE | &quot;enterprise&quot; |
| FULL | &quot;full&quot; |
| NONE | &quot;none&quot; |
| READ_ONLY | &quot;read-only&quot; |



