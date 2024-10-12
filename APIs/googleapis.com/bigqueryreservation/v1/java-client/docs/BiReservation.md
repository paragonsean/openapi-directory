

# BiReservation

Represents a BI Reservation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The resource name of the singleton BI reservation. Reservation names have the form &#x60;projects/{project_id}/locations/{location_id}/biReservation&#x60;. |  [optional] |
|**preferredTables** | [**List&lt;TableReference&gt;**](TableReference.md) | Preferred tables to use BI capacity for. |  [optional] |
|**size** | **String** | Size of a reservation, in bytes. |  [optional] |
|**updateTime** | **String** | Output only. The last update timestamp of a reservation. |  [optional] [readonly] |



