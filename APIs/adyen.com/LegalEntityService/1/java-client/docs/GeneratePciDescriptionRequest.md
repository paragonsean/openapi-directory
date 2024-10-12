

# GeneratePciDescriptionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalSalesChannels** | [**List&lt;AdditionalSalesChannelsEnum&gt;**](#List&lt;AdditionalSalesChannelsEnum&gt;) | An array of additional sales channels to generate PCI questionnaires. Include the relevant sales channels if you need your user to sign PCI questionnaires. Not required if you [create stores](https://docs.adyen.com/marketplaces-and-platforms/additional-for-platform-setup/create-stores/) and [add payment methods](https://docs.adyen.com/marketplaces-and-platforms/payment-methods/) before you generate the questionnaires.  Possible values: *  **eCommerce** *  **pos** *  **ecomMoto** *  **posMoto**   |  [optional] |
|**language** | **String** | Sets the language of the PCI questionnaire. Its value is a two-character [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code, for example, **en**. |  [optional] |



## Enum: List&lt;AdditionalSalesChannelsEnum&gt;

| Name | Value |
|---- | -----|
| E_COMMERCE | &quot;eCommerce&quot; |
| ECOM_MOTO | &quot;ecomMoto&quot; |
| POS | &quot;pos&quot; |
| POS_MOTO | &quot;posMoto&quot; |



