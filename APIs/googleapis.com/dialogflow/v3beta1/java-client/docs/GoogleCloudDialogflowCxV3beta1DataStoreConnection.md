

# GoogleCloudDialogflowCxV3beta1DataStoreConnection

A data store connection. It represents a data store in Discovery Engine and the type of the contents it contains.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataStore** | **String** | The full name of the referenced data store. Formats: &#x60;projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}&#x60; &#x60;projects/{project}/locations/{location}/dataStores/{data_store}&#x60; |  [optional] |
|**dataStoreType** | [**DataStoreTypeEnum**](#DataStoreTypeEnum) | The type of the connected data store. |  [optional] |



## Enum: DataStoreTypeEnum

| Name | Value |
|---- | -----|
| DATA_STORE_TYPE_UNSPECIFIED | &quot;DATA_STORE_TYPE_UNSPECIFIED&quot; |
| PUBLIC_WEB | &quot;PUBLIC_WEB&quot; |
| UNSTRUCTURED | &quot;UNSTRUCTURED&quot; |
| STRUCTURED | &quot;STRUCTURED&quot; |



