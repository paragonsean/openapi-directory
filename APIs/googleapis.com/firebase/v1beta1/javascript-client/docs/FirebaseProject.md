# FirebaseManagementApi.FirebaseProject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | A set of user-defined annotations for the FirebaseProject. Learn more about annotations in Google&#39;s [AIP-128 standard](https://google.aip.dev/128#annotations). These annotations are intended solely for developers and client-side tools. Firebase services will not mutate this annotations set. | [optional] 
**displayName** | **String** | The user-assigned display name of the Project. | [optional] 
**etag** | **String** | This checksum is computed by the server based on the value of other fields, and it may be sent with update requests to ensure the client has an up-to-date value before proceeding. Learn more about &#x60;etag&#x60; in Google&#39;s [AIP-154 standard](https://google.aip.dev/154#declarative-friendly-resources). This etag is strongly validated. | [optional] 
**name** | **String** | The resource name of the Project, in the format: projects/PROJECT_IDENTIFIER PROJECT_IDENTIFIER: the Project&#39;s [&#x60;ProjectNumber&#x60;](../projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [&#x60;ProjectId&#x60;](../projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google&#39;s [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for PROJECT_IDENTIFIER in any response body will be the &#x60;ProjectId&#x60;. | [optional] 
**projectId** | **String** | Output only. Immutable. A user-assigned unique identifier for the Project. This identifier may appear in URLs or names for some Firebase resources associated with the Project, but it should generally be treated as a convenience alias to reference the Project. | [optional] [readonly] 
**projectNumber** | **String** | Output only. Immutable. The globally unique, Google-assigned canonical identifier for the Project. Use this identifier when configuring integrations and/or making API calls to Firebase or third-party services. | [optional] [readonly] 
**resources** | [**DefaultResources**](DefaultResources.md) |  | [optional] 
**state** | **String** | Output only. The lifecycle state of the Project. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETED` (value: `"DELETED"`)




