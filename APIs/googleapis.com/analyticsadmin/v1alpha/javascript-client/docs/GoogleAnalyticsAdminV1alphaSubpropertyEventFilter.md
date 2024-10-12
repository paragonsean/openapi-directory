# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaSubpropertyEventFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applyToProperty** | **String** | Immutable. Resource name of the Subproperty that uses this filter. | [optional] 
**filterClauses** | [**[GoogleAnalyticsAdminV1alphaSubpropertyEventFilterClause]**](GoogleAnalyticsAdminV1alphaSubpropertyEventFilterClause.md) | Required. Unordered list. Filter clauses that define the SubpropertyEventFilter. All clauses are AND&#39;ed together to determine what data is sent to the subproperty. | [optional] 
**name** | **String** | Output only. Format: properties/{ordinary_property_id}/subpropertyEventFilters/{sub_property_event_filter} Example: properties/1234/subpropertyEventFilters/5678 | [optional] [readonly] 


