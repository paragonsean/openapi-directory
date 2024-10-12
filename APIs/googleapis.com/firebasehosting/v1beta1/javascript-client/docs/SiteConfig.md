# FirebaseHostingApi.SiteConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudLoggingEnabled** | **Boolean** | Whether or not web requests made by site visitors are logged via Cloud Logging. | [optional] 
**maxVersions** | **String** | The number of FINALIZED versions that will be held for a site before automatic deletion. When a new version is deployed, content for versions in storage in excess of this number will be deleted, and will no longer be billed for storage usage. Oldest versions will be deleted first; sites are created with an unlimited number of max_versions by default. | [optional] 


