# RecommendationsAiBeta.GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **String** | Required. The filter string to specify the events to be deleted. Empty string filter is not allowed. The eligible fields for filtering are: * &#x60;eventType&#x60;: UserEvent.eventType field of type string. * &#x60;eventTime&#x60;: in ISO 8601 \&quot;zulu\&quot; format. * &#x60;visitorId&#x60;: field of type string. Specifying this will delete all events associated with a visitor. * &#x60;userId&#x60;: field of type string. Specifying this will delete all events associated with a user. Examples: * Deleting all events in a time range: &#x60;eventTime &gt; \&quot;2012-04-23T18:25:43.511Z\&quot; eventTime &lt; \&quot;2012-04-23T18:30:43.511Z\&quot;&#x60; * Deleting specific eventType in time range: &#x60;eventTime &gt; \&quot;2012-04-23T18:25:43.511Z\&quot; eventType &#x3D; \&quot;detail-page-view\&quot;&#x60; * Deleting all events for a specific visitor: &#x60;visitorId &#x3D; \&quot;visitor1024\&quot;&#x60; The filtering fields are assumed to have an implicit AND. | [optional] 
**force** | **Boolean** | Optional. The default value is false. Override this flag to true to actually perform the purge. If the field is not set to true, a sampling of events to be deleted will be returned. | [optional] 


