

# HotelProductDepositPolicy

the deposit/prepay policy information applicable to the offer. It includes accepted payments, deadline and the amount due

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptedPayments** | [**HotelProductPaymentPolicy**](HotelProductPaymentPolicy.md) |  |  [optional] |
|**amount** | **String** | Deposit-Prepay amount |  [optional] |
|**deadline** | **OffsetDateTime** | The date and time of the deadline in ISO 8601[https://www.w3.org/TR/NOTE-datetime].   Example: 2010-08-14T13:00:00  Please note that this value is expressed in the hotels local time zone |  [optional] |
|**description** | [**QualifiedFreeText**](QualifiedFreeText.md) |  |  [optional] |



