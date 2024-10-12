

# CreateOrganizationAdminRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationMethod** | [**AuthenticationMethodEnum**](#AuthenticationMethodEnum) | The method of authentication the user will use to sign in to the Meraki dashboard. Can be one of &#39;Email&#39; or &#39;Cisco SecureX Sign-On&#39;. The default is Email authentication |  [optional] |
|**email** | **String** | The email of the dashboard administrator. This attribute can not be updated. |  |
|**name** | **String** | The name of the dashboard administrator |  |
|**networks** | [**List&lt;CreateOrganizationAdminRequestNetworksInner&gt;**](CreateOrganizationAdminRequestNetworksInner.md) | The list of networks that the dashboard administrator has privileges on |  [optional] |
|**orgAccess** | [**OrgAccessEnum**](#OrgAccessEnum) | The privilege of the dashboard administrator on the organization. Can be one of &#39;full&#39;, &#39;read-only&#39;, &#39;enterprise&#39; or &#39;none&#39; |  |
|**tags** | [**List&lt;CreateOrganizationAdminRequestTagsInner&gt;**](CreateOrganizationAdminRequestTagsInner.md) | The list of tags that the dashboard administrator has privileges on |  [optional] |



## Enum: AuthenticationMethodEnum

| Name | Value |
|---- | -----|
| CISCO_SECURE_X_SIGN_ON | &quot;Cisco SecureX Sign-On&quot; |
| EMAIL | &quot;Email&quot; |



## Enum: OrgAccessEnum

| Name | Value |
|---- | -----|
| ENTERPRISE | &quot;enterprise&quot; |
| FULL | &quot;full&quot; |
| NONE | &quot;none&quot; |
| READ_ONLY | &quot;read-only&quot; |



