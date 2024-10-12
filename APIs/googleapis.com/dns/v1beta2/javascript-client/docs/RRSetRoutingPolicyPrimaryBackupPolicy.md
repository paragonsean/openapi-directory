# CloudDnsApi.RRSetRoutingPolicyPrimaryBackupPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupGeoTargets** | [**RRSetRoutingPolicyGeoPolicy**](RRSetRoutingPolicyGeoPolicy.md) |  | [optional] 
**kind** | **String** |  | [optional] [default to &#39;dns#rRSetRoutingPolicyPrimaryBackupPolicy&#39;]
**primaryTargets** | [**RRSetRoutingPolicyHealthCheckTargets**](RRSetRoutingPolicyHealthCheckTargets.md) |  | [optional] 
**trickleTraffic** | **Number** | When serving state is PRIMARY, this field provides the option of sending a small percentage of the traffic to the backup targets. | [optional] 


