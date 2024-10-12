

# GrpcRouteRouteRule

Describes how to route traffic.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**GrpcRouteRouteAction**](GrpcRouteRouteAction.md) |  |  [optional] |
|**matches** | [**List&lt;GrpcRouteRouteMatch&gt;**](GrpcRouteRouteMatch.md) | Optional. Matches define conditions used for matching the rule against incoming gRPC requests. Each match is independent, i.e. this rule will be matched if ANY one of the matches is satisfied. If no matches field is specified, this rule will unconditionally match traffic. |  [optional] |



