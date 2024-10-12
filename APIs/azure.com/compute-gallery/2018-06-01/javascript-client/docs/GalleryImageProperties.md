# SharedImageGalleryServiceClient.GalleryImageProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of this gallery Image Definition resource. This property is updatable. | [optional] 
**disallowed** | [**Disallowed**](Disallowed.md) |  | [optional] 
**endOfLifeDate** | **Date** | The end of life date of the gallery Image Definition. This property can be used for decommissioning purposes. This property is updatable. | [optional] 
**eula** | **String** | The Eula agreement for the gallery Image Definition. | [optional] 
**identifier** | [**GalleryImageIdentifier**](GalleryImageIdentifier.md) |  | 
**osState** | **String** | The allowed values for OS State are &#39;Generalized&#39;. | 
**osType** | **String** | This property allows you to specify the type of the OS that is included in the disk when creating a VM from a managed image. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Windows** &lt;br&gt;&lt;br&gt; **Linux** | 
**privacyStatementUri** | **String** | The privacy statement uri. | [optional] 
**provisioningState** | **String** | The provisioning state, which only appears in the response. | [optional] [readonly] 
**purchasePlan** | [**ImagePurchasePlan**](ImagePurchasePlan.md) |  | [optional] 
**recommended** | [**RecommendedMachineConfiguration**](RecommendedMachineConfiguration.md) |  | [optional] 
**releaseNoteUri** | **String** | The release note uri. | [optional] 



## Enum: OsStateEnum


* `Generalized` (value: `"Generalized"`)

* `Specialized` (value: `"Specialized"`)





## Enum: OsTypeEnum


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)





## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Failed` (value: `"Failed"`)

* `Succeeded` (value: `"Succeeded"`)

* `Deleting` (value: `"Deleting"`)

* `Migrating` (value: `"Migrating"`)




