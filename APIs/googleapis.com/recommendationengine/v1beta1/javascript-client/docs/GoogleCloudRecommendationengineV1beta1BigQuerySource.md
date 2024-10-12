# RecommendationsAiBeta.GoogleCloudRecommendationengineV1beta1BigQuerySource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataSchema** | **String** | Optional. The schema to use when parsing the data from the source. Supported values for catalog imports: 1: \&quot;catalog_recommendations_ai\&quot; using https://cloud.google.com/recommendations-ai/docs/upload-catalog#json (Default for catalogItems.import) 2: \&quot;catalog_merchant_center\&quot; using https://cloud.google.com/recommendations-ai/docs/upload-catalog#mc Supported values for user event imports: 1: \&quot;user_events_recommendations_ai\&quot; using https://cloud.google.com/recommendations-ai/docs/manage-user-events#import (Default for userEvents.import) 2. \&quot;user_events_ga360\&quot; using https://support.google.com/analytics/answer/3437719?hl&#x3D;en | [optional] 
**datasetId** | **String** | Required. The BigQuery data set to copy the data from. | [optional] 
**gcsStagingDir** | **String** | Optional. Intermediate Cloud Storage directory used for the import. Can be specified if one wants to have the BigQuery export to a specific Cloud Storage directory. | [optional] 
**projectId** | **String** | Optional. The project id (can be project # or id) that the BigQuery source is in. If not specified, inherits the project id from the parent request. | [optional] 
**tableId** | **String** | Required. The BigQuery table to copy the data from. | [optional] 


