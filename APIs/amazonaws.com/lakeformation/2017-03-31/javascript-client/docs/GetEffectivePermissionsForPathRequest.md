# AwsLakeFormation.GetEffectivePermissionsForPathRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalogId** | **String** | The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.  | [optional] 
**resourceArn** | **String** | The Amazon Resource Name (ARN) of the resource for which you want to get permissions. | 
**nextToken** | **String** | A continuation token, if this is not the first call to retrieve this list. | [optional] 
**maxResults** | **Number** | The maximum number of results to return. | [optional] 


