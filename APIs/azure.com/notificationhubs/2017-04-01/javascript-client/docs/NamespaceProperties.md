# NotificationHubsManagementClient.NamespaceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | The time the namespace was created. | [optional] 
**critical** | **Boolean** | Whether or not the namespace is set as Critical. | [optional] 
**dataCenter** | **String** | Data center for the namespace | [optional] 
**enabled** | **Boolean** | Whether or not the namespace is currently enabled. | [optional] 
**metricId** | **String** | Identifier for Azure Insights metrics | [optional] [readonly] 
**name** | **String** | The name of the namespace. | [optional] 
**namespaceType** | **String** | The namespace type. | [optional] 
**provisioningState** | **String** | Provisioning state of the Namespace. | [optional] 
**region** | **String** | Specifies the targeted region in which the namespace should be created. It can be any of the following values: Australia East, Australia Southeast, Central US, East US, East US 2, West US, North Central US, South Central US, East Asia, Southeast Asia, Brazil South, Japan East, Japan West, North Europe, West Europe | [optional] 
**scaleUnit** | **String** | ScaleUnit where the namespace gets created | [optional] 
**serviceBusEndpoint** | **String** | Endpoint you can use to perform NotificationHub operations. | [optional] 
**status** | **String** | Status of the namespace. It can be any of these values:1 &#x3D; Created/Active2 &#x3D; Creating3 &#x3D; Suspended4 &#x3D; Deleting | [optional] 
**subscriptionId** | **String** | The Id of the Azure subscription associated with the namespace. | [optional] 
**updatedAt** | **Date** | The time the namespace was updated. | [optional] 



## Enum: NamespaceTypeEnum


* `Messaging` (value: `"Messaging"`)

* `NotificationHub` (value: `"NotificationHub"`)




