# VertexAiSearchForRetailApi.GoogleCloudRetailV2alphaImportProductsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorsConfig** | [**GoogleCloudRetailV2alphaImportErrorsConfig**](GoogleCloudRetailV2alphaImportErrorsConfig.md) |  | [optional] 
**inputConfig** | [**GoogleCloudRetailV2alphaProductInputConfig**](GoogleCloudRetailV2alphaProductInputConfig.md) |  | [optional] 
**notificationPubsubTopic** | **String** | Full Pub/Sub topic name for receiving notification. If this field is set, when the import is finished, a notification is sent to specified Pub/Sub topic. The message data is JSON string of a Operation. Format of the Pub/Sub topic is &#x60;projects/{project}/topics/{topic}&#x60;. It has to be within the same project as ImportProductsRequest.parent. Make sure that both &#x60;cloud-retail-customer-data-access@system.gserviceaccount.com&#x60; and &#x60;service-@gcp-sa-retail.iam.gserviceaccount.com&#x60; have the &#x60;pubsub.topics.publish&#x60; IAM permission on the topic. Only supported when ImportProductsRequest.reconciliation_mode is set to &#x60;FULL&#x60;. | [optional] 
**reconciliationMode** | **String** | The mode of reconciliation between existing products and the products to be imported. Defaults to ReconciliationMode.INCREMENTAL. | [optional] 
**requestId** | **String** | Deprecated. This field has no effect. | [optional] 
**skipDefaultBranchProtection** | **Boolean** | If true, this performs the FULL import even if it would delete a large proportion of the products in the default branch, which could potentially cause outages if you have live predict/search traffic. Only supported when ImportProductsRequest.reconciliation_mode is set to &#x60;FULL&#x60;. | [optional] 
**updateMask** | **String** | Indicates which fields in the provided imported &#x60;products&#x60; to update. If not set, all fields are updated. If provided, only the existing product fields are updated. Missing products will not be created. | [optional] 



## Enum: ReconciliationModeEnum


* `RECONCILIATION_MODE_UNSPECIFIED` (value: `"RECONCILIATION_MODE_UNSPECIFIED"`)

* `INCREMENTAL` (value: `"INCREMENTAL"`)

* `FULL` (value: `"FULL"`)




