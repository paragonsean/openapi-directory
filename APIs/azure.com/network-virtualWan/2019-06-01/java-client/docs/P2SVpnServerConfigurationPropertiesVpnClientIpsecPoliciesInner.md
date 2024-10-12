

# P2SVpnServerConfigurationPropertiesVpnClientIpsecPoliciesInner

An IPSec Policy configuration for a virtual network gateway connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dhGroup** | [**DhGroupEnum**](#DhGroupEnum) | The DH Groups used in IKE Phase 1 for initial SA. |  |
|**ikeEncryption** | [**IkeEncryptionEnum**](#IkeEncryptionEnum) | The IKE encryption algorithm (IKE phase 2). |  |
|**ikeIntegrity** | [**IkeIntegrityEnum**](#IkeIntegrityEnum) | The IKE integrity algorithm (IKE phase 2). |  |
|**ipsecEncryption** | [**IpsecEncryptionEnum**](#IpsecEncryptionEnum) | The IPSec encryption algorithm (IKE phase 1). |  |
|**ipsecIntegrity** | [**IpsecIntegrityEnum**](#IpsecIntegrityEnum) | The IPSec integrity algorithm (IKE phase 1). |  |
|**pfsGroup** | [**PfsGroupEnum**](#PfsGroupEnum) | The Pfs Groups used in IKE Phase 2 for new child SA. |  |
|**saDataSizeKilobytes** | **Integer** | The IPSec Security Association (also called Quick Mode or Phase 2 SA) payload size in KB for a site to site VPN tunnel. |  |
|**saLifeTimeSeconds** | **Integer** | The IPSec Security Association (also called Quick Mode or Phase 2 SA) lifetime in seconds for a site to site VPN tunnel. |  |



## Enum: DhGroupEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| DH_GROUP1 | &quot;DHGroup1&quot; |
| DH_GROUP2 | &quot;DHGroup2&quot; |
| DH_GROUP14 | &quot;DHGroup14&quot; |
| DH_GROUP2048 | &quot;DHGroup2048&quot; |
| ECP256 | &quot;ECP256&quot; |
| ECP384 | &quot;ECP384&quot; |
| DH_GROUP24 | &quot;DHGroup24&quot; |



## Enum: IkeEncryptionEnum

| Name | Value |
|---- | -----|
| DES | &quot;DES&quot; |
| DES3 | &quot;DES3&quot; |
| AES128 | &quot;AES128&quot; |
| AES192 | &quot;AES192&quot; |
| AES256 | &quot;AES256&quot; |
| GCMAES256 | &quot;GCMAES256&quot; |
| GCMAES128 | &quot;GCMAES128&quot; |



## Enum: IkeIntegrityEnum

| Name | Value |
|---- | -----|
| MD5 | &quot;MD5&quot; |
| SHA1 | &quot;SHA1&quot; |
| SHA256 | &quot;SHA256&quot; |
| SHA384 | &quot;SHA384&quot; |
| GCMAES256 | &quot;GCMAES256&quot; |
| GCMAES128 | &quot;GCMAES128&quot; |



## Enum: IpsecEncryptionEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| DES | &quot;DES&quot; |
| DES3 | &quot;DES3&quot; |
| AES128 | &quot;AES128&quot; |
| AES192 | &quot;AES192&quot; |
| AES256 | &quot;AES256&quot; |
| GCMAES128 | &quot;GCMAES128&quot; |
| GCMAES192 | &quot;GCMAES192&quot; |
| GCMAES256 | &quot;GCMAES256&quot; |



## Enum: IpsecIntegrityEnum

| Name | Value |
|---- | -----|
| MD5 | &quot;MD5&quot; |
| SHA1 | &quot;SHA1&quot; |
| SHA256 | &quot;SHA256&quot; |
| GCMAES128 | &quot;GCMAES128&quot; |
| GCMAES192 | &quot;GCMAES192&quot; |
| GCMAES256 | &quot;GCMAES256&quot; |



## Enum: PfsGroupEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| PFS1 | &quot;PFS1&quot; |
| PFS2 | &quot;PFS2&quot; |
| PFS2048 | &quot;PFS2048&quot; |
| ECP256 | &quot;ECP256&quot; |
| ECP384 | &quot;ECP384&quot; |
| PFS24 | &quot;PFS24&quot; |
| PFS14 | &quot;PFS14&quot; |
| PFSMM | &quot;PFSMM&quot; |



