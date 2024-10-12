# RealTimeBiddingApi.Buyer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeCreativeCount** | **String** | Output only. The number of creatives that this buyer submitted through the API or bid with in the last 30 days. This is counted against the maximum number of active creatives. | [optional] [readonly] 
**bidder** | **String** | Output only. The name of the bidder resource that is responsible for receiving bidding traffic for this account. The bidder name must follow the pattern &#x60;bidders/{bidderAccountId}&#x60;, where &#x60;{bidderAccountId}&#x60; is the account ID of the bidder receiving traffic for this buyer. | [optional] [readonly] 
**billingIds** | **[String]** | Output only. A list of billing IDs associated with this account. These IDs appear on: 1. A bid request, to signal which buyers are eligible to bid on a given opportunity, and which pretargeting configurations were matched for each eligible buyer. 2. The bid response, to attribute a winning impression to a specific account for billing, reporting, policy and publisher block enforcement. | [optional] [readonly] 
**displayName** | **String** | Output only. The diplay name associated with this buyer account, as visible to sellers. | [optional] [readonly] 
**maximumActiveCreativeCount** | **String** | Output only. The maximum number of active creatives that this buyer can have. | [optional] [readonly] 
**name** | **String** | Output only. Name of the buyer resource that must follow the pattern &#x60;buyers/{buyerAccountId}&#x60;, where &#x60;{buyerAccountId}&#x60; is the account ID of the buyer account whose information is to be received. One can get their account ID on the Authorized Buyers or Open Bidding UI, or by contacting their Google account manager. | [optional] [readonly] 


