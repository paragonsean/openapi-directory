# DataLabelingApi.GoogleCloudDatalabelingV1beta1Dataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockingResources** | **[String]** | Output only. The names of any related resources that are blocking changes to the dataset. | [optional] 
**createTime** | **String** | Output only. Time the dataset is created. | [optional] 
**dataItemCount** | **String** | Output only. The number of data items in the dataset. | [optional] 
**description** | **String** | Optional. User-provided description of the annotation specification set. The description can be up to 10000 characters long. | [optional] 
**displayName** | **String** | Required. The display name of the dataset. Maximum of 64 characters. | [optional] 
**inputConfigs** | [**[GoogleCloudDatalabelingV1beta1InputConfig]**](GoogleCloudDatalabelingV1beta1InputConfig.md) | Output only. This is populated with the original input configs where ImportData is called. It is available only after the clients import data to this dataset. | [optional] 
**lastMigrateTime** | **String** | Last time that the Dataset is migrated to AI Platform V2. If any of the AnnotatedDataset is migrated, the last_migration_time in Dataset is also updated. | [optional] 
**name** | **String** | Output only. Dataset resource name, format is: projects/{project_id}/datasets/{dataset_id} | [optional] 


