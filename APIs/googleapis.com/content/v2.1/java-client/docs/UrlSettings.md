

# UrlSettings

Specifications related to the `Checkout` URL. The `UriTemplate` is of the form `https://www.mystore.com/checkout?item_id={id}` where `{id}` will be automatically replaced with data from the merchant account with this attribute [offer_id](https://developers.google.com/shopping-content/reference/rest/v2.1/products#Product.FIELDS.offer_id)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cartUriTemplate** | **String** | URL template when the placeholders are expanded will redirect the buyer to the cart page on the merchant website with the selected item in cart. |  [optional] |
|**checkoutUriTemplate** | **String** | URL template when the placeholders are expanded will redirect the buyer to the merchant checkout page with the item in the cart. |  [optional] |



