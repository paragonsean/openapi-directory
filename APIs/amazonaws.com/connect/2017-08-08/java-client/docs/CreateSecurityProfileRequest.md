

# CreateSecurityProfileRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**securityProfileName** | **String** | The name of the security profile. |  |
|**description** | **String** | The description of the security profile. |  [optional] |
|**permissions** | **List&lt;String&gt;** | Permissions assigned to the security profile. For a list of valid permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html\&quot;&gt;List of security profile permissions&lt;/a&gt;.  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags used to organize, track, or control access for this resource. For example, { \&quot;tags\&quot;: {\&quot;key1\&quot;:\&quot;value1\&quot;, \&quot;key2\&quot;:\&quot;value2\&quot;} }. |  [optional] |
|**allowedAccessControlTags** | **Map&lt;String, String&gt;** | The list of tags that a security profile uses to restrict access to resources in Amazon Connect. |  [optional] |
|**tagRestrictedResources** | **List&lt;String&gt;** | The list of resources that a security profile applies tag restrictions to in Amazon Connect. Following are acceptable ResourceNames: &lt;code&gt;User&lt;/code&gt; | &lt;code&gt;SecurityProfile&lt;/code&gt; | &lt;code&gt;Queue&lt;/code&gt; | &lt;code&gt;RoutingProfile&lt;/code&gt;  |  [optional] |



