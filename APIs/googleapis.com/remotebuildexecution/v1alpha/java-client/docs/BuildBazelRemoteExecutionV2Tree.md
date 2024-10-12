

# BuildBazelRemoteExecutionV2Tree

A `Tree` contains all the Directory protos in a single directory Merkle tree, compressed into one message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**children** | [**List&lt;BuildBazelRemoteExecutionV2Directory&gt;**](BuildBazelRemoteExecutionV2Directory.md) | All the child directories: the directories referred to by the root and, recursively, all its children. In order to reconstruct the directory tree, the client must take the digests of each of the child directories and then build up a tree starting from the &#x60;root&#x60;. Servers SHOULD ensure that these are ordered consistently such that two actions producing equivalent output directories on the same server implementation also produce Tree messages with matching digests. |  [optional] |
|**root** | [**BuildBazelRemoteExecutionV2Directory**](BuildBazelRemoteExecutionV2Directory.md) |  |  [optional] |



