

# TcpRouteRouteMatch

RouteMatch defines the predicate used to match requests to a given action. Multiple match types are \"OR\"ed for evaluation. If no routeMatch field is specified, this rule will unconditionally match traffic.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Required. Must be specified in the CIDR range format. A CIDR range consists of an IP Address and a prefix length to construct the subnet mask. By default, the prefix length is 32 (i.e. matches a single IP address). Only IPV4 addresses are supported. Examples: \&quot;10.0.0.1\&quot; - matches against this exact IP address. \&quot;10.0.0.0/8\&quot; - matches against any IP address within the 10.0.0.0 subnet and 255.255.255.0 mask. \&quot;0.0.0.0/0\&quot; - matches against any IP address&#39;. |  [optional] |
|**port** | **String** | Required. Specifies the destination port to match against. |  [optional] |



