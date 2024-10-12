# CloudDnsApi.RRSetRoutingPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo** | [**RRSetRoutingPolicyGeoPolicy**](RRSetRoutingPolicyGeoPolicy.md) |  | [optional] 
**geoPolicy** | [**RRSetRoutingPolicyGeoPolicy**](RRSetRoutingPolicyGeoPolicy.md) |  | [optional] 
**healthCheck** | **String** | The selfLink attribute of the HealthCheck resource to use for this RRSetRoutingPolicy. https://cloud.google.com/compute/docs/reference/rest/v1/healthChecks | [optional] 
**kind** | **String** |  | [optional] [default to &#39;dns#rRSetRoutingPolicy&#39;]
**primaryBackup** | [**RRSetRoutingPolicyPrimaryBackupPolicy**](RRSetRoutingPolicyPrimaryBackupPolicy.md) |  | [optional] 
**wrr** | [**RRSetRoutingPolicyWrrPolicy**](RRSetRoutingPolicyWrrPolicy.md) |  | [optional] 
**wrrPolicy** | [**RRSetRoutingPolicyWrrPolicy**](RRSetRoutingPolicyWrrPolicy.md) |  | [optional] 


