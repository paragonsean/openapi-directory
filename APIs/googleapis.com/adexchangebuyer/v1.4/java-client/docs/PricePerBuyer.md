

# PricePerBuyer

Used to specify pricing rules for buyers. Each PricePerBuyer in a product can become [0,1] deals. To check if there is a PricePerBuyer for a particular buyer we look for the most specific matching rule - we first look for a rule matching the buyer and otherwise look for a matching rule where no buyer is set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auctionTier** | **String** | Optional access type for this buyer. |  [optional] |
|**billedBuyer** | [**Buyer**](Buyer.md) |  |  [optional] |
|**buyer** | [**Buyer**](Buyer.md) |  |  [optional] |
|**price** | [**Price**](Price.md) |  |  [optional] |



