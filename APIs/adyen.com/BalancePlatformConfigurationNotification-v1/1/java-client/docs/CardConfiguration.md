

# CardConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activation** | **String** | Overrides the activation label design ID defined in the &#x60;configurationProfileId&#x60;. The activation label is attached to the card and contains the activation instructions. |  [optional] |
|**activationUrl** | **String** | Your app&#39;s URL, if you want to activate cards through your app. For example, **my-app://ref1236a7d**. A QR code is created based on this URL, and is included in the carrier. Before you use this field, reach out to your Adyen contact to set up the QR code process.   Maximum length: 255 characters. |  [optional] |
|**bulkAddress** | [**BulkAddress**](BulkAddress.md) | Overrides the shipment bulk address defined in the &#x60;configurationProfileId&#x60;. |  [optional] |
|**cardImageId** | **String** | The ID of the card image. This is the image that will be printed on the full front of the card. |  [optional] |
|**carrier** | **String** | Overrides the carrier design ID defined in the &#x60;configurationProfileId&#x60;. The carrier is the letter or packaging to which the card is attached. |  [optional] |
|**carrierImageId** | **String** | The ID of the carrier image. This is the image that will printed on the letter to which the card is attached. |  [optional] |
|**configurationProfileId** | **String** | The ID of the card configuration profile that contains the settings of the card. For example, the envelope and PIN mailer designs or the logistics company handling the shipment. All the settings in the profile are applied to the card, unless you provide other fields to override them.  For example, send the &#x60;shipmentMethod&#x60; to override the logistics company defined in the card configuration profile. |  |
|**currency** | **String** | The three-letter [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217) currency code of the card. For example, **EUR**. |  [optional] |
|**envelope** | **String** | Overrides the envelope design ID defined in the &#x60;configurationProfileId&#x60;.  |  [optional] |
|**insert** | **String** | Overrides the insert design ID defined in the &#x60;configurationProfileId&#x60;. An insert is any additional material, such as marketing materials, that are shipped together with the card. |  [optional] |
|**language** | **String** | The two-letter [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code of the card. For example, **en**. |  [optional] |
|**logoImageId** | **String** | The ID of the logo image. This is the image that will be printed on the partial front of the card, such as a logo on the upper right corner. |  [optional] |
|**pinMailer** | **String** | Overrides the PIN mailer design ID defined in the &#x60;configurationProfileId&#x60;. The PIN mailer is the letter on which the PIN is printed. |  [optional] |
|**shipmentMethod** | **String** | Overrides the logistics company defined in the &#x60;configurationProfileId&#x60;. |  [optional] |



