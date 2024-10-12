

# CreateBackupSelectionRequestBackupSelection

<p>Used to specify a set of resources to a backup plan.</p> <p>Specifying your desired <code>Conditions</code>, <code>ListOfTags</code>, <code>NotResources</code>, and/or <code>Resources</code> is recommended. If none of these are specified, Backup will attempt to select all supported and opted-in storage resources, which could have unintended cost implications.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**selectionName** | [**String**](String.md) |  |  [optional] |
|**iamRoleArn** | [**String**](String.md) |  |  [optional] |
|**resources** | [**List**](List.md) |  |  [optional] |
|**listOfTags** | [**List**](List.md) |  |  [optional] |
|**notResources** | [**List**](List.md) |  |  [optional] |
|**conditions** | [**CreateBackupSelectionRequestBackupSelectionConditions**](CreateBackupSelectionRequestBackupSelectionConditions.md) |  |  [optional] |



