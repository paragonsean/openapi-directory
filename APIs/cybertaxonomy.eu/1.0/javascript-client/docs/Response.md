# EuBonUtis.Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checklist** | **String** |  | [optional] 
**checklistCitation** | **String** |  | [optional] 
**checklistId** | **String** |  | [optional] 
**checklistUrl** | **String** |  | [optional] 
**checklistVersion** | **String** |  | [optional] 
**matchingNameString** | **String** | Refers to the name string of the accepted taxon, synonym or otherName which was matching the query string | [optional] 
**matchingNameType** | **String** | Reports which of the names was matching the query string:  &#39;taxon&#39;, &#39;synonym&#39;, &#39;vernacularName&#39;, or &#39;otherName&#39; | [optional] 
**otherNames** | [**[OtherNames]**](OtherNames.md) |  | [optional] 
**synonyms** | [**[Synonym]**](Synonym.md) | The list synonyms related to the accepted taxon | [optional] 
**taxon** | [**Taxon**](Taxon.md) |  | [optional] 
**vernacularNames** | **[String]** | A common or vernacular name. | [optional] 



## Enum: MatchingNameTypeEnum


* `TAXON` (value: `"TAXON"`)

* `SYNONYM` (value: `"SYNONYM"`)

* `VERNACULAR_NAME` (value: `"VERNACULAR_NAME"`)

* `OTHER_NAME` (value: `"OTHER_NAME"`)




