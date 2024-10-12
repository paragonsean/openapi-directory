

# BlogArticle


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**announcementType** | [**AnnouncementTypeEnum**](#AnnouncementTypeEnum) |  |  [optional] |
|**author** | **String** |  |  [optional] |
|**content** | **String** | Article content |  [optional] |
|**createdAt** | **OffsetDateTime** | the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z |  [optional] |
|**excerpt** | **String** | Article excerpt |  [optional] |
|**id** | **Long** |  |  [optional] |
|**language** | **String** | language code |  [optional] |
|**links** | [**BlogArticleLinks**](BlogArticleLinks.md) |  |  [optional] |
|**slug** | **String** |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**topic** | **String** |  |  [optional] |



## Enum: AnnouncementTypeEnum

| Name | Value |
|---- | -----|
| ARTICLE | &quot;article&quot; |
| CASE | &quot;case&quot; |
| FAMOUS_TRANSLATORS | &quot;famous-translators&quot; |
| SALES | &quot;sales&quot; |



