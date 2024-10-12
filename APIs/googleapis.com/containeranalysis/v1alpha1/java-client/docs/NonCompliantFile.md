

# NonCompliantFile

Details about files that caused a compliance check to fail.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayCommand** | **String** | Command to display the non-compliant files. |  [optional] |
|**path** | **String** | display_command is a single command that can be used to display a list of non compliant files. When there is no such command, we can also iterate a list of non compliant file using &#39;path&#39;. Empty if &#x60;display_command&#x60; is set. |  [optional] |
|**reason** | **String** | Explains why a file is non compliant for a CIS check. |  [optional] |



