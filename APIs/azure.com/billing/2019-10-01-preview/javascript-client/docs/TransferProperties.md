# BillingManagementClient.TransferProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAccountId** | **String** | Target billing account Id. | [optional] [readonly] 
**billingProfileId** | **String** | Target billing profile Id. | [optional] [readonly] 
**canceledBy** | **String** | Email Id who user canceled the transfer. | [optional] [readonly] 
**creationTime** | **Date** | Transfer creation time. | [optional] [readonly] 
**detailedTransferStatus** | [**[DetailedTransferStatus]**](DetailedTransferStatus.md) | Detailed transfer status. | [optional] [readonly] 
**expirationTime** | **Date** | Transfer expiration time. | [optional] [readonly] 
**initiatorCustomerType** | **String** | Customer type of the initiator. | [optional] [readonly] 
**initiatorEmailId** | **String** | Email Id of initiator of transfer. | [optional] [readonly] 
**invoiceSectionId** | **String** | Target invoice section Id. | [optional] [readonly] 
**lastModifiedTime** | **Date** | Transfer last modification time. | [optional] [readonly] 
**recipientEmailId** | **String** | Email Id of recipient of transfer. | [optional] [readonly] 
**resellerId** | **String** | Reseller Id for transfer. | [optional] [readonly] 
**resellerName** | **String** | Reseller name for transfer. | [optional] [readonly] 
**transferStatus** | [**TransferStatus**](TransferStatus.md) |  | [optional] 


