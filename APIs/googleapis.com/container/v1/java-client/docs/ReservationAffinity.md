

# ReservationAffinity

[ReservationAffinity](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) is the configuration of desired reservation which instances could take capacity from.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumeReservationType** | [**ConsumeReservationTypeEnum**](#ConsumeReservationTypeEnum) | Corresponds to the type of reservation consumption. |  [optional] |
|**key** | **String** | Corresponds to the label key of a reservation resource. To target a SPECIFIC_RESERVATION by name, specify \&quot;compute.googleapis.com/reservation-name\&quot; as the key and specify the name of your reservation as its value. |  [optional] |
|**values** | **List&lt;String&gt;** | Corresponds to the label value(s) of reservation resource(s). |  [optional] |



## Enum: ConsumeReservationTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| NO_RESERVATION | &quot;NO_RESERVATION&quot; |
| ANY_RESERVATION | &quot;ANY_RESERVATION&quot; |
| SPECIFIC_RESERVATION | &quot;SPECIFIC_RESERVATION&quot; |



