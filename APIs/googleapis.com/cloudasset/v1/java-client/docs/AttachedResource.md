

# AttachedResource

Attached resource representation, which is defined by the corresponding service provider. It represents an attached resource's payload.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetType** | **String** | The type of this attached resource. Example: &#x60;osconfig.googleapis.com/Inventory&#x60; You can find the supported attached asset types of each resource in this table: &#x60;https://cloud.google.com/asset-inventory/docs/supported-asset-types&#x60; |  [optional] |
|**versionedResources** | [**List&lt;VersionedResource&gt;**](VersionedResource.md) | Versioned resource representations of this attached resource. This is repeated because there could be multiple versions of the attached resource representations during version migration. |  [optional] |



