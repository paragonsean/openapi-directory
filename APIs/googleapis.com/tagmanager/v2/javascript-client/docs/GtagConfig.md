# TagManagerApi.GtagConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Google tag account ID. | [optional] 
**containerId** | **String** | Google tag container ID. | [optional] 
**fingerprint** | **String** | The fingerprint of the Google tag config as computed at storage time. This value is recomputed whenever the config is modified. | [optional] 
**gtagConfigId** | **String** | The ID uniquely identifies the Google tag config. | [optional] 
**parameter** | [**[Parameter]**](Parameter.md) | The Google tag config&#39;s parameters. @mutable tagmanager.accounts.containers.workspaces.gtag_config.create @mutable tagmanager.accounts.containers.workspaces.gtag_config.update | [optional] 
**path** | **String** | Google tag config&#39;s API relative path. | [optional] 
**tagManagerUrl** | **String** | Auto generated link to the tag manager UI | [optional] 
**type** | **String** | Google tag config type. @required tagmanager.accounts.containers.workspaces.gtag_config.create @required tagmanager.accounts.containers.workspaces.gtag_config.update @mutable tagmanager.accounts.containers.workspaces.gtag_config.create @mutable tagmanager.accounts.containers.workspaces.gtag_config.update | [optional] 
**workspaceId** | **String** | Google tag workspace ID. Only used by GTM containers. Set to 0 otherwise. | [optional] 


