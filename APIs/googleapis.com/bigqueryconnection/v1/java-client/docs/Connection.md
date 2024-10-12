

# Connection

Configuration parameters to establish connection with an external data source, except the credential attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aws** | [**AwsProperties**](AwsProperties.md) |  |  [optional] |
|**azure** | [**AzureProperties**](AzureProperties.md) |  |  [optional] |
|**cloudResource** | [**CloudResourceProperties**](CloudResourceProperties.md) |  |  [optional] |
|**cloudSpanner** | [**CloudSpannerProperties**](CloudSpannerProperties.md) |  |  [optional] |
|**cloudSql** | [**CloudSqlProperties**](CloudSqlProperties.md) |  |  [optional] |
|**_configuration** | [**ConnectorConfiguration**](ConnectorConfiguration.md) |  |  [optional] |
|**creationTime** | **String** | Output only. The creation timestamp of the connection. |  [optional] [readonly] |
|**description** | **String** | User provided description. |  [optional] |
|**friendlyName** | **String** | User provided display name for the connection. |  [optional] |
|**hasCredential** | **Boolean** | Output only. True, if credential is configured for this connection. |  [optional] [readonly] |
|**kmsKeyName** | **String** | Optional. The Cloud KMS key that is used for encryption. Example: &#x60;projects/[kms_project_id]/locations/[region]/keyRings/[key_region]/cryptoKeys/[key]&#x60; |  [optional] |
|**lastModifiedTime** | **String** | Output only. The last update timestamp of the connection. |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name of the connection in the form of: &#x60;projects/{project_id}/locations/{location_id}/connections/{connection_id}&#x60; |  [optional] [readonly] |
|**salesforceDataCloud** | [**SalesforceDataCloudProperties**](SalesforceDataCloudProperties.md) |  |  [optional] |
|**spark** | [**SparkProperties**](SparkProperties.md) |  |  [optional] |



