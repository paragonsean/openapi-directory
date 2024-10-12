

# JobMetadata

Metadata available primarily for filtering jobs. Will be included in the ListJob response and Job SUMMARY view.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigTableDetails** | [**List&lt;BigTableIODetails&gt;**](BigTableIODetails.md) | Identification of a Cloud Bigtable source used in the Dataflow job. |  [optional] |
|**bigqueryDetails** | [**List&lt;BigQueryIODetails&gt;**](BigQueryIODetails.md) | Identification of a BigQuery source used in the Dataflow job. |  [optional] |
|**datastoreDetails** | [**List&lt;DatastoreIODetails&gt;**](DatastoreIODetails.md) | Identification of a Datastore source used in the Dataflow job. |  [optional] |
|**fileDetails** | [**List&lt;FileIODetails&gt;**](FileIODetails.md) | Identification of a File source used in the Dataflow job. |  [optional] |
|**pubsubDetails** | [**List&lt;PubSubIODetails&gt;**](PubSubIODetails.md) | Identification of a Pub/Sub source used in the Dataflow job. |  [optional] |
|**sdkVersion** | [**SdkVersion**](SdkVersion.md) |  |  [optional] |
|**spannerDetails** | [**List&lt;SpannerIODetails&gt;**](SpannerIODetails.md) | Identification of a Spanner source used in the Dataflow job. |  [optional] |
|**userDisplayProperties** | **Map&lt;String, String&gt;** | List of display properties to help UI filter jobs. |  [optional] |



