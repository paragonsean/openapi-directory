

# GETCreateStackInstancesDeploymentTargetsParameter

<p>[Service-managed permissions] The Organizations accounts to which StackSets deploys. StackSets doesn't deploy stack instances to the organization management account, even if the organization management account is in your organization or in an OU in your organization.</p> <p>For update operations, you can specify either <code>Accounts</code> or <code>OrganizationalUnitIds</code>. For create and delete operations, specify <code>OrganizationalUnitIds</code>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accounts** | [**List**](List.md) |  |  [optional] |
|**accountsUrl** | [**String**](String.md) |  |  [optional] |
|**organizationalUnitIds** | [**List**](List.md) |  |  [optional] |
|**accountFilterType** | [**AccountFilterType**](AccountFilterType.md) |  |  [optional] |



