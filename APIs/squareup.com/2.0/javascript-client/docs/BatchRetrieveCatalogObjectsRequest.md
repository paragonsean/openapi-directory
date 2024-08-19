# SquareConnectApi.BatchRetrieveCatalogObjectsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalogVersion** | **Number** | The specific version of the catalog objects to be included in the response.  This allows you to retrieve historical versions of objects. The specified version value is matched against the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s&#39; &#x60;version&#x60; attribute. | [optional] 
**includeRelatedObjects** | **Boolean** | If &#x60;true&#x60;, the response will include additional objects that are related to the requested objects, as follows:  If the &#x60;objects&#x60; field of the response contains a CatalogItem, its associated CatalogCategory objects, CatalogTax objects, CatalogImage objects and CatalogModifierLists will be returned in the &#x60;related_objects&#x60; field of the response. If the &#x60;objects&#x60; field of the response contains a CatalogItemVariation, its parent CatalogItem will be returned in the &#x60;related_objects&#x60; field of the response. | [optional] 
**objectIds** | **[String]** | The IDs of the CatalogObjects to be retrieved. | 


