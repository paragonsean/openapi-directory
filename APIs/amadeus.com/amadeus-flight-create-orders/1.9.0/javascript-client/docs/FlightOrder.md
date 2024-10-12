# FlightCreateOrders.FlightOrder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associatedRecords** | [**[AssociatedRecord]**](AssociatedRecord.md) | list of associated record | [optional] [readonly] 
**automatedProcess** | [**[AutomatedProcess]**](AutomatedProcess.md) | list of automatic queuing | [optional] 
**contacts** | [**[Contact]**](Contact.md) | list of general contact information | [optional] 
**flightOffers** | [**[FlightOffer]**](FlightOffer.md) | list of flight offer | 
**formOfIdentifications** | [**[FormOfIdentification]**](FormOfIdentification.md) | list of forms of identifications applicable to travelers by airline | [optional] 
**formOfPayments** | [**[FormOfPayment]**](FormOfPayment.md) | list of form of payments | [optional] [readonly] 
**id** | **String** | unique identifier of the flight order | [optional] [readonly] 
**ownerOfficeId** | **String** | office Id where will be transfered the ownership of the order | [optional] 
**queuingOfficeId** | **String** | office Id where to queue the order | [optional] 
**remarks** | [**Remarks**](Remarks.md) |  | [optional] 
**ticketingAgreement** | [**TicketingAgreement**](TicketingAgreement.md) |  | [optional] 
**tickets** | [**[AirTravelDocument]**](AirTravelDocument.md) | list of tickets | [optional] [readonly] 
**travelers** | [**[Traveler]**](Traveler.md) | list of travelers | [optional] 
**type** | **String** | the resource name | 


