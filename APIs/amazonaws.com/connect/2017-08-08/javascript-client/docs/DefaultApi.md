# AmazonConnectService.DefaultApi

All URIs are relative to *http://connect.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activateEvaluationForm**](DefaultApi.md#activateEvaluationForm) | **POST** /evaluation-forms/{InstanceId}/{EvaluationFormId}/activate | 
[**associateApprovedOrigin**](DefaultApi.md#associateApprovedOrigin) | **PUT** /instance/{InstanceId}/approved-origin | 
[**associateBot**](DefaultApi.md#associateBot) | **PUT** /instance/{InstanceId}/bot | 
[**associateDefaultVocabulary**](DefaultApi.md#associateDefaultVocabulary) | **PUT** /default-vocabulary/{InstanceId}/{LanguageCode} | 
[**associateInstanceStorageConfig**](DefaultApi.md#associateInstanceStorageConfig) | **PUT** /instance/{InstanceId}/storage-config | 
[**associateLambdaFunction**](DefaultApi.md#associateLambdaFunction) | **PUT** /instance/{InstanceId}/lambda-function | 
[**associateLexBot**](DefaultApi.md#associateLexBot) | **PUT** /instance/{InstanceId}/lex-bot | 
[**associatePhoneNumberContactFlow**](DefaultApi.md#associatePhoneNumberContactFlow) | **PUT** /phone-number/{PhoneNumberId}/contact-flow | 
[**associateQueueQuickConnects**](DefaultApi.md#associateQueueQuickConnects) | **POST** /queues/{InstanceId}/{QueueId}/associate-quick-connects | 
[**associateRoutingProfileQueues**](DefaultApi.md#associateRoutingProfileQueues) | **POST** /routing-profiles/{InstanceId}/{RoutingProfileId}/associate-queues | 
[**associateSecurityKey**](DefaultApi.md#associateSecurityKey) | **PUT** /instance/{InstanceId}/security-key | 
[**claimPhoneNumber**](DefaultApi.md#claimPhoneNumber) | **POST** /phone-number/claim | 
[**createAgentStatus**](DefaultApi.md#createAgentStatus) | **PUT** /agent-status/{InstanceId} | 
[**createContactFlow**](DefaultApi.md#createContactFlow) | **PUT** /contact-flows/{InstanceId} | 
[**createContactFlowModule**](DefaultApi.md#createContactFlowModule) | **PUT** /contact-flow-modules/{InstanceId} | 
[**createEvaluationForm**](DefaultApi.md#createEvaluationForm) | **PUT** /evaluation-forms/{InstanceId} | 
[**createHoursOfOperation**](DefaultApi.md#createHoursOfOperation) | **PUT** /hours-of-operations/{InstanceId} | 
[**createInstance**](DefaultApi.md#createInstance) | **PUT** /instance | 
[**createIntegrationAssociation**](DefaultApi.md#createIntegrationAssociation) | **PUT** /instance/{InstanceId}/integration-associations | 
[**createParticipant**](DefaultApi.md#createParticipant) | **POST** /contact/create-participant | 
[**createPrompt**](DefaultApi.md#createPrompt) | **PUT** /prompts/{InstanceId} | 
[**createQueue**](DefaultApi.md#createQueue) | **PUT** /queues/{InstanceId} | 
[**createQuickConnect**](DefaultApi.md#createQuickConnect) | **PUT** /quick-connects/{InstanceId} | 
[**createRoutingProfile**](DefaultApi.md#createRoutingProfile) | **PUT** /routing-profiles/{InstanceId} | 
[**createRule**](DefaultApi.md#createRule) | **POST** /rules/{InstanceId} | 
[**createSecurityProfile**](DefaultApi.md#createSecurityProfile) | **PUT** /security-profiles/{InstanceId} | 
[**createTaskTemplate**](DefaultApi.md#createTaskTemplate) | **PUT** /instance/{InstanceId}/task/template | 
[**createTrafficDistributionGroup**](DefaultApi.md#createTrafficDistributionGroup) | **PUT** /traffic-distribution-group | 
[**createUseCase**](DefaultApi.md#createUseCase) | **PUT** /instance/{InstanceId}/integration-associations/{IntegrationAssociationId}/use-cases | 
[**createUser**](DefaultApi.md#createUser) | **PUT** /users/{InstanceId} | 
[**createUserHierarchyGroup**](DefaultApi.md#createUserHierarchyGroup) | **PUT** /user-hierarchy-groups/{InstanceId} | 
[**createVocabulary**](DefaultApi.md#createVocabulary) | **POST** /vocabulary/{InstanceId} | 
[**deactivateEvaluationForm**](DefaultApi.md#deactivateEvaluationForm) | **POST** /evaluation-forms/{InstanceId}/{EvaluationFormId}/deactivate | 
[**deleteContactEvaluation**](DefaultApi.md#deleteContactEvaluation) | **DELETE** /contact-evaluations/{InstanceId}/{EvaluationId} | 
[**deleteContactFlow**](DefaultApi.md#deleteContactFlow) | **DELETE** /contact-flows/{InstanceId}/{ContactFlowId} | 
[**deleteContactFlowModule**](DefaultApi.md#deleteContactFlowModule) | **DELETE** /contact-flow-modules/{InstanceId}/{ContactFlowModuleId} | 
[**deleteEvaluationForm**](DefaultApi.md#deleteEvaluationForm) | **DELETE** /evaluation-forms/{InstanceId}/{EvaluationFormId} | 
[**deleteHoursOfOperation**](DefaultApi.md#deleteHoursOfOperation) | **DELETE** /hours-of-operations/{InstanceId}/{HoursOfOperationId} | 
[**deleteInstance**](DefaultApi.md#deleteInstance) | **DELETE** /instance/{InstanceId} | 
[**deleteIntegrationAssociation**](DefaultApi.md#deleteIntegrationAssociation) | **DELETE** /instance/{InstanceId}/integration-associations/{IntegrationAssociationId} | 
[**deletePrompt**](DefaultApi.md#deletePrompt) | **DELETE** /prompts/{InstanceId}/{PromptId} | 
[**deleteQueue**](DefaultApi.md#deleteQueue) | **DELETE** /queues/{InstanceId}/{QueueId} | 
[**deleteQuickConnect**](DefaultApi.md#deleteQuickConnect) | **DELETE** /quick-connects/{InstanceId}/{QuickConnectId} | 
[**deleteRoutingProfile**](DefaultApi.md#deleteRoutingProfile) | **DELETE** /routing-profiles/{InstanceId}/{RoutingProfileId} | 
[**deleteRule**](DefaultApi.md#deleteRule) | **DELETE** /rules/{InstanceId}/{RuleId} | 
[**deleteSecurityProfile**](DefaultApi.md#deleteSecurityProfile) | **DELETE** /security-profiles/{InstanceId}/{SecurityProfileId} | 
[**deleteTaskTemplate**](DefaultApi.md#deleteTaskTemplate) | **DELETE** /instance/{InstanceId}/task/template/{TaskTemplateId} | 
[**deleteTrafficDistributionGroup**](DefaultApi.md#deleteTrafficDistributionGroup) | **DELETE** /traffic-distribution-group/{TrafficDistributionGroupId} | 
[**deleteUseCase**](DefaultApi.md#deleteUseCase) | **DELETE** /instance/{InstanceId}/integration-associations/{IntegrationAssociationId}/use-cases/{UseCaseId} | 
[**deleteUser**](DefaultApi.md#deleteUser) | **DELETE** /users/{InstanceId}/{UserId} | 
[**deleteUserHierarchyGroup**](DefaultApi.md#deleteUserHierarchyGroup) | **DELETE** /user-hierarchy-groups/{InstanceId}/{HierarchyGroupId} | 
[**deleteVocabulary**](DefaultApi.md#deleteVocabulary) | **POST** /vocabulary-remove/{InstanceId}/{VocabularyId} | 
[**describeAgentStatus**](DefaultApi.md#describeAgentStatus) | **GET** /agent-status/{InstanceId}/{AgentStatusId} | 
[**describeContact**](DefaultApi.md#describeContact) | **GET** /contacts/{InstanceId}/{ContactId} | 
[**describeContactEvaluation**](DefaultApi.md#describeContactEvaluation) | **GET** /contact-evaluations/{InstanceId}/{EvaluationId} | 
[**describeContactFlow**](DefaultApi.md#describeContactFlow) | **GET** /contact-flows/{InstanceId}/{ContactFlowId} | 
[**describeContactFlowModule**](DefaultApi.md#describeContactFlowModule) | **GET** /contact-flow-modules/{InstanceId}/{ContactFlowModuleId} | 
[**describeEvaluationForm**](DefaultApi.md#describeEvaluationForm) | **GET** /evaluation-forms/{InstanceId}/{EvaluationFormId} | 
[**describeHoursOfOperation**](DefaultApi.md#describeHoursOfOperation) | **GET** /hours-of-operations/{InstanceId}/{HoursOfOperationId} | 
[**describeInstance**](DefaultApi.md#describeInstance) | **GET** /instance/{InstanceId} | 
[**describeInstanceAttribute**](DefaultApi.md#describeInstanceAttribute) | **GET** /instance/{InstanceId}/attribute/{AttributeType} | 
[**describeInstanceStorageConfig**](DefaultApi.md#describeInstanceStorageConfig) | **GET** /instance/{InstanceId}/storage-config/{AssociationId}#resourceType | 
[**describePhoneNumber**](DefaultApi.md#describePhoneNumber) | **GET** /phone-number/{PhoneNumberId} | 
[**describePrompt**](DefaultApi.md#describePrompt) | **GET** /prompts/{InstanceId}/{PromptId} | 
[**describeQueue**](DefaultApi.md#describeQueue) | **GET** /queues/{InstanceId}/{QueueId} | 
[**describeQuickConnect**](DefaultApi.md#describeQuickConnect) | **GET** /quick-connects/{InstanceId}/{QuickConnectId} | 
[**describeRoutingProfile**](DefaultApi.md#describeRoutingProfile) | **GET** /routing-profiles/{InstanceId}/{RoutingProfileId} | 
[**describeRule**](DefaultApi.md#describeRule) | **GET** /rules/{InstanceId}/{RuleId} | 
[**describeSecurityProfile**](DefaultApi.md#describeSecurityProfile) | **GET** /security-profiles/{InstanceId}/{SecurityProfileId} | 
[**describeTrafficDistributionGroup**](DefaultApi.md#describeTrafficDistributionGroup) | **GET** /traffic-distribution-group/{TrafficDistributionGroupId} | 
[**describeUser**](DefaultApi.md#describeUser) | **GET** /users/{InstanceId}/{UserId} | 
[**describeUserHierarchyGroup**](DefaultApi.md#describeUserHierarchyGroup) | **GET** /user-hierarchy-groups/{InstanceId}/{HierarchyGroupId} | 
[**describeUserHierarchyStructure**](DefaultApi.md#describeUserHierarchyStructure) | **GET** /user-hierarchy-structure/{InstanceId} | 
[**describeVocabulary**](DefaultApi.md#describeVocabulary) | **GET** /vocabulary/{InstanceId}/{VocabularyId} | 
[**disassociateApprovedOrigin**](DefaultApi.md#disassociateApprovedOrigin) | **DELETE** /instance/{InstanceId}/approved-origin#origin | 
[**disassociateBot**](DefaultApi.md#disassociateBot) | **POST** /instance/{InstanceId}/bot | 
[**disassociateInstanceStorageConfig**](DefaultApi.md#disassociateInstanceStorageConfig) | **DELETE** /instance/{InstanceId}/storage-config/{AssociationId}#resourceType | 
[**disassociateLambdaFunction**](DefaultApi.md#disassociateLambdaFunction) | **DELETE** /instance/{InstanceId}/lambda-function#functionArn | 
[**disassociateLexBot**](DefaultApi.md#disassociateLexBot) | **DELETE** /instance/{InstanceId}/lex-bot#botName&amp;lexRegion | 
[**disassociatePhoneNumberContactFlow**](DefaultApi.md#disassociatePhoneNumberContactFlow) | **DELETE** /phone-number/{PhoneNumberId}/contact-flow#instanceId | 
[**disassociateQueueQuickConnects**](DefaultApi.md#disassociateQueueQuickConnects) | **POST** /queues/{InstanceId}/{QueueId}/disassociate-quick-connects | 
[**disassociateRoutingProfileQueues**](DefaultApi.md#disassociateRoutingProfileQueues) | **POST** /routing-profiles/{InstanceId}/{RoutingProfileId}/disassociate-queues | 
[**disassociateSecurityKey**](DefaultApi.md#disassociateSecurityKey) | **DELETE** /instance/{InstanceId}/security-key/{AssociationId} | 
[**dismissUserContact**](DefaultApi.md#dismissUserContact) | **POST** /users/{InstanceId}/{UserId}/contact | 
[**getContactAttributes**](DefaultApi.md#getContactAttributes) | **GET** /contact/attributes/{InstanceId}/{InitialContactId} | 
[**getCurrentMetricData**](DefaultApi.md#getCurrentMetricData) | **POST** /metrics/current/{InstanceId} | 
[**getCurrentUserData**](DefaultApi.md#getCurrentUserData) | **POST** /metrics/userdata/{InstanceId} | 
[**getFederationToken**](DefaultApi.md#getFederationToken) | **GET** /user/federate/{InstanceId} | 
[**getMetricData**](DefaultApi.md#getMetricData) | **POST** /metrics/historical/{InstanceId} | 
[**getMetricDataV2**](DefaultApi.md#getMetricDataV2) | **POST** /metrics/data | 
[**getPromptFile**](DefaultApi.md#getPromptFile) | **GET** /prompts/{InstanceId}/{PromptId}/file | 
[**getTaskTemplate**](DefaultApi.md#getTaskTemplate) | **GET** /instance/{InstanceId}/task/template/{TaskTemplateId} | 
[**getTrafficDistribution**](DefaultApi.md#getTrafficDistribution) | **GET** /traffic-distribution/{Id} | 
[**listAgentStatuses**](DefaultApi.md#listAgentStatuses) | **GET** /agent-status/{InstanceId} | 
[**listApprovedOrigins**](DefaultApi.md#listApprovedOrigins) | **GET** /instance/{InstanceId}/approved-origins | 
[**listBots**](DefaultApi.md#listBots) | **GET** /instance/{InstanceId}/bots#lexVersion | 
[**listContactEvaluations**](DefaultApi.md#listContactEvaluations) | **GET** /contact-evaluations/{InstanceId}#contactId | 
[**listContactFlowModules**](DefaultApi.md#listContactFlowModules) | **GET** /contact-flow-modules-summary/{InstanceId} | 
[**listContactFlows**](DefaultApi.md#listContactFlows) | **GET** /contact-flows-summary/{InstanceId} | 
[**listContactReferences**](DefaultApi.md#listContactReferences) | **GET** /contact/references/{InstanceId}/{ContactId}#referenceTypes | 
[**listDefaultVocabularies**](DefaultApi.md#listDefaultVocabularies) | **POST** /default-vocabulary-summary/{InstanceId} | 
[**listEvaluationFormVersions**](DefaultApi.md#listEvaluationFormVersions) | **GET** /evaluation-forms/{InstanceId}/{EvaluationFormId}/versions | 
[**listEvaluationForms**](DefaultApi.md#listEvaluationForms) | **GET** /evaluation-forms/{InstanceId} | 
[**listHoursOfOperations**](DefaultApi.md#listHoursOfOperations) | **GET** /hours-of-operations-summary/{InstanceId} | 
[**listInstanceAttributes**](DefaultApi.md#listInstanceAttributes) | **GET** /instance/{InstanceId}/attributes | 
[**listInstanceStorageConfigs**](DefaultApi.md#listInstanceStorageConfigs) | **GET** /instance/{InstanceId}/storage-configs#resourceType | 
[**listInstances**](DefaultApi.md#listInstances) | **GET** /instance | 
[**listIntegrationAssociations**](DefaultApi.md#listIntegrationAssociations) | **GET** /instance/{InstanceId}/integration-associations | 
[**listLambdaFunctions**](DefaultApi.md#listLambdaFunctions) | **GET** /instance/{InstanceId}/lambda-functions | 
[**listLexBots**](DefaultApi.md#listLexBots) | **GET** /instance/{InstanceId}/lex-bots | 
[**listPhoneNumbers**](DefaultApi.md#listPhoneNumbers) | **GET** /phone-numbers-summary/{InstanceId} | 
[**listPhoneNumbersV2**](DefaultApi.md#listPhoneNumbersV2) | **POST** /phone-number/list | 
[**listPrompts**](DefaultApi.md#listPrompts) | **GET** /prompts-summary/{InstanceId} | 
[**listQueueQuickConnects**](DefaultApi.md#listQueueQuickConnects) | **GET** /queues/{InstanceId}/{QueueId}/quick-connects | 
[**listQueues**](DefaultApi.md#listQueues) | **GET** /queues-summary/{InstanceId} | 
[**listQuickConnects**](DefaultApi.md#listQuickConnects) | **GET** /quick-connects/{InstanceId} | 
[**listRoutingProfileQueues**](DefaultApi.md#listRoutingProfileQueues) | **GET** /routing-profiles/{InstanceId}/{RoutingProfileId}/queues | 
[**listRoutingProfiles**](DefaultApi.md#listRoutingProfiles) | **GET** /routing-profiles-summary/{InstanceId} | 
[**listRules**](DefaultApi.md#listRules) | **GET** /rules/{InstanceId} | 
[**listSecurityKeys**](DefaultApi.md#listSecurityKeys) | **GET** /instance/{InstanceId}/security-keys | 
[**listSecurityProfilePermissions**](DefaultApi.md#listSecurityProfilePermissions) | **GET** /security-profiles-permissions/{InstanceId}/{SecurityProfileId} | 
[**listSecurityProfiles**](DefaultApi.md#listSecurityProfiles) | **GET** /security-profiles-summary/{InstanceId} | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**listTaskTemplates**](DefaultApi.md#listTaskTemplates) | **GET** /instance/{InstanceId}/task/template | 
[**listTrafficDistributionGroups**](DefaultApi.md#listTrafficDistributionGroups) | **GET** /traffic-distribution-groups | 
[**listUseCases**](DefaultApi.md#listUseCases) | **GET** /instance/{InstanceId}/integration-associations/{IntegrationAssociationId}/use-cases | 
[**listUserHierarchyGroups**](DefaultApi.md#listUserHierarchyGroups) | **GET** /user-hierarchy-groups-summary/{InstanceId} | 
[**listUsers**](DefaultApi.md#listUsers) | **GET** /users-summary/{InstanceId} | 
[**monitorContact**](DefaultApi.md#monitorContact) | **POST** /contact/monitor | 
[**putUserStatus**](DefaultApi.md#putUserStatus) | **PUT** /users/{InstanceId}/{UserId}/status | 
[**releasePhoneNumber**](DefaultApi.md#releasePhoneNumber) | **DELETE** /phone-number/{PhoneNumberId} | 
[**replicateInstance**](DefaultApi.md#replicateInstance) | **POST** /instance/{InstanceId}/replicate | 
[**resumeContactRecording**](DefaultApi.md#resumeContactRecording) | **POST** /contact/resume-recording | 
[**searchAvailablePhoneNumbers**](DefaultApi.md#searchAvailablePhoneNumbers) | **POST** /phone-number/search-available | 
[**searchHoursOfOperations**](DefaultApi.md#searchHoursOfOperations) | **POST** /search-hours-of-operations | 
[**searchPrompts**](DefaultApi.md#searchPrompts) | **POST** /search-prompts | 
[**searchQueues**](DefaultApi.md#searchQueues) | **POST** /search-queues | 
[**searchQuickConnects**](DefaultApi.md#searchQuickConnects) | **POST** /search-quick-connects | 
[**searchResourceTags**](DefaultApi.md#searchResourceTags) | **POST** /search-resource-tags | 
[**searchRoutingProfiles**](DefaultApi.md#searchRoutingProfiles) | **POST** /search-routing-profiles | 
[**searchSecurityProfiles**](DefaultApi.md#searchSecurityProfiles) | **POST** /search-security-profiles | 
[**searchUsers**](DefaultApi.md#searchUsers) | **POST** /search-users | 
[**searchVocabularies**](DefaultApi.md#searchVocabularies) | **POST** /vocabulary-summary/{InstanceId} | 
[**startChatContact**](DefaultApi.md#startChatContact) | **PUT** /contact/chat | 
[**startContactEvaluation**](DefaultApi.md#startContactEvaluation) | **PUT** /contact-evaluations/{InstanceId} | 
[**startContactRecording**](DefaultApi.md#startContactRecording) | **POST** /contact/start-recording | 
[**startContactStreaming**](DefaultApi.md#startContactStreaming) | **POST** /contact/start-streaming | 
[**startOutboundVoiceContact**](DefaultApi.md#startOutboundVoiceContact) | **PUT** /contact/outbound-voice | 
[**startTaskContact**](DefaultApi.md#startTaskContact) | **PUT** /contact/task | 
[**stopContact**](DefaultApi.md#stopContact) | **POST** /contact/stop | 
[**stopContactRecording**](DefaultApi.md#stopContactRecording) | **POST** /contact/stop-recording | 
[**stopContactStreaming**](DefaultApi.md#stopContactStreaming) | **POST** /contact/stop-streaming | 
[**submitContactEvaluation**](DefaultApi.md#submitContactEvaluation) | **POST** /contact-evaluations/{InstanceId}/{EvaluationId}/submit | 
[**suspendContactRecording**](DefaultApi.md#suspendContactRecording) | **POST** /contact/suspend-recording | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**transferContact**](DefaultApi.md#transferContact) | **POST** /contact/transfer | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateAgentStatus**](DefaultApi.md#updateAgentStatus) | **POST** /agent-status/{InstanceId}/{AgentStatusId} | 
[**updateContact**](DefaultApi.md#updateContact) | **POST** /contacts/{InstanceId}/{ContactId} | 
[**updateContactAttributes**](DefaultApi.md#updateContactAttributes) | **POST** /contact/attributes | 
[**updateContactEvaluation**](DefaultApi.md#updateContactEvaluation) | **POST** /contact-evaluations/{InstanceId}/{EvaluationId} | 
[**updateContactFlowContent**](DefaultApi.md#updateContactFlowContent) | **POST** /contact-flows/{InstanceId}/{ContactFlowId}/content | 
[**updateContactFlowMetadata**](DefaultApi.md#updateContactFlowMetadata) | **POST** /contact-flows/{InstanceId}/{ContactFlowId}/metadata | 
[**updateContactFlowModuleContent**](DefaultApi.md#updateContactFlowModuleContent) | **POST** /contact-flow-modules/{InstanceId}/{ContactFlowModuleId}/content | 
[**updateContactFlowModuleMetadata**](DefaultApi.md#updateContactFlowModuleMetadata) | **POST** /contact-flow-modules/{InstanceId}/{ContactFlowModuleId}/metadata | 
[**updateContactFlowName**](DefaultApi.md#updateContactFlowName) | **POST** /contact-flows/{InstanceId}/{ContactFlowId}/name | 
[**updateContactSchedule**](DefaultApi.md#updateContactSchedule) | **POST** /contact/schedule | 
[**updateEvaluationForm**](DefaultApi.md#updateEvaluationForm) | **PUT** /evaluation-forms/{InstanceId}/{EvaluationFormId} | 
[**updateHoursOfOperation**](DefaultApi.md#updateHoursOfOperation) | **POST** /hours-of-operations/{InstanceId}/{HoursOfOperationId} | 
[**updateInstanceAttribute**](DefaultApi.md#updateInstanceAttribute) | **POST** /instance/{InstanceId}/attribute/{AttributeType} | 
[**updateInstanceStorageConfig**](DefaultApi.md#updateInstanceStorageConfig) | **POST** /instance/{InstanceId}/storage-config/{AssociationId}#resourceType | 
[**updateParticipantRoleConfig**](DefaultApi.md#updateParticipantRoleConfig) | **PUT** /contact/participant-role-config/{InstanceId}/{ContactId} | 
[**updatePhoneNumber**](DefaultApi.md#updatePhoneNumber) | **PUT** /phone-number/{PhoneNumberId} | 
[**updatePrompt**](DefaultApi.md#updatePrompt) | **POST** /prompts/{InstanceId}/{PromptId} | 
[**updateQueueHoursOfOperation**](DefaultApi.md#updateQueueHoursOfOperation) | **POST** /queues/{InstanceId}/{QueueId}/hours-of-operation | 
[**updateQueueMaxContacts**](DefaultApi.md#updateQueueMaxContacts) | **POST** /queues/{InstanceId}/{QueueId}/max-contacts | 
[**updateQueueName**](DefaultApi.md#updateQueueName) | **POST** /queues/{InstanceId}/{QueueId}/name | 
[**updateQueueOutboundCallerConfig**](DefaultApi.md#updateQueueOutboundCallerConfig) | **POST** /queues/{InstanceId}/{QueueId}/outbound-caller-config | 
[**updateQueueStatus**](DefaultApi.md#updateQueueStatus) | **POST** /queues/{InstanceId}/{QueueId}/status | 
[**updateQuickConnectConfig**](DefaultApi.md#updateQuickConnectConfig) | **POST** /quick-connects/{InstanceId}/{QuickConnectId}/config | 
[**updateQuickConnectName**](DefaultApi.md#updateQuickConnectName) | **POST** /quick-connects/{InstanceId}/{QuickConnectId}/name | 
[**updateRoutingProfileAgentAvailabilityTimer**](DefaultApi.md#updateRoutingProfileAgentAvailabilityTimer) | **POST** /routing-profiles/{InstanceId}/{RoutingProfileId}/agent-availability-timer | 
[**updateRoutingProfileConcurrency**](DefaultApi.md#updateRoutingProfileConcurrency) | **POST** /routing-profiles/{InstanceId}/{RoutingProfileId}/concurrency | 
[**updateRoutingProfileDefaultOutboundQueue**](DefaultApi.md#updateRoutingProfileDefaultOutboundQueue) | **POST** /routing-profiles/{InstanceId}/{RoutingProfileId}/default-outbound-queue | 
[**updateRoutingProfileName**](DefaultApi.md#updateRoutingProfileName) | **POST** /routing-profiles/{InstanceId}/{RoutingProfileId}/name | 
[**updateRoutingProfileQueues**](DefaultApi.md#updateRoutingProfileQueues) | **POST** /routing-profiles/{InstanceId}/{RoutingProfileId}/queues | 
[**updateRule**](DefaultApi.md#updateRule) | **PUT** /rules/{InstanceId}/{RuleId} | 
[**updateSecurityProfile**](DefaultApi.md#updateSecurityProfile) | **POST** /security-profiles/{InstanceId}/{SecurityProfileId} | 
[**updateTaskTemplate**](DefaultApi.md#updateTaskTemplate) | **POST** /instance/{InstanceId}/task/template/{TaskTemplateId} | 
[**updateTrafficDistribution**](DefaultApi.md#updateTrafficDistribution) | **PUT** /traffic-distribution/{Id} | 
[**updateUserHierarchy**](DefaultApi.md#updateUserHierarchy) | **POST** /users/{InstanceId}/{UserId}/hierarchy | 
[**updateUserHierarchyGroupName**](DefaultApi.md#updateUserHierarchyGroupName) | **POST** /user-hierarchy-groups/{InstanceId}/{HierarchyGroupId}/name | 
[**updateUserHierarchyStructure**](DefaultApi.md#updateUserHierarchyStructure) | **POST** /user-hierarchy-structure/{InstanceId} | 
[**updateUserIdentityInfo**](DefaultApi.md#updateUserIdentityInfo) | **POST** /users/{InstanceId}/{UserId}/identity-info | 
[**updateUserPhoneConfig**](DefaultApi.md#updateUserPhoneConfig) | **POST** /users/{InstanceId}/{UserId}/phone-config | 
[**updateUserRoutingProfile**](DefaultApi.md#updateUserRoutingProfile) | **POST** /users/{InstanceId}/{UserId}/routing-profile | 
[**updateUserSecurityProfiles**](DefaultApi.md#updateUserSecurityProfiles) | **POST** /users/{InstanceId}/{UserId}/security-profiles | 



## activateEvaluationForm

> ActivateEvaluationFormResponse activateEvaluationForm(instanceId, evaluationFormId, activateEvaluationFormRequest, opts)



Activates an evaluation form in the specified Amazon Connect instance. After the evaluation form is activated, it is available to start new evaluations based on the form. 

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let evaluationFormId = "evaluationFormId_example"; // String | The unique identifier for the evaluation form.
let activateEvaluationFormRequest = new AmazonConnectService.ActivateEvaluationFormRequest(); // ActivateEvaluationFormRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.activateEvaluationForm(instanceId, evaluationFormId, activateEvaluationFormRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **evaluationFormId** | **String**| The unique identifier for the evaluation form. | 
 **activateEvaluationFormRequest** | [**ActivateEvaluationFormRequest**](ActivateEvaluationFormRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ActivateEvaluationFormResponse**](ActivateEvaluationFormResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateApprovedOrigin

> associateApprovedOrigin(instanceId, associateApprovedOriginRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Associates an approved origin to an Amazon Connect instance.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let associateApprovedOriginRequest = new AmazonConnectService.AssociateApprovedOriginRequest(); // AssociateApprovedOriginRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateApprovedOrigin(instanceId, associateApprovedOriginRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **associateApprovedOriginRequest** | [**AssociateApprovedOriginRequest**](AssociateApprovedOriginRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateBot

> associateBot(instanceId, associateBotRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Allows the specified Amazon Connect instance to access the specified Amazon Lex or Amazon Lex V2 bot.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let associateBotRequest = new AmazonConnectService.AssociateBotRequest(); // AssociateBotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateBot(instanceId, associateBotRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **associateBotRequest** | [**AssociateBotRequest**](AssociateBotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateDefaultVocabulary

> Object associateDefaultVocabulary(instanceId, languageCode, associateDefaultVocabularyRequest, opts)



Associates an existing vocabulary as the default. Contact Lens for Amazon Connect uses the vocabulary in post-call and real-time analysis sessions for the given language.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let languageCode = "languageCode_example"; // String | The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html\">What is Amazon Transcribe?</a> 
let associateDefaultVocabularyRequest = new AmazonConnectService.AssociateDefaultVocabularyRequest(); // AssociateDefaultVocabularyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateDefaultVocabulary(instanceId, languageCode, associateDefaultVocabularyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **languageCode** | **String**| The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html\&quot;&gt;What is Amazon Transcribe?&lt;/a&gt;  | 
 **associateDefaultVocabularyRequest** | [**AssociateDefaultVocabularyRequest**](AssociateDefaultVocabularyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateInstanceStorageConfig

> AssociateInstanceStorageConfigResponse associateInstanceStorageConfig(instanceId, associateInstanceStorageConfigRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Associates a storage resource type for the first time. You can only associate one type of storage configuration in a single call. This means, for example, that you can&#39;t define an instance with multiple S3 buckets for storing chat transcripts.&lt;/p&gt; &lt;p&gt;This API does not create a resource that doesn&#39;t exist. It only associates it to the instance. Ensure that the resource being specified in the storage configuration, like an S3 bucket, exists when being used for association.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let associateInstanceStorageConfigRequest = new AmazonConnectService.AssociateInstanceStorageConfigRequest(); // AssociateInstanceStorageConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateInstanceStorageConfig(instanceId, associateInstanceStorageConfigRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **associateInstanceStorageConfigRequest** | [**AssociateInstanceStorageConfigRequest**](AssociateInstanceStorageConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateInstanceStorageConfigResponse**](AssociateInstanceStorageConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateLambdaFunction

> associateLambdaFunction(instanceId, associateLambdaFunctionRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Allows the specified Amazon Connect instance to access the specified Lambda function.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let associateLambdaFunctionRequest = new AmazonConnectService.AssociateLambdaFunctionRequest(); // AssociateLambdaFunctionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateLambdaFunction(instanceId, associateLambdaFunctionRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **associateLambdaFunctionRequest** | [**AssociateLambdaFunctionRequest**](AssociateLambdaFunctionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateLexBot

> associateLexBot(instanceId, associateLexBotRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Allows the specified Amazon Connect instance to access the specified Amazon Lex V1 bot. This API only supports the association of Amazon Lex V1 bots.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let associateLexBotRequest = new AmazonConnectService.AssociateLexBotRequest(); // AssociateLexBotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateLexBot(instanceId, associateLexBotRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **associateLexBotRequest** | [**AssociateLexBotRequest**](AssociateLexBotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associatePhoneNumberContactFlow

> associatePhoneNumberContactFlow(phoneNumberId, associatePhoneNumberContactFlowRequest, opts)



&lt;p&gt;Associates a flow with a phone number claimed to your Amazon Connect instance.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the number is claimed to a traffic distribution group, and you are calling this API using an instance in the Amazon Web Services Region where the traffic distribution group was created, you can use either a full phone number ARN or UUID value for the &lt;code&gt;PhoneNumberId&lt;/code&gt; URI request parameter. However, if the number is claimed to a traffic distribution group and you are calling this API using an instance in the alternate Amazon Web Services Region associated with the traffic distribution group, you must provide a full phone number ARN. If a UUID is provided in this scenario, you will receive a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let phoneNumberId = "phoneNumberId_example"; // String | A unique identifier for the phone number.
let associatePhoneNumberContactFlowRequest = new AmazonConnectService.AssociatePhoneNumberContactFlowRequest(); // AssociatePhoneNumberContactFlowRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associatePhoneNumberContactFlow(phoneNumberId, associatePhoneNumberContactFlowRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phoneNumberId** | **String**| A unique identifier for the phone number. | 
 **associatePhoneNumberContactFlowRequest** | [**AssociatePhoneNumberContactFlowRequest**](AssociatePhoneNumberContactFlowRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateQueueQuickConnects

> associateQueueQuickConnects(instanceId, queueId, associateQueueQuickConnectsRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Associates a set of quick connects with a queue.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let queueId = "queueId_example"; // String | The identifier for the queue.
let associateQueueQuickConnectsRequest = new AmazonConnectService.AssociateQueueQuickConnectsRequest(); // AssociateQueueQuickConnectsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateQueueQuickConnects(instanceId, queueId, associateQueueQuickConnectsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **queueId** | **String**| The identifier for the queue. | 
 **associateQueueQuickConnectsRequest** | [**AssociateQueueQuickConnectsRequest**](AssociateQueueQuickConnectsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateRoutingProfileQueues

> associateRoutingProfileQueues(instanceId, routingProfileId, associateRoutingProfileQueuesRequest, opts)



Associates a set of queues with a routing profile.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let routingProfileId = "routingProfileId_example"; // String | The identifier of the routing profile.
let associateRoutingProfileQueuesRequest = new AmazonConnectService.AssociateRoutingProfileQueuesRequest(); // AssociateRoutingProfileQueuesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateRoutingProfileQueues(instanceId, routingProfileId, associateRoutingProfileQueuesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **routingProfileId** | **String**| The identifier of the routing profile. | 
 **associateRoutingProfileQueuesRequest** | [**AssociateRoutingProfileQueuesRequest**](AssociateRoutingProfileQueuesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateSecurityKey

> AssociateSecurityKeyResponse associateSecurityKey(instanceId, associateSecurityKeyRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Associates a security key to the instance.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let associateSecurityKeyRequest = new AmazonConnectService.AssociateSecurityKeyRequest(); // AssociateSecurityKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateSecurityKey(instanceId, associateSecurityKeyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **associateSecurityKeyRequest** | [**AssociateSecurityKeyRequest**](AssociateSecurityKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateSecurityKeyResponse**](AssociateSecurityKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## claimPhoneNumber

> ClaimPhoneNumberResponse claimPhoneNumber(claimPhoneNumberRequest, opts)



&lt;p&gt;Claims an available phone number to your Amazon Connect instance or traffic distribution group. You can call this API only in the same Amazon Web Services Region where the Amazon Connect instance or traffic distribution group was created.&lt;/p&gt; &lt;p&gt;For more information about how to use this operation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/claim-phone-number.html\&quot;&gt;Claim a phone number in your country&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/claim-phone-numbers-traffic-distribution-groups.html\&quot;&gt;Claim phone numbers to traffic distribution groups&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt;You can call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchAvailablePhoneNumbers.html\&quot;&gt;SearchAvailablePhoneNumbers&lt;/a&gt; API for available phone numbers that you can claim. Call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribePhoneNumber.html\&quot;&gt;DescribePhoneNumber&lt;/a&gt; API to verify the status of a previous &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html\&quot;&gt;ClaimPhoneNumber&lt;/a&gt; operation.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If you plan to claim and release numbers frequently during a 30 day period, contact us for a service quota exception. Otherwise, it is possible you will be blocked from claiming and releasing any more numbers until 30 days past the oldest number released has expired.&lt;/p&gt; &lt;p&gt;By default you can claim and release up to 200% of your maximum number of active phone numbers during any 30 day period. If you claim and release phone numbers using the UI or API during a rolling 30 day cycle that exceeds 200% of your phone number service level quota, you will be blocked from claiming any more numbers until 30 days past the oldest number released has expired. &lt;/p&gt; &lt;p&gt;For example, if you already have 99 claimed numbers and a service level quota of 99 phone numbers, and in any 30 day period you release 99, claim 99, and then release 99, you will have exceeded the 200% limit. At that point you are blocked from claiming any more numbers until you open an Amazon Web Services support ticket.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let claimPhoneNumberRequest = new AmazonConnectService.ClaimPhoneNumberRequest(); // ClaimPhoneNumberRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.claimPhoneNumber(claimPhoneNumberRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **claimPhoneNumberRequest** | [**ClaimPhoneNumberRequest**](ClaimPhoneNumberRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ClaimPhoneNumberResponse**](ClaimPhoneNumberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAgentStatus

> CreateAgentStatusResponse createAgentStatus(instanceId, createAgentStatusRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Creates an agent status for the specified Amazon Connect instance.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createAgentStatusRequest = new AmazonConnectService.CreateAgentStatusRequest(); // CreateAgentStatusRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAgentStatus(instanceId, createAgentStatusRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createAgentStatusRequest** | [**CreateAgentStatusRequest**](CreateAgentStatusRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAgentStatusResponse**](CreateAgentStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createContactFlow

> CreateContactFlowResponse createContactFlow(instanceId, createContactFlowRequest, opts)



&lt;p&gt;Creates a flow for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;You can also create and update flows using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/flow-language.html\&quot;&gt;Amazon Connect Flow language&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance.
let createContactFlowRequest = new AmazonConnectService.CreateContactFlowRequest(); // CreateContactFlowRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createContactFlow(instanceId, createContactFlowRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. | 
 **createContactFlowRequest** | [**CreateContactFlowRequest**](CreateContactFlowRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateContactFlowResponse**](CreateContactFlowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createContactFlowModule

> CreateContactFlowModuleResponse createContactFlowModule(instanceId, createContactFlowModuleRequest, opts)



Creates a flow module for the specified Amazon Connect instance. 

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createContactFlowModuleRequest = new AmazonConnectService.CreateContactFlowModuleRequest(); // CreateContactFlowModuleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createContactFlowModule(instanceId, createContactFlowModuleRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createContactFlowModuleRequest** | [**CreateContactFlowModuleRequest**](CreateContactFlowModuleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateContactFlowModuleResponse**](CreateContactFlowModuleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createEvaluationForm

> CreateEvaluationFormResponse createEvaluationForm(instanceId, createEvaluationFormRequest, opts)



Creates an evaluation form in the specified Amazon Connect instance. The form can be used to define questions related to agent performance, and create sections to organize such questions. Question and section identifiers cannot be duplicated within the same evaluation form.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createEvaluationFormRequest = new AmazonConnectService.CreateEvaluationFormRequest(); // CreateEvaluationFormRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createEvaluationForm(instanceId, createEvaluationFormRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createEvaluationFormRequest** | [**CreateEvaluationFormRequest**](CreateEvaluationFormRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateEvaluationFormResponse**](CreateEvaluationFormResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createHoursOfOperation

> CreateHoursOfOperationResponse createHoursOfOperation(instanceId, createHoursOfOperationRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Creates hours of operation. &lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createHoursOfOperationRequest = new AmazonConnectService.CreateHoursOfOperationRequest(); // CreateHoursOfOperationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createHoursOfOperation(instanceId, createHoursOfOperationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createHoursOfOperationRequest** | [**CreateHoursOfOperationRequest**](CreateHoursOfOperationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateHoursOfOperationResponse**](CreateHoursOfOperationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createInstance

> CreateInstanceResponse createInstance(createInstanceRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Initiates an Amazon Connect instance with all the supported channels enabled. It does not attach any storage, such as Amazon Simple Storage Service (Amazon S3) or Amazon Kinesis. It also does not allow for any configurations on features, such as Contact Lens for Amazon Connect. &lt;/p&gt; &lt;p&gt;Amazon Connect enforces a limit on the total number of instances that you can create or delete in 30 days. If you exceed this limit, you will get an error message indicating there has been an excessive number of attempts at creating or deleting instances. You must wait 30 days before you can restart creating and deleting instances in your account.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let createInstanceRequest = new AmazonConnectService.CreateInstanceRequest(); // CreateInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createInstance(createInstanceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createInstanceRequest** | [**CreateInstanceRequest**](CreateInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateInstanceResponse**](CreateInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createIntegrationAssociation

> CreateIntegrationAssociationResponse createIntegrationAssociation(instanceId, createIntegrationAssociationRequest, opts)



Creates an Amazon Web Services resource association with an Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createIntegrationAssociationRequest = new AmazonConnectService.CreateIntegrationAssociationRequest(); // CreateIntegrationAssociationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createIntegrationAssociation(instanceId, createIntegrationAssociationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createIntegrationAssociationRequest** | [**CreateIntegrationAssociationRequest**](CreateIntegrationAssociationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateIntegrationAssociationResponse**](CreateIntegrationAssociationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createParticipant

> CreateParticipantResponse createParticipant(createParticipantRequest, opts)



Adds a new participant into an on-going chat contact. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/chat-customize-flow.html\&quot;&gt;Customize chat flow experiences by integrating custom participants&lt;/a&gt;.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let createParticipantRequest = new AmazonConnectService.CreateParticipantRequest(); // CreateParticipantRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createParticipant(createParticipantRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createParticipantRequest** | [**CreateParticipantRequest**](CreateParticipantRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateParticipantResponse**](CreateParticipantResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPrompt

> CreatePromptResponse createPrompt(instanceId, createPromptRequest, opts)



Creates a prompt. For more information about prompts, such as supported file types and maximum length, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/prompts.html\&quot;&gt;Create prompts&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator&#39;s Guide&lt;/i&gt;.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createPromptRequest = new AmazonConnectService.CreatePromptRequest(); // CreatePromptRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPrompt(instanceId, createPromptRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createPromptRequest** | [**CreatePromptRequest**](CreatePromptRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePromptResponse**](CreatePromptResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createQueue

> CreateQueueResponse createQueue(instanceId, createQueueRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Creates a new queue for the specified Amazon Connect instance.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the number being used in the input is claimed to a traffic distribution group, and you are calling this API using an instance in the Amazon Web Services Region where the traffic distribution group was created, you can use either a full phone number ARN or UUID value for the &lt;code&gt;OutboundCallerIdNumberId&lt;/code&gt; value of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_OutboundCallerConfig\&quot;&gt;OutboundCallerConfig&lt;/a&gt; request body parameter. However, if the number is claimed to a traffic distribution group and you are calling this API using an instance in the alternate Amazon Web Services Region associated with the traffic distribution group, you must provide a full phone number ARN. If a UUID is provided in this scenario, you will receive a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Only use the phone number ARN format that doesn&#39;t contain &lt;code&gt;instance&lt;/code&gt; in the path, for example, &lt;code&gt;arn:aws:connect:us-east-1:1234567890:phone-number/uuid&lt;/code&gt;. This is the same ARN format that is returned when you call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html\&quot;&gt;ListPhoneNumbersV2&lt;/a&gt; API.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createQueueRequest = new AmazonConnectService.CreateQueueRequest(); // CreateQueueRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createQueue(instanceId, createQueueRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createQueueRequest** | [**CreateQueueRequest**](CreateQueueRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateQueueResponse**](CreateQueueResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createQuickConnect

> CreateQuickConnectResponse createQuickConnect(instanceId, createQuickConnectRequest, opts)



Creates a quick connect for the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createQuickConnectRequest = new AmazonConnectService.CreateQuickConnectRequest(); // CreateQuickConnectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createQuickConnect(instanceId, createQuickConnectRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createQuickConnectRequest** | [**CreateQuickConnectRequest**](CreateQuickConnectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateQuickConnectResponse**](CreateQuickConnectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRoutingProfile

> CreateRoutingProfileResponse createRoutingProfile(instanceId, createRoutingProfileRequest, opts)



Creates a new routing profile.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createRoutingProfileRequest = new AmazonConnectService.CreateRoutingProfileRequest(); // CreateRoutingProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRoutingProfile(instanceId, createRoutingProfileRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createRoutingProfileRequest** | [**CreateRoutingProfileRequest**](CreateRoutingProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRoutingProfileResponse**](CreateRoutingProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRule

> CreateRuleResponse createRule(instanceId, createRuleRequest, opts)



&lt;p&gt;Creates a rule for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;Use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/connect-rules-language.html\&quot;&gt;Rules Function language&lt;/a&gt; to code conditions for the rule. &lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createRuleRequest = new AmazonConnectService.CreateRuleRequest(); // CreateRuleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRule(instanceId, createRuleRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createRuleRequest** | [**CreateRuleRequest**](CreateRuleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRuleResponse**](CreateRuleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSecurityProfile

> CreateSecurityProfileResponse createSecurityProfile(instanceId, createSecurityProfileRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Creates a security profile.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createSecurityProfileRequest = new AmazonConnectService.CreateSecurityProfileRequest(); // CreateSecurityProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSecurityProfile(instanceId, createSecurityProfileRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createSecurityProfileRequest** | [**CreateSecurityProfileRequest**](CreateSecurityProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSecurityProfileResponse**](CreateSecurityProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTaskTemplate

> CreateTaskTemplateResponse createTaskTemplate(instanceId, createTaskTemplateRequest, opts)



Creates a new task template in the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createTaskTemplateRequest = new AmazonConnectService.CreateTaskTemplateRequest(); // CreateTaskTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createTaskTemplate(instanceId, createTaskTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createTaskTemplateRequest** | [**CreateTaskTemplateRequest**](CreateTaskTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateTaskTemplateResponse**](CreateTaskTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTrafficDistributionGroup

> CreateTrafficDistributionGroupResponse createTrafficDistributionGroup(createTrafficDistributionGroupRequest, opts)



&lt;p&gt;Creates a traffic distribution group given an Amazon Connect instance that has been replicated. &lt;/p&gt; &lt;p&gt;For more information about creating traffic distribution groups, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/setup-traffic-distribution-groups.html\&quot;&gt;Set up traffic distribution groups&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let createTrafficDistributionGroupRequest = new AmazonConnectService.CreateTrafficDistributionGroupRequest(); // CreateTrafficDistributionGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createTrafficDistributionGroup(createTrafficDistributionGroupRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createTrafficDistributionGroupRequest** | [**CreateTrafficDistributionGroupRequest**](CreateTrafficDistributionGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateTrafficDistributionGroupResponse**](CreateTrafficDistributionGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createUseCase

> CreateUseCaseResponse createUseCase(instanceId, integrationAssociationId, createUseCaseRequest, opts)



Creates a use case for an integration association.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let integrationAssociationId = "integrationAssociationId_example"; // String | The identifier for the integration association.
let createUseCaseRequest = new AmazonConnectService.CreateUseCaseRequest(); // CreateUseCaseRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createUseCase(instanceId, integrationAssociationId, createUseCaseRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **integrationAssociationId** | **String**| The identifier for the integration association. | 
 **createUseCaseRequest** | [**CreateUseCaseRequest**](CreateUseCaseRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateUseCaseResponse**](CreateUseCaseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createUser

> CreateUserResponse createUser(instanceId, createUserRequest, opts)



&lt;p&gt;Creates a user account for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For information about how to create user accounts using the Amazon Connect console, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/user-management.html\&quot;&gt;Add Users&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createUserRequest = new AmazonConnectService.CreateUserRequest(); // CreateUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createUser(instanceId, createUserRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createUserRequest** | [**CreateUserRequest**](CreateUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createUserHierarchyGroup

> CreateUserHierarchyGroupResponse createUserHierarchyGroup(instanceId, createUserHierarchyGroupRequest, opts)



Creates a new user hierarchy group.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createUserHierarchyGroupRequest = new AmazonConnectService.CreateUserHierarchyGroupRequest(); // CreateUserHierarchyGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createUserHierarchyGroup(instanceId, createUserHierarchyGroupRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createUserHierarchyGroupRequest** | [**CreateUserHierarchyGroupRequest**](CreateUserHierarchyGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateUserHierarchyGroupResponse**](CreateUserHierarchyGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVocabulary

> CreateVocabularyResponse createVocabulary(instanceId, createVocabularyRequest, opts)



Creates a custom vocabulary associated with your Amazon Connect instance. You can set a custom vocabulary to be your default vocabulary for a given language. Contact Lens for Amazon Connect uses the default vocabulary in post-call and real-time contact analysis sessions for that language.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let createVocabularyRequest = new AmazonConnectService.CreateVocabularyRequest(); // CreateVocabularyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createVocabulary(instanceId, createVocabularyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **createVocabularyRequest** | [**CreateVocabularyRequest**](CreateVocabularyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateVocabularyResponse**](CreateVocabularyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deactivateEvaluationForm

> DeactivateEvaluationFormResponse deactivateEvaluationForm(instanceId, evaluationFormId, deactivateEvaluationFormRequest, opts)



Deactivates an evaluation form in the specified Amazon Connect instance. After a form is deactivated, it is no longer available for users to start new evaluations based on the form. 

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let evaluationFormId = "evaluationFormId_example"; // String | The unique identifier for the evaluation form.
let deactivateEvaluationFormRequest = new AmazonConnectService.DeactivateEvaluationFormRequest(); // DeactivateEvaluationFormRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deactivateEvaluationForm(instanceId, evaluationFormId, deactivateEvaluationFormRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **evaluationFormId** | **String**| The unique identifier for the evaluation form. | 
 **deactivateEvaluationFormRequest** | [**DeactivateEvaluationFormRequest**](DeactivateEvaluationFormRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeactivateEvaluationFormResponse**](DeactivateEvaluationFormResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteContactEvaluation

> deleteContactEvaluation(instanceId, evaluationId, opts)



Deletes a contact evaluation in the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let evaluationId = "evaluationId_example"; // String | A unique identifier for the contact evaluation.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteContactEvaluation(instanceId, evaluationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **evaluationId** | **String**| A unique identifier for the contact evaluation. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteContactFlow

> Object deleteContactFlow(instanceId, contactFlowId, opts)



Deletes a flow for the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let contactFlowId = "contactFlowId_example"; // String | The identifier of the flow.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteContactFlow(instanceId, contactFlowId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **contactFlowId** | **String**| The identifier of the flow. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteContactFlowModule

> Object deleteContactFlowModule(instanceId, contactFlowModuleId, opts)



Deletes the specified flow module.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let contactFlowModuleId = "contactFlowModuleId_example"; // String | The identifier of the flow module.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteContactFlowModule(instanceId, contactFlowModuleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **contactFlowModuleId** | **String**| The identifier of the flow module. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEvaluationForm

> deleteEvaluationForm(instanceId, evaluationFormId, opts)



&lt;p&gt;Deletes an evaluation form in the specified Amazon Connect instance. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the version property is provided, only the specified version of the evaluation form is deleted.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If no version is provided, then the full form (all versions) is deleted.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let evaluationFormId = "evaluationFormId_example"; // String | The unique identifier for the evaluation form.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': 56 // Number | The unique identifier for the evaluation form.
};
apiInstance.deleteEvaluationForm(instanceId, evaluationFormId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **evaluationFormId** | **String**| The unique identifier for the evaluation form. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **Number**| The unique identifier for the evaluation form. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteHoursOfOperation

> deleteHoursOfOperation(instanceId, hoursOfOperationId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Deletes an hours of operation.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let hoursOfOperationId = "hoursOfOperationId_example"; // String | The identifier for the hours of operation.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteHoursOfOperation(instanceId, hoursOfOperationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **hoursOfOperationId** | **String**| The identifier for the hours of operation. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteInstance

> deleteInstance(instanceId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Deletes the Amazon Connect instance.&lt;/p&gt; &lt;p&gt;Amazon Connect enforces a limit on the total number of instances that you can create or delete in 30 days. If you exceed this limit, you will get an error message indicating there has been an excessive number of attempts at creating or deleting instances. You must wait 30 days before you can restart creating and deleting instances in your account.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteInstance(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteIntegrationAssociation

> deleteIntegrationAssociation(instanceId, integrationAssociationId, opts)



Deletes an Amazon Web Services resource association from an Amazon Connect instance. The association must not have any use cases associated with it.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let integrationAssociationId = "integrationAssociationId_example"; // String | The identifier for the integration association.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteIntegrationAssociation(instanceId, integrationAssociationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **integrationAssociationId** | **String**| The identifier for the integration association. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePrompt

> deletePrompt(instanceId, promptId, opts)



Deletes a prompt.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let promptId = "promptId_example"; // String | A unique identifier for the prompt.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deletePrompt(instanceId, promptId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **promptId** | **String**| A unique identifier for the prompt. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteQueue

> deleteQueue(instanceId, queueId, opts)



Deletes a queue.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let queueId = "queueId_example"; // String | The identifier for the queue.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteQueue(instanceId, queueId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **queueId** | **String**| The identifier for the queue. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteQuickConnect

> deleteQuickConnect(instanceId, quickConnectId, opts)



Deletes a quick connect.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let quickConnectId = "quickConnectId_example"; // String | The identifier for the quick connect.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteQuickConnect(instanceId, quickConnectId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **quickConnectId** | **String**| The identifier for the quick connect. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRoutingProfile

> deleteRoutingProfile(instanceId, routingProfileId, opts)



Deletes a routing profile.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let routingProfileId = "routingProfileId_example"; // String | The identifier of the routing profile.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRoutingProfile(instanceId, routingProfileId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **routingProfileId** | **String**| The identifier of the routing profile. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRule

> deleteRule(instanceId, ruleId, opts)



Deletes a rule for the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let ruleId = "ruleId_example"; // String | A unique identifier for the rule.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRule(instanceId, ruleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **ruleId** | **String**| A unique identifier for the rule. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSecurityProfile

> deleteSecurityProfile(instanceId, securityProfileId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Deletes a security profile.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let securityProfileId = "securityProfileId_example"; // String | The identifier for the security profle.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSecurityProfile(instanceId, securityProfileId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **securityProfileId** | **String**| The identifier for the security profle. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTaskTemplate

> Object deleteTaskTemplate(instanceId, taskTemplateId, opts)



Deletes the task template.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let taskTemplateId = "taskTemplateId_example"; // String | A unique identifier for the task template.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteTaskTemplate(instanceId, taskTemplateId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **taskTemplateId** | **String**| A unique identifier for the task template. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTrafficDistributionGroup

> Object deleteTrafficDistributionGroup(trafficDistributionGroupId, opts)



&lt;p&gt;Deletes a traffic distribution group. This API can be called only in the Region where the traffic distribution group is created.&lt;/p&gt; &lt;p&gt;For more information about deleting traffic distribution groups, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/delete-traffic-distribution-groups.html\&quot;&gt;Delete traffic distribution groups&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let trafficDistributionGroupId = "trafficDistributionGroupId_example"; // String | The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteTrafficDistributionGroup(trafficDistributionGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trafficDistributionGroupId** | **String**| The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteUseCase

> deleteUseCase(instanceId, integrationAssociationId, useCaseId, opts)



Deletes a use case from an integration association.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let integrationAssociationId = "integrationAssociationId_example"; // String | The identifier for the integration association.
let useCaseId = "useCaseId_example"; // String | The identifier for the use case.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteUseCase(instanceId, integrationAssociationId, useCaseId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **integrationAssociationId** | **String**| The identifier for the integration association. | 
 **useCaseId** | **String**| The identifier for the use case. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteUser

> deleteUser(instanceId, userId, opts)



&lt;p&gt;Deletes a user account from the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For information about what happens to a user&#39;s data when their account is deleted, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/delete-users.html\&quot;&gt;Delete Users from Your Amazon Connect Instance&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let userId = "userId_example"; // String | The identifier of the user.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteUser(instanceId, userId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **userId** | **String**| The identifier of the user. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteUserHierarchyGroup

> deleteUserHierarchyGroup(hierarchyGroupId, instanceId, opts)



Deletes an existing user hierarchy group. It must not be associated with any agents or have any active child groups.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let hierarchyGroupId = "hierarchyGroupId_example"; // String | The identifier of the hierarchy group.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteUserHierarchyGroup(hierarchyGroupId, instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hierarchyGroupId** | **String**| The identifier of the hierarchy group. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVocabulary

> DeleteVocabularyResponse deleteVocabulary(instanceId, vocabularyId, opts)



Deletes the vocabulary that has the given identifier.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let vocabularyId = "vocabularyId_example"; // String | The identifier of the custom vocabulary.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVocabulary(instanceId, vocabularyId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **vocabularyId** | **String**| The identifier of the custom vocabulary. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteVocabularyResponse**](DeleteVocabularyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeAgentStatus

> DescribeAgentStatusResponse describeAgentStatus(instanceId, agentStatusId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Describes an agent status.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let agentStatusId = "agentStatusId_example"; // String | The identifier for the agent status.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAgentStatus(instanceId, agentStatusId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **agentStatusId** | **String**| The identifier for the agent status. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAgentStatusResponse**](DescribeAgentStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeContact

> DescribeContactResponse describeContact(instanceId, contactId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Describes the specified contact. &lt;/p&gt; &lt;important&gt; &lt;p&gt;Contact information remains available in Amazon Connect for 24 months, and then it is deleted.&lt;/p&gt; &lt;p&gt;Only data from November 12, 2021, and later is returned by this API.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let contactId = "contactId_example"; // String | The identifier of the contact.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeContact(instanceId, contactId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **contactId** | **String**| The identifier of the contact. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeContactResponse**](DescribeContactResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeContactEvaluation

> DescribeContactEvaluationResponse describeContactEvaluation(instanceId, evaluationId, opts)



Describes a contact evaluation in the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let evaluationId = "evaluationId_example"; // String | A unique identifier for the contact evaluation.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeContactEvaluation(instanceId, evaluationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **evaluationId** | **String**| A unique identifier for the contact evaluation. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeContactEvaluationResponse**](DescribeContactEvaluationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeContactFlow

> DescribeContactFlowResponse describeContactFlow(instanceId, contactFlowId, opts)



&lt;p&gt;Describes the specified flow.&lt;/p&gt; &lt;p&gt;You can also create and update flows using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/flow-language.html\&quot;&gt;Amazon Connect Flow language&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance.
let contactFlowId = "contactFlowId_example"; // String | The identifier of the flow.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeContactFlow(instanceId, contactFlowId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. | 
 **contactFlowId** | **String**| The identifier of the flow. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeContactFlowResponse**](DescribeContactFlowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeContactFlowModule

> DescribeContactFlowModuleResponse describeContactFlowModule(instanceId, contactFlowModuleId, opts)



Describes the specified flow module.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let contactFlowModuleId = "contactFlowModuleId_example"; // String | The identifier of the flow module.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeContactFlowModule(instanceId, contactFlowModuleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **contactFlowModuleId** | **String**| The identifier of the flow module. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeContactFlowModuleResponse**](DescribeContactFlowModuleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeEvaluationForm

> DescribeEvaluationFormResponse describeEvaluationForm(instanceId, evaluationFormId, opts)



Describes an evaluation form in the specified Amazon Connect instance. If the version property is not provided, the latest version of the evaluation form is described.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let evaluationFormId = "evaluationFormId_example"; // String | A unique identifier for the contact evaluation.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': 56 // Number | A version of the evaluation form.
};
apiInstance.describeEvaluationForm(instanceId, evaluationFormId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **evaluationFormId** | **String**| A unique identifier for the contact evaluation. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **Number**| A version of the evaluation form. | [optional] 

### Return type

[**DescribeEvaluationFormResponse**](DescribeEvaluationFormResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeHoursOfOperation

> DescribeHoursOfOperationResponse describeHoursOfOperation(instanceId, hoursOfOperationId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Describes the hours of operation.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let hoursOfOperationId = "hoursOfOperationId_example"; // String | The identifier for the hours of operation.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeHoursOfOperation(instanceId, hoursOfOperationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **hoursOfOperationId** | **String**| The identifier for the hours of operation. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeHoursOfOperationResponse**](DescribeHoursOfOperationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeInstance

> DescribeInstanceResponse describeInstance(instanceId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Returns the current state of the specified instance identifier. It tracks the instance while it is being created and returns an error status, if applicable. &lt;/p&gt; &lt;p&gt;If an instance is not created successfully, the instance status reason field returns details relevant to the reason. The instance in a failed state is returned only for 24 hours after the CreateInstance API was invoked.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeInstance(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeInstanceResponse**](DescribeInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeInstanceAttribute

> DescribeInstanceAttributeResponse describeInstanceAttribute(instanceId, attributeType, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Describes the specified instance attribute.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let attributeType = "attributeType_example"; // String | The type of attribute.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeInstanceAttribute(instanceId, attributeType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **attributeType** | **String**| The type of attribute. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeInstanceAttributeResponse**](DescribeInstanceAttributeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeInstanceStorageConfig

> DescribeInstanceStorageConfigResponse describeInstanceStorageConfig(instanceId, associationId, resourceType, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Retrieves the current storage configurations for the specified resource type, association ID, and instance ID.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let associationId = "associationId_example"; // String | The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
let resourceType = "resourceType_example"; // String | A valid resource type.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeInstanceStorageConfig(instanceId, associationId, resourceType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **associationId** | **String**| The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID. | 
 **resourceType** | **String**| A valid resource type. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeInstanceStorageConfigResponse**](DescribeInstanceStorageConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describePhoneNumber

> DescribePhoneNumberResponse describePhoneNumber(phoneNumberId, opts)



&lt;p&gt;Gets details and status of a phone number that’s claimed to your Amazon Connect instance or traffic distribution group.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the number is claimed to a traffic distribution group, and you are calling in the Amazon Web Services Region where the traffic distribution group was created, you can use either a phone number ARN or UUID value for the &lt;code&gt;PhoneNumberId&lt;/code&gt; URI request parameter. However, if the number is claimed to a traffic distribution group and you are calling this API in the alternate Amazon Web Services Region associated with the traffic distribution group, you must provide a full phone number ARN. If a UUID is provided in this scenario, you will receive a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let phoneNumberId = "phoneNumberId_example"; // String | A unique identifier for the phone number.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describePhoneNumber(phoneNumberId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phoneNumberId** | **String**| A unique identifier for the phone number. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribePhoneNumberResponse**](DescribePhoneNumberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describePrompt

> DescribePromptResponse describePrompt(instanceId, promptId, opts)



Describes the prompt.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let promptId = "promptId_example"; // String | A unique identifier for the prompt.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describePrompt(instanceId, promptId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **promptId** | **String**| A unique identifier for the prompt. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribePromptResponse**](DescribePromptResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeQueue

> DescribeQueueResponse describeQueue(instanceId, queueId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Describes the specified queue.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let queueId = "queueId_example"; // String | The identifier for the queue.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeQueue(instanceId, queueId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **queueId** | **String**| The identifier for the queue. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeQueueResponse**](DescribeQueueResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeQuickConnect

> DescribeQuickConnectResponse describeQuickConnect(instanceId, quickConnectId, opts)



Describes the quick connect.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let quickConnectId = "quickConnectId_example"; // String | The identifier for the quick connect.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeQuickConnect(instanceId, quickConnectId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **quickConnectId** | **String**| The identifier for the quick connect. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeQuickConnectResponse**](DescribeQuickConnectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeRoutingProfile

> DescribeRoutingProfileResponse describeRoutingProfile(instanceId, routingProfileId, opts)



Describes the specified routing profile.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let routingProfileId = "routingProfileId_example"; // String | The identifier of the routing profile.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeRoutingProfile(instanceId, routingProfileId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **routingProfileId** | **String**| The identifier of the routing profile. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeRoutingProfileResponse**](DescribeRoutingProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeRule

> DescribeRuleResponse describeRule(instanceId, ruleId, opts)



Describes a rule for the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let ruleId = "ruleId_example"; // String | A unique identifier for the rule.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeRule(instanceId, ruleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **ruleId** | **String**| A unique identifier for the rule. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeRuleResponse**](DescribeRuleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeSecurityProfile

> DescribeSecurityProfileResponse describeSecurityProfile(securityProfileId, instanceId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Gets basic information about the security profle.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let securityProfileId = "securityProfileId_example"; // String | The identifier for the security profle.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeSecurityProfile(securityProfileId, instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **securityProfileId** | **String**| The identifier for the security profle. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeSecurityProfileResponse**](DescribeSecurityProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeTrafficDistributionGroup

> DescribeTrafficDistributionGroupResponse describeTrafficDistributionGroup(trafficDistributionGroupId, opts)



Gets details and status of a traffic distribution group.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let trafficDistributionGroupId = "trafficDistributionGroupId_example"; // String | The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeTrafficDistributionGroup(trafficDistributionGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trafficDistributionGroupId** | **String**| The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeTrafficDistributionGroupResponse**](DescribeTrafficDistributionGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeUser

> DescribeUserResponse describeUser(userId, instanceId, opts)



Describes the specified user account. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID in the Amazon Connect console&lt;/a&gt; (it’s the final part of the ARN). The console does not display the user IDs. Instead, list the users and note the IDs provided in the output.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let userId = "userId_example"; // String | The identifier of the user account.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeUser(userId, instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**| The identifier of the user account. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeUserResponse**](DescribeUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeUserHierarchyGroup

> DescribeUserHierarchyGroupResponse describeUserHierarchyGroup(hierarchyGroupId, instanceId, opts)



Describes the specified hierarchy group.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let hierarchyGroupId = "hierarchyGroupId_example"; // String | The identifier of the hierarchy group.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeUserHierarchyGroup(hierarchyGroupId, instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hierarchyGroupId** | **String**| The identifier of the hierarchy group. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeUserHierarchyGroupResponse**](DescribeUserHierarchyGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeUserHierarchyStructure

> DescribeUserHierarchyStructureResponse describeUserHierarchyStructure(instanceId, opts)



Describes the hierarchy structure of the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeUserHierarchyStructure(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeUserHierarchyStructureResponse**](DescribeUserHierarchyStructureResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeVocabulary

> DescribeVocabularyResponse describeVocabulary(instanceId, vocabularyId, opts)



Describes the specified vocabulary.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let vocabularyId = "vocabularyId_example"; // String | The identifier of the custom vocabulary.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeVocabulary(instanceId, vocabularyId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **vocabularyId** | **String**| The identifier of the custom vocabulary. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeVocabularyResponse**](DescribeVocabularyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateApprovedOrigin

> disassociateApprovedOrigin(instanceId, origin, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Revokes access to integrated applications from Amazon Connect.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let origin = "origin_example"; // String | The domain URL of the integrated application.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateApprovedOrigin(instanceId, origin, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **origin** | **String**| The domain URL of the integrated application. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateBot

> disassociateBot(instanceId, associateBotRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Revokes authorization from the specified instance to access the specified Amazon Lex or Amazon Lex V2 bot. &lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let associateBotRequest = new AmazonConnectService.AssociateBotRequest(); // AssociateBotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateBot(instanceId, associateBotRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **associateBotRequest** | [**AssociateBotRequest**](AssociateBotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateInstanceStorageConfig

> disassociateInstanceStorageConfig(instanceId, associationId, resourceType, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Removes the storage type configurations for the specified resource type and association ID.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let associationId = "associationId_example"; // String | The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
let resourceType = "resourceType_example"; // String | A valid resource type.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateInstanceStorageConfig(instanceId, associationId, resourceType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **associationId** | **String**| The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID. | 
 **resourceType** | **String**| A valid resource type. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateLambdaFunction

> disassociateLambdaFunction(instanceId, functionArn, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Remove the Lambda function from the dropdown options available in the relevant flow blocks.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance..
let functionArn = "functionArn_example"; // String | The Amazon Resource Name (ARN) of the Lambda function being disassociated.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateLambdaFunction(instanceId, functionArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance.. | 
 **functionArn** | **String**| The Amazon Resource Name (ARN) of the Lambda function being disassociated. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateLexBot

> disassociateLexBot(instanceId, botName, lexRegion, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Revokes authorization from the specified instance to access the specified Amazon Lex bot.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let botName = "botName_example"; // String | The name of the Amazon Lex bot. Maximum character limit of 50.
let lexRegion = "lexRegion_example"; // String | The Amazon Web Services Region in which the Amazon Lex bot has been created.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateLexBot(instanceId, botName, lexRegion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **botName** | **String**| The name of the Amazon Lex bot. Maximum character limit of 50. | 
 **lexRegion** | **String**| The Amazon Web Services Region in which the Amazon Lex bot has been created. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociatePhoneNumberContactFlow

> disassociatePhoneNumberContactFlow(phoneNumberId, instanceId, opts)



&lt;p&gt;Removes the flow association from a phone number claimed to your Amazon Connect instance.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the number is claimed to a traffic distribution group, and you are calling this API using an instance in the Amazon Web Services Region where the traffic distribution group was created, you can use either a full phone number ARN or UUID value for the &lt;code&gt;PhoneNumberId&lt;/code&gt; URI request parameter. However, if the number is claimed to a traffic distribution group and you are calling this API using an instance in the alternate Amazon Web Services Region associated with the traffic distribution group, you must provide a full phone number ARN. If a UUID is provided in this scenario, you will receive a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let phoneNumberId = "phoneNumberId_example"; // String | A unique identifier for the phone number.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociatePhoneNumberContactFlow(phoneNumberId, instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phoneNumberId** | **String**| A unique identifier for the phone number. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateQueueQuickConnects

> disassociateQueueQuickConnects(instanceId, queueId, disassociateQueueQuickConnectsRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Disassociates a set of quick connects from a queue.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let queueId = "queueId_example"; // String | The identifier for the queue.
let disassociateQueueQuickConnectsRequest = new AmazonConnectService.DisassociateQueueQuickConnectsRequest(); // DisassociateQueueQuickConnectsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateQueueQuickConnects(instanceId, queueId, disassociateQueueQuickConnectsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **queueId** | **String**| The identifier for the queue. | 
 **disassociateQueueQuickConnectsRequest** | [**DisassociateQueueQuickConnectsRequest**](DisassociateQueueQuickConnectsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateRoutingProfileQueues

> disassociateRoutingProfileQueues(instanceId, routingProfileId, disassociateRoutingProfileQueuesRequest, opts)



Disassociates a set of queues from a routing profile.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let routingProfileId = "routingProfileId_example"; // String | The identifier of the routing profile.
let disassociateRoutingProfileQueuesRequest = new AmazonConnectService.DisassociateRoutingProfileQueuesRequest(); // DisassociateRoutingProfileQueuesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateRoutingProfileQueues(instanceId, routingProfileId, disassociateRoutingProfileQueuesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **routingProfileId** | **String**| The identifier of the routing profile. | 
 **disassociateRoutingProfileQueuesRequest** | [**DisassociateRoutingProfileQueuesRequest**](DisassociateRoutingProfileQueuesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateSecurityKey

> disassociateSecurityKey(instanceId, associationId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Deletes the specified security key.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let associationId = "associationId_example"; // String | The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateSecurityKey(instanceId, associationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **associationId** | **String**| The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dismissUserContact

> Object dismissUserContact(userId, instanceId, dismissUserContactRequest, opts)



Dismisses contacts from an agent’s CCP and returns the agent to an available state, which allows the agent to receive a new routed contact. Contacts can only be dismissed if they are in a &lt;code&gt;MISSED&lt;/code&gt;, &lt;code&gt;ERROR&lt;/code&gt;, &lt;code&gt;ENDED&lt;/code&gt;, or &lt;code&gt;REJECTED&lt;/code&gt; state in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/about-contact-states.html\&quot;&gt;Agent Event Stream&lt;/a&gt;.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let userId = "userId_example"; // String | The identifier of the user account.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can find the instanceId in the ARN of the instance.
let dismissUserContactRequest = new AmazonConnectService.DismissUserContactRequest(); // DismissUserContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.dismissUserContact(userId, instanceId, dismissUserContactRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**| The identifier of the user account. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can find the instanceId in the ARN of the instance. | 
 **dismissUserContactRequest** | [**DismissUserContactRequest**](DismissUserContactRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getContactAttributes

> GetContactAttributesResponse getContactAttributes(instanceId, initialContactId, opts)



Retrieves the contact attributes for the specified contact.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance.
let initialContactId = "initialContactId_example"; // String | The identifier of the initial contact.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getContactAttributes(instanceId, initialContactId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. | 
 **initialContactId** | **String**| The identifier of the initial contact. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetContactAttributesResponse**](GetContactAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCurrentMetricData

> GetCurrentMetricDataResponse getCurrentMetricData(instanceId, getCurrentMetricDataRequest, opts)



&lt;p&gt;Gets the real-time metric data from the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For a description of each metric, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/real-time-metrics-definitions.html\&quot;&gt;Real-time Metrics Definitions&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let getCurrentMetricDataRequest = new AmazonConnectService.GetCurrentMetricDataRequest(); // GetCurrentMetricDataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.getCurrentMetricData(instanceId, getCurrentMetricDataRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **getCurrentMetricDataRequest** | [**GetCurrentMetricDataRequest**](GetCurrentMetricDataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**GetCurrentMetricDataResponse**](GetCurrentMetricDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCurrentUserData

> GetCurrentUserDataResponse getCurrentUserData(instanceId, getCurrentUserDataRequest, opts)



Gets the real-time active user data from the specified Amazon Connect instance. 

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let getCurrentUserDataRequest = new AmazonConnectService.GetCurrentUserDataRequest(); // GetCurrentUserDataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.getCurrentUserData(instanceId, getCurrentUserDataRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **getCurrentUserDataRequest** | [**GetCurrentUserDataRequest**](GetCurrentUserDataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**GetCurrentUserDataResponse**](GetCurrentUserDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getFederationToken

> GetFederationTokenResponse getFederationToken(instanceId, opts)



&lt;p&gt;Retrieves a token for federation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API doesn&#39;t support root users. If you try to invoke GetFederationToken with root credentials, an error message similar to the following one appears: &lt;/p&gt; &lt;p&gt; &lt;code&gt;Provided identity: Principal: .... User: .... cannot be used for federation with Amazon Connect&lt;/code&gt; &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getFederationToken(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetFederationTokenResponse**](GetFederationTokenResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMetricData

> GetMetricDataResponse getMetricData(instanceId, getMetricDataRequest, opts)



&lt;p&gt;Gets historical metric data from the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For a description of each historical metric, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/historical-metrics-definitions.html\&quot;&gt;Historical Metrics Definitions&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let getMetricDataRequest = new AmazonConnectService.GetMetricDataRequest(); // GetMetricDataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.getMetricData(instanceId, getMetricDataRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **getMetricDataRequest** | [**GetMetricDataRequest**](GetMetricDataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**GetMetricDataResponse**](GetMetricDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getMetricDataV2

> GetMetricDataV2Response getMetricDataV2(getMetricDataV2Request, opts)



&lt;p&gt;Gets metric data from the specified Amazon Connect instance. &lt;/p&gt; &lt;p&gt; &lt;code&gt;GetMetricDataV2&lt;/code&gt; offers more features than &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricData.html\&quot;&gt;GetMetricData&lt;/a&gt;, the previous version of this API. It has new metrics, offers filtering at a metric level, and offers the ability to filter and group data by channels, queues, routing profiles, agents, and agent hierarchy levels. It can retrieve historical data for the last 35 days, in 24-hour intervals.&lt;/p&gt; &lt;p&gt;For a description of the historical metrics that are supported by &lt;code&gt;GetMetricDataV2&lt;/code&gt; and &lt;code&gt;GetMetricData&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/historical-metrics-definitions.html\&quot;&gt;Historical metrics definitions&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator&#39;s Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let getMetricDataV2Request = new AmazonConnectService.GetMetricDataV2Request(); // GetMetricDataV2Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.getMetricDataV2(getMetricDataV2Request, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **getMetricDataV2Request** | [**GetMetricDataV2Request**](GetMetricDataV2Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**GetMetricDataV2Response**](GetMetricDataV2Response.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getPromptFile

> GetPromptFileResponse getPromptFile(instanceId, promptId, opts)



Gets the prompt file.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let promptId = "promptId_example"; // String | A unique identifier for the prompt.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPromptFile(instanceId, promptId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **promptId** | **String**| A unique identifier for the prompt. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPromptFileResponse**](GetPromptFileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTaskTemplate

> GetTaskTemplateResponse getTaskTemplate(instanceId, taskTemplateId, opts)



Gets details about a specific task template in the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let taskTemplateId = "taskTemplateId_example"; // String | A unique identifier for the task template.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'snapshotVersion': "snapshotVersion_example" // String | The system generated version of a task template that is associated with a task, when the task is created.
};
apiInstance.getTaskTemplate(instanceId, taskTemplateId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **taskTemplateId** | **String**| A unique identifier for the task template. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **snapshotVersion** | **String**| The system generated version of a task template that is associated with a task, when the task is created. | [optional] 

### Return type

[**GetTaskTemplateResponse**](GetTaskTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrafficDistribution

> GetTrafficDistributionResponse getTrafficDistribution(id, opts)



Retrieves the current traffic distribution for a given traffic distribution group.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let id = "id_example"; // String | The identifier of the traffic distribution group.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getTrafficDistribution(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The identifier of the traffic distribution group. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetTrafficDistributionResponse**](GetTrafficDistributionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAgentStatuses

> ListAgentStatusResponse listAgentStatuses(instanceId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Lists agent statuses.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'agentStatusTypes': [new AmazonConnectService.AgentStatusType()], // [AgentStatusType] | Available agent status types.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listAgentStatuses(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **agentStatusTypes** | [**[AgentStatusType]**](AgentStatusType.md)| Available agent status types. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListAgentStatusResponse**](ListAgentStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listApprovedOrigins

> ListApprovedOriginsResponse listApprovedOrigins(instanceId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Returns a paginated list of all approved origins associated with the instance.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listApprovedOrigins(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListApprovedOriginsResponse**](ListApprovedOriginsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBots

> ListBotsResponse listBots(instanceId, lexVersion, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;For the specified version of Amazon Lex, returns a paginated list of all the Amazon Lex bots currently associated with the instance. Use this API to returns both Amazon Lex V1 and V2 bots.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let lexVersion = "lexVersion_example"; // String | The version of Amazon Lex or Amazon Lex V2.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listBots(instanceId, lexVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **lexVersion** | **String**| The version of Amazon Lex or Amazon Lex V2. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListBotsResponse**](ListBotsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listContactEvaluations

> ListContactEvaluationsResponse listContactEvaluations(instanceId, contactId, opts)



Lists contact evaluations in the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let contactId = "contactId_example"; // String | The identifier of the contact in this instance of Amazon Connect. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p> <important> <p>This is not expected to be set because the value returned in the previous response is always null.</p> </important>
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listContactEvaluations(instanceId, contactId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **contactId** | **String**| The identifier of the contact in this instance of Amazon Connect.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| &lt;p&gt;The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This is not expected to be set because the value returned in the previous response is always null.&lt;/p&gt; &lt;/important&gt; | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListContactEvaluationsResponse**](ListContactEvaluationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listContactFlowModules

> ListContactFlowModulesResponse listContactFlowModules(instanceId, opts)



Provides information about the flow modules for the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'state': "state_example", // String | The state of the flow module.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listContactFlowModules(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **state** | **String**| The state of the flow module. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListContactFlowModulesResponse**](ListContactFlowModulesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listContactFlows

> ListContactFlowsResponse listContactFlows(instanceId, opts)



&lt;p&gt;Provides information about the flows for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;You can also create and update flows using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/flow-language.html\&quot;&gt;Amazon Connect Flow language&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information about flows, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/concepts-contact-flows.html\&quot;&gt;Flows&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'contactFlowTypes': [new AmazonConnectService.ContactFlowType()], // [ContactFlowType] | The type of flow.
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page. The default MaxResult size is 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listContactFlows(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **contactFlowTypes** | [**[ContactFlowType]**](ContactFlowType.md)| The type of flow. | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. The default MaxResult size is 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListContactFlowsResponse**](ListContactFlowsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listContactReferences

> ListContactReferencesResponse listContactReferences(instanceId, contactId, referenceTypes, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;For the specified &lt;code&gt;referenceTypes&lt;/code&gt;, returns a list of references associated with the contact. &lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let contactId = "contactId_example"; // String | The identifier of the initial contact.
let referenceTypes = [new AmazonConnectService.ReferenceType()]; // [ReferenceType] | The type of reference.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p> <important> <p>This is not expected to be set, because the value returned in the previous response is always null.</p> </important>
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listContactReferences(instanceId, contactId, referenceTypes, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **contactId** | **String**| The identifier of the initial contact. | 
 **referenceTypes** | [**[ReferenceType]**](ReferenceType.md)| The type of reference. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| &lt;p&gt;The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This is not expected to be set, because the value returned in the previous response is always null.&lt;/p&gt; &lt;/important&gt; | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListContactReferencesResponse**](ListContactReferencesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDefaultVocabularies

> ListDefaultVocabulariesResponse listDefaultVocabularies(instanceId, listDefaultVocabulariesRequest, opts)



Lists the default vocabularies for the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let listDefaultVocabulariesRequest = new AmazonConnectService.ListDefaultVocabulariesRequest(); // ListDefaultVocabulariesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listDefaultVocabularies(instanceId, listDefaultVocabulariesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **listDefaultVocabulariesRequest** | [**ListDefaultVocabulariesRequest**](ListDefaultVocabulariesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListDefaultVocabulariesResponse**](ListDefaultVocabulariesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listEvaluationFormVersions

> ListEvaluationFormVersionsResponse listEvaluationFormVersions(instanceId, evaluationFormId, opts)



Lists versions of an evaluation form in the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let evaluationFormId = "evaluationFormId_example"; // String | The unique identifier for the evaluation form.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listEvaluationFormVersions(instanceId, evaluationFormId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **evaluationFormId** | **String**| The unique identifier for the evaluation form. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListEvaluationFormVersionsResponse**](ListEvaluationFormVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEvaluationForms

> ListEvaluationFormsResponse listEvaluationForms(instanceId, opts)



Lists evaluation forms in the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listEvaluationForms(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListEvaluationFormsResponse**](ListEvaluationFormsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listHoursOfOperations

> ListHoursOfOperationsResponse listHoursOfOperations(instanceId, opts)



&lt;p&gt;Provides information about the hours of operation for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For more information about hours of operation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/set-hours-operation.html\&quot;&gt;Set the Hours of Operation for a Queue&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page. The default MaxResult size is 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listHoursOfOperations(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. The default MaxResult size is 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListHoursOfOperationsResponse**](ListHoursOfOperationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInstanceAttributes

> ListInstanceAttributesResponse listInstanceAttributes(instanceId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Returns a paginated list of all attribute types for the given instance.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listInstanceAttributes(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListInstanceAttributesResponse**](ListInstanceAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInstanceStorageConfigs

> ListInstanceStorageConfigsResponse listInstanceStorageConfigs(instanceId, resourceType, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Returns a paginated list of storage configs for the identified instance and resource type.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let resourceType = "resourceType_example"; // String | A valid resource type.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listInstanceStorageConfigs(instanceId, resourceType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **resourceType** | **String**| A valid resource type. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListInstanceStorageConfigsResponse**](ListInstanceStorageConfigsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInstances

> ListInstancesResponse listInstances(opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Return a list of instances which are in active state, creation-in-progress state, and failed state. Instances that aren&#39;t successfully created (they are in a failed state) are returned only for 24 hours after the CreateInstance API was invoked.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listInstances(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListInstancesResponse**](ListInstancesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listIntegrationAssociations

> ListIntegrationAssociationsResponse listIntegrationAssociations(instanceId, opts)



Provides summary information about the Amazon Web Services resource associations for the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'integrationType': "integrationType_example", // String | The integration type.
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listIntegrationAssociations(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **integrationType** | **String**| The integration type. | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListIntegrationAssociationsResponse**](ListIntegrationAssociationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLambdaFunctions

> ListLambdaFunctionsResponse listLambdaFunctions(instanceId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Returns a paginated list of all Lambda functions that display in the dropdown options in the relevant flow blocks.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listLambdaFunctions(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListLambdaFunctionsResponse**](ListLambdaFunctionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLexBots

> ListLexBotsResponse listLexBots(instanceId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Returns a paginated list of all the Amazon Lex V1 bots currently associated with the instance. To return both Amazon Lex V1 and V2 bots, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_ListBots.html\&quot;&gt;ListBots&lt;/a&gt; API. &lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page. If no value is specified, the default is 10. 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listLexBots(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. If no value is specified, the default is 10.  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListLexBotsResponse**](ListLexBotsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPhoneNumbers

> ListPhoneNumbersResponse listPhoneNumbers(instanceId, opts)



&lt;p&gt;Provides information about the phone numbers for the specified Amazon Connect instance. &lt;/p&gt; &lt;p&gt;For more information about phone numbers, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/contact-center-phone-number.html\&quot;&gt;Set Up Phone Numbers for Your Contact Center&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The phone number &lt;code&gt;Arn&lt;/code&gt; value that is returned from each of the items in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbers.html#connect-ListPhoneNumbers-response-PhoneNumberSummaryList\&quot;&gt;PhoneNumberSummaryList&lt;/a&gt; cannot be used to tag phone number resources. It will fail with a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;. Instead, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html\&quot;&gt;ListPhoneNumbersV2&lt;/a&gt; API. It returns the new phone number ARN that can be used to tag phone number resources.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'phoneNumberTypes': [new AmazonConnectService.PhoneNumberType()], // [PhoneNumberType] | The type of phone number.
  'phoneNumberCountryCodes': [new AmazonConnectService.PhoneNumberCountryCode()], // [PhoneNumberCountryCode] | The ISO country code.
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page. The default MaxResult size is 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listPhoneNumbers(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **phoneNumberTypes** | [**[PhoneNumberType]**](PhoneNumberType.md)| The type of phone number. | [optional] 
 **phoneNumberCountryCodes** | [**[PhoneNumberCountryCode]**](PhoneNumberCountryCode.md)| The ISO country code. | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. The default MaxResult size is 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListPhoneNumbersResponse**](ListPhoneNumbersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPhoneNumbersV2

> ListPhoneNumbersV2Response listPhoneNumbersV2(listPhoneNumbersV2Request, opts)



&lt;p&gt;Lists phone numbers claimed to your Amazon Connect instance or traffic distribution group. If the provided &lt;code&gt;TargetArn&lt;/code&gt; is a traffic distribution group, you can call this API in both Amazon Web Services Regions associated with traffic distribution group.&lt;/p&gt; &lt;p&gt;For more information about phone numbers, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/contact-center-phone-number.html\&quot;&gt;Set Up Phone Numbers for Your Contact Center&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let listPhoneNumbersV2Request = new AmazonConnectService.ListPhoneNumbersV2Request(); // ListPhoneNumbersV2Request | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listPhoneNumbersV2(listPhoneNumbersV2Request, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listPhoneNumbersV2Request** | [**ListPhoneNumbersV2Request**](ListPhoneNumbersV2Request.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListPhoneNumbersV2Response**](ListPhoneNumbersV2Response.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPrompts

> ListPromptsResponse listPrompts(instanceId, opts)



Provides information about the prompts for the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page. The default MaxResult size is 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listPrompts(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. The default MaxResult size is 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListPromptsResponse**](ListPromptsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listQueueQuickConnects

> ListQueueQuickConnectsResponse listQueueQuickConnects(instanceId, queueId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Lists the quick connects associated with a queue.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let queueId = "queueId_example"; // String | The identifier for the queue.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page. The default MaxResult size is 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listQueueQuickConnects(instanceId, queueId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **queueId** | **String**| The identifier for the queue. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. The default MaxResult size is 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListQueueQuickConnectsResponse**](ListQueueQuickConnectsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listQueues

> ListQueuesResponse listQueues(instanceId, opts)



&lt;p&gt;Provides information about the queues for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;If you do not specify a &lt;code&gt;QueueTypes&lt;/code&gt; parameter, both standard and agent queues are returned. This might cause an unexpected truncation of results if you have more than 1000 agents and you limit the number of results of the API call in code.&lt;/p&gt; &lt;p&gt;For more information about queues, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/concepts-queues-standard-and-agent.html\&quot;&gt;Queues: Standard and Agent&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'queueTypes': [new AmazonConnectService.QueueType()], // [QueueType] | The type of queue.
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page. The default MaxResult size is 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listQueues(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **queueTypes** | [**[QueueType]**](QueueType.md)| The type of queue. | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. The default MaxResult size is 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListQueuesResponse**](ListQueuesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listQuickConnects

> ListQuickConnectsResponse listQuickConnects(instanceId, opts)



Provides information about the quick connects for the specified Amazon Connect instance. 

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page. The default MaxResult size is 100.
  'quickConnectTypes': [new AmazonConnectService.QuickConnectType()], // [QuickConnectType] | The type of quick connect. In the Amazon Connect console, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE).
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listQuickConnects(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. The default MaxResult size is 100. | [optional] 
 **quickConnectTypes** | [**[QuickConnectType]**](QuickConnectType.md)| The type of quick connect. In the Amazon Connect console, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE). | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListQuickConnectsResponse**](ListQuickConnectsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRoutingProfileQueues

> ListRoutingProfileQueuesResponse listRoutingProfileQueues(instanceId, routingProfileId, opts)



Lists the queues associated with a routing profile.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let routingProfileId = "routingProfileId_example"; // String | The identifier of the routing profile.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page. The default MaxResult size is 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listRoutingProfileQueues(instanceId, routingProfileId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **routingProfileId** | **String**| The identifier of the routing profile. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. The default MaxResult size is 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListRoutingProfileQueuesResponse**](ListRoutingProfileQueuesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRoutingProfiles

> ListRoutingProfilesResponse listRoutingProfiles(instanceId, opts)



&lt;p&gt;Provides summary information about the routing profiles for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For more information about routing profiles, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing.html\&quot;&gt;Routing Profiles&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/routing-profiles.html\&quot;&gt;Create a Routing Profile&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page. The default MaxResult size is 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listRoutingProfiles(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. The default MaxResult size is 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListRoutingProfilesResponse**](ListRoutingProfilesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRules

> ListRulesResponse listRules(instanceId, opts)



List all rules for the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'publishStatus': "publishStatus_example", // String | The publish status of the rule.
  'eventSourceName': "eventSourceName_example", // String | The name of the event source.
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listRules(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **publishStatus** | **String**| The publish status of the rule. | [optional] 
 **eventSourceName** | **String**| The name of the event source. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListRulesResponse**](ListRulesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSecurityKeys

> ListSecurityKeysResponse listSecurityKeys(instanceId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Returns a paginated list of all security keys associated with the instance.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listSecurityKeys(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListSecurityKeysResponse**](ListSecurityKeysResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSecurityProfilePermissions

> ListSecurityProfilePermissionsResponse listSecurityProfilePermissions(securityProfileId, instanceId, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Lists the permissions granted to a security profile.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let securityProfileId = "securityProfileId_example"; // String | The identifier for the security profle.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listSecurityProfilePermissions(securityProfileId, instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **securityProfileId** | **String**| The identifier for the security profle. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListSecurityProfilePermissionsResponse**](ListSecurityProfilePermissionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSecurityProfiles

> ListSecurityProfilesResponse listSecurityProfiles(instanceId, opts)



&lt;p&gt;Provides summary information about the security profiles for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For more information about security profiles, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html\&quot;&gt;Security Profiles&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page. The default MaxResult size is 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listSecurityProfiles(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. The default MaxResult size is 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListSecurityProfilesResponse**](ListSecurityProfilesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



&lt;p&gt;Lists the tags for the specified resource.&lt;/p&gt; &lt;p&gt;For sample policies that use tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/security_iam_id-based-policy-examples.html\&quot;&gt;Amazon Connect Identity-Based Policy Examples&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource. All Amazon Connect resources (instances, queues, flows, routing profiles, etc) have an ARN. To locate the ARN for an instance, for example, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">Find your Amazon Connect instance ID/ARN</a>. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. All Amazon Connect resources (instances, queues, flows, routing profiles, etc) have an ARN. To locate the ARN for an instance, for example, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;Find your Amazon Connect instance ID/ARN&lt;/a&gt;.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTaskTemplates

> ListTaskTemplatesResponse listTaskTemplates(instanceId, opts)



Lists task templates for the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p> <important> <p>It is not expected that you set this because the value returned in the previous response is always null.</p> </important>
  'maxResults': 56, // Number | <p>The maximum number of results to return per page.</p> <important> <p>It is not expected that you set this.</p> </important>
  'status': "status_example", // String | Marks a template as <code>ACTIVE</code> or <code>INACTIVE</code> for a task to refer to it. Tasks can only be created from <code>ACTIVE</code> templates. If a template is marked as <code>INACTIVE</code>, then a task that refers to this template cannot be created.
  'name': "name_example", // String | The name of the task template.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listTaskTemplates(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| &lt;p&gt;The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.&lt;/p&gt; &lt;important&gt; &lt;p&gt;It is not expected that you set this because the value returned in the previous response is always null.&lt;/p&gt; &lt;/important&gt; | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of results to return per page.&lt;/p&gt; &lt;important&gt; &lt;p&gt;It is not expected that you set this.&lt;/p&gt; &lt;/important&gt; | [optional] 
 **status** | **String**| Marks a template as &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;INACTIVE&lt;/code&gt; for a task to refer to it. Tasks can only be created from &lt;code&gt;ACTIVE&lt;/code&gt; templates. If a template is marked as &lt;code&gt;INACTIVE&lt;/code&gt;, then a task that refers to this template cannot be created. | [optional] 
 **name** | **String**| The name of the task template. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListTaskTemplatesResponse**](ListTaskTemplatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTrafficDistributionGroups

> ListTrafficDistributionGroupsResponse listTrafficDistributionGroups(opts)



Lists traffic distribution groups.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'instanceId': "instanceId_example", // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listTrafficDistributionGroups(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListTrafficDistributionGroupsResponse**](ListTrafficDistributionGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUseCases

> ListUseCasesResponse listUseCases(instanceId, integrationAssociationId, opts)



Lists the use cases for the integration association. 

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let integrationAssociationId = "integrationAssociationId_example"; // String | The identifier for the integration association.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listUseCases(instanceId, integrationAssociationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **integrationAssociationId** | **String**| The identifier for the integration association. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListUseCasesResponse**](ListUseCasesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUserHierarchyGroups

> ListUserHierarchyGroupsResponse listUserHierarchyGroups(instanceId, opts)



&lt;p&gt;Provides summary information about the hierarchy groups for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;For more information about agent hierarchies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/agent-hierarchy.html\&quot;&gt;Set Up Agent Hierarchies&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page. The default MaxResult size is 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listUserHierarchyGroups(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. The default MaxResult size is 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListUserHierarchyGroupsResponse**](ListUserHierarchyGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUsers

> ListUsersResponse listUsers(instanceId, opts)



Provides summary information about the users for the specified Amazon Connect instance.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56, // Number | The maximum number of results to return per page. The default MaxResult size is 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listUsers(instanceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. The default MaxResult size is 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## monitorContact

> MonitorContactResponse monitorContact(monitorContactRequest, opts)



Initiates silent monitoring of a contact. The Contact Control Panel (CCP) of the user specified by &lt;i&gt;userId&lt;/i&gt; will be set to silent monitoring mode on the contact.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let monitorContactRequest = new AmazonConnectService.MonitorContactRequest(); // MonitorContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.monitorContact(monitorContactRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitorContactRequest** | [**MonitorContactRequest**](MonitorContactRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**MonitorContactResponse**](MonitorContactResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putUserStatus

> Object putUserStatus(userId, instanceId, putUserStatusRequest, opts)



&lt;p&gt;Changes the current status of a user or agent in Amazon Connect. If the agent is currently handling a contact, this sets the agent&#39;s next status.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/metrics-agent-status.html\&quot;&gt;Agent status&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/set-next-status.html\&quot;&gt;Set your next status&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let userId = "userId_example"; // String | The identifier of the user.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let putUserStatusRequest = new AmazonConnectService.PutUserStatusRequest(); // PutUserStatusRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putUserStatus(userId, instanceId, putUserStatusRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**| The identifier of the user. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **putUserStatusRequest** | [**PutUserStatusRequest**](PutUserStatusRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## releasePhoneNumber

> releasePhoneNumber(phoneNumberId, opts)



&lt;p&gt;Releases a phone number previously claimed to an Amazon Connect instance or traffic distribution group. You can call this API only in the Amazon Web Services Region where the number was claimed.&lt;/p&gt; &lt;important&gt; &lt;p&gt;To release phone numbers from a traffic distribution group, use the &lt;code&gt;ReleasePhoneNumber&lt;/code&gt; API, not the Amazon Connect console.&lt;/p&gt; &lt;p&gt;After releasing a phone number, the phone number enters into a cooldown period of 30 days. It cannot be searched for or claimed again until the period has ended. If you accidentally release a phone number, contact Amazon Web Services Support.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If you plan to claim and release numbers frequently during a 30 day period, contact us for a service quota exception. Otherwise, it is possible you will be blocked from claiming and releasing any more numbers until 30 days past the oldest number released has expired.&lt;/p&gt; &lt;p&gt;By default you can claim and release up to 200% of your maximum number of active phone numbers during any 30 day period. If you claim and release phone numbers using the UI or API during a rolling 30 day cycle that exceeds 200% of your phone number service level quota, you will be blocked from claiming any more numbers until 30 days past the oldest number released has expired. &lt;/p&gt; &lt;p&gt;For example, if you already have 99 claimed numbers and a service level quota of 99 phone numbers, and in any 30 day period you release 99, claim 99, and then release 99, you will have exceeded the 200% limit. At that point you are blocked from claiming any more numbers until you open an Amazon Web Services support ticket.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let phoneNumberId = "phoneNumberId_example"; // String | A unique identifier for the phone number.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.
};
apiInstance.releasePhoneNumber(phoneNumberId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phoneNumberId** | **String**| A unique identifier for the phone number. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicateInstance

> ReplicateInstanceResponse replicateInstance(instanceId, replicateInstanceRequest, opts)



&lt;p&gt;Replicates an Amazon Connect instance in the specified Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;For more information about replicating an Amazon Connect instance, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/create-replica-connect-instance.html\&quot;&gt;Create a replica of your existing Amazon Connect instance&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance. You can provide the <code>InstanceId</code>, or the entire ARN.
let replicateInstanceRequest = new AmazonConnectService.ReplicateInstanceRequest(); // ReplicateInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.replicateInstance(instanceId, replicateInstanceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. You can provide the &lt;code&gt;InstanceId&lt;/code&gt;, or the entire ARN. | 
 **replicateInstanceRequest** | [**ReplicateInstanceRequest**](ReplicateInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ReplicateInstanceResponse**](ReplicateInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resumeContactRecording

> Object resumeContactRecording(resumeContactRecordingRequest, opts)



&lt;p&gt;When a contact is being recorded, and the recording has been suspended using SuspendContactRecording, this API resumes recording the call or screen.&lt;/p&gt; &lt;p&gt;Voice and screen recordings are supported.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let resumeContactRecordingRequest = new AmazonConnectService.ResumeContactRecordingRequest(); // ResumeContactRecordingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.resumeContactRecording(resumeContactRecordingRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resumeContactRecordingRequest** | [**ResumeContactRecordingRequest**](ResumeContactRecordingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchAvailablePhoneNumbers

> SearchAvailablePhoneNumbersResponse searchAvailablePhoneNumbers(searchAvailablePhoneNumbersRequest, opts)



Searches for available phone numbers that you can claim to your Amazon Connect instance or traffic distribution group. If the provided &lt;code&gt;TargetArn&lt;/code&gt; is a traffic distribution group, you can call this API in both Amazon Web Services Regions associated with the traffic distribution group.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let searchAvailablePhoneNumbersRequest = new AmazonConnectService.SearchAvailablePhoneNumbersRequest(); // SearchAvailablePhoneNumbersRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchAvailablePhoneNumbers(searchAvailablePhoneNumbersRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchAvailablePhoneNumbersRequest** | [**SearchAvailablePhoneNumbersRequest**](SearchAvailablePhoneNumbersRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchAvailablePhoneNumbersResponse**](SearchAvailablePhoneNumbersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchHoursOfOperations

> SearchHoursOfOperationsResponse searchHoursOfOperations(searchHoursOfOperationsRequest, opts)



Searches the hours of operation in an Amazon Connect instance, with optional filtering.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let searchHoursOfOperationsRequest = new AmazonConnectService.SearchHoursOfOperationsRequest(); // SearchHoursOfOperationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchHoursOfOperations(searchHoursOfOperationsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchHoursOfOperationsRequest** | [**SearchHoursOfOperationsRequest**](SearchHoursOfOperationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchHoursOfOperationsResponse**](SearchHoursOfOperationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchPrompts

> SearchPromptsResponse searchPrompts(searchPromptsRequest, opts)



Searches prompts in an Amazon Connect instance, with optional filtering.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let searchPromptsRequest = new AmazonConnectService.SearchPromptsRequest(); // SearchPromptsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchPrompts(searchPromptsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchPromptsRequest** | [**SearchPromptsRequest**](SearchPromptsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchPromptsResponse**](SearchPromptsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchQueues

> SearchQueuesResponse searchQueues(searchQueuesRequest, opts)



Searches queues in an Amazon Connect instance, with optional filtering.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let searchQueuesRequest = new AmazonConnectService.SearchQueuesRequest(); // SearchQueuesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchQueues(searchQueuesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchQueuesRequest** | [**SearchQueuesRequest**](SearchQueuesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchQueuesResponse**](SearchQueuesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchQuickConnects

> SearchQuickConnectsResponse searchQuickConnects(searchQuickConnectsRequest, opts)



Searches quick connects in an Amazon Connect instance, with optional filtering.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let searchQuickConnectsRequest = new AmazonConnectService.SearchQuickConnectsRequest(); // SearchQuickConnectsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchQuickConnects(searchQuickConnectsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchQuickConnectsRequest** | [**SearchQuickConnectsRequest**](SearchQuickConnectsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchQuickConnectsResponse**](SearchQuickConnectsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchResourceTags

> SearchResourceTagsResponse searchResourceTags(searchResourceTagsRequest, opts)



Searches tags used in an Amazon Connect instance using optional search criteria.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let searchResourceTagsRequest = new AmazonConnectService.SearchResourceTagsRequest(); // SearchResourceTagsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchResourceTags(searchResourceTagsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchResourceTagsRequest** | [**SearchResourceTagsRequest**](SearchResourceTagsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchResourceTagsResponse**](SearchResourceTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchRoutingProfiles

> SearchRoutingProfilesResponse searchRoutingProfiles(searchRoutingProfilesRequest, opts)



Searches routing profiles in an Amazon Connect instance, with optional filtering.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let searchRoutingProfilesRequest = new AmazonConnectService.SearchRoutingProfilesRequest(); // SearchRoutingProfilesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchRoutingProfiles(searchRoutingProfilesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchRoutingProfilesRequest** | [**SearchRoutingProfilesRequest**](SearchRoutingProfilesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchRoutingProfilesResponse**](SearchRoutingProfilesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchSecurityProfiles

> SearchSecurityProfilesResponse searchSecurityProfiles(searchSecurityProfilesRequest, opts)



Searches security profiles in an Amazon Connect instance, with optional filtering.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let searchSecurityProfilesRequest = new AmazonConnectService.SearchSecurityProfilesRequest(); // SearchSecurityProfilesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchSecurityProfiles(searchSecurityProfilesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchSecurityProfilesRequest** | [**SearchSecurityProfilesRequest**](SearchSecurityProfilesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchSecurityProfilesResponse**](SearchSecurityProfilesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchUsers

> SearchUsersResponse searchUsers(searchUsersRequest, opts)



&lt;p&gt;Searches users in an Amazon Connect instance, with optional filtering.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;AfterContactWorkTimeLimit&lt;/code&gt; is returned in milliseconds. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let searchUsersRequest = new AmazonConnectService.SearchUsersRequest(); // SearchUsersRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchUsers(searchUsersRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchUsersRequest** | [**SearchUsersRequest**](SearchUsersRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchUsersResponse**](SearchUsersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchVocabularies

> SearchVocabulariesResponse searchVocabularies(instanceId, searchVocabulariesRequest, opts)



Searches for vocabularies within a specific Amazon Connect instance using &lt;code&gt;State&lt;/code&gt;, &lt;code&gt;NameStartsWith&lt;/code&gt;, and &lt;code&gt;LanguageCode&lt;/code&gt;.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let searchVocabulariesRequest = new AmazonConnectService.SearchVocabulariesRequest(); // SearchVocabulariesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.searchVocabularies(instanceId, searchVocabulariesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **searchVocabulariesRequest** | [**SearchVocabulariesRequest**](SearchVocabulariesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**SearchVocabulariesResponse**](SearchVocabulariesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startChatContact

> StartChatContactResponse startChatContact(startChatContactRequest, opts)



&lt;p&gt;Initiates a flow to start a new chat for the customer. Response of this API provides a token required to obtain credentials from the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html\&quot;&gt;CreateParticipantConnection&lt;/a&gt; API in the Amazon Connect Participant Service.&lt;/p&gt; &lt;p&gt;When a new chat contact is successfully created, clients must subscribe to the participant’s connection for the created chat within 5 minutes. This is achieved by invoking &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html\&quot;&gt;CreateParticipantConnection&lt;/a&gt; with WEBSOCKET and CONNECTION_CREDENTIALS. &lt;/p&gt; &lt;p&gt;A 429 error occurs in the following situations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;API rate limit is exceeded. API TPS throttling returns a &lt;code&gt;TooManyRequests&lt;/code&gt; exception.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html\&quot;&gt;quota for concurrent active chats&lt;/a&gt; is exceeded. Active chat throttling returns a &lt;code&gt;LimitExceededException&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you use the &lt;code&gt;ChatDurationInMinutes&lt;/code&gt; parameter and receive a 400 error, your account may not support the ability to configure custom chat durations. For more information, contact Amazon Web Services Support. &lt;/p&gt; &lt;p&gt;For more information about chat, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/chat.html\&quot;&gt;Chat&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let startChatContactRequest = new AmazonConnectService.StartChatContactRequest(); // StartChatContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startChatContact(startChatContactRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startChatContactRequest** | [**StartChatContactRequest**](StartChatContactRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartChatContactResponse**](StartChatContactResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startContactEvaluation

> StartContactEvaluationResponse startContactEvaluation(instanceId, startContactEvaluationRequest, opts)



&lt;p&gt;Starts an empty evaluation in the specified Amazon Connect instance, using the given evaluation form for the particular contact. The evaluation form version used for the contact evaluation corresponds to the currently activated version. If no version is activated for the evaluation form, the contact evaluation cannot be started. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Evaluations created through the public API do not contain answer values suggested from automation.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let startContactEvaluationRequest = new AmazonConnectService.StartContactEvaluationRequest(); // StartContactEvaluationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startContactEvaluation(instanceId, startContactEvaluationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **startContactEvaluationRequest** | [**StartContactEvaluationRequest**](StartContactEvaluationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartContactEvaluationResponse**](StartContactEvaluationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startContactRecording

> Object startContactRecording(startContactRecordingRequest, opts)



&lt;p&gt;Starts recording the contact: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the API is called &lt;i&gt;before&lt;/i&gt; the agent joins the call, recording starts when the agent joins the call.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the API is called &lt;i&gt;after&lt;/i&gt; the agent joins the call, recording starts at the time of the API call.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;StartContactRecording is a one-time action. For example, if you use StopContactRecording to stop recording an ongoing call, you can&#39;t use StartContactRecording to restart it. For scenarios where the recording has started and you want to suspend and resume it, such as when collecting sensitive information (for example, a credit card number), use SuspendContactRecording and ResumeContactRecording.&lt;/p&gt; &lt;p&gt;You can use this API to override the recording behavior configured in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/set-recording-behavior.html\&quot;&gt;Set recording behavior&lt;/a&gt; block.&lt;/p&gt; &lt;p&gt;Only voice recordings are supported at this time.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let startContactRecordingRequest = new AmazonConnectService.StartContactRecordingRequest(); // StartContactRecordingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startContactRecording(startContactRecordingRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startContactRecordingRequest** | [**StartContactRecordingRequest**](StartContactRecordingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startContactStreaming

> StartContactStreamingResponse startContactStreaming(startContactStreamingRequest, opts)



&lt;p&gt; Initiates real-time message streaming for a new chat contact.&lt;/p&gt; &lt;p&gt; For more information about message streaming, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/chat-message-streaming.html\&quot;&gt;Enable real-time chat message streaming&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let startContactStreamingRequest = new AmazonConnectService.StartContactStreamingRequest(); // StartContactStreamingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startContactStreaming(startContactStreamingRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startContactStreamingRequest** | [**StartContactStreamingRequest**](StartContactStreamingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartContactStreamingResponse**](StartContactStreamingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startOutboundVoiceContact

> StartOutboundVoiceContactResponse startOutboundVoiceContact(startOutboundVoiceContactRequest, opts)



&lt;p&gt;Places an outbound call to a contact, and then initiates the flow. It performs the actions in the flow that&#39;s specified (in &lt;code&gt;ContactFlowId&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;Agents do not initiate the outbound API, which means that they do not dial the contact. If the flow places an outbound call to a contact, and then puts the contact in queue, the call is then routed to the agent, like any other inbound case.&lt;/p&gt; &lt;p&gt;There is a 60-second dialing timeout for this operation. If the call is not connected after 60 seconds, it fails.&lt;/p&gt; &lt;note&gt; &lt;p&gt;UK numbers with a 447 prefix are not allowed by default. Before you can dial these UK mobile numbers, you must submit a service quota increase request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html\&quot;&gt;Amazon Connect Service Quotas&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;Campaign calls are not allowed by default. Before you can make a call with &lt;code&gt;TrafficType&lt;/code&gt; &#x3D; &lt;code&gt;CAMPAIGN&lt;/code&gt;, you must submit a service quota increase request to the quota &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#outbound-communications-quotas\&quot;&gt;Amazon Connect campaigns&lt;/a&gt;. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let startOutboundVoiceContactRequest = new AmazonConnectService.StartOutboundVoiceContactRequest(); // StartOutboundVoiceContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startOutboundVoiceContact(startOutboundVoiceContactRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startOutboundVoiceContactRequest** | [**StartOutboundVoiceContactRequest**](StartOutboundVoiceContactRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartOutboundVoiceContactResponse**](StartOutboundVoiceContactResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startTaskContact

> StartTaskContactResponse startTaskContact(startTaskContactRequest, opts)



Initiates a flow to start a new task.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let startTaskContactRequest = new AmazonConnectService.StartTaskContactRequest(); // StartTaskContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startTaskContact(startTaskContactRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startTaskContactRequest** | [**StartTaskContactRequest**](StartTaskContactRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartTaskContactResponse**](StartTaskContactResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopContact

> Object stopContact(stopContactRequest, opts)



&lt;p&gt;Ends the specified contact. This call does not work for the following initiation methods:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;DISCONNECT&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;TRANSFER&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;QUEUE_TRANSFER&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let stopContactRequest = new AmazonConnectService.StopContactRequest(); // StopContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopContact(stopContactRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stopContactRequest** | [**StopContactRequest**](StopContactRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopContactRecording

> Object stopContactRecording(resumeContactRecordingRequest, opts)



&lt;p&gt;Stops recording a call when a contact is being recorded. StopContactRecording is a one-time action. If you use StopContactRecording to stop recording an ongoing call, you can&#39;t use StartContactRecording to restart it. For scenarios where the recording has started and you want to suspend it for sensitive information (for example, to collect a credit card number), and then restart it, use SuspendContactRecording and ResumeContactRecording.&lt;/p&gt; &lt;p&gt;Only voice recordings are supported at this time.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let resumeContactRecordingRequest = new AmazonConnectService.ResumeContactRecordingRequest(); // ResumeContactRecordingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopContactRecording(resumeContactRecordingRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resumeContactRecordingRequest** | [**ResumeContactRecordingRequest**](ResumeContactRecordingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopContactStreaming

> Object stopContactStreaming(stopContactStreamingRequest, opts)



 Ends message streaming on a specified contact. To restart message streaming on that contact, call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_StartContactStreaming.html\&quot;&gt;StartContactStreaming&lt;/a&gt; API. 

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let stopContactStreamingRequest = new AmazonConnectService.StopContactStreamingRequest(); // StopContactStreamingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopContactStreaming(stopContactStreamingRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stopContactStreamingRequest** | [**StopContactStreamingRequest**](StopContactStreamingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## submitContactEvaluation

> SubmitContactEvaluationResponse submitContactEvaluation(instanceId, evaluationId, updateContactEvaluationRequest, opts)



&lt;p&gt;Submits a contact evaluation in the specified Amazon Connect instance. Answers included in the request are merged with existing answers for the given evaluation. If no answers or notes are passed, the evaluation is submitted with the existing answers and notes. You can delete an answer or note by passing an empty object (&lt;code&gt;{}&lt;/code&gt;) to the question identifier. &lt;/p&gt; &lt;p&gt;If a contact evaluation is already in submitted state, this operation will trigger a resubmission.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let evaluationId = "evaluationId_example"; // String | A unique identifier for the contact evaluation.
let updateContactEvaluationRequest = new AmazonConnectService.UpdateContactEvaluationRequest(); // UpdateContactEvaluationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.submitContactEvaluation(instanceId, evaluationId, updateContactEvaluationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **evaluationId** | **String**| A unique identifier for the contact evaluation. | 
 **updateContactEvaluationRequest** | [**UpdateContactEvaluationRequest**](UpdateContactEvaluationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SubmitContactEvaluationResponse**](SubmitContactEvaluationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## suspendContactRecording

> Object suspendContactRecording(resumeContactRecordingRequest, opts)



&lt;p&gt;When a contact is being recorded, this API suspends recording the call or screen. For example, you might suspend the call or screen recording while collecting sensitive information, such as a credit card number. Then use ResumeContactRecording to restart recording.&lt;/p&gt; &lt;p&gt;The period of time that the recording is suspended is filled with silence in the final recording.&lt;/p&gt; &lt;p&gt;Voice and screen recordings are supported.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let resumeContactRecordingRequest = new AmazonConnectService.ResumeContactRecordingRequest(); // ResumeContactRecordingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.suspendContactRecording(resumeContactRecordingRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resumeContactRecordingRequest** | [**ResumeContactRecordingRequest**](ResumeContactRecordingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> tagResource(resourceArn, tagResourceRequest, opts)



&lt;p&gt;Adds the specified tags to the specified resource.&lt;/p&gt; &lt;p&gt;Some of the supported resource types are agents, routing profiles, queues, quick connects, contact flows, agent statuses, hours of operation, phone numbers, security profiles, and task templates. For a complete list, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/tagging.html\&quot;&gt;Tagging resources in Amazon Connect&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For sample policies that use tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/security_iam_id-based-policy-examples.html\&quot;&gt;Amazon Connect Identity-Based Policy Examples&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
let tagResourceRequest = new AmazonConnectService.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceArn, tagResourceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferContact

> TransferContactResponse transferContact(transferContactRequest, opts)



&lt;p&gt;Transfers contacts from one agent or queue to another agent or queue at any point after a contact is created. You can transfer a contact to another queue by providing the flow which orchestrates the contact to the destination queue. This gives you more control over contact handling and helps you adhere to the service level agreement (SLA) guaranteed to your customers.&lt;/p&gt; &lt;p&gt;Note the following requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Transfer is supported for only &lt;code&gt;TASK&lt;/code&gt; contacts.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Do not use both &lt;code&gt;QueueId&lt;/code&gt; and &lt;code&gt;UserId&lt;/code&gt; in the same call.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The following flow types are supported: Inbound flow, Transfer to agent flow, and Transfer to queue flow.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;TransferContact&lt;/code&gt; API can be called only on active contacts.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A contact cannot be transferred more than 11 times.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let transferContactRequest = new AmazonConnectService.TransferContactRequest(); // TransferContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.transferContact(transferContactRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferContactRequest** | [**TransferContactRequest**](TransferContactRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**TransferContactResponse**](TransferContactResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> untagResource(resourceArn, tagKeys, opts)



Removes the specified tags from the specified resource.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
let tagKeys = ["null"]; // [String] | The tag keys.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, tagKeys, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
 **tagKeys** | [**[String]**](String.md)| The tag keys. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAgentStatus

> updateAgentStatus(instanceId, agentStatusId, updateAgentStatusRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates agent status.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let agentStatusId = "agentStatusId_example"; // String | The identifier of the agent status.
let updateAgentStatusRequest = new AmazonConnectService.UpdateAgentStatusRequest(); // UpdateAgentStatusRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAgentStatus(instanceId, agentStatusId, updateAgentStatusRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **agentStatusId** | **String**| The identifier of the agent status. | 
 **updateAgentStatusRequest** | [**UpdateAgentStatusRequest**](UpdateAgentStatusRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateContact

> Object updateContact(instanceId, contactId, updateContactRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Adds or updates user-defined contact information associated with the specified contact. At least one field to be updated must be present in the request.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You can add or update user-defined contact information for both ongoing and completed contacts.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let contactId = "contactId_example"; // String | The identifier of the contact. This is the identifier of the contact associated with the first interaction with your contact center.
let updateContactRequest = new AmazonConnectService.UpdateContactRequest(); // UpdateContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateContact(instanceId, contactId, updateContactRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **contactId** | **String**| The identifier of the contact. This is the identifier of the contact associated with the first interaction with your contact center. | 
 **updateContactRequest** | [**UpdateContactRequest**](UpdateContactRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateContactAttributes

> Object updateContactAttributes(updateContactAttributesRequest, opts)



&lt;p&gt;Creates or updates user-defined contact attributes associated with the specified contact.&lt;/p&gt; &lt;p&gt;You can create or update user-defined attributes for both ongoing and completed contacts. For example, while the call is active, you can update the customer&#39;s name or the reason the customer called. You can add notes about steps that the agent took during the call that display to the next agent that takes the call. You can also update attributes for a contact using data from your CRM application and save the data with the contact in Amazon Connect. You could also flag calls for additional analysis, such as legal review or to identify abusive callers.&lt;/p&gt; &lt;p&gt;Contact attributes are available in Amazon Connect for 24 months, and are then deleted. For information about contact record retention and the maximum size of the contact record attributes section, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#feature-limits\&quot;&gt;Feature specifications&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let updateContactAttributesRequest = new AmazonConnectService.UpdateContactAttributesRequest(); // UpdateContactAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateContactAttributes(updateContactAttributesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateContactAttributesRequest** | [**UpdateContactAttributesRequest**](UpdateContactAttributesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateContactEvaluation

> UpdateContactEvaluationResponse updateContactEvaluation(instanceId, evaluationId, updateContactEvaluationRequest, opts)



Updates details about a contact evaluation in the specified Amazon Connect instance. A contact evaluation must be in draft state. Answers included in the request are merged with existing answers for the given evaluation. An answer or note can be deleted by passing an empty object (&lt;code&gt;{}&lt;/code&gt;) to the question identifier. 

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let evaluationId = "evaluationId_example"; // String | A unique identifier for the contact evaluation.
let updateContactEvaluationRequest = new AmazonConnectService.UpdateContactEvaluationRequest(); // UpdateContactEvaluationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateContactEvaluation(instanceId, evaluationId, updateContactEvaluationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **evaluationId** | **String**| A unique identifier for the contact evaluation. | 
 **updateContactEvaluationRequest** | [**UpdateContactEvaluationRequest**](UpdateContactEvaluationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateContactEvaluationResponse**](UpdateContactEvaluationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateContactFlowContent

> Object updateContactFlowContent(instanceId, contactFlowId, updateContactFlowContentRequest, opts)



&lt;p&gt;Updates the specified flow.&lt;/p&gt; &lt;p&gt;You can also create and update flows using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/flow-language.html\&quot;&gt;Amazon Connect Flow language&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance.
let contactFlowId = "contactFlowId_example"; // String | The identifier of the flow.
let updateContactFlowContentRequest = new AmazonConnectService.UpdateContactFlowContentRequest(); // UpdateContactFlowContentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateContactFlowContent(instanceId, contactFlowId, updateContactFlowContentRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. | 
 **contactFlowId** | **String**| The identifier of the flow. | 
 **updateContactFlowContentRequest** | [**UpdateContactFlowContentRequest**](UpdateContactFlowContentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateContactFlowMetadata

> Object updateContactFlowMetadata(instanceId, contactFlowId, updateContactFlowMetadataRequest, opts)



Updates metadata about specified flow.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let contactFlowId = "contactFlowId_example"; // String | The identifier of the flow.
let updateContactFlowMetadataRequest = new AmazonConnectService.UpdateContactFlowMetadataRequest(); // UpdateContactFlowMetadataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateContactFlowMetadata(instanceId, contactFlowId, updateContactFlowMetadataRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **contactFlowId** | **String**| The identifier of the flow. | 
 **updateContactFlowMetadataRequest** | [**UpdateContactFlowMetadataRequest**](UpdateContactFlowMetadataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateContactFlowModuleContent

> Object updateContactFlowModuleContent(instanceId, contactFlowModuleId, updateContactFlowModuleContentRequest, opts)



Updates specified flow module for the specified Amazon Connect instance. 

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let contactFlowModuleId = "contactFlowModuleId_example"; // String | The identifier of the flow module.
let updateContactFlowModuleContentRequest = new AmazonConnectService.UpdateContactFlowModuleContentRequest(); // UpdateContactFlowModuleContentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateContactFlowModuleContent(instanceId, contactFlowModuleId, updateContactFlowModuleContentRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **contactFlowModuleId** | **String**| The identifier of the flow module. | 
 **updateContactFlowModuleContentRequest** | [**UpdateContactFlowModuleContentRequest**](UpdateContactFlowModuleContentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateContactFlowModuleMetadata

> Object updateContactFlowModuleMetadata(instanceId, contactFlowModuleId, updateContactFlowModuleMetadataRequest, opts)



Updates metadata about specified flow module.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let contactFlowModuleId = "contactFlowModuleId_example"; // String | The identifier of the flow module.
let updateContactFlowModuleMetadataRequest = new AmazonConnectService.UpdateContactFlowModuleMetadataRequest(); // UpdateContactFlowModuleMetadataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateContactFlowModuleMetadata(instanceId, contactFlowModuleId, updateContactFlowModuleMetadataRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **contactFlowModuleId** | **String**| The identifier of the flow module. | 
 **updateContactFlowModuleMetadataRequest** | [**UpdateContactFlowModuleMetadataRequest**](UpdateContactFlowModuleMetadataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateContactFlowName

> Object updateContactFlowName(instanceId, contactFlowId, updateContactFlowNameRequest, opts)



&lt;p&gt;The name of the flow.&lt;/p&gt; &lt;p&gt;You can also create and update flows using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/flow-language.html\&quot;&gt;Amazon Connect Flow language&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance.
let contactFlowId = "contactFlowId_example"; // String | The identifier of the flow.
let updateContactFlowNameRequest = new AmazonConnectService.UpdateContactFlowNameRequest(); // UpdateContactFlowNameRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateContactFlowName(instanceId, contactFlowId, updateContactFlowNameRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. | 
 **contactFlowId** | **String**| The identifier of the flow. | 
 **updateContactFlowNameRequest** | [**UpdateContactFlowNameRequest**](UpdateContactFlowNameRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateContactSchedule

> Object updateContactSchedule(updateContactScheduleRequest, opts)



Updates the scheduled time of a task contact that is already scheduled.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let updateContactScheduleRequest = new AmazonConnectService.UpdateContactScheduleRequest(); // UpdateContactScheduleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateContactSchedule(updateContactScheduleRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateContactScheduleRequest** | [**UpdateContactScheduleRequest**](UpdateContactScheduleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEvaluationForm

> UpdateEvaluationFormResponse updateEvaluationForm(instanceId, evaluationFormId, updateEvaluationFormRequest, opts)



&lt;p&gt;Updates details about a specific evaluation form version in the specified Amazon Connect instance. Question and section identifiers cannot be duplicated within the same evaluation form.&lt;/p&gt; &lt;p&gt;This operation does not support partial updates. Instead it does a full update of evaluation form content.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let evaluationFormId = "evaluationFormId_example"; // String | The unique identifier for the evaluation form.
let updateEvaluationFormRequest = new AmazonConnectService.UpdateEvaluationFormRequest(); // UpdateEvaluationFormRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateEvaluationForm(instanceId, evaluationFormId, updateEvaluationFormRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **evaluationFormId** | **String**| The unique identifier for the evaluation form. | 
 **updateEvaluationFormRequest** | [**UpdateEvaluationFormRequest**](UpdateEvaluationFormRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateEvaluationFormResponse**](UpdateEvaluationFormResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateHoursOfOperation

> updateHoursOfOperation(instanceId, hoursOfOperationId, updateHoursOfOperationRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates the hours of operation.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let hoursOfOperationId = "hoursOfOperationId_example"; // String | The identifier of the hours of operation.
let updateHoursOfOperationRequest = new AmazonConnectService.UpdateHoursOfOperationRequest(); // UpdateHoursOfOperationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateHoursOfOperation(instanceId, hoursOfOperationId, updateHoursOfOperationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **hoursOfOperationId** | **String**| The identifier of the hours of operation. | 
 **updateHoursOfOperationRequest** | [**UpdateHoursOfOperationRequest**](UpdateHoursOfOperationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateInstanceAttribute

> updateInstanceAttribute(instanceId, attributeType, updateInstanceAttributeRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates the value for the specified attribute type.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let attributeType = "attributeType_example"; // String | <p>The type of attribute.</p> <note> <p>Only allowlisted customers can consume USE_CUSTOM_TTS_VOICES. To access this feature, contact Amazon Web Services Support for allowlisting.</p> </note>
let updateInstanceAttributeRequest = new AmazonConnectService.UpdateInstanceAttributeRequest(); // UpdateInstanceAttributeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateInstanceAttribute(instanceId, attributeType, updateInstanceAttributeRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **attributeType** | **String**| &lt;p&gt;The type of attribute.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only allowlisted customers can consume USE_CUSTOM_TTS_VOICES. To access this feature, contact Amazon Web Services Support for allowlisting.&lt;/p&gt; &lt;/note&gt; | 
 **updateInstanceAttributeRequest** | [**UpdateInstanceAttributeRequest**](UpdateInstanceAttributeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateInstanceStorageConfig

> updateInstanceStorageConfig(instanceId, associationId, resourceType, updateInstanceStorageConfigRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates an existing configuration for a resource type. This API is idempotent.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let associationId = "associationId_example"; // String | The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
let resourceType = "resourceType_example"; // String | A valid resource type.
let updateInstanceStorageConfigRequest = new AmazonConnectService.UpdateInstanceStorageConfigRequest(); // UpdateInstanceStorageConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateInstanceStorageConfig(instanceId, associationId, resourceType, updateInstanceStorageConfigRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **associationId** | **String**| The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID. | 
 **resourceType** | **String**| A valid resource type. | 
 **updateInstanceStorageConfigRequest** | [**UpdateInstanceStorageConfigRequest**](UpdateInstanceStorageConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateParticipantRoleConfig

> Object updateParticipantRoleConfig(instanceId, contactId, updateParticipantRoleConfigRequest, opts)



&lt;p&gt;Updates timeouts for when human chat participants are to be considered idle, and when agents are automatically disconnected from a chat due to idleness. You can set four timers:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Customer idle timeout&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Customer auto-disconnect timeout&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Agent idle timeout&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Agent auto-disconnect timeout&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about how chat timeouts work, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/setup-chat-timeouts.html\&quot;&gt;Set up chat timeouts for human participants&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let contactId = "contactId_example"; // String | The identifier of the contact in this instance of Amazon Connect. 
let updateParticipantRoleConfigRequest = new AmazonConnectService.UpdateParticipantRoleConfigRequest(); // UpdateParticipantRoleConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateParticipantRoleConfig(instanceId, contactId, updateParticipantRoleConfigRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **contactId** | **String**| The identifier of the contact in this instance of Amazon Connect.  | 
 **updateParticipantRoleConfigRequest** | [**UpdateParticipantRoleConfigRequest**](UpdateParticipantRoleConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePhoneNumber

> UpdatePhoneNumberResponse updatePhoneNumber(phoneNumberId, updatePhoneNumberRequest, opts)



&lt;p&gt;Updates your claimed phone number from its current Amazon Connect instance or traffic distribution group to another Amazon Connect instance or traffic distribution group in the same Amazon Web Services Region.&lt;/p&gt; &lt;important&gt; &lt;p&gt;After using this API, you must verify that the phone number is attached to the correct flow in the target instance or traffic distribution group. You need to do this because the API switches only the phone number to a new instance or traffic distribution group. It doesn&#39;t migrate the flow configuration of the phone number, too.&lt;/p&gt; &lt;p&gt;You can call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribePhoneNumber.html\&quot;&gt;DescribePhoneNumber&lt;/a&gt; API to verify the status of a previous &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html\&quot;&gt;UpdatePhoneNumber&lt;/a&gt; operation.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let phoneNumberId = "phoneNumberId_example"; // String | A unique identifier for the phone number.
let updatePhoneNumberRequest = new AmazonConnectService.UpdatePhoneNumberRequest(); // UpdatePhoneNumberRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePhoneNumber(phoneNumberId, updatePhoneNumberRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phoneNumberId** | **String**| A unique identifier for the phone number. | 
 **updatePhoneNumberRequest** | [**UpdatePhoneNumberRequest**](UpdatePhoneNumberRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdatePhoneNumberResponse**](UpdatePhoneNumberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePrompt

> UpdatePromptResponse updatePrompt(instanceId, promptId, updatePromptRequest, opts)



Updates a prompt.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let promptId = "promptId_example"; // String | A unique identifier for the prompt.
let updatePromptRequest = new AmazonConnectService.UpdatePromptRequest(); // UpdatePromptRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePrompt(instanceId, promptId, updatePromptRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **promptId** | **String**| A unique identifier for the prompt. | 
 **updatePromptRequest** | [**UpdatePromptRequest**](UpdatePromptRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdatePromptResponse**](UpdatePromptResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateQueueHoursOfOperation

> updateQueueHoursOfOperation(instanceId, queueId, updateQueueHoursOfOperationRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates the hours of operation for the specified queue.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let queueId = "queueId_example"; // String | The identifier for the queue.
let updateQueueHoursOfOperationRequest = new AmazonConnectService.UpdateQueueHoursOfOperationRequest(); // UpdateQueueHoursOfOperationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateQueueHoursOfOperation(instanceId, queueId, updateQueueHoursOfOperationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **queueId** | **String**| The identifier for the queue. | 
 **updateQueueHoursOfOperationRequest** | [**UpdateQueueHoursOfOperationRequest**](UpdateQueueHoursOfOperationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateQueueMaxContacts

> updateQueueMaxContacts(instanceId, queueId, updateQueueMaxContactsRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates the maximum number of contacts allowed in a queue before it is considered full.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let queueId = "queueId_example"; // String | The identifier for the queue.
let updateQueueMaxContactsRequest = new AmazonConnectService.UpdateQueueMaxContactsRequest(); // UpdateQueueMaxContactsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateQueueMaxContacts(instanceId, queueId, updateQueueMaxContactsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **queueId** | **String**| The identifier for the queue. | 
 **updateQueueMaxContactsRequest** | [**UpdateQueueMaxContactsRequest**](UpdateQueueMaxContactsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateQueueName

> updateQueueName(instanceId, queueId, updateQueueNameRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates the name and description of a queue. At least &lt;code&gt;Name&lt;/code&gt; or &lt;code&gt;Description&lt;/code&gt; must be provided.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let queueId = "queueId_example"; // String | The identifier for the queue.
let updateQueueNameRequest = new AmazonConnectService.UpdateQueueNameRequest(); // UpdateQueueNameRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateQueueName(instanceId, queueId, updateQueueNameRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **queueId** | **String**| The identifier for the queue. | 
 **updateQueueNameRequest** | [**UpdateQueueNameRequest**](UpdateQueueNameRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateQueueOutboundCallerConfig

> updateQueueOutboundCallerConfig(instanceId, queueId, updateQueueOutboundCallerConfigRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates the outbound caller ID name, number, and outbound whisper flow for a specified queue.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the number being used in the input is claimed to a traffic distribution group, and you are calling this API using an instance in the Amazon Web Services Region where the traffic distribution group was created, you can use either a full phone number ARN or UUID value for the &lt;code&gt;OutboundCallerIdNumberId&lt;/code&gt; value of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_OutboundCallerConfig\&quot;&gt;OutboundCallerConfig&lt;/a&gt; request body parameter. However, if the number is claimed to a traffic distribution group and you are calling this API using an instance in the alternate Amazon Web Services Region associated with the traffic distribution group, you must provide a full phone number ARN. If a UUID is provided in this scenario, you will receive a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Only use the phone number ARN format that doesn&#39;t contain &lt;code&gt;instance&lt;/code&gt; in the path, for example, &lt;code&gt;arn:aws:connect:us-east-1:1234567890:phone-number/uuid&lt;/code&gt;. This is the same ARN format that is returned when you call the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html\&quot;&gt;ListPhoneNumbersV2&lt;/a&gt; API.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let queueId = "queueId_example"; // String | The identifier for the queue.
let updateQueueOutboundCallerConfigRequest = new AmazonConnectService.UpdateQueueOutboundCallerConfigRequest(); // UpdateQueueOutboundCallerConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateQueueOutboundCallerConfig(instanceId, queueId, updateQueueOutboundCallerConfigRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **queueId** | **String**| The identifier for the queue. | 
 **updateQueueOutboundCallerConfigRequest** | [**UpdateQueueOutboundCallerConfigRequest**](UpdateQueueOutboundCallerConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateQueueStatus

> updateQueueStatus(instanceId, queueId, updateQueueStatusRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates the status of the queue.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let queueId = "queueId_example"; // String | The identifier for the queue.
let updateQueueStatusRequest = new AmazonConnectService.UpdateQueueStatusRequest(); // UpdateQueueStatusRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateQueueStatus(instanceId, queueId, updateQueueStatusRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **queueId** | **String**| The identifier for the queue. | 
 **updateQueueStatusRequest** | [**UpdateQueueStatusRequest**](UpdateQueueStatusRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateQuickConnectConfig

> updateQuickConnectConfig(instanceId, quickConnectId, updateQuickConnectConfigRequest, opts)



Updates the configuration settings for the specified quick connect.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let quickConnectId = "quickConnectId_example"; // String | The identifier for the quick connect.
let updateQuickConnectConfigRequest = new AmazonConnectService.UpdateQuickConnectConfigRequest(); // UpdateQuickConnectConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateQuickConnectConfig(instanceId, quickConnectId, updateQuickConnectConfigRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **quickConnectId** | **String**| The identifier for the quick connect. | 
 **updateQuickConnectConfigRequest** | [**UpdateQuickConnectConfigRequest**](UpdateQuickConnectConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateQuickConnectName

> updateQuickConnectName(instanceId, quickConnectId, updateQuickConnectNameRequest, opts)



Updates the name and description of a quick connect. The request accepts the following data in JSON format. At least &lt;code&gt;Name&lt;/code&gt; or &lt;code&gt;Description&lt;/code&gt; must be provided.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let quickConnectId = "quickConnectId_example"; // String | The identifier for the quick connect.
let updateQuickConnectNameRequest = new AmazonConnectService.UpdateQuickConnectNameRequest(); // UpdateQuickConnectNameRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateQuickConnectName(instanceId, quickConnectId, updateQuickConnectNameRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **quickConnectId** | **String**| The identifier for the quick connect. | 
 **updateQuickConnectNameRequest** | [**UpdateQuickConnectNameRequest**](UpdateQuickConnectNameRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRoutingProfileAgentAvailabilityTimer

> updateRoutingProfileAgentAvailabilityTimer(instanceId, routingProfileId, updateRoutingProfileAgentAvailabilityTimerRequest, opts)



Whether agents with this routing profile will have their routing order calculated based on &lt;i&gt;time since their last inbound contact&lt;/i&gt; or &lt;i&gt;longest idle time&lt;/i&gt;. 

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let routingProfileId = "routingProfileId_example"; // String | The identifier of the routing profile.
let updateRoutingProfileAgentAvailabilityTimerRequest = new AmazonConnectService.UpdateRoutingProfileAgentAvailabilityTimerRequest(); // UpdateRoutingProfileAgentAvailabilityTimerRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRoutingProfileAgentAvailabilityTimer(instanceId, routingProfileId, updateRoutingProfileAgentAvailabilityTimerRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **routingProfileId** | **String**| The identifier of the routing profile. | 
 **updateRoutingProfileAgentAvailabilityTimerRequest** | [**UpdateRoutingProfileAgentAvailabilityTimerRequest**](UpdateRoutingProfileAgentAvailabilityTimerRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRoutingProfileConcurrency

> updateRoutingProfileConcurrency(instanceId, routingProfileId, updateRoutingProfileConcurrencyRequest, opts)



Updates the channels that agents can handle in the Contact Control Panel (CCP) for a routing profile.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let routingProfileId = "routingProfileId_example"; // String | The identifier of the routing profile.
let updateRoutingProfileConcurrencyRequest = new AmazonConnectService.UpdateRoutingProfileConcurrencyRequest(); // UpdateRoutingProfileConcurrencyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRoutingProfileConcurrency(instanceId, routingProfileId, updateRoutingProfileConcurrencyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **routingProfileId** | **String**| The identifier of the routing profile. | 
 **updateRoutingProfileConcurrencyRequest** | [**UpdateRoutingProfileConcurrencyRequest**](UpdateRoutingProfileConcurrencyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRoutingProfileDefaultOutboundQueue

> updateRoutingProfileDefaultOutboundQueue(instanceId, routingProfileId, updateRoutingProfileDefaultOutboundQueueRequest, opts)



Updates the default outbound queue of a routing profile.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let routingProfileId = "routingProfileId_example"; // String | The identifier of the routing profile.
let updateRoutingProfileDefaultOutboundQueueRequest = new AmazonConnectService.UpdateRoutingProfileDefaultOutboundQueueRequest(); // UpdateRoutingProfileDefaultOutboundQueueRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRoutingProfileDefaultOutboundQueue(instanceId, routingProfileId, updateRoutingProfileDefaultOutboundQueueRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **routingProfileId** | **String**| The identifier of the routing profile. | 
 **updateRoutingProfileDefaultOutboundQueueRequest** | [**UpdateRoutingProfileDefaultOutboundQueueRequest**](UpdateRoutingProfileDefaultOutboundQueueRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRoutingProfileName

> updateRoutingProfileName(instanceId, routingProfileId, updateRoutingProfileNameRequest, opts)



Updates the name and description of a routing profile. The request accepts the following data in JSON format. At least &lt;code&gt;Name&lt;/code&gt; or &lt;code&gt;Description&lt;/code&gt; must be provided.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let routingProfileId = "routingProfileId_example"; // String | The identifier of the routing profile.
let updateRoutingProfileNameRequest = new AmazonConnectService.UpdateRoutingProfileNameRequest(); // UpdateRoutingProfileNameRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRoutingProfileName(instanceId, routingProfileId, updateRoutingProfileNameRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **routingProfileId** | **String**| The identifier of the routing profile. | 
 **updateRoutingProfileNameRequest** | [**UpdateRoutingProfileNameRequest**](UpdateRoutingProfileNameRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRoutingProfileQueues

> updateRoutingProfileQueues(instanceId, routingProfileId, updateRoutingProfileQueuesRequest, opts)



Updates the properties associated with a set of queues for a routing profile.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let routingProfileId = "routingProfileId_example"; // String | The identifier of the routing profile.
let updateRoutingProfileQueuesRequest = new AmazonConnectService.UpdateRoutingProfileQueuesRequest(); // UpdateRoutingProfileQueuesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRoutingProfileQueues(instanceId, routingProfileId, updateRoutingProfileQueuesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **routingProfileId** | **String**| The identifier of the routing profile. | 
 **updateRoutingProfileQueuesRequest** | [**UpdateRoutingProfileQueuesRequest**](UpdateRoutingProfileQueuesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRule

> updateRule(ruleId, instanceId, updateRuleRequest, opts)



&lt;p&gt;Updates a rule for the specified Amazon Connect instance.&lt;/p&gt; &lt;p&gt;Use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/connect-rules-language.html\&quot;&gt;Rules Function language&lt;/a&gt; to code conditions for the rule. &lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let ruleId = "ruleId_example"; // String | A unique identifier for the rule.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let updateRuleRequest = new AmazonConnectService.UpdateRuleRequest(); // UpdateRuleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRule(ruleId, instanceId, updateRuleRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruleId** | **String**| A unique identifier for the rule. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **updateRuleRequest** | [**UpdateRuleRequest**](UpdateRuleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSecurityProfile

> updateSecurityProfile(securityProfileId, instanceId, updateSecurityProfileRequest, opts)



&lt;p&gt;This API is in preview release for Amazon Connect and is subject to change.&lt;/p&gt; &lt;p&gt;Updates a security profile.&lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let securityProfileId = "securityProfileId_example"; // String | The identifier for the security profle.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let updateSecurityProfileRequest = new AmazonConnectService.UpdateSecurityProfileRequest(); // UpdateSecurityProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSecurityProfile(securityProfileId, instanceId, updateSecurityProfileRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **securityProfileId** | **String**| The identifier for the security profle. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **updateSecurityProfileRequest** | [**UpdateSecurityProfileRequest**](UpdateSecurityProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTaskTemplate

> UpdateTaskTemplateResponse updateTaskTemplate(taskTemplateId, instanceId, updateTaskTemplateRequest, opts)



Updates details about a specific task template in the specified Amazon Connect instance. This operation does not support partial updates. Instead it does a full update of template content.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let taskTemplateId = "taskTemplateId_example"; // String | A unique identifier for the task template.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let updateTaskTemplateRequest = new AmazonConnectService.UpdateTaskTemplateRequest(); // UpdateTaskTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateTaskTemplate(taskTemplateId, instanceId, updateTaskTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskTemplateId** | **String**| A unique identifier for the task template. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **updateTaskTemplateRequest** | [**UpdateTaskTemplateRequest**](UpdateTaskTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateTaskTemplateResponse**](UpdateTaskTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTrafficDistribution

> Object updateTrafficDistribution(id, updateTrafficDistributionRequest, opts)



&lt;p&gt;Updates the traffic distribution for a given traffic distribution group. &lt;/p&gt; &lt;p&gt;For more information about updating a traffic distribution group, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/update-telephony-traffic-distribution.html\&quot;&gt;Update telephony traffic distribution across Amazon Web Services Regions &lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let id = "id_example"; // String | The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.
let updateTrafficDistributionRequest = new AmazonConnectService.UpdateTrafficDistributionRequest(); // UpdateTrafficDistributionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateTrafficDistribution(id, updateTrafficDistributionRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region. | 
 **updateTrafficDistributionRequest** | [**UpdateTrafficDistributionRequest**](UpdateTrafficDistributionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUserHierarchy

> updateUserHierarchy(userId, instanceId, updateUserHierarchyRequest, opts)



Assigns the specified hierarchy group to the specified user.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let userId = "userId_example"; // String | The identifier of the user account.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let updateUserHierarchyRequest = new AmazonConnectService.UpdateUserHierarchyRequest(); // UpdateUserHierarchyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateUserHierarchy(userId, instanceId, updateUserHierarchyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**| The identifier of the user account. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **updateUserHierarchyRequest** | [**UpdateUserHierarchyRequest**](UpdateUserHierarchyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUserHierarchyGroupName

> updateUserHierarchyGroupName(hierarchyGroupId, instanceId, updateUserHierarchyGroupNameRequest, opts)



Updates the name of the user hierarchy group. 

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let hierarchyGroupId = "hierarchyGroupId_example"; // String | The identifier of the hierarchy group.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let updateUserHierarchyGroupNameRequest = new AmazonConnectService.UpdateUserHierarchyGroupNameRequest(); // UpdateUserHierarchyGroupNameRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateUserHierarchyGroupName(hierarchyGroupId, instanceId, updateUserHierarchyGroupNameRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hierarchyGroupId** | **String**| The identifier of the hierarchy group. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **updateUserHierarchyGroupNameRequest** | [**UpdateUserHierarchyGroupNameRequest**](UpdateUserHierarchyGroupNameRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUserHierarchyStructure

> updateUserHierarchyStructure(instanceId, updateUserHierarchyStructureRequest, opts)



Updates the user hierarchy structure: add, remove, and rename user hierarchy levels.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let updateUserHierarchyStructureRequest = new AmazonConnectService.UpdateUserHierarchyStructureRequest(); // UpdateUserHierarchyStructureRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateUserHierarchyStructure(instanceId, updateUserHierarchyStructureRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **updateUserHierarchyStructureRequest** | [**UpdateUserHierarchyStructureRequest**](UpdateUserHierarchyStructureRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUserIdentityInfo

> updateUserIdentityInfo(userId, instanceId, updateUserIdentityInfoRequest, opts)



&lt;p&gt;Updates the identity information for the specified user.&lt;/p&gt; &lt;important&gt; &lt;p&gt;We strongly recommend limiting who has the ability to invoke &lt;code&gt;UpdateUserIdentityInfo&lt;/code&gt;. Someone with that ability can change the login credentials of other users by changing their email address. This poses a security risk to your organization. They can change the email address of a user to the attacker&#39;s email address, and then reset the password through email. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-best-practices.html\&quot;&gt;Best Practices for Security Profiles&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let userId = "userId_example"; // String | The identifier of the user account.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let updateUserIdentityInfoRequest = new AmazonConnectService.UpdateUserIdentityInfoRequest(); // UpdateUserIdentityInfoRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateUserIdentityInfo(userId, instanceId, updateUserIdentityInfoRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**| The identifier of the user account. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **updateUserIdentityInfoRequest** | [**UpdateUserIdentityInfoRequest**](UpdateUserIdentityInfoRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUserPhoneConfig

> updateUserPhoneConfig(userId, instanceId, updateUserPhoneConfigRequest, opts)



Updates the phone configuration settings for the specified user.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let userId = "userId_example"; // String | The identifier of the user account.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let updateUserPhoneConfigRequest = new AmazonConnectService.UpdateUserPhoneConfigRequest(); // UpdateUserPhoneConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateUserPhoneConfig(userId, instanceId, updateUserPhoneConfigRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**| The identifier of the user account. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **updateUserPhoneConfigRequest** | [**UpdateUserPhoneConfigRequest**](UpdateUserPhoneConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUserRoutingProfile

> updateUserRoutingProfile(userId, instanceId, updateUserRoutingProfileRequest, opts)



Assigns the specified routing profile to the specified user.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let userId = "userId_example"; // String | The identifier of the user account.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let updateUserRoutingProfileRequest = new AmazonConnectService.UpdateUserRoutingProfileRequest(); // UpdateUserRoutingProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateUserRoutingProfile(userId, instanceId, updateUserRoutingProfileRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**| The identifier of the user account. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **updateUserRoutingProfileRequest** | [**UpdateUserRoutingProfileRequest**](UpdateUserRoutingProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUserSecurityProfiles

> updateUserSecurityProfiles(userId, instanceId, updateUserSecurityProfilesRequest, opts)



Assigns the specified security profiles to the specified user.

### Example

```javascript
import AmazonConnectService from 'amazon_connect_service';
let defaultClient = AmazonConnectService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectService.DefaultApi();
let userId = "userId_example"; // String | The identifier of the user account.
let instanceId = "instanceId_example"; // String | The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.
let updateUserSecurityProfilesRequest = new AmazonConnectService.UpdateUserSecurityProfilesRequest(); // UpdateUserSecurityProfilesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateUserSecurityProfiles(userId, instanceId, updateUserSecurityProfilesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**| The identifier of the user account. | 
 **instanceId** | **String**| The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
 **updateUserSecurityProfilesRequest** | [**UpdateUserSecurityProfilesRequest**](UpdateUserSecurityProfilesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

