

# MotorcycleListing

Represents a full list of attributes available with Marketcheck for a car

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**build** | [**MotorcycleBuild**](MotorcycleBuild.md) |  |  [optional] |
|**color** | **String** | Color of the motorcycle |  [optional] |
|**dealer** | [**NestDealer**](NestDealer.md) |  |  [optional] |
|**dpUrl** | **String** | Details Page url of the specific motorcycle |  [optional] |
|**extra** | [**ListingNestExtraAttributes**](ListingNestExtraAttributes.md) |  |  [optional] |
|**firstSeenAt** | **Integer** | Listing first seen at first scraped timestamp |  [optional] |
|**firstSeenAtDate** | **String** | Listing first seen at first scraped date |  [optional] |
|**heading** | **String** | Listing title as displayed on the source website |  [optional] |
|**id** | **String** | Unique identifier representing a specific listing from the Marketcheck database |  [optional] |
|**inventoryType** | **String** | Inventory type of motorcycle |  [optional] |
|**lastSeenAt** | **Integer** | Listing last seen at (most recent) timestamp |  [optional] |
|**lastSeenAtDate** | **String** | Listing last seen at (most recent) date |  [optional] |
|**media** | [**ListingNestMedia**](ListingNestMedia.md) |  |  [optional] |
|**miles** | **Integer** | Odometer reading / reported miles usage for the motorcycle |  [optional] |
|**msrp** | **Integer** | MSRP for the motorcycle |  [optional] |
|**price** | **Integer** | Asking price for the motorcycle |  [optional] |
|**scrapedAt** | **BigDecimal** | Listing last seen at date timestamp |  [optional] |
|**scrapedAtDate** | **String** | Listing last seen at date |  [optional] |
|**sellerType** | **String** | Seller type for the motorcycle |  [optional] |
|**source** | **String** | Source domain of the listing |  [optional] |
|**stockNo** | **String** | Stock number of motorcycle in dealers inventory |  [optional] |
|**vin** | **String** | VIN for the Motorcycle |  [optional] |



