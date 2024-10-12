

# AmenitySeat

Characteristics for a group of seat, such as Distance from one seat to the another in front or behind it or width space

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amenityType** | [**AmenityTypeEnum**](#AmenityTypeEnum) |  |  [optional] |
|**legSpace** | **Integer** | Space between 2 seats |  [optional] |
|**medias** | [**List&lt;AmenityMedia&gt;**](AmenityMedia.md) | list of media associated to the seat (rich content) |  [optional] |
|**spaceUnit** | [**SpaceUnitEnum**](#SpaceUnitEnum) |  |  [optional] |
|**tilt** | [**TiltEnum**](#TiltEnum) | Flatness of a seat |  [optional] |



## Enum: AmenityTypeEnum

| Name | Value |
|---- | -----|
| SEAT | &quot;SEAT&quot; |



## Enum: SpaceUnitEnum

| Name | Value |
|---- | -----|
| INCHES | &quot;INCHES&quot; |
| CENTIMENTERS | &quot;CENTIMENTERS&quot; |



## Enum: TiltEnum

| Name | Value |
|---- | -----|
| FULL_FLAT | &quot;FULL_FLAT&quot; |
| ANGLE_FLAT | &quot;ANGLE_FLAT&quot; |
| NORMAL | &quot;NORMAL&quot; |



