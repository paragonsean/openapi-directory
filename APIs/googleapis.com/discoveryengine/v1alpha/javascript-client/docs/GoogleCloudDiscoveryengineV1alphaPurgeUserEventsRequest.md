# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaPurgeUserEventsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **String** | Required. The filter string to specify the events to be deleted with a length limit of 5,000 characters. The eligible fields for filtering are: * &#x60;eventType&#x60;: Double quoted UserEvent.event_type string. * &#x60;eventTime&#x60;: in ISO 8601 \&quot;zulu\&quot; format. * &#x60;userPseudoId&#x60;: Double quoted string. Specifying this will delete all events associated with a visitor. * &#x60;userId&#x60;: Double quoted string. Specifying this will delete all events associated with a user. Examples: * Deleting all events in a time range: &#x60;eventTime &gt; \&quot;2012-04-23T18:25:43.511Z\&quot; eventTime &lt; \&quot;2012-04-23T18:30:43.511Z\&quot;&#x60; * Deleting specific eventType: &#x60;eventType &#x3D; \&quot;search\&quot;&#x60; * Deleting all events for a specific visitor: &#x60;userPseudoId &#x3D; \&quot;visitor1024\&quot;&#x60; * Deleting all events inside a DataStore: &#x60;*&#x60; The filtering fields are assumed to have an implicit AND. | [optional] 
**force** | **Boolean** | The &#x60;force&#x60; field is currently not supported. Purge user event requests will permanently delete all purgeable events. Once the development is complete: If &#x60;force&#x60; is set to false, the method will return the expected purge count without deleting any user events. This field will default to false if not included in the request. | [optional] 


