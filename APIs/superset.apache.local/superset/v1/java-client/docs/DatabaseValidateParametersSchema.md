

# DatabaseValidateParametersSchema


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configurationMethod** | **Object** | Configuration_method is used on the frontend to inform the backend whether to explode parameters or to provide only a sqlalchemy_uri. |  |
|**databaseName** | **String** | A database name to identify this connection. |  [optional] |
|**encryptedExtra** | **String** | &lt;p&gt;JSON string containing additional connection configuration.&lt;br&gt;This is used to provide connection information for systems like Hive, Presto, and BigQuery, which do not conform to the username:password syntax normally used by SQLAlchemy.&lt;/p&gt; |  [optional] |
|**engine** | **String** | SQLAlchemy engine to use |  |
|**extra** | **String** | &lt;p&gt;JSON string containing extra configuration elements.&lt;br&gt;1. The &lt;code&gt;engine_params&lt;/code&gt; object gets unpacked into the &lt;a href&#x3D;\&quot;https://docs.sqlalchemy.org/en/latest/core/engines.html#sqlalchemy.create_engine\&quot;&gt;sqlalchemy.create_engine&lt;/a&gt; call, while the &lt;code&gt;metadata_params&lt;/code&gt; gets unpacked into the &lt;a href&#x3D;\&quot;https://docs.sqlalchemy.org/en/rel_1_0/core/metadata.html#sqlalchemy.schema.MetaData\&quot;&gt;sqlalchemy.MetaData&lt;/a&gt; call.&lt;br&gt;2. The &lt;code&gt;metadata_cache_timeout&lt;/code&gt; is a cache timeout setting in seconds for metadata fetch of this database. Specify it as &lt;strong&gt;\&quot;metadata_cache_timeout\&quot;: {\&quot;schema_cache_timeout\&quot;: 600, \&quot;table_cache_timeout\&quot;: 600}&lt;/strong&gt;. If unset, cache will not be enabled for the functionality. A timeout of 0 indicates that the cache never expires.&lt;br&gt;3. The &lt;code&gt;schemas_allowed_for_csv_upload&lt;/code&gt; is a comma separated list of schemas that CSVs are allowed to upload to. Specify it as &lt;strong&gt;\&quot;schemas_allowed_for_csv_upload\&quot;: [\&quot;public\&quot;, \&quot;csv_upload\&quot;]&lt;/strong&gt;. If database flavor does not support schema or any schema is allowed to be accessed, just leave the list empty&lt;br&gt;4. the &lt;code&gt;version&lt;/code&gt; field is a string specifying the this db&#39;s version. This should be used with Presto DBs so that the syntax is correct&lt;br&gt;5. The &lt;code&gt;allows_virtual_table_explore&lt;/code&gt; field is a boolean specifying whether or not the Explore button in SQL Lab results is shown.&lt;/p&gt; |  [optional] |
|**impersonateUser** | **Boolean** | If Presto, all the queries in SQL Lab are going to be executed as the currently logged on user who must have permission to run them.&lt;br/&gt;If Hive and hive.server2.enable.doAs is enabled, will run the queries as service account, but impersonate the currently logged on user via hive.server2.proxy.user property. |  [optional] |
|**parameters** | **Map&lt;String, Object&gt;** | DB-specific parameters for configuration |  [optional] |
|**serverCert** | **String** | &lt;p&gt;Optional CA_BUNDLE contents to validate HTTPS requests. Only available on certain database engines.&lt;/p&gt; |  [optional] |



