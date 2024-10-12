

# Permissions

Permissions the identity has for keys, secrets and certificates.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificates** | [**List&lt;CertificatesEnum&gt;**](#List&lt;CertificatesEnum&gt;) | Permissions to certificates |  [optional] |
|**keys** | [**List&lt;KeysEnum&gt;**](#List&lt;KeysEnum&gt;) | Permissions to keys |  [optional] |
|**secrets** | [**List&lt;SecretsEnum&gt;**](#List&lt;SecretsEnum&gt;) | Permissions to secrets |  [optional] |



## Enum: List&lt;CertificatesEnum&gt;

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
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



## Enum: List&lt;KeysEnum&gt;

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
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
| ALL | &quot;all&quot; |
| GET | &quot;get&quot; |
| LIST | &quot;list&quot; |
| SET | &quot;set&quot; |
| DELETE | &quot;delete&quot; |
| BACKUP | &quot;backup&quot; |
| RESTORE | &quot;restore&quot; |
| RECOVER | &quot;recover&quot; |
| PURGE | &quot;purge&quot; |



