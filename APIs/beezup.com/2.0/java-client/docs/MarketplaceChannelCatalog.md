

# MarketplaceChannelCatalog

This object indicates you the association between a channel catalog and a marketplace. The account identifier will be automatically defined based on your marketplace merchant identfier.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiSettingsStatus** | **BeezUPCommonApiSettingsStatus** |  |  |
|**beezUPChannelCatalogId** | **String** | The channel catalog identifier |  |
|**beezUPChannelId** | **String** | The channel identifier |  |
|**beezUPMarketplaceName** | **Object** | The marketplace name |  |
|**beezUPStoreId** | **String** | The store identifier |  |
|**beezUPStoreName** | **String** | The store name |  |
|**enabled** | **Boolean** | The enabled status of the Channel Catalog |  |
|**links** | [**MarketplaceChannelCatalogLinks**](MarketplaceChannelCatalogLinks.md) |  |  |
|**lovLinks** | [**MarketplaceChannelCatalogLovLinks**](MarketplaceChannelCatalogLovLinks.md) |  |  |
|**marketplaceAccountId** | **Integer** | The marketplace account identifier in BeezUP. This account identifier is based on your api settings. |  [optional] |
|**marketplaceBusinessCode** | **String** | In an marketplace technical code like CDiscount you can have several marketplaces like GO SPORT, etc. We identify them by a business code. |  |
|**marketplaceIsoCountryCodeAlpha2** | **String** | The marketplace country iso code alpha 2 (see http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Decoding_table for more details) |  |
|**marketplaceMarketPlaceId** | **String** | The marketplace identifier in the marketplace |  |
|**marketplaceMerchantIdentifiers** | **Map&lt;String, String&gt;** | The marketplace merchant identifier list |  [optional] |
|**marketplaceTechnicalCode** | **String** | The technical code of the marketplace. |  |



