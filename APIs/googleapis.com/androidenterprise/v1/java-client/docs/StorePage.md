

# StorePage

Definition of a managed Google Play store page, made of a localized name and links to other pages. A page also contains clusters defined as a subcollection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Unique ID of this page. Assigned by the server. Immutable once assigned. |  [optional] |
|**link** | **List&lt;String&gt;** | Ordered list of pages a user should be able to reach from this page. The list can&#39;t include this page. It is recommended that the basic pages are created first, before adding the links between pages. The API doesn&#39;t verify that the pages exist or the pages are reachable. |  [optional] |
|**name** | [**List&lt;LocalizedText&gt;**](LocalizedText.md) | Ordered list of localized strings giving the name of this page. The text displayed is the one that best matches the user locale, or the first entry if there is no good match. There needs to be at least one entry. |  [optional] |



