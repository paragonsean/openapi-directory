

# LoggingConfig

The runtime logging config of the job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**driverLogLevels** | [**Map&lt;String, InnerEnum&gt;**](#Map&lt;String, InnerEnum&gt;) | The per-package log levels for the driver. This can include \&quot;root\&quot; package name to configure rootLogger. Examples: - &#39;com.google &#x3D; FATAL&#39; - &#39;root &#x3D; INFO&#39; - &#39;org.apache &#x3D; DEBUG&#39; |  [optional] |



## Enum: Map&lt;String, InnerEnum&gt;

| Name | Value |
|---- | -----|
| LEVEL_UNSPECIFIED | &quot;LEVEL_UNSPECIFIED&quot; |
| ALL | &quot;ALL&quot; |
| TRACE | &quot;TRACE&quot; |
| DEBUG | &quot;DEBUG&quot; |
| INFO | &quot;INFO&quot; |
| WARN | &quot;WARN&quot; |
| ERROR | &quot;ERROR&quot; |
| FATAL | &quot;FATAL&quot; |
| FALSE | &quot;false&quot; |



