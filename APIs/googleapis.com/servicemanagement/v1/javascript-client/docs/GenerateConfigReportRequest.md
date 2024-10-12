# ServiceManagementApi.GenerateConfigReportRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**newConfig** | **{String: Object}** | Required. Service configuration for which we want to generate the report. For this version of API, the supported types are google.api.servicemanagement.v1.ConfigRef, google.api.servicemanagement.v1.ConfigSource, and google.api.Service | [optional] 
**oldConfig** | **{String: Object}** | Optional. Service configuration against which the comparison will be done. For this version of API, the supported types are google.api.servicemanagement.v1.ConfigRef, google.api.servicemanagement.v1.ConfigSource, and google.api.Service | [optional] 


