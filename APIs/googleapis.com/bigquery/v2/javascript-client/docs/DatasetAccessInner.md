# BigQueryApi.DatasetAccessInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | [**DatasetAccessEntry**](DatasetAccessEntry.md) |  | [optional] 
**domain** | **String** | [Pick one] A domain to grant access to. Any users signed in with the domain specified will be granted the specified access. Example: \&quot;example.com\&quot;. Maps to IAM policy member \&quot;domain:DOMAIN\&quot;. | [optional] 
**groupByEmail** | **String** | [Pick one] An email address of a Google Group to grant access to. Maps to IAM policy member \&quot;group:GROUP\&quot;. | [optional] 
**iamMember** | **String** | [Pick one] Some other type of member that appears in the IAM Policy but isn&#39;t a user, group, domain, or special group. | [optional] 
**role** | **String** | An IAM role ID that should be granted to the user, group, or domain specified in this access entry. The following legacy mappings will be applied: OWNER &lt;&#x3D;&gt; roles/bigquery.dataOwner WRITER &lt;&#x3D;&gt; roles/bigquery.dataEditor READER &lt;&#x3D;&gt; roles/bigquery.dataViewer This field will accept any of the above formats, but will return only the legacy format. For example, if you set this field to \&quot;roles/bigquery.dataOwner\&quot;, it will be returned back as \&quot;OWNER\&quot;. | [optional] 
**routine** | [**RoutineReference**](RoutineReference.md) |  | [optional] 
**specialGroup** | **String** | [Pick one] A special group to grant access to. Possible values include: projectOwners: Owners of the enclosing project. projectReaders: Readers of the enclosing project. projectWriters: Writers of the enclosing project. allAuthenticatedUsers: All authenticated BigQuery users. Maps to similarly-named IAM members. | [optional] 
**userByEmail** | **String** | [Pick one] An email address of a user to grant access to. For example: fred@example.com. Maps to IAM policy member \&quot;user:EMAIL\&quot; or \&quot;serviceAccount:EMAIL\&quot;. | [optional] 
**view** | [**TableReference**](TableReference.md) |  | [optional] 


