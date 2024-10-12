

# IndividualName

The Individual Name resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**direction** | [**DirectionEnum**](#DirectionEnum) | The direction used to render the individual&#39;s name. |  [optional] |
|**familyName** | **String** | The individual&#39;s family name. |  [optional] |
|**formalSalutation** | **String** | The individual&#39;s formal salutation, for example, \&quot;Mr William Smith\&quot;. |  [optional] |
|**fromDate** | **OffsetDateTime** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |
|**givenName** | **String** | The individual&#39;s given name. |  [optional] |
|**id** | **String** | The resource&#39;s unique identifier. |  [optional] [readonly] |
|**informalSalutation** | **String** | The individual&#39;s informal salutation, for example, \&quot;Bill\&quot;. |  [optional] |
|**middleName** | **String** | The individual&#39;s middle name. |  [optional] |
|**namePrefix** | [**NamePrefixEnum**](#NamePrefixEnum) | The individual&#39;s name prefix. |  [optional] |
|**nameSuffix** | **String** | The individual&#39;s name suffix, for example, \&quot;Jr\&quot; or \&quot;Sr\&quot;. |  [optional] |
|**nameType** | [**NameTypeEnum**](#NameTypeEnum) | The name type. |  [optional] |
|**toDate** | **OffsetDateTime** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| LEFT_TO_RIGHT | &quot;left-to-right&quot; |
| RIGHT_TO_LEFT | &quot;right-to-left&quot; |



## Enum: NamePrefixEnum

| Name | Value |
|---- | -----|
| MR | &quot;Mr&quot; |
| MS | &quot;Ms&quot; |



## Enum: NameTypeEnum

| Name | Value |
|---- | -----|
| ALIAS | &quot;Alias&quot; |
| PRINCIPAL_NAME | &quot;Principal Name&quot; |



