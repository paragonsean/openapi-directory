

# KeywordTask


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyword** | **String** | keyword (search term) |  |
|**localizationCode** | [**LocalizationCodeEnum**](#LocalizationCodeEnum) | A code for the localization, which is a combination of country and language |  |
|**localizationZip** | **String** | option to localize the results per zip code |  [optional] |
|**searchEngine** | [**SearchEngineEnum**](#SearchEngineEnum) | google/bing/google_mobile |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | status of this task request. \&quot;ok\&quot; means we&#39;re working on collecting it. \&quot;invalid\&quot; means there was an error and it won&#39;t be collected |  [optional] |
|**taskId** | **String** | the assigned task id for this task. Should be used later in the serp-collect request |  [optional] |



## Enum: LocalizationCodeEnum

| Name | Value |
|---- | -----|
| US | &quot;us&quot; |
| UK | &quot;uk&quot; |
| AU | &quot;au&quot; |
| BR | &quot;br&quot; |
| BE_DUTCH | &quot;be_dutch&quot; |
| BE_FRENCH | &quot;be_french&quot; |
| CA | &quot;ca&quot; |
| DE | &quot;de&quot; |
| ES | &quot;es&quot; |
| IE | &quot;ie&quot; |
| IL | &quot;il&quot; |
| NL | &quot;nl&quot; |
| SG | &quot;sg&quot; |
| ZA | &quot;za&quot; |
| IT | &quot;it&quot; |
| IS | &quot;is&quot; |
| CH | &quot;ch&quot; |
| FR | &quot;fr&quot; |
| SE | &quot;se&quot; |
| AT | &quot;at&quot; |
| DK | &quot;dk&quot; |
| NZ | &quot;nz&quot; |
| GR | &quot;gr&quot; |
| IN | &quot;in&quot; |
| MS | &quot;ms&quot; |
| PL | &quot;pl&quot; |
| HK | &quot;hk&quot; |
| ID | &quot;id&quot; |
| RU | &quot;ru&quot; |
| AE | &quot;ae&quot; |
| FI | &quot;fi&quot; |
| PT | &quot;pt&quot; |
| MX | &quot;mx&quot; |
| TR | &quot;tr&quot; |
| CL | &quot;cl&quot; |
| JP | &quot;jp&quot; |
| AR | &quot;ar&quot; |



## Enum: SearchEngineEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |
| BING | &quot;bing&quot; |
| GOOGLE_MOBILE | &quot;google_mobile&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;ok&quot; |
| INVALID | &quot;invalid&quot; |



