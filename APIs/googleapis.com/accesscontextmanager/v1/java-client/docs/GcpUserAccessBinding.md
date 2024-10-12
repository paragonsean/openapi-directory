

# GcpUserAccessBinding

Restricts access to Cloud Console and Google Cloud APIs for a set of users using Context-Aware Access.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessLevels** | **List&lt;String&gt;** | Optional. Access level that a user must have to be granted access. Only one access level is supported, not multiple. This repeated field must have exactly one element. Example: \&quot;accessPolicies/9522/accessLevels/device_trusted\&quot; |  [optional] |
|**dryRunAccessLevels** | **List&lt;String&gt;** | Optional. Dry run access level that will be evaluated but will not be enforced. The access denial based on dry run policy will be logged. Only one access level is supported, not multiple. This list must have exactly one element. Example: \&quot;accessPolicies/9522/accessLevels/device_trusted\&quot; |  [optional] |
|**groupKey** | **String** | Required. Immutable. Google Group id whose members are subject to this binding&#39;s restrictions. See \&quot;id\&quot; in the [G Suite Directory API&#39;s Groups resource] (https://developers.google.com/admin-sdk/directory/v1/reference/groups#resource). If a group&#39;s email address/alias is changed, this resource will continue to point at the changed group. This field does not accept group email addresses or aliases. Example: \&quot;01d520gv4vjcrht\&quot; |  [optional] |
|**name** | **String** | Immutable. Assigned by the server during creation. The last segment has an arbitrary length and has only URI unreserved characters (as defined by [RFC 3986 Section 2.3](https://tools.ietf.org/html/rfc3986#section-2.3)). Should not be specified by the client during creation. Example: \&quot;organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N\&quot; |  [optional] |



