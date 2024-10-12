

# FormOfIdentification

alternative means of identifying stakeholders for eTicket.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carrierCode** | **String** | providing the airline / carrier code |  [optional] |
|**flightOfferIds** | **List&lt;String&gt;** | Id of the concerned flightOffers |  [optional] |
|**identificationType** | [**IdentificationTypeEnum**](#IdentificationTypeEnum) | Type of identification |  [optional] |
|**number** | **String** | identification number relative to the type of identification either ticket number, booking number, passport number, identity card number, drivers licence number, other ID |  [optional] |
|**travelerIds** | **List&lt;String&gt;** | Ids of the concerned travelers |  [optional] |



## Enum: IdentificationTypeEnum

| Name | Value |
|---- | -----|
| DRIVERS_LICENSE | &quot;DRIVERS_LICENSE&quot; |
| PASSPORT | &quot;PASSPORT&quot; |
| NATIONAL_IDENTITY_CARD | &quot;NATIONAL_IDENTITY_CARD&quot; |
| BOOKING_CONFIRMATION | &quot;BOOKING_CONFIRMATION&quot; |
| TICKET | &quot;TICKET&quot; |
| OTHER_ID | &quot;OTHER_ID&quot; |



