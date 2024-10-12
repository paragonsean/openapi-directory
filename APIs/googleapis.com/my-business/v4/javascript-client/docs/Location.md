# GoogleMyBusinessApi.Location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adWordsLocationExtensions** | [**AdWordsLocationExtensions**](AdWordsLocationExtensions.md) |  | [optional] 
**additionalCategories** | [**[Category]**](Category.md) | Additional categories to describe your business. Categories help your customers find accurate, specific results for services they&#39;re interested in. To keep your business information accurate and live, make sure that you use as few categories as possible to describe your overall core business. Choose categories that are as specific as possible, but representative of your main business. | [optional] 
**additionalPhones** | **[String]** | Up to two phone numbers (mobile or landline, no fax) at which your business can be called, in addition to your primary phone number. | [optional] 
**address** | [**PostalAddress**](PostalAddress.md) |  | [optional] 
**attributes** | [**[Attribute]**](Attribute.md) | Attributes for this location. | [optional] 
**labels** | **[String]** | A collection of free-form strings to allow you to tag your business. These labels are NOT user facing; only you can see them. Limited to 255 characters (per label). | [optional] 
**languageCode** | **String** | The language of the location. Set during creation and not updateable. | [optional] 
**latlng** | [**LatLng**](LatLng.md) |  | [optional] 
**locationKey** | [**LocationKey**](LocationKey.md) |  | [optional] 
**locationName** | **String** | Location name should reflect your business&#39;s real-world name, as used consistently on your storefront, website, and stationery, and as known to customers. Any additional information, when relevant, can be included in other fields of the resource (for example, &#x60;Address&#x60;, &#x60;Categories&#x60;). Don&#39;t add unnecessary information to your name (for example, prefer \&quot;Google\&quot; over \&quot;Google Inc. - Mountain View Corporate Headquarters\&quot;). Don&#39;t include marketing taglines, store codes, special characters, hours or closed/open status, phone numbers, website URLs, service/product information, location/address or directions, or containment information (for example, \&quot;Chase ATM in Duane Reade\&quot;). | [optional] 
**locationState** | [**LocationState**](LocationState.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**moreHours** | [**[MoreHours]**](MoreHours.md) | More hours for a business&#39;s different departments or specific customers. | [optional] 
**name** | **String** | Google identifier for this location in the form: &#x60;accounts/{account_id}/locations/{location_id}&#x60; In the context of matches, this field will not be populated. | [optional] 
**openInfo** | [**OpenInfo**](OpenInfo.md) |  | [optional] 
**priceLists** | [**[PriceList]**](PriceList.md) | Price list information for this location. | [optional] 
**primaryCategory** | [**Category**](Category.md) |  | [optional] 
**primaryPhone** | **String** | A phone number that connects to your individual business location as directly as possible. Use a local phone number instead of a central, call center helpline number whenever possible. | [optional] 
**profile** | [**Profile**](Profile.md) |  | [optional] 
**regularHours** | [**BusinessHours**](BusinessHours.md) |  | [optional] 
**relationshipData** | [**RelationshipData**](RelationshipData.md) |  | [optional] 
**serviceArea** | [**ServiceAreaBusiness**](ServiceAreaBusiness.md) |  | [optional] 
**specialHours** | [**SpecialHours**](SpecialHours.md) |  | [optional] 
**storeCode** | **String** | External identifier for this location, which must be unique inside a given account. This is a means of associating the location with your own records. | [optional] 
**websiteUrl** | **String** | A URL for this business. If possible, use a URL that represents this individual business location instead of a generic website/URL that represents all locations, or the brand. | [optional] 


