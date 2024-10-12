

# Listing

RETS MLS Listing Property

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**StreetAddress**](StreetAddress.md) |  |  [optional] |
|**agent** | [**Agent**](Agent.md) |  |  [optional] |
|**association** | [**Association**](Association.md) |  |  [optional] |
|**coAgent** | [**Agent**](Agent.md) |  |  [optional] |
|**disclaimer** | **String** | Data accuracy disclaimer. The value in the disclaimer may change depending on your MLS vendors rules.  |  [optional] |
|**geo** | [**GeographicData**](GeographicData.md) |  |  [optional] |
|**leaseTerm** | **String** | Represents the length of the lease. |  [optional] |
|**leaseType** | **String** | Information about the status of the existing lease on the property. |  [optional] |
|**listDate** | **OffsetDateTime** | Date and time the listing became Active |  [optional] |
|**listPrice** | **Double** | Price of the listing |  [optional] |
|**listingId** | **String** | Data Dictionary v1.3 ListingId. The well known identifier for the listing. The value is the id or number by the MLS as a public identifier for the listing.  This identifier should not be confused with the &#x60;mlsId&#x60;, which is specific to the SimplyRETS API.  |  [optional] |
|**mls** | [**MlsInformation**](MlsInformation.md) |  |  [optional] |
|**mlsId** | **Long** | A unique identifier for this listing specific to the SimplyRETS API. Thie identifier is specific to the SimplyRETS api and has no correlation with the MLS number. Use this id when making requests to the single listing endpoint (eg, &#x60;/properties/{mlsId}&#x60;).  Applications should not rely on specific &#x60;mlsId&#x60;s being present. Instead, apps should dynamically use the &#x60;mlsId&#x60; after using other more general query parameters. Many mls vendors require listings which are expired, terminated or sold to be purged, which will render calls to specific &#x60;mlsId&#x60;s to return nothing (or possibly a 404).  |  [optional] |
|**modified** | **OffsetDateTime** | Date and time of the last modification |  [optional] |
|**office** | [**Office**](Office.md) |  |  [optional] |
|**photos** | **List&lt;String&gt;** | Photos of the property. Images are served over https and are suitable for production use on secure websites  |  [optional] |
|**privateRemarks** | **String** | Agent only remarks |  [optional] |
|**property** | [**Property**](Property.md) |  |  [optional] |
|**remarks** | **String** | Description or remarks |  [optional] |
|**sales** | [**Sales**](Sales.md) |  |  [optional] |
|**school** | [**School**](School.md) |  |  [optional] |
|**showingInstructions** | **String** | Public instructions for showing the property. |  [optional] |
|**tax** | [**Tax**](Tax.md) |  |  [optional] |
|**virtualTourUrl** | **String** | The URL for an unbranded virtual tour of the property.  **Added on 2016/05/04 - Not available for all RETS vendors**  |  [optional] |



