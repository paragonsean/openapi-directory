

# FlinkJob

A Dataproc job for running Apache Flink applications on YARN.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**args** | **List&lt;String&gt;** | Optional. The arguments to pass to the driver. Do not include arguments, such as --conf, that can be set as job properties, since a collision might occur that causes an incorrect job submission. |  [optional] |
|**jarFileUris** | **List&lt;String&gt;** | Optional. HCFS URIs of jar files to add to the CLASSPATHs of the Flink driver and tasks. |  [optional] |
|**loggingConfig** | [**LoggingConfig**](LoggingConfig.md) |  |  [optional] |
|**mainClass** | **String** | The name of the driver&#39;s main class. The jar file that contains the class must be in the default CLASSPATH or specified in jarFileUris. |  [optional] |
|**mainJarFileUri** | **String** | The HCFS URI of the jar file that contains the main class. |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | Optional. A mapping of property names to values, used to configure Flink. Properties that conflict with values set by the Dataproc API might beoverwritten. Can include properties set in/etc/flink/conf/flink-defaults.conf and classes in user code. |  [optional] |
|**savepointUri** | **String** | Optional. HCFS URI of the savepoint, which contains the last saved progress for starting the current job. |  [optional] |



