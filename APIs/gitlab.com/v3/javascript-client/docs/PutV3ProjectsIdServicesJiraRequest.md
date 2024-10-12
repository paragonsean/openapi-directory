# Gitlab.PutV3ProjectsIdServicesJiraRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **String** | The URL to the JIRA project which is being linked to this GitLab project, e.g., https://jira.example.com | 
**projectKey** | **String** | The short identifier for your JIRA project, all uppercase, e.g., PROJ | 
**username** | **String** | The username of the user created to be used with GitLab/JIRA | [optional] 
**password** | **String** | The password of the user created to be used with GitLab/JIRA | [optional] 
**jiraIssueTransitionId** | **Number** | The ID of a transition that moves issues to a closed state. You can find this number under the JIRA workflow administration (**Administration &gt; Issues &gt; Workflows**) by selecting **View** under **Operations** of the desired workflow of your project. The ID of each state can be found inside the parenthesis of each transition name under the **Transitions (id)** column ([see screenshot][trans]). By default, this ID is set to &#x60;2&#x60; | [optional] 
**commitEvents** | **String** | Event will be triggered when a commit is created/updated | [optional] 
**mergeRequestEvents** | **String** | Event will be triggered when a merge request is created/updated/merged | [optional] 


