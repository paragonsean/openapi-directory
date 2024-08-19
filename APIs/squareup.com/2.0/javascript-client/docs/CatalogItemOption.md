# SquareConnectApi.CatalogItemOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The item option&#39;s human-readable description. Displayed in the Square Point of Sale app for the seller and in the Online Store or on receipts for the buyer. This is a searchable attribute for use in applicable query filters. | [optional] 
**displayName** | **String** | The item option&#39;s display name for the customer. This is a searchable attribute for use in applicable query filters. | [optional] 
**name** | **String** | The item option&#39;s display name for the seller. Must be unique across all item options. This is a searchable attribute for use in applicable query filters. | [optional] 
**showColors** | **Boolean** | If true, display colors for entries in &#x60;values&#x60; when present. | [optional] 
**values** | [**[CatalogObject]**](CatalogObject.md) | A list of CatalogObjects containing the &#x60;CatalogItemOptionValue&#x60;s for this item. | [optional] 


