

# ReposUpdateBranchProtectionRequestRequiredPullRequestReviewsDismissalRestrictions

Specify which users and teams can dismiss pull request reviews. Pass an empty `dismissal_restrictions` object to disable. User and team `dismissal_restrictions` are only available for organization-owned repositories. Omit this parameter for personal repositories.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**teams** | **List&lt;String&gt;** | The list of team &#x60;slug&#x60;s with dismissal access |  [optional] |
|**users** | **List&lt;String&gt;** | The list of user &#x60;login&#x60;s with dismissal access |  [optional] |



