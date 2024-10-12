

# ListingsPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categories** | [**List&lt;ListingsPostRequestCategoriesInner&gt;**](ListingsPostRequestCategoriesInner.md) |  |  [optional] |
|**condition** | [**ListingsPostRequestCondition**](ListingsPostRequestCondition.md) |  |  [optional] |
|**description** | **String** | Product description. Please keep formatting to a minimum. |  [optional] |
|**exclusiveChannel** | [**ExclusiveChannelEnum**](#ExclusiveChannelEnum) | Currently for users of seller sites only, this allows you to have a listing available only to your seller site by setting this to &#39;seller_site&#39; |  [optional] |
|**finish** | **String** | Finish, e.g. &#39;Sunburst&#39; |  [optional] |
|**hasInventory** | **Boolean** | Set true if selling more than one |  [optional] |
|**inventory** | **Integer** | Number of items available for sale. Reverb will increment and decrement automatically. |  [optional] |
|**location** | [**ListingsPostRequestLocation**](ListingsPostRequestLocation.md) |  |  [optional] |
|**make** | **String** | ex: Fender, Gibson |  [optional] |
|**model** | **String** | ex: Stratocaster, SG |  [optional] |
|**multiItem** | **Boolean** | Specifies if the listing is a bundle of multiple individual items |  [optional] |
|**offersEnabled** | **Boolean** | Whether the listing accepts negotiated offers (default: true) |  [optional] |
|**originCountryCode** | **String** | Country of origin/manufacture, ISO code (e.g: US) |  [optional] |
|**photos** | **List&lt;String&gt;** | An array of image URLs. Ex: [&#39;http://my.site.com/image.jpg&#39;] |  [optional] |
|**preorderInfo** | [**ListingsPostRequestPreorderInfo**](ListingsPostRequestPreorderInfo.md) |  |  [optional] |
|**price** | [**ConversationsConversationIdOfferPostRequestPrice**](ConversationsConversationIdOfferPostRequestPrice.md) |  |  [optional] |
|**prop65Warning** | **String** | If your listing contains chemicals that are required to be reported under California Prop 65, please provide your warning statement. We will add the required &#39;Warning&#39; label and link to California&#39;s information page, so you only need to provide the body of the warning. For more information, see https://www.p65warnings.ca.gov/new-proposition-65-warnings |  [optional] |
|**publish** | **Boolean** | Publish your listing if draft |  [optional] |
|**seller** | [**ListingsPostRequestSeller**](ListingsPostRequestSeller.md) |  |  [optional] |
|**sellerCost** | **String** | Cost of goods in your currency as a POSIX-compliant decimal number (internal use only, not shown to buyers) |  [optional] |
|**shipping** | [**ListingsPostRequestShipping**](ListingsPostRequestShipping.md) |  |  [optional] |
|**shippingProfileId** | **String** | id of a shop&#39;s shipping profile |  [optional] |
|**shippingProfileName** | **String** | DEPRECATED, please use shipping_profile_id. Name of a shipping profile |  [optional] |
|**sku** | **String** | Unique identifier for product |  [optional] |
|**soldAsIs** | **Boolean** | This item is sold As-Is and cannot be returned |  [optional] |
|**storageLocation** | **String** | Internal note used by sellers to back reference their catalog system when entering a listing |  [optional] |
|**taxExempt** | **Boolean** | Listing is exempt from taxes / VAT |  [optional] |
|**title** | **String** | Title of your listing |  [optional] |
|**upc** | **String** | Valid UPC code |  [optional] |
|**upcDoesNotApply** | **Boolean** | True if a brand new product has no UPC code, ie for a handmade or custom item |  [optional] |
|**videos** | [**List&lt;ListingsPostRequestVideosInner&gt;**](ListingsPostRequestVideosInner.md) | List of YouTube video urls. Note: ONLY ONE ALLOWED |  [optional] |
|**year** | **String** | Supports many formats. Ex: 1979, mid-70s, late 90s |  [optional] |



## Enum: ExclusiveChannelEnum

| Name | Value |
|---- | -----|
| SELLER_SITE | &quot;seller_site&quot; |
| REVERB | &quot;reverb&quot; |
| NONE | &quot;none&quot; |



