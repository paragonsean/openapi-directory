# WebSiteManagementClient.CsmSiteRecoveryEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recoverConfig** | **Boolean** | If true, then the website&#39;s configuration will be reverted to its state at SnapshotTime | [optional] 
**siteName** | **String** | [Optional] Destination web app name into which web app should be recovered. This is case when new web app should be created instead. | [optional] 
**slotName** | **String** | [Optional] Destination web app slot name into which web app should be recovered | [optional] 
**snapshotTime** | **Date** | Point in time in which the site recover should be attempted. | [optional] 


