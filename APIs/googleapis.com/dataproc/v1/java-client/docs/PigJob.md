

# PigJob

A Dataproc job for running Apache Pig (https://pig.apache.org/) queries on YARN.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**continueOnFailure** | **Boolean** | Optional. Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. |  [optional] |
|**jarFileUris** | **List&lt;String&gt;** | Optional. HCFS URIs of jar files to add to the CLASSPATH of the Pig Client and Hadoop MapReduce (MR) tasks. Can contain Pig UDFs. |  [optional] |
|**loggingConfig** | [**LoggingConfig**](LoggingConfig.md) |  |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | Optional. A mapping of property names to values, used to configure Pig. Properties that conflict with values set by the Dataproc API might be overwritten. Can include properties set in /etc/hadoop/conf/_*-site.xml, /etc/pig/conf/pig.properties, and classes in user code. |  [optional] |
|**queryFileUri** | **String** | The HCFS URI of the script that contains the Pig queries. |  [optional] |
|**queryList** | [**QueryList**](QueryList.md) |  |  [optional] |
|**scriptVariables** | **Map&lt;String, String&gt;** | Optional. Mapping of query variable names to values (equivalent to the Pig command: name&#x3D;[value]). |  [optional] |



