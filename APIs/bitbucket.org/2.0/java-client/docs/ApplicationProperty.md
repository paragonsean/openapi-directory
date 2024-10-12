

# ApplicationProperty

An application property. It is a caller defined JSON object that Bitbucket will store and return.  The `_attributes` field at its top level can be used to control who is allowed to read and update the property.  The keys of the JSON object must match an allowed pattern. For details,  see [Application properties](/cloud/bitbucket/application-properties/). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**List&lt;AttributesEnum&gt;**](#List&lt;AttributesEnum&gt;) |  |  [optional] |



## Enum: List&lt;AttributesEnum&gt;

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| READ_ONLY | &quot;read_only&quot; |



