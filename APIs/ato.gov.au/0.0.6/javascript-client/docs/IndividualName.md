# BusinessRegistries.IndividualName

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **String** | The direction used to render the individual&#39;s name. | [optional] [default to &#39;left-to-right&#39;]
**familyName** | **String** | The individual&#39;s family name. | [optional] 
**formalSalutation** | **String** | The individual&#39;s formal salutation, for example, \&quot;Mr William Smith\&quot;. | [optional] 
**fromDate** | **Date** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 
**givenName** | **String** | The individual&#39;s given name. | [optional] 
**id** | **String** | The resource&#39;s unique identifier. | [optional] [readonly] 
**informalSalutation** | **String** | The individual&#39;s informal salutation, for example, \&quot;Bill\&quot;. | [optional] 
**middleName** | **String** | The individual&#39;s middle name. | [optional] 
**namePrefix** | **String** | The individual&#39;s name prefix. | [optional] [default to &#39;Mr&#39;]
**nameSuffix** | **String** | The individual&#39;s name suffix, for example, \&quot;Jr\&quot; or \&quot;Sr\&quot;. | [optional] 
**nameType** | **String** | The name type. | [optional] [default to &#39;Principal Name&#39;]
**toDate** | **Date** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 



## Enum: DirectionEnum


* `left-to-right` (value: `"left-to-right"`)

* `right-to-left` (value: `"right-to-left"`)





## Enum: NamePrefixEnum


* `Mr` (value: `"Mr"`)

* `Ms` (value: `"Ms"`)





## Enum: NameTypeEnum


* `Alias` (value: `"Alias"`)

* `Principal Name` (value: `"Principal Name"`)




