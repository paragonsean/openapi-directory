# Betriebsstellen.Station

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RB** | **Number** | Regional code | [optional] 
**UIC** | **String** | UIC RICS code | [optional] 
**abbrev** | **String** | Abbrevation name of station or halt | [optional] 
**borderStation** | **Boolean** | Station is at a country border | [optional] 
**id** | **Number** | Identifying number | [optional] 
**locationCode** | **String** | Primary location code | [optional] 
**name** | **String** | Long name of station or halt | [optional] 
**_short** | **String** | Short name of station or halt | [optional] 
**status** | **String** | State of operation | [optional] 
**timeTableRelevant** | **Boolean** | Relevant for time table | [optional] 
**type** | **String** | Type of station or halt | [optional] 
**validFrom** | **String** | Start date for validity | [optional] 
**validTill** | **String** | End date for validity or null if still valid | [optional] 



## Enum: StatusEnum


* `in use` (value: `"in use"`)

* `out of service` (value: `"out of service"`)

* `formerly` (value: `"formerly"`)

* `planned` (value: `"planned"`)

* `study` (value: `"study"`)





## Enum: TypeEnum


* `Abzw` (value: `"Abzw"`)

* `Anst` (value: `"Anst"`)

* `Awanst` (value: `"Awanst"`)

* `Bf` (value: `"Bf"`)




