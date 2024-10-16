# call_fire_api_documentation

CallFireApiDocumentation - JavaScript client for call_fire_api_documentation
CallFire
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: V2
- Package version: V2
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://www.callfire.com](https://www.callfire.com)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install call_fire_api_documentation --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your call_fire_api_documentation from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var CallFireApiDocumentation = require('call_fire_api_documentation');

var defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
var basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME'
basicAuth.password = 'YOUR PASSWORD'

var api = new CallFireApiDocumentation.CallsApi()
var id = 789; // {Number} An id of a call broadcast
var opts = {
  'strictValidation': true, // {Boolean} Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
  'batchRequest': new CallFireApiDocumentation.BatchRequest() // {BatchRequest} A request object
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.addCallBroadcastBatch(id, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.callfire.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CallFireApiDocumentation.CallsApi* | [**addCallBroadcastBatch**](docs/CallsApi.md#addCallBroadcastBatch) | **POST** /calls/broadcasts/{id}/batches | Add batches to a call broadcast
*CallFireApiDocumentation.CallsApi* | [**addCallBroadcastRecipients**](docs/CallsApi.md#addCallBroadcastRecipients) | **POST** /calls/broadcasts/{id}/recipients | Add recipients to a call broadcast
*CallFireApiDocumentation.CallsApi* | [**archiveVoiceBroadcast**](docs/CallsApi.md#archiveVoiceBroadcast) | **POST** /calls/broadcasts/{id}/archive | Archive voice broadcast
*CallFireApiDocumentation.CallsApi* | [**createCallBroadcast**](docs/CallsApi.md#createCallBroadcast) | **POST** /calls/broadcasts | Create a call broadcast
*CallFireApiDocumentation.CallsApi* | [**findCallBroadcasts**](docs/CallsApi.md#findCallBroadcasts) | **GET** /calls/broadcasts | Find call broadcasts
*CallFireApiDocumentation.CallsApi* | [**findCalls**](docs/CallsApi.md#findCalls) | **GET** /calls | Find calls
*CallFireApiDocumentation.CallsApi* | [**getCall**](docs/CallsApi.md#getCall) | **GET** /calls/{id} | Find a specific call
*CallFireApiDocumentation.CallsApi* | [**getCallBroadcast**](docs/CallsApi.md#getCallBroadcast) | **GET** /calls/broadcasts/{id} | Find a specific call broadcast
*CallFireApiDocumentation.CallsApi* | [**getCallBroadcastBatches**](docs/CallsApi.md#getCallBroadcastBatches) | **GET** /calls/broadcasts/{id}/batches | Find batches in a call broadcast
*CallFireApiDocumentation.CallsApi* | [**getCallBroadcastCalls**](docs/CallsApi.md#getCallBroadcastCalls) | **GET** /calls/broadcasts/{id}/calls | Find calls in a call broadcast
*CallFireApiDocumentation.CallsApi* | [**getCallBroadcastStats**](docs/CallsApi.md#getCallBroadcastStats) | **GET** /calls/broadcasts/{id}/stats | Get statistics on call broadcast
*CallFireApiDocumentation.CallsApi* | [**getCallRecording**](docs/CallsApi.md#getCallRecording) | **GET** /calls/recordings/{id} | Get call recording by id
*CallFireApiDocumentation.CallsApi* | [**getCallRecordingByName**](docs/CallsApi.md#getCallRecordingByName) | **GET** /calls/{id}/recordings/{name} | Get call recording by name
*CallFireApiDocumentation.CallsApi* | [**getCallRecordingMp3**](docs/CallsApi.md#getCallRecordingMp3) | **GET** /calls/recordings/{id}.mp3 | Get call recording in mp3 format
*CallFireApiDocumentation.CallsApi* | [**getCallRecordingMp3ByName**](docs/CallsApi.md#getCallRecordingMp3ByName) | **GET** /calls/{id}/recordings/{name}.mp3 | Get call mp3 recording by name
*CallFireApiDocumentation.CallsApi* | [**getCallRecordings**](docs/CallsApi.md#getCallRecordings) | **GET** /calls/{id}/recordings | Get call recordings for a call
*CallFireApiDocumentation.CallsApi* | [**sendCalls**](docs/CallsApi.md#sendCalls) | **POST** /calls | Send calls
*CallFireApiDocumentation.CallsApi* | [**startVoiceBroadcast**](docs/CallsApi.md#startVoiceBroadcast) | **POST** /calls/broadcasts/{id}/start | Start voice broadcast
*CallFireApiDocumentation.CallsApi* | [**stopVoiceBroadcast**](docs/CallsApi.md#stopVoiceBroadcast) | **POST** /calls/broadcasts/{id}/stop | Stop voice broadcast
*CallFireApiDocumentation.CallsApi* | [**toggleCallBroadcastRecipientsStatus**](docs/CallsApi.md#toggleCallBroadcastRecipientsStatus) | **POST** /calls/broadcasts/{id}/toggleRecipientsStatus | Disable/enable undialed recipients in broadcast
*CallFireApiDocumentation.CallsApi* | [**updateCallBroadcast**](docs/CallsApi.md#updateCallBroadcast) | **PUT** /calls/broadcasts/{id} | Update a call broadcast
*CallFireApiDocumentation.CampaignsApi* | [**deleteCampaignSound**](docs/CampaignsApi.md#deleteCampaignSound) | **DELETE** /campaigns/sounds/{id} | Delete a specific sound
*CallFireApiDocumentation.CampaignsApi* | [**findCampaignSounds**](docs/CampaignsApi.md#findCampaignSounds) | **GET** /campaigns/sounds | Find sounds
*CallFireApiDocumentation.CampaignsApi* | [**getCampaignBatch**](docs/CampaignsApi.md#getCampaignBatch) | **GET** /campaigns/batches/{id} | Find a specific batch
*CallFireApiDocumentation.CampaignsApi* | [**getCampaignSound**](docs/CampaignsApi.md#getCampaignSound) | **GET** /campaigns/sounds/{id} | Find a specific sound
*CallFireApiDocumentation.CampaignsApi* | [**getCampaignSoundDataMp3**](docs/CampaignsApi.md#getCampaignSoundDataMp3) | **GET** /campaigns/sounds/{id}.mp3 | Download a MP3 sound
*CallFireApiDocumentation.CampaignsApi* | [**getCampaignSoundDataWav**](docs/CampaignsApi.md#getCampaignSoundDataWav) | **GET** /campaigns/sounds/{id}.wav | Download a WAV sound
*CallFireApiDocumentation.CampaignsApi* | [**postCallCampaignSound**](docs/CampaignsApi.md#postCallCampaignSound) | **POST** /campaigns/sounds/calls | Add sound via call
*CallFireApiDocumentation.CampaignsApi* | [**postFileCampaignSound**](docs/CampaignsApi.md#postFileCampaignSound) | **POST** /campaigns/sounds/files | Add sound via file
*CallFireApiDocumentation.CampaignsApi* | [**postTTSCampaignSound**](docs/CampaignsApi.md#postTTSCampaignSound) | **POST** /campaigns/sounds/tts | Add sound via text-to-speech
*CallFireApiDocumentation.CampaignsApi* | [**updateCampaignBatch**](docs/CampaignsApi.md#updateCampaignBatch) | **PUT** /campaigns/batches/{id} | Update a batch
*CallFireApiDocumentation.ContactsApi* | [**addContactListItems**](docs/ContactsApi.md#addContactListItems) | **POST** /contacts/lists/{id}/items | Add contacts to a contact list
*CallFireApiDocumentation.ContactsApi* | [**addDoNotContacts**](docs/ContactsApi.md#addDoNotContacts) | **POST** /contacts/dncs | Add do not contact (dnc) numbers
*CallFireApiDocumentation.ContactsApi* | [**createContactList**](docs/ContactsApi.md#createContactList) | **POST** /contacts/lists | Create contact lists
*CallFireApiDocumentation.ContactsApi* | [**createContactListFromFile**](docs/ContactsApi.md#createContactListFromFile) | **POST** /contacts/lists/upload | Create contact list from file
*CallFireApiDocumentation.ContactsApi* | [**createContacts**](docs/ContactsApi.md#createContacts) | **POST** /contacts | Create contacts
*CallFireApiDocumentation.ContactsApi* | [**deleteContact**](docs/ContactsApi.md#deleteContact) | **DELETE** /contacts/{id} | Delete a contact
*CallFireApiDocumentation.ContactsApi* | [**deleteContactList**](docs/ContactsApi.md#deleteContactList) | **DELETE** /contacts/lists/{id} | Delete a contact list
*CallFireApiDocumentation.ContactsApi* | [**deleteDoNotContact**](docs/ContactsApi.md#deleteDoNotContact) | **DELETE** /contacts/dncs/{number} | Delete do not contact (dnc) number. If number contains commas treat as list of numbers
*CallFireApiDocumentation.ContactsApi* | [**deleteDoNotContactsBySource**](docs/ContactsApi.md#deleteDoNotContactsBySource) | **DELETE** /contacts/dncs/sources/{source} | Delete do not contact (dnc) numbers contained in source.
*CallFireApiDocumentation.ContactsApi* | [**findContactLists**](docs/ContactsApi.md#findContactLists) | **GET** /contacts/lists | Find contact lists
*CallFireApiDocumentation.ContactsApi* | [**findContacts**](docs/ContactsApi.md#findContacts) | **GET** /contacts | Find contacts
*CallFireApiDocumentation.ContactsApi* | [**findDoNotContacts**](docs/ContactsApi.md#findDoNotContacts) | **GET** /contacts/dncs | Find do not contact (dnc) items
*CallFireApiDocumentation.ContactsApi* | [**getContact**](docs/ContactsApi.md#getContact) | **GET** /contacts/{id} | Find a specific contact
*CallFireApiDocumentation.ContactsApi* | [**getContactHistory**](docs/ContactsApi.md#getContactHistory) | **GET** /contacts/{id}/history | Find a contact&#39;s history
*CallFireApiDocumentation.ContactsApi* | [**getContactList**](docs/ContactsApi.md#getContactList) | **GET** /contacts/lists/{id} | Find a specific contact list
*CallFireApiDocumentation.ContactsApi* | [**getContactListItems**](docs/ContactsApi.md#getContactListItems) | **GET** /contacts/lists/{id}/items | Find contacts in a contact list
*CallFireApiDocumentation.ContactsApi* | [**getDoNotContact**](docs/ContactsApi.md#getDoNotContact) | **GET** /contacts/dncs/{number} | Get do not contact (dnc)
*CallFireApiDocumentation.ContactsApi* | [**getUniversalDoNotContacts**](docs/ContactsApi.md#getUniversalDoNotContacts) | **GET** /contacts/dncs/universals/{toNumber} | Find universal do not contacts (udnc) associated with toNumber
*CallFireApiDocumentation.ContactsApi* | [**removeContactListItem**](docs/ContactsApi.md#removeContactListItem) | **DELETE** /contacts/lists/{id}/items/{contactId} | Delete a contact from a contact list
*CallFireApiDocumentation.ContactsApi* | [**removeContactListItems**](docs/ContactsApi.md#removeContactListItems) | **DELETE** /contacts/lists/{id}/items | Delete contacts from a contact list
*CallFireApiDocumentation.ContactsApi* | [**updateContact**](docs/ContactsApi.md#updateContact) | **PUT** /contacts/{id} | Update a contact
*CallFireApiDocumentation.ContactsApi* | [**updateContactList**](docs/ContactsApi.md#updateContactList) | **PUT** /contacts/lists/{id} | Update a contact list
*CallFireApiDocumentation.ContactsApi* | [**updateDoNotContact**](docs/ContactsApi.md#updateDoNotContact) | **PUT** /contacts/dncs/{number} | Update an individual do not contact (dnc) number
*CallFireApiDocumentation.KeywordsApi* | [**findKeywordLeaseConfigs**](docs/KeywordsApi.md#findKeywordLeaseConfigs) | **GET** /keywords/leases/configs | Find keyword lease configs
*CallFireApiDocumentation.KeywordsApi* | [**findKeywordLeases**](docs/KeywordsApi.md#findKeywordLeases) | **GET** /keywords/leases | Find keyword leases
*CallFireApiDocumentation.KeywordsApi* | [**findKeywords**](docs/KeywordsApi.md#findKeywords) | **GET** /keywords | Find keywords
*CallFireApiDocumentation.KeywordsApi* | [**getKeywordLease**](docs/KeywordsApi.md#getKeywordLease) | **GET** /keywords/leases/{keyword} | Find a specific lease
*CallFireApiDocumentation.KeywordsApi* | [**getKeywordLeaseById**](docs/KeywordsApi.md#getKeywordLeaseById) | **GET** /keywords/leases/id/{id} | Find a keyword by id
*CallFireApiDocumentation.KeywordsApi* | [**getKeywordLeaseConfig**](docs/KeywordsApi.md#getKeywordLeaseConfig) | **GET** /keywords/leases/configs/{keyword} | Find a specific keyword lease config
*CallFireApiDocumentation.KeywordsApi* | [**isKeywordAvailable**](docs/KeywordsApi.md#isKeywordAvailable) | **GET** /keywords/{keyword}/available | Check for a specific keyword
*CallFireApiDocumentation.KeywordsApi* | [**updateKeywordLease**](docs/KeywordsApi.md#updateKeywordLease) | **PUT** /keywords/leases/{keyword} | Update a lease
*CallFireApiDocumentation.KeywordsApi* | [**updateKeywordLeaseConfig**](docs/KeywordsApi.md#updateKeywordLeaseConfig) | **PUT** /keywords/leases/configs/{keyword} | Update a keyword lease config
*CallFireApiDocumentation.MeApi* | [**createApiCredential**](docs/MeApi.md#createApiCredential) | **POST** /me/api/credentials | Create api credentials
*CallFireApiDocumentation.MeApi* | [**deleteApiCredential**](docs/MeApi.md#deleteApiCredential) | **DELETE** /me/api/credentials/{id} | Delete api credentials
*CallFireApiDocumentation.MeApi* | [**disableApiCredentials**](docs/MeApi.md#disableApiCredentials) | **POST** /me/api/credentials/{id}/disable | Disable specified API credentials
*CallFireApiDocumentation.MeApi* | [**enableApiCredentials**](docs/MeApi.md#enableApiCredentials) | **POST** /me/api/credentials/{id}/enable | Enable specified API credentials
*CallFireApiDocumentation.MeApi* | [**findApiCredentials**](docs/MeApi.md#findApiCredentials) | **GET** /me/api/credentials | Find api credentials
*CallFireApiDocumentation.MeApi* | [**getAccount**](docs/MeApi.md#getAccount) | **GET** /me/account | Find account details
*CallFireApiDocumentation.MeApi* | [**getApiCredential**](docs/MeApi.md#getApiCredential) | **GET** /me/api/credentials/{id} | Find a specific api credential
*CallFireApiDocumentation.MeApi* | [**getBillingPlanUsage**](docs/MeApi.md#getBillingPlanUsage) | **GET** /me/billing/plan-usage | Find plan usage
*CallFireApiDocumentation.MeApi* | [**getCallerIds**](docs/MeApi.md#getCallerIds) | **GET** /me/callerids | Find caller ids
*CallFireApiDocumentation.MeApi* | [**getCreditUsage**](docs/MeApi.md#getCreditUsage) | **GET** /me/billing/credit-usage | Find credit usage
*CallFireApiDocumentation.MeApi* | [**sendVerificationCodeToCallerId**](docs/MeApi.md#sendVerificationCodeToCallerId) | **POST** /me/callerids/{callerid} | Create a caller id
*CallFireApiDocumentation.MeApi* | [**verifyCallerId**](docs/MeApi.md#verifyCallerId) | **POST** /me/callerids/{callerid}/verification-code | Verify a caller id
*CallFireApiDocumentation.MediaApi* | [**createMedia**](docs/MediaApi.md#createMedia) | **POST** /media | Create media
*CallFireApiDocumentation.MediaApi* | [**findMedia**](docs/MediaApi.md#findMedia) | **GET** /media | Find media
*CallFireApiDocumentation.MediaApi* | [**getMedia**](docs/MediaApi.md#getMedia) | **GET** /media/{id} | Get a specific media
*CallFireApiDocumentation.MediaApi* | [**getMediaData**](docs/MediaApi.md#getMediaData) | **GET** /media/{id}.{extension} | Download media by extension
*CallFireApiDocumentation.MediaApi* | [**getMediaDataBinary**](docs/MediaApi.md#getMediaDataBinary) | **GET** /media/{id}/file | Download a MP3 media
*CallFireApiDocumentation.MediaApi* | [**getMediaDataByKey**](docs/MediaApi.md#getMediaDataByKey) | **GET** /media/public/{key}.{extension} | Download media by extension
*CallFireApiDocumentation.NumbersApi* | [**findNumberLeaseConfigs**](docs/NumbersApi.md#findNumberLeaseConfigs) | **GET** /numbers/leases/configs | Find lease configs
*CallFireApiDocumentation.NumbersApi* | [**findNumberLeases**](docs/NumbersApi.md#findNumberLeases) | **GET** /numbers/leases | Find leases
*CallFireApiDocumentation.NumbersApi* | [**findNumberRegions**](docs/NumbersApi.md#findNumberRegions) | **GET** /numbers/regions | Find number regions
*CallFireApiDocumentation.NumbersApi* | [**findNumbersLocal**](docs/NumbersApi.md#findNumbersLocal) | **GET** /numbers/local | Find local numbers
*CallFireApiDocumentation.NumbersApi* | [**findNumbersTollfree**](docs/NumbersApi.md#findNumbersTollfree) | **GET** /numbers/tollfree | Find tollfree numbers
*CallFireApiDocumentation.NumbersApi* | [**getNumberLease**](docs/NumbersApi.md#getNumberLease) | **GET** /numbers/leases/{number} | Find a specific lease
*CallFireApiDocumentation.NumbersApi* | [**getNumberLeaseConfig**](docs/NumbersApi.md#getNumberLeaseConfig) | **GET** /numbers/leases/configs/{number} | Find a specific lease config
*CallFireApiDocumentation.NumbersApi* | [**updateNumberLease**](docs/NumbersApi.md#updateNumberLease) | **PUT** /numbers/leases/{number} | Update a lease
*CallFireApiDocumentation.NumbersApi* | [**updateNumberLeaseConfig**](docs/NumbersApi.md#updateNumberLeaseConfig) | **PUT** /numbers/leases/configs/{number} | Update a lease config
*CallFireApiDocumentation.OrdersApi* | [**findOrders**](docs/OrdersApi.md#findOrders) | **GET** /orders | Find orders
*CallFireApiDocumentation.OrdersApi* | [**getOrder**](docs/OrdersApi.md#getOrder) | **GET** /orders/{id} | Find a specific order
*CallFireApiDocumentation.OrdersApi* | [**orderKeywords**](docs/OrdersApi.md#orderKeywords) | **POST** /orders/keywords | Purchase keywords
*CallFireApiDocumentation.OrdersApi* | [**orderNumbers**](docs/OrdersApi.md#orderNumbers) | **POST** /orders/numbers | Purchase numbers
*CallFireApiDocumentation.ReportsApi* | [**getDeliveryReports**](docs/ReportsApi.md#getDeliveryReports) | **GET** /reports/delivery | Get delivery reports by ad hoc criteria
*CallFireApiDocumentation.TextsApi* | [**addTextBroadcastBatch**](docs/TextsApi.md#addTextBroadcastBatch) | **POST** /texts/broadcasts/{id}/batches | Add batches to a text broadcast
*CallFireApiDocumentation.TextsApi* | [**addTextBroadcastRecipients**](docs/TextsApi.md#addTextBroadcastRecipients) | **POST** /texts/broadcasts/{id}/recipients | Add recipients to a text broadcast
*CallFireApiDocumentation.TextsApi* | [**archiveTextBroadcast**](docs/TextsApi.md#archiveTextBroadcast) | **POST** /texts/broadcasts/{id}/archive | Archive text broadcast
*CallFireApiDocumentation.TextsApi* | [**createTextAutoReply**](docs/TextsApi.md#createTextAutoReply) | **POST** /texts/auto-replys | Create an auto reply
*CallFireApiDocumentation.TextsApi* | [**createTextBroadcast**](docs/TextsApi.md#createTextBroadcast) | **POST** /texts/broadcasts | Create a text broadcast
*CallFireApiDocumentation.TextsApi* | [**deleteTextAutoReply**](docs/TextsApi.md#deleteTextAutoReply) | **DELETE** /texts/auto-replys/{id} | Delete an auto reply
*CallFireApiDocumentation.TextsApi* | [**findTextAutoReplys**](docs/TextsApi.md#findTextAutoReplys) | **GET** /texts/auto-replys | Find auto replies
*CallFireApiDocumentation.TextsApi* | [**findTextBroadcasts**](docs/TextsApi.md#findTextBroadcasts) | **GET** /texts/broadcasts | Find text broadcasts
*CallFireApiDocumentation.TextsApi* | [**findTexts**](docs/TextsApi.md#findTexts) | **GET** /texts | Find texts
*CallFireApiDocumentation.TextsApi* | [**getText**](docs/TextsApi.md#getText) | **GET** /texts/{id} | Find a specific text
*CallFireApiDocumentation.TextsApi* | [**getTextAutoReply**](docs/TextsApi.md#getTextAutoReply) | **GET** /texts/auto-replys/{id} | Find a specific auto reply
*CallFireApiDocumentation.TextsApi* | [**getTextBroadcast**](docs/TextsApi.md#getTextBroadcast) | **GET** /texts/broadcasts/{id} | Find a specific text broadcast
*CallFireApiDocumentation.TextsApi* | [**getTextBroadcastBatches**](docs/TextsApi.md#getTextBroadcastBatches) | **GET** /texts/broadcasts/{id}/batches | Find batches in a text broadcast
*CallFireApiDocumentation.TextsApi* | [**getTextBroadcastStats**](docs/TextsApi.md#getTextBroadcastStats) | **GET** /texts/broadcasts/{id}/stats | Get statistics on text broadcast
*CallFireApiDocumentation.TextsApi* | [**getTextBroadcastTexts**](docs/TextsApi.md#getTextBroadcastTexts) | **GET** /texts/broadcasts/{id}/texts | Find texts in a text broadcast
*CallFireApiDocumentation.TextsApi* | [**sendTexts**](docs/TextsApi.md#sendTexts) | **POST** /texts | Send texts
*CallFireApiDocumentation.TextsApi* | [**startTextBroadcast**](docs/TextsApi.md#startTextBroadcast) | **POST** /texts/broadcasts/{id}/start | Start text broadcast
*CallFireApiDocumentation.TextsApi* | [**stopTextBroadcast**](docs/TextsApi.md#stopTextBroadcast) | **POST** /texts/broadcasts/{id}/stop | Stop text broadcast
*CallFireApiDocumentation.TextsApi* | [**toggleTextBroadcastRecipientsStatus**](docs/TextsApi.md#toggleTextBroadcastRecipientsStatus) | **POST** /texts/broadcasts/{id}/toggleRecipientsStatus | Disable/enable undialed recipients in broadcast
*CallFireApiDocumentation.TextsApi* | [**updateTextBroadcast**](docs/TextsApi.md#updateTextBroadcast) | **PUT** /texts/broadcasts/{id} | Update a text broadcast
*CallFireApiDocumentation.WebhooksApi* | [**createWebhook**](docs/WebhooksApi.md#createWebhook) | **POST** /webhooks | Create a webhook
*CallFireApiDocumentation.WebhooksApi* | [**deleteWebhook**](docs/WebhooksApi.md#deleteWebhook) | **DELETE** /webhooks/{id} | Delete a webhook
*CallFireApiDocumentation.WebhooksApi* | [**findWebhookResources**](docs/WebhooksApi.md#findWebhookResources) | **GET** /webhooks/resources | Find webhook resources
*CallFireApiDocumentation.WebhooksApi* | [**findWebhooks**](docs/WebhooksApi.md#findWebhooks) | **GET** /webhooks | Find webhooks
*CallFireApiDocumentation.WebhooksApi* | [**getWebhook**](docs/WebhooksApi.md#getWebhook) | **GET** /webhooks/{id} | Find a specific webhook
*CallFireApiDocumentation.WebhooksApi* | [**getWebhookResource**](docs/WebhooksApi.md#getWebhookResource) | **GET** /webhooks/resources/{resource} | Find specific webhook resource
*CallFireApiDocumentation.WebhooksApi* | [**updateWebhook**](docs/WebhooksApi.md#updateWebhook) | **PUT** /webhooks/{id} | Update a webhook


## Documentation for Models

 - [CallFireApiDocumentation.A2pUpgradeLeaseDto](docs/A2pUpgradeLeaseDto.md)
 - [CallFireApiDocumentation.A2pUpgradeLeasePage](docs/A2pUpgradeLeasePage.md)
 - [CallFireApiDocumentation.Account](docs/Account.md)
 - [CallFireApiDocumentation.AddContactListContactsRequest](docs/AddContactListContactsRequest.md)
 - [CallFireApiDocumentation.AddDoNotContactRequest](docs/AddDoNotContactRequest.md)
 - [CallFireApiDocumentation.ApiCredential](docs/ApiCredential.md)
 - [CallFireApiDocumentation.ApiCredentialPage](docs/ApiCredentialPage.md)
 - [CallFireApiDocumentation.ApiValidator](docs/ApiValidator.md)
 - [CallFireApiDocumentation.AuthController](docs/AuthController.md)
 - [CallFireApiDocumentation.AuthToken](docs/AuthToken.md)
 - [CallFireApiDocumentation.Batch](docs/Batch.md)
 - [CallFireApiDocumentation.BatchPage](docs/BatchPage.md)
 - [CallFireApiDocumentation.BatchRequest](docs/BatchRequest.md)
 - [CallFireApiDocumentation.BillingPlanUsage](docs/BillingPlanUsage.md)
 - [CallFireApiDocumentation.Call](docs/Call.md)
 - [CallFireApiDocumentation.CallBroadcast](docs/CallBroadcast.md)
 - [CallFireApiDocumentation.CallBroadcastPage](docs/CallBroadcastPage.md)
 - [CallFireApiDocumentation.CallBroadcastSounds](docs/CallBroadcastSounds.md)
 - [CallFireApiDocumentation.CallBroadcastStats](docs/CallBroadcastStats.md)
 - [CallFireApiDocumentation.CallCreateSound](docs/CallCreateSound.md)
 - [CallFireApiDocumentation.CallList](docs/CallList.md)
 - [CallFireApiDocumentation.CallPage](docs/CallPage.md)
 - [CallFireApiDocumentation.CallRecipient](docs/CallRecipient.md)
 - [CallFireApiDocumentation.CallRecord](docs/CallRecord.md)
 - [CallFireApiDocumentation.CallRecording](docs/CallRecording.md)
 - [CallFireApiDocumentation.CallRecordingList](docs/CallRecordingList.md)
 - [CallFireApiDocumentation.CallTrackingConfig](docs/CallTrackingConfig.md)
 - [CallFireApiDocumentation.CallerId](docs/CallerId.md)
 - [CallFireApiDocumentation.CallerIdList](docs/CallerIdList.md)
 - [CallFireApiDocumentation.CallerIdVerificationRequest](docs/CallerIdVerificationRequest.md)
 - [CallFireApiDocumentation.CampaignSound](docs/CampaignSound.md)
 - [CallFireApiDocumentation.CampaignSoundPage](docs/CampaignSoundPage.md)
 - [CallFireApiDocumentation.Contact](docs/Contact.md)
 - [CallFireApiDocumentation.ContactHistory](docs/ContactHistory.md)
 - [CallFireApiDocumentation.ContactList](docs/ContactList.md)
 - [CallFireApiDocumentation.ContactListPage](docs/ContactListPage.md)
 - [CallFireApiDocumentation.ContactPage](docs/ContactPage.md)
 - [CallFireApiDocumentation.CreateContactListRequest](docs/CreateContactListRequest.md)
 - [CallFireApiDocumentation.CreditUsage](docs/CreditUsage.md)
 - [CallFireApiDocumentation.DateTimeZone](docs/DateTimeZone.md)
 - [CallFireApiDocumentation.DeliveryReport](docs/DeliveryReport.md)
 - [CallFireApiDocumentation.DncListDto](docs/DncListDto.md)
 - [CallFireApiDocumentation.DoNotContact](docs/DoNotContact.md)
 - [CallFireApiDocumentation.DoNotContactPage](docs/DoNotContactPage.md)
 - [CallFireApiDocumentation.Duration](docs/Duration.md)
 - [CallFireApiDocumentation.ErrorResponse](docs/ErrorResponse.md)
 - [CallFireApiDocumentation.GoogleAnalytics](docs/GoogleAnalytics.md)
 - [CallFireApiDocumentation.ItemList](docs/ItemList.md)
 - [CallFireApiDocumentation.ItemListUniversalDoNotContact](docs/ItemListUniversalDoNotContact.md)
 - [CallFireApiDocumentation.ItemListWebhookResource](docs/ItemListWebhookResource.md)
 - [CallFireApiDocumentation.IvrInboundConfig](docs/IvrInboundConfig.md)
 - [CallFireApiDocumentation.Keyword](docs/Keyword.md)
 - [CallFireApiDocumentation.KeywordConfig](docs/KeywordConfig.md)
 - [CallFireApiDocumentation.KeywordLease](docs/KeywordLease.md)
 - [CallFireApiDocumentation.KeywordLeasePage](docs/KeywordLeasePage.md)
 - [CallFireApiDocumentation.KeywordList](docs/KeywordList.md)
 - [CallFireApiDocumentation.KeywordPurchaseRequest](docs/KeywordPurchaseRequest.md)
 - [CallFireApiDocumentation.LocalDate](docs/LocalDate.md)
 - [CallFireApiDocumentation.LocalTime](docs/LocalTime.md)
 - [CallFireApiDocumentation.LocalTimeRestriction](docs/LocalTimeRestriction.md)
 - [CallFireApiDocumentation.LocalTimeZoneRestriction](docs/LocalTimeZoneRestriction.md)
 - [CallFireApiDocumentation.Locale](docs/Locale.md)
 - [CallFireApiDocumentation.ManagedAccountDto](docs/ManagedAccountDto.md)
 - [CallFireApiDocumentation.ManagedAccountsPage](docs/ManagedAccountsPage.md)
 - [CallFireApiDocumentation.Media](docs/Media.md)
 - [CallFireApiDocumentation.MediaPage](docs/MediaPage.md)
 - [CallFireApiDocumentation.MessageTemplateCategory](docs/MessageTemplateCategory.md)
 - [CallFireApiDocumentation.MessageTemplateCategoryPage](docs/MessageTemplateCategoryPage.md)
 - [CallFireApiDocumentation.ModelNumber](docs/ModelNumber.md)
 - [CallFireApiDocumentation.Note](docs/Note.md)
 - [CallFireApiDocumentation.NumberConfig](docs/NumberConfig.md)
 - [CallFireApiDocumentation.NumberConfigPage](docs/NumberConfigPage.md)
 - [CallFireApiDocumentation.NumberLease](docs/NumberLease.md)
 - [CallFireApiDocumentation.NumberLeasePage](docs/NumberLeasePage.md)
 - [CallFireApiDocumentation.NumberList](docs/NumberList.md)
 - [CallFireApiDocumentation.NumberOrder](docs/NumberOrder.md)
 - [CallFireApiDocumentation.NumberOrderItem](docs/NumberOrderItem.md)
 - [CallFireApiDocumentation.NumberPurchaseRequest](docs/NumberPurchaseRequest.md)
 - [CallFireApiDocumentation.OAuthSession](docs/OAuthSession.md)
 - [CallFireApiDocumentation.Page](docs/Page.md)
 - [CallFireApiDocumentation.PageDeliveryReport](docs/PageDeliveryReport.md)
 - [CallFireApiDocumentation.PageKeywordLease](docs/PageKeywordLease.md)
 - [CallFireApiDocumentation.PageNumberOrder](docs/PageNumberOrder.md)
 - [CallFireApiDocumentation.PageText](docs/PageText.md)
 - [CallFireApiDocumentation.PageWebhook](docs/PageWebhook.md)
 - [CallFireApiDocumentation.QuestionResponse](docs/QuestionResponse.md)
 - [CallFireApiDocumentation.Recipient](docs/Recipient.md)
 - [CallFireApiDocumentation.Region](docs/Region.md)
 - [CallFireApiDocumentation.RegionPage](docs/RegionPage.md)
 - [CallFireApiDocumentation.ResourceId](docs/ResourceId.md)
 - [CallFireApiDocumentation.ResourceIdList](docs/ResourceIdList.md)
 - [CallFireApiDocumentation.RetryConfig](docs/RetryConfig.md)
 - [CallFireApiDocumentation.Schedule](docs/Schedule.md)
 - [CallFireApiDocumentation.StringList](docs/StringList.md)
 - [CallFireApiDocumentation.TemporalUnit](docs/TemporalUnit.md)
 - [CallFireApiDocumentation.Text](docs/Text.md)
 - [CallFireApiDocumentation.TextAutoReply](docs/TextAutoReply.md)
 - [CallFireApiDocumentation.TextAutoReplyPage](docs/TextAutoReplyPage.md)
 - [CallFireApiDocumentation.TextBroadcast](docs/TextBroadcast.md)
 - [CallFireApiDocumentation.TextBroadcastCreateResponse](docs/TextBroadcastCreateResponse.md)
 - [CallFireApiDocumentation.TextBroadcastPage](docs/TextBroadcastPage.md)
 - [CallFireApiDocumentation.TextBroadcastStatsDto](docs/TextBroadcastStatsDto.md)
 - [CallFireApiDocumentation.TextInboundConfig](docs/TextInboundConfig.md)
 - [CallFireApiDocumentation.TextList](docs/TextList.md)
 - [CallFireApiDocumentation.TextPage](docs/TextPage.md)
 - [CallFireApiDocumentation.TextRecipient](docs/TextRecipient.md)
 - [CallFireApiDocumentation.TextRecord](docs/TextRecord.md)
 - [CallFireApiDocumentation.TextToSpeech](docs/TextToSpeech.md)
 - [CallFireApiDocumentation.TimeZone](docs/TimeZone.md)
 - [CallFireApiDocumentation.UniversalDoNotContact](docs/UniversalDoNotContact.md)
 - [CallFireApiDocumentation.UpdateContactListRequest](docs/UpdateContactListRequest.md)
 - [CallFireApiDocumentation.User](docs/User.md)
 - [CallFireApiDocumentation.Webhook](docs/Webhook.md)
 - [CallFireApiDocumentation.WebhookPage](docs/WebhookPage.md)
 - [CallFireApiDocumentation.WebhookResource](docs/WebhookResource.md)
 - [CallFireApiDocumentation.WeeklySchedule](docs/WeeklySchedule.md)
 - [CallFireApiDocumentation.ZoneId](docs/ZoneId.md)
 - [CallFireApiDocumentation.ZoneOffset](docs/ZoneOffset.md)
 - [CallFireApiDocumentation.ZoneOffsetTransition](docs/ZoneOffsetTransition.md)
 - [CallFireApiDocumentation.ZoneOffsetTransitionRule](docs/ZoneOffsetTransitionRule.md)
 - [CallFireApiDocumentation.ZoneRules](docs/ZoneRules.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### basicAuth

- **Type**: HTTP basic authentication

