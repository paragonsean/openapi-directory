

# Location

Location returns the location name, and if the location is recommended for GKE cluster scheduling.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Contains the name of the resource requested. Specified in the format &#x60;projects/_*_/locations/_*&#x60;. |  [optional] |
|**recommended** | **Boolean** | Whether the location is recommended for GKE cluster scheduling. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Contains the type of location this Location is for. Regional or Zonal. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LOCATION_TYPE_UNSPECIFIED | &quot;LOCATION_TYPE_UNSPECIFIED&quot; |
| ZONE | &quot;ZONE&quot; |
| REGION | &quot;REGION&quot; |



