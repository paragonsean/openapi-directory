

# ReservationAffinity

Reservation Affinity for consuming Zonal reservation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumeReservationType** | [**ConsumeReservationTypeEnum**](#ConsumeReservationTypeEnum) | Optional. Type of reservation to consume |  [optional] |
|**key** | **String** | Optional. Corresponds to the label key of reservation resource. |  [optional] |
|**values** | **List&lt;String&gt;** | Optional. Corresponds to the label values of reservation resource. |  [optional] |



## Enum: ConsumeReservationTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| NO_RESERVATION | &quot;NO_RESERVATION&quot; |
| ANY_RESERVATION | &quot;ANY_RESERVATION&quot; |
| SPECIFIC_RESERVATION | &quot;SPECIFIC_RESERVATION&quot; |



