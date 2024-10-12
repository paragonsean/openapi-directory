

# EndpointAuthorization

Describes an endpoint authorization for authorizing Redshift-managed VPC endpoint access to a cluster across Amazon Web Services accounts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**grantor** | [**String**](String.md) |  |  [optional] |
|**grantee** | [**String**](String.md) |  |  [optional] |
|**clusterIdentifier** | [**String**](String.md) |  |  [optional] |
|**authorizeTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**clusterStatus** | [**String**](String.md) |  |  [optional] |
|**status** | [**AuthorizationStatus**](AuthorizationStatus.md) |  |  [optional] |
|**allowedAllVPCs** | [**Boolean**](Boolean.md) |  |  [optional] |
|**allowedVPCs** | [**List**](List.md) |  |  [optional] |
|**endpointCount** | [**Integer**](Integer.md) |  |  [optional] |



