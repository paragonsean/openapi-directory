

# HiveJob

A Dataproc job for running Apache Hive (https://hive.apache.org/) queries on YARN.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**continueOnFailure** | **Boolean** | Optional. Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. |  [optional] |
|**jarFileUris** | **List&lt;String&gt;** | Optional. HCFS URIs of jar files to add to the CLASSPATH of the Hive server and Hadoop MapReduce (MR) tasks. Can contain Hive SerDes and UDFs. |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | Optional. A mapping of property names and values, used to configure Hive. Properties that conflict with values set by the Dataproc API might be overwritten. Can include properties set in /etc/hadoop/conf/_*-site.xml, /etc/hive/conf/hive-site.xml, and classes in user code. |  [optional] |
|**queryFileUri** | **String** | The HCFS URI of the script that contains Hive queries. |  [optional] |
|**queryList** | [**QueryList**](QueryList.md) |  |  [optional] |
|**scriptVariables** | **Map&lt;String, String&gt;** | Optional. Mapping of query variable names to values (equivalent to the Hive command: SET name&#x3D;\&quot;value\&quot;;). |  [optional] |



