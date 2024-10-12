

# AdditionalDataLodging


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lodgingCheckInDate** | **String** | The arrival date. * Date format: **yyyyMmDd**. For example, for 2023 April 22, **20230422**. |  [optional] |
|**lodgingCheckOutDate** | **String** | The departure date. * Date format: **yyyyMmDd**. For example, for 2023 April 22, **20230422**. |  [optional] |
|**lodgingCustomerServiceTollFreeNumber** | **String** | The toll-free phone number for the lodging. * Format: numeric * Max length: 17 characters. * For US and CA numbers must be 10 characters in length * Must not start with a space * Must not contain any special characters such as + or - *Must not be all zeros. |  [optional] |
|**lodgingFireSafetyActIndicator** | **String** | Identifies that the facility complies with the Hotel and Motel Fire Safety Act of 1990. Must be &#39;Y&#39; or &#39;N&#39;. * Format: alphabetic * Max length: 1 character |  [optional] |
|**lodgingFolioCashAdvances** | **String** | The folio cash advances, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Format: numeric * Max length: 12 characters |  [optional] |
|**lodgingFolioNumber** | **String** | The card acceptor’s internal invoice or billing ID reference number. * Max length: 25 characters. * Must not start with a space *Must not be all zeros. |  [optional] |
|**lodgingFoodBeverageCharges** | **String** | Any charges for food and beverages associated with the booking, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Format: numeric * Max length: 12 characters |  [optional] |
|**lodgingNoShowIndicator** | **String** | Indicates if the customer didn&#39;t check in for their booking.  Possible values:  * **Y**: the customer didn&#39;t check in  * **N**: the customer checked in |  [optional] |
|**lodgingPrepaidExpenses** | **String** | The prepaid expenses for the booking. * Format: numeric * Max length: 12 characters |  [optional] |
|**lodgingPropertyPhoneNumber** | **String** | The lodging property location&#39;s phone number. * Format: numeric. * Min length: 10 characters * Max length: 17 characters * For US and CA numbers must be 10 characters in length * Must not start with a space * Must not contain any special characters such as + or - *Must not be all zeros. |  [optional] |
|**lodgingRoom1NumberOfNights** | **String** | The total number of nights the room is booked for. * Format: numeric * Must be a number between 0 and 99 * Max length: 4 characters |  [optional] |
|**lodgingRoom1Rate** | **String** | The rate for the room, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Format: numeric * Max length: 12 characters * Must not be a negative number |  [optional] |
|**lodgingTotalRoomTax** | **String** | The total room tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Format: numeric * Max length: 12 characters * Must not be a negative number |  [optional] |
|**lodgingTotalTax** | **String** | The total tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). * Format: numeric * Max length: 12 characters * Must not be a negative number |  [optional] |
|**travelEntertainmentAuthDataDuration** | **String** | The number of nights. This should be included in the auth message. * Format: numeric * Max length: 4 characters |  [optional] |
|**travelEntertainmentAuthDataMarket** | **String** | Indicates what market-specific dataset will be submitted. Must be &#39;H&#39; for Hotel. This should be included in the auth message.  * Format: alphanumeric * Max length: 1 character |  [optional] |



