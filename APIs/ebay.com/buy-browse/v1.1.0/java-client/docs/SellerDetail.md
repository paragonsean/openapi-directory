

# SellerDetail

The type that defines the fields for basic and detailed information about the seller of the item returned by the <b> item</b> resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**feedbackPercentage** | **String** | The percentage of the total positive feedback. |  [optional] |
|**feedbackScore** | **Integer** | The feedback score of the seller. This value is based on the ratings from eBay members that bought items from this seller. |  [optional] |
|**sellerAccountType** | **String** | This indicates if the seller is a business or an individual. This is determined when the seller registers with eBay. If they register for a business account, this value will be BUSINESS. If they register for a private account, this value will be INDIVIDUAL. This designation is required by the tax laws in the following countries: This field is returned only on the following sites. EBAY_AT, EBAY_BE, EBAY_CH, EBAY_DE, EBAY_ES, EBAY_FR, EBAY_GB, EBAY_IE, EBAY_IT, EBAY_PL Valid Values: BUSINESS or INDIVIDUAL Code so that your app gracefully handles any future changes to this list. |  [optional] |
|**sellerLegalInfo** | [**SellerLegalInfo**](SellerLegalInfo.md) |  |  [optional] |
|**username** | **String** | The user name created by the seller for use on eBay. |  [optional] |



