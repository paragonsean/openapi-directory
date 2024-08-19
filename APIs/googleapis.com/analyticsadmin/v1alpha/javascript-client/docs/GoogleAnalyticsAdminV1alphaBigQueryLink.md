# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaBigQueryLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Time when the link was created. | [optional] [readonly] 
**dailyExportEnabled** | **Boolean** | If set true, enables daily data export to the linked Google Cloud project. | [optional] 
**excludedEvents** | **[String]** | The list of event names that will be excluded from exports. | [optional] 
**exportStreams** | **[String]** | The list of streams under the parent property for which data will be exported. Format: properties/{property_id}/dataStreams/{stream_id} Example: [&#39;properties/1000/dataStreams/2000&#39;] | [optional] 
**freshDailyExportEnabled** | **Boolean** | If set true, enables fresh daily export to the linked Google Cloud project. | [optional] 
**includeAdvertisingId** | **Boolean** | If set true, exported data will include advertising identifiers for mobile app streams. | [optional] 
**name** | **String** | Output only. Resource name of this BigQuery link. Format: &#39;properties/{property_id}/bigQueryLinks/{bigquery_link_id}&#39; Format: &#39;properties/1234/bigQueryLinks/abc567&#39; | [optional] [readonly] 
**project** | **String** | Immutable. The linked Google Cloud project. When creating a BigQueryLink, you may provide this resource name using either a project number or project ID. Once this resource has been created, the returned project will always have a project that contains a project number. Format: &#39;projects/{project number}&#39; Example: &#39;projects/1234&#39; | [optional] 
**streamingExportEnabled** | **Boolean** | If set true, enables streaming export to the linked Google Cloud project. | [optional] 


