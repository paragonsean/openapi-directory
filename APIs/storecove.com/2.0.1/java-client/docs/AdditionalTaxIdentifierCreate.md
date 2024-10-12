

# AdditionalTaxIdentifierCreate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** | The ISO3166 country code to use this identifier for in case of consumerTaxMode. |  |
|**county** | **String** | The county/state inside the country code to use this identifier for in case of consumerTaxMode. Leave empty to create an additional tax identifier for the entire country. For India, use the two last characters of ISO 3166-2:IN (https://en.wikipedia.org/wiki/States_and_union_territories_of_India). |  [optional] |
|**identifier** | **String** | The identifier. |  |
|**scheme** | **String** | The scheme of the identifier. |  |
|**superscheme** | **String** | The superscheme of the identifier. Should always be \&quot;iso6523-actorid-upis\&quot;. |  |
|**thirdPartyPassword** | **String** | The password to use to authenticate to a system through which to send the document, or to obtain tax authority approval to send it. This field is currently relevant only for India and mandatory when creating an IN tax identifier. |  [optional] |
|**thirdPartyUsername** | **String** | The username to use to authenticate to a system through which to send the document, or to obtain tax authority approval to send it. This field is currently relevant only for India and mandatory when creating an IN tax identifier. |  [optional] |



