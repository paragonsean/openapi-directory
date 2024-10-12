# PolicyStatesClient.PolicyState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**odataContext** | **String** | OData context string; used by OData clients to resolve type information based on metadata. | [optional] 
**odataId** | **String** | OData entity ID; always set to null since policy state records do not have an entity ID. | [optional] 
**complianceState** | **String** | Compliance state of the resource. | [optional] 
**effectiveParameters** | **String** | Effective parameters for the policy assignment. | [optional] 
**isCompliant** | **Boolean** | Flag which states whether the resource is compliant against the policy assignment it was evaluated against. | [optional] 
**managementGroupIds** | **String** | Comma separated list of management group IDs, which represent the hierarchy of the management groups the resource is under. | [optional] 
**policyAssignmentId** | **String** | Policy assignment ID. | [optional] 
**policyAssignmentName** | **String** | Policy assignment name. | [optional] 
**policyAssignmentOwner** | **String** | Policy assignment owner. | [optional] 
**policyAssignmentParameters** | **String** | Policy assignment parameters. | [optional] 
**policyAssignmentScope** | **String** | Policy assignment scope. | [optional] 
**policyDefinitionAction** | **String** | Policy definition action, i.e. effect. | [optional] 
**policyDefinitionCategory** | **String** | Policy definition category. | [optional] 
**policyDefinitionId** | **String** | Policy definition ID. | [optional] 
**policyDefinitionName** | **String** | Policy definition name. | [optional] 
**policyDefinitionReferenceId** | **String** | Reference ID for the policy definition inside the policy set, if the policy assignment is for a policy set. | [optional] 
**policyEvaluationDetails** | [**PolicyEvaluationDetails**](PolicyEvaluationDetails.md) |  | [optional] 
**policySetDefinitionCategory** | **String** | Policy set definition category, if the policy assignment is for a policy set. | [optional] 
**policySetDefinitionId** | **String** | Policy set definition ID, if the policy assignment is for a policy set. | [optional] 
**policySetDefinitionName** | **String** | Policy set definition name, if the policy assignment is for a policy set. | [optional] 
**policySetDefinitionOwner** | **String** | Policy set definition owner, if the policy assignment is for a policy set. | [optional] 
**policySetDefinitionParameters** | **String** | Policy set definition parameters, if the policy assignment is for a policy set. | [optional] 
**resourceGroup** | **String** | Resource group name. | [optional] 
**resourceId** | **String** | Resource ID. | [optional] 
**resourceLocation** | **String** | Resource location. | [optional] 
**resourceTags** | **String** | List of resource tags. | [optional] 
**resourceType** | **String** | Resource type. | [optional] 
**subscriptionId** | **String** | Subscription ID. | [optional] 
**timestamp** | **Date** | Timestamp for the policy state record. | [optional] 


