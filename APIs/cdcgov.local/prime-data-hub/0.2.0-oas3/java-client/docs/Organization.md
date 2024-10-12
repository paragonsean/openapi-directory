

# Organization

An organization connected to data hub

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countyName** | **String** | the county name (must match FIPS name) |  [optional] |
|**description** | **String** | the displayable description of the organization |  |
|**jurisdiction** | [**JurisdictionEnum**](#JurisdictionEnum) |  |  |
|**meta** | [**SettingMetadata**](SettingMetadata.md) |  |  [optional] |
|**name** | **String** | the unique id for the organization |  |
|**stateCode** | **String** | the two letter code for the organization |  [optional] |



## Enum: JurisdictionEnum

| Name | Value |
|---- | -----|
| NATIONAL | &quot;National&quot; |
| STATE | &quot;State&quot; |
| COUNTY | &quot;County&quot; |



