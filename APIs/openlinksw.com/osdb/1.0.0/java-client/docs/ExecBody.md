

# ExecBody


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionSpecificProperty1** | **String** | An example action specific property. There may be 0, 1 or more action specific properties, each holding an action specific parameter value. |  [optional] |
|**actionSpecificProperty2** | **String** | An example action specific property. There may be 0, 1 or more action specific properties, each holding an action specific parameter value. |  [optional] |
|**osdbColonBodyDataEncoding** | **String** | The media type of the data associated with osdb:body_data_raw or osdb:body_data_src_url. In the case of osdb:body_data_raw, this is the media type before base64 encoding. |  [optional] |
|**osdbColonBodyDataRaw** | **byte[]** | Input data for the action (e.g. CSV data). The data must be base64 encoded by the client. Alternatively, clients can use osdb:body_data_src_url to supply the input data via a web-accessible document. |  [optional] |
|**osdbColonBodyDataSrcUrl** | **URI** | URL of a resource containing input data for the action (e.g. CSV data). Clients can instead use osdb:body_data_raw to supply the input data directly. |  [optional] |
|**osdbColonOutputType** | [**OsdbColonOutputTypeEnum**](#OsdbColonOutputTypeEnum) | An OSDB-specific parameter controlling the action output type. If omitted, the native action output is returned. |  [optional] |
|**osdbColonResponseFormat** | **String** | Preferred response MIME type. This must be an output MIME type supported natively by the action or, if &#39;osdb:output_type&#39; is set to &#39;generate_rdf&#39;, a Virtuoso Sponger output format. i.e. &#39;application/ld+json&#39;, &#39;text/turtle&#39; or &#39;application/rdf+xml&#39;. |  [optional] |



## Enum: OsdbColonOutputTypeEnum

| Name | Value |
|---- | -----|
| URL_ONLY | &quot;url_only&quot; |
| GENERATE_RDF | &quot;generate_rdf&quot; |
| DISPLAY_RDF | &quot;display_rdf&quot; |



