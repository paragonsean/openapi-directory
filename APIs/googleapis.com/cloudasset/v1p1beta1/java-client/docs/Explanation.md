

# Explanation

Explanation about the IAM policy search result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**matchedPermissions** | [**Map&lt;String, Permissions&gt;**](Permissions.md) | The map from roles to their included permission matching the permission query (e.g. containing &#x60;policy.role.permissions:&#x60;). Example role string: \&quot;roles/compute.instanceAdmin\&quot;. The roles can also be found in the returned &#x60;policy&#x60; bindings. Note that the map is populated only if requesting with a permission query. |  [optional] |



