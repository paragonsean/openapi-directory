

# YumRepository

Represents a single Yum package repository. This repository is added to a repo file that is stored at `/etc/yum.repos.d/google_osconfig.repo`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseUrl** | **String** | Required. The location of the repository directory. |  [optional] |
|**displayName** | **String** | The display name of the repository. |  [optional] |
|**gpgKeys** | **List&lt;String&gt;** | URIs of GPG keys. |  [optional] |
|**id** | **String** | Required. A one word, unique name for this repository. This is the &#x60;repo id&#x60; in the Yum config file and also the &#x60;display_name&#x60; if &#x60;display_name&#x60; is omitted. This id is also used as the unique identifier when checking for guest policy conflicts. |  [optional] |



