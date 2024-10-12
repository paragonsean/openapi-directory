# BigQueryApi.SparkOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archiveUris** | **[String]** | Archive files to be extracted into the working directory of each executor. For more information about Apache Spark, see [Apache Spark](https://spark.apache.org/docs/latest/index.html). | [optional] 
**connection** | **String** | Fully qualified name of the user-provided Spark connection object. Format: &#x60;&#x60;&#x60;\&quot;projects/{project_id}/locations/{location_id}/connections/{connection_id}\&quot;&#x60;&#x60;&#x60; | [optional] 
**containerImage** | **String** | Custom container image for the runtime environment. | [optional] 
**fileUris** | **[String]** | Files to be placed in the working directory of each executor. For more information about Apache Spark, see [Apache Spark](https://spark.apache.org/docs/latest/index.html). | [optional] 
**jarUris** | **[String]** | JARs to include on the driver and executor CLASSPATH. For more information about Apache Spark, see [Apache Spark](https://spark.apache.org/docs/latest/index.html). | [optional] 
**mainClass** | **String** | The fully qualified name of a class in jar_uris, for example, com.example.wordcount. Exactly one of main_class and main_jar_uri field should be set for Java/Scala language type. | [optional] 
**mainFileUri** | **String** | The main file/jar URI of the Spark application. Exactly one of the definition_body field and the main_file_uri field must be set for Python. Exactly one of main_class and main_file_uri field should be set for Java/Scala language type. | [optional] 
**properties** | **{String: String}** | Configuration properties as a set of key/value pairs, which will be passed on to the Spark application. For more information, see [Apache Spark](https://spark.apache.org/docs/latest/index.html) and the [procedure option list](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#procedure_option_list). | [optional] 
**pyFileUris** | **[String]** | Python files to be placed on the PYTHONPATH for PySpark application. Supported file types: &#x60;.py&#x60;, &#x60;.egg&#x60;, and &#x60;.zip&#x60;. For more information about Apache Spark, see [Apache Spark](https://spark.apache.org/docs/latest/index.html). | [optional] 
**runtimeVersion** | **String** | Runtime version. If not specified, the default runtime version is used. | [optional] 


