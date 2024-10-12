# MerakiDashboardApi.GetOrganizationBrandingPolicies200ResponseInnerAdminSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliesTo** | **String** | Which kinds of admins this policy applies to. Can be one of &#39;All organization admins&#39;, &#39;All enterprise admins&#39;, &#39;All network admins&#39;, &#39;All admins of networks...&#39;, &#39;All admins of networks tagged...&#39;, &#39;Specific admins...&#39;, &#39;All admins&#39; or &#39;All SAML admins&#39;. | [optional] 
**values** | **[String]** |       If &#39;appliesTo&#39; is set to one of &#39;Specific admins...&#39;, &#39;All admins of networks...&#39; or &#39;All admins of networks tagged...&#39;, then you must specify this &#39;values&#39; property to provide the set of       entities to apply the branding policy to. For &#39;Specific admins...&#39;, specify an array of admin IDs. For &#39;All admins of       networks...&#39;, specify an array of network IDs and/or configuration template IDs. For &#39;All admins of networks tagged...&#39;,       specify an array of tag names.  | [optional] 



## Enum: AppliesToEnum


* `All SAML admins` (value: `"All SAML admins"`)

* `All admins` (value: `"All admins"`)

* `All admins of networks tagged...` (value: `"All admins of networks tagged..."`)

* `All admins of networks...` (value: `"All admins of networks..."`)

* `All enterprise admins` (value: `"All enterprise admins"`)

* `All network admins` (value: `"All network admins"`)

* `All organization admins` (value: `"All organization admins"`)

* `Specific admins...` (value: `"Specific admins..."`)




