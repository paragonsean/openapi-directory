# CloudSearchApi.AuditLoggingSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logAdminReadActions** | **Boolean** | Indicates whether audit logging is on/off for admin activity read APIs i.e. Get/List DataSources, Get/List SearchApplications etc. | [optional] 
**logDataReadActions** | **Boolean** | Indicates whether audit logging is on/off for data access read APIs i.e. ListItems, GetItem etc. | [optional] 
**logDataWriteActions** | **Boolean** | Indicates whether audit logging is on/off for data access write APIs i.e. IndexItem etc. | [optional] 
**project** | **String** | The resource name of the GCP Project to store audit logs. Cloud audit logging will be enabled after project_name has been updated through CustomerService. Format: projects/{project_id} | [optional] 


