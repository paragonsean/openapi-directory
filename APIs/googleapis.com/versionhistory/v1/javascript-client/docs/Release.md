# VersionhistoryGoogleapisComApi.Release

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fraction** | **Number** | Rollout fraction. This fraction indicates the fraction of people that should receive this version in this release. If the fraction is not specified in ReleaseManager, the API will assume fraction is 1. | [optional] 
**fractionGroup** | **String** | Rollout fraction group. Only fractions with the same fraction_group are statistically comparable: there may be non-fractional differences between different fraction groups. | [optional] 
**name** | **String** | Release name. Format is \&quot;{product}/platforms/{platform}/channels/{channel}/versions/{version}/releases/{release}\&quot; | [optional] 
**serving** | [**Interval**](Interval.md) |  | [optional] 
**version** | **String** | String containing just the version number. e.g. \&quot;84.0.4147.38\&quot; | [optional] 


