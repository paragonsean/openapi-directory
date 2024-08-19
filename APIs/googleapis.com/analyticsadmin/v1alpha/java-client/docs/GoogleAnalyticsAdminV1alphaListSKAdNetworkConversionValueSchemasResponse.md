

# GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse

Response message for ListSKAdNetworkConversionValueSchemas RPC

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. Currently, Google Analytics supports only one SKAdNetworkConversionValueSchema per dataStream, so this will never be populated. |  [optional] |
|**skadnetworkConversionValueSchemas** | [**List&lt;GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema&gt;**](GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema.md) | List of SKAdNetworkConversionValueSchemas. This will have at most one value. |  [optional] |



