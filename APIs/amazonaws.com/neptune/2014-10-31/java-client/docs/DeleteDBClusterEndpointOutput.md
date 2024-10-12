

# DeleteDBClusterEndpointOutput

<p>This data type represents the information you need to connect to an Amazon Neptune DB cluster. This data type is used as a response element in the following actions:</p> <ul> <li> <p> <code>CreateDBClusterEndpoint</code> </p> </li> <li> <p> <code>DescribeDBClusterEndpoints</code> </p> </li> <li> <p> <code>ModifyDBClusterEndpoint</code> </p> </li> <li> <p> <code>DeleteDBClusterEndpoint</code> </p> </li> </ul> <p>For the data structure that represents Amazon RDS DB instance endpoints, see <code>Endpoint</code>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dbClusterEndpointIdentifier** | [**String**](String.md) |  |  [optional] |
|**dbClusterIdentifier** | [**String**](String.md) |  |  [optional] |
|**dbClusterEndpointResourceIdentifier** | [**String**](String.md) |  |  [optional] |
|**endpoint** | [**String**](String.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**endpointType** | [**String**](String.md) |  |  [optional] |
|**customEndpointType** | [**String**](String.md) |  |  [optional] |
|**staticMembers** | [**List**](List.md) |  |  [optional] |
|**excludedMembers** | [**List**](List.md) |  |  [optional] |
|**dbClusterEndpointArn** | [**String**](String.md) |  |  [optional] |



