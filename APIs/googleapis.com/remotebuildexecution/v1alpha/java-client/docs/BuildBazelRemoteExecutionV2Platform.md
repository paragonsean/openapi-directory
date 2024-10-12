

# BuildBazelRemoteExecutionV2Platform

A `Platform` is a set of requirements, such as hardware, operating system, or compiler toolchain, for an Action's execution environment. A `Platform` is represented as a series of key-value pairs representing the properties that are required of the platform.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**List&lt;BuildBazelRemoteExecutionV2PlatformProperty&gt;**](BuildBazelRemoteExecutionV2PlatformProperty.md) | The properties that make up this platform. In order to ensure that equivalent &#x60;Platform&#x60;s always hash to the same value, the properties MUST be lexicographically sorted by name, and then by value. Sorting of strings is done by code point, equivalently, by the UTF-8 bytes. |  [optional] |



