# FigshareApi.ArticleEmbargo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embargoDate** | **String** | Date when embargo lifts | 
**embargoOptions** | **[Object]** | List of embargo permissions that are associated with the article. If the type is logged_in and the group_ids list is empty, then the whole institution can see the article; if there are multiple group_ids, then only users that are under those groups can see the article. | 
**embargoReason** | **String** | Reason for embargo | 
**embargoTitle** | **String** | Title for embargo | 
**embargoType** | **String** | Embargo type | 
**isEmbargoed** | **Boolean** | True if embargoed | 


