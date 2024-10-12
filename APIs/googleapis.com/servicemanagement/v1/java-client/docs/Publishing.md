

# Publishing

This message configures the settings for publishing [Google Cloud Client libraries](https://cloud.google.com/apis/docs/cloud-client-libraries) generated from the service config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiShortName** | **String** | Used as a tracking tag when collecting data about the APIs developer relations artifacts like docs, packages delivered to package managers, etc. Example: \&quot;speech\&quot;. |  [optional] |
|**codeownerGithubTeams** | **List&lt;String&gt;** | GitHub teams to be added to CODEOWNERS in the directory in GitHub containing source code for the client libraries for this API. |  [optional] |
|**docTagPrefix** | **String** | A prefix used in sample code when demarking regions to be included in documentation. |  [optional] |
|**documentationUri** | **String** | Link to product home page. Example: https://cloud.google.com/asset-inventory/docs/overview |  [optional] |
|**githubLabel** | **String** | GitHub label to apply to issues and pull requests opened for this API. |  [optional] |
|**librarySettings** | [**List&lt;ClientLibrarySettings&gt;**](ClientLibrarySettings.md) | Client library settings. If the same version string appears multiple times in this list, then the last one wins. Settings from earlier settings with the same version string are discarded. |  [optional] |
|**methodSettings** | [**List&lt;MethodSettings&gt;**](MethodSettings.md) | A list of API method settings, e.g. the behavior for methods that use the long-running operation pattern. |  [optional] |
|**newIssueUri** | **String** | Link to a *public* URI where users can report issues. Example: https://issuetracker.google.com/issues/new?component&#x3D;190865&amp;template&#x3D;1161103 |  [optional] |
|**organization** | [**OrganizationEnum**](#OrganizationEnum) | For whom the client library is being published. |  [optional] |
|**protoReferenceDocumentationUri** | **String** | Optional link to proto reference documentation. Example: https://cloud.google.com/pubsub/lite/docs/reference/rpc |  [optional] |
|**restReferenceDocumentationUri** | **String** | Optional link to REST reference documentation. Example: https://cloud.google.com/pubsub/lite/docs/reference/rest |  [optional] |



## Enum: OrganizationEnum

| Name | Value |
|---- | -----|
| CLIENT_LIBRARY_ORGANIZATION_UNSPECIFIED | &quot;CLIENT_LIBRARY_ORGANIZATION_UNSPECIFIED&quot; |
| CLOUD | &quot;CLOUD&quot; |
| ADS | &quot;ADS&quot; |
| PHOTOS | &quot;PHOTOS&quot; |
| STREET_VIEW | &quot;STREET_VIEW&quot; |
| SHOPPING | &quot;SHOPPING&quot; |
| GEO | &quot;GEO&quot; |
| GENERATIVE_AI | &quot;GENERATIVE_AI&quot; |



