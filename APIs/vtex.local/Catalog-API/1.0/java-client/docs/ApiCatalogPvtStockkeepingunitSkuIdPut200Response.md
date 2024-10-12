

# ApiCatalogPvtStockkeepingunitSkuIdPut200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activateIfPossible** | **Boolean** | When set to &#x60;true&#x60;, this attribute will automatically update the SKU as active once associated with an image or an active component. |  [optional] |
|**commercialConditionId** | **Integer** | Used to define SKU specific promotions or installment rules. In case of no specific condition, use &#x60;1&#x60; (default value). This field does not accept &#x60;0&#x60;. Find out more by reading [Registering a commercial condition](https://help.vtex.com/tutorial/registering-a-commercial-condition--tutorials_445). |  [optional] |
|**creationDate** | **String** | Date and time of the SKU&#39;s creation. |  [optional] |
|**cubicWeight** | **BigDecimal** | [Cubic weight](https://help.vtex.com/en/tutorial/understanding-the-cubic-weight-factor--tutorials_128). |  [optional] |
|**estimatedDateArrival** | **String** | SKU estimated arrival date in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format, when the product is on pre-sale. You must take into consideration both the launch date and the freight calculation for the arrival date. |  [optional] |
|**height** | **BigDecimal** | SKU real height. |  [optional] |
|**id** | **Integer** | SKU unique identifier. |  [optional] |
|**isActive** | **Boolean** | Shows if the SKU is active (&#x60;true&#x60;) or not (&#x60;false&#x60;). |  [optional] |
|**isKit** | **Boolean** | Flag to set whether the product SKU is made up of one or more SKUs, thereby becoming a bundle. Must be enabled if you are adding a bundle. Once activated, the flag cannot be reverted. |  [optional] |
|**kitItensSellApart** | **Boolean** | Defines if Kit components can be sold apart. |  [optional] |
|**length** | **BigDecimal** | SKU real length. |  [optional] |
|**manufacturerCode** | **String** | Provided by the manufacturers to identify their product. This field should be filled in if the product has a specific manufacturer’s code. |  [optional] |
|**measurementUnit** | **String** | Used only in cases when you need to convert the unit of measure for sale. If a product is sold in boxes for example, but customers want to buy per square meter (m²). In common cases, use &#x60;&#39;un&#39;&#x60;. |  [optional] |
|**modalType** | **String** | Links an unusual type of SKU to a carrier specialized in delivering it. This field should be filled in with the name of the modal (e.g. \&quot;Chemicals\&quot; or \&quot;Refrigerated products\&quot;). To learn more about this feature, read our articles [How the modal works](https://help.vtex.com/en/tutorial/how-does-the-modal-work--tutorials_125) and [Setting up modal for carriers](https://help.vtex.com/en/tutorial/configure-modal--3jhLqxuPhuiq24UoykCcqy). |  [optional] |
|**name** | **String** | SKU name, meaning the variation of the previously added product. For example: **Product** - _Fridge_, **SKU** - _110V_. |  [optional] |
|**packagedHeight** | **BigDecimal** | Height used for shipping calculation. |  [optional] |
|**packagedLength** | **BigDecimal** | Length used for shipping calculation. |  [optional] |
|**packagedWeightKg** | **Integer** | Weight used for shipping calculation, in the measurement [configured in the store](https://help.vtex.com/en/tutorial/filling-in-system-settings--tutorials_269), which by default is in grams. |  [optional] |
|**packagedWidth** | **BigDecimal** | Width used for shipping calculation. |  [optional] |
|**productId** | **Integer** | ID of the Product associated with this SKU. |  [optional] |
|**refId** | **String** | Reference code used internally for organizational purposes. Must be unique. It is not required only if EAN code already exists. If not, this field must be provided. |  [optional] |
|**rewardValue** | **BigDecimal** | Credit that the customer receives when finalizing an order of one specific SKU unit. By filling this field out with &#x60;1&#x60;, the customer gets U$ 1 credit on the site. |  [optional] |
|**unitMultiplier** | **BigDecimal** | This is the multiple number of SKU. If the Multiplier is 5.0000, the product can be added in multiple quantities of 5, 10, 15, 20, onward. |  [optional] |
|**videos** | **List&lt;String&gt;** | Videos URLs. |  [optional] |
|**weightKg** | **BigDecimal** | Weight of the SKU in the measurement [configured in the store](https://help.vtex.com/en/tutorial/filling-in-system-settings--tutorials_269), which by default is in grams. |  [optional] |
|**width** | **BigDecimal** | SKU real width. |  [optional] |



