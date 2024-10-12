# AutomationActionsV4.FieldTypeDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** |  | [optional] 
**externalOptions** | **Boolean** |  | 
**externalOptionsReferenceType** | **String** |  | [optional] 
**fieldType** | **String** |  | [optional] 
**helpText** | **String** |  | [optional] 
**label** | **String** |  | [optional] 
**name** | **String** |  | 
**options** | [**[Option]**](Option.md) |  | 
**optionsUrl** | **String** |  | [optional] 
**referencedObjectType** | **String** |  | [optional] 
**type** | **String** |  | 



## Enum: FieldTypeEnum


* `booleancheckbox` (value: `"booleancheckbox"`)

* `checkbox` (value: `"checkbox"`)

* `date` (value: `"date"`)

* `file` (value: `"file"`)

* `number` (value: `"number"`)

* `phonenumber` (value: `"phonenumber"`)

* `radio` (value: `"radio"`)

* `select` (value: `"select"`)

* `text` (value: `"text"`)

* `textarea` (value: `"textarea"`)

* `calculation_equation` (value: `"calculation_equation"`)

* `calculation_rollup` (value: `"calculation_rollup"`)

* `calculation_score` (value: `"calculation_score"`)

* `calculation_read_time` (value: `"calculation_read_time"`)

* `unknown` (value: `"unknown"`)

* `html` (value: `"html"`)





## Enum: ReferencedObjectTypeEnum


* `CONTACT` (value: `"CONTACT"`)

* `COMPANY` (value: `"COMPANY"`)

* `DEAL` (value: `"DEAL"`)

* `ENGAGEMENT` (value: `"ENGAGEMENT"`)

* `TICKET` (value: `"TICKET"`)

* `OWNER` (value: `"OWNER"`)

* `PRODUCT` (value: `"PRODUCT"`)

* `LINE_ITEM` (value: `"LINE_ITEM"`)

* `BET_DELIVERABLE_SERVICE` (value: `"BET_DELIVERABLE_SERVICE"`)

* `CONTENT` (value: `"CONTENT"`)

* `CONVERSATION` (value: `"CONVERSATION"`)

* `BET_ALERT` (value: `"BET_ALERT"`)

* `PORTAL` (value: `"PORTAL"`)

* `QUOTE` (value: `"QUOTE"`)

* `FORM_SUBMISSION_INBOUNDDB` (value: `"FORM_SUBMISSION_INBOUNDDB"`)

* `QUOTA` (value: `"QUOTA"`)

* `UNSUBSCRIBE` (value: `"UNSUBSCRIBE"`)

* `COMMUNICATION` (value: `"COMMUNICATION"`)

* `FEEDBACK_SUBMISSION` (value: `"FEEDBACK_SUBMISSION"`)

* `ATTRIBUTION` (value: `"ATTRIBUTION"`)

* `SALESFORCE_SYNC_ERROR` (value: `"SALESFORCE_SYNC_ERROR"`)

* `RESTORABLE_CRM_OBJECT` (value: `"RESTORABLE_CRM_OBJECT"`)

* `HUB` (value: `"HUB"`)

* `LANDING_PAGE` (value: `"LANDING_PAGE"`)

* `PRODUCT_OR_FOLDER` (value: `"PRODUCT_OR_FOLDER"`)

* `TASK` (value: `"TASK"`)

* `FORM` (value: `"FORM"`)

* `MARKETING_EMAIL` (value: `"MARKETING_EMAIL"`)

* `AD_ACCOUNT` (value: `"AD_ACCOUNT"`)

* `AD_CAMPAIGN` (value: `"AD_CAMPAIGN"`)

* `AD_GROUP` (value: `"AD_GROUP"`)

* `AD` (value: `"AD"`)

* `KEYWORD` (value: `"KEYWORD"`)

* `CAMPAIGN` (value: `"CAMPAIGN"`)

* `SOCIAL_CHANNEL` (value: `"SOCIAL_CHANNEL"`)

* `SOCIAL_POST` (value: `"SOCIAL_POST"`)

* `SITE_PAGE` (value: `"SITE_PAGE"`)

* `BLOG_POST` (value: `"BLOG_POST"`)

* `IMPORT` (value: `"IMPORT"`)

* `EXPORT` (value: `"EXPORT"`)

* `CTA` (value: `"CTA"`)

* `TASK_TEMPLATE` (value: `"TASK_TEMPLATE"`)

* `AUTOMATION_PLATFORM_FLOW` (value: `"AUTOMATION_PLATFORM_FLOW"`)

* `OBJECT_LIST` (value: `"OBJECT_LIST"`)

* `NOTE` (value: `"NOTE"`)

* `MEETING_EVENT` (value: `"MEETING_EVENT"`)

* `CALL` (value: `"CALL"`)

* `EMAIL` (value: `"EMAIL"`)

* `PUBLISHING_TASK` (value: `"PUBLISHING_TASK"`)

* `CONVERSATION_SESSION` (value: `"CONVERSATION_SESSION"`)

* `CONTACT_CREATE_ATTRIBUTION` (value: `"CONTACT_CREATE_ATTRIBUTION"`)

* `INVOICE` (value: `"INVOICE"`)

* `MARKETING_EVENT` (value: `"MARKETING_EVENT"`)

* `CONVERSATION_INBOX` (value: `"CONVERSATION_INBOX"`)

* `CHATFLOW` (value: `"CHATFLOW"`)

* `MEDIA_BRIDGE` (value: `"MEDIA_BRIDGE"`)

* `SEQUENCE` (value: `"SEQUENCE"`)

* `SEQUENCE_STEP` (value: `"SEQUENCE_STEP"`)

* `FORECAST` (value: `"FORECAST"`)

* `SNIPPET` (value: `"SNIPPET"`)

* `TEMPLATE` (value: `"TEMPLATE"`)

* `DEAL_CREATE_ATTRIBUTION` (value: `"DEAL_CREATE_ATTRIBUTION"`)

* `QUOTE_TEMPLATE` (value: `"QUOTE_TEMPLATE"`)

* `QUOTE_MODULE` (value: `"QUOTE_MODULE"`)

* `QUOTE_MODULE_FIELD` (value: `"QUOTE_MODULE_FIELD"`)

* `QUOTE_FIELD` (value: `"QUOTE_FIELD"`)

* `SEQUENCE_ENROLLMENT` (value: `"SEQUENCE_ENROLLMENT"`)

* `SUBSCRIPTION` (value: `"SUBSCRIPTION"`)

* `ACCEPTANCE_TEST` (value: `"ACCEPTANCE_TEST"`)

* `SOCIAL_BROADCAST` (value: `"SOCIAL_BROADCAST"`)

* `DEAL_SPLIT` (value: `"DEAL_SPLIT"`)

* `DEAL_REGISTRATION` (value: `"DEAL_REGISTRATION"`)

* `GOAL_TARGET` (value: `"GOAL_TARGET"`)

* `GOAL_TARGET_GROUP` (value: `"GOAL_TARGET_GROUP"`)

* `PORTAL_OBJECT_SYNC_MESSAGE` (value: `"PORTAL_OBJECT_SYNC_MESSAGE"`)

* `FILE_MANAGER_FILE` (value: `"FILE_MANAGER_FILE"`)

* `FILE_MANAGER_FOLDER` (value: `"FILE_MANAGER_FOLDER"`)

* `SEQUENCE_STEP_ENROLLMENT` (value: `"SEQUENCE_STEP_ENROLLMENT"`)

* `APPROVAL` (value: `"APPROVAL"`)

* `APPROVAL_STEP` (value: `"APPROVAL_STEP"`)

* `CTA_VARIANT` (value: `"CTA_VARIANT"`)

* `SALES_DOCUMENT` (value: `"SALES_DOCUMENT"`)

* `DISCOUNT` (value: `"DISCOUNT"`)

* `FEE` (value: `"FEE"`)

* `TAX` (value: `"TAX"`)

* `MARKETING_CALENDAR` (value: `"MARKETING_CALENDAR"`)

* `PERMISSIONS_TESTING` (value: `"PERMISSIONS_TESTING"`)

* `PRIVACY_SCANNER_COOKIE` (value: `"PRIVACY_SCANNER_COOKIE"`)

* `DATA_SYNC_STATE` (value: `"DATA_SYNC_STATE"`)

* `WEB_INTERACTIVE` (value: `"WEB_INTERACTIVE"`)

* `PLAYBOOK` (value: `"PLAYBOOK"`)

* `FOLDER` (value: `"FOLDER"`)

* `PLAYBOOK_QUESTION` (value: `"PLAYBOOK_QUESTION"`)

* `PLAYBOOK_SUBMISSION` (value: `"PLAYBOOK_SUBMISSION"`)

* `PLAYBOOK_SUBMISSION_ANSWER` (value: `"PLAYBOOK_SUBMISSION_ANSWER"`)

* `COMMERCE_PAYMENT` (value: `"COMMERCE_PAYMENT"`)

* `GSC_PROPERTY` (value: `"GSC_PROPERTY"`)

* `SOX_PROTECTED_DUMMY_TYPE` (value: `"SOX_PROTECTED_DUMMY_TYPE"`)

* `BLOG_LISTING_PAGE` (value: `"BLOG_LISTING_PAGE"`)

* `QUARANTINED_SUBMISSION` (value: `"QUARANTINED_SUBMISSION"`)

* `PAYMENT_SCHEDULE` (value: `"PAYMENT_SCHEDULE"`)

* `PAYMENT_SCHEDULE_INSTALLMENT` (value: `"PAYMENT_SCHEDULE_INSTALLMENT"`)

* `MARKETING_CAMPAIGN_UTM` (value: `"MARKETING_CAMPAIGN_UTM"`)

* `DISCOUNT_TEMPLATE` (value: `"DISCOUNT_TEMPLATE"`)

* `DISCOUNT_CODE` (value: `"DISCOUNT_CODE"`)

* `FEEDBACK_SURVEY` (value: `"FEEDBACK_SURVEY"`)

* `CMS_URL` (value: `"CMS_URL"`)

* `SALES_TASK` (value: `"SALES_TASK"`)

* `SALES_WORKLOAD` (value: `"SALES_WORKLOAD"`)

* `USER` (value: `"USER"`)

* `POSTAL_MAIL` (value: `"POSTAL_MAIL"`)

* `SCHEMAS_BACKEND_TEST` (value: `"SCHEMAS_BACKEND_TEST"`)

* `PAYMENT_LINK` (value: `"PAYMENT_LINK"`)

* `SUBMISSION_TAG` (value: `"SUBMISSION_TAG"`)

* `CAMPAIGN_STEP` (value: `"CAMPAIGN_STEP"`)

* `SCHEDULING_PAGE` (value: `"SCHEDULING_PAGE"`)

* `SOX_PROTECTED_TEST_TYPE` (value: `"SOX_PROTECTED_TEST_TYPE"`)

* `ORDER` (value: `"ORDER"`)

* `MARKETING_SMS` (value: `"MARKETING_SMS"`)

* `PARTNER_ACCOUNT` (value: `"PARTNER_ACCOUNT"`)

* `CAMPAIGN_TEMPLATE` (value: `"CAMPAIGN_TEMPLATE"`)

* `CAMPAIGN_TEMPLATE_STEP` (value: `"CAMPAIGN_TEMPLATE_STEP"`)

* `PLAYLIST` (value: `"PLAYLIST"`)

* `CLIP` (value: `"CLIP"`)

* `CAMPAIGN_BUDGET_ITEM` (value: `"CAMPAIGN_BUDGET_ITEM"`)

* `CAMPAIGN_SPEND_ITEM` (value: `"CAMPAIGN_SPEND_ITEM"`)

* `MIC` (value: `"MIC"`)

* `CONTENT_AUDIT` (value: `"CONTENT_AUDIT"`)

* `CONTENT_AUDIT_PAGE` (value: `"CONTENT_AUDIT_PAGE"`)

* `PLAYLIST_FOLDER` (value: `"PLAYLIST_FOLDER"`)

* `LEAD` (value: `"LEAD"`)

* `ABANDONED_CART` (value: `"ABANDONED_CART"`)

* `EXTERNAL_WEB_URL` (value: `"EXTERNAL_WEB_URL"`)

* `VIEW` (value: `"VIEW"`)

* `VIEW_BLOCK` (value: `"VIEW_BLOCK"`)

* `ROSTER` (value: `"ROSTER"`)

* `CART` (value: `"CART"`)

* `AUTOMATION_PLATFORM_FLOW_ACTION` (value: `"AUTOMATION_PLATFORM_FLOW_ACTION"`)

* `SOCIAL_PROFILE` (value: `"SOCIAL_PROFILE"`)

* `PARTNER_CLIENT` (value: `"PARTNER_CLIENT"`)

* `ROSTER_MEMBER` (value: `"ROSTER_MEMBER"`)

* `MARKETING_EVENT_ATTENDANCE` (value: `"MARKETING_EVENT_ATTENDANCE"`)

* `ALL_PAGES` (value: `"ALL_PAGES"`)

* `AI_FORECAST` (value: `"AI_FORECAST"`)

* `CRM_PIPELINES_DUMMY_TYPE` (value: `"CRM_PIPELINES_DUMMY_TYPE"`)

* `KNOWLEDGE_ARTICLE` (value: `"KNOWLEDGE_ARTICLE"`)

* `PROPERTY_INFO` (value: `"PROPERTY_INFO"`)

* `DATA_PRIVACY_CONSENT` (value: `"DATA_PRIVACY_CONSENT"`)

* `GOAL_TEMPLATE` (value: `"GOAL_TEMPLATE"`)

* `SCORE_CONFIGURATION` (value: `"SCORE_CONFIGURATION"`)

* `AUDIENCE` (value: `"AUDIENCE"`)

* `PARTNER_CLIENT_REVENUE` (value: `"PARTNER_CLIENT_REVENUE"`)

* `AUTOMATION_JOURNEY` (value: `"AUTOMATION_JOURNEY"`)

* `UNKNOWN` (value: `"UNKNOWN"`)





## Enum: TypeEnum


* `string` (value: `"string"`)

* `number` (value: `"number"`)

* `bool` (value: `"bool"`)

* `datetime` (value: `"datetime"`)

* `enumeration` (value: `"enumeration"`)

* `date` (value: `"date"`)

* `phone_number` (value: `"phone_number"`)

* `currency_number` (value: `"currency_number"`)

* `json` (value: `"json"`)

* `object_coordinates` (value: `"object_coordinates"`)




