

# HadoopJob

A Dataproc job for running Apache Hadoop MapReduce (https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html) jobs on Apache Hadoop YARN (https://hadoop.apache.org/docs/r2.7.1/hadoop-yarn/hadoop-yarn-site/YARN.html).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archiveUris** | **List&lt;String&gt;** | Optional. HCFS URIs of archives to be extracted in the working directory of Hadoop drivers and tasks. Supported file types: .jar, .tar, .tar.gz, .tgz, or .zip. |  [optional] |
|**args** | **List&lt;String&gt;** | Optional. The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo&#x3D;bar, that can be set as job properties, since a collision might occur that causes an incorrect job submission. |  [optional] |
|**fileUris** | **List&lt;String&gt;** | Optional. HCFS (Hadoop Compatible Filesystem) URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks. |  [optional] |
|**jarFileUris** | **List&lt;String&gt;** | Optional. Jar file URIs to add to the CLASSPATHs of the Hadoop driver and tasks. |  [optional] |
|**loggingConfig** | [**LoggingConfig**](LoggingConfig.md) |  |  [optional] |
|**mainClass** | **String** | The name of the driver&#39;s main class. The jar file containing the class must be in the default CLASSPATH or specified in jar_file_uris. |  [optional] |
|**mainJarFileUri** | **String** | The HCFS URI of the jar file containing the main class. Examples: &#39;gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar&#39; &#39;hdfs:/tmp/test-samples/custom-wordcount.jar&#39; &#39;file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar&#39; |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | Optional. A mapping of property names to values, used to configure Hadoop. Properties that conflict with values set by the Dataproc API might be overwritten. Can include properties set in /etc/hadoop/conf/_*-site and classes in user code. |  [optional] |



