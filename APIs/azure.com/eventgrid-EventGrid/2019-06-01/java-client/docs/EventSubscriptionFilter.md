

# EventSubscriptionFilter

Filter for the Event Subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advancedFilters** | [**List&lt;AdvancedFilter&gt;**](AdvancedFilter.md) | An array of advanced filters that are used for filtering event subscriptions. |  [optional] |
|**includedEventTypes** | **List&lt;String&gt;** | A list of applicable event types that need to be part of the event subscription. If it is desired to subscribe to all default event types, set the IncludedEventTypes to null. |  [optional] |
|**isSubjectCaseSensitive** | **Boolean** | Specifies if the SubjectBeginsWith and SubjectEndsWith properties of the filter   should be compared in a case sensitive manner. |  [optional] |
|**subjectBeginsWith** | **String** | An optional string to filter events for an event subscription based on a resource path prefix.  The format of this depends on the publisher of the events.   Wildcard characters are not supported in this path. |  [optional] |
|**subjectEndsWith** | **String** | An optional string to filter events for an event subscription based on a resource path suffix.  Wildcard characters are not supported in this path. |  [optional] |



