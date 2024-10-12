

# FlightOrder

input parameter to create a flight order

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associatedRecords** | [**List&lt;AssociatedRecord&gt;**](AssociatedRecord.md) | list of associated record |  [optional] [readonly] |
|**automatedProcess** | [**List&lt;AutomatedProcess&gt;**](AutomatedProcess.md) | list of automatic queuing |  [optional] |
|**contacts** | [**List&lt;Contact&gt;**](Contact.md) | list of general contact information |  [optional] |
|**flightOffers** | [**List&lt;FlightOffer&gt;**](FlightOffer.md) | list of flight offer |  |
|**formOfIdentifications** | [**List&lt;FormOfIdentification&gt;**](FormOfIdentification.md) | list of forms of identifications applicable to travelers by airline |  [optional] |
|**formOfPayments** | [**List&lt;FormOfPayment&gt;**](FormOfPayment.md) | list of form of payments |  [optional] [readonly] |
|**id** | **String** | unique identifier of the flight order |  [optional] [readonly] |
|**ownerOfficeId** | **String** | office Id where will be transfered the ownership of the order |  [optional] |
|**queuingOfficeId** | **String** | office Id where to queue the order |  [optional] |
|**remarks** | [**Remarks**](Remarks.md) |  |  [optional] |
|**ticketingAgreement** | [**TicketingAgreement**](TicketingAgreement.md) |  |  [optional] |
|**tickets** | [**List&lt;AirTravelDocument&gt;**](AirTravelDocument.md) | list of tickets |  [optional] [readonly] |
|**travelers** | [**List&lt;Traveler&gt;**](Traveler.md) | list of travelers |  [optional] |
|**type** | **String** | the resource name |  |



