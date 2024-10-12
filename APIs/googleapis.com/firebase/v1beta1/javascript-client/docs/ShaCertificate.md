# FirebaseManagementApi.ShaCertificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certType** | **String** | The type of SHA certificate encoded in the hash. | [optional] 
**name** | **String** | The resource name of the ShaCertificate for the AndroidApp, in the format: projects/PROJECT_IDENTIFIER/androidApps/APP_ID/sha/SHA_HASH * PROJECT_IDENTIFIER: the parent Project&#39;s [&#x60;ProjectNumber&#x60;](../projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [&#x60;ProjectId&#x60;](../projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google&#39;s [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for PROJECT_IDENTIFIER in any response body will be the &#x60;ProjectId&#x60;. * APP_ID: the globally unique, Firebase-assigned identifier for the App (see [&#x60;appId&#x60;](../projects.androidApps#AndroidApp.FIELDS.app_id)). * SHA_HASH: the certificate hash for the App (see [&#x60;shaHash&#x60;](../projects.androidApps.sha#ShaCertificate.FIELDS.sha_hash)). | [optional] 
**shaHash** | **String** | The certificate hash for the &#x60;AndroidApp&#x60;. | [optional] 



## Enum: CertTypeEnum


* `CERTIFICATE_TYPE_UNSPECIFIED` (value: `"SHA_CERTIFICATE_TYPE_UNSPECIFIED"`)

* `1` (value: `"SHA_1"`)

* `256` (value: `"SHA_256"`)




