# FlightOrderManagement.AirTravelDocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentNumber** | **String** | Identifier of the travel document prefixed by its owner code [NALC - 3 digits]. Can either be a primary or a conjunctive document number. Necessary for TicketingReference definition. | [optional] 
**documentStatus** | **String** | Status of the travel document contained in the fare element | [optional] 
**documentType** | **String** | Type of the travel document | [optional] 
**segmentIds** | **[String]** | Ids of the impacted segments | [optional] 
**travelerId** | **String** | id of the impacted traveler | [optional] 



## Enum: DocumentStatusEnum


* `ISSUED` (value: `"ISSUED"`)

* `REFUNDED` (value: `"REFUNDED"`)

* `VOID` (value: `"VOID"`)

* `ORIGINAL` (value: `"ORIGINAL"`)

* `EXCHANGED` (value: `"EXCHANGED"`)





## Enum: DocumentTypeEnum


* `ETICKET` (value: `"ETICKET"`)

* `PTICKET` (value: `"PTICKET"`)

* `EMD` (value: `"EMD"`)

* `MCO` (value: `"MCO"`)




