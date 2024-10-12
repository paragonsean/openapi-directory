# DracoonApi.CreateActiveDirectoryConfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adExportGroup** | **String** | If &#x60;userImport&#x60; is set to &#x60;true&#x60;,  the user must be member of this Active Directory group to receive a newly created DRACOON account. | [optional] 
**alias** | **String** | Unique name for an Active Directory configuration | 
**createHomeFolder** | **Boolean** | DEPRECATED, will be ignored  Determines whether a room is created for each user that is created by automatic import (like a home folder).  Room&#39;s name will equal the user&#39;s login name. | [optional] [default to false]
**homeFolderParent** | **Number** | DEPRECATED, will be ignored  ID of the room in which the individual rooms for users will be created. | [optional] 
**ldapUsersDomain** | **String** | Search scope of Active Directory; only users below this node can log on. | 
**sdsImportGroup** | **Number** | User group that is assigned to users who are created by automatic import.  Reset with &#x60;0&#x60; | [optional] 
**serverAdminName** | **String** | Distinguished Name (DN) of Active Directory administrative account | 
**serverAdminPassword** | **String** | Password of Active Directory administrative account | 
**serverIp** | **String** | IPv4 or IPv6 address or host name | 
**serverPort** | **Number** | Port | 
**sslFingerPrint** | **String** | SSL finger print of Active Directory server.  Mandatory for LDAPS connections.  Format: &#x60;Algorithm/Fingerprint&#x60; | [optional] 
**useLdaps** | **Boolean** | Determines whether LDAPS should be used instead of plain LDAP. | [optional] [default to false]
**userFilter** | **String** | Name of Active Directory attribute that is used as login name. | 
**userImport** | **Boolean** | Determines if a DRACOON account is automatically created for a new user  who successfully logs on with his / her AD / IDP account. | [optional] [default to false]


