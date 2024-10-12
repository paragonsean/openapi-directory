/**
 * Developer documentation
 * # Welcome  Implementing a new tool can be daunting, but it doesn't have to. You can implement journy.io in a few different ways to ensure it fits with the rest of your tech stack seamlessly.  We welcome your feedback, ideas and suggestions. We really want to make your life easier, so if we’re falling short or should be doing something different, we want to hear about it. Send us an email at [hi@journy.io](mailto:hi@journy.io) or reach out via the chat on our website or on our platform.  There are multiple ways you can send us data about users and accounts. We have both frontend and backend APIs, which can be used together at the same time.  If you already use [Segment](https://segment.com/), you can [get up and running with journy.io in seconds](https://help.journy.io/en/articles/6488307-the-segment-connector).  # Concepts  ## Users  The most basic entity is a user, a specific individual that completed an interaction with your product.  We support multiple types of users, often differentiated by it's external ID prefix. E.g. In the case you are building an ordering app, there could easily be an administrator (who updates products and checks for orders) and the end-customers who place orders. One could have a typical ADM-XXXXXXXX ID, while the other would be referenced by USR-XXXXXXXXX.  ## Accounts  In B2B SaaS, users can be part of multiple accounts. E.g. Imagine you're building a content scheduling app where an agency can manage the social media posts of their clients. Each client of the agency has its own account in the product.  If your app doesn't have the concept of a team or group of users, you can ignore accounts.  ## Events  An event is a data point that represents an interaction between a user and/or an account; and your product. Events can represents any range of interactions. E.g. Every time a customer creates an invoice in an invoicing app. Actions like creating an invoice can be tracked as an event in journy.io.  It's critical to track events properly. You'll need to provide either an account ID, or a user ID, or both; when tracking an event. E.g. If a user updates his personal settings, you can omit the account ID as the event would not be related to any account. In a same logic, an account could get a 'suspend account' event (with account ID) from an internal process, whereas no user would be associated. In most cases, events will be associated to both 1 user and 1 account.  You can optionally pass extra details as metadata (e.g. amount of the invoice). This gets particarly powerfull when creating computed properties on those event metadata. E.g. Our above ordering app could send journy.io 'Place Order' events with metadata 'price', on which journy.io very easily would compute a total order value (for each account) for the last 30 days.  💡 Metadata does not update the properties of a user or account.  # Frontend vs backend  The best implementations we see employ a hybrid approach to maximize data quality while maintaining the flexibility to easily collect the data they need.  We recommend using our JavaScript snippet to track screen views and our backend API to sync users, sync accounts and track events.  When evaluating how to track a particular event, we suggest starting with server-side and only use frontend if it's not possible to collect purely server-side. This can be the case if you need to track interactions with your product that don't result in any natural server requests (such as a button click that opens a modal).  # Frontend  ## Setup  💡 You can find the JavaScript snippet in the website settings in the connections view.  Copy the JavaScript snippet and place it in the head or body of your application.  The snippet automatically calls `journy(\"init\", { ... })` and `journy(\"pageview\")`.  ## Identify user  💡 A user ID should be a robust, static, unique identifier that you recognize a user by in your own systems. Because these IDs are consistent across a customer’s lifetime, you should include a user ID in identify calls as often as you can. Ideally, the user ID should be a database ID.  💡 journy.io does not recommend using simple email addresses or usernames as user ID, as these can change over time. journy.io recommends that you use static IDs instead, so the IDs never change. When you use a static ID, you can still recognize the user in your analytics tools, even if the user changes their email address.  💡 The properties `full_name`, `first_name`, `last_name`, `phone` and `registered_at` will be used for creating contacts in destinations like Intercom, HubSpot, Salesforce, ...  `journy(\"identify\")` allows you to identify the user that is currently using your product.  ```ts journy(\"identify\", {   // Email or user ID is required   email: \"john.doe@acme.com\",   // Unique identifier for the user in your database   userId: \"20\",    // Optional   // Hash of the user ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\",    // Optional   properties: {     full_name: \"John Doe\",     // or     first_name: \"John\",     last_name: \"Doe\",      phone: \"123\",     registered_at: new Date(/_* ... *_/),     is_admin: true,     key_with_empty_value: \"\",     this_property_will_be_deleted: null,   }, }); ```  ## Identify account  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  💡 The properties `name`, `mrr`, `plan` and `registered_at` will be used to create companies in destinations like Intercom, HubSpot, Salesforce, ...  `journy(\"account\")` allows you to identify the business account (i.e. organization) using your product.  ```ts journy(\"account\", {   // Required   // Unique identifier for the account in your database   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\",    // Optional   properties: {     name: \"ACME, Inc\",     mrr: 399,     plan: \"Pro\",     registered_at: new Date(/_* ... *_/),     is_paying: true,     key_with_empty_value: \"\",     this_property_will_be_deleted: null,   }, }); ```  ## Send page view  💡 In applications, we advise you to use screen views instead of page views.  The JavaScript snippet in the site settings includes a `pageview` by default.  ```ts journy(\"pageview\"); ```  If you have a B2B application, we recommend to set account ID for every page view that happens within the context of an account.  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  ```ts journy(\"pageview\", {   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\", }); ```  ## Send screen view  In applications, we strongly advise you to use screen views instead of page views.  Page URLs in applications often include the account ID (e.g. https://app.acme.com/accountId/settings).  This makes it difficult to create signals, segments, ... based on those URLs.  That's what screen views solve. It allows you to set a name for the screen being viewed (e.g. Account settings).  ```ts journy(\"screen\", { name: \"Personal settings\" }); ```  If you have a B2B application, we recommend to set account ID for every screen view that happens within the context of an account.  Example: \"Personal settings\" would be without account ID, \"Team settings\" would be with account ID.  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  ```ts journy(\"screen\", {   name: \"Account settings\",   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\", }); ```  ## Trigger an event  💡 Use past tense for event names.  User events:  ```js journy(\"event\", {   // required   name: \"signed_in\",    // optional   metadata: {     key: \"value\",   }, }); ```  Account events:  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  ```js journy(\"event\", {   // required   name: \"created_invoice\",   accountId: \"30\",    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \"hash\",    // optional   metadata: {     key: \"value\",     amount: 100,     allow_wire_transfer: true,   }, }); ```  ## Identity verification  Identity verification ensures that one person can't impersonate another.  Identity verification requires you to add an hash (HMAC) (that you generate on your server using SHA256) to your installation snippet alongside your user ID and account ID.  journy.io won't accept requests for a logged-in user without a valid hash. The hash is calculated using a secret key, which you should never share. Without this secret key, no third party can send journy.io a valid hash for one of your users, so they can't impersonate your users.  This is optional but highly recommended.  You can enable identify verification in the website settings in the connections view.  ```js journy(\"identify\", {   userId: \"userId\",   verification: \"USER_ID_HMAC_VALUE_HERE\" })  journy(\"account\", {   accountId: \"accountId\",   verification: \"ACCOUNT_ID_HMAC_VALUE_HERE\" })  journy(\"event\", {   accountId: \"accountId\",   verification: \"ACCOUNT_ID_HMAC_VALUE_HERE\" }) ```  ### PHP  ```php <?php  hash_hmac(   'sha256', // hash function   id, // user or account ID   'secret' // secret key (keep safe!) ); ```  ### Node.js  ```js import { createHmac } from \"crypto\"  createHmac(   \"sha256\", // hash function   'secret' // secret key (keep safe!) ).update(id).digest(\"hex\") // user or account ID ```  ### Ruby  ```ruby OpenSSL::HMAC.hexdigest(   'sha256', # hash function   'secret', # secret key (keep safe!)   id.to_s # user or account ID ) ```  ### Python  ``` import hmac import hashlib  hmac.new(   b'secret', # secret key (keep safe!)   bytes(id, encoding='utf-8'), # user or account ID   digestmod=hashlib.sha256 # hash function ).hexdigest() ```  ## Single page application  You can use our JavaScript snippet inside single page applications.  You should call `journy(\"screen\")` (or `journy(\"pageview\")`) whenever a user in your application transitions to another page. You can do this by listening to router change events. The current page URL will always be resolved using `window.location.href`.  You can trigger events using `journy(\"event\")` whenever you need to.  ### Next.js  We built a demo app with Next.js. You can find the code [here](https://github.com/journy-io/js-sdk-demo-app).  This [component](https://github.com/journy-io/js-sdk-demo-app/blob/main/components/Journy.js) should be a great start.  You can use the `Script` component from Next.js to load the web snippet and call `init`.  Don't forget to listen on route changes. You can use the `useRouter` hook for that.  ### React Router v6  You can use the [`useLocation`](https://reactrouter.com/docs/en/v6/api#uselocation) hook to listen for route changes:  ```js import React, { useEffect } from \"react\"; import { useLocation } from 'react-router-dom';  function App() {   const location = useLocation();    useEffect(() => {     journy(\"screen\", { name: \"name\" });     // or     journy(\"pageview\");   }, [location]);    return (       // ...   ); } ```  ### Vue Router  You can use [`router.afterEach`](https://router.vuejs.org/guide/advanced/navigation-guards.html#global-after-hooks) to listen for route changes:  ```js const router = new VueRouter({ ... });  router.afterEach((to, from) => {   journy(\"screen\", { name: \"name\" });   // or   journy(\"pageview\"); }); ```  Note: We don't accept a page URL argument for `journy(\"pageview\")`. The current page URL will always be resolved using `window.location.href`.  ## TypeScript  We published an [npm package](https://www.npmjs.com/package/@journyio/web-types) with type definitions to enable type-safe usage of our JavaScript snippet. The code and documentation is available on [GitHub](https://github.com/journy-io/web-types).  ## Localhost  By default a site doesn't allow page views from other domains than the registered domain. This makes it difficult to test your tracking implementation locally.  You can enable \"Allow any domain\" in the site settings to disable the domain check.  This will allow you to test the JavaScript snippet with localhost as hostname.  # Backend  The journy.io API is organized around REST. Our API has predictable resource-oriented URLs, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  The API is hosted on api.journy.io.  ## Official SDKs  Our SDKs are designed to help you interact with our APIs with less friction. They are written in several different languages and help bridge the gap between your application and journy.io APIs. They take away the need to know the exact URL and HTTP method to use for each API call among other things leaving you more time to focus on making your application.  | Language   | Package                                                                        | Source code                                                                | |------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------| | 💚 Node.js | [npm install @journyio/sdk ](https://www.npmjs.com/package/@journyio/sdk)      | [github.com/journy-io/js-sdk](https://github.com/journy-io/js-sdk)         | | 🐘 PHP     | [composer require journy-io/sdk](https://packagist.org/packages/journy-io/sdk) | [github.com/journy-io/php-sdk](https://github.com/journy-io/php-sdk)       | | 🐍 Python  | [pip install journyio-sdk](https://pypi.org/project/journyio-sdk/)             | [github.com/journy-io/python-sdk](https://github.com/journy-io/python-sdk) | | 💎 Ruby    | Coming soon                                                                    | Coming soon                                                                |  Your favourite programming language not included? [Let us know!](mailto:hi@journy.io)  In the meanwhile, you can use [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) to generate a client for your programming language.  ## Authentication  The journy.io API uses API keys to authenticate requests. You can view and manage your API keys in the [connections screen](https://system.journy.io).  Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, and so forth.  All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.  For every request send to the API we expect a header `X-Api-Key` to be set with the API Key.  ## Permissions  When creating an API Key in [the application](https://system.journy.io) you will have the choice to give permissions to an API Key (which you can change later on). These permissions restrict the API Key from different actions. When an API Key tries to perform a certain action it doesn't have the permissions for, you will receive a `401: Unauthorized` response.  ## Rate limiting  To prevent abuse of the API there is a maximum throughput of 1800 requests per minute. If you need a higher throughput, please contact us.  To keep our platform healthy and stable, we'll block API keys that consistently hit our rate limits. Therefore, please consider taking this throughput into account.  In every response the headers `X-RateLimit-Limit` and `X-RateLimit-Remaining` will be set. The `X-RateLimit-Limit`-header will always contain the current limit of requests per minute. The `X-RateLimit-Remaining`-header will always contain the amount of requests you have left in the current sliding window.  💡 The client-side tracking uses different rate limits.  ## Errors  journy.io uses conventional HTTP response codes to indicate the success or failure of an API request. In general: Codes in the 2xx range indicate success. Codes in the 4xx range indicate an error that failed given the information provided (e.g. a required parameter was omitted). Codes in the 5xx range indicate an error with journy.io's servers (these are rare).  When performing a `POST`- or `PUT`-request with a requestBody, or when including parameters, these parameters and fields will automatically be checked and validated against the API Spec. When any error occurs, you will get a response with an `errors`-field, structured as follows:  ```json {   \"errors\": {     \"parameters\": {       \"header\": {         \"headerParameterName\": \"Describe what's wrong with the header parameter.\",         ...       },       \"query\": {         \"queryParameterName\": \"Describe what's wrong with the query parameter.\",         ...       },       \"path\": {         \"pathParameterName\": \"Describe what's wrong with the path parameter.\",         ...       },     },     \"fields\": {       \"fieldName\": \"Describe what's wrong with the fieldName.\",       \"object.fieldName\": \"Describe what's wrong with the fieldName of the included object.\",        ...     }   } } ```  ## Best practices  ### Track accounts & users immediately on creation  When you create an account in your database, immediately sending data about that account to journy.io helps your team stay in sync. The same goes for users. Call [Upsert account](#operation/upsertAccount) as soon as possible, right after the account is first created in your database.  ### Update account data daily  Not every account is active every day. But, you may have properties on the account that change through background processing. That's why we recommend updating every one of your accounts' data in a recurring daily process. This way, you know that your accounts are updated every day in journy.io.  ## Changelog  ### December 2021  [POST /events](#operation/trackJourneyEvent) will be moved to [POST /track](#operation/trackEvent). [POST /events](#operation/trackJourneyEvent) is deprecated and will be removed in the future.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: hi@journy.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import AddUserToAccountRequest from './model/AddUserToAccountRequest';
import AddUserToAccountRequestUsersInner from './model/AddUserToAccountRequestUsersInner';
import AddUserToAccountRequestUsersInnerIdentification from './model/AddUserToAccountRequestUsersInnerIdentification';
import DeleteAccount202Response from './model/DeleteAccount202Response';
import DeleteAccount202ResponseAllOfMeta from './model/DeleteAccount202ResponseAllOfMeta';
import DeleteAccount400Response from './model/DeleteAccount400Response';
import DeleteAccount400ResponseAllOfErrors from './model/DeleteAccount400ResponseAllOfErrors';
import DeleteAccount400ResponseAllOfErrorsParameters from './model/DeleteAccount400ResponseAllOfErrorsParameters';
import DeleteAccountRequest from './model/DeleteAccountRequest';
import DeleteAccountRequestIdentification from './model/DeleteAccountRequestIdentification';
import DeleteUserRequest from './model/DeleteUserRequest';
import GetAccountProperties200Response from './model/GetAccountProperties200Response';
import GetAccountProperties200ResponseAllOfDataInner from './model/GetAccountProperties200ResponseAllOfDataInner';
import GetAccountProperties200ResponseAllOfDataInnerGroup from './model/GetAccountProperties200ResponseAllOfDataInnerGroup';
import GetAccountSegments200Response from './model/GetAccountSegments200Response';
import GetAccountSegments200ResponseAllOfDataInner from './model/GetAccountSegments200ResponseAllOfDataInner';
import GetEvents200Response from './model/GetEvents200Response';
import GetEvents200ResponseAllOfDataInner from './model/GetEvents200ResponseAllOfDataInner';
import GetEvents200ResponseAllOfDataInnerGroup from './model/GetEvents200ResponseAllOfDataInnerGroup';
import GetTrackingSnippet200Response from './model/GetTrackingSnippet200Response';
import GetTrackingSnippet200ResponseAllOfData from './model/GetTrackingSnippet200ResponseAllOfData';
import GetValidity200Response from './model/GetValidity200Response';
import GetValidity200ResponseAllOfData from './model/GetValidity200ResponseAllOfData';
import LinkRequest from './model/LinkRequest';
import TrackEventRequest from './model/TrackEventRequest';
import TrackEventRequestMetadataValue from './model/TrackEventRequestMetadataValue';
import TrackJourneyEventRequest from './model/TrackJourneyEventRequest';
import TrackJourneyEventRequestIdentification from './model/TrackJourneyEventRequestIdentification';
import TrackJourneyEventRequestMetadataValue from './model/TrackJourneyEventRequestMetadataValue';
import UpsertAccount201Response from './model/UpsertAccount201Response';
import UpsertAccountRequest from './model/UpsertAccountRequest';
import UpsertAccountRequestPropertiesValue from './model/UpsertAccountRequestPropertiesValue';
import UpsertUser201Response from './model/UpsertUser201Response';
import UpsertUserRequest from './model/UpsertUserRequest';
import AccountsApi from './api/AccountsApi';
import EventsApi from './api/EventsApi';
import PropertiesApi from './api/PropertiesApi';
import SegmentsApi from './api/SegmentsApi';
import TrackApi from './api/TrackApi';
import UsersApi from './api/UsersApi';
import ValidationApi from './api/ValidationApi';
import WebsitesApi from './api/WebsitesApi';


/**
* # Welcome  Implementing a new tool can be daunting, but it doesn&#39;t have to. You can implement journy.io in a few different ways to ensure it fits with the rest of your tech stack seamlessly.  We welcome your feedback, ideas and suggestions. We really want to make your life easier, so if we’re falling short or should be doing something different, we want to hear about it. Send us an email at [hi@journy.io](mailto:hi@journy.io) or reach out via the chat on our website or on our platform.  There are multiple ways you can send us data about users and accounts. We have both frontend and backend APIs, which can be used together at the same time.  If you already use [Segment](https://segment.com/), you can [get up and running with journy.io in seconds](https://help.journy.io/en/articles/6488307-the-segment-connector).  # Concepts  ## Users  The most basic entity is a user, a specific individual that completed an interaction with your product.  We support multiple types of users, often differentiated by it&#39;s external ID prefix. E.g. In the case you are building an ordering app, there could easily be an administrator (who updates products and checks for orders) and the end-customers who place orders. One could have a typical ADM-XXXXXXXX ID, while the other would be referenced by USR-XXXXXXXXX.  ## Accounts  In B2B SaaS, users can be part of multiple accounts. E.g. Imagine you&#39;re building a content scheduling app where an agency can manage the social media posts of their clients. Each client of the agency has its own account in the product.  If your app doesn&#39;t have the concept of a team or group of users, you can ignore accounts.  ## Events  An event is a data point that represents an interaction between a user and/or an account; and your product. Events can represents any range of interactions. E.g. Every time a customer creates an invoice in an invoicing app. Actions like creating an invoice can be tracked as an event in journy.io.  It&#39;s critical to track events properly. You&#39;ll need to provide either an account ID, or a user ID, or both; when tracking an event. E.g. If a user updates his personal settings, you can omit the account ID as the event would not be related to any account. In a same logic, an account could get a &#39;suspend account&#39; event (with account ID) from an internal process, whereas no user would be associated. In most cases, events will be associated to both 1 user and 1 account.  You can optionally pass extra details as metadata (e.g. amount of the invoice). This gets particarly powerfull when creating computed properties on those event metadata. E.g. Our above ordering app could send journy.io &#39;Place Order&#39; events with metadata &#39;price&#39;, on which journy.io very easily would compute a total order value (for each account) for the last 30 days.  💡 Metadata does not update the properties of a user or account.  # Frontend vs backend  The best implementations we see employ a hybrid approach to maximize data quality while maintaining the flexibility to easily collect the data they need.  We recommend using our JavaScript snippet to track screen views and our backend API to sync users, sync accounts and track events.  When evaluating how to track a particular event, we suggest starting with server-side and only use frontend if it&#39;s not possible to collect purely server-side. This can be the case if you need to track interactions with your product that don&#39;t result in any natural server requests (such as a button click that opens a modal).  # Frontend  ## Setup  💡 You can find the JavaScript snippet in the website settings in the connections view.  Copy the JavaScript snippet and place it in the head or body of your application.  The snippet automatically calls &#x60;journy(\&quot;init\&quot;, { ... })&#x60; and &#x60;journy(\&quot;pageview\&quot;)&#x60;.  ## Identify user  💡 A user ID should be a robust, static, unique identifier that you recognize a user by in your own systems. Because these IDs are consistent across a customer’s lifetime, you should include a user ID in identify calls as often as you can. Ideally, the user ID should be a database ID.  💡 journy.io does not recommend using simple email addresses or usernames as user ID, as these can change over time. journy.io recommends that you use static IDs instead, so the IDs never change. When you use a static ID, you can still recognize the user in your analytics tools, even if the user changes their email address.  💡 The properties &#x60;full_name&#x60;, &#x60;first_name&#x60;, &#x60;last_name&#x60;, &#x60;phone&#x60; and &#x60;registered_at&#x60; will be used for creating contacts in destinations like Intercom, HubSpot, Salesforce, ...  &#x60;journy(\&quot;identify\&quot;)&#x60; allows you to identify the user that is currently using your product.  &#x60;&#x60;&#x60;ts journy(\&quot;identify\&quot;, {   // Email or user ID is required   email: \&quot;john.doe@acme.com\&quot;,   // Unique identifier for the user in your database   userId: \&quot;20\&quot;,    // Optional   // Hash of the user ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \&quot;hash\&quot;,    // Optional   properties: {     full_name: \&quot;John Doe\&quot;,     // or     first_name: \&quot;John\&quot;,     last_name: \&quot;Doe\&quot;,      phone: \&quot;123\&quot;,     registered_at: new Date(/_* ... *_/),     is_admin: true,     key_with_empty_value: \&quot;\&quot;,     this_property_will_be_deleted: null,   }, }); &#x60;&#x60;&#x60;  ## Identify account  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  💡 The properties &#x60;name&#x60;, &#x60;mrr&#x60;, &#x60;plan&#x60; and &#x60;registered_at&#x60; will be used to create companies in destinations like Intercom, HubSpot, Salesforce, ...  &#x60;journy(\&quot;account\&quot;)&#x60; allows you to identify the business account (i.e. organization) using your product.  &#x60;&#x60;&#x60;ts journy(\&quot;account\&quot;, {   // Required   // Unique identifier for the account in your database   accountId: \&quot;30\&quot;,    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \&quot;hash\&quot;,    // Optional   properties: {     name: \&quot;ACME, Inc\&quot;,     mrr: 399,     plan: \&quot;Pro\&quot;,     registered_at: new Date(/_* ... *_/),     is_paying: true,     key_with_empty_value: \&quot;\&quot;,     this_property_will_be_deleted: null,   }, }); &#x60;&#x60;&#x60;  ## Send page view  💡 In applications, we advise you to use screen views instead of page views.  The JavaScript snippet in the site settings includes a &#x60;pageview&#x60; by default.  &#x60;&#x60;&#x60;ts journy(\&quot;pageview\&quot;); &#x60;&#x60;&#x60;  If you have a B2B application, we recommend to set account ID for every page view that happens within the context of an account.  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  &#x60;&#x60;&#x60;ts journy(\&quot;pageview\&quot;, {   accountId: \&quot;30\&quot;,    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \&quot;hash\&quot;, }); &#x60;&#x60;&#x60;  ## Send screen view  In applications, we strongly advise you to use screen views instead of page views.  Page URLs in applications often include the account ID (e.g. https://app.acme.com/accountId/settings).  This makes it difficult to create signals, segments, ... based on those URLs.  That&#39;s what screen views solve. It allows you to set a name for the screen being viewed (e.g. Account settings).  &#x60;&#x60;&#x60;ts journy(\&quot;screen\&quot;, { name: \&quot;Personal settings\&quot; }); &#x60;&#x60;&#x60;  If you have a B2B application, we recommend to set account ID for every screen view that happens within the context of an account.  Example: \&quot;Personal settings\&quot; would be without account ID, \&quot;Team settings\&quot; would be with account ID.  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  &#x60;&#x60;&#x60;ts journy(\&quot;screen\&quot;, {   name: \&quot;Account settings\&quot;,   accountId: \&quot;30\&quot;,    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \&quot;hash\&quot;, }); &#x60;&#x60;&#x60;  ## Trigger an event  💡 Use past tense for event names.  User events:  &#x60;&#x60;&#x60;js journy(\&quot;event\&quot;, {   // required   name: \&quot;signed_in\&quot;,    // optional   metadata: {     key: \&quot;value\&quot;,   }, }); &#x60;&#x60;&#x60;  Account events:  💡 An account ID should be a robust, static, unique identifier that you recognize an account by in your own systems. Ideally, the account ID should be a database ID.  &#x60;&#x60;&#x60;js journy(\&quot;event\&quot;, {   // required   name: \&quot;created_invoice\&quot;,   accountId: \&quot;30\&quot;,    // Optional   // Hash of the account ID using a backend secret   // You can find the secret in the website settings   // Recommended to prevent spoofing   verification: \&quot;hash\&quot;,    // optional   metadata: {     key: \&quot;value\&quot;,     amount: 100,     allow_wire_transfer: true,   }, }); &#x60;&#x60;&#x60;  ## Identity verification  Identity verification ensures that one person can&#39;t impersonate another.  Identity verification requires you to add an hash (HMAC) (that you generate on your server using SHA256) to your installation snippet alongside your user ID and account ID.  journy.io won&#39;t accept requests for a logged-in user without a valid hash. The hash is calculated using a secret key, which you should never share. Without this secret key, no third party can send journy.io a valid hash for one of your users, so they can&#39;t impersonate your users.  This is optional but highly recommended.  You can enable identify verification in the website settings in the connections view.  &#x60;&#x60;&#x60;js journy(\&quot;identify\&quot;, {   userId: \&quot;userId\&quot;,   verification: \&quot;USER_ID_HMAC_VALUE_HERE\&quot; })  journy(\&quot;account\&quot;, {   accountId: \&quot;accountId\&quot;,   verification: \&quot;ACCOUNT_ID_HMAC_VALUE_HERE\&quot; })  journy(\&quot;event\&quot;, {   accountId: \&quot;accountId\&quot;,   verification: \&quot;ACCOUNT_ID_HMAC_VALUE_HERE\&quot; }) &#x60;&#x60;&#x60;  ### PHP  &#x60;&#x60;&#x60;php &lt;?php  hash_hmac(   &#39;sha256&#39;, // hash function   id, // user or account ID   &#39;secret&#39; // secret key (keep safe!) ); &#x60;&#x60;&#x60;  ### Node.js  &#x60;&#x60;&#x60;js import { createHmac } from \&quot;crypto\&quot;  createHmac(   \&quot;sha256\&quot;, // hash function   &#39;secret&#39; // secret key (keep safe!) ).update(id).digest(\&quot;hex\&quot;) // user or account ID &#x60;&#x60;&#x60;  ### Ruby  &#x60;&#x60;&#x60;ruby OpenSSL::HMAC.hexdigest(   &#39;sha256&#39;, # hash function   &#39;secret&#39;, # secret key (keep safe!)   id.to_s # user or account ID ) &#x60;&#x60;&#x60;  ### Python  &#x60;&#x60;&#x60; import hmac import hashlib  hmac.new(   b&#39;secret&#39;, # secret key (keep safe!)   bytes(id, encoding&#x3D;&#39;utf-8&#39;), # user or account ID   digestmod&#x3D;hashlib.sha256 # hash function ).hexdigest() &#x60;&#x60;&#x60;  ## Single page application  You can use our JavaScript snippet inside single page applications.  You should call &#x60;journy(\&quot;screen\&quot;)&#x60; (or &#x60;journy(\&quot;pageview\&quot;)&#x60;) whenever a user in your application transitions to another page. You can do this by listening to router change events. The current page URL will always be resolved using &#x60;window.location.href&#x60;.  You can trigger events using &#x60;journy(\&quot;event\&quot;)&#x60; whenever you need to.  ### Next.js  We built a demo app with Next.js. You can find the code [here](https://github.com/journy-io/js-sdk-demo-app).  This [component](https://github.com/journy-io/js-sdk-demo-app/blob/main/components/Journy.js) should be a great start.  You can use the &#x60;Script&#x60; component from Next.js to load the web snippet and call &#x60;init&#x60;.  Don&#39;t forget to listen on route changes. You can use the &#x60;useRouter&#x60; hook for that.  ### React Router v6  You can use the [&#x60;useLocation&#x60;](https://reactrouter.com/docs/en/v6/api#uselocation) hook to listen for route changes:  &#x60;&#x60;&#x60;js import React, { useEffect } from \&quot;react\&quot;; import { useLocation } from &#39;react-router-dom&#39;;  function App() {   const location &#x3D; useLocation();    useEffect(() &#x3D;&gt; {     journy(\&quot;screen\&quot;, { name: \&quot;name\&quot; });     // or     journy(\&quot;pageview\&quot;);   }, [location]);    return (       // ...   ); } &#x60;&#x60;&#x60;  ### Vue Router  You can use [&#x60;router.afterEach&#x60;](https://router.vuejs.org/guide/advanced/navigation-guards.html#global-after-hooks) to listen for route changes:  &#x60;&#x60;&#x60;js const router &#x3D; new VueRouter({ ... });  router.afterEach((to, from) &#x3D;&gt; {   journy(\&quot;screen\&quot;, { name: \&quot;name\&quot; });   // or   journy(\&quot;pageview\&quot;); }); &#x60;&#x60;&#x60;  Note: We don&#39;t accept a page URL argument for &#x60;journy(\&quot;pageview\&quot;)&#x60;. The current page URL will always be resolved using &#x60;window.location.href&#x60;.  ## TypeScript  We published an [npm package](https://www.npmjs.com/package/@journyio/web-types) with type definitions to enable type-safe usage of our JavaScript snippet. The code and documentation is available on [GitHub](https://github.com/journy-io/web-types).  ## Localhost  By default a site doesn&#39;t allow page views from other domains than the registered domain. This makes it difficult to test your tracking implementation locally.  You can enable \&quot;Allow any domain\&quot; in the site settings to disable the domain check.  This will allow you to test the JavaScript snippet with localhost as hostname.  # Backend  The journy.io API is organized around REST. Our API has predictable resource-oriented URLs, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  The API is hosted on api.journy.io.  ## Official SDKs  Our SDKs are designed to help you interact with our APIs with less friction. They are written in several different languages and help bridge the gap between your application and journy.io APIs. They take away the need to know the exact URL and HTTP method to use for each API call among other things leaving you more time to focus on making your application.  | Language   | Package                                                                        | Source code                                                                | |------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------| | 💚 Node.js | [npm install @journyio/sdk ](https://www.npmjs.com/package/@journyio/sdk)      | [github.com/journy-io/js-sdk](https://github.com/journy-io/js-sdk)         | | 🐘 PHP     | [composer require journy-io/sdk](https://packagist.org/packages/journy-io/sdk) | [github.com/journy-io/php-sdk](https://github.com/journy-io/php-sdk)       | | 🐍 Python  | [pip install journyio-sdk](https://pypi.org/project/journyio-sdk/)             | [github.com/journy-io/python-sdk](https://github.com/journy-io/python-sdk) | | 💎 Ruby    | Coming soon                                                                    | Coming soon                                                                |  Your favourite programming language not included? [Let us know!](mailto:hi@journy.io)  In the meanwhile, you can use [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) to generate a client for your programming language.  ## Authentication  The journy.io API uses API keys to authenticate requests. You can view and manage your API keys in the [connections screen](https://system.journy.io).  Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, and so forth.  All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.  For every request send to the API we expect a header &#x60;X-Api-Key&#x60; to be set with the API Key.  ## Permissions  When creating an API Key in [the application](https://system.journy.io) you will have the choice to give permissions to an API Key (which you can change later on). These permissions restrict the API Key from different actions. When an API Key tries to perform a certain action it doesn&#39;t have the permissions for, you will receive a &#x60;401: Unauthorized&#x60; response.  ## Rate limiting  To prevent abuse of the API there is a maximum throughput of 1800 requests per minute. If you need a higher throughput, please contact us.  To keep our platform healthy and stable, we&#39;ll block API keys that consistently hit our rate limits. Therefore, please consider taking this throughput into account.  In every response the headers &#x60;X-RateLimit-Limit&#x60; and &#x60;X-RateLimit-Remaining&#x60; will be set. The &#x60;X-RateLimit-Limit&#x60;-header will always contain the current limit of requests per minute. The &#x60;X-RateLimit-Remaining&#x60;-header will always contain the amount of requests you have left in the current sliding window.  💡 The client-side tracking uses different rate limits.  ## Errors  journy.io uses conventional HTTP response codes to indicate the success or failure of an API request. In general: Codes in the 2xx range indicate success. Codes in the 4xx range indicate an error that failed given the information provided (e.g. a required parameter was omitted). Codes in the 5xx range indicate an error with journy.io&#39;s servers (these are rare).  When performing a &#x60;POST&#x60;- or &#x60;PUT&#x60;-request with a requestBody, or when including parameters, these parameters and fields will automatically be checked and validated against the API Spec. When any error occurs, you will get a response with an &#x60;errors&#x60;-field, structured as follows:  &#x60;&#x60;&#x60;json {   \&quot;errors\&quot;: {     \&quot;parameters\&quot;: {       \&quot;header\&quot;: {         \&quot;headerParameterName\&quot;: \&quot;Describe what&#39;s wrong with the header parameter.\&quot;,         ...       },       \&quot;query\&quot;: {         \&quot;queryParameterName\&quot;: \&quot;Describe what&#39;s wrong with the query parameter.\&quot;,         ...       },       \&quot;path\&quot;: {         \&quot;pathParameterName\&quot;: \&quot;Describe what&#39;s wrong with the path parameter.\&quot;,         ...       },     },     \&quot;fields\&quot;: {       \&quot;fieldName\&quot;: \&quot;Describe what&#39;s wrong with the fieldName.\&quot;,       \&quot;object.fieldName\&quot;: \&quot;Describe what&#39;s wrong with the fieldName of the included object.\&quot;,        ...     }   } } &#x60;&#x60;&#x60;  ## Best practices  ### Track accounts &amp; users immediately on creation  When you create an account in your database, immediately sending data about that account to journy.io helps your team stay in sync. The same goes for users. Call [Upsert account](#operation/upsertAccount) as soon as possible, right after the account is first created in your database.  ### Update account data daily  Not every account is active every day. But, you may have properties on the account that change through background processing. That&#39;s why we recommend updating every one of your accounts&#39; data in a recurring daily process. This way, you know that your accounts are updated every day in journy.io.  ## Changelog  ### December 2021  [POST /events](#operation/trackJourneyEvent) will be moved to [POST /track](#operation/trackEvent). [POST /events](#operation/trackJourneyEvent) is deprecated and will be removed in the future..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var DeveloperDocumentation = require('index'); // See note below*.
* var xxxSvc = new DeveloperDocumentation.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new DeveloperDocumentation.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new DeveloperDocumentation.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new DeveloperDocumentation.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AddUserToAccountRequest model constructor.
     * @property {module:model/AddUserToAccountRequest}
     */
    AddUserToAccountRequest,

    /**
     * The AddUserToAccountRequestUsersInner model constructor.
     * @property {module:model/AddUserToAccountRequestUsersInner}
     */
    AddUserToAccountRequestUsersInner,

    /**
     * The AddUserToAccountRequestUsersInnerIdentification model constructor.
     * @property {module:model/AddUserToAccountRequestUsersInnerIdentification}
     */
    AddUserToAccountRequestUsersInnerIdentification,

    /**
     * The DeleteAccount202Response model constructor.
     * @property {module:model/DeleteAccount202Response}
     */
    DeleteAccount202Response,

    /**
     * The DeleteAccount202ResponseAllOfMeta model constructor.
     * @property {module:model/DeleteAccount202ResponseAllOfMeta}
     */
    DeleteAccount202ResponseAllOfMeta,

    /**
     * The DeleteAccount400Response model constructor.
     * @property {module:model/DeleteAccount400Response}
     */
    DeleteAccount400Response,

    /**
     * The DeleteAccount400ResponseAllOfErrors model constructor.
     * @property {module:model/DeleteAccount400ResponseAllOfErrors}
     */
    DeleteAccount400ResponseAllOfErrors,

    /**
     * The DeleteAccount400ResponseAllOfErrorsParameters model constructor.
     * @property {module:model/DeleteAccount400ResponseAllOfErrorsParameters}
     */
    DeleteAccount400ResponseAllOfErrorsParameters,

    /**
     * The DeleteAccountRequest model constructor.
     * @property {module:model/DeleteAccountRequest}
     */
    DeleteAccountRequest,

    /**
     * The DeleteAccountRequestIdentification model constructor.
     * @property {module:model/DeleteAccountRequestIdentification}
     */
    DeleteAccountRequestIdentification,

    /**
     * The DeleteUserRequest model constructor.
     * @property {module:model/DeleteUserRequest}
     */
    DeleteUserRequest,

    /**
     * The GetAccountProperties200Response model constructor.
     * @property {module:model/GetAccountProperties200Response}
     */
    GetAccountProperties200Response,

    /**
     * The GetAccountProperties200ResponseAllOfDataInner model constructor.
     * @property {module:model/GetAccountProperties200ResponseAllOfDataInner}
     */
    GetAccountProperties200ResponseAllOfDataInner,

    /**
     * The GetAccountProperties200ResponseAllOfDataInnerGroup model constructor.
     * @property {module:model/GetAccountProperties200ResponseAllOfDataInnerGroup}
     */
    GetAccountProperties200ResponseAllOfDataInnerGroup,

    /**
     * The GetAccountSegments200Response model constructor.
     * @property {module:model/GetAccountSegments200Response}
     */
    GetAccountSegments200Response,

    /**
     * The GetAccountSegments200ResponseAllOfDataInner model constructor.
     * @property {module:model/GetAccountSegments200ResponseAllOfDataInner}
     */
    GetAccountSegments200ResponseAllOfDataInner,

    /**
     * The GetEvents200Response model constructor.
     * @property {module:model/GetEvents200Response}
     */
    GetEvents200Response,

    /**
     * The GetEvents200ResponseAllOfDataInner model constructor.
     * @property {module:model/GetEvents200ResponseAllOfDataInner}
     */
    GetEvents200ResponseAllOfDataInner,

    /**
     * The GetEvents200ResponseAllOfDataInnerGroup model constructor.
     * @property {module:model/GetEvents200ResponseAllOfDataInnerGroup}
     */
    GetEvents200ResponseAllOfDataInnerGroup,

    /**
     * The GetTrackingSnippet200Response model constructor.
     * @property {module:model/GetTrackingSnippet200Response}
     */
    GetTrackingSnippet200Response,

    /**
     * The GetTrackingSnippet200ResponseAllOfData model constructor.
     * @property {module:model/GetTrackingSnippet200ResponseAllOfData}
     */
    GetTrackingSnippet200ResponseAllOfData,

    /**
     * The GetValidity200Response model constructor.
     * @property {module:model/GetValidity200Response}
     */
    GetValidity200Response,

    /**
     * The GetValidity200ResponseAllOfData model constructor.
     * @property {module:model/GetValidity200ResponseAllOfData}
     */
    GetValidity200ResponseAllOfData,

    /**
     * The LinkRequest model constructor.
     * @property {module:model/LinkRequest}
     */
    LinkRequest,

    /**
     * The TrackEventRequest model constructor.
     * @property {module:model/TrackEventRequest}
     */
    TrackEventRequest,

    /**
     * The TrackEventRequestMetadataValue model constructor.
     * @property {module:model/TrackEventRequestMetadataValue}
     */
    TrackEventRequestMetadataValue,

    /**
     * The TrackJourneyEventRequest model constructor.
     * @property {module:model/TrackJourneyEventRequest}
     */
    TrackJourneyEventRequest,

    /**
     * The TrackJourneyEventRequestIdentification model constructor.
     * @property {module:model/TrackJourneyEventRequestIdentification}
     */
    TrackJourneyEventRequestIdentification,

    /**
     * The TrackJourneyEventRequestMetadataValue model constructor.
     * @property {module:model/TrackJourneyEventRequestMetadataValue}
     */
    TrackJourneyEventRequestMetadataValue,

    /**
     * The UpsertAccount201Response model constructor.
     * @property {module:model/UpsertAccount201Response}
     */
    UpsertAccount201Response,

    /**
     * The UpsertAccountRequest model constructor.
     * @property {module:model/UpsertAccountRequest}
     */
    UpsertAccountRequest,

    /**
     * The UpsertAccountRequestPropertiesValue model constructor.
     * @property {module:model/UpsertAccountRequestPropertiesValue}
     */
    UpsertAccountRequestPropertiesValue,

    /**
     * The UpsertUser201Response model constructor.
     * @property {module:model/UpsertUser201Response}
     */
    UpsertUser201Response,

    /**
     * The UpsertUserRequest model constructor.
     * @property {module:model/UpsertUserRequest}
     */
    UpsertUserRequest,

    /**
    * The AccountsApi service constructor.
    * @property {module:api/AccountsApi}
    */
    AccountsApi,

    /**
    * The EventsApi service constructor.
    * @property {module:api/EventsApi}
    */
    EventsApi,

    /**
    * The PropertiesApi service constructor.
    * @property {module:api/PropertiesApi}
    */
    PropertiesApi,

    /**
    * The SegmentsApi service constructor.
    * @property {module:api/SegmentsApi}
    */
    SegmentsApi,

    /**
    * The TrackApi service constructor.
    * @property {module:api/TrackApi}
    */
    TrackApi,

    /**
    * The UsersApi service constructor.
    * @property {module:api/UsersApi}
    */
    UsersApi,

    /**
    * The ValidationApi service constructor.
    * @property {module:api/ValidationApi}
    */
    ValidationApi,

    /**
    * The WebsitesApi service constructor.
    * @property {module:api/WebsitesApi}
    */
    WebsitesApi
};
