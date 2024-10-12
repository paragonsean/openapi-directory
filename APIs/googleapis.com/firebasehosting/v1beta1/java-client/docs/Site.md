

# Site

A `Site` represents a Firebase Hosting site.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | Optional. The [ID of a Web App](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps#WebApp.FIELDS.app_id) associated with the Hosting site. |  [optional] |
|**defaultUrl** | **String** | Output only. The default URL for the Hosting site. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Optional. User-specified labels for the Hosting site. |  [optional] |
|**name** | **String** | Output only. The fully-qualified resource name of the Hosting site, in the format: projects/PROJECT_IDENTIFIER/sites/SITE_ID PROJECT_IDENTIFIER: the Firebase project&#39;s [&#x60;ProjectNumber&#x60;](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [&#x60;ProjectId&#x60;](https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google&#39;s [AIP 2510 standard](https://google.aip.dev/cloud/2510). |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The type of Hosting site. Every Firebase project has a &#x60;DEFAULT_SITE&#x60;, which is created when Hosting is provisioned for the project. All additional sites are &#x60;USER_SITE&#x60;. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| DEFAULT_SITE | &quot;DEFAULT_SITE&quot; |
| USER_SITE | &quot;USER_SITE&quot; |



