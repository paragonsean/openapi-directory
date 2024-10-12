

# Account

Represents a Google Tag Manager Account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The Account ID uniquely identifies the GTM Account. |  [optional] |
|**fingerprint** | **String** | The fingerprint of the GTM Account as computed at storage time. This value is recomputed whenever the account is modified. |  [optional] |
|**name** | **String** | Account display name. @mutable tagmanager.accounts.create @mutable tagmanager.accounts.update |  [optional] |
|**shareData** | **Boolean** | Whether the account shares data anonymously with Google and others. @mutable tagmanager.accounts.create @mutable tagmanager.accounts.update |  [optional] |



