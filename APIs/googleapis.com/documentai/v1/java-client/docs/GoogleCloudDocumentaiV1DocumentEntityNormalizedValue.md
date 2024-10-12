

# GoogleCloudDocumentaiV1DocumentEntityNormalizedValue

Parsed and normalized entity value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressValue** | [**GoogleTypePostalAddress**](GoogleTypePostalAddress.md) |  |  [optional] |
|**booleanValue** | **Boolean** | Boolean value. Can be used for entities with binary values, or for checkboxes. |  [optional] |
|**dateValue** | [**GoogleTypeDate**](GoogleTypeDate.md) |  |  [optional] |
|**datetimeValue** | [**GoogleTypeDateTime**](GoogleTypeDateTime.md) |  |  [optional] |
|**floatValue** | **Float** | Float value. |  [optional] |
|**integerValue** | **Integer** | Integer value. |  [optional] |
|**moneyValue** | [**GoogleTypeMoney**](GoogleTypeMoney.md) |  |  [optional] |
|**text** | **String** | Optional. An optional field to store a normalized string. For some entity types, one of respective &#x60;structured_value&#x60; fields may also be populated. Also not all the types of &#x60;structured_value&#x60; will be normalized. For example, some processors may not generate &#x60;float&#x60; or &#x60;integer&#x60; normalized text by default. Below are sample formats mapped to structured values. - Money/Currency type (&#x60;money_value&#x60;) is in the ISO 4217 text format. - Date type (&#x60;date_value&#x60;) is in the ISO 8601 text format. - Datetime type (&#x60;datetime_value&#x60;) is in the ISO 8601 text format. |  [optional] |



