

# GenerateConfigReportRequest

Request message for GenerateConfigReport method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**newConfig** | **Map&lt;String, Object&gt;** | Required. Service configuration for which we want to generate the report. For this version of API, the supported types are google.api.servicemanagement.v1.ConfigRef, google.api.servicemanagement.v1.ConfigSource, and google.api.Service |  [optional] |
|**oldConfig** | **Map&lt;String, Object&gt;** | Optional. Service configuration against which the comparison will be done. For this version of API, the supported types are google.api.servicemanagement.v1.ConfigRef, google.api.servicemanagement.v1.ConfigSource, and google.api.Service |  [optional] |



