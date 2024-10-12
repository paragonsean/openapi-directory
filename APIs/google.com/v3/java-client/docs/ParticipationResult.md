

# ParticipationResult

Represents a result from querying for participation stats for an account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | [**Key**](Key.md) |  |  [optional] |
|**missedParticipationCount** | **String** | The total number of opportunities **not** eligible for the Google Ads auction process. Comprised of the following: * Landing page missing * Price missing * Price problem * Price unavailable * Other |  [optional] |
|**missedParticipationCountDetails** | [**MissedParticipationCountDetails**](MissedParticipationCountDetails.md) |  |  [optional] |
|**opportunityCount** | **String** | For a specific hotel, the total number of opportunities that were available. Opportunities are the total number of instances when a hotel ad could have been displayed to a user. |  [optional] |
|**participationCount** | **String** | The total number of opportunities for which you were eligible to enter in the Google Ads auction process. |  [optional] |
|**participationPercent** | **Double** | The percentage rate of participation where the number of successfully participated opportunities is divided by the total number of opportunities. For example, if a property was eligible to enter the Google Ads auction 90 times out of 100 opportunities, the participation rate is 90%. |  [optional] |
|**partnerHotelDisplayName** | **String** | Partner&#39;s hotel display name. This field is only populated when the result is aggregated by &#x60;partnerHotelId&#x60;. |  [optional] |



