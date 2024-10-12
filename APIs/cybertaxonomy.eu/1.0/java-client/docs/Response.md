

# Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checklist** | **String** |  |  [optional] |
|**checklistCitation** | **String** |  |  [optional] |
|**checklistId** | **String** |  |  [optional] |
|**checklistUrl** | **String** |  |  [optional] |
|**checklistVersion** | **String** |  |  [optional] |
|**matchingNameString** | **String** | Refers to the name string of the accepted taxon, synonym or otherName which was matching the query string |  [optional] |
|**matchingNameType** | [**MatchingNameTypeEnum**](#MatchingNameTypeEnum) | Reports which of the names was matching the query string:  &#39;taxon&#39;, &#39;synonym&#39;, &#39;vernacularName&#39;, or &#39;otherName&#39; |  [optional] |
|**otherNames** | [**List&lt;OtherNames&gt;**](OtherNames.md) |  |  [optional] |
|**synonyms** | [**List&lt;Synonym&gt;**](Synonym.md) | The list synonyms related to the accepted taxon |  [optional] |
|**taxon** | [**Taxon**](Taxon.md) |  |  [optional] |
|**vernacularNames** | **List&lt;String&gt;** | A common or vernacular name. |  [optional] |



## Enum: MatchingNameTypeEnum

| Name | Value |
|---- | -----|
| TAXON | &quot;TAXON&quot; |
| SYNONYM | &quot;SYNONYM&quot; |
| VERNACULAR_NAME | &quot;VERNACULAR_NAME&quot; |
| OTHER_NAME | &quot;OTHER_NAME&quot; |



