# GoogleCloudMemorystoreForRedisApi.Location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The friendly name for this location, typically a nearby city name. For example, \&quot;Tokyo\&quot;. | [optional] 
**labels** | **{String: String}** | Cross-service attributes for the location. For example {\&quot;cloud.googleapis.com/region\&quot;: \&quot;us-east1\&quot;} | [optional] 
**locationId** | **String** | Resource ID for the region. For example: \&quot;us-east1\&quot;. | [optional] 
**metadata** | **{String: Object}** | Output only. The set of available zones in the location. The map is keyed by the lowercase ID of each zone, as defined by Compute Engine. These keys can be specified in &#x60;location_id&#x60; or &#x60;alternative_location_id&#x60; fields when creating a Redis instance. | [optional] 
**name** | **String** | Full resource name for the region. For example: \&quot;projects/example-project/locations/us-east1\&quot;. | [optional] 


