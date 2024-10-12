

# LoadBalancingSettingsListResult

Result of the request to list load balancing settings. It contains a list of load balancing settings objects and a URL link to get the next set of results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextLink** | **String** | URL to get the next set of LoadBalancingSettings objects if there are any. |  [optional] |
|**value** | [**List&lt;LoadBalancingSettingsModel&gt;**](LoadBalancingSettingsModel.md) | List of Backend Pools within a Front Door. |  [optional] [readonly] |



