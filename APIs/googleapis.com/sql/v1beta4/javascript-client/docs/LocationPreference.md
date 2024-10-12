# CloudSqlAdminApi.LocationPreference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**followGaeApplication** | **String** | The App Engine application to follow, it must be in the same region as the Cloud SQL instance. WARNING: Changing this might restart the instance. | [optional] 
**kind** | **String** | This is always &#x60;sql#locationPreference&#x60;. | [optional] 
**secondaryZone** | **String** | The preferred Compute Engine zone for the secondary/failover (for example: us-central1-a, us-central1-b, etc.). To disable this field, set it to &#39;no_secondary_zone&#39;. | [optional] 
**zone** | **String** | The preferred Compute Engine zone (for example: us-central1-a, us-central1-b, etc.). WARNING: Changing this might restart the instance. | [optional] 


