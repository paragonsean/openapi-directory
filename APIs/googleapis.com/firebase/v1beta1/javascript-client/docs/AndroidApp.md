# FirebaseManagementApi.AndroidApp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiKeyId** | **String** | The globally unique, Google-assigned identifier (UID) for the Firebase API key associated with the &#x60;AndroidApp&#x60;. Be aware that this value is the UID of the API key, _not_ the [&#x60;keyString&#x60;](https://cloud.google.com/api-keys/docs/reference/rest/v2/projects.locations.keys#Key.FIELDS.key_string) of the API key. The &#x60;keyString&#x60; is the value that can be found in the App&#39;s [configuration artifact](../../rest/v1beta1/projects.androidApps/getConfig). If &#x60;api_key_id&#x60; is not set in requests to [&#x60;androidApps.Create&#x60;](../../rest/v1beta1/projects.androidApps/create), then Firebase automatically associates an &#x60;api_key_id&#x60; with the &#x60;AndroidApp&#x60;. This auto-associated key may be an existing valid key or, if no valid key exists, a new one will be provisioned. In patch requests, &#x60;api_key_id&#x60; cannot be set to an empty value, and the new UID must have no restrictions or only have restrictions that are valid for the associated &#x60;AndroidApp&#x60;. We recommend using the [Google Cloud Console](https://console.cloud.google.com/apis/credentials) to manage API keys. | [optional] 
**appId** | **String** | Output only. Immutable. The globally unique, Firebase-assigned identifier for the &#x60;AndroidApp&#x60;. This identifier should be treated as an opaque token, as the data format is not specified. | [optional] [readonly] 
**displayName** | **String** | The user-assigned display name for the &#x60;AndroidApp&#x60;. | [optional] 
**etag** | **String** | This checksum is computed by the server based on the value of other fields, and it may be sent with update requests to ensure the client has an up-to-date value before proceeding. Learn more about &#x60;etag&#x60; in Google&#39;s [AIP-154 standard](https://google.aip.dev/154#declarative-friendly-resources). This etag is strongly validated. | [optional] 
**expireTime** | **String** | Output only. Timestamp of when the App will be considered expired and cannot be undeleted. This value is only provided if the App is in the &#x60;DELETED&#x60; state. | [optional] [readonly] 
**name** | **String** | The resource name of the AndroidApp, in the format: projects/ PROJECT_IDENTIFIER/androidApps/APP_ID * PROJECT_IDENTIFIER: the parent Project&#39;s [&#x60;ProjectNumber&#x60;](../projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [&#x60;ProjectId&#x60;](../projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google&#39;s [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for PROJECT_IDENTIFIER in any response body will be the &#x60;ProjectId&#x60;. * APP_ID: the globally unique, Firebase-assigned identifier for the App (see [&#x60;appId&#x60;](../projects.androidApps#AndroidApp.FIELDS.app_id)). | [optional] 
**packageName** | **String** | Immutable. The canonical package name of the Android app as would appear in the Google Play Developer Console. | [optional] 
**projectId** | **String** | Output only. Immutable. A user-assigned unique identifier of the parent FirebaseProject for the &#x60;AndroidApp&#x60;. | [optional] [readonly] 
**sha1Hashes** | **[String]** | The SHA1 certificate hashes for the AndroidApp. | [optional] 
**sha256Hashes** | **[String]** | The SHA256 certificate hashes for the AndroidApp. | [optional] 
**state** | **String** | Output only. The lifecycle state of the App. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETED` (value: `"DELETED"`)




