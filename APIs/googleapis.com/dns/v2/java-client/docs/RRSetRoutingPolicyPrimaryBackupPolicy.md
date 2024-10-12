

# RRSetRoutingPolicyPrimaryBackupPolicy

Configures a RRSetRoutingPolicy such that all queries are responded with the primary_targets if they are healthy. And if all of them are unhealthy, then we fallback to a geo localized policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupGeoTargets** | [**RRSetRoutingPolicyGeoPolicy**](RRSetRoutingPolicyGeoPolicy.md) |  |  [optional] |
|**kind** | **String** |  |  [optional] |
|**primaryTargets** | [**RRSetRoutingPolicyHealthCheckTargets**](RRSetRoutingPolicyHealthCheckTargets.md) |  |  [optional] |
|**trickleTraffic** | **Double** | When serving state is PRIMARY, this field provides the option of sending a small percentage of the traffic to the backup targets. |  [optional] |



