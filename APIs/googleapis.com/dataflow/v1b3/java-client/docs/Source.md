

# Source

A source that records can be read and decoded from.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseSpecs** | **List&lt;Map&lt;String, Object&gt;&gt;** | While splitting, sources may specify the produced bundles as differences against another source, in order to save backend-side memory and allow bigger jobs. For details, see SourceSplitRequest. To support this use case, the full set of parameters of the source is logically obtained by taking the latest explicitly specified value of each parameter in the order: base_specs (later items win), spec (overrides anything in base_specs). |  [optional] |
|**codec** | **Map&lt;String, Object&gt;** | The codec to use to decode data read from the source. |  [optional] |
|**doesNotNeedSplitting** | **Boolean** | Setting this value to true hints to the framework that the source doesn&#39;t need splitting, and using SourceSplitRequest on it would yield SOURCE_SPLIT_OUTCOME_USE_CURRENT. E.g. a file splitter may set this to true when splitting a single file into a set of byte ranges of appropriate size, and set this to false when splitting a filepattern into individual files. However, for efficiency, a file splitter may decide to produce file subranges directly from the filepattern to avoid a splitting round-trip. See SourceSplitRequest for an overview of the splitting process. This field is meaningful only in the Source objects populated by the user (e.g. when filling in a DerivedSource). Source objects supplied by the framework to the user don&#39;t have this field populated. |  [optional] |
|**metadata** | [**SourceMetadata**](SourceMetadata.md) |  |  [optional] |
|**spec** | **Map&lt;String, Object&gt;** | The source to read from, plus its parameters. |  [optional] |



