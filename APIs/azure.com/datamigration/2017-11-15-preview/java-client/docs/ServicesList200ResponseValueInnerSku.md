

# ServicesList200ResponseValueInnerSku

An Azure SKU instance

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | The capacity of the SKU, if it supports scaling |  [optional] |
|**family** | **String** | The SKU family, used when the service has multiple performance classes within a tier, such as &#39;A&#39;, &#39;D&#39;, etc. for virtual machines |  [optional] |
|**name** | **String** | The unique name of the SKU, such as &#39;P3&#39; |  [optional] |
|**size** | **String** | The size of the SKU, used when the name alone does not denote a service size or when a SKU has multiple performance classes within a family, e.g. &#39;A1&#39; for virtual machines |  [optional] |
|**tier** | **String** | The tier of the SKU, such as &#39;Free&#39;, &#39;Basic&#39;, &#39;Standard&#39;, or &#39;Premium&#39; |  [optional] |



