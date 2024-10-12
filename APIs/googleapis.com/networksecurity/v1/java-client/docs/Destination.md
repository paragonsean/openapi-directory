

# Destination

Specification of traffic destination attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hosts** | **List&lt;String&gt;** | Required. List of host names to match. Matched against the \&quot;:authority\&quot; header in http requests. At least one host should match. Each host can be an exact match, or a prefix match (example \&quot;mydomain.*\&quot;) or a suffix match (example \&quot;*.myorg.com\&quot;) or a presence (any) match \&quot;*\&quot;. |  [optional] |
|**httpHeaderMatch** | [**HttpHeaderMatch**](HttpHeaderMatch.md) |  |  [optional] |
|**methods** | **List&lt;String&gt;** | Optional. A list of HTTP methods to match. At least one method should match. Should not be set for gRPC services. |  [optional] |
|**ports** | **List&lt;Integer&gt;** | Required. List of destination ports to match. At least one port should match. |  [optional] |



