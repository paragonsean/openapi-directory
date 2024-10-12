# CloudLoggingApi.LogView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The creation timestamp of the view. | [optional] [readonly] 
**description** | **String** | Optional. Describes this view. | [optional] 
**filter** | **String** | Optional. Filter that restricts which log entries in a bucket are visible in this view.Filters must be logical conjunctions that use the AND operator, and they can use any of the following qualifiers: SOURCE(), which specifies a project, folder, organization, or billing account of origin. resource.type, which specifies the resource type. LOG_ID(), which identifies the log.They can also use the negations of these qualifiers with the NOT operator.For example:SOURCE(\&quot;projects/myproject\&quot;) AND resource.type &#x3D; \&quot;gce_instance\&quot; AND NOT LOG_ID(\&quot;stdout\&quot;) | [optional] 
**name** | **String** | Output only. The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view | [optional] [readonly] 
**updateTime** | **String** | Output only. The last update timestamp of the view. | [optional] [readonly] 


