

# TaxDataOrderTaxDetailsItemInterface

Interface OrderTaxDetailsItemInterface

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appliedTaxes** | [**List&lt;TaxDataOrderTaxDetailsAppliedTaxInterface&gt;**](TaxDataOrderTaxDetailsAppliedTaxInterface.md) | Applied taxes |  [optional] |
|**associatedItemId** | **Integer** | Associated item id if this item is associated with another item, null otherwise |  [optional] |
|**extensionAttributes** | **Object** | ExtensionInterface class for @see \\Magento\\Tax\\Api\\Data\\OrderTaxDetailsItemInterface |  [optional] |
|**itemId** | **Integer** | Item id if this item is a product |  [optional] |
|**type** | **String** | Type (shipping, product, weee, gift wrapping, etc) |  [optional] |



