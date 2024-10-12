

# CreateAnEntityParametersTrust

Details of the trust entity to create. Required if `structure` is equal to `trust`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**CreateAnEntityParametersTrustAddress**](CreateAnEntityParametersTrustAddress.md) |  |  |
|**category** | [**CategoryEnum**](#CategoryEnum) | Whether the trust is &#x60;revocable&#x60; or &#x60;irrevocable&#x60;. Irrevocable trusts require their own Employer Identification Number. Revocable trusts require information about the individual &#x60;grantor&#x60; who created the trust. |  |
|**formationDocumentFileId** | **String** | The identifier of the File containing the formation document of the trust. |  [optional] |
|**formationState** | **String** | The two-letter United States Postal Service (USPS) abbreviation for the state in which the trust was formed. |  [optional] |
|**grantor** | [**CreateAnEntityParametersTrustGrantor**](CreateAnEntityParametersTrustGrantor.md) |  |  [optional] |
|**name** | **String** | The legal name of the trust. |  |
|**taxIdentifier** | **String** | The Employer Identification Number (EIN) for the trust. Required if &#x60;category&#x60; is equal to &#x60;irrevocable&#x60;. |  [optional] |
|**trustees** | [**List&lt;CreateAnEntityParametersTrustTrusteesInner&gt;**](CreateAnEntityParametersTrustTrusteesInner.md) | The trustees of the trust. |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| REVOCABLE | &quot;revocable&quot; |
| IRREVOCABLE | &quot;irrevocable&quot; |



