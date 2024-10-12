

# CommitComparison

Commit Comparison

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aheadBy** | **Integer** |  |  |
|**baseCommit** | [**Commit**](Commit.md) |  |  |
|**behindBy** | **Integer** |  |  |
|**commits** | [**List&lt;Commit&gt;**](Commit.md) |  |  |
|**diffUrl** | **URI** |  |  |
|**files** | [**List&lt;DiffEntry&gt;**](DiffEntry.md) |  |  [optional] |
|**htmlUrl** | **URI** |  |  |
|**mergeBaseCommit** | [**Commit**](Commit.md) |  |  |
|**patchUrl** | **URI** |  |  |
|**permalinkUrl** | **URI** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**totalCommits** | **Integer** |  |  |
|**url** | **URI** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DIVERGED | &quot;diverged&quot; |
| AHEAD | &quot;ahead&quot; |
| BEHIND | &quot;behind&quot; |
| IDENTICAL | &quot;identical&quot; |



