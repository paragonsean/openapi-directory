

# BuyingOptionDistribution

The container that defines the fields for the buying options refinements. This container is returned when <b> fieldgroups</b> is set to <code>BUYING_OPTION_REFINEMENTS</code> or <code>FULL</code> in the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buyingOption** | **String** | The container that returns the buying option type. This will be AUCTION or FIXED_PRICE or both. For details, see buyingOptions. |  [optional] |
|**matchCount** | **Integer** | The number of items having this buying option. |  [optional] |
|**refinementHref** | **String** | The HATEOAS reference for this buying option. |  [optional] |



