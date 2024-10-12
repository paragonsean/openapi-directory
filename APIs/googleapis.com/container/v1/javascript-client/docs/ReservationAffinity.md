# KubernetesEngineApi.ReservationAffinity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumeReservationType** | **String** | Corresponds to the type of reservation consumption. | [optional] 
**key** | **String** | Corresponds to the label key of a reservation resource. To target a SPECIFIC_RESERVATION by name, specify \&quot;compute.googleapis.com/reservation-name\&quot; as the key and specify the name of your reservation as its value. | [optional] 
**values** | **[String]** | Corresponds to the label value(s) of reservation resource(s). | [optional] 



## Enum: ConsumeReservationTypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `NO_RESERVATION` (value: `"NO_RESERVATION"`)

* `ANY_RESERVATION` (value: `"ANY_RESERVATION"`)

* `SPECIFIC_RESERVATION` (value: `"SPECIFIC_RESERVATION"`)




