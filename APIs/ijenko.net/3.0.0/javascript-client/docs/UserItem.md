# IoEIoTApiToCreateEndUserApplications.UserItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canLogin** | **Boolean** | true if the user owning the account (can get tokens with /auth/login) | [optional] [readonly] [default to false]
**email** | **String** |  | 
**id** | **String** | Unique identifier of the *User* | 
**locale** | **String** | Locale identifier (language, region). See https://tools.ietf.org/html/rfc5646 and https://www.iana.org/assignments/lang-subtags-templates/lang-subtags-templates.xhtml .  | 
**metadata** | **{String: Object}** | Subset of metadata attached to the resource selected using the &#39;embed-metadata&#39; parameter | [optional] 
**name** | **String** |  | 
**phoneNumber** | **String** | Phone number of the *User* in international format, for SMS notifications. | [optional] 


