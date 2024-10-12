

# RRSetRoutingPolicy

A RRSetRoutingPolicy represents ResourceRecordSet data that is returned dynamically with the response varying based on configured properties such as geolocation or by weighted random selection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**geo** | [**RRSetRoutingPolicyGeoPolicy**](RRSetRoutingPolicyGeoPolicy.md) |  |  [optional] |
|**geoPolicy** | [**RRSetRoutingPolicyGeoPolicy**](RRSetRoutingPolicyGeoPolicy.md) |  |  [optional] |
|**healthCheck** | **String** | The selfLink attribute of the HealthCheck resource to use for this RRSetRoutingPolicy. https://cloud.google.com/compute/docs/reference/rest/v1/healthChecks |  [optional] |
|**kind** | **String** |  |  [optional] |
|**primaryBackup** | [**RRSetRoutingPolicyPrimaryBackupPolicy**](RRSetRoutingPolicyPrimaryBackupPolicy.md) |  |  [optional] |
|**wrr** | [**RRSetRoutingPolicyWrrPolicy**](RRSetRoutingPolicyWrrPolicy.md) |  |  [optional] |
|**wrrPolicy** | [**RRSetRoutingPolicyWrrPolicy**](RRSetRoutingPolicyWrrPolicy.md) |  |  [optional] |



