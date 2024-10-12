

# Article

A single article

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationDate** | **OffsetDateTime** | timestamp the article was available in the Zalando webshop |  |
|**additionalInfos** | **List&lt;String&gt;** | any additional information of the article  |  |
|**ageGroups** | [**List&lt;AgeGroupsEnum&gt;**](#List&lt;AgeGroupsEnum&gt;) | age group of the article belongs to |  |
|**attributes** | [**List&lt;ArticleAttribute&gt;**](ArticleAttribute.md) | article attributes |  |
|**available** | **Boolean** | will be true if at least one article unit is available |  |
|**brand** | [**Brand**](Brand.md) |  |  |
|**categoryKeys** | **List&lt;String&gt;** | category keys of the article belongs to |  |
|**color** | **String** | the main color of the article |  |
|**genders** | [**List&lt;GendersEnum&gt;**](#List&lt;GendersEnum&gt;) | gender of the article belongs to |  |
|**id** | **String** | unique article id |  |
|**media** | [**ArticleMedia**](ArticleMedia.md) |  |  |
|**modelId** | **String** | unique article model id |  |
|**name** | **String** | article name |  |
|**season** | [**SeasonEnum**](#SeasonEnum) | collection season the article belongs to |  |
|**seasonYear** | **String** | collection year the article belongs to. Could be either a year or &#39;ALL&#39; |  |
|**shopUrl** | **URI** | url of the article within the Zalando webshop |  |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**units** | [**List&lt;ArticleUnit&gt;**](ArticleUnit.md) | price of the article |  |



## Enum: List&lt;AgeGroupsEnum&gt;

| Name | Value |
|---- | -----|
| BABY | &quot;BABY&quot; |
| CHILD | &quot;CHILD&quot; |
| TEEN | &quot;TEEN&quot; |
| ADULT | &quot;ADULT&quot; |



## Enum: List&lt;GendersEnum&gt;

| Name | Value |
|---- | -----|
| MALE | &quot;MALE&quot; |
| FEMALE | &quot;FEMALE&quot; |



## Enum: SeasonEnum

| Name | Value |
|---- | -----|
| SUMMER | &quot;SUMMER&quot; |
| WINTER | &quot;WINTER&quot; |
| ALL | &quot;ALL&quot; |



