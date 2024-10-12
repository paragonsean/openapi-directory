

# Location

A location. See the [help center article] (https://support.google.com/business/answer/3038177) for a detailed description of these fields, or the [category endpoint](/my-business/reference/rest/v4/categories) for a list of valid business categories.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adWordsLocationExtensions** | [**AdWordsLocationExtensions**](AdWordsLocationExtensions.md) |  |  [optional] |
|**categories** | [**Categories**](Categories.md) |  |  [optional] |
|**labels** | **List&lt;String&gt;** | Optional. A collection of free-form strings to allow you to tag your business. These labels are NOT user facing; only you can see them. Must be between 1-255 characters per label. |  [optional] |
|**languageCode** | **String** | Immutable. The language of the location. Set during creation and not updateable. |  [optional] |
|**latlng** | [**LatLng**](LatLng.md) |  |  [optional] |
|**metadata** | [**Metadata**](Metadata.md) |  |  [optional] |
|**moreHours** | [**List&lt;MoreHours&gt;**](MoreHours.md) | Optional. More hours for a business&#39;s different departments or specific customers. |  [optional] |
|**name** | **String** | Google identifier for this location in the form: &#x60;locations/{location_id}&#x60;. |  [optional] |
|**openInfo** | [**OpenInfo**](OpenInfo.md) |  |  [optional] |
|**phoneNumbers** | [**PhoneNumbers**](PhoneNumbers.md) |  |  [optional] |
|**profile** | [**Profile**](Profile.md) |  |  [optional] |
|**regularHours** | [**BusinessHours**](BusinessHours.md) |  |  [optional] |
|**relationshipData** | [**RelationshipData**](RelationshipData.md) |  |  [optional] |
|**serviceArea** | [**ServiceAreaBusiness**](ServiceAreaBusiness.md) |  |  [optional] |
|**serviceItems** | [**List&lt;ServiceItem&gt;**](ServiceItem.md) | Optional. List of services supported by merchants. A service can be haircut, install water heater, etc. Duplicated service items will be removed automatically. |  [optional] |
|**specialHours** | [**SpecialHours**](SpecialHours.md) |  |  [optional] |
|**storeCode** | **String** | Optional. External identifier for this location, which must be unique within a given account. This is a means of associating the location with your own records. |  [optional] |
|**storefrontAddress** | [**PostalAddress**](PostalAddress.md) |  |  [optional] |
|**title** | **String** | Required. Location name should reflect your business&#39;s real-world name, as used consistently on your storefront, website, and stationery, and as known to customers. Any additional information, when relevant, can be included in other fields of the resource (for example, &#x60;Address&#x60;, &#x60;Categories&#x60;). Don&#39;t add unnecessary information to your name (for example, prefer \&quot;Google\&quot; over \&quot;Google Inc. - Mountain View Corporate Headquarters\&quot;). Don&#39;t include marketing taglines, store codes, special characters, hours or closed/open status, phone numbers, website URLs, service/product information, location/address or directions, or containment information (for example, \&quot;Chase ATM in Duane Reade\&quot;). |  [optional] |
|**websiteUri** | **String** | Optional. A URL for this business. If possible, use a URL that represents this individual business location instead of a generic website/URL that represents all locations, or the brand. |  [optional] |



