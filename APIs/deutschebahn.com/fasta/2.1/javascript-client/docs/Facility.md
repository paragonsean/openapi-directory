# FaStaStationFacilitiesStatus.Facility

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Textual description of the facility. | [optional] 
**equipmentnumber** | **Number** | Unique identifier of the facility. | 
**geocoordX** | **Number** | Longitude component of geocoordinate in WGS84 format. | [optional] 
**geocoordY** | **Number** | Latitude component of geocoordinate in WGS84 format. | [optional] 
**operatorname** | **String** | The name of the operator of the facility. | [optional] 
**state** | **String** | Operational state of the facility. | 
**stateExplanation** | **String** | Detailed description of the state. | [optional] 
**stationnumber** | **Number** | Number of the station the facility belongs to. | 
**type** | **String** | Type of the facility. | 



## Enum: StateEnum


* `ACTIVE` (value: `"ACTIVE"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `UNKNOWN` (value: `"UNKNOWN"`)





## Enum: TypeEnum


* `ESCALATOR` (value: `"ESCALATOR"`)

* `ELEVATOR` (value: `"ELEVATOR"`)




