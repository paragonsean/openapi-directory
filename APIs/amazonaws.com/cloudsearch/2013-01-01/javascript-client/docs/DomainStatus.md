# AmazonCloudSearch.DomainStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domainId** | **String** | An internally generated unique identifier for a domain. | 
**domainName** | **String** | A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen). | 
**ARN** | **String** | The Amazon Resource Name (ARN) of the search domain. See &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Identifiers for IAM Entities&lt;/a&gt; in &lt;i&gt;Using AWS Identity and Access Management&lt;/i&gt; for more information. | [optional] 
**created** | **Boolean** |  | [optional] 
**deleted** | **Boolean** |  | [optional] 
**docService** | [**DomainStatusDocService**](DomainStatusDocService.md) |  | [optional] 
**searchService** | [**DomainStatusSearchService**](DomainStatusSearchService.md) |  | [optional] 
**requiresIndexDocuments** | **Boolean** |  | 
**processing** | **Boolean** |  | [optional] 
**searchInstanceType** | **String** |  | [optional] 
**searchPartitionCount** | **Number** |  | [optional] 
**searchInstanceCount** | **Number** |  | [optional] 
**limits** | [**Limits**](Limits.md) |  | [optional] 


