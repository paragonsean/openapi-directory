

# GetOrganizationBrandingPolicies200ResponseInnerAdminSettings

Settings for describing which kinds of admins this policy applies to.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appliesTo** | [**AppliesToEnum**](#AppliesToEnum) | Which kinds of admins this policy applies to. Can be one of &#39;All organization admins&#39;, &#39;All enterprise admins&#39;, &#39;All network admins&#39;, &#39;All admins of networks...&#39;, &#39;All admins of networks tagged...&#39;, &#39;Specific admins...&#39;, &#39;All admins&#39; or &#39;All SAML admins&#39;. |  [optional] |
|**values** | **List&lt;String&gt;** |       If &#39;appliesTo&#39; is set to one of &#39;Specific admins...&#39;, &#39;All admins of networks...&#39; or &#39;All admins of networks tagged...&#39;, then you must specify this &#39;values&#39; property to provide the set of       entities to apply the branding policy to. For &#39;Specific admins...&#39;, specify an array of admin IDs. For &#39;All admins of       networks...&#39;, specify an array of network IDs and/or configuration template IDs. For &#39;All admins of networks tagged...&#39;,       specify an array of tag names.  |  [optional] |



## Enum: AppliesToEnum

| Name | Value |
|---- | -----|
| ALL_SAML_ADMINS | &quot;All SAML admins&quot; |
| ALL_ADMINS | &quot;All admins&quot; |
| ALL_ADMINS_OF_NETWORKS_TAGGED_ | &quot;All admins of networks tagged...&quot; |
| ALL_ADMINS_OF_NETWORKS_ | &quot;All admins of networks...&quot; |
| ALL_ENTERPRISE_ADMINS | &quot;All enterprise admins&quot; |
| ALL_NETWORK_ADMINS | &quot;All network admins&quot; |
| ALL_ORGANIZATION_ADMINS | &quot;All organization admins&quot; |
| SPECIFIC_ADMINS_ | &quot;Specific admins...&quot; |



