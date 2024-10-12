# EventGridManagementClient.EventSubscriptionFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advancedFilters** | [**[AdvancedFilter]**](AdvancedFilter.md) | A list of advanced filters. | [optional] 
**includedEventTypes** | **[String]** | A list of applicable event types that need to be part of the event subscription.   If it is desired to subscribe to all event types, the string \&quot;all\&quot; needs to be specified as an element in this list. | [optional] 
**isSubjectCaseSensitive** | **Boolean** | Specifies if the SubjectBeginsWith and SubjectEndsWith properties of the filter   should be compared in a case sensitive manner. | [optional] [default to false]
**subjectBeginsWith** | **String** | An optional string to filter events for an event subscription based on a resource path prefix.  The format of this depends on the publisher of the events.   Wildcard characters are not supported in this path. | [optional] 
**subjectEndsWith** | **String** | An optional string to filter events for an event subscription based on a resource path suffix.  Wildcard characters are not supported in this path. | [optional] 


