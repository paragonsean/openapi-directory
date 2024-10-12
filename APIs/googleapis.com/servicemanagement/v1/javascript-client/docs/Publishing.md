# ServiceManagementApi.Publishing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiShortName** | **String** | Used as a tracking tag when collecting data about the APIs developer relations artifacts like docs, packages delivered to package managers, etc. Example: \&quot;speech\&quot;. | [optional] 
**codeownerGithubTeams** | **[String]** | GitHub teams to be added to CODEOWNERS in the directory in GitHub containing source code for the client libraries for this API. | [optional] 
**docTagPrefix** | **String** | A prefix used in sample code when demarking regions to be included in documentation. | [optional] 
**documentationUri** | **String** | Link to product home page. Example: https://cloud.google.com/asset-inventory/docs/overview | [optional] 
**githubLabel** | **String** | GitHub label to apply to issues and pull requests opened for this API. | [optional] 
**librarySettings** | [**[ClientLibrarySettings]**](ClientLibrarySettings.md) | Client library settings. If the same version string appears multiple times in this list, then the last one wins. Settings from earlier settings with the same version string are discarded. | [optional] 
**methodSettings** | [**[MethodSettings]**](MethodSettings.md) | A list of API method settings, e.g. the behavior for methods that use the long-running operation pattern. | [optional] 
**newIssueUri** | **String** | Link to a *public* URI where users can report issues. Example: https://issuetracker.google.com/issues/new?component&#x3D;190865&amp;template&#x3D;1161103 | [optional] 
**organization** | **String** | For whom the client library is being published. | [optional] 
**protoReferenceDocumentationUri** | **String** | Optional link to proto reference documentation. Example: https://cloud.google.com/pubsub/lite/docs/reference/rpc | [optional] 
**restReferenceDocumentationUri** | **String** | Optional link to REST reference documentation. Example: https://cloud.google.com/pubsub/lite/docs/reference/rest | [optional] 



## Enum: OrganizationEnum


* `CLIENT_LIBRARY_ORGANIZATION_UNSPECIFIED` (value: `"CLIENT_LIBRARY_ORGANIZATION_UNSPECIFIED"`)

* `CLOUD` (value: `"CLOUD"`)

* `ADS` (value: `"ADS"`)

* `PHOTOS` (value: `"PHOTOS"`)

* `STREET_VIEW` (value: `"STREET_VIEW"`)

* `SHOPPING` (value: `"SHOPPING"`)

* `GEO` (value: `"GEO"`)

* `GENERATIVE_AI` (value: `"GENERATIVE_AI"`)




