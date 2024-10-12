

# PublisherConnection

An Open Bidding exchange's connection to a publisher. This is initiated by the publisher for the bidder to review. If approved by the bidder, this means that the bidder agrees to receive bid requests from the publisher.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**biddingState** | [**BiddingStateEnum**](#BiddingStateEnum) | Whether the publisher has been approved by the bidder. |  [optional] |
|**createTime** | **String** | Output only. The time at which the publisher initiated a connection with the bidder (irrespective of if or when the bidder approves it). This is subsequently updated if the publisher revokes and re-initiates the connection. |  [optional] [readonly] |
|**displayName** | **String** | Output only. Publisher display name. |  [optional] [readonly] |
|**name** | **String** | Output only. Name of the publisher connection. This follows the pattern &#x60;bidders/{bidder}/publisherConnections/{publisher}&#x60;, where &#x60;{bidder}&#x60; represents the account ID of the bidder, and &#x60;{publisher}&#x60; is the ads.txt/app-ads.txt publisher ID. |  [optional] [readonly] |
|**publisherPlatform** | [**PublisherPlatformEnum**](#PublisherPlatformEnum) | Output only. Whether the publisher is an Ad Manager or AdMob publisher. |  [optional] [readonly] |



## Enum: BiddingStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| REJECTED | &quot;REJECTED&quot; |
| APPROVED | &quot;APPROVED&quot; |



## Enum: PublisherPlatformEnum

| Name | Value |
|---- | -----|
| PUBLISHER_PLATFORM_UNSPECIFIED | &quot;PUBLISHER_PLATFORM_UNSPECIFIED&quot; |
| GOOGLE_AD_MANAGER | &quot;GOOGLE_AD_MANAGER&quot; |
| ADMOB | &quot;ADMOB&quot; |



