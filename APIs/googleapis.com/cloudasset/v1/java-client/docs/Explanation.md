

# Explanation

Explanation about the IAM policy search result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**matchedPermissions** | [**Map&lt;String, Permissions&gt;**](Permissions.md) | The map from roles to their included permissions that match the permission query (i.e., a query containing &#x60;policy.role.permissions:&#x60;). Example: if query &#x60;policy.role.permissions:compute.disk.get&#x60; matches a policy binding that contains owner role, the matched_permissions will be &#x60;{\&quot;roles/owner\&quot;: [\&quot;compute.disk.get\&quot;]}&#x60;. The roles can also be found in the returned &#x60;policy&#x60; bindings. Note that the map is populated only for requests with permission queries. |  [optional] |



