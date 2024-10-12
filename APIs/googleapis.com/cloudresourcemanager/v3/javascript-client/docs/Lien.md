# CloudResourceManagerApi.Lien

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | The creation time of this Lien. | [optional] 
**name** | **String** | A system-generated unique identifier for this Lien. Example: &#x60;liens/1234abcd&#x60; | [optional] 
**origin** | **String** | A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically. Maximum length of 200 characters. Example: &#39;compute.googleapis.com&#39; | [optional] 
**parent** | **String** | A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens are supported. Example: &#x60;projects/1234&#x60; | [optional] 
**reason** | **String** | Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200 characters. Example: &#39;Holds production API key&#39; | [optional] 
**restrictions** | **[String]** | The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM permission. The server will validate the permissions against those for which Liens are supported. An empty list is meaningless and will be rejected. Example: [&#39;resourcemanager.projects.delete&#39;] | [optional] 


