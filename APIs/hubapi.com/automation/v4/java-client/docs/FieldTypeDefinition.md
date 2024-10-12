

# FieldTypeDefinition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** |  |  [optional] |
|**externalOptions** | **Boolean** |  |  |
|**externalOptionsReferenceType** | **String** |  |  [optional] |
|**fieldType** | [**FieldTypeEnum**](#FieldTypeEnum) |  |  [optional] |
|**helpText** | **String** |  |  [optional] |
|**label** | **String** |  |  [optional] |
|**name** | **String** |  |  |
|**options** | [**List&lt;Option&gt;**](Option.md) |  |  |
|**optionsUrl** | **String** |  |  [optional] |
|**referencedObjectType** | [**ReferencedObjectTypeEnum**](#ReferencedObjectTypeEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: FieldTypeEnum

| Name | Value |
|---- | -----|
| BOOLEANCHECKBOX | &quot;booleancheckbox&quot; |
| CHECKBOX | &quot;checkbox&quot; |
| DATE | &quot;date&quot; |
| FILE | &quot;file&quot; |
| NUMBER | &quot;number&quot; |
| PHONENUMBER | &quot;phonenumber&quot; |
| RADIO | &quot;radio&quot; |
| SELECT | &quot;select&quot; |
| TEXT | &quot;text&quot; |
| TEXTAREA | &quot;textarea&quot; |
| CALCULATION_EQUATION | &quot;calculation_equation&quot; |
| CALCULATION_ROLLUP | &quot;calculation_rollup&quot; |
| CALCULATION_SCORE | &quot;calculation_score&quot; |
| CALCULATION_READ_TIME | &quot;calculation_read_time&quot; |
| UNKNOWN | &quot;unknown&quot; |
| HTML | &quot;html&quot; |



## Enum: ReferencedObjectTypeEnum

| Name | Value |
|---- | -----|
| CONTACT | &quot;CONTACT&quot; |
| COMPANY | &quot;COMPANY&quot; |
| DEAL | &quot;DEAL&quot; |
| ENGAGEMENT | &quot;ENGAGEMENT&quot; |
| TICKET | &quot;TICKET&quot; |
| OWNER | &quot;OWNER&quot; |
| PRODUCT | &quot;PRODUCT&quot; |
| LINE_ITEM | &quot;LINE_ITEM&quot; |
| BET_DELIVERABLE_SERVICE | &quot;BET_DELIVERABLE_SERVICE&quot; |
| CONTENT | &quot;CONTENT&quot; |
| CONVERSATION | &quot;CONVERSATION&quot; |
| BET_ALERT | &quot;BET_ALERT&quot; |
| PORTAL | &quot;PORTAL&quot; |
| QUOTE | &quot;QUOTE&quot; |
| FORM_SUBMISSION_INBOUNDDB | &quot;FORM_SUBMISSION_INBOUNDDB&quot; |
| QUOTA | &quot;QUOTA&quot; |
| UNSUBSCRIBE | &quot;UNSUBSCRIBE&quot; |
| COMMUNICATION | &quot;COMMUNICATION&quot; |
| FEEDBACK_SUBMISSION | &quot;FEEDBACK_SUBMISSION&quot; |
| ATTRIBUTION | &quot;ATTRIBUTION&quot; |
| SALESFORCE_SYNC_ERROR | &quot;SALESFORCE_SYNC_ERROR&quot; |
| RESTORABLE_CRM_OBJECT | &quot;RESTORABLE_CRM_OBJECT&quot; |
| HUB | &quot;HUB&quot; |
| LANDING_PAGE | &quot;LANDING_PAGE&quot; |
| PRODUCT_OR_FOLDER | &quot;PRODUCT_OR_FOLDER&quot; |
| TASK | &quot;TASK&quot; |
| FORM | &quot;FORM&quot; |
| MARKETING_EMAIL | &quot;MARKETING_EMAIL&quot; |
| AD_ACCOUNT | &quot;AD_ACCOUNT&quot; |
| AD_CAMPAIGN | &quot;AD_CAMPAIGN&quot; |
| AD_GROUP | &quot;AD_GROUP&quot; |
| AD | &quot;AD&quot; |
| KEYWORD | &quot;KEYWORD&quot; |
| CAMPAIGN | &quot;CAMPAIGN&quot; |
| SOCIAL_CHANNEL | &quot;SOCIAL_CHANNEL&quot; |
| SOCIAL_POST | &quot;SOCIAL_POST&quot; |
| SITE_PAGE | &quot;SITE_PAGE&quot; |
| BLOG_POST | &quot;BLOG_POST&quot; |
| IMPORT | &quot;IMPORT&quot; |
| EXPORT | &quot;EXPORT&quot; |
| CTA | &quot;CTA&quot; |
| TASK_TEMPLATE | &quot;TASK_TEMPLATE&quot; |
| AUTOMATION_PLATFORM_FLOW | &quot;AUTOMATION_PLATFORM_FLOW&quot; |
| OBJECT_LIST | &quot;OBJECT_LIST&quot; |
| NOTE | &quot;NOTE&quot; |
| MEETING_EVENT | &quot;MEETING_EVENT&quot; |
| CALL | &quot;CALL&quot; |
| EMAIL | &quot;EMAIL&quot; |
| PUBLISHING_TASK | &quot;PUBLISHING_TASK&quot; |
| CONVERSATION_SESSION | &quot;CONVERSATION_SESSION&quot; |
| CONTACT_CREATE_ATTRIBUTION | &quot;CONTACT_CREATE_ATTRIBUTION&quot; |
| INVOICE | &quot;INVOICE&quot; |
| MARKETING_EVENT | &quot;MARKETING_EVENT&quot; |
| CONVERSATION_INBOX | &quot;CONVERSATION_INBOX&quot; |
| CHATFLOW | &quot;CHATFLOW&quot; |
| MEDIA_BRIDGE | &quot;MEDIA_BRIDGE&quot; |
| SEQUENCE | &quot;SEQUENCE&quot; |
| SEQUENCE_STEP | &quot;SEQUENCE_STEP&quot; |
| FORECAST | &quot;FORECAST&quot; |
| SNIPPET | &quot;SNIPPET&quot; |
| TEMPLATE | &quot;TEMPLATE&quot; |
| DEAL_CREATE_ATTRIBUTION | &quot;DEAL_CREATE_ATTRIBUTION&quot; |
| QUOTE_TEMPLATE | &quot;QUOTE_TEMPLATE&quot; |
| QUOTE_MODULE | &quot;QUOTE_MODULE&quot; |
| QUOTE_MODULE_FIELD | &quot;QUOTE_MODULE_FIELD&quot; |
| QUOTE_FIELD | &quot;QUOTE_FIELD&quot; |
| SEQUENCE_ENROLLMENT | &quot;SEQUENCE_ENROLLMENT&quot; |
| SUBSCRIPTION | &quot;SUBSCRIPTION&quot; |
| ACCEPTANCE_TEST | &quot;ACCEPTANCE_TEST&quot; |
| SOCIAL_BROADCAST | &quot;SOCIAL_BROADCAST&quot; |
| DEAL_SPLIT | &quot;DEAL_SPLIT&quot; |
| DEAL_REGISTRATION | &quot;DEAL_REGISTRATION&quot; |
| GOAL_TARGET | &quot;GOAL_TARGET&quot; |
| GOAL_TARGET_GROUP | &quot;GOAL_TARGET_GROUP&quot; |
| PORTAL_OBJECT_SYNC_MESSAGE | &quot;PORTAL_OBJECT_SYNC_MESSAGE&quot; |
| FILE_MANAGER_FILE | &quot;FILE_MANAGER_FILE&quot; |
| FILE_MANAGER_FOLDER | &quot;FILE_MANAGER_FOLDER&quot; |
| SEQUENCE_STEP_ENROLLMENT | &quot;SEQUENCE_STEP_ENROLLMENT&quot; |
| APPROVAL | &quot;APPROVAL&quot; |
| APPROVAL_STEP | &quot;APPROVAL_STEP&quot; |
| CTA_VARIANT | &quot;CTA_VARIANT&quot; |
| SALES_DOCUMENT | &quot;SALES_DOCUMENT&quot; |
| DISCOUNT | &quot;DISCOUNT&quot; |
| FEE | &quot;FEE&quot; |
| TAX | &quot;TAX&quot; |
| MARKETING_CALENDAR | &quot;MARKETING_CALENDAR&quot; |
| PERMISSIONS_TESTING | &quot;PERMISSIONS_TESTING&quot; |
| PRIVACY_SCANNER_COOKIE | &quot;PRIVACY_SCANNER_COOKIE&quot; |
| DATA_SYNC_STATE | &quot;DATA_SYNC_STATE&quot; |
| WEB_INTERACTIVE | &quot;WEB_INTERACTIVE&quot; |
| PLAYBOOK | &quot;PLAYBOOK&quot; |
| FOLDER | &quot;FOLDER&quot; |
| PLAYBOOK_QUESTION | &quot;PLAYBOOK_QUESTION&quot; |
| PLAYBOOK_SUBMISSION | &quot;PLAYBOOK_SUBMISSION&quot; |
| PLAYBOOK_SUBMISSION_ANSWER | &quot;PLAYBOOK_SUBMISSION_ANSWER&quot; |
| COMMERCE_PAYMENT | &quot;COMMERCE_PAYMENT&quot; |
| GSC_PROPERTY | &quot;GSC_PROPERTY&quot; |
| SOX_PROTECTED_DUMMY_TYPE | &quot;SOX_PROTECTED_DUMMY_TYPE&quot; |
| BLOG_LISTING_PAGE | &quot;BLOG_LISTING_PAGE&quot; |
| QUARANTINED_SUBMISSION | &quot;QUARANTINED_SUBMISSION&quot; |
| PAYMENT_SCHEDULE | &quot;PAYMENT_SCHEDULE&quot; |
| PAYMENT_SCHEDULE_INSTALLMENT | &quot;PAYMENT_SCHEDULE_INSTALLMENT&quot; |
| MARKETING_CAMPAIGN_UTM | &quot;MARKETING_CAMPAIGN_UTM&quot; |
| DISCOUNT_TEMPLATE | &quot;DISCOUNT_TEMPLATE&quot; |
| DISCOUNT_CODE | &quot;DISCOUNT_CODE&quot; |
| FEEDBACK_SURVEY | &quot;FEEDBACK_SURVEY&quot; |
| CMS_URL | &quot;CMS_URL&quot; |
| SALES_TASK | &quot;SALES_TASK&quot; |
| SALES_WORKLOAD | &quot;SALES_WORKLOAD&quot; |
| USER | &quot;USER&quot; |
| POSTAL_MAIL | &quot;POSTAL_MAIL&quot; |
| SCHEMAS_BACKEND_TEST | &quot;SCHEMAS_BACKEND_TEST&quot; |
| PAYMENT_LINK | &quot;PAYMENT_LINK&quot; |
| SUBMISSION_TAG | &quot;SUBMISSION_TAG&quot; |
| CAMPAIGN_STEP | &quot;CAMPAIGN_STEP&quot; |
| SCHEDULING_PAGE | &quot;SCHEDULING_PAGE&quot; |
| SOX_PROTECTED_TEST_TYPE | &quot;SOX_PROTECTED_TEST_TYPE&quot; |
| ORDER | &quot;ORDER&quot; |
| MARKETING_SMS | &quot;MARKETING_SMS&quot; |
| PARTNER_ACCOUNT | &quot;PARTNER_ACCOUNT&quot; |
| CAMPAIGN_TEMPLATE | &quot;CAMPAIGN_TEMPLATE&quot; |
| CAMPAIGN_TEMPLATE_STEP | &quot;CAMPAIGN_TEMPLATE_STEP&quot; |
| PLAYLIST | &quot;PLAYLIST&quot; |
| CLIP | &quot;CLIP&quot; |
| CAMPAIGN_BUDGET_ITEM | &quot;CAMPAIGN_BUDGET_ITEM&quot; |
| CAMPAIGN_SPEND_ITEM | &quot;CAMPAIGN_SPEND_ITEM&quot; |
| MIC | &quot;MIC&quot; |
| CONTENT_AUDIT | &quot;CONTENT_AUDIT&quot; |
| CONTENT_AUDIT_PAGE | &quot;CONTENT_AUDIT_PAGE&quot; |
| PLAYLIST_FOLDER | &quot;PLAYLIST_FOLDER&quot; |
| LEAD | &quot;LEAD&quot; |
| ABANDONED_CART | &quot;ABANDONED_CART&quot; |
| EXTERNAL_WEB_URL | &quot;EXTERNAL_WEB_URL&quot; |
| VIEW | &quot;VIEW&quot; |
| VIEW_BLOCK | &quot;VIEW_BLOCK&quot; |
| ROSTER | &quot;ROSTER&quot; |
| CART | &quot;CART&quot; |
| AUTOMATION_PLATFORM_FLOW_ACTION | &quot;AUTOMATION_PLATFORM_FLOW_ACTION&quot; |
| SOCIAL_PROFILE | &quot;SOCIAL_PROFILE&quot; |
| PARTNER_CLIENT | &quot;PARTNER_CLIENT&quot; |
| ROSTER_MEMBER | &quot;ROSTER_MEMBER&quot; |
| MARKETING_EVENT_ATTENDANCE | &quot;MARKETING_EVENT_ATTENDANCE&quot; |
| ALL_PAGES | &quot;ALL_PAGES&quot; |
| AI_FORECAST | &quot;AI_FORECAST&quot; |
| CRM_PIPELINES_DUMMY_TYPE | &quot;CRM_PIPELINES_DUMMY_TYPE&quot; |
| KNOWLEDGE_ARTICLE | &quot;KNOWLEDGE_ARTICLE&quot; |
| PROPERTY_INFO | &quot;PROPERTY_INFO&quot; |
| DATA_PRIVACY_CONSENT | &quot;DATA_PRIVACY_CONSENT&quot; |
| GOAL_TEMPLATE | &quot;GOAL_TEMPLATE&quot; |
| SCORE_CONFIGURATION | &quot;SCORE_CONFIGURATION&quot; |
| AUDIENCE | &quot;AUDIENCE&quot; |
| PARTNER_CLIENT_REVENUE | &quot;PARTNER_CLIENT_REVENUE&quot; |
| AUTOMATION_JOURNEY | &quot;AUTOMATION_JOURNEY&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| STRING | &quot;string&quot; |
| NUMBER | &quot;number&quot; |
| BOOL | &quot;bool&quot; |
| DATETIME | &quot;datetime&quot; |
| ENUMERATION | &quot;enumeration&quot; |
| DATE | &quot;date&quot; |
| PHONE_NUMBER | &quot;phone_number&quot; |
| CURRENCY_NUMBER | &quot;currency_number&quot; |
| JSON | &quot;json&quot; |
| OBJECT_COORDINATES | &quot;object_coordinates&quot; |



