

# ProgrammaticGuaranteedTerms

Pricing terms for Programmatic Guaranteed Deals.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fixedPrice** | [**Price**](Price.md) |  |  [optional] |
|**guaranteedLooks** | **String** | Count of guaranteed looks. For CPD deals, buyer changes to guaranteed_looks will be ignored. |  [optional] |
|**impressionCap** | **String** | The lifetime impression cap for CPM Sponsorship deals. Deal will stop serving when cap is reached. |  [optional] |
|**minimumDailyLooks** | **String** | Daily minimum looks for CPD deal types. For CPD deals, buyer should negotiate on this field instead of guaranteed_looks. |  [optional] |
|**percentShareOfVoice** | **String** | For sponsorship deals, this is the percentage of the seller&#39;s eligible impressions that the deal will serve until the cap is reached. Valid value is within range 0~100. |  [optional] |
|**reservationType** | [**ReservationTypeEnum**](#ReservationTypeEnum) | The reservation type for a Programmatic Guaranteed deal. This indicates whether the number of impressions is fixed, or a percent of available impressions. If not specified, the default reservation type is STANDARD. |  [optional] |



## Enum: ReservationTypeEnum

| Name | Value |
|---- | -----|
| RESERVATION_TYPE_UNSPECIFIED | &quot;RESERVATION_TYPE_UNSPECIFIED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| SPONSORSHIP | &quot;SPONSORSHIP&quot; |



