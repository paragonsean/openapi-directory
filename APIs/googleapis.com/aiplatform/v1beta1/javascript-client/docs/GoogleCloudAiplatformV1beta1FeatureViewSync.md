# VertexAiApi.GoogleCloudAiplatformV1beta1FeatureViewSync

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Time when this FeatureViewSync is created. Creation of a FeatureViewSync means that the job is pending / waiting for sufficient resources but may not have started the actual data transfer yet. | [optional] [readonly] 
**finalStatus** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**name** | **String** | Identifier. Name of the FeatureViewSync. Format: &#x60;projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}/featureViewSyncs/{feature_view_sync}&#x60; | [optional] 
**runTime** | [**GoogleTypeInterval**](GoogleTypeInterval.md) |  | [optional] 
**syncSummary** | [**GoogleCloudAiplatformV1beta1FeatureViewSyncSyncSummary**](GoogleCloudAiplatformV1beta1FeatureViewSyncSyncSummary.md) |  | [optional] 


