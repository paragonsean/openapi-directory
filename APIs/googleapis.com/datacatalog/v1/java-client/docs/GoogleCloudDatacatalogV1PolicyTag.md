

# GoogleCloudDatacatalogV1PolicyTag

Denotes one policy tag in a taxonomy, for example, SSN. Policy tags can be defined in a hierarchy. For example: ``` + Geolocation + LatLong + City + ZipCode ``` Where the \"Geolocation\" policy tag contains three children.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**childPolicyTags** | **List&lt;String&gt;** | Output only. Resource names of child policy tags of this policy tag. |  [optional] [readonly] |
|**description** | **String** | Description of this policy tag. If not set, defaults to empty. The description must contain only Unicode characters, tabs, newlines, carriage returns and page breaks, and be at most 2000 bytes long when encoded in UTF-8. |  [optional] |
|**displayName** | **String** | Required. User-defined name of this policy tag. The name can&#39;t start or end with spaces and must be unique within the parent taxonomy, contain only Unicode letters, numbers, underscores, dashes and spaces, and be at most 200 bytes long when encoded in UTF-8. |  [optional] |
|**name** | **String** | Identifier. Resource name of this policy tag in the URL format. The policy tag manager generates unique taxonomy IDs and policy tag IDs. |  [optional] |
|**parentPolicyTag** | **String** | Resource name of this policy tag&#39;s parent policy tag. If empty, this is a top level tag. If not set, defaults to an empty string. For example, for the \&quot;LatLong\&quot; policy tag in the example above, this field contains the resource name of the \&quot;Geolocation\&quot; policy tag, and, for \&quot;Geolocation\&quot;, this field is empty. |  [optional] |



