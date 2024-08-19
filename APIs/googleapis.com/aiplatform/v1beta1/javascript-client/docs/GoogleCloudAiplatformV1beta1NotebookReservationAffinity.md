# VertexAiApi.GoogleCloudAiplatformV1beta1NotebookReservationAffinity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumeReservationType** | **String** | Required. Specifies the type of reservation from which this instance can consume resources: RESERVATION_ANY (default), RESERVATION_SPECIFIC, or RESERVATION_NONE. See Consuming reserved instances for examples. | [optional] 
**key** | **String** | Optional. Corresponds to the label key of a reservation resource. To target a RESERVATION_SPECIFIC by name, use compute.googleapis.com/reservation-name as the key and specify the name of your reservation as its value. | [optional] 
**values** | **[String]** | Optional. Corresponds to the label values of a reservation resource. This must be the full path name of Reservation. | [optional] 



## Enum: ConsumeReservationTypeEnum


* `AFFINITY_TYPE_UNSPECIFIED` (value: `"RESERVATION_AFFINITY_TYPE_UNSPECIFIED"`)

* `NONE` (value: `"RESERVATION_NONE"`)

* `ANY` (value: `"RESERVATION_ANY"`)

* `SPECIFIC` (value: `"RESERVATION_SPECIFIC"`)




