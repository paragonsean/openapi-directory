# CanadaHolidaysApi.Holiday

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **Date** | ISO date: the literal date of the holiday | 
**federal** | **Number** | Whether this holiday is observed by federally-regulated industries. | 
**id** | **Number** | Primary key for a holiday | 
**nameEn** | **String** | English name | 
**nameFr** | **String** | French name | 
**observedDate** | **Date** | ISO date: when this holiday is observed | 
**optional** | **Number** | Whether this is a province-wide statutory holiday, or one that is optional for employers. | [optional] 
**provinces** | [**[Province]**](Province.md) |  | [optional] 



## Enum: FederalEnum


* `1` (value: `1`)

* `0` (value: `0`)





## Enum: OptionalEnum


* `1` (value: `1`)




