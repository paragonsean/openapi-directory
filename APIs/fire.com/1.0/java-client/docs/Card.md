

# Card


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blocked** | **Boolean** | Whether the card is blocked or not |  [optional] |
|**cardId** | **Long** | card id assigned by fire.com |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date-time the card was created |  [optional] |
|**emailAddress** | **String** | card user email address |  [optional] |
|**eurIcan** | **Long** | identifier for the eur fire.com account (assigned by fire.com) |  [optional] |
|**expiryDate** | **OffsetDateTime** | card expiry date |  [optional] |
|**firstName** | **String** | card user first name |  [optional] |
|**gbpIcan** | **Long** | identifier for the gbp fire.com account (assigned by fire.com) |  [optional] |
|**lastName** | **String** | card user last name |  [optional] |
|**maskedPan** | **String** | card number (masked) |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) | card provider |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | card status |  [optional] |
|**statusReason** | [**StatusReasonEnum**](#StatusReasonEnum) | reason for card status |  [optional] |
|**userId** | **Long** | card user id assigned by fire.com |  [optional] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| MASTERCARD | &quot;MASTERCARD&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| LIVE | &quot;LIVE&quot; |
| CREATED_ACTIVE | &quot;CREATED_ACTIVE&quot; |
| CREATED_INACTIVE | &quot;CREATED_INACTIVE&quot; |
| DEACTIVATED | &quot;DEACTIVATED&quot; |



## Enum: StatusReasonEnum

| Name | Value |
|---- | -----|
| LOST_CARD | &quot;LOST_CARD&quot; |
| STOLEN_CARD | &quot;STOLEN_CARD&quot; |
| CARD_DESTROYED | &quot;CARD_DESTROYED&quot; |



