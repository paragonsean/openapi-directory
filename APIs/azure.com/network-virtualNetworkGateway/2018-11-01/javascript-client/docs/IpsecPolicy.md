# NetworkManagementClient.IpsecPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhGroup** | **String** | The DH Groups used in IKE Phase 1 for initial SA. | 
**ikeEncryption** | **String** | The IKE encryption algorithm (IKE phase 2). | 
**ikeIntegrity** | **String** | The IKE integrity algorithm (IKE phase 2). | 
**ipsecEncryption** | **String** | The IPSec encryption algorithm (IKE phase 1). | 
**ipsecIntegrity** | **String** | The IPSec integrity algorithm (IKE phase 1). | 
**pfsGroup** | **String** | The Pfs Groups used in IKE Phase 2 for new child SA. | 
**saDataSizeKilobytes** | **Number** | The IPSec Security Association (also called Quick Mode or Phase 2 SA) payload size in KB for a site to site VPN tunnel. | 
**saLifeTimeSeconds** | **Number** | The IPSec Security Association (also called Quick Mode or Phase 2 SA) lifetime in seconds for a site to site VPN tunnel. | 



## Enum: DhGroupEnum


* `None` (value: `"None"`)

* `DHGroup1` (value: `"DHGroup1"`)

* `DHGroup2` (value: `"DHGroup2"`)

* `DHGroup14` (value: `"DHGroup14"`)

* `DHGroup2048` (value: `"DHGroup2048"`)

* `ECP256` (value: `"ECP256"`)

* `ECP384` (value: `"ECP384"`)

* `DHGroup24` (value: `"DHGroup24"`)





## Enum: IkeEncryptionEnum


* `DES` (value: `"DES"`)

* `DES3` (value: `"DES3"`)

* `AES128` (value: `"AES128"`)

* `AES192` (value: `"AES192"`)

* `AES256` (value: `"AES256"`)

* `GCMAES256` (value: `"GCMAES256"`)

* `GCMAES128` (value: `"GCMAES128"`)





## Enum: IkeIntegrityEnum


* `MD5` (value: `"MD5"`)

* `SHA1` (value: `"SHA1"`)

* `SHA256` (value: `"SHA256"`)

* `SHA384` (value: `"SHA384"`)

* `GCMAES256` (value: `"GCMAES256"`)

* `GCMAES128` (value: `"GCMAES128"`)





## Enum: IpsecEncryptionEnum


* `None` (value: `"None"`)

* `DES` (value: `"DES"`)

* `DES3` (value: `"DES3"`)

* `AES128` (value: `"AES128"`)

* `AES192` (value: `"AES192"`)

* `AES256` (value: `"AES256"`)

* `GCMAES128` (value: `"GCMAES128"`)

* `GCMAES192` (value: `"GCMAES192"`)

* `GCMAES256` (value: `"GCMAES256"`)





## Enum: IpsecIntegrityEnum


* `MD5` (value: `"MD5"`)

* `SHA1` (value: `"SHA1"`)

* `SHA256` (value: `"SHA256"`)

* `GCMAES128` (value: `"GCMAES128"`)

* `GCMAES192` (value: `"GCMAES192"`)

* `GCMAES256` (value: `"GCMAES256"`)





## Enum: PfsGroupEnum


* `None` (value: `"None"`)

* `PFS1` (value: `"PFS1"`)

* `PFS2` (value: `"PFS2"`)

* `PFS2048` (value: `"PFS2048"`)

* `ECP256` (value: `"ECP256"`)

* `ECP384` (value: `"ECP384"`)

* `PFS24` (value: `"PFS24"`)

* `PFS14` (value: `"PFS14"`)

* `PFSMM` (value: `"PFSMM"`)




