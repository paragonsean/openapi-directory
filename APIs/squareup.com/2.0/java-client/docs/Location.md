

# Location



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address**](Address.md) |  |  [optional] |
|**businessEmail** | **String** | The email of the location. This email is visible to the customers of the location. For example, the email appears on customer receipts.  For example, &#x60;help&amp;#64;squareup.com&#x60;. |  [optional] |
|**businessHours** | [**BusinessHours**](BusinessHours.md) |  |  [optional] |
|**businessName** | **String** | The business name of the location This is the name visible to the customers of the location. For example, this name appears on customer receipts. |  [optional] |
|**capabilities** | **List&lt;String&gt;** | The Square features that are enabled for the location. See [LocationCapability](https://developer.squareup.com/reference/square_2021-08-18/enums/LocationCapability) for possible values. |  [optional] |
|**coordinates** | [**Coordinates**](Coordinates.md) |  |  [optional] |
|**country** | **String** | The country of the location, in ISO 3166-1-alpha-2 format.  See [Country](https://developer.squareup.com/reference/square_2021-08-18/enums/Country) for possible values. |  [optional] |
|**createdAt** | **String** | The time when the location was created, in RFC 3339 format. For more information, see [Working with Dates](https://developer.squareup.com/docs/build-basics/working-with-dates). |  [optional] |
|**currency** | **String** | The currency used for all transactions at this location, in ISO 4217 format. See [Currency](https://developer.squareup.com/reference/square_2021-08-18/enums/Currency) for possible values. |  [optional] |
|**description** | **String** | The description of the location. |  [optional] |
|**facebookUrl** | **String** | The Facebook profile URL of the location. The URL should begin with &#39;facebook.com/&#39;. For example, &#x60;https://www.facebook.com/square&#x60;. |  [optional] |
|**fullFormatLogoUrl** | **String** | The URL of a full-format logo image for the location. The Seller must choose this logo in the Seller dashboard (Receipts section) for the logo to appear on transactions (such as receipts, invoices) that Square generates on behalf of the Seller. This image can have an aspect ratio of 2:1 or greater and is recommended to be at least 1280x648 pixels. |  [optional] |
|**id** | **String** | The Square-issued ID of the location. |  [optional] |
|**instagramUsername** | **String** | The Instagram username of the location without the &#39;&amp;#64;&#39; symbol. For example, &#x60;square&#x60;. |  [optional] |
|**languageCode** | **String** | The language associated with the location, in [BCP 47 format](https://tools.ietf.org/html/bcp47#appendix-A).  For more information, see [Location language code](https://developer.squareup.com/docs/locations-api#location-language-code). |  [optional] |
|**logoUrl** | **String** | The URL of the logo image for the location. The Seller must choose this logo in the Seller dashboard (Receipts section) for the logo to appear on transactions (such as receipts, invoices) that Square generates on behalf of the Seller. This image should have an aspect ratio close to 1:1 and is recommended to be at least 200x200 pixels. |  [optional] |
|**mcc** | **String** | The merchant category code (MCC) of the location, as standardized by ISO 18245. The MCC describes the kind of goods or services sold at the location. |  [optional] |
|**merchantId** | **String** | The ID of the merchant that owns the location. |  [optional] |
|**name** | **String** | The name of the location. This information appears in the dashboard as the nickname. A location name must be unique within a seller account. |  [optional] |
|**phoneNumber** | **String** | The phone number of the location in human readable format. For example, &#x60;+353 80 0 098 8099&#x60;. |  [optional] |
|**posBackgroundUrl** | **String** | The URL of the Point of Sale background image for the location. |  [optional] |
|**status** | **String** | The status of the location, either active or inactive. |  [optional] |
|**taxIds** | [**TaxIds**](TaxIds.md) |  |  [optional] |
|**timezone** | **String** | The [IANA Timezone](https://www.iana.org/time-zones) identifier for the timezone of the location. |  [optional] |
|**twitterUsername** | **String** | The Twitter username of the location without the &#39;&amp;#64;&#39; symbol. For example, &#x60;Square&#x60;. |  [optional] |
|**type** | **String** | The type of the location, either physical or mobile. |  [optional] |
|**websiteUrl** | **String** | The website URL of the location.  For example, &#x60;https://squareup.com&#x60;. |  [optional] |



