# PtvTimetableApiVersion3.V3DynamoDbTimetable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicableLocalDate** | **String** | Formated date string of applicable date | [optional] [readonly] 
**exists** | **Boolean** | True if the named table has been created in DynamoDB (i.e. at least one departure record has been loaded),              or false if there are no records for this date and transport type. | [optional] 
**parserMappingVersion** | **String** | Diva Mapping Version used to load Parser into DynamoDB | [optional] 
**parserVersion** | **Number** | Parser verison | [optional] 
**ptMappingVersion** | **String** | Diva Mapping Version used to load PT into DynamoDB | [optional] 
**ptVersion** | **Number** | PT version | [optional] 
**tableName** | **String** | Name of corresponding table in DynamoDB. | [optional] 
**transportType** | **Number** | A.k.a. Transport Mode (e.g. Train, Tram, Bus, V/Line, Nightrider) | [optional] 



## Enum: TransportTypeEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)




