# AppCenterClient.ReleasesUpdateDetails400ResponseAllOfDestinationsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Error Codes:&lt;br&gt; &lt;b&gt;invalid_store_secrets&lt;/b&gt;: While distributing to store, secrets provided for store are not valid.&lt;br&gt; &lt;b&gt;store_release_bad_request&lt;/b&gt;: Proper package release details for the store is not provided.&lt;br&gt; &lt;b&gt;store_release_unauthorized&lt;/b&gt;: User is not authorized to publish to store due to invalid developer credentials.&lt;br&gt; &lt;b&gt;store_release_forbidden&lt;/b&gt;: Publish to store is forbidden due to conflicts/errors in the release version and already existing version in the store.&lt;br&gt; &lt;b&gt;store_release_promotion&lt;/b&gt;: Release already distributed, promoting a release is not supported.&lt;br&gt; &lt;b&gt;store_track_deactivated&lt;/b&gt;: One or more tracks would be deactivated with this release. This is not supported yet.&lt;br&gt; &lt;b&gt;store_release_not_found&lt;/b&gt;: App with the given package name is not found in the store.&lt;br&gt; &lt;b&gt;store_release_not_available&lt;/b&gt;: The release is not available.&lt;br&gt; &lt;b&gt;internal_server_error&lt;/b&gt;: Failed to distribute to a destination due to an internal server error.  | [optional] 
**id** | **String** |  | [optional] 
**message** | **String** |  | [optional] 
**name** | **String** |  | [optional] 


