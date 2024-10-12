

# OSPolicyAssignmentInstanceFilter

Filters to select target VMs for an assignment. If more than one filter criteria is specified below, a VM will be selected if and only if it satisfies all of them.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**all** | **Boolean** | Target all VMs in the project. If true, no other criteria is permitted. |  [optional] |
|**exclusionLabels** | [**List&lt;OSPolicyAssignmentLabelSet&gt;**](OSPolicyAssignmentLabelSet.md) | List of label sets used for VM exclusion. If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM. |  [optional] |
|**inclusionLabels** | [**List&lt;OSPolicyAssignmentLabelSet&gt;**](OSPolicyAssignmentLabelSet.md) | List of label sets used for VM inclusion. If the list has more than one &#x60;LabelSet&#x60;, the VM is included if any of the label sets are applicable for the VM. |  [optional] |
|**inventories** | [**List&lt;OSPolicyAssignmentInstanceFilterInventory&gt;**](OSPolicyAssignmentInstanceFilterInventory.md) | List of inventories to select VMs. A VM is selected if its inventory data matches at least one of the following inventories. |  [optional] |
|**osShortNames** | **List&lt;String&gt;** | Deprecated. Use the &#x60;inventories&#x60; field instead. A VM is selected if it&#39;s OS short name matches with any of the values provided in this list. |  [optional] |



