

# GoogleCloudRedisV1LocationMetadata

This location metadata represents additional configuration options for a given location where a Redis instance may be created. All fields are output only. It is returned as content of the `google.cloud.location.Location.metadata` field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableZones** | **Map&lt;String, Object&gt;** | Output only. The set of available zones in the location. The map is keyed by the lowercase ID of each zone, as defined by GCE. These keys can be specified in &#x60;location_id&#x60; or &#x60;alternative_location_id&#x60; fields when creating a Redis instance. |  [optional] [readonly] |



