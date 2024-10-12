# RealTimeBiddingApi.PublisherConnection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biddingState** | **String** | Whether the publisher has been approved by the bidder. | [optional] 
**createTime** | **String** | Output only. The time at which the publisher initiated a connection with the bidder (irrespective of if or when the bidder approves it). This is subsequently updated if the publisher revokes and re-initiates the connection. | [optional] [readonly] 
**displayName** | **String** | Output only. Publisher display name. | [optional] [readonly] 
**name** | **String** | Output only. Name of the publisher connection. This follows the pattern &#x60;bidders/{bidder}/publisherConnections/{publisher}&#x60;, where &#x60;{bidder}&#x60; represents the account ID of the bidder, and &#x60;{publisher}&#x60; is the ads.txt/app-ads.txt publisher ID. | [optional] [readonly] 
**publisherPlatform** | **String** | Output only. Whether the publisher is an Ad Manager or AdMob publisher. | [optional] [readonly] 



## Enum: BiddingStateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `REJECTED` (value: `"REJECTED"`)

* `APPROVED` (value: `"APPROVED"`)





## Enum: PublisherPlatformEnum


* `PUBLISHER_PLATFORM_UNSPECIFIED` (value: `"PUBLISHER_PLATFORM_UNSPECIFIED"`)

* `GOOGLE_AD_MANAGER` (value: `"GOOGLE_AD_MANAGER"`)

* `ADMOB` (value: `"ADMOB"`)




