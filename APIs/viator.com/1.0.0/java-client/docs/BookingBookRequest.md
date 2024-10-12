

# BookingBookRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**booker** | [**BookingBookRequestBooker**](BookingBookRequestBooker.md) |  |  [optional] |
|**currencyCode** | **String** | **currency code** for the currency the booking will be submitted in (you will be billed in this currency) |  [optional] |
|**demo** | **Boolean** | **specifier**: &#x60;true&#x60; if this is a *demo* booking only (demos do not send any notifications, are automatically confirmed and OnRequest products become freesale products. Default value is true. Production must have &#x60;demo&#x60; set to &#x60;false&#x60;. |  [optional] |
|**items** | [**List&lt;BookingBookRequestItemsInner&gt;**](BookingBookRequestItemsInner.md) | **array** of items to be booked |  [optional] |
|**partnerDetail** | [**BookingBookRequestPartnerDetail**](BookingBookRequestPartnerDetail.md) |  |  [optional] |



