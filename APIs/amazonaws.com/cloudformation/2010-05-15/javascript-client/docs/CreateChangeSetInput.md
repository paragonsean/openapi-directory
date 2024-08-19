# AwsCloudFormation.CreateChangeSetInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stackName** | **String** |  | 
**templateBody** | **String** |  | [optional] 
**templateURL** | **String** |  | [optional] 
**usePreviousTemplate** | **Boolean** |  | [optional] 
**parameters** | **Array** |  | [optional] 
**capabilities** | **Array** |  | [optional] 
**resourceTypes** | **Array** |  | [optional] 
**roleARN** | **String** |  | [optional] 
**rollbackConfiguration** | [**DescribeChangeSetOutputRollbackConfiguration**](DescribeChangeSetOutputRollbackConfiguration.md) |  | [optional] 
**notificationARNs** | **Array** |  | [optional] 
**tags** | **Array** |  | [optional] 
**changeSetName** | **String** |  | 
**clientToken** | **String** |  | [optional] 
**description** | **String** |  | [optional] 
**changeSetType** | [**ChangeSetType**](ChangeSetType.md) |  | [optional] 
**resourcesToImport** | **Array** |  | [optional] 
**includeNestedStacks** | **Boolean** |  | [optional] 
**onStackFailure** | [**OnStackFailure**](OnStackFailure.md) |  | [optional] 


