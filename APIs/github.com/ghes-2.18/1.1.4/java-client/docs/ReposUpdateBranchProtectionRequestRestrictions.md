

# ReposUpdateBranchProtectionRequestRestrictions

Restrict who can push to the protected branch. User, app, and team `restrictions` are only available for organization-owned repositories. Set to `null` to disable.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apps** | **List&lt;String&gt;** | The list of app &#x60;slug&#x60;s with push access |  [optional] |
|**teams** | **List&lt;String&gt;** | The list of team &#x60;slug&#x60;s with push access |  |
|**users** | **List&lt;String&gt;** | The list of user &#x60;login&#x60;s with push access |  |



