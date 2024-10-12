# CatalogApi.SkulistbyProductId

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activateIfPossible** | **Boolean** | When set to &#x60;true&#x60;, this attribute will automatically update the SKU as active once associated with an image or an active component. | [optional] 
**commercialConditionId** | **Number** | SKU Commercial Condition ID. | [optional] 
**cubicWeight** | **Number** | [Cubic weight](https://help.vtex.com/en/tutorial/understanding-the-cubic-weight-factor--tutorials_128). | [optional] 
**dateUpdated** | **String** | Date when the product was updated for the most recent time. | [optional] 
**estimatedDateArrival** | **String** | SKU estimated arrival date in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format, when the product is on pre-sale. You must take into consideration both the launch date and the freight calculation for the arrival date. | [optional] 
**flagKitItensSellApart** | **Boolean** | Defines if the SKU bundle items can be sold separately. | [optional] 
**height** | **Number** | SKU Height. | [optional] 
**id** | **Number** | SKU ID. | [optional] 
**internalNote** | **String** | Internal note. | [optional] 
**isActive** | **Boolean** | Defines if the SKU is active or not. | [optional] 
**isDynamicKit** | **String** |  | [optional] 
**isGiftCardRecharge** | **Boolean** | Defines if the purchase of the SKU will generate reward value for the customer. | [optional] 
**isInventoried** | **Boolean** |  | [optional] 
**isKit** | **Boolean** | Flag to set whether the product SKU is made up of one or more SKUs, thereby becoming a bundle. Must be enabled if you are adding a bundle. Once activated, the flag cannot be reverted. | [optional] 
**isPersisted** | **Boolean** | Defines if the SKU is persisted. | [optional] 
**isRemoved** | **Boolean** | Defines if the SKU is removed. | [optional] 
**isTransported** | **Boolean** |  | [optional] 
**length** | **Number** | SKU Length. | [optional] 
**manufacturerCode** | **String** | Product Supplier ID. | [optional] 
**measurementUnit** | **String** | Measurement unit. | [optional] 
**modalId** | **Number** | Delivery Method (Modal Type) ID. | [optional] 
**modalType** | **String** | Links an unusual type of SKU to a carrier specialized in delivering it. This field should be filled in with the name of the modal (e.g. \&quot;Chemicals\&quot; or \&quot;Refrigerated products\&quot;). To learn more about this feature, read our articles [How the modal works](https://help.vtex.com/en/tutorial/how-does-the-modal-work--tutorials_125) and [Setting up modal for carriers](https://help.vtex.com/en/tutorial/configure-modal--3jhLqxuPhuiq24UoykCcqy). | [optional] 
**name** | **String** | SKU Name. | [optional] 
**position** | **Number** | SKU Position. | [optional] 
**productId** | **Number** | Product ID. | [optional] 
**realHeight** | **Number** | Real SKU Height. | [optional] 
**realLength** | **Number** | Real SKU Length. | [optional] 
**realWeightKg** | **Number** | Real Weight of the SKU in the measurement [configured in the store](https://help.vtex.com/en/tutorial/filling-in-system-settings--tutorials_269), which by default is in grams. | [optional] 
**realWidth** | **Number** | Real SKU Width. | [optional] 
**refId** | **String** | Product Reference ID. | [optional] 
**referenceStockKeepingUnitId** | **String** | SKU Reference ID. | [optional] 
**rewardValue** | **Number** | Reward value related to the SKU. | [optional] 
**unitMultiplier** | **Number** | This is the multiple number of SKU. If the Multiplier is 5.0000, the product can be added in multiple quantities of 5, 10, 15, 20, onward. | [optional] 
**weightKg** | **Number** | Weight of the SKU in the measurement [configured in the store](https://help.vtex.com/en/tutorial/filling-in-system-settings--tutorials_269), which by default is in grams. | [optional] 
**width** | **Number** | SKU Width. | [optional] 
**isKitOptimized** | **Boolean** | Defines if the SKU is a Optimized bundle. | [optional] 


