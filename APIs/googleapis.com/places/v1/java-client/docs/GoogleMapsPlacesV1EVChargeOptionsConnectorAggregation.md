

# GoogleMapsPlacesV1EVChargeOptionsConnectorAggregation

EV charging information grouped by [type, max_charge_rate_kw]. Shows EV charge aggregation of connectors that have the same type and max charge rate in kw.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilityLastUpdateTime** | **String** | The timestamp when the connector availability information in this aggregation was last updated. |  [optional] |
|**availableCount** | **Integer** | Number of connectors in this aggregation that are currently available. |  [optional] |
|**count** | **Integer** | Number of connectors in this aggregation. |  [optional] |
|**maxChargeRateKw** | **Double** | The static max charging rate in kw of each connector in the aggregation. |  [optional] |
|**outOfServiceCount** | **Integer** | Number of connectors in this aggregation that are currently out of service. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The connector type of this aggregation. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;EV_CONNECTOR_TYPE_UNSPECIFIED&quot; |
| OTHER | &quot;EV_CONNECTOR_TYPE_OTHER&quot; |
| J1772 | &quot;EV_CONNECTOR_TYPE_J1772&quot; |
| TYPE_2 | &quot;EV_CONNECTOR_TYPE_TYPE_2&quot; |
| CHADEMO | &quot;EV_CONNECTOR_TYPE_CHADEMO&quot; |
| CCS_COMBO_1 | &quot;EV_CONNECTOR_TYPE_CCS_COMBO_1&quot; |
| CCS_COMBO_2 | &quot;EV_CONNECTOR_TYPE_CCS_COMBO_2&quot; |
| TESLA | &quot;EV_CONNECTOR_TYPE_TESLA&quot; |
| UNSPECIFIED_GB_T | &quot;EV_CONNECTOR_TYPE_UNSPECIFIED_GB_T&quot; |
| UNSPECIFIED_WALL_OUTLET | &quot;EV_CONNECTOR_TYPE_UNSPECIFIED_WALL_OUTLET&quot; |



