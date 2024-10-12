

# LineItemFlight

Settings that control the active duration of a line item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateRange** | [**DateRange**](DateRange.md) |  |  [optional] |
|**flightDateType** | [**FlightDateTypeEnum**](#FlightDateTypeEnum) | Required. The type of the line item&#39;s flight dates. |  [optional] |
|**triggerId** | **String** | The ID of the manual trigger associated with the line item. * Required when flight_date_type is &#x60;LINE_ITEM_FLIGHT_DATE_TYPE_TRIGGER&#x60;. Must not be set otherwise. * When set, the line item&#39;s flight dates are inherited from its parent insertion order. * Active line items will spend when the selected trigger is activated within the parent insertion order&#39;s flight dates. **Warning:** Line Items using manual triggers no longer serve in Display &amp; Video 360. This field will sunset on August 1, 2023. Read our [feature deprecation announcement](/display-video/api/deprecations#features.manual_triggers) for more information. |  [optional] |



## Enum: FlightDateTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;LINE_ITEM_FLIGHT_DATE_TYPE_UNSPECIFIED&quot; |
| INHERITED | &quot;LINE_ITEM_FLIGHT_DATE_TYPE_INHERITED&quot; |
| CUSTOM | &quot;LINE_ITEM_FLIGHT_DATE_TYPE_CUSTOM&quot; |
| TRIGGER | &quot;LINE_ITEM_FLIGHT_DATE_TYPE_TRIGGER&quot; |



