

# Election

Information about the election that was queried.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**electionDay** | **String** | Day of the election in YYYY-MM-DD format. |  [optional] |
|**id** | **String** | The unique ID of this election. |  [optional] |
|**name** | **String** | A displayable name for the election. |  [optional] |
|**ocdDivisionId** | **String** | The political division of the election. Represented as an OCD Division ID. Voters within these political jurisdictions are covered by this election. This is typically a state such as ocd-division/country:us/state:ca or for the midterms or general election the entire US (i.e. ocd-division/country:us). |  [optional] |
|**shapeLookupBehavior** | [**ShapeLookupBehaviorEnum**](#ShapeLookupBehaviorEnum) |  |  [optional] |



## Enum: ShapeLookupBehaviorEnum

| Name | Value |
|---- | -----|
| SHAPE_LOOKUP_DEFAULT | &quot;shapeLookupDefault&quot; |
| SHAPE_LOOKUP_DISABLED | &quot;shapeLookupDisabled&quot; |
| SHAPE_LOOKUP_ENABLED | &quot;shapeLookupEnabled&quot; |



