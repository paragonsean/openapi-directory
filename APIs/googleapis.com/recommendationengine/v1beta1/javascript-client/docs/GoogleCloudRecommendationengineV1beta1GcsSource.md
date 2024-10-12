# RecommendationsAiBeta.GoogleCloudRecommendationengineV1beta1GcsSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputUris** | **[String]** | Required. Google Cloud Storage URIs to input files. URI can be up to 2000 characters long. URIs can match the full object path (for example, &#x60;gs://bucket/directory/object.json&#x60;) or a pattern matching one or more files, such as &#x60;gs://bucket/directory/_*.json&#x60;. A request can contain at most 100 files, and each file can be up to 2 GB. See [Importing catalog information](/recommendations-ai/docs/upload-catalog) for the expected file format and setup instructions. | [optional] 
**jsonSchema** | **String** | Optional. The schema to use when parsing the data from the source. Supported values for catalog imports: 1: \&quot;catalog_recommendations_ai\&quot; using https://cloud.google.com/recommendations-ai/docs/upload-catalog#json (Default for catalogItems.import) 2: \&quot;catalog_merchant_center\&quot; using https://cloud.google.com/recommendations-ai/docs/upload-catalog#mc Supported values for user events imports: 1: \&quot;user_events_recommendations_ai\&quot; using https://cloud.google.com/recommendations-ai/docs/manage-user-events#import (Default for userEvents.import) 2. \&quot;user_events_ga360\&quot; using https://support.google.com/analytics/answer/3437719?hl&#x3D;en | [optional] 


