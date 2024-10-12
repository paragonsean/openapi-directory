# FirebaseManagementApi.FirebaseAppInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiKeyId** | **String** | The globally unique, Google-assigned identifier (UID) for the Firebase API key associated with the App. Be aware that this value is the UID of the API key, _not_ the [&#x60;keyString&#x60;](https://cloud.google.com/api-keys/docs/reference/rest/v2/projects.locations.keys#Key.FIELDS.key_string) of the API key. The &#x60;keyString&#x60; is the value that can be found in the App&#39;s configuration artifact ([&#x60;AndroidApp&#x60;](../../rest/v1beta1/projects.androidApps/getConfig) | [&#x60;IosApp&#x60;](../../rest/v1beta1/projects.iosApps/getConfig) | [&#x60;WebApp&#x60;](../../rest/v1beta1/projects.webApps/getConfig)). If &#x60;api_key_id&#x60; is not set in requests to create the App ([&#x60;AndroidApp&#x60;](../../rest/v1beta1/projects.androidApps/create) | [&#x60;IosApp&#x60;](../../rest/v1beta1/projects.iosApps/create) | [&#x60;WebApp&#x60;](../../rest/v1beta1/projects.webApps/create)), then Firebase automatically associates an &#x60;api_key_id&#x60; with the App. This auto-associated key may be an existing valid key or, if no valid key exists, a new one will be provisioned. | [optional] 
**appId** | **String** | Output only. Immutable. The globally unique, Firebase-assigned identifier for the &#x60;WebApp&#x60;. This identifier should be treated as an opaque token, as the data format is not specified. | [optional] [readonly] 
**displayName** | **String** | The user-assigned display name of the Firebase App. | [optional] 
**expireTime** | **String** | Output only. Timestamp of when the App will be considered expired and cannot be undeleted. This value is only provided if the App is in the &#x60;DELETED&#x60; state. | [optional] [readonly] 
**name** | **String** | The resource name of the Firebase App, in the format: projects/PROJECT_ID /iosApps/APP_ID or projects/PROJECT_ID/androidApps/APP_ID or projects/ PROJECT_ID/webApps/APP_ID | [optional] 
**namespace** | **String** | Output only. Immutable. The platform-specific identifier of the App. *Note:* For most use cases, use &#x60;appId&#x60;, which is the canonical, globally unique identifier for referencing an App. This string is derived from a native identifier for each platform: &#x60;packageName&#x60; for an &#x60;AndroidApp&#x60;, &#x60;bundleId&#x60; for an &#x60;IosApp&#x60;, and &#x60;webId&#x60; for a &#x60;WebApp&#x60;. Its contents should be treated as opaque, as the native identifier format may change as platforms evolve. This string is only unique within a &#x60;FirebaseProject&#x60; and its associated Apps. | [optional] [readonly] 
**platform** | **String** | The platform of the Firebase App. | [optional] 
**state** | **String** | Output only. The lifecycle state of the App. | [optional] [readonly] 



## Enum: PlatformEnum


* `PLATFORM_UNSPECIFIED` (value: `"PLATFORM_UNSPECIFIED"`)

* `IOS` (value: `"IOS"`)

* `ANDROID` (value: `"ANDROID"`)

* `WEB` (value: `"WEB"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETED` (value: `"DELETED"`)




