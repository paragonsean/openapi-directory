

# Listing

Represents a full list of attributes available with Marketcheck for a car

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseExtColor** | **String** | Base exterior color of the car |  [optional] |
|**baseIntColor** | **String** | Base interior color of the car |  [optional] |
|**build** | [**Build**](Build.md) |  |  [optional] |
|**carfax1Owner** | **Boolean** | Flag to indicate whether listing is carfax_1_owner |  [optional] |
|**carfaxCleanTitle** | **Boolean** | Flag to indicate whether listing is carfax_clean_title |  [optional] |
|**dataSource** | **String** | Data source of the listing |  [optional] |
|**dealer** | [**NestDealer**](NestDealer.md) |  |  [optional] |
|**dom** | **Integer** | Days on Market value for the car based on current and historical listings found in the Marketcheck database for this car |  [optional] |
|**dom180** | **Integer** | Days on Market value for the car based on current and last 6 month listings found in the Marketcheck database for this car |  [optional] |
|**domActive** | **Integer** | Days on Market value for the car based on current and last 30 days listings found in the Marketcheck database for this car |  [optional] |
|**exteriorColor** | **String** | Exterior color of the car |  [optional] |
|**extra** | [**ListingNestExtraAttributes**](ListingNestExtraAttributes.md) |  |  [optional] |
|**financingOptions** | [**List&lt;ListingFinance&gt;**](ListingFinance.md) | Array of all finance offers for this listing |  [optional] |
|**firstSeenAt** | **Integer** | Listing first seen at first scraped timestamp |  [optional] |
|**firstSeenAtDate** | **String** | Listing first seen at first scraped date |  [optional] |
|**firstSeenAtMc** | **Integer** | Listing first seen at first scraped at MC timestamp |  [optional] |
|**firstSeenAtMcDate** | **String** | Listing first seen at first scraped at MC date |  [optional] |
|**firstSeenAtSource** | **Integer** | Listing first seen at source relisted timestamp |  [optional] |
|**firstSeenAtSourceDate** | **String** | Listing first seen at source relisted date |  [optional] |
|**heading** | **String** | Listing title as displayed on the source website |  [optional] |
|**id** | **String** | Unique identifier representing a specific listing from the Marketcheck database |  [optional] |
|**interiorColor** | **String** | Interior color of the car |  [optional] |
|**inventoryType** | **String** | Inventory type of car |  [optional] |
|**isCertified** | **Integer** | Certified car |  [optional] |
|**lastSeenAt** | **Integer** | Listing last seen at (most recent) timestamp |  [optional] |
|**lastSeenAtDate** | **String** | Listing last seen at (most recent) date |  [optional] |
|**leasingOptions** | [**List&lt;ListingLease&gt;**](ListingLease.md) | Array of all finance offers for this listing |  [optional] |
|**media** | [**ListingNestMedia**](ListingNestMedia.md) |  |  [optional] |
|**miles** | **Integer** | Odometer reading / reported miles usage for the car |  [optional] |
|**msrp** | **Integer** | MSRP for the car |  [optional] |
|**price** | **Integer** | Asking price for the car |  [optional] |
|**priceChangePercent** | **Double** | Percentage difference between the cars&#39;s current price and ref_price i.e. last reported price |  [optional] |
|**rank** | **Integer** | Relative rank of the listing determined by ranking service |  [optional] |
|**refMiles** | **String** | Last Odometer reading / reported miles usage for the car. If the asking miles value is not or is available then the last_miles could perhaps be used. last_miles is the miles for the car listed on the source website as of last_miles_dt date |  [optional] |
|**refMilesDt** | **Integer** | The date at which the last miles was reported online. This is earlier to last_seen_date |  [optional] |
|**refPrice** | **String** | Last reported price for the car. If the asking price value is not or is available then the last_price could perhaps be used. last_price is the price for the car listed on the source website as of last_price_dt date |  [optional] |
|**refPriceDt** | **Integer** | The date at which the last price was reported online. This is earlier to last_seen_date |  [optional] |
|**score** | **Double** | Score of the ranked listing as per the ranking criteria determined by ranking service |  [optional] |
|**scrapedAt** | **Integer** | Listing last seen at date timestamp |  [optional] |
|**scrapedAtDate** | **String** | Listing last seen at date |  [optional] |
|**sellerType** | **String** | Seller type for the car |  [optional] |
|**source** | **String** | Source domain of the listing |  [optional] |
|**stockNo** | **String** | Stock number of car in dealers inventory |  [optional] |
|**vdpUrl** | **String** | Vehicle Details Page url of the specific car |  [optional] |
|**vehicleRegistrationMark** | **String** |  Vehicle Registration Mark of the car |  [optional] |
|**vin** | **String** | VIN for the car |  [optional] |



