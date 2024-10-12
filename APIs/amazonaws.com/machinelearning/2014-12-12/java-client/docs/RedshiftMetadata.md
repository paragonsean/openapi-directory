

# RedshiftMetadata

Describes the <code>DataSource</code> details specific to Amazon Redshift.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**redshiftDatabase** | [**RedshiftDatabase**](RedshiftDatabase.md) |  |  [optional] |
|**databaseUserName** | **String** | A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an Amazon Redshift cluster. The username should have sufficient permissions to execute the &lt;code&gt;RedshiftSelectSqlQuery&lt;/code&gt; query. The username should be valid for an Amazon Redshift &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html\&quot;&gt;USER&lt;/a&gt;. |  [optional] |
|**selectSqlQuery** | [**String**](String.md) |  |  [optional] |



