# VertexAiApi.GoogleCloudAiplatformV1PublisherModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frameworks** | **[String]** | Optional. Additional information about the model&#39;s Frameworks. | [optional] 
**launchStage** | **String** | Optional. Indicates the launch stage of the model. | [optional] 
**name** | **String** | Output only. The resource name of the PublisherModel. | [optional] [readonly] 
**openSourceCategory** | **String** | Required. Indicates the open source category of the publisher model. | [optional] 
**predictSchemata** | [**GoogleCloudAiplatformV1PredictSchemata**](GoogleCloudAiplatformV1PredictSchemata.md) |  | [optional] 
**publisherModelTemplate** | **String** | Optional. Output only. Immutable. Used to indicate this model has a publisher model and provide the template of the publisher model resource name. | [optional] [readonly] 
**supportedActions** | [**GoogleCloudAiplatformV1PublisherModelCallToAction**](GoogleCloudAiplatformV1PublisherModelCallToAction.md) |  | [optional] 
**versionId** | **String** | Output only. Immutable. The version ID of the PublisherModel. A new version is committed when a new model version is uploaded under an existing model id. It is an auto-incrementing decimal number in string representation. | [optional] [readonly] 
**versionState** | **String** | Optional. Indicates the state of the model version. | [optional] 



## Enum: LaunchStageEnum


* `LAUNCH_STAGE_UNSPECIFIED` (value: `"LAUNCH_STAGE_UNSPECIFIED"`)

* `DOGFOOD` (value: `"DOGFOOD"`)

* `EXPERIMENTAL` (value: `"EXPERIMENTAL"`)

* `PRIVATE_PREVIEW` (value: `"PRIVATE_PREVIEW"`)

* `PUBLIC_PREVIEW` (value: `"PUBLIC_PREVIEW"`)

* `GA` (value: `"GA"`)





## Enum: OpenSourceCategoryEnum


* `OPEN_SOURCE_CATEGORY_UNSPECIFIED` (value: `"OPEN_SOURCE_CATEGORY_UNSPECIFIED"`)

* `PROPRIETARY` (value: `"PROPRIETARY"`)

* `GOOGLE_OWNED_OSS_WITH_GOOGLE_CHECKPOINT` (value: `"GOOGLE_OWNED_OSS_WITH_GOOGLE_CHECKPOINT"`)

* `THIRD_PARTY_OWNED_OSS_WITH_GOOGLE_CHECKPOINT` (value: `"THIRD_PARTY_OWNED_OSS_WITH_GOOGLE_CHECKPOINT"`)

* `GOOGLE_OWNED_OSS` (value: `"GOOGLE_OWNED_OSS"`)

* `THIRD_PARTY_OWNED_OSS` (value: `"THIRD_PARTY_OWNED_OSS"`)





## Enum: VersionStateEnum


* `UNSPECIFIED` (value: `"VERSION_STATE_UNSPECIFIED"`)

* `STABLE` (value: `"VERSION_STATE_STABLE"`)

* `UNSTABLE` (value: `"VERSION_STATE_UNSTABLE"`)




