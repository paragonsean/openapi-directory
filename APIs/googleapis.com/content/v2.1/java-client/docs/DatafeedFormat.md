

# DatafeedFormat


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnDelimiter** | **String** | Delimiter for the separation of values in a delimiter-separated values feed. If not specified, the delimiter will be auto-detected. Ignored for non-DSV data feeds. Acceptable values are: - \&quot;&#x60;pipe&#x60;\&quot; - \&quot;&#x60;tab&#x60;\&quot; - \&quot;&#x60;tilde&#x60;\&quot;  |  [optional] |
|**fileEncoding** | **String** | Character encoding scheme of the data feed. If not specified, the encoding will be auto-detected. Acceptable values are: - \&quot;&#x60;latin-1&#x60;\&quot; - \&quot;&#x60;utf-16be&#x60;\&quot; - \&quot;&#x60;utf-16le&#x60;\&quot; - \&quot;&#x60;utf-8&#x60;\&quot; - \&quot;&#x60;windows-1252&#x60;\&quot;  |  [optional] |
|**quotingMode** | **String** | Specifies how double quotes are interpreted. If not specified, the mode will be auto-detected. Ignored for non-DSV data feeds. Acceptable values are: - \&quot;&#x60;normal character&#x60;\&quot; - \&quot;&#x60;value quoting&#x60;\&quot;  |  [optional] |



