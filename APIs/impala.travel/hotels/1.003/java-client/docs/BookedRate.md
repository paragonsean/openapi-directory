

# BookedRate

Information on the price of the booked room, other components of the room (such as breakfast, lunch or a welcome drink) and the cancellation policies that apply.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cancellationPolicies** | [**Set&lt;CancellationPolicy&gt;**](CancellationPolicy.md) |  |  |
|**components** | [**Set&lt;RateComponent&gt;**](RateComponent.md) |  |  |
|**end** | **LocalDate** |  |  |
|**hotelAgreement** | [**HotelAgreementStub**](HotelAgreementStub.md) |  |  |
|**maxOccupancy** | **BigDecimal** |  |  [optional] |
|**retailRate** | [**BookedRateRetailRate**](BookedRateRetailRate.md) |  |  |
|**sellerCommissionPercentage** | **Float** | The commission percentage you as a seller will earn from this booking, based on &#x60;retailRate.total&#x60;. |  |
|**start** | **LocalDate** |  |  |



