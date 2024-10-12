# FigshareApi.ProjectCompletePrivate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **Number** | ID of the account owning the project | 
**collaborators** | [**[Collaborator]**](Collaborator.md) | List of project collaborators | 
**createdDate** | **String** | Date when project was created | 
**customFields** | [**[CustomArticleField]**](CustomArticleField.md) | Collection custom fields | 
**description** | **String** | Project description | 
**figshareUrl** | **String** | Project public url | 
**funding** | **String** | Project funding | 
**fundingList** | [**[FundingInformation]**](FundingInformation.md) | Full Project funding information | 
**groupId** | **Number** | Group of project if any | 
**modifiedDate** | **String** | Date when project was last modified | 
**quota** | **Number** | Project quota | 
**usedQuota** | **Number** | Project used quota | 
**usedQuotaPrivate** | **Number** | Project private quota used | 
**usedQuotaPublic** | **Number** | Project public quota used | 
**role** | **String** | Role inside this project | 
**storage** | **String** | Project storage type | 
**id** | **Number** | Project id | 
**publishedDate** | **String** | Date when project was published | 
**title** | **String** | Project title | 
**url** | **String** | Api endpoint | 



## Enum: RoleEnum


* `Owner` (value: `"Owner"`)

* `Collaborator` (value: `"Collaborator"`)

* `Viewer` (value: `"Viewer"`)





## Enum: StorageEnum


* `individual` (value: `"individual"`)

* `group` (value: `"group"`)




