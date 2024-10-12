

# Portfolio


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTime** | **String** | The time in ISO 8601 format when the portfolio was created. |  |
|**description** | **String** | The portfolio&#39;s description. |  |
|**link** | **String** | The link to the portfolio. |  |
|**metadata** | [**PortfolioMetadata**](PortfolioMetadata.md) |  |  |
|**modifiedTime** | **String** | The time in ISO 8601 format when the portfolio&#39;s data was last modified. |  |
|**name** | **String** | The display name of the portfolio. |  |
|**sort** | [**SortEnum**](#SortEnum) | The default video sort order for the portfolio:  Option descriptions:  * &#x60;alphabetical&#x60; - The default sort order is alphabetical by name.  * &#x60;clips&#x60; - The default sort order is video creation date.  * &#x60;modified&#x60; - The default sort order is the order in which the videos were modified.  * &#x60;recent&#x60; - The default sort order is the order in which the videos were added.  |  |
|**uri** | **String** | The canonical relative URI of the portfolio. |  |



## Enum: SortEnum

| Name | Value |
|---- | -----|
| ALPHABETICAL | &quot;alphabetical&quot; |
| CLIPS | &quot;clips&quot; |
| MODIFIED | &quot;modified&quot; |
| RECENT | &quot;recent&quot; |



