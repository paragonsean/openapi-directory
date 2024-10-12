

# ImportExport

The structure that can be imported to or exported from Otoroshi. It represent the memory state of Otoroshi

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**admins** | [**List&lt;ImportExportAdminsInner&gt;**](ImportExportAdminsInner.md) | Current U2F admin at the time of export |  |
|**apiKeys** | [**List&lt;ImportExportApiKeysInner&gt;**](ImportExportApiKeysInner.md) | Current apik keys at the time of export |  |
|**appConfig** | **Map&lt;String, String&gt;** | Current env variables at the time of export |  [optional] |
|**config** | [**GlobalConfig**](GlobalConfig.md) |  |  |
|**date** | **OffsetDateTime** |  |  |
|**dateRaw** | **Long** |  |  |
|**errorTemplates** | [**List&lt;ImportExportErrorTemplatesInner&gt;**](ImportExportErrorTemplatesInner.md) | Current error templates at the time of export |  |
|**label** | **String** |  |  |
|**serviceDescriptors** | [**List&lt;ImportExportServiceDescriptorsInner&gt;**](ImportExportServiceDescriptorsInner.md) | Current service descriptors at the time of export |  |
|**serviceGroups** | [**List&lt;ImportExportServiceGroupsInner&gt;**](ImportExportServiceGroupsInner.md) | Current service groups at the time of export |  |
|**simpleAdmins** | [**List&lt;ImportExportSimpleAdminsInner&gt;**](ImportExportSimpleAdminsInner.md) | Current simple admins at the time of export |  |
|**stats** | [**ImportExportStats**](ImportExportStats.md) |  |  |



