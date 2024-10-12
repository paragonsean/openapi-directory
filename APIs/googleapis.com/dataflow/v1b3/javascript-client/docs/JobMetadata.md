# DataflowApi.JobMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigTableDetails** | [**[BigTableIODetails]**](BigTableIODetails.md) | Identification of a Cloud Bigtable source used in the Dataflow job. | [optional] 
**bigqueryDetails** | [**[BigQueryIODetails]**](BigQueryIODetails.md) | Identification of a BigQuery source used in the Dataflow job. | [optional] 
**datastoreDetails** | [**[DatastoreIODetails]**](DatastoreIODetails.md) | Identification of a Datastore source used in the Dataflow job. | [optional] 
**fileDetails** | [**[FileIODetails]**](FileIODetails.md) | Identification of a File source used in the Dataflow job. | [optional] 
**pubsubDetails** | [**[PubSubIODetails]**](PubSubIODetails.md) | Identification of a Pub/Sub source used in the Dataflow job. | [optional] 
**sdkVersion** | [**SdkVersion**](SdkVersion.md) |  | [optional] 
**spannerDetails** | [**[SpannerIODetails]**](SpannerIODetails.md) | Identification of a Spanner source used in the Dataflow job. | [optional] 
**userDisplayProperties** | **{String: String}** | List of display properties to help UI filter jobs. | [optional] 


