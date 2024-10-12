

# Offer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**Map&lt;String, LinkObject&gt;**](LinkObject.md) | Link to request addon offers for this stay |  [optional] |
|**adults** | **Integer** | Number of adults the offer is calculated for |  [optional] |
|**availableRooms** | **Integer** | Number of currently available rooms for that specific offer |  [optional] |
|**breakdown** | [**List&lt;RoomOfferDailyRate&gt;**](RoomOfferDailyRate.md) | In this collection you will get an entry with price information for every day. |  [optional] |
|**cancellationPolicies** | [**List&lt;CancellationPolicy&gt;**](CancellationPolicy.md) | List of cancellation policies defined for that rate |  [optional] |
|**currency** | **String** | The amounts of this offer are always in this currency |  [optional] |
|**depositPolicies** | [**List&lt;DepositPolicy&gt;**](DepositPolicy.md) | List of Deposit policies defined for that rate |  [optional] |
|**generalPolicies** | [**List&lt;GeneralPolicy&gt;**](GeneralPolicy.md) | List of general policies defined for that rate |  [optional] |
|**guaranteeTypes** | [**AcceptedGuaranteeTypes**](AcceptedGuaranteeTypes.md) |  |  [optional] |
|**includedServices** | **List&lt;String&gt;** | A list of  of services included already in the rate for this offer |  [optional] |
|**noshowPolicy** | [**NoShowPolicy**](NoShowPolicy.md) |  |  [optional] |
|**ratePlanCode** | **String** | The code of the rate plan for this offer |  [optional] |
|**totalStay** | [**Rate**](Rate.md) |  |  [optional] |



