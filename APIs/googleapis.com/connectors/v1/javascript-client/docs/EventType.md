# ConnectorsApi.EventType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Created time. | [optional] [readonly] 
**enrichedEventPayloadSchema** | **String** | Output only. Schema of the event payload after enriched. Will be null if read before send is not supported. | [optional] [readonly] 
**entityType** | **String** | Output only. Runtime entity type name. Will be null if entity type map is not available. Used for read before send feature. | [optional] [readonly] 
**eventPayloadSchema** | **String** | Output only. Schema of webhook event payload. | [optional] [readonly] 
**eventTypeId** | **String** | Output only. Event type id. Example: &#x60;ticket.created&#x60;. | [optional] [readonly] 
**idPath** | **String** | Output only. Id path denotes the path of id in webhook payload. | [optional] [readonly] 
**name** | **String** | Output only. Resource name of the eventtype. Format: projects/{project}/locations/{location}/providers/{provider}/connectors/{connector}/versions/{version}/eventtypes/{eventtype} Only global location is supported for Connector resource. | [optional] [readonly] 
**updateTime** | **String** | Output only. Updated time. | [optional] [readonly] 


