

# BoxProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensions** | [**Point**](Point.md) | the [height,length,width] of the box. |  |
|**name** | **String** | name for the type of box. |  [optional] |
|**price** | **Integer** | Fixed price of the container, in whole units of currency, default USD cents. This can represent the cost of a flat rate carton, the cost of the actual carton materials, or it can include any other flat fees that may need to be added on a &lt;i&gt;per-carton&lt;/i&gt; basis, such as handling, accessorial surchages, oversize fees, etc. This value is &lt;i&gt;added&lt;/i&gt; to any rate table rates defined for the carton. |  [optional] |
|**rateTable** | [**RateTable**](RateTable.md) | An optional rate table definition for improved carton selection and pricing optimization. Defaults are included using retail rates for FedEx and UPS if carrier and service is provided, but optimization can be improved with more data passed in a carton&#39;s specific rate table. Methods are &lt;ol&gt;&lt;li&gt;Provide carrier, service, and zone.&lt;/li&gt;&lt;li&gt;Provide all acceptable weights and prices to use for the carton, similar to actual carrier rate tables.&lt;/li&gt;&lt;li&gt;Provide the coefficients required for a simple linear weight-dependent pricing model.&lt;/li&gt;&lt;/ol&gt; |  [optional] |
|**weightMax** | **BigDecimal** | maximum allowable gross weight for the box, i.e., all packed item weights plus the weightTare. |  |
|**weightTare** | **BigDecimal** | weight of the container when empty or otherwise unladen, i.e., of the box itself. |  [optional] |



