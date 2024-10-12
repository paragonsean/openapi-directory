

# AdvancedOptionsStatus

<p>Status of the advanced options for the specified domain. The following options are available: </p> <ul> <li> <p> <code>\"rest.action.multi.allow_explicit_index\": \"true\" | \"false\"</code> - Note the use of a string rather than a boolean. Specifies whether explicit references to indexes are allowed inside the body of HTTP requests. If you want to configure access policies for domain sub-resources, such as specific indexes and domain APIs, you must disable this property. Default is true.</p> </li> <li> <p> <code>\"indices.fielddata.cache.size\": \"80\" </code> - Note the use of a string rather than a boolean. Specifies the percentage of heap space allocated to field data. Default is unbounded.</p> </li> <li> <p> <code>\"indices.query.bool.max_clause_count\": \"1024\"</code> - Note the use of a string rather than a boolean. Specifies the maximum number of clauses allowed in a Lucene boolean query. Default is 1,024. Queries with more than the permitted number of clauses result in a <code>TooManyClauses</code> error.</p> </li> <li> <p> <code>\"override_main_response_version\": \"true\" | \"false\"</code> - Note the use of a string rather than a boolean. Specifies whether the domain reports its version as 7.10 to allow Elasticsearch OSS clients and plugins to continue working with it. Default is false when creating a domain and true when upgrading a domain.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options\">Advanced cluster parameters</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**options** | [**Map**](Map.md) |  |  |
|**status** | [**AdvancedOptionsStatusStatus**](AdvancedOptionsStatusStatus.md) |  |  |



