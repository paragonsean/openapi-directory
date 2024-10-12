# BigQueryApi.ExternalDataConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autodetect** | **Boolean** | Try to detect schema and format options automatically. Any option specified explicitly will be honored. | [optional] 
**avroOptions** | [**AvroOptions**](AvroOptions.md) |  | [optional] 
**bigtableOptions** | [**BigtableOptions**](BigtableOptions.md) |  | [optional] 
**compression** | **String** | Optional. The compression type of the data source. Possible values include GZIP and NONE. The default value is NONE. This setting is ignored for Google Cloud Bigtable, Google Cloud Datastore backups, Avro, ORC and Parquet formats. An empty string is an invalid value. | [optional] 
**connectionId** | **String** | Optional. The connection specifying the credentials to be used to read external storage, such as Azure Blob, Cloud Storage, or S3. The connection_id can have the form \&quot;&lt;project\\_id&gt;.&lt;location\\_id&gt;.&lt;connection\\_id&gt;\&quot; or \&quot;projects/&lt;project\\_id&gt;/locations/&lt;location\\_id&gt;/connections/&lt;connection\\_id&gt;\&quot;. | [optional] 
**csvOptions** | [**CsvOptions**](CsvOptions.md) |  | [optional] 
**decimalTargetTypes** | **[String]** | Defines the list of possible SQL data types to which the source decimal values are converted. This list and the precision and the scale parameters of the decimal field determine the target type. In the order of NUMERIC, BIGNUMERIC, and STRING, a type is picked if it is in the specified list and if it supports the precision and the scale. STRING supports all precision and scale values. If none of the listed types supports the precision and the scale, the type supporting the widest range in the specified list is picked, and if a value exceeds the supported range when reading the data, an error will be thrown. Example: Suppose the value of this field is [\&quot;NUMERIC\&quot;, \&quot;BIGNUMERIC\&quot;]. If (precision,scale) is: * (38,9) -&gt; NUMERIC; * (39,9) -&gt; BIGNUMERIC (NUMERIC cannot hold 30 integer digits); * (38,10) -&gt; BIGNUMERIC (NUMERIC cannot hold 10 fractional digits); * (76,38) -&gt; BIGNUMERIC; * (77,38) -&gt; BIGNUMERIC (error if value exeeds supported range). This field cannot contain duplicate types. The order of the types in this field is ignored. For example, [\&quot;BIGNUMERIC\&quot;, \&quot;NUMERIC\&quot;] is the same as [\&quot;NUMERIC\&quot;, \&quot;BIGNUMERIC\&quot;] and NUMERIC always takes precedence over BIGNUMERIC. Defaults to [\&quot;NUMERIC\&quot;, \&quot;STRING\&quot;] for ORC and [\&quot;NUMERIC\&quot;] for the other file formats. | [optional] 
**fileSetSpecType** | **String** | Optional. Specifies how source URIs are interpreted for constructing the file set to load. By default source URIs are expanded against the underlying storage. Other options include specifying manifest files. Only applicable to object storage systems. | [optional] 
**googleSheetsOptions** | [**GoogleSheetsOptions**](GoogleSheetsOptions.md) |  | [optional] 
**hivePartitioningOptions** | [**HivePartitioningOptions**](HivePartitioningOptions.md) |  | [optional] 
**ignoreUnknownValues** | **Boolean** | Optional. Indicates if BigQuery should allow extra values that are not represented in the table schema. If true, the extra values are ignored. If false, records with extra columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false. The sourceFormat property determines what BigQuery treats as an extra value: CSV: Trailing columns JSON: Named values that don&#39;t match any column names Google Cloud Bigtable: This setting is ignored. Google Cloud Datastore backups: This setting is ignored. Avro: This setting is ignored. ORC: This setting is ignored. Parquet: This setting is ignored. | [optional] 
**jsonExtension** | **String** | Optional. Load option to be used together with source_format newline-delimited JSON to indicate that a variant of JSON is being loaded. To load newline-delimited GeoJSON, specify GEOJSON (and source_format must be set to NEWLINE_DELIMITED_JSON). | [optional] 
**jsonOptions** | [**JsonOptions**](JsonOptions.md) |  | [optional] 
**maxBadRecords** | **Number** | Optional. The maximum number of bad records that BigQuery can ignore when reading data. If the number of bad records exceeds this value, an invalid error is returned in the job result. The default value is 0, which requires that all records are valid. This setting is ignored for Google Cloud Bigtable, Google Cloud Datastore backups, Avro, ORC and Parquet formats. | [optional] 
**metadataCacheMode** | **String** | Optional. Metadata Cache Mode for the table. Set this to enable caching of metadata from external data source. | [optional] 
**objectMetadata** | **String** | Optional. ObjectMetadata is used to create Object Tables. Object Tables contain a listing of objects (with their metadata) found at the source_uris. If ObjectMetadata is set, source_format should be omitted. Currently SIMPLE is the only supported Object Metadata type. | [optional] 
**parquetOptions** | [**ParquetOptions**](ParquetOptions.md) |  | [optional] 
**referenceFileSchemaUri** | **String** | Optional. When creating an external table, the user can provide a reference file with the table schema. This is enabled for the following formats: AVRO, PARQUET, ORC. | [optional] 
**schema** | [**TableSchema**](TableSchema.md) |  | [optional] 
**sourceFormat** | **String** | [Required] The data format. For CSV files, specify \&quot;CSV\&quot;. For Google sheets, specify \&quot;GOOGLE_SHEETS\&quot;. For newline-delimited JSON, specify \&quot;NEWLINE_DELIMITED_JSON\&quot;. For Avro files, specify \&quot;AVRO\&quot;. For Google Cloud Datastore backups, specify \&quot;DATASTORE_BACKUP\&quot;. For Apache Iceberg tables, specify \&quot;ICEBERG\&quot;. For ORC files, specify \&quot;ORC\&quot;. For Parquet files, specify \&quot;PARQUET\&quot;. [Beta] For Google Cloud Bigtable, specify \&quot;BIGTABLE\&quot;. | [optional] 
**sourceUris** | **[String]** | [Required] The fully-qualified URIs that point to your data in Google Cloud. For Google Cloud Storage URIs: Each URI can contain one &#39;*&#39; wildcard character and it must come after the &#39;bucket&#39; name. Size limits related to load jobs apply to external data sources. For Google Cloud Bigtable URIs: Exactly one URI can be specified and it has be a fully specified and valid HTTPS URL for a Google Cloud Bigtable table. For Google Cloud Datastore backups, exactly one URI can be specified. Also, the &#39;*&#39; wildcard character is not allowed. | [optional] 



## Enum: [DecimalTargetTypesEnum]


* `DECIMAL_TARGET_TYPE_UNSPECIFIED` (value: `"DECIMAL_TARGET_TYPE_UNSPECIFIED"`)

* `NUMERIC` (value: `"NUMERIC"`)

* `BIGNUMERIC` (value: `"BIGNUMERIC"`)

* `STRING` (value: `"STRING"`)





## Enum: FileSetSpecTypeEnum


* `FILE_SYSTEM_MATCH` (value: `"FILE_SET_SPEC_TYPE_FILE_SYSTEM_MATCH"`)

* `NEW_LINE_DELIMITED_MANIFEST` (value: `"FILE_SET_SPEC_TYPE_NEW_LINE_DELIMITED_MANIFEST"`)





## Enum: JsonExtensionEnum


* `JSON_EXTENSION_UNSPECIFIED` (value: `"JSON_EXTENSION_UNSPECIFIED"`)

* `GEOJSON` (value: `"GEOJSON"`)





## Enum: MetadataCacheModeEnum


* `METADATA_CACHE_MODE_UNSPECIFIED` (value: `"METADATA_CACHE_MODE_UNSPECIFIED"`)

* `AUTOMATIC` (value: `"AUTOMATIC"`)

* `MANUAL` (value: `"MANUAL"`)





## Enum: ObjectMetadataEnum


* `OBJECT_METADATA_UNSPECIFIED` (value: `"OBJECT_METADATA_UNSPECIFIED"`)

* `DIRECTORY` (value: `"DIRECTORY"`)

* `SIMPLE` (value: `"SIMPLE"`)




