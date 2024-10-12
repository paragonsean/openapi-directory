

# SNMP3Config


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationPassword** | **String** |  |  [optional] |
|**authenticationType** | [**AuthenticationTypeEnum**](#AuthenticationTypeEnum) |  |  [optional] |
|**contextName** | **String** |  |  [optional] |
|**privacyPassword** | **String** |  |  [optional] |
|**privacyType** | [**PrivacyTypeEnum**](#PrivacyTypeEnum) |  |  [optional] |
|**username** | **String** |  |  [optional] |



## Enum: AuthenticationTypeEnum

| Name | Value |
|---- | -----|
| NO_AUTH | &quot;NO_AUTH&quot; |
| MD5 | &quot;MD5&quot; |
| SHA | &quot;SHA&quot; |



## Enum: PrivacyTypeEnum

| Name | Value |
|---- | -----|
| AES | &quot;AES&quot; |
| DES | &quot;DES&quot; |
| AES128 | &quot;AES128&quot; |
| AES192 | &quot;AES192&quot; |
| AES256 | &quot;AES256&quot; |
| _3_DES | &quot;3DES&quot; |
| NO_PRIV | &quot;NO_PRIV&quot; |



