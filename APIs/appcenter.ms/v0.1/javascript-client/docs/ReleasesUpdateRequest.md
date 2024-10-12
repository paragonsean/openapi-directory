# AppCenterClient.ReleasesUpdateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | [**ReleasesGetLatestByDistributionGroup200ResponseBuild**](ReleasesGetLatestByDistributionGroup200ResponseBuild.md) |  | [optional] 
**destinationId** | **String** | OBSOLETE. Will be removed in future releases - use destinations instead. Id of a destination. The release will be associated with this destination. If the destination doesn&#39;t exist a 400 is returned. If both destination name and id are passed, the id is taking precedence. | [optional] 
**destinationName** | **String** | OBSOLETE. Will be removed in future releases - use destinations instead. Name of a destination. The release will be associated with this destination. If the destination doesn&#39;t exist a 400 is returned. If both distribution group name and id are passed, the id is taking precedence. | [optional] 
**destinationType** | **String** | Not used anymore. | [optional] 
**destinations** | [**[ReleasesUpdateRequestDestinationsInner]**](ReleasesUpdateRequestDestinationsInner.md) | Distribute this release under the following list of destinations (store groups or distribution groups). | [optional] 
**distributionGroupId** | **String** | OBSOLETE. Will be removed in future releases - use destinations instead. Id of a distribution group. The release will be associated with this distribution group. If the distribution group doesn&#39;t exist a 400 is returned. If both distribution group name and id are passed, the id is taking precedence. | [optional] 
**distributionGroupName** | **String** | OBSOLETE. Will be removed in future releases - use destinations instead. Name of a distribution group. The release will be associated with this distribution group. If the distribution group doesn&#39;t exist a 400 is returned. If both distribution group name and id are passed, the id is taking precedence. | [optional] 
**mandatoryUpdate** | **Boolean** | A boolean which determines whether this version should be a mandatory update or not. | [optional] 
**metadata** | [**ReleasesUpdateRequestMetadata**](ReleasesUpdateRequestMetadata.md) |  | [optional] 
**notifyTesters** | **Boolean** | A boolean which determines whether to notify testers of a new release, default to true. | [optional] [default to true]
**releaseNotes** | **String** | Release notes for this release. | [optional] 


