

# HistoricalListing

Represents a car history entry

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carfax1Owner** | **Boolean** | Flag to indicate whether listing is carfax_1_owner |  [optional] |
|**carfaxCleanTitle** | **Boolean** | Flag to indicate whether listing is carfax_clean_title |  [optional] |
|**city** | **String** | City of the listing |  [optional] |
|**dataSource** | **String** | Data source of the listing |  [optional] |
|**dealerId** | **Integer** | Unique MC assigned dealers id for the listing |  [optional] |
|**dom** | **Integer** | Days on Market value for the car based on current and historical listings found in the Marketcheck database for this car |  [optional] |
|**dom180** | **Integer** | Days on Market value for the car based on current and last 6 month listings found in the Marketcheck database for this car |  [optional] |
|**domActive** | **Integer** | Days on Market value for the car based on current and last 30 days listings found in the Marketcheck database for this car |  [optional] |
|**exteriorColor** | **String** | Exterior color of the car |  [optional] |
|**financingOptions** | [**List&lt;ListingFinance&gt;**](ListingFinance.md) | Array of all finance offers for this listing |  [optional] |
|**firstSeenAt** | **Integer** | Listing first seen at first scraped timestamp |  [optional] |
|**firstSeenAtDate** | **String** | Listing first seen at first scraped date |  [optional] |
|**heading** | **String** | Listing title as displayed on the source website |  [optional] |
|**id** | **String** | Unique identifier representing a specific listing from the Marketcheck database |  [optional] |
|**interiorColor** | **String** | Interior color of the car |  [optional] |
|**inventoryType** | **String** | Inventory type of car |  [optional] |
|**isCertified** | **Integer** | Certified car |  [optional] |
|**isSearchable** | **String** | Flag to indicate listing is marked searchable or not |  [optional] |
|**lastSeenAt** | **Integer** | Listing last seen at (most recent) timestamp |  [optional] |
|**lastSeenAtDate** | **String** | Listing last seen at (most recent) date |  [optional] |
|**latitude** | **String** | Latitude of the listing |  [optional] |
|**leasingOptions** | [**List&lt;ListingLease&gt;**](ListingLease.md) | Array of all finance offers for this listing |  [optional] |
|**longitude** | **String** | Longitude of the listing |  [optional] |
|**miles** | **Integer** | Odometer reading / reported miles usage for the car |  [optional] |
|**msrp** | **Integer** | MSRP for the car |  [optional] |
|**price** | **Integer** | Asking price for the car |  [optional] |
|**refMiles** | **String** | Last Odometer reading / reported miles usage for the car. If the asking miles value is not or is available then the last_miles could perhaps be used. last_miles is the miles for the car listed on the source website as of last_miles_dt date |  [optional] |
|**refMilesDt** | **Integer** | The date at which the last miles was reported online. This is earlier to last_seen_date |  [optional] |
|**refPrice** | **String** | Last reported price for the car. If the asking price value is not or is available then the last_price could perhaps be used. last_price is the price for the car listed on the source website as of last_price_dt date |  [optional] |
|**refPriceDt** | **Integer** | The date at which the last price was reported online. This is earlier to last_seen_date |  [optional] |
|**scrapedAt** | **Integer** | Listing last seen at date timestamp |  [optional] |
|**scrapedAtDate** | **String** | Listing last seen at date |  [optional] |
|**sellerName** | **String** | Seller name of the listing from the Marketcheck database |  [optional] |
|**sellerNameO** | **String** | Seller name of the listing from the Marketcheck database |  [optional] |
|**sellerType** | **String** | Seller type for the car |  [optional] |
|**source** | **String** | Source domain of the listing |  [optional] |
|**state** | **String** | State of the listing |  [optional] |
|**statusDate** | **Integer** | Timestamp of status date |  [optional] |
|**stockNo** | **String** | Stock number of car in dealers inventory |  [optional] |
|**street** | **String** | Street of the listing |  [optional] |
|**trimR** | **String** | Trim of the car |  [optional] |
|**vdpUrl** | **String** | Vehicle Details Page url of the specific car |  [optional] |
|**vin** | **String** | VIN for the car |  [optional] |
|**zip** | **String** | Zip of the listing |  [optional] |



