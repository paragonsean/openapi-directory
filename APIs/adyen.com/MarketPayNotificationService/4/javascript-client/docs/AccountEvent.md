# ClassicPlatformsNotifications.AccountEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **String** | The event. &gt;Permitted values: &#x60;InactivateAccount&#x60;, &#x60;RefundNotPaidOutTransfers&#x60;. For more information, refer to [Verification checks](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process). | [optional] 
**executionDate** | **Date** | The date on which the event will take place. | [optional] 
**reason** | **String** | The reason why this event has been created. | [optional] 



## Enum: EventEnum


* `InactivateAccount` (value: `"InactivateAccount"`)

* `RefundNotPaidOutTransfers` (value: `"RefundNotPaidOutTransfers"`)




