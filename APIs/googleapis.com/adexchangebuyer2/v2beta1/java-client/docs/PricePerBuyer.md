

# PricePerBuyer

Used to specify pricing rules for buyers/advertisers. Each PricePerBuyer in a product can become 0 or 1 deals. To check if there is a PricePerBuyer for a particular buyer or buyer/advertiser pair, we look for the most specific matching rule - we first look for a rule matching the buyer and advertiser, next a rule with the buyer but an empty advertiser list, and otherwise look for a matching rule where no buyer is set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserIds** | **List&lt;String&gt;** | The list of advertisers for this price when associated with this buyer. If empty, all advertisers with this buyer pay this price. |  [optional] |
|**buyer** | [**Buyer**](Buyer.md) |  |  [optional] |
|**price** | [**Price**](Price.md) |  |  [optional] |



