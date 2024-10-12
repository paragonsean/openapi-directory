

# Facility

A facility provided by this API is either a public elevator or escalator located at a German railway station.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Textual description of the facility. |  [optional] |
|**equipmentnumber** | **Long** | Unique identifier of the facility. |  |
|**geocoordX** | **Double** | Longitude component of geocoordinate in WGS84 format. |  [optional] |
|**geocoordY** | **Double** | Latitude component of geocoordinate in WGS84 format. |  [optional] |
|**operatorname** | **String** | The name of the operator of the facility. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Operational state of the facility. |  |
|**stateExplanation** | **String** | Detailed description of the state. |  [optional] |
|**stationnumber** | **Long** | Number of the station the facility belongs to. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the facility. |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ESCALATOR | &quot;ESCALATOR&quot; |
| ELEVATOR | &quot;ELEVATOR&quot; |



