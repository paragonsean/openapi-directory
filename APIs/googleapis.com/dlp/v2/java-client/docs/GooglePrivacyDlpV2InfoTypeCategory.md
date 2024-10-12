

# GooglePrivacyDlpV2InfoTypeCategory

Classification of infoTypes to organize them according to geographic location, industry, and data type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**industryCategory** | [**IndustryCategoryEnum**](#IndustryCategoryEnum) | The group of relevant businesses where this infoType is commonly used |  [optional] |
|**locationCategory** | [**LocationCategoryEnum**](#LocationCategoryEnum) | The region or country that issued the ID or document represented by the infoType. |  [optional] |
|**typeCategory** | [**TypeCategoryEnum**](#TypeCategoryEnum) | The class of identifiers where this infoType belongs |  [optional] |



## Enum: IndustryCategoryEnum

| Name | Value |
|---- | -----|
| INDUSTRY_UNSPECIFIED | &quot;INDUSTRY_UNSPECIFIED&quot; |
| FINANCE | &quot;FINANCE&quot; |
| HEALTH | &quot;HEALTH&quot; |
| TELECOMMUNICATIONS | &quot;TELECOMMUNICATIONS&quot; |



## Enum: LocationCategoryEnum

| Name | Value |
|---- | -----|
| LOCATION_UNSPECIFIED | &quot;LOCATION_UNSPECIFIED&quot; |
| GLOBAL | &quot;GLOBAL&quot; |
| ARGENTINA | &quot;ARGENTINA&quot; |
| AUSTRALIA | &quot;AUSTRALIA&quot; |
| BELGIUM | &quot;BELGIUM&quot; |
| BRAZIL | &quot;BRAZIL&quot; |
| CANADA | &quot;CANADA&quot; |
| CHILE | &quot;CHILE&quot; |
| CHINA | &quot;CHINA&quot; |
| COLOMBIA | &quot;COLOMBIA&quot; |
| CROATIA | &quot;CROATIA&quot; |
| DENMARK | &quot;DENMARK&quot; |
| FRANCE | &quot;FRANCE&quot; |
| FINLAND | &quot;FINLAND&quot; |
| GERMANY | &quot;GERMANY&quot; |
| HONG_KONG | &quot;HONG_KONG&quot; |
| INDIA | &quot;INDIA&quot; |
| INDONESIA | &quot;INDONESIA&quot; |
| IRELAND | &quot;IRELAND&quot; |
| ISRAEL | &quot;ISRAEL&quot; |
| ITALY | &quot;ITALY&quot; |
| JAPAN | &quot;JAPAN&quot; |
| KOREA | &quot;KOREA&quot; |
| MEXICO | &quot;MEXICO&quot; |
| THE_NETHERLANDS | &quot;THE_NETHERLANDS&quot; |
| NEW_ZEALAND | &quot;NEW_ZEALAND&quot; |
| NORWAY | &quot;NORWAY&quot; |
| PARAGUAY | &quot;PARAGUAY&quot; |
| PERU | &quot;PERU&quot; |
| POLAND | &quot;POLAND&quot; |
| PORTUGAL | &quot;PORTUGAL&quot; |
| SINGAPORE | &quot;SINGAPORE&quot; |
| SOUTH_AFRICA | &quot;SOUTH_AFRICA&quot; |
| SPAIN | &quot;SPAIN&quot; |
| SWEDEN | &quot;SWEDEN&quot; |
| SWITZERLAND | &quot;SWITZERLAND&quot; |
| TAIWAN | &quot;TAIWAN&quot; |
| THAILAND | &quot;THAILAND&quot; |
| TURKEY | &quot;TURKEY&quot; |
| UNITED_KINGDOM | &quot;UNITED_KINGDOM&quot; |
| UNITED_STATES | &quot;UNITED_STATES&quot; |
| URUGUAY | &quot;URUGUAY&quot; |
| VENEZUELA | &quot;VENEZUELA&quot; |
| INTERNAL | &quot;INTERNAL&quot; |



## Enum: TypeCategoryEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| PII | &quot;PII&quot; |
| SPII | &quot;SPII&quot; |
| DEMOGRAPHIC | &quot;DEMOGRAPHIC&quot; |
| CREDENTIAL | &quot;CREDENTIAL&quot; |
| GOVERNMENT_ID | &quot;GOVERNMENT_ID&quot; |
| DOCUMENT | &quot;DOCUMENT&quot; |
| CONTEXTUAL_INFORMATION | &quot;CONTEXTUAL_INFORMATION&quot; |



