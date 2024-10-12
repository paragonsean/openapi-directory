

# ContinuousDeploymentSingleHeaderConfig

This configuration determines which HTTP requests are sent to the staging distribution. If the HTTP request contains a header and value that matches what you specify here, the request is sent to the staging distribution. Otherwise the request is sent to the primary distribution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**header** | [**String**](String.md) |  |  |
|**value** | [**String**](String.md) |  |  |



