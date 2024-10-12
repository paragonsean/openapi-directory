# BigQueryConnectionApi.AzureProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **String** | Output only. The name of the Azure Active Directory Application. | [optional] [readonly] 
**clientId** | **String** | Output only. The client id of the Azure Active Directory Application. | [optional] [readonly] 
**customerTenantId** | **String** | The id of customer&#39;s directory that host the data. | [optional] 
**federatedApplicationClientId** | **String** | The client ID of the user&#39;s Azure Active Directory Application used for a federated connection. | [optional] 
**identity** | **String** | Output only. A unique Google-owned and Google-generated identity for the Connection. This identity will be used to access the user&#39;s Azure Active Directory Application. | [optional] [readonly] 
**objectId** | **String** | Output only. The object id of the Azure Active Directory Application. | [optional] [readonly] 
**redirectUri** | **String** | The URL user will be redirected to after granting consent during connection setup. | [optional] 


