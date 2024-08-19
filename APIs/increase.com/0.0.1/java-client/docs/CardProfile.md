

# CardProfile

This contains artwork and metadata relating to a Card's appearance in digital wallet apps like Apple Pay and Google Pay. For more information, see our guide on [digital card artwork](https://increase.com/documentation/card-art)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the Card Dispute was created. |  |
|**description** | **String** | A description you can use to identify the Card Profile. |  |
|**digitalWallets** | [**DigitalWallets**](DigitalWallets.md) |  |  |
|**id** | **String** | The Card Profile identifier. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the Card Profile. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;card_profile&#x60;. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| REJECTED | &quot;rejected&quot; |
| ACTIVE | &quot;active&quot; |
| ARCHIVED | &quot;archived&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CARD_PROFILE | &quot;card_profile&quot; |



