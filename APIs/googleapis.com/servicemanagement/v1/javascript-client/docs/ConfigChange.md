# ServiceManagementApi.ConfigChange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advices** | [**[Advice]**](Advice.md) | Collection of advice provided for this change, useful for determining the possible impact of this change. | [optional] 
**changeType** | **String** | The type for this change, either ADDED, REMOVED, or MODIFIED. | [optional] 
**element** | **String** | Object hierarchy path to the change, with levels separated by a &#39;.&#39; character. For repeated fields, an applicable unique identifier field is used for the index (usually selector, name, or id). For maps, the term &#39;key&#39; is used. If the field has no unique identifier, the numeric index is used. Examples: - visibility.rules[selector&#x3D;&#x3D;\&quot;google.LibraryService.ListBooks\&quot;].restriction - quota.metric_rules[selector&#x3D;&#x3D;\&quot;google\&quot;].metric_costs[key&#x3D;&#x3D;\&quot;reads\&quot;].value - logging.producer_destinations[0] | [optional] 
**newValue** | **String** | Value of the changed object in the new Service configuration, in JSON format. This field will not be populated if ChangeType &#x3D;&#x3D; REMOVED. | [optional] 
**oldValue** | **String** | Value of the changed object in the old Service configuration, in JSON format. This field will not be populated if ChangeType &#x3D;&#x3D; ADDED. | [optional] 



## Enum: ChangeTypeEnum


* `CHANGE_TYPE_UNSPECIFIED` (value: `"CHANGE_TYPE_UNSPECIFIED"`)

* `ADDED` (value: `"ADDED"`)

* `REMOVED` (value: `"REMOVED"`)

* `MODIFIED` (value: `"MODIFIED"`)




