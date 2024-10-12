

# RankCollectResponseTasksInnerTaskId

the id of the task you want to look for

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorMessage** | **String** | error message in case task status is invalid |  [optional] |
|**keyword** | **String** | keyword (search term) |  [optional] |
|**localPackRank** | **Integer** | relevent only to google: show the local pack rank of the domain in case exist |  [optional] |
|**localizationCode** | [**LocalizationCodeEnum**](#LocalizationCodeEnum) | A code for the localization, which is a combination of country and language |  [optional] |
|**localizationZip** | **String** | option to localize the results per zip code |  [optional] |
|**rank** | **Integer** | the exact rank of the domain in the search engine asked |  [optional] |
|**ready** | [**ReadyEnum**](#ReadyEnum) | task ready indicator |  [optional] |
|**searchEngine** | [**SearchEngineEnum**](#SearchEngineEnum) | google/bing/google_mobile |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | task status in terms of success |  [optional] |



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



## Enum: ReadyEnum

| Name | Value |
|---- | -----|
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |



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



