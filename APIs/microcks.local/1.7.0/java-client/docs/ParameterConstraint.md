

# ParameterConstraint

Companion object for Operation that may be used to express constraints on request parameters

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**in** | [**InEnum**](#InEnum) | Parameter location |  [optional] |
|**mustMatchRegexp** | **String** | Whether it&#39;s a regular expression matching constraint |  [optional] |
|**name** | **String** | Parameter name |  |
|**recopy** | **Boolean** | Whether it&#39;s a recopy constraint |  [optional] |
|**required** | **Boolean** | Whether it&#39;s a required constraint |  [optional] |



## Enum: InEnum

| Name | Value |
|---- | -----|
| PATH | &quot;path&quot; |
| QUERY | &quot;query&quot; |
| HEADER | &quot;header&quot; |



