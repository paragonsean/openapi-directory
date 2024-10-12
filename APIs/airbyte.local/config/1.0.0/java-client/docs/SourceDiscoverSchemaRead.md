

# SourceDiscoverSchemaRead

Returns the results of a discover catalog job. If the job was not successful, the catalog field will not be present. jobInfo will aways be present and its status be used to determine if the job was successful or not.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**breakingChange** | **Boolean** |  |  [optional] |
|**catalog** | [**AirbyteCatalog**](AirbyteCatalog.md) |  |  [optional] |
|**catalogDiff** | [**CatalogDiff**](CatalogDiff.md) |  |  [optional] |
|**catalogId** | **UUID** |  |  [optional] |
|**connectionStatus** | **ConnectionStatus** |  |  [optional] |
|**jobInfo** | [**SynchronousJobRead**](SynchronousJobRead.md) |  |  |



