

# CertificateAttributes

The certificate management attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**recoveryLevel** | [**RecoveryLevelEnum**](#RecoveryLevelEnum) | Reflects the deletion recovery level currently in effect for certificates in the current vault. If it contains &#39;Purgeable&#39;, the certificate can be permanently deleted by a privileged user; otherwise, only the system can purge the certificate, at the end of the retention interval. |  [optional] [readonly] |
|**created** | **Integer** | Creation time in UTC. |  [optional] [readonly] |
|**enabled** | **Boolean** | Determines whether the object is enabled. |  [optional] |
|**exp** | **Integer** | Expiry date in UTC. |  [optional] |
|**nbf** | **Integer** | Not before date in UTC. |  [optional] |
|**updated** | **Integer** | Last updated time in UTC. |  [optional] [readonly] |



## Enum: RecoveryLevelEnum

| Name | Value |
|---- | -----|
| PURGEABLE | &quot;Purgeable&quot; |
| RECOVERABLE_PURGEABLE | &quot;Recoverable+Purgeable&quot; |
| RECOVERABLE | &quot;Recoverable&quot; |
| RECOVERABLE_PROTECTED_SUBSCRIPTION | &quot;Recoverable+ProtectedSubscription&quot; |



