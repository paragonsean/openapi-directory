

# GetMembershipGraphResponse

The response message for MembershipsService.GetMembershipGraph.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjacencyList** | [**List&lt;MembershipAdjacencyList&gt;**](MembershipAdjacencyList.md) | The membership graph&#39;s path information represented as an adjacency list. |  [optional] |
|**groups** | [**List&lt;Group&gt;**](Group.md) | The resources representing each group in the adjacency list. Each group in this list can be correlated to a &#39;group&#39; of the MembershipAdjacencyList using the &#39;name&#39; of the Group resource. |  [optional] |



