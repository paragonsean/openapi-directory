# HetrasBookingApiVersion0.Offer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{String: LinkObject}**](LinkObject.md) | Link to request addon offers for this stay | [optional] 
**adults** | **Number** | Number of adults the offer is calculated for | [optional] 
**availableRooms** | **Number** | Number of currently available rooms for that specific offer | [optional] 
**breakdown** | [**[RoomOfferDailyRate]**](RoomOfferDailyRate.md) | In this collection you will get an entry with price information for every day. | [optional] 
**cancellationPolicies** | [**[CancellationPolicy]**](CancellationPolicy.md) | List of cancellation policies defined for that rate | [optional] 
**currency** | **String** | The amounts of this offer are always in this currency | [optional] 
**depositPolicies** | [**[DepositPolicy]**](DepositPolicy.md) | List of Deposit policies defined for that rate | [optional] 
**generalPolicies** | [**[GeneralPolicy]**](GeneralPolicy.md) | List of general policies defined for that rate | [optional] 
**guaranteeTypes** | [**AcceptedGuaranteeTypes**](AcceptedGuaranteeTypes.md) |  | [optional] 
**includedServices** | **[String]** | A list of  of services included already in the rate for this offer | [optional] 
**noshowPolicy** | [**NoShowPolicy**](NoShowPolicy.md) |  | [optional] 
**ratePlanCode** | **String** | The code of the rate plan for this offer | [optional] 
**totalStay** | [**Rate**](Rate.md) |  | [optional] 


