

# Resource

 Information about an instance of an AWS resource associated with a project. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** |  Simplified name for type of AWS resource (e.g., bucket is an Amazon S3 bucket).  |  [optional] |
|**name** | **String** |  Name of the AWS resource (e.g., for an Amazon S3 bucket this is the name of the bucket).  |  [optional] |
|**arn** | **String** |  AWS resource name which uniquely identifies the resource in AWS systems.  |  [optional] |
|**feature** | **String** |  Identifies which feature in AWS Mobile Hub is associated with this AWS resource.  |  [optional] |
|**attributes** | **Map&lt;String, String&gt;** |  Key-value attribute pairs.  |  [optional] |



