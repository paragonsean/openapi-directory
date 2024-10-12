# CloudIdentityAwareProxyApi.PolicyName

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Identifies an instance of the type. ID format varies by type. The ID format is defined in the IAM .service file that defines the type, either in path_mapping or in a comment. | [optional] 
**region** | **String** | For Cloud IAM: The location of the Policy. Must be empty or \&quot;global\&quot; for Policies owned by global IAM. Must name a region from prodspec/cloud-iam-cloudspec for Regional IAM Policies, see go/iam-faq#where-is-iam-currently-deployed. For Local IAM: This field should be set to \&quot;local\&quot;. | [optional] 
**type** | **String** | Resource type. Types are defined in IAM&#39;s .service files. Valid values for type might be &#39;gce&#39;, &#39;gcs&#39;, &#39;project&#39;, &#39;account&#39; etc. | [optional] 


