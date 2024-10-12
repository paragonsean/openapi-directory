

# HotelBookingQuery


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**guests** | [**Set&lt;Stakeholder&gt;**](Stakeholder.md) | minimum one guest is mandatory |  |
|**offerId** | **String** | offerId to book |  |
|**payments** | [**Set&lt;Payment&gt;**](Payment.md) | payments (often mandatory) |  [optional] |
|**rooms** | [**List&lt;Room&gt;**](Room.md) | rooms repartition (when used the &#x60;rooms&#x60; array items must match the shopping offer &#x60;roomQuantity&#x60;) |  [optional] |



