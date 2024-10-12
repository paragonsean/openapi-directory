# TagManagerApi.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The Account ID uniquely identifies the GTM Account. | [optional] 
**features** | [**AccountFeatures**](AccountFeatures.md) |  | [optional] 
**fingerprint** | **String** | The fingerprint of the GTM Account as computed at storage time. This value is recomputed whenever the account is modified. | [optional] 
**name** | **String** | Account display name. @mutable tagmanager.accounts.create @mutable tagmanager.accounts.update | [optional] 
**path** | **String** | GTM Account&#39;s API relative path. | [optional] 
**shareData** | **Boolean** | Whether the account shares data anonymously with Google and others. This flag enables benchmarking by sharing your data in an anonymous form. Google will remove all identifiable information about your website, combine the data with hundreds of other anonymous sites and report aggregate trends in the benchmarking service. @mutable tagmanager.accounts.create @mutable tagmanager.accounts.update | [optional] 
**tagManagerUrl** | **String** | Auto generated link to the tag manager UI | [optional] 


