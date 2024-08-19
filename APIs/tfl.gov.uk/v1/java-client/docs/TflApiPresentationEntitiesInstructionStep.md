

# TflApiPresentationEntitiesInstructionStep


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cumulativeDistance** | **Integer** |  |  [optional] |
|**cumulativeTravelTime** | **Integer** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**descriptionHeading** | **String** |  |  [optional] |
|**distance** | **Integer** |  |  [optional] |
|**latitude** | **Double** |  |  [optional] |
|**longitude** | **Double** |  |  [optional] |
|**pathAttribute** | [**TflApiPresentationEntitiesPathAttribute**](TflApiPresentationEntitiesPathAttribute.md) |  |  [optional] |
|**skyDirection** | **Integer** |  |  [optional] |
|**skyDirectionDescription** | [**SkyDirectionDescriptionEnum**](#SkyDirectionDescriptionEnum) |  |  [optional] |
|**streetName** | **String** |  |  [optional] |
|**trackType** | [**TrackTypeEnum**](#TrackTypeEnum) |  |  [optional] |
|**turnDirection** | **String** |  |  [optional] |



## Enum: SkyDirectionDescriptionEnum

| Name | Value |
|---- | -----|
| NORTH | &quot;North&quot; |
| NORTH_EAST | &quot;NorthEast&quot; |
| EAST | &quot;East&quot; |
| SOUTH_EAST | &quot;SouthEast&quot; |
| SOUTH | &quot;South&quot; |
| SOUTH_WEST | &quot;SouthWest&quot; |
| WEST | &quot;West&quot; |
| NORTH_WEST | &quot;NorthWest&quot; |



## Enum: TrackTypeEnum

| Name | Value |
|---- | -----|
| CYCLE_SUPER_HIGHWAY | &quot;CycleSuperHighway&quot; |
| CANAL_TOWPATH | &quot;CanalTowpath&quot; |
| QUIET_ROAD | &quot;QuietRoad&quot; |
| PROVISION_FOR_CYCLISTS | &quot;ProvisionForCyclists&quot; |
| BUSY_ROADS | &quot;BusyRoads&quot; |
| NONE | &quot;None&quot; |
| PUSH_BIKE | &quot;PushBike&quot; |
| QUIETWAY | &quot;Quietway&quot; |



