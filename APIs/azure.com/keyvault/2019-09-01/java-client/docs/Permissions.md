

# Permissions

Permissions the identity has for keys, secrets, certificates and storage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificates** | [**List&lt;CertificatesEnum&gt;**](#List&lt;CertificatesEnum&gt;) | Permissions to certificates |  [optional] |
|**keys** | [**List&lt;KeysEnum&gt;**](#List&lt;KeysEnum&gt;) | Permissions to keys |  [optional] |
|**secrets** | [**List&lt;SecretsEnum&gt;**](#List&lt;SecretsEnum&gt;) | Permissions to secrets |  [optional] |
|**storage** | [**List&lt;StorageEnum&gt;**](#List&lt;StorageEnum&gt;) | Permissions to storage accounts |  [optional] |



## Enum: List&lt;CertificatesEnum&gt;

| Name | Value |
|---- | -----|
| GET | &quot;get&quot; |
| LIST | &quot;list&quot; |
| DELETE | &quot;delete&quot; |
| CREATE | &quot;create&quot; |
| IMPORT | &quot;import&quot; |
| UPDATE | &quot;update&quot; |
| MANAGECONTACTS | &quot;managecontacts&quot; |
| GETISSUERS | &quot;getissuers&quot; |
| LISTISSUERS | &quot;listissuers&quot; |
| SETISSUERS | &quot;setissuers&quot; |
| DELETEISSUERS | &quot;deleteissuers&quot; |
| MANAGEISSUERS | &quot;manageissuers&quot; |
| RECOVER | &quot;recover&quot; |
| PURGE | &quot;purge&quot; |
| BACKUP | &quot;backup&quot; |
| RESTORE | &quot;restore&quot; |



## Enum: List&lt;KeysEnum&gt;

| Name | Value |
|---- | -----|
| ENCRYPT | &quot;encrypt&quot; |
| DECRYPT | &quot;decrypt&quot; |
| WRAP_KEY | &quot;wrapKey&quot; |
| UNWRAP_KEY | &quot;unwrapKey&quot; |
| SIGN | &quot;sign&quot; |
| VERIFY | &quot;verify&quot; |
| GET | &quot;get&quot; |
| LIST | &quot;list&quot; |
| CREATE | &quot;create&quot; |
| UPDATE | &quot;update&quot; |
| IMPORT | &quot;import&quot; |
| DELETE | &quot;delete&quot; |
| BACKUP | &quot;backup&quot; |
| RESTORE | &quot;restore&quot; |
| RECOVER | &quot;recover&quot; |
| PURGE | &quot;purge&quot; |



## Enum: List&lt;SecretsEnum&gt;

| Name | Value |
|---- | -----|
| GET | &quot;get&quot; |
| LIST | &quot;list&quot; |
| SET | &quot;set&quot; |
| DELETE | &quot;delete&quot; |
| BACKUP | &quot;backup&quot; |
| RESTORE | &quot;restore&quot; |
| RECOVER | &quot;recover&quot; |
| PURGE | &quot;purge&quot; |



## Enum: List&lt;StorageEnum&gt;

| Name | Value |
|---- | -----|
| GET | &quot;get&quot; |
| LIST | &quot;list&quot; |
| DELETE | &quot;delete&quot; |
| SET | &quot;set&quot; |
| UPDATE | &quot;update&quot; |
| REGENERATEKEY | &quot;regeneratekey&quot; |
| RECOVER | &quot;recover&quot; |
| PURGE | &quot;purge&quot; |
| BACKUP | &quot;backup&quot; |
| RESTORE | &quot;restore&quot; |
| SETSAS | &quot;setsas&quot; |
| LISTSAS | &quot;listsas&quot; |
| GETSAS | &quot;getsas&quot; |
| DELETESAS | &quot;deletesas&quot; |



