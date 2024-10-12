# NetworkServicesApi.HttpRouteRouteRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**HttpRouteRouteAction**](HttpRouteRouteAction.md) |  | [optional] 
**matches** | [**[HttpRouteRouteMatch]**](HttpRouteRouteMatch.md) | A list of matches define conditions used for matching the rule against incoming HTTP requests. Each match is independent, i.e. this rule will be matched if ANY one of the matches is satisfied. If no matches field is specified, this rule will unconditionally match traffic. If a default rule is desired to be configured, add a rule with no matches specified to the end of the rules list. | [optional] 


