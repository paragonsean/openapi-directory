

# Repo

A repository (or repo) is a Git repository storing versioned source content.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mirrorConfig** | [**MirrorConfig**](MirrorConfig.md) |  |  [optional] |
|**name** | **String** | Resource name of the repository, of the form &#x60;projects//repos/&#x60;. The repo name may contain slashes. eg, &#x60;projects/myproject/repos/name/with/slash&#x60; |  [optional] |
|**pubsubConfigs** | [**Map&lt;String, PubsubConfig&gt;**](PubsubConfig.md) | How this repository publishes a change in the repository through Cloud Pub/Sub. Keyed by the topic names. |  [optional] |
|**size** | **String** | The disk usage of the repo, in bytes. Read-only field. Size is only returned by GetRepo. |  [optional] |
|**url** | **String** | URL to clone the repository from Google Cloud Source Repositories. Read-only field. |  [optional] |



