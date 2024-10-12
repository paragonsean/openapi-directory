

# GoogleAdsSearchads360V0CommonTargetImpressionShare

An automated bidding strategy that sets bids so that a certain percentage of search ads are shown at the top of the first page (or other targeted location).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cpcBidCeilingMicros** | **String** | The highest CPC bid the automated bidding system is permitted to specify. This is a required field entered by the advertiser that sets the ceiling and specified in local micros. |  [optional] |
|**location** | [**LocationEnum**](#LocationEnum) | The targeted location on the search results page. |  [optional] |
|**locationFractionMicros** | **String** | The chosen fraction of ads to be shown in the targeted location in micros. For example, 1% equals 10,000. |  [optional] |



## Enum: LocationEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ANYWHERE_ON_PAGE | &quot;ANYWHERE_ON_PAGE&quot; |
| TOP_OF_PAGE | &quot;TOP_OF_PAGE&quot; |
| ABSOLUTE_TOP_OF_PAGE | &quot;ABSOLUTE_TOP_OF_PAGE&quot; |



