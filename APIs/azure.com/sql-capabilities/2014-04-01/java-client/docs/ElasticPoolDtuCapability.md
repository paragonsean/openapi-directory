

# ElasticPoolDtuCapability

The Elastic Pool DTU capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includedMaxSize** | [**MaxSizeCapability**](MaxSizeCapability.md) |  |  [optional] |
|**limit** | **Long** | The maximum size of the database (see &#39;unit&#39; for the units). |  [optional] [readonly] |
|**maxDatabaseCount** | **Long** | The maximum number of databases supported. |  [optional] [readonly] |
|**status** | **CapabilityStatus** |  |  [optional] |
|**supportedMaxSizes** | [**List&lt;MaxSizeCapability&gt;**](MaxSizeCapability.md) | The list of supported max sizes. |  [optional] [readonly] |
|**supportedPerDatabaseMaxDtus** | [**List&lt;ElasticPoolPerDatabaseMaxDtuCapability&gt;**](ElasticPoolPerDatabaseMaxDtuCapability.md) | The list of supported max database DTUs. |  [optional] [readonly] |
|**supportedPerDatabaseMaxSizes** | [**List&lt;MaxSizeCapability&gt;**](MaxSizeCapability.md) | The list of supported max database sizes. |  [optional] [readonly] |



