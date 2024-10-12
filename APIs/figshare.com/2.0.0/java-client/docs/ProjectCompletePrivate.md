

# ProjectCompletePrivate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **Long** | ID of the account owning the project |  |
|**collaborators** | [**List&lt;Collaborator&gt;**](Collaborator.md) | List of project collaborators |  |
|**createdDate** | **String** | Date when project was created |  |
|**customFields** | [**List&lt;CustomArticleField&gt;**](CustomArticleField.md) | Collection custom fields |  |
|**description** | **String** | Project description |  |
|**figshareUrl** | **String** | Project public url |  |
|**funding** | **String** | Project funding |  |
|**fundingList** | [**List&lt;FundingInformation&gt;**](FundingInformation.md) | Full Project funding information |  |
|**groupId** | **Long** | Group of project if any |  |
|**modifiedDate** | **String** | Date when project was last modified |  |
|**quota** | **Long** | Project quota |  |
|**usedQuota** | **Long** | Project used quota |  |
|**usedQuotaPrivate** | **Long** | Project private quota used |  |
|**usedQuotaPublic** | **Long** | Project public quota used |  |
|**role** | [**RoleEnum**](#RoleEnum) | Role inside this project |  |
|**storage** | [**StorageEnum**](#StorageEnum) | Project storage type |  |
|**id** | **Long** | Project id |  |
|**publishedDate** | **String** | Date when project was published |  |
|**title** | **String** | Project title |  |
|**url** | **String** | Api endpoint |  |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| OWNER | &quot;Owner&quot; |
| COLLABORATOR | &quot;Collaborator&quot; |
| VIEWER | &quot;Viewer&quot; |



## Enum: StorageEnum

| Name | Value |
|---- | -----|
| INDIVIDUAL | &quot;individual&quot; |
| GROUP | &quot;group&quot; |



