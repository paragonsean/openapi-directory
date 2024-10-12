

# UpdateOrganizationAdminRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the dashboard administrator |  [optional] |
|**networks** | [**List&lt;CreateOrganizationAdminRequestNetworksInner&gt;**](CreateOrganizationAdminRequestNetworksInner.md) | The list of networks that the dashboard administrator has privileges on |  [optional] |
|**orgAccess** | [**OrgAccessEnum**](#OrgAccessEnum) | The privilege of the dashboard administrator on the organization. Can be one of &#39;full&#39;, &#39;read-only&#39;, &#39;enterprise&#39; or &#39;none&#39; |  [optional] |
|**tags** | [**List&lt;CreateOrganizationAdminRequestTagsInner&gt;**](CreateOrganizationAdminRequestTagsInner.md) | The list of tags that the dashboard administrator has privileges on |  [optional] |



## Enum: OrgAccessEnum

| Name | Value |
|---- | -----|
| ENTERPRISE | &quot;enterprise&quot; |
| FULL | &quot;full&quot; |
| NONE | &quot;none&quot; |
| READ_ONLY | &quot;read-only&quot; |



