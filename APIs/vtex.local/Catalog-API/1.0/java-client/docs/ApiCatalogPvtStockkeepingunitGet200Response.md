

# ApiCatalogPvtStockkeepingunitGet200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activateIfPossible** | **Boolean** | When set to &#x60;true&#x60;, this attribute will automatically update the SKU as active once associated with an image or an active component. |  [optional] |
|**commercialConditionId** | **Integer** | Commercial Condition ID. |  [optional] |
|**creationDate** | **String** | SKU Creation Date. |  [optional] |
|**cubicWeight** | **BigDecimal** | [Cubic Weight](https://help.vtex.com/en/tutorial/understanding-the-cubic-weight-factor--tutorials_128). |  [optional] |
|**estimatedDateArrival** | **String** | SKU estimated arrival date in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format, when the product is on pre-sale. You must take into consideration both the launch date and the freight calculation for the arrival date. |  [optional] |
|**height** | **BigDecimal** | SKU Height. |  [optional] |
|**id** | **Integer** | SKU ID. |  [optional] |
|**isActive** | **Boolean** | Defines if the SKU is active (&#x60;true&#x60;) or not (&#x60;false&#x60;). |  [optional] |
|**isKit** | **Boolean** | Shows if the SKU is a Kit (&#x60;true&#x60;) or not (&#x60;false&#x60;). |  [optional] |
|**kitItensSellApart** | **Boolean** | Defines if Kit components can be sold apart. |  [optional] |
|**length** | **BigDecimal** | SKU Length. |  [optional] |
|**manufacturerCode** | **String** | Manufacturer Code. |  [optional] |
|**measurementUnit** | **String** | Measurement Unit. |  [optional] |
|**modalType** | **String** | Links an unusual type of SKU to a carrier specialized in delivering it. This field should be filled in with the name of the modal (e.g. \&quot;Chemicals\&quot; or \&quot;Refrigerated products\&quot;). To learn more about this feature, read our articles [How the modal works](https://help.vtex.com/en/tutorial/how-does-the-modal-work--tutorials_125) and [Setting up modal for carriers](https://help.vtex.com/en/tutorial/configure-modal--3jhLqxuPhuiq24UoykCcqy). |  [optional] |
|**name** | **String** | SKU Name. |  [optional] |
|**packagedHeight** | **BigDecimal** | Packaged Height. |  [optional] |
|**packagedLength** | **BigDecimal** | Packaged Length. |  [optional] |
|**packagedWeightKg** | **BigDecimal** | Packaged Weight, in the measurement [configured in the store](https://help.vtex.com/en/tutorial/filling-in-system-settings--tutorials_269), which by default is in grams. |  [optional] |
|**packagedWidth** | **BigDecimal** | Packaged Width. |  [optional] |
|**productId** | **Integer** | Product ID. |  [optional] |
|**refId** | **String** | SKU RefId. |  [optional] |
|**rewardValue** | **BigDecimal** | Defines the value of the reward for clients who purchase the SKU. |  [optional] |
|**unitMultiplier** | **BigDecimal** | This is the multiple number of SKU. If the Multiplier is 5.0000, the product can be added in multiple quantities of 5, 10, 15, 20, onward. |  [optional] |
|**videos** | **String** | Video URLs. |  [optional] |
|**weightKg** | **BigDecimal** | Weight of the SKU in the measurement [configured in the store](https://help.vtex.com/en/tutorial/filling-in-system-settings--tutorials_269), which by default is in grams. |  [optional] |
|**width** | **BigDecimal** | SKU Width. |  [optional] |



