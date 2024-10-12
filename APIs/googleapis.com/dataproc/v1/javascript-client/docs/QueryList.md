# CloudDataprocApi.QueryList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | **[String]** | Required. The queries to execute. You do not need to end a query expression with a semicolon. Multiple queries can be specified in one string by separating each with a semicolon. Here is an example of a Dataproc API snippet that uses a QueryList to specify a HiveJob: \&quot;hiveJob\&quot;: { \&quot;queryList\&quot;: { \&quot;queries\&quot;: [ \&quot;query1\&quot;, \&quot;query2\&quot;, \&quot;query3;query4\&quot;, ] } }  | [optional] 


