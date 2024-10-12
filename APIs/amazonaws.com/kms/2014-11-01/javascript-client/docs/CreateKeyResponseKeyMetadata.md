# AwsKeyManagementService.CreateKeyResponseKeyMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aWSAccountId** | **String** |  | [optional] 
**keyId** | **String** |  | 
**arn** | **String** |  | [optional] 
**creationDate** | **Date** |  | [optional] 
**enabled** | **Boolean** |  | [optional] 
**description** | **String** |  | [optional] 
**keyUsage** | [**KeyUsageType**](KeyUsageType.md) |  | [optional] 
**keyState** | [**KeyState**](KeyState.md) |  | [optional] 
**deletionDate** | **Date** |  | [optional] 
**validTo** | **Date** |  | [optional] 
**origin** | [**OriginType**](OriginType.md) |  | [optional] 
**customKeyStoreId** | **String** |  | [optional] 
**cloudHsmClusterId** | **String** |  | [optional] 
**expirationModel** | [**ExpirationModelType**](ExpirationModelType.md) |  | [optional] 
**keyManager** | [**KeyManagerType**](KeyManagerType.md) |  | [optional] 
**customerMasterKeySpec** | [**CustomerMasterKeySpec**](CustomerMasterKeySpec.md) |  | [optional] 
**keySpec** | [**KeySpec**](KeySpec.md) |  | [optional] 
**encryptionAlgorithms** | **Array** |  | [optional] 
**signingAlgorithms** | **Array** |  | [optional] 
**multiRegion** | **Boolean** |  | [optional] 
**multiRegionConfiguration** | [**KeyMetadataMultiRegionConfiguration**](KeyMetadataMultiRegionConfiguration.md) |  | [optional] 
**pendingDeletionWindowInDays** | **Number** |  | [optional] 
**macAlgorithms** | **Array** |  | [optional] 
**xksKeyConfiguration** | [**KeyMetadataXksKeyConfiguration**](KeyMetadataXksKeyConfiguration.md) |  | [optional] 


