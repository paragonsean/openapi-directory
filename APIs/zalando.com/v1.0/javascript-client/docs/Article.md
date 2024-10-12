# ZalandoShop.Article

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationDate** | **Date** | timestamp the article was available in the Zalando webshop | 
**additionalInfos** | **[String]** | any additional information of the article  | 
**ageGroups** | **[String]** | age group of the article belongs to | 
**attributes** | [**[ArticleAttribute]**](ArticleAttribute.md) | article attributes | 
**available** | **Boolean** | will be true if at least one article unit is available | 
**brand** | [**Brand**](Brand.md) |  | 
**categoryKeys** | **[String]** | category keys of the article belongs to | 
**color** | **String** | the main color of the article | 
**genders** | **[String]** | gender of the article belongs to | 
**id** | **String** | unique article id | 
**media** | [**ArticleMedia**](ArticleMedia.md) |  | 
**modelId** | **String** | unique article model id | 
**name** | **String** | article name | 
**season** | **String** | collection season the article belongs to | 
**seasonYear** | **String** | collection year the article belongs to. Could be either a year or &#39;ALL&#39; | 
**shopUrl** | **String** | url of the article within the Zalando webshop | 
**tags** | **[String]** |  | [optional] 
**units** | [**[ArticleUnit]**](ArticleUnit.md) | price of the article | 



## Enum: [AgeGroupsEnum]


* `BABY` (value: `"BABY"`)

* `CHILD` (value: `"CHILD"`)

* `TEEN` (value: `"TEEN"`)

* `ADULT` (value: `"ADULT"`)





## Enum: [GendersEnum]


* `MALE` (value: `"MALE"`)

* `FEMALE` (value: `"FEMALE"`)





## Enum: SeasonEnum


* `SUMMER` (value: `"SUMMER"`)

* `WINTER` (value: `"WINTER"`)

* `ALL` (value: `"ALL"`)




