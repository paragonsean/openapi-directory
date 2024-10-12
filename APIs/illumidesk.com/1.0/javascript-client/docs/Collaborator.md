# IllumiDesk.Collaborator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **String** | Collaborator&#39;s valid email address. | [optional] 
**firstName** | **String** | Collaborator&#39;s first name. | [optional] 
**id** | **String** | Collaborator unique identifier in UUID format. | [optional] 
**joined** | **String** | Date time of when collaborator joined. | [optional] 
**lastName** | **String** | Collaborator&#39;s last name. | [optional] 
**owner** | **Boolean** | Boolean that states whether collaborator is project owner, or not.  | [optional] 
**permissions** | **[String]** | Collaborator permissions. Project creators are assigned owner priviledges by default. Permissions are write and read.  | [optional] 
**project** | **String** | Collaborator project name. | [optional] 
**user** | **String** | Collaborator user name. | [optional] 
**username** | **String** | Collaborator&#39;s user name. This must be a valid user name within the system.  | [optional] 



## Enum: [PermissionsEnum]


* `write_project` (value: `"write_project"`)

* `read_project` (value: `"read_project"`)




