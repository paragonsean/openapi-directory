# DracoonApi.TestActiveDirectoryConfigResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ldapUsersDomain** | **String** | Search scope of Active Directory; only users below this node can log on. | 
**serverAdminName** | **String** | Distinguished Name (DN) of Active Directory administrative account | 
**serverAdminPassword** | **String** | Password of Active Directory administrative account | 
**serverIp** | **String** | IPv4 or IPv6 address or host name | 
**serverPort** | **Number** | Port | 
**sslFingerPrint** | **String** | SSL finger print of Active Directory server.  Mandatory for LDAPS connections.  Format: &#x60;Algorithm/Fingerprint&#x60; | [optional] 
**useLdaps** | **Boolean** | Determines whether LDAPS should be used instead of plain LDAP. | 


