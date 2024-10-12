

# Rate

Information on the price of the room, other components of the room (such as breakfast, lunch or a welcome drink) and the cancellation policies that apply.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cancellationPolicies** | [**Set&lt;CancellationPolicy&gt;**](CancellationPolicy.md) |  |  |
|**components** | [**Set&lt;RateComponent&gt;**](RateComponent.md) |  |  |
|**end** | **LocalDate** |  |  |
|**hotelAgreement** | [**HotelAgreementStub**](HotelAgreementStub.md) |  |  |
|**maxOccupancy** | **Integer** | Maximum number of adults included in the rate. |  |
|**rateId** | **String** |  |  |
|**ratePlanId** | **Integer** | The rate plan ID that is attached to this rate. Each rate plan ID can specify a unique combination of a cancellation policy and a meal plan. |  [optional] |
|**retailRate** | [**BookedRateRetailRate**](BookedRateRetailRate.md) |  |  |
|**roomsSellable** | **BigDecimal** | Amount of rooms which can be sold for this occupancy level and room type at this rate price. |  [optional] |
|**sellerCommissionPercentage** | **Float** | The commission percentage you as a seller will earn from this booking, based on &#x60;retailRate.total&#x60;. |  |
|**sellerToImpalaPayment** | [**Money**](Money.md) | This is the amount payable to the hotel, which Impala will collect from you on the hotel&#39;s behalf. The Impala fee will be requested in addition to this, and also documented in a VAT invoice. |  [optional] |
|**start** | **LocalDate** |  |  |



