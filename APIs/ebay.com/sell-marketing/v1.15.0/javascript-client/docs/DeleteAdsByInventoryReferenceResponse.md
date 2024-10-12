# MarketingApi.DeleteAdsByInventoryReferenceResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adIds** | **[String]** | The unique identifier of the ad that was deleted, or the ad that the seller attempted to delete.&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt;Although the field name is plural and it is an array, only one ad ID will be returned here since there can be only one ad per listing.&lt;/span&gt; | [optional] 
**errors** | [**[Error]**](Error.md) | The container for the errors associated with the request. | [optional] 
**inventoryReferenceId** | **String** | The inventory reference ID is a seller-defined SKU value for a single-item listing, or a seller-defined identifier for an inventory item group. Both of these values are defined when using the Inventory API, and an inventory item group is used to create a multiple-variation listing. | [optional] 
**inventoryReferenceType** | **String** | The enumeration value returned here indicates if the ad was for a single-variation listing or a multiple-variation listing. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/marketing/types/pls:InventoryReferenceTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**statusCode** | **Number** | An HTTP status code indicating if the corresponding ad was successfully deleted or not. &lt;code&gt;200 Successful&lt;/code&gt; should be returned for successfully deleted ads. &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt;A status code is returned for each ad that the seller deletes, or attempts to delete.&lt;/span&gt; | [optional] 


