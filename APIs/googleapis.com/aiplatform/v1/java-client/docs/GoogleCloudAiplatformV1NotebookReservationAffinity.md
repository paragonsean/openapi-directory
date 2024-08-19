

# GoogleCloudAiplatformV1NotebookReservationAffinity

Notebook Reservation Affinity for consuming Zonal reservation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumeReservationType** | [**ConsumeReservationTypeEnum**](#ConsumeReservationTypeEnum) | Required. Specifies the type of reservation from which this instance can consume resources: RESERVATION_ANY (default), RESERVATION_SPECIFIC, or RESERVATION_NONE. See Consuming reserved instances for examples. |  [optional] |
|**key** | **String** | Optional. Corresponds to the label key of a reservation resource. To target a RESERVATION_SPECIFIC by name, use compute.googleapis.com/reservation-name as the key and specify the name of your reservation as its value. |  [optional] |
|**values** | **List&lt;String&gt;** | Optional. Corresponds to the label values of a reservation resource. This must be the full path name of Reservation. |  [optional] |



## Enum: ConsumeReservationTypeEnum

| Name | Value |
|---- | -----|
| AFFINITY_TYPE_UNSPECIFIED | &quot;RESERVATION_AFFINITY_TYPE_UNSPECIFIED&quot; |
| NONE | &quot;RESERVATION_NONE&quot; |
| ANY | &quot;RESERVATION_ANY&quot; |
| SPECIFIC | &quot;RESERVATION_SPECIFIC&quot; |



