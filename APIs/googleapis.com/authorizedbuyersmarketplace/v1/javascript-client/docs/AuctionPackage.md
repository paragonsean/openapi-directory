# AuthorizedBuyersMarketplaceApi.AuctionPackage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Time the auction package was created. | [optional] [readonly] 
**creator** | **String** | Output only. The buyer that created this auction package. Format: &#x60;buyers/{buyerAccountId}&#x60; | [optional] [readonly] 
**description** | **String** | Output only. A description of the auction package. | [optional] [readonly] 
**displayName** | **String** | The display_name assigned to the auction package. | [optional] 
**name** | **String** | Immutable. The unique identifier for the auction package. Format: &#x60;buyers/{accountId}/auctionPackages/{auctionPackageId}&#x60; The auction_package_id part of name is sent in the BidRequest to all RTB bidders and is returned as deal_id by the bidder in the BidResponse. | [optional] 
**subscribedClients** | **[String]** | Output only. The list of clients of the current buyer that are subscribed to the AuctionPackage. Format: &#x60;buyers/{buyerAccountId}/clients/{clientAccountId}&#x60; | [optional] [readonly] 
**updateTime** | **String** | Output only. Time the auction package was last updated. This value is only increased when this auction package is updated but never when a buyer subscribed. | [optional] [readonly] 


