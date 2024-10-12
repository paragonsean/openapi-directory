

# ProjectBillingInfo

Encapsulation of billing information for a Google Cloud Console project. A project has at most one associated billing account at a time (but a billing account can be assigned to multiple projects).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAccountName** | **String** | The resource name of the billing account associated with the project, if any. For example, &#x60;billingAccounts/012345-567890-ABCDEF&#x60;. |  [optional] |
|**billingEnabled** | **Boolean** | Output only. True if the project is associated with an open billing account, to which usage on the project is charged. False if the project is associated with a closed billing account, or no billing account at all, and therefore cannot use paid services. |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name for the &#x60;ProjectBillingInfo&#x60;; has the form &#x60;projects/{project_id}/billingInfo&#x60;. For example, the resource name for the billing information for project &#x60;tokyo-rain-123&#x60; would be &#x60;projects/tokyo-rain-123/billingInfo&#x60;. |  [optional] [readonly] |
|**projectId** | **String** | Output only. The ID of the project that this &#x60;ProjectBillingInfo&#x60; represents, such as &#x60;tokyo-rain-123&#x60;. This is a convenience field so that you don&#39;t need to parse the &#x60;name&#x60; field to obtain a project ID. |  [optional] [readonly] |



