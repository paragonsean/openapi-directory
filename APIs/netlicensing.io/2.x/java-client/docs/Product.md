

# Product


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | If set to &#39;false&#39;, the Product is disabled. No new Licensees can be registered for the Product, existing Licensees can not obtain new Licenses |  [optional] |
|**licenseeAutoCreate** | **Boolean** | If set to &#39;true&#39;, non-existing Licensees will be created at first validation attempt. |  [optional] |
|**name** | **String** | Product name. Together with the version identifies the Product for the end customer |  [optional] |
|**number** | **String** | Unique number that identifies the Product. Vendor can assign this number when creating a Product or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product. |  [optional] |
|**version** | **String** | Product version. Convenience parameter, additional to the Product name. |  [optional] |



