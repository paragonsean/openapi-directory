

# PhoneNumber

A person's phone number.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canonicalForm** | **String** | Output only. The canonicalized [ITU-T E.164](https://law.resource.org/pub/us/cfr/ibr/004/itu-t.E.164.1.2008.pdf) form of the phone number. |  [optional] [readonly] |
|**formattedType** | **String** | Output only. The type of the phone number translated and formatted in the viewer&#39;s account locale or the &#x60;Accept-Language&#x60; HTTP header locale. |  [optional] [readonly] |
|**metadata** | [**FieldMetadata**](FieldMetadata.md) |  |  [optional] |
|**type** | **String** | The type of the phone number. The type can be custom or one of these predefined values: * &#x60;home&#x60; * &#x60;work&#x60; * &#x60;mobile&#x60; * &#x60;homeFax&#x60; * &#x60;workFax&#x60; * &#x60;otherFax&#x60; * &#x60;pager&#x60; * &#x60;workMobile&#x60; * &#x60;workPager&#x60; * &#x60;main&#x60; * &#x60;googleVoice&#x60; * &#x60;other&#x60; |  [optional] |
|**value** | **String** | The phone number. |  [optional] |



