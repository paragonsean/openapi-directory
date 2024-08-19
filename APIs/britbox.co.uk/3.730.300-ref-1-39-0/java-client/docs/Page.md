

# Page


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Unique identifier for the page. |  |
|**isStatic** | **Boolean** | True if this page is static and doesn&#39;t have any dynamic content to load.  Static pages don&#39;t need to go back to the page endpoint to load page content instead the page summary loaded with the sitemap should be enough to determine the page template type and render based on this.  |  |
|**isSystemPage** | **Boolean** | True if this page is a system page type.  **DEPRECATED** This property doesn&#39;t have any real use in client applications anymore so shouldn&#39;t be used. It especially shouldn&#39;t be used to determine if a page is static or not. Use the &#x60;isStatic&#x60; property instead.  |  |
|**key** | **String** | Key used to lookup a known page. |  [optional] |
|**path** | **String** | Unique path for the page. |  |
|**template** | **String** | Identifier for of the page template to render this page. |  |
|**title** | **String** | Title of the page. |  |
|**customFields** | **Map&lt;String, Object&gt;** | A map of custom fields defined by a curator for a page. |  [optional] |
|**entries** | [**List&lt;PageEntry&gt;**](PageEntry.md) | Entries of a page |  |
|**item** | [**ItemDetail**](ItemDetail.md) |  |  [optional] |
|**_list** | [**ItemList**](ItemList.md) |  |  [optional] |
|**metadata** | [**PageMetadata**](PageMetadata.md) |  |  [optional] |
|**themes** | [**List&lt;Theme&gt;**](Theme.md) |  |  [optional] |



