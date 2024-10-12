# FigshareApi.CollectionUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**articles** | **[Number]** | List of articles to be associated with the collection | [optional] 
**authors** | **[Object]** | List of authors to be associated with the collection. The list can contain the following fields: id, name, first_name, last_name, email, orcid_id. If an id is supplied, it will take priority and everything else will be ignored. No more than 10 authors. For adding more authors use the specific authors endpoint. | [optional] 
**categories** | **[Number]** | List of category ids to be associated with the collection (e.g [1, 23, 33, 66]) | [optional] 
**categoriesBySourceId** | **[String]** | List of category source ids to be associated with the article, supersedes the categories property | [optional] 
**customFields** | **Object** | List of key, values pairs to be associated with the collection | [optional] 
**customFieldsList** | [**[CustomArticleFieldAdd]**](CustomArticleFieldAdd.md) | List of custom fields values, supersedes custom_fields parameter | [optional] 
**description** | **String** | The collection description. In a publisher case, usually this is the remote collection description | [optional] [default to &#39;&#39;]
**doi** | **String** | Not applicable for regular users. In an institutional case, make sure your group supports setting DOIs. This setting is applied by figshare via opening a ticket through our support/helpdesk system. | [optional] [default to &#39;&#39;]
**funding** | **String** | Grant number or funding authority | [optional] [default to &#39;&#39;]
**fundingList** | [**[FundingCreate]**](FundingCreate.md) | Funding creation / update items | [optional] 
**groupId** | **Number** | Not applicable to regular users. This field is reserved to institutions/publishers with access to assign to specific groups | [optional] 
**handle** | **String** | Not applicable for regular users. In an institutional case, make sure your group supports setting Handles. This setting is applied by figshare via opening a ticket through our support/helpdesk system. | [optional] [default to &#39;&#39;]
**keywords** | **[String]** | List of tags to be associated with the collection. Tags can be used instead | [optional] 
**references** | **[String]** | List of links to be associated with the collection (e.g [\&quot;http://link1\&quot;, \&quot;http://link2\&quot;, \&quot;http://link3\&quot;]) | [optional] 
**resourceDoi** | **String** | Not applicable to regular users. In a publisher case, this is the publisher article DOI. | [optional] [default to &#39;&#39;]
**resourceId** | **String** | Not applicable to regular users. In a publisher case, this is the publisher article id | [optional] 
**resourceLink** | **String** | Not applicable to regular users. In a publisher case, this is the publisher article link | [optional] 
**resourceTitle** | **String** | Not applicable to regular users. In a publisher case, this is the publisher article title. | [optional] [default to &#39;&#39;]
**resourceVersion** | **Number** | Not applicable to regular users. In a publisher case, this is the publisher article version | [optional] 
**tags** | **[String]** | List of tags to be associated with the collection. Keywords can be used instead | [optional] 
**timeline** | [**TimelineUpdate**](TimelineUpdate.md) |  | [optional] 
**title** | **String** | Title of collection | [optional] 


