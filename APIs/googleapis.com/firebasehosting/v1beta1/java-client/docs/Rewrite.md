

# Rewrite

A [`Rewrite`](https://firebase.google.com/docs/hosting/full-config#rewrites) specifies a URL pattern that, if matched to the request URL path, triggers Hosting to respond as if the service were given the specified destination URL.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dynamicLinks** | **Boolean** | The request will be forwarded to Firebase Dynamic Links. |  [optional] |
|**function** | **String** | The function to proxy requests to. Must match the exported function name exactly. |  [optional] |
|**functionRegion** | **String** | Optional. Specify a Cloud region for rewritten Functions invocations. If not provided, defaults to us-central1. |  [optional] |
|**glob** | **String** | The user-supplied [glob](https://firebase.google.com/docs/hosting/full-config#glob_pattern_matching) to match against the request URL path. |  [optional] |
|**path** | **String** | The URL path to rewrite the request to. |  [optional] |
|**regex** | **String** | The user-supplied RE2 regular expression to match against the request URL path. |  [optional] |
|**run** | [**CloudRunRewrite**](CloudRunRewrite.md) |  |  [optional] |



