# LinodeApi.StackScript

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | The date this StackScript was created.  | [optional] [readonly] 
**deploymentsActive** | **Number** | Count of currently active, deployed Linodes created from this StackScript.  | [optional] [readonly] 
**deploymentsTotal** | **Number** | The total number of times this StackScript has been deployed.  | [optional] [readonly] 
**description** | **String** | A description for the StackScript.  | [optional] 
**id** | **Number** | The unique ID of this StackScript. | [optional] [readonly] 
**images** | **[String]** | An array of Image IDs. These are the Images that can be deployed with this StackScript.  &#x60;any/all&#x60; indicates that all available Images, including private Images, are accepted.  | [optional] 
**isPublic** | **Boolean** | This determines whether other users can use your StackScript. **Once a StackScript is made public, it cannot be made private.**  | [optional] 
**label** | **String** | The StackScript&#39;s label is for display purposes only.  | [optional] 
**mine** | **Boolean** | Returns &#x60;true&#x60; if this StackScript is owned by the account of the user making the request, and the user making the request is unrestricted or has access to this StackScript.  | [optional] [readonly] 
**revNote** | **String** | This field allows you to add notes for the set of revisions made to this StackScript.  | [optional] 
**script** | **String** | The script to execute when provisioning a new Linode with this StackScript.  | [optional] 
**updated** | **Date** | The date this StackScript was last updated.  | [optional] [readonly] 
**userDefinedFields** | [**[UserDefinedField]**](UserDefinedField.md) | This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized parameters during deployment. See [Declare User-Defined Fields (UDFs)](/docs/products/tools/stackscripts/guides/write-a-custom-script/#declare-user-defined-fields-udfs) for more information.  | [optional] [readonly] 
**userGravatarId** | **String** | The Gravatar ID for the User who created the StackScript.  | [optional] [readonly] 
**username** | **String** | The User who created the StackScript.  | [optional] [readonly] 


