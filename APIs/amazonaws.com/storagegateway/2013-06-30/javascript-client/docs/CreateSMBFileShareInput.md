# AwsStorageGateway.CreateSMBFileShareInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** |  | 
**gatewayARN** | **String** |  | 
**kMSEncrypted** | **Boolean** |  | [optional] 
**kMSKey** | **String** |  | [optional] 
**role** | **String** |  | 
**locationARN** | **String** |  | 
**defaultStorageClass** | **String** |  | [optional] 
**objectACL** | [**ObjectACL**](ObjectACL.md) |  | [optional] 
**readOnly** | **Boolean** |  | [optional] 
**guessMIMETypeEnabled** | **Boolean** |  | [optional] 
**requesterPays** | **Boolean** |  | [optional] 
**sMBACLEnabled** | **Boolean** |  | [optional] 
**accessBasedEnumeration** | **Boolean** |  | [optional] 
**adminUserList** | **Array** |  | [optional] 
**validUserList** | **Array** |  | [optional] 
**invalidUserList** | **Array** |  | [optional] 
**auditDestinationARN** | **String** |  | [optional] 
**authentication** | **String** |  | [optional] 
**caseSensitivity** | [**CaseSensitivity**](CaseSensitivity.md) |  | [optional] 
**tags** | **Array** |  | [optional] 
**fileShareName** | **String** |  | [optional] 
**cacheAttributes** | [**CreateNFSFileShareInputCacheAttributes**](CreateNFSFileShareInputCacheAttributes.md) |  | [optional] 
**notificationPolicy** | **String** |  | [optional] 
**vPCEndpointDNSName** | **String** |  | [optional] 
**bucketRegion** | **String** |  | [optional] 
**oplocksEnabled** | **Boolean** |  | [optional] 


