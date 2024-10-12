

# ExpirationPolicy

A policy that specifies the conditions for resource expiration (i.e., automatic resource deletion).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ttl** | **String** | Optional. Specifies the \&quot;time-to-live\&quot; duration for an associated resource. The resource expires if it is not active for a period of &#x60;ttl&#x60;. The definition of \&quot;activity\&quot; depends on the type of the associated resource. The minimum and maximum allowed values for &#x60;ttl&#x60; depend on the type of the associated resource, as well. If &#x60;ttl&#x60; is not set, the associated resource never expires. |  [optional] |



