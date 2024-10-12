

# ListingsPostRequestPreorderInfo

Create or update a preorder listing. Requires opt-in. Please contact sales@reverb.com if you would like to activate this feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**leadTime** | **Integer** | The amount of time before the item will be ready to ship. When lead_time is submitted it is converted into days and added to the current date to produce &#x60;estimated_ship_date&#x60; in the response body of the request. |  [optional] |
|**leadTimeUnit** | [**LeadTimeUnitEnum**](#LeadTimeUnitEnum) | The unit of time which lead_time is measured in |  |
|**shipDate** | **String** | The date the item will be available to ship. In the response body of the request, &#x60;estimated_ship_date&#x60;, will be the same as ship_date. Date must be ISO8601 format - e.g: 2015-04-09T10:52:23-00:00. |  [optional] |



## Enum: LeadTimeUnitEnum

| Name | Value |
|---- | -----|
| DAYS | &quot;days&quot; |
| WEEKS | &quot;weeks&quot; |



