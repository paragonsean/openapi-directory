

# Trust

Details of the trust entity. Will be present if `structure` is equal to `trust`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address2**](Address2.md) |  |  |
|**category** | [**CategoryEnum**](#CategoryEnum) | Whether the trust is &#x60;revocable&#x60; or &#x60;irrevocable&#x60;. |  |
|**formationDocumentFileId** | **String** | The ID for the File containing the formation document of the trust. |  |
|**formationState** | **String** | The two-letter United States Postal Service (USPS) abbreviation for the state in which the trust was formed. |  |
|**grantor** | [**Individual3**](Individual3.md) |  |  |
|**name** | **String** | The trust&#39;s name |  |
|**taxIdentifier** | **String** | The Employer Identification Number (EIN) of the trust itself. |  |
|**trustees** | [**List&lt;TrusteesElement&gt;**](TrusteesElement.md) | The trustees of the trust. |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| REVOCABLE | &quot;revocable&quot; |
| IRREVOCABLE | &quot;irrevocable&quot; |



