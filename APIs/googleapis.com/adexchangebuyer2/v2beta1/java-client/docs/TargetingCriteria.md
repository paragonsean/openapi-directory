

# TargetingCriteria

Advertisers can target different attributes of an ad slot. For example, they can choose to show ads only if the user is in the U.S. Such targeting criteria can be specified as part of Shared Targeting.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exclusions** | [**List&lt;TargetingValue&gt;**](TargetingValue.md) | The list of values to exclude from targeting. Each value is AND&#39;d together. |  [optional] |
|**inclusions** | [**List&lt;TargetingValue&gt;**](TargetingValue.md) | The list of value to include as part of the targeting. Each value is OR&#39;d together. |  [optional] |
|**key** | **String** | The key representing the shared targeting criterion. Targeting criteria defined by Google ad servers will begin with GOOG_. Third parties may define their own keys. A list of permissible keys along with the acceptable values will be provided as part of the external documentation. |  [optional] |



