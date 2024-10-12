# DracoonApi.CharacterRules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mustContainCharacters** | **[String]** | Characters which a password must contain:  * &#x60;alpha&#x60; - at least one alphabetical character (&#x60;uppercase&#x60; OR &#x60;lowercase&#x60;)  * &#x60;uppercase&#x60; - at least one uppercase character  * &#x60;lowercase&#x60; - at least one lowercase character  * &#x60;numeric&#x60; - at least one numeric character  * &#x60;special&#x60; - at least one special character (letters and digits excluded)  * &#x60;all&#x60; - combination of &#x60;uppercase&#x60;, &#x60;lowercase&#x60;, &#x60;numeric&#x60; and &#x60;special&#x60; (available only in request models)  * &#x60;none&#x60; - none of the above | 
**numberOfCharacteristicsToEnforce** | **Number** | Number of characteristics to enforce  e.g. from &#x60;[\&quot;uppercase\&quot;, \&quot;lowercase\&quot;, \&quot;numeric\&quot;, \&quot;special\&quot;]&#x60;  all 4 character sets can be enforced; but also only 2 of them | 



## Enum: MustContainCharactersEnum


* `alpha` (value: `"alpha"`)

* `uppercase` (value: `"uppercase"`)

* `lowercase` (value: `"lowercase"`)

* `numeric` (value: `"numeric"`)

* `special` (value: `"special"`)

* `all` (value: `"all"`)

* `none` (value: `"none"`)




