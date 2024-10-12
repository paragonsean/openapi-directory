

# FloodlightActivityGroup

Contains properties of a Floodlight activity group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of this floodlight activity group. This is a read-only field that can be left blank. |  [optional] |
|**advertiserId** | **String** | Advertiser ID of this floodlight activity group. If this field is left blank, the value will be copied over either from the floodlight configuration&#39;s advertiser or from the existing activity group&#39;s advertiser. |  [optional] |
|**advertiserIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**floodlightConfigurationId** | **String** | Floodlight configuration ID of this floodlight activity group. This is a required field. |  [optional] |
|**floodlightConfigurationIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**id** | **String** | ID of this floodlight activity group. This is a read-only, auto-generated field. |  [optional] |
|**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#floodlightActivityGroup\&quot;. |  [optional] |
|**name** | **String** | Name of this floodlight activity group. This is a required field. Must be less than 65 characters long and cannot contain quotes. |  [optional] |
|**subaccountId** | **String** | Subaccount ID of this floodlight activity group. This is a read-only field that can be left blank. |  [optional] |
|**tagString** | **String** | Value of the type&#x3D; parameter in the floodlight tag, which the ad servers use to identify the activity group that the activity belongs to. This is optional: if empty, a new tag string will be generated for you. This string must be 1 to 8 characters long, with valid characters being a-z0-9[ _ ]. This tag string must also be unique among activity groups of the same floodlight configuration. This field is read-only after insertion. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the floodlight activity group. This is a required field that is read-only after insertion. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COUNTER | &quot;COUNTER&quot; |
| SALE | &quot;SALE&quot; |



