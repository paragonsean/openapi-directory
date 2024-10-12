

# ResourceDataSyncSourceWithState

<p>The data type name for including resource data sync state. There are four sync states:</p> <p> <code>OrganizationNotExists</code> (Your organization doesn't exist)</p> <p> <code>NoPermissions</code> (The system can't locate the service-linked role. This role is automatically created when a user creates a resource data sync in Amazon Web Services Systems Manager Explorer.)</p> <p> <code>InvalidOrganizationalUnit</code> (You specified or selected an invalid unit in the resource data sync configuration.)</p> <p> <code>TrustedAccessDisabled</code> (You disabled Systems Manager access in the organization in Organizations.)</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sourceType** | [**String**](String.md) |  |  [optional] |
|**awsOrganizationsSource** | [**ResourceDataSyncSourceWithStateAwsOrganizationsSource**](ResourceDataSyncSourceWithStateAwsOrganizationsSource.md) |  |  [optional] |
|**sourceRegions** | [**List**](List.md) |  |  [optional] |
|**includeFutureRegions** | [**Boolean**](Boolean.md) |  |  [optional] |
|**state** | [**String**](String.md) |  |  [optional] |
|**enableAllOpsDataSources** | [**Boolean**](Boolean.md) |  |  [optional] |



