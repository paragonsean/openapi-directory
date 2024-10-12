# CoreApiV2.Article

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authors** | **[String]** | List of article authors | [optional] 
**citations** | [**[Citation]**](Citation.md) | Citations found in the article | [optional] 
**contributors** | **[String]** | List of article contributors | [optional] 
**datePublished** | **String** | Date article published | [optional] 
**description** | **String** | The abstract | [optional] 
**doi** | **String** | The DOI of the article | [optional] 
**downloadUrl** | **String** | The download PDF URL which is displayed on our /display/[ArticleID] page | [optional] 
**fulltext** | **String** | Article full text | [optional] 
**fulltextIdentifier** | **String** | The URL to the fulltext | [optional] 
**fulltextUrls** | **[String]** | URLs of the fulltext version of this article | [optional] 
**id** | **Number** | Article ID | 
**identifiers** | **[String]** | List of document identifiers | [optional] 
**journals** | [**[ArticleJournal]**](ArticleJournal.md) | List of journals this article belongs to | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 
**oai** | **String** | The OAI of the article | [optional] 
**publisher** | **String** | Publisher of the article | [optional] 
**rawRecordXml** | [**RawRecordXml**](RawRecordXml.md) |  | [optional] 
**relations** | **[String]** | URLs of relating articles, etc. | [optional] 
**repositories** | [**[Repository]**](Repository.md) | List of repositories this article belongs to | [optional] 
**repositoryDocument** | **Object** |  | [optional] 
**similarities** | [**[Similar]**](Similar.md) | Similar articles | [optional] 
**subjects** | **[String]** | Article subjects | [optional] 
**title** | **String** | Article title | [optional] 
**topics** | **[String]** | Article topics | [optional] 
**types** | **[String]** | Types, e.g. conference paper, journal paper, etc. | [optional] 
**year** | **Number** | Year the article was published | [optional] 


