

# OutpostConfigRequest

The configuration of your local Amazon EKS cluster on an Amazon Web Services Outpost. Before creating a cluster on an Outpost, review <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-local-cluster-create.html\">Creating a local cluster on an Outpost</a> in the <i>Amazon EKS User Guide</i>. This API isn't available for Amazon EKS clusters on the Amazon Web Services cloud.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**outpostArns** | [**List**](List.md) |  |  |
|**controlPlaneInstanceType** | [**String**](String.md) |  |  |
|**controlPlanePlacement** | [**CreateClusterRequestOutpostConfigControlPlanePlacement**](CreateClusterRequestOutpostConfigControlPlanePlacement.md) |  |  [optional] |



