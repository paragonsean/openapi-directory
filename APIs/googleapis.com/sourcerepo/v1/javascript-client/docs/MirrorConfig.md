# CloudSourceRepositoriesApi.MirrorConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployKeyId** | **String** | ID of the SSH deploy key at the other hosting service. Removing this key from the other service would deauthorize Google Cloud Source Repositories from mirroring. | [optional] 
**url** | **String** | URL of the main repository at the other hosting service. | [optional] 
**webhookId** | **String** | ID of the webhook listening to updates to trigger mirroring. Removing this webhook from the other hosting service will stop Google Cloud Source Repositories from receiving notifications, and thereby disabling mirroring. | [optional] 


