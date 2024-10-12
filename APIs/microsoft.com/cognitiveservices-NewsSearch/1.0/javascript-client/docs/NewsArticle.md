# NewsSearchClient.NewsArticle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The news category that the article belongs to. For example, Sports. If the news category cannot be determined, the article does not include this field. | [optional] [readonly] 
**clusteredArticles** | [**[NewsArticle]**](NewsArticle.md) | A list of related news articles. | [optional] [readonly] 
**headline** | **Boolean** | A Boolean value that indicates whether the news article is a headline. If true, the article is a headline. The article includes this field only for news categories requests that do not specify the category query parameter. | [optional] [readonly] 


