

# CreateStoreRequest

The request to create a store. The store identifier is optional, if null it will be automatically computed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countryIsoCodeAlpha3** | **String** | The country iso code alpha 3 based on the list of values /user/lov/StoreCountry |  |
|**id** | **String** | The store identifier |  [optional] |
|**name** | **String** | The store name. Must be unique. |  |
|**sectors** | **List&lt;String&gt;** | The store&#39;s sectors based on the list of values /user/lov/ParamSector |  |
|**url** | **String** | The url of your store |  |



