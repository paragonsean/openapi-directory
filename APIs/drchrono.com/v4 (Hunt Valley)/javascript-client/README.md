# openapi-js-client

OpenapiJsClient - JavaScript client for openapi-js-client
This document is intended as a detailed reference for the precise behavior of
the drchrono API. If this is your first time using the API, start with our <a href=\"/api-docs-old/tutorial\">tutorial</a>. If you are upgrading from a previous version, take a look at the changelog section.

# Authorization

## Initial authorization

There are three main steps in the OAuth 2.0 authentication workflow:

1. Redirect the provider to the authorization page.
2. The provider authorizes your application and is redirected back to
   your web application.
3. Your application exchanges the `authorization_code` that came with
   the redirect for an `access_token` and `refresh_token`.

### Step 1: Redirect to drchrono

The first step is redirecting your user to drchrono, typically with a button
labeled \"Connect to drchrono\" or \"Login with drchrono\".  This is just a link that
takes your user to the following URL:

    https://drchrono.com/o/authorize/?redirect_uri=REDIRECT_URI_ENCODED&response_type=code&client_id=CLIENT_ID_ENCODED&scope=SCOPES_ENCODED

- `REDIRECT_URI_ENCODED` is the URL-encoded version of the redirect URI (as registered for your application and used in later steps).
- `CLIENT_ID_ENCODED` is the URL-encoded version of your application's client ID.
- `SCOPES_ENCODED` is a URL-encoded version of a space-separated list of scopes, which can be found in each endpoint or omitted to default to all scopes.

The `scope` parameter consists of an optional, space-separated list of scopes your application is requesting.
If omitted, all scopes will be requested.

Scopes are of the form `BASE_SCOPE:[read|write]` where `BASE_SCOPE` is any of `user`, `calendar`, `patients`, `patients:summary`, `billing`, `clinical` and `labs`.
You should request only the scopes you need.
For instance, an application which sends \"Happy Birthday!\" emails to a doctor's patients on their birthdays would use the scope parameter `\"patients:summary:read\"`,
while one that allows patients to schedule appointments online would need at least
`\"patients:summary:read patients:summary:write calendar:read calendar:write clinical:read clinical:write\"`.

### Step 2: Provider authorization

After logging in (if necessary), the provider will be presented with a screen
with your application's name and the list of permissions you requested (via the
`scope` parameter).

When they click the \"Authorize\" button, they will be redirected to your redirect
URI with a `code` query parameter appended, which contains an authorization code to be
used in step 3.  If they click the \"Cancel\" button, they will be redirected to
your redirect URI with `error=access_denied` instead.

Note: This authorization code expires extremely quickly, so you must perform
step 3 immediately, ideally before rendering the resulting page for the end
user.

### Step 3: Token exchange

The `code` obtained from step 2 is usable exactly once to obtain an access token
and refresh token.  Here is an example token exchange in Python:

    import datetime, pytz, requests

    if 'error' in get_params:
        raise ValueError('Error authorizing application: %s' % get_params[error])

    response = requests.post('https://drchrono.com/o/token/', data={
        'code': get_params['code'],
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://mytestapp.com/redirect_uri',
        'client_id': 'abcdefg12345',
        'client_secret': 'abcdefg12345',
    })
    response.raise_for_status()
    data = response.json()

    # Save these in your database associated with the user
    access_token = data['access_token']
    refresh_token = data['refresh_token']
    expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])

You now have all you need to make API requests authenticated as that provider.
When using this access token, you'll only be able to access the data that the
user has access to and that you have been granted permissions for.

## Refreshing an access token

Access tokens only last 48 hours (given in seconds in the `'expires_in'` key in
the token exchange step above), so they occasionally need to be refreshed.  It
would be inconvenient to ask the user to re-authorize every time, so instead you
can use the refresh token like the original authorization to obtain a new access
token.  Replace the `code` parameter with `refresh_token`, change the value
`grant_type` from `authorization_code` to `refresh_token`, and omit the
`redirect_uri` parameter.

Example in Python:

    ...
    response = requests.post('https://drchrono.com/o/token/', data={
        'refresh_token': get_refresh_token(),
        'grant_type': 'refresh_token',
        'client_id': 'abcdefg12345',
        'client_secret': 'abcdefg12345',
    })
    ...

# Webhooks

In order to use drchrono API webhooks, you first need to have an API application on file
(even if it is in Test Model).
Each API webhook is associated with one API application, go to
<a href=\"/api-management/\" target=\"_blank\">here</a> to set up both API applications and webhooks!

Once you registered an API application, you will see webhook section in each saved API applications.
Create a webhook and register some events there and save all the changes, then you are good to go!

## Webhooks setup

All fields under webhooks section are required.

**Callback URL**
Callback URl is used to receive all hooks when subscribed events are triggered. This should be an URL under your control.

**Secret token**
Secret token is used to verify webhooks, this is very important, please set something with high entropy. Also we will
talk more about this later.

**Events**

Events is used to register events you want to receiver notification when they happen. Currently we support following events.

Event name | Event description
---------- | -----------------
`APPOINTMENT_CREATE` | We will deliver a hook any time an appointment is created
`APPOINTMENT_MODIFY` | We will deliver a hook any time an appointment is modified
`PATIENT_CREATE` | We will deliver a hook any time a patient is created
`PATIENT_MODIFY` | We will deliver a hook any time a patient is modified
`PATIENT_PROBLEM_CREATE` | We will deliver a hook any time a patient problem is created
`PATIENT_PROBLEM_MODIFY` | We will deliver a hook any time a patient problem is modified
`PATIENT_ALLERGY_CREATE` | We will deliver a hook any time a patient allergy is created
`PATIENT_ALLERGY_MODIFY` | We will deliver a hook any time a patient allergy is modified
`PATIENT_MEDICATION_CREATE` | We will deliver a hook any time a patient medication is created
`PATIENT_MEDICATION_MODIFY` | We will deliver a hook any time a patient medication is modified
`CLINICAL_NOTE_LOCK` | We will deliver a hook any time a clinical note is locked
`CLINICAL_NOTE_UNLOCK` | We will deliver a hook any time a clinical note is unlocked
`TASK_CREATE` | We will deliver a hook any time a task is created
`TASK_MODIFY` | We will deliver a hook any time a task is modified and any time creation, modification and deletion of task notes, associated task item
`TASK_DELETE` | We will deliver a hook any time a task is deleted


## Webhooks verification

In order to make sure the callback URL in webhook is under your control, we added a verification
step before we send any hooks out to you.

Verification can be done by clicking \"Verify webhook\" button in webhooks setup page. After you click
the button, we will send a `GET` request to the callback URL, along with a parameter called `msg`.

Please use your webhook's secret token as hash key and SHA-256 as digest constructor, hash the `msg` value with
<a href=\"https://tools.ietf.org/html/rfc2104.html\">HMAC algorithm</a>.
And we expect a `200` JSON response, in JSON response body, there should be a key called `secret_token` existing, and its value should be
equal to the <strong>hashed</strong> `msg`. Otherwise, verification will fail.

Here is an example webhook verification in Python:

    import hashlib, hmac

    def webhook_verify(request):
        secret_token = hmac.new(WEBHOOK_SECRET_TOKEN, request.GET['msg'], hashlib.sha256).hexdigest()
        return json_response({
            'secret_token': secret_token
        })

<div class=\"alert alert-warning\">
<b>Note:</b> Verification will be needed when webhook is first created and anytime callback URl is changed.
</div>


## Webhooks header and body

**Header**

Key | Value
--- | -----
`X-drchrono-event` | Event that triggered this hook, could be any one event above or `PING`
`X-drchrono-signature` | Secret token associated with this webhook
`X-drchrono-delivery` | ID of this delivery

**Body**

Key | Value
--- | -----
`receiver` | This will be an JSON representation of the webhook
`object` | This will be an JSON representation of the object related to the triggered event, this would share same serializer as drchrono API

## Webhooks ping and deliveries

Webhooks ping and deliveries will be sent as `POST` requests.

**PING**:

You can always ping your webhook to check things, by clicking the \"Ping webhook\" button in webhook setup page. And a hook with header `X-drchrono-event: PING` would be sent to the callback URL.

**Deliveries**:

You can check recent deliveries by clicking the \"deliveries\" link in webhook setup page. And you can resend a hook by clicking \"redeliver\" button after select a specific delivery.

## Webhooks delivery mechanism

We will delivery a hook the moment a subscribed event is triggered. We will not record any response header or body you send back after you receive the hook.
However we only consider the response status code. We will consider any `2xx` responses as successfully delivered.
Any other responses, like `302` would be considered failing.
And we will try to redeliver unsuccessfully delivered hooks 3 times, first redeliver happens at 1 hour after the initial event,
second receliver happens 3 hours after the initial event, and the third redeliver happens 7 hours after the initial event.
After these redeliveries, if the delivery is still unsuccessful, you have to redeliver it by hand.


## Webhooks security

You may want to secure your webhooks to only consider requests send out from drchrono. And this is where <code>secret_token</code> is needed in
request header.
Try to set the <code>secret_token</code> to something with high entropy, a good example could be taking the output of
<code>ruby -rsecurerandom -e 'puts SecureRandom.hex(20)'</code>.
After this, you might want to verify all request headers you received on your server with this token.


# iframe integration

Some API apps provide additional functionality for interacting with patient data
not offered by drchrono, and can benefit by being incorporated into drchrono's
patient information page via iframe.  We have created a simple API to make this
possible.

To make an existing API application accessible via an iframe on the patient
page, you need to update either \"Patient iframe\" or \"Clinical note iframe\" section in API management page,
to make the iframe to appear on (either the patient page or the clinical note page),
with the URL that the iframe will use for each page, and the height it should
have. The application will be reviewed before it is approved to ensure that it
is functional and secure.

## Register a Doctor

iframe applications will appear as choices on the left-hand menu of the patient
page for doctors registered with your application.  To register a doctor with
your application, make a `POST` request to the `/api/iframe_integration`
endpoint using the access token for the corresponding doctor. This endpoint does not
expect any payload.

To disable your iframe application for a doctor, make a `DELETE` request to the
same endpoint.

## Populating the iframe

There are two places where the iframe can be displayed, either within the
patient detail page or the clinical note page, shown below respectively:

<img src=\"{% asset 'public/images/iframe_patient_page.png' %}\" alt=\"Iframe on the patient page\"/>

<img src=\"{% asset 'public/images/iframe_clinical_note.png' %}\" alt=\"Iframe on the clinical note page\"/>

When requesting approval for your iframe app, you must specify a URL for one or
both of these pages which will serve as the base URL for your IFrame
contents. When a doctor views your iframe, the source URL will have various
query parameters appended to it, for example for the patient page the `src`
parameter of the IFrame will be:

```
<iframe_url>?doctor_id=<doctor_id>&patient_id=<patient_id>&practice_id=<practice_id>&iat=<iat>&jwt=<jwt>
```

The `jwt` parameter is crucial if your application transfers any sort of PHI and
does not implement its own login system.  It encapsulates the other parameters
in a [JSON web token (JWT)](http://jwt.io) and signs them using SHA-256 HMAC
with your `client_secret` as the key.  This verifies that the iframe is being
loaded within one of drchrono's pages by an authorized user.  In production, you
should validate the JWT using an approved library (which are listed on the
[official site](http://jwt.io)), and only use the parameters extracted from the
JWT.  Using Python and Django, this might look like:

    import jwt

    CLIENT_SECRET = <client_secret>
    MAX_TIME_DRIFT_SECONDS = 60

    def validate_parameters(request):
        token = request.GET['jwt']

        return jwt.decode(token, CLIENT_SECRET, algorithms=['HS256'], leeway=MAX_TIME_DRIFT_SECONDS)

Modern browsers' same-origin policy means that data cannot be passed between
your application and drchrono's page through the iframe.  Therefore, interaction
must happen through the API, using information provided in JWT.

# Versions and deprecation

## Stability Policy

Changes to this API version will be limited to adding endpoints, or adding fields to existing
endpoints, or adding optional query parameters. Any new fields which are not read-only will be optional.

## Deprecation Policy

The drchrono API is versioned. Versions can be in the following states:

* **Active:** This is our latest and greatest version of the API. It is actively supported by
our API team and is improved upon with new features, bug fixes and optimizations that do
not break backwards compatibility.

* **Deprecated:** A deprecated API version is considered second best--having been
surpassed by our active API version. An API version remains in this state for one year,
after which time it falls to the not supported state. A deprecated API version is passively supported;
while it won't be removed until becoming unsupported, it may not receive new features but will likely
be subject to security updates and performance improvements.

* **Unsupported:** An API version in the not supported state may be deactivated at any
time. An application using an unsupported API version should migrate to an active API version.

## Version Map
| Version Name | Previous Name | Start Date | Deprecation Date |
|--------------|---------------|------------|------------------|
| v2           | v2015_08      | 08/2015    | TBA              |
| v3           | v2016_06      | 06/2016    |                  |
| v4           | N/A           | 09/2018    |                  |

If you are looking for documentation for an older version

- [V4(Hunt Valley)](/api-docs-old/v4/documentation) (old V4 documentation)
- [V3(Sunnyvale)](/api-docs-old/v3/documentation)
- [V2(Mountain View)](/api-docs-old/v2/documentation)

# Changelog

Here's changelog for different versions

- [V4 Changelog](/api-docs-old/v4/changelog)
- [V3 changelog](/api-docs-old/v3/changelog)


This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v4 (Hunt Valley)
- Package version: v4 (Hunt Valley)
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install openapi-js-client --save
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

To use the link you just defined in your project, switch to the directory you want to use your openapi-js-client from, and run:

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
var OpenapiJsClient = require('openapi-js-client');

var defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
var drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = "YOUR ACCESS TOKEN"

var api = new OpenapiJsClient.AdministrativeApi()
var opts = {
  'cursor': "cursor_example", // {String} 
  'pageSize': 56, // {Number} 
  'doctor': 56 // {Number} 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.doctorsList(opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://app.drchrono.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OpenapiJsClient.AdministrativeApi* | [**doctorsList**](docs/AdministrativeApi.md#doctorsList) | **GET** /api/doctors | 
*OpenapiJsClient.AdministrativeApi* | [**doctorsRead**](docs/AdministrativeApi.md#doctorsRead) | **GET** /api/doctors/{id} | 
*OpenapiJsClient.AdministrativeApi* | [**userGroupsList**](docs/AdministrativeApi.md#userGroupsList) | **GET** /api/user_groups | 
*OpenapiJsClient.AdministrativeApi* | [**userGroupsRead**](docs/AdministrativeApi.md#userGroupsRead) | **GET** /api/user_groups/{id} | 
*OpenapiJsClient.AdministrativeApi* | [**usersList**](docs/AdministrativeApi.md#usersList) | **GET** /api/users | 
*OpenapiJsClient.AdministrativeApi* | [**usersRead**](docs/AdministrativeApi.md#usersRead) | **GET** /api/users/{id} | 
*OpenapiJsClient.BillingApi* | [**billingProfilesList**](docs/BillingApi.md#billingProfilesList) | **GET** /api/billing_profiles | 
*OpenapiJsClient.BillingApi* | [**billingProfilesRead**](docs/BillingApi.md#billingProfilesRead) | **GET** /api/billing_profiles/{id} | 
*OpenapiJsClient.BillingApi* | [**commLogsCreate**](docs/BillingApi.md#commLogsCreate) | **POST** /api/comm_logs | 
*OpenapiJsClient.BillingApi* | [**commLogsList**](docs/BillingApi.md#commLogsList) | **GET** /api/comm_logs | 
*OpenapiJsClient.BillingApi* | [**commLogsPartialUpdate**](docs/BillingApi.md#commLogsPartialUpdate) | **PATCH** /api/comm_logs/{id} | 
*OpenapiJsClient.BillingApi* | [**commLogsRead**](docs/BillingApi.md#commLogsRead) | **GET** /api/comm_logs/{id} | 
*OpenapiJsClient.BillingApi* | [**commLogsUpdate**](docs/BillingApi.md#commLogsUpdate) | **PUT** /api/comm_logs/{id} | 
*OpenapiJsClient.BillingApi* | [**customInsurancePlanNamesList**](docs/BillingApi.md#customInsurancePlanNamesList) | **GET** /api/custom_insurance_plan_names | 
*OpenapiJsClient.BillingApi* | [**customInsurancePlanNamesRead**](docs/BillingApi.md#customInsurancePlanNamesRead) | **GET** /api/custom_insurance_plan_names/{id} | 
*OpenapiJsClient.BillingApi* | [**eligibilityChecksList**](docs/BillingApi.md#eligibilityChecksList) | **GET** /api/eligibility_checks | 
*OpenapiJsClient.BillingApi* | [**eligibilityChecksRead**](docs/BillingApi.md#eligibilityChecksRead) | **GET** /api/eligibility_checks/{id} | 
*OpenapiJsClient.BillingApi* | [**lineItemsCreate**](docs/BillingApi.md#lineItemsCreate) | **POST** /api/line_items | 
*OpenapiJsClient.BillingApi* | [**lineItemsDelete**](docs/BillingApi.md#lineItemsDelete) | **DELETE** /api/line_items/{id} | 
*OpenapiJsClient.BillingApi* | [**lineItemsList**](docs/BillingApi.md#lineItemsList) | **GET** /api/line_items | 
*OpenapiJsClient.BillingApi* | [**lineItemsPartialUpdate**](docs/BillingApi.md#lineItemsPartialUpdate) | **PATCH** /api/line_items/{id} | 
*OpenapiJsClient.BillingApi* | [**lineItemsRead**](docs/BillingApi.md#lineItemsRead) | **GET** /api/line_items/{id} | 
*OpenapiJsClient.BillingApi* | [**lineItemsUpdate**](docs/BillingApi.md#lineItemsUpdate) | **PUT** /api/line_items/{id} | 
*OpenapiJsClient.BillingApi* | [**patientPaymentLogList**](docs/BillingApi.md#patientPaymentLogList) | **GET** /api/patient_payment_log | 
*OpenapiJsClient.BillingApi* | [**patientPaymentLogRead**](docs/BillingApi.md#patientPaymentLogRead) | **GET** /api/patient_payment_log/{id} | 
*OpenapiJsClient.BillingApi* | [**patientPaymentsCreate**](docs/BillingApi.md#patientPaymentsCreate) | **POST** /api/patient_payments | 
*OpenapiJsClient.BillingApi* | [**patientPaymentsList**](docs/BillingApi.md#patientPaymentsList) | **GET** /api/patient_payments | 
*OpenapiJsClient.BillingApi* | [**patientPaymentsRead**](docs/BillingApi.md#patientPaymentsRead) | **GET** /api/patient_payments/{id} | 
*OpenapiJsClient.BillingApi* | [**proceduresList**](docs/BillingApi.md#proceduresList) | **GET** /api/procedures | 
*OpenapiJsClient.BillingApi* | [**proceduresRead**](docs/BillingApi.md#proceduresRead) | **GET** /api/procedures/{id} | 
*OpenapiJsClient.BillingApi* | [**transactionsList**](docs/BillingApi.md#transactionsList) | **GET** /api/transactions | 
*OpenapiJsClient.BillingApi* | [**transactionsRead**](docs/BillingApi.md#transactionsRead) | **GET** /api/transactions/{id} | 
*OpenapiJsClient.ClinicalApi* | [**allergiesCreate**](docs/ClinicalApi.md#allergiesCreate) | **POST** /api/allergies | 
*OpenapiJsClient.ClinicalApi* | [**allergiesList**](docs/ClinicalApi.md#allergiesList) | **GET** /api/allergies | 
*OpenapiJsClient.ClinicalApi* | [**allergiesPartialUpdate**](docs/ClinicalApi.md#allergiesPartialUpdate) | **PATCH** /api/allergies/{id} | 
*OpenapiJsClient.ClinicalApi* | [**allergiesRead**](docs/ClinicalApi.md#allergiesRead) | **GET** /api/allergies/{id} | 
*OpenapiJsClient.ClinicalApi* | [**allergiesUpdate**](docs/ClinicalApi.md#allergiesUpdate) | **PUT** /api/allergies/{id} | 
*OpenapiJsClient.ClinicalApi* | [**amendmentsCreate**](docs/ClinicalApi.md#amendmentsCreate) | **POST** /api/amendments | 
*OpenapiJsClient.ClinicalApi* | [**amendmentsDelete**](docs/ClinicalApi.md#amendmentsDelete) | **DELETE** /api/amendments/{id} | 
*OpenapiJsClient.ClinicalApi* | [**amendmentsList**](docs/ClinicalApi.md#amendmentsList) | **GET** /api/amendments | 
*OpenapiJsClient.ClinicalApi* | [**amendmentsPartialUpdate**](docs/ClinicalApi.md#amendmentsPartialUpdate) | **PATCH** /api/amendments/{id} | 
*OpenapiJsClient.ClinicalApi* | [**amendmentsRead**](docs/ClinicalApi.md#amendmentsRead) | **GET** /api/amendments/{id} | 
*OpenapiJsClient.ClinicalApi* | [**amendmentsUpdate**](docs/ClinicalApi.md#amendmentsUpdate) | **PUT** /api/amendments/{id} | 
*OpenapiJsClient.ClinicalApi* | [**appointmentProfilesCreate**](docs/ClinicalApi.md#appointmentProfilesCreate) | **POST** /api/appointment_profiles | 
*OpenapiJsClient.ClinicalApi* | [**appointmentProfilesDelete**](docs/ClinicalApi.md#appointmentProfilesDelete) | **DELETE** /api/appointment_profiles/{id} | 
*OpenapiJsClient.ClinicalApi* | [**appointmentProfilesList**](docs/ClinicalApi.md#appointmentProfilesList) | **GET** /api/appointment_profiles | 
*OpenapiJsClient.ClinicalApi* | [**appointmentProfilesPartialUpdate**](docs/ClinicalApi.md#appointmentProfilesPartialUpdate) | **PATCH** /api/appointment_profiles/{id} | 
*OpenapiJsClient.ClinicalApi* | [**appointmentProfilesRead**](docs/ClinicalApi.md#appointmentProfilesRead) | **GET** /api/appointment_profiles/{id} | 
*OpenapiJsClient.ClinicalApi* | [**appointmentProfilesUpdate**](docs/ClinicalApi.md#appointmentProfilesUpdate) | **PUT** /api/appointment_profiles/{id} | 
*OpenapiJsClient.ClinicalApi* | [**appointmentTemplatesCreate**](docs/ClinicalApi.md#appointmentTemplatesCreate) | **POST** /api/appointment_templates | 
*OpenapiJsClient.ClinicalApi* | [**appointmentTemplatesDelete**](docs/ClinicalApi.md#appointmentTemplatesDelete) | **DELETE** /api/appointment_templates/{id} | 
*OpenapiJsClient.ClinicalApi* | [**appointmentTemplatesList**](docs/ClinicalApi.md#appointmentTemplatesList) | **GET** /api/appointment_templates | 
*OpenapiJsClient.ClinicalApi* | [**appointmentTemplatesPartialUpdate**](docs/ClinicalApi.md#appointmentTemplatesPartialUpdate) | **PATCH** /api/appointment_templates/{id} | 
*OpenapiJsClient.ClinicalApi* | [**appointmentTemplatesRead**](docs/ClinicalApi.md#appointmentTemplatesRead) | **GET** /api/appointment_templates/{id} | 
*OpenapiJsClient.ClinicalApi* | [**appointmentTemplatesUpdate**](docs/ClinicalApi.md#appointmentTemplatesUpdate) | **PUT** /api/appointment_templates/{id} | 
*OpenapiJsClient.ClinicalApi* | [**appointmentsCreate**](docs/ClinicalApi.md#appointmentsCreate) | **POST** /api/appointments | 
*OpenapiJsClient.ClinicalApi* | [**appointmentsDelete**](docs/ClinicalApi.md#appointmentsDelete) | **DELETE** /api/appointments/{id} | 
*OpenapiJsClient.ClinicalApi* | [**appointmentsList**](docs/ClinicalApi.md#appointmentsList) | **GET** /api/appointments | 
*OpenapiJsClient.ClinicalApi* | [**appointmentsPartialUpdate**](docs/ClinicalApi.md#appointmentsPartialUpdate) | **PATCH** /api/appointments/{id} | 
*OpenapiJsClient.ClinicalApi* | [**appointmentsRead**](docs/ClinicalApi.md#appointmentsRead) | **GET** /api/appointments/{id} | 
*OpenapiJsClient.ClinicalApi* | [**appointmentsUpdate**](docs/ClinicalApi.md#appointmentsUpdate) | **PUT** /api/appointments/{id} | 
*OpenapiJsClient.ClinicalApi* | [**carePlansList**](docs/ClinicalApi.md#carePlansList) | **GET** /api/care_plans | 
*OpenapiJsClient.ClinicalApi* | [**carePlansRead**](docs/ClinicalApi.md#carePlansRead) | **GET** /api/care_plans/{id} | 
*OpenapiJsClient.ClinicalApi* | [**careTeamMembersList**](docs/ClinicalApi.md#careTeamMembersList) | **GET** /api/care_team_members | 
*OpenapiJsClient.ClinicalApi* | [**careTeamMembersRead**](docs/ClinicalApi.md#careTeamMembersRead) | **GET** /api/care_team_members/{id} | 
*OpenapiJsClient.ClinicalApi* | [**claimBillingNotesCreate**](docs/ClinicalApi.md#claimBillingNotesCreate) | **POST** /api/claim_billing_notes | 
*OpenapiJsClient.ClinicalApi* | [**claimBillingNotesList**](docs/ClinicalApi.md#claimBillingNotesList) | **GET** /api/claim_billing_notes | 
*OpenapiJsClient.ClinicalApi* | [**claimBillingNotesRead**](docs/ClinicalApi.md#claimBillingNotesRead) | **GET** /api/claim_billing_notes/{id} | 
*OpenapiJsClient.ClinicalApi* | [**clinicalNoteFieldTypesList**](docs/ClinicalApi.md#clinicalNoteFieldTypesList) | **GET** /api/clinical_note_field_types | 
*OpenapiJsClient.ClinicalApi* | [**clinicalNoteFieldTypesRead**](docs/ClinicalApi.md#clinicalNoteFieldTypesRead) | **GET** /api/clinical_note_field_types/{id} | 
*OpenapiJsClient.ClinicalApi* | [**clinicalNoteFieldValuesCreate**](docs/ClinicalApi.md#clinicalNoteFieldValuesCreate) | **POST** /api/clinical_note_field_values | 
*OpenapiJsClient.ClinicalApi* | [**clinicalNoteFieldValuesList**](docs/ClinicalApi.md#clinicalNoteFieldValuesList) | **GET** /api/clinical_note_field_values | 
*OpenapiJsClient.ClinicalApi* | [**clinicalNoteFieldValuesPartialUpdate**](docs/ClinicalApi.md#clinicalNoteFieldValuesPartialUpdate) | **PATCH** /api/clinical_note_field_values/{id} | 
*OpenapiJsClient.ClinicalApi* | [**clinicalNoteFieldValuesRead**](docs/ClinicalApi.md#clinicalNoteFieldValuesRead) | **GET** /api/clinical_note_field_values/{id} | 
*OpenapiJsClient.ClinicalApi* | [**clinicalNoteFieldValuesUpdate**](docs/ClinicalApi.md#clinicalNoteFieldValuesUpdate) | **PUT** /api/clinical_note_field_values/{id} | 
*OpenapiJsClient.ClinicalApi* | [**clinicalNoteTemplatesList**](docs/ClinicalApi.md#clinicalNoteTemplatesList) | **GET** /api/clinical_note_templates | 
*OpenapiJsClient.ClinicalApi* | [**clinicalNoteTemplatesRead**](docs/ClinicalApi.md#clinicalNoteTemplatesRead) | **GET** /api/clinical_note_templates/{id} | 
*OpenapiJsClient.ClinicalApi* | [**clinicalNotesList**](docs/ClinicalApi.md#clinicalNotesList) | **GET** /api/clinical_notes | 
*OpenapiJsClient.ClinicalApi* | [**clinicalNotesRead**](docs/ClinicalApi.md#clinicalNotesRead) | **GET** /api/clinical_notes/{id} | 
*OpenapiJsClient.ClinicalApi* | [**consentFormsApplyToAppointment**](docs/ClinicalApi.md#consentFormsApplyToAppointment) | **POST** /api/consent_forms/{id}/apply_to_appointment | 
*OpenapiJsClient.ClinicalApi* | [**consentFormsCreate**](docs/ClinicalApi.md#consentFormsCreate) | **POST** /api/consent_forms | 
*OpenapiJsClient.ClinicalApi* | [**consentFormsList**](docs/ClinicalApi.md#consentFormsList) | **GET** /api/consent_forms | 
*OpenapiJsClient.ClinicalApi* | [**consentFormsPartialUpdate**](docs/ClinicalApi.md#consentFormsPartialUpdate) | **PATCH** /api/consent_forms/{id} | 
*OpenapiJsClient.ClinicalApi* | [**consentFormsRead**](docs/ClinicalApi.md#consentFormsRead) | **GET** /api/consent_forms/{id} | 
*OpenapiJsClient.ClinicalApi* | [**consentFormsUnapplyFromAppointment**](docs/ClinicalApi.md#consentFormsUnapplyFromAppointment) | **POST** /api/consent_forms/{id}/unapply_from_appointment | 
*OpenapiJsClient.ClinicalApi* | [**consentFormsUpdate**](docs/ClinicalApi.md#consentFormsUpdate) | **PUT** /api/consent_forms/{id} | 
*OpenapiJsClient.ClinicalApi* | [**customAppointmentFieldsCreate**](docs/ClinicalApi.md#customAppointmentFieldsCreate) | **POST** /api/custom_appointment_fields | 
*OpenapiJsClient.ClinicalApi* | [**customAppointmentFieldsList**](docs/ClinicalApi.md#customAppointmentFieldsList) | **GET** /api/custom_appointment_fields | 
*OpenapiJsClient.ClinicalApi* | [**customAppointmentFieldsPartialUpdate**](docs/ClinicalApi.md#customAppointmentFieldsPartialUpdate) | **PATCH** /api/custom_appointment_fields/{id} | 
*OpenapiJsClient.ClinicalApi* | [**customAppointmentFieldsRead**](docs/ClinicalApi.md#customAppointmentFieldsRead) | **GET** /api/custom_appointment_fields/{id} | 
*OpenapiJsClient.ClinicalApi* | [**customAppointmentFieldsUpdate**](docs/ClinicalApi.md#customAppointmentFieldsUpdate) | **PUT** /api/custom_appointment_fields/{id} | 
*OpenapiJsClient.ClinicalApi* | [**customDemographicsCreate**](docs/ClinicalApi.md#customDemographicsCreate) | **POST** /api/custom_demographics | 
*OpenapiJsClient.ClinicalApi* | [**customDemographicsList**](docs/ClinicalApi.md#customDemographicsList) | **GET** /api/custom_demographics | 
*OpenapiJsClient.ClinicalApi* | [**customDemographicsPartialUpdate**](docs/ClinicalApi.md#customDemographicsPartialUpdate) | **PATCH** /api/custom_demographics/{id} | 
*OpenapiJsClient.ClinicalApi* | [**customDemographicsRead**](docs/ClinicalApi.md#customDemographicsRead) | **GET** /api/custom_demographics/{id} | 
*OpenapiJsClient.ClinicalApi* | [**customDemographicsUpdate**](docs/ClinicalApi.md#customDemographicsUpdate) | **PUT** /api/custom_demographics/{id} | 
*OpenapiJsClient.ClinicalApi* | [**customVitalsList**](docs/ClinicalApi.md#customVitalsList) | **GET** /api/custom_vitals | 
*OpenapiJsClient.ClinicalApi* | [**customVitalsRead**](docs/ClinicalApi.md#customVitalsRead) | **GET** /api/custom_vitals/{id} | 
*OpenapiJsClient.ClinicalApi* | [**documentsCreate**](docs/ClinicalApi.md#documentsCreate) | **POST** /api/documents | 
*OpenapiJsClient.ClinicalApi* | [**documentsDelete**](docs/ClinicalApi.md#documentsDelete) | **DELETE** /api/documents/{id} | 
*OpenapiJsClient.ClinicalApi* | [**documentsList**](docs/ClinicalApi.md#documentsList) | **GET** /api/documents | 
*OpenapiJsClient.ClinicalApi* | [**documentsPartialUpdate**](docs/ClinicalApi.md#documentsPartialUpdate) | **PATCH** /api/documents/{id} | 
*OpenapiJsClient.ClinicalApi* | [**documentsRead**](docs/ClinicalApi.md#documentsRead) | **GET** /api/documents/{id} | 
*OpenapiJsClient.ClinicalApi* | [**documentsUpdate**](docs/ClinicalApi.md#documentsUpdate) | **PUT** /api/documents/{id} | 
*OpenapiJsClient.ClinicalApi* | [**eobsCreate**](docs/ClinicalApi.md#eobsCreate) | **POST** /api/eobs | 
*OpenapiJsClient.ClinicalApi* | [**eobsList**](docs/ClinicalApi.md#eobsList) | **GET** /api/eobs | 
*OpenapiJsClient.ClinicalApi* | [**eobsRead**](docs/ClinicalApi.md#eobsRead) | **GET** /api/eobs/{id} | 
*OpenapiJsClient.ClinicalApi* | [**feeSchedulesList**](docs/ClinicalApi.md#feeSchedulesList) | **GET** /api/fee_schedules | 
*OpenapiJsClient.ClinicalApi* | [**feeSchedulesRead**](docs/ClinicalApi.md#feeSchedulesRead) | **GET** /api/fee_schedules/{id} | 
*OpenapiJsClient.ClinicalApi* | [**implantableDevicesList**](docs/ClinicalApi.md#implantableDevicesList) | **GET** /api/implantable_devices | 
*OpenapiJsClient.ClinicalApi* | [**implantableDevicesRead**](docs/ClinicalApi.md#implantableDevicesRead) | **GET** /api/implantable_devices/{id} | 
*OpenapiJsClient.ClinicalApi* | [**insurancesList**](docs/ClinicalApi.md#insurancesList) | **GET** /api/insurances | 
*OpenapiJsClient.ClinicalApi* | [**insurancesRead**](docs/ClinicalApi.md#insurancesRead) | **GET** /api/insurances/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labDocumentsCreate**](docs/ClinicalApi.md#labDocumentsCreate) | **POST** /api/lab_documents | 
*OpenapiJsClient.ClinicalApi* | [**labDocumentsDelete**](docs/ClinicalApi.md#labDocumentsDelete) | **DELETE** /api/lab_documents/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labDocumentsList**](docs/ClinicalApi.md#labDocumentsList) | **GET** /api/lab_documents | 
*OpenapiJsClient.ClinicalApi* | [**labDocumentsPartialUpdate**](docs/ClinicalApi.md#labDocumentsPartialUpdate) | **PATCH** /api/lab_documents/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labDocumentsRead**](docs/ClinicalApi.md#labDocumentsRead) | **GET** /api/lab_documents/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labDocumentsUpdate**](docs/ClinicalApi.md#labDocumentsUpdate) | **PUT** /api/lab_documents/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labOrdersCreate**](docs/ClinicalApi.md#labOrdersCreate) | **POST** /api/lab_orders | 
*OpenapiJsClient.ClinicalApi* | [**labOrdersDelete**](docs/ClinicalApi.md#labOrdersDelete) | **DELETE** /api/lab_orders/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labOrdersList**](docs/ClinicalApi.md#labOrdersList) | **GET** /api/lab_orders | 
*OpenapiJsClient.ClinicalApi* | [**labOrdersPartialUpdate**](docs/ClinicalApi.md#labOrdersPartialUpdate) | **PATCH** /api/lab_orders/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labOrdersRead**](docs/ClinicalApi.md#labOrdersRead) | **GET** /api/lab_orders/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labOrdersSummaryList**](docs/ClinicalApi.md#labOrdersSummaryList) | **GET** /api/lab_orders_summary | 
*OpenapiJsClient.ClinicalApi* | [**labOrdersSummaryRead**](docs/ClinicalApi.md#labOrdersSummaryRead) | **GET** /api/lab_orders_summary/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labOrdersUpdate**](docs/ClinicalApi.md#labOrdersUpdate) | **PUT** /api/lab_orders/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labResultsCreate**](docs/ClinicalApi.md#labResultsCreate) | **POST** /api/lab_results | 
*OpenapiJsClient.ClinicalApi* | [**labResultsDelete**](docs/ClinicalApi.md#labResultsDelete) | **DELETE** /api/lab_results/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labResultsList**](docs/ClinicalApi.md#labResultsList) | **GET** /api/lab_results | 
*OpenapiJsClient.ClinicalApi* | [**labResultsPartialUpdate**](docs/ClinicalApi.md#labResultsPartialUpdate) | **PATCH** /api/lab_results/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labResultsRead**](docs/ClinicalApi.md#labResultsRead) | **GET** /api/lab_results/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labResultsUpdate**](docs/ClinicalApi.md#labResultsUpdate) | **PUT** /api/lab_results/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labTestsCreate**](docs/ClinicalApi.md#labTestsCreate) | **POST** /api/lab_tests | 
*OpenapiJsClient.ClinicalApi* | [**labTestsDelete**](docs/ClinicalApi.md#labTestsDelete) | **DELETE** /api/lab_tests/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labTestsList**](docs/ClinicalApi.md#labTestsList) | **GET** /api/lab_tests | 
*OpenapiJsClient.ClinicalApi* | [**labTestsPartialUpdate**](docs/ClinicalApi.md#labTestsPartialUpdate) | **PATCH** /api/lab_tests/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labTestsRead**](docs/ClinicalApi.md#labTestsRead) | **GET** /api/lab_tests/{id} | 
*OpenapiJsClient.ClinicalApi* | [**labTestsUpdate**](docs/ClinicalApi.md#labTestsUpdate) | **PUT** /api/lab_tests/{id} | 
*OpenapiJsClient.ClinicalApi* | [**medicationsAppendToPharmacyNote**](docs/ClinicalApi.md#medicationsAppendToPharmacyNote) | **PATCH** /api/medications/{id}/append_to_pharmacy_note | 
*OpenapiJsClient.ClinicalApi* | [**medicationsCreate**](docs/ClinicalApi.md#medicationsCreate) | **POST** /api/medications | 
*OpenapiJsClient.ClinicalApi* | [**medicationsList**](docs/ClinicalApi.md#medicationsList) | **GET** /api/medications | 
*OpenapiJsClient.ClinicalApi* | [**medicationsPartialUpdate**](docs/ClinicalApi.md#medicationsPartialUpdate) | **PATCH** /api/medications/{id} | 
*OpenapiJsClient.ClinicalApi* | [**medicationsRead**](docs/ClinicalApi.md#medicationsRead) | **GET** /api/medications/{id} | 
*OpenapiJsClient.ClinicalApi* | [**medicationsUpdate**](docs/ClinicalApi.md#medicationsUpdate) | **PUT** /api/medications/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientCommunicationsCreate**](docs/ClinicalApi.md#patientCommunicationsCreate) | **POST** /api/patient_communications | 
*OpenapiJsClient.ClinicalApi* | [**patientCommunicationsList**](docs/ClinicalApi.md#patientCommunicationsList) | **GET** /api/patient_communications | 
*OpenapiJsClient.ClinicalApi* | [**patientCommunicationsPartialUpdate**](docs/ClinicalApi.md#patientCommunicationsPartialUpdate) | **PATCH** /api/patient_communications/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientCommunicationsRead**](docs/ClinicalApi.md#patientCommunicationsRead) | **GET** /api/patient_communications/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientCommunicationsUpdate**](docs/ClinicalApi.md#patientCommunicationsUpdate) | **PUT** /api/patient_communications/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientFlagTypesCreate**](docs/ClinicalApi.md#patientFlagTypesCreate) | **POST** /api/patient_flag_types | 
*OpenapiJsClient.ClinicalApi* | [**patientFlagTypesList**](docs/ClinicalApi.md#patientFlagTypesList) | **GET** /api/patient_flag_types | 
*OpenapiJsClient.ClinicalApi* | [**patientFlagTypesPartialUpdate**](docs/ClinicalApi.md#patientFlagTypesPartialUpdate) | **PATCH** /api/patient_flag_types/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientFlagTypesRead**](docs/ClinicalApi.md#patientFlagTypesRead) | **GET** /api/patient_flag_types/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientFlagTypesUpdate**](docs/ClinicalApi.md#patientFlagTypesUpdate) | **PUT** /api/patient_flag_types/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientInterventionsCreate**](docs/ClinicalApi.md#patientInterventionsCreate) | **POST** /api/patient_interventions | 
*OpenapiJsClient.ClinicalApi* | [**patientInterventionsList**](docs/ClinicalApi.md#patientInterventionsList) | **GET** /api/patient_interventions | 
*OpenapiJsClient.ClinicalApi* | [**patientInterventionsPartialUpdate**](docs/ClinicalApi.md#patientInterventionsPartialUpdate) | **PATCH** /api/patient_interventions/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientInterventionsRead**](docs/ClinicalApi.md#patientInterventionsRead) | **GET** /api/patient_interventions/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientInterventionsUpdate**](docs/ClinicalApi.md#patientInterventionsUpdate) | **PUT** /api/patient_interventions/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientLabResultsCreate**](docs/ClinicalApi.md#patientLabResultsCreate) | **POST** /api/patient_lab_results | 
*OpenapiJsClient.ClinicalApi* | [**patientLabResultsDelete**](docs/ClinicalApi.md#patientLabResultsDelete) | **DELETE** /api/patient_lab_results/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientLabResultsList**](docs/ClinicalApi.md#patientLabResultsList) | **GET** /api/patient_lab_results | 
*OpenapiJsClient.ClinicalApi* | [**patientLabResultsPartialUpdate**](docs/ClinicalApi.md#patientLabResultsPartialUpdate) | **PATCH** /api/patient_lab_results/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientLabResultsRead**](docs/ClinicalApi.md#patientLabResultsRead) | **GET** /api/patient_lab_results/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientLabResultsUpdate**](docs/ClinicalApi.md#patientLabResultsUpdate) | **PUT** /api/patient_lab_results/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientMessagesCreate**](docs/ClinicalApi.md#patientMessagesCreate) | **POST** /api/patient_messages | 
*OpenapiJsClient.ClinicalApi* | [**patientMessagesList**](docs/ClinicalApi.md#patientMessagesList) | **GET** /api/patient_messages | 
*OpenapiJsClient.ClinicalApi* | [**patientMessagesPartialUpdate**](docs/ClinicalApi.md#patientMessagesPartialUpdate) | **PATCH** /api/patient_messages/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientMessagesRead**](docs/ClinicalApi.md#patientMessagesRead) | **GET** /api/patient_messages/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientMessagesUpdate**](docs/ClinicalApi.md#patientMessagesUpdate) | **PUT** /api/patient_messages/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientPhysicalExamsCreate**](docs/ClinicalApi.md#patientPhysicalExamsCreate) | **POST** /api/patient_physical_exams | 
*OpenapiJsClient.ClinicalApi* | [**patientPhysicalExamsList**](docs/ClinicalApi.md#patientPhysicalExamsList) | **GET** /api/patient_physical_exams | 
*OpenapiJsClient.ClinicalApi* | [**patientPhysicalExamsPartialUpdate**](docs/ClinicalApi.md#patientPhysicalExamsPartialUpdate) | **PATCH** /api/patient_physical_exams/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientPhysicalExamsRead**](docs/ClinicalApi.md#patientPhysicalExamsRead) | **GET** /api/patient_physical_exams/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientPhysicalExamsUpdate**](docs/ClinicalApi.md#patientPhysicalExamsUpdate) | **PUT** /api/patient_physical_exams/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientRiskAssessmentsCreate**](docs/ClinicalApi.md#patientRiskAssessmentsCreate) | **POST** /api/patient_risk_assessments | 
*OpenapiJsClient.ClinicalApi* | [**patientRiskAssessmentsList**](docs/ClinicalApi.md#patientRiskAssessmentsList) | **GET** /api/patient_risk_assessments | 
*OpenapiJsClient.ClinicalApi* | [**patientRiskAssessmentsPartialUpdate**](docs/ClinicalApi.md#patientRiskAssessmentsPartialUpdate) | **PATCH** /api/patient_risk_assessments/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientRiskAssessmentsRead**](docs/ClinicalApi.md#patientRiskAssessmentsRead) | **GET** /api/patient_risk_assessments/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientRiskAssessmentsUpdate**](docs/ClinicalApi.md#patientRiskAssessmentsUpdate) | **PUT** /api/patient_risk_assessments/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientVaccineRecordsCreate**](docs/ClinicalApi.md#patientVaccineRecordsCreate) | **POST** /api/patient_vaccine_records | 
*OpenapiJsClient.ClinicalApi* | [**patientVaccineRecordsList**](docs/ClinicalApi.md#patientVaccineRecordsList) | **GET** /api/patient_vaccine_records | 
*OpenapiJsClient.ClinicalApi* | [**patientVaccineRecordsPartialUpdate**](docs/ClinicalApi.md#patientVaccineRecordsPartialUpdate) | **PATCH** /api/patient_vaccine_records/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientVaccineRecordsRead**](docs/ClinicalApi.md#patientVaccineRecordsRead) | **GET** /api/patient_vaccine_records/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientVaccineRecordsUpdate**](docs/ClinicalApi.md#patientVaccineRecordsUpdate) | **PUT** /api/patient_vaccine_records/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientsCcda**](docs/ClinicalApi.md#patientsCcda) | **GET** /api/patients/{id}/ccda | 
*OpenapiJsClient.ClinicalApi* | [**patientsCreate**](docs/ClinicalApi.md#patientsCreate) | **POST** /api/patients | 
*OpenapiJsClient.ClinicalApi* | [**patientsDelete**](docs/ClinicalApi.md#patientsDelete) | **DELETE** /api/patients/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientsList**](docs/ClinicalApi.md#patientsList) | **GET** /api/patients | 
*OpenapiJsClient.ClinicalApi* | [**patientsOnpatientAccessCreate**](docs/ClinicalApi.md#patientsOnpatientAccessCreate) | **POST** /api/patients/{id}/onpatient_access | 
*OpenapiJsClient.ClinicalApi* | [**patientsOnpatientAccessDelete**](docs/ClinicalApi.md#patientsOnpatientAccessDelete) | **DELETE** /api/patients/{id}/onpatient_access | 
*OpenapiJsClient.ClinicalApi* | [**patientsOnpatientAccessRead**](docs/ClinicalApi.md#patientsOnpatientAccessRead) | **GET** /api/patients/{id}/onpatient_access | 
*OpenapiJsClient.ClinicalApi* | [**patientsPartialUpdate**](docs/ClinicalApi.md#patientsPartialUpdate) | **PATCH** /api/patients/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientsQrda1**](docs/ClinicalApi.md#patientsQrda1) | **GET** /api/patients/{id}/qrda1 | 
*OpenapiJsClient.ClinicalApi* | [**patientsRead**](docs/ClinicalApi.md#patientsRead) | **GET** /api/patients/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientsSummaryCreate**](docs/ClinicalApi.md#patientsSummaryCreate) | **POST** /api/patients_summary | 
*OpenapiJsClient.ClinicalApi* | [**patientsSummaryDelete**](docs/ClinicalApi.md#patientsSummaryDelete) | **DELETE** /api/patients_summary/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientsSummaryList**](docs/ClinicalApi.md#patientsSummaryList) | **GET** /api/patients_summary | 
*OpenapiJsClient.ClinicalApi* | [**patientsSummaryPartialUpdate**](docs/ClinicalApi.md#patientsSummaryPartialUpdate) | **PATCH** /api/patients_summary/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientsSummaryRead**](docs/ClinicalApi.md#patientsSummaryRead) | **GET** /api/patients_summary/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientsSummaryUpdate**](docs/ClinicalApi.md#patientsSummaryUpdate) | **PUT** /api/patients_summary/{id} | 
*OpenapiJsClient.ClinicalApi* | [**patientsUpdate**](docs/ClinicalApi.md#patientsUpdate) | **PUT** /api/patients/{id} | 
*OpenapiJsClient.ClinicalApi* | [**prescriptionMessagesList**](docs/ClinicalApi.md#prescriptionMessagesList) | **GET** /api/prescription_messages | 
*OpenapiJsClient.ClinicalApi* | [**prescriptionMessagesRead**](docs/ClinicalApi.md#prescriptionMessagesRead) | **GET** /api/prescription_messages/{id} | 
*OpenapiJsClient.ClinicalApi* | [**problemsCreate**](docs/ClinicalApi.md#problemsCreate) | **POST** /api/problems | 
*OpenapiJsClient.ClinicalApi* | [**problemsList**](docs/ClinicalApi.md#problemsList) | **GET** /api/problems | 
*OpenapiJsClient.ClinicalApi* | [**problemsPartialUpdate**](docs/ClinicalApi.md#problemsPartialUpdate) | **PATCH** /api/problems/{id} | 
*OpenapiJsClient.ClinicalApi* | [**problemsRead**](docs/ClinicalApi.md#problemsRead) | **GET** /api/problems/{id} | 
*OpenapiJsClient.ClinicalApi* | [**problemsUpdate**](docs/ClinicalApi.md#problemsUpdate) | **PUT** /api/problems/{id} | 
*OpenapiJsClient.ClinicalApi* | [**reminderProfilesCreate**](docs/ClinicalApi.md#reminderProfilesCreate) | **POST** /api/reminder_profiles | 
*OpenapiJsClient.ClinicalApi* | [**reminderProfilesDelete**](docs/ClinicalApi.md#reminderProfilesDelete) | **DELETE** /api/reminder_profiles/{id} | 
*OpenapiJsClient.ClinicalApi* | [**reminderProfilesList**](docs/ClinicalApi.md#reminderProfilesList) | **GET** /api/reminder_profiles | 
*OpenapiJsClient.ClinicalApi* | [**reminderProfilesPartialUpdate**](docs/ClinicalApi.md#reminderProfilesPartialUpdate) | **PATCH** /api/reminder_profiles/{id} | 
*OpenapiJsClient.ClinicalApi* | [**reminderProfilesRead**](docs/ClinicalApi.md#reminderProfilesRead) | **GET** /api/reminder_profiles/{id} | 
*OpenapiJsClient.ClinicalApi* | [**reminderProfilesUpdate**](docs/ClinicalApi.md#reminderProfilesUpdate) | **PUT** /api/reminder_profiles/{id} | 
*OpenapiJsClient.ClinicalApi* | [**sublabsCreate**](docs/ClinicalApi.md#sublabsCreate) | **POST** /api/sublabs | 
*OpenapiJsClient.ClinicalApi* | [**sublabsDelete**](docs/ClinicalApi.md#sublabsDelete) | **DELETE** /api/sublabs/{id} | 
*OpenapiJsClient.ClinicalApi* | [**sublabsList**](docs/ClinicalApi.md#sublabsList) | **GET** /api/sublabs | 
*OpenapiJsClient.ClinicalApi* | [**sublabsPartialUpdate**](docs/ClinicalApi.md#sublabsPartialUpdate) | **PATCH** /api/sublabs/{id} | 
*OpenapiJsClient.ClinicalApi* | [**sublabsRead**](docs/ClinicalApi.md#sublabsRead) | **GET** /api/sublabs/{id} | 
*OpenapiJsClient.ClinicalApi* | [**sublabsUpdate**](docs/ClinicalApi.md#sublabsUpdate) | **PUT** /api/sublabs/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**inventoryCategoriesList**](docs/PracticeManagementApi.md#inventoryCategoriesList) | **GET** /api/inventory_categories | 
*OpenapiJsClient.PracticeManagementApi* | [**inventoryCategoriesRead**](docs/PracticeManagementApi.md#inventoryCategoriesRead) | **GET** /api/inventory_categories/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**inventoryVaccinesCreate**](docs/PracticeManagementApi.md#inventoryVaccinesCreate) | **POST** /api/inventory_vaccines | 
*OpenapiJsClient.PracticeManagementApi* | [**inventoryVaccinesList**](docs/PracticeManagementApi.md#inventoryVaccinesList) | **GET** /api/inventory_vaccines | 
*OpenapiJsClient.PracticeManagementApi* | [**inventoryVaccinesRead**](docs/PracticeManagementApi.md#inventoryVaccinesRead) | **GET** /api/inventory_vaccines/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**messagesCreate**](docs/PracticeManagementApi.md#messagesCreate) | **POST** /api/messages | 
*OpenapiJsClient.PracticeManagementApi* | [**messagesDelete**](docs/PracticeManagementApi.md#messagesDelete) | **DELETE** /api/messages/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**messagesList**](docs/PracticeManagementApi.md#messagesList) | **GET** /api/messages | 
*OpenapiJsClient.PracticeManagementApi* | [**messagesPartialUpdate**](docs/PracticeManagementApi.md#messagesPartialUpdate) | **PATCH** /api/messages/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**messagesRead**](docs/PracticeManagementApi.md#messagesRead) | **GET** /api/messages/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**messagesUpdate**](docs/PracticeManagementApi.md#messagesUpdate) | **PUT** /api/messages/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**officesAddExamRoom**](docs/PracticeManagementApi.md#officesAddExamRoom) | **POST** /api/offices/{id}/add_exam_room | 
*OpenapiJsClient.PracticeManagementApi* | [**officesList**](docs/PracticeManagementApi.md#officesList) | **GET** /api/offices | 
*OpenapiJsClient.PracticeManagementApi* | [**officesPartialUpdate**](docs/PracticeManagementApi.md#officesPartialUpdate) | **PATCH** /api/offices/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**officesRead**](docs/PracticeManagementApi.md#officesRead) | **GET** /api/offices/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**officesUpdate**](docs/PracticeManagementApi.md#officesUpdate) | **PUT** /api/offices/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**taskCategoriesCreate**](docs/PracticeManagementApi.md#taskCategoriesCreate) | **POST** /api/task_categories | 
*OpenapiJsClient.PracticeManagementApi* | [**taskCategoriesList**](docs/PracticeManagementApi.md#taskCategoriesList) | **GET** /api/task_categories | 
*OpenapiJsClient.PracticeManagementApi* | [**taskCategoriesPartialUpdate**](docs/PracticeManagementApi.md#taskCategoriesPartialUpdate) | **PATCH** /api/task_categories/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**taskCategoriesRead**](docs/PracticeManagementApi.md#taskCategoriesRead) | **GET** /api/task_categories/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**taskCategoriesUpdate**](docs/PracticeManagementApi.md#taskCategoriesUpdate) | **PUT** /api/task_categories/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**taskNotesCreate**](docs/PracticeManagementApi.md#taskNotesCreate) | **POST** /api/task_notes | 
*OpenapiJsClient.PracticeManagementApi* | [**taskNotesList**](docs/PracticeManagementApi.md#taskNotesList) | **GET** /api/task_notes | 
*OpenapiJsClient.PracticeManagementApi* | [**taskNotesPartialUpdate**](docs/PracticeManagementApi.md#taskNotesPartialUpdate) | **PATCH** /api/task_notes/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**taskNotesRead**](docs/PracticeManagementApi.md#taskNotesRead) | **GET** /api/task_notes/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**taskNotesUpdate**](docs/PracticeManagementApi.md#taskNotesUpdate) | **PUT** /api/task_notes/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**taskStatusesCreate**](docs/PracticeManagementApi.md#taskStatusesCreate) | **POST** /api/task_statuses | 
*OpenapiJsClient.PracticeManagementApi* | [**taskStatusesList**](docs/PracticeManagementApi.md#taskStatusesList) | **GET** /api/task_statuses | 
*OpenapiJsClient.PracticeManagementApi* | [**taskStatusesPartialUpdate**](docs/PracticeManagementApi.md#taskStatusesPartialUpdate) | **PATCH** /api/task_statuses/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**taskStatusesRead**](docs/PracticeManagementApi.md#taskStatusesRead) | **GET** /api/task_statuses/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**taskStatusesUpdate**](docs/PracticeManagementApi.md#taskStatusesUpdate) | **PUT** /api/task_statuses/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**taskTemplatesCreate**](docs/PracticeManagementApi.md#taskTemplatesCreate) | **POST** /api/task_templates | 
*OpenapiJsClient.PracticeManagementApi* | [**taskTemplatesList**](docs/PracticeManagementApi.md#taskTemplatesList) | **GET** /api/task_templates | 
*OpenapiJsClient.PracticeManagementApi* | [**taskTemplatesPartialUpdate**](docs/PracticeManagementApi.md#taskTemplatesPartialUpdate) | **PATCH** /api/task_templates/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**taskTemplatesRead**](docs/PracticeManagementApi.md#taskTemplatesRead) | **GET** /api/task_templates/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**taskTemplatesUpdate**](docs/PracticeManagementApi.md#taskTemplatesUpdate) | **PUT** /api/task_templates/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**tasksCreate**](docs/PracticeManagementApi.md#tasksCreate) | **POST** /api/tasks | 
*OpenapiJsClient.PracticeManagementApi* | [**tasksList**](docs/PracticeManagementApi.md#tasksList) | **GET** /api/tasks | 
*OpenapiJsClient.PracticeManagementApi* | [**tasksPartialUpdate**](docs/PracticeManagementApi.md#tasksPartialUpdate) | **PATCH** /api/tasks/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**tasksRead**](docs/PracticeManagementApi.md#tasksRead) | **GET** /api/tasks/{id} | 
*OpenapiJsClient.PracticeManagementApi* | [**tasksUpdate**](docs/PracticeManagementApi.md#tasksUpdate) | **PUT** /api/tasks/{id} | 


## Documentation for Models

 - [OpenapiJsClient.AllergiesList200Response](docs/AllergiesList200Response.md)
 - [OpenapiJsClient.AmendmentsList200Response](docs/AmendmentsList200Response.md)
 - [OpenapiJsClient.Appointment](docs/Appointment.md)
 - [OpenapiJsClient.AppointmentProfile](docs/AppointmentProfile.md)
 - [OpenapiJsClient.AppointmentProfilesList200Response](docs/AppointmentProfilesList200Response.md)
 - [OpenapiJsClient.AppointmentStatusTransition](docs/AppointmentStatusTransition.md)
 - [OpenapiJsClient.AppointmentTemplate](docs/AppointmentTemplate.md)
 - [OpenapiJsClient.AppointmentTemplatesList200Response](docs/AppointmentTemplatesList200Response.md)
 - [OpenapiJsClient.AppointmentsList200Response](docs/AppointmentsList200Response.md)
 - [OpenapiJsClient.AssociatedTaskItem](docs/AssociatedTaskItem.md)
 - [OpenapiJsClient.AutoAccidentInsurance](docs/AutoAccidentInsurance.md)
 - [OpenapiJsClient.BillingLineItem](docs/BillingLineItem.md)
 - [OpenapiJsClient.BillingProfile](docs/BillingProfile.md)
 - [OpenapiJsClient.BillingProfilesList200Response](docs/BillingProfilesList200Response.md)
 - [OpenapiJsClient.CarePlan](docs/CarePlan.md)
 - [OpenapiJsClient.CarePlansList200Response](docs/CarePlansList200Response.md)
 - [OpenapiJsClient.CareTeamMember](docs/CareTeamMember.md)
 - [OpenapiJsClient.CareTeamMembersList200Response](docs/CareTeamMembersList200Response.md)
 - [OpenapiJsClient.CashPayment](docs/CashPayment.md)
 - [OpenapiJsClient.CashPaymentLog](docs/CashPaymentLog.md)
 - [OpenapiJsClient.ClaimBillingNotes](docs/ClaimBillingNotes.md)
 - [OpenapiJsClient.ClaimBillingNotes1](docs/ClaimBillingNotes1.md)
 - [OpenapiJsClient.ClaimBillingNotesList200Response](docs/ClaimBillingNotesList200Response.md)
 - [OpenapiJsClient.ClinicalNote](docs/ClinicalNote.md)
 - [OpenapiJsClient.ClinicalNote1](docs/ClinicalNote1.md)
 - [OpenapiJsClient.ClinicalNoteField](docs/ClinicalNoteField.md)
 - [OpenapiJsClient.ClinicalNoteFieldTypesList200Response](docs/ClinicalNoteFieldTypesList200Response.md)
 - [OpenapiJsClient.ClinicalNoteFieldValuesList200Response](docs/ClinicalNoteFieldValuesList200Response.md)
 - [OpenapiJsClient.ClinicalNoteSection](docs/ClinicalNoteSection.md)
 - [OpenapiJsClient.ClinicalNoteTemplatesList200Response](docs/ClinicalNoteTemplatesList200Response.md)
 - [OpenapiJsClient.ClinicalNotesList200Response](docs/ClinicalNotesList200Response.md)
 - [OpenapiJsClient.CommLogsList200Response](docs/CommLogsList200Response.md)
 - [OpenapiJsClient.ConsentForm](docs/ConsentForm.md)
 - [OpenapiJsClient.ConsentFormsList200Response](docs/ConsentFormsList200Response.md)
 - [OpenapiJsClient.Coverage](docs/Coverage.md)
 - [OpenapiJsClient.CptCodesInner](docs/CptCodesInner.md)
 - [OpenapiJsClient.CustomAppointmentFieldType](docs/CustomAppointmentFieldType.md)
 - [OpenapiJsClient.CustomAppointmentFieldValue](docs/CustomAppointmentFieldValue.md)
 - [OpenapiJsClient.CustomAppointmentFieldsList200Response](docs/CustomAppointmentFieldsList200Response.md)
 - [OpenapiJsClient.CustomDemographicsList200Response](docs/CustomDemographicsList200Response.md)
 - [OpenapiJsClient.CustomInsurancePlanName](docs/CustomInsurancePlanName.md)
 - [OpenapiJsClient.CustomInsurancePlanNamesList200Response](docs/CustomInsurancePlanNamesList200Response.md)
 - [OpenapiJsClient.CustomPatientFieldType](docs/CustomPatientFieldType.md)
 - [OpenapiJsClient.CustomPatientFieldValue](docs/CustomPatientFieldValue.md)
 - [OpenapiJsClient.CustomProcedureCodesInner](docs/CustomProcedureCodesInner.md)
 - [OpenapiJsClient.CustomVitalType](docs/CustomVitalType.md)
 - [OpenapiJsClient.CustomVitalValue](docs/CustomVitalValue.md)
 - [OpenapiJsClient.CustomVitalsList200Response](docs/CustomVitalsList200Response.md)
 - [OpenapiJsClient.Doctor](docs/Doctor.md)
 - [OpenapiJsClient.DoctorFeeSchedule](docs/DoctorFeeSchedule.md)
 - [OpenapiJsClient.DoctorMessage](docs/DoctorMessage.md)
 - [OpenapiJsClient.DoctorsList200Response](docs/DoctorsList200Response.md)
 - [OpenapiJsClient.DocumentsList200Response](docs/DocumentsList200Response.md)
 - [OpenapiJsClient.EOBObject](docs/EOBObject.md)
 - [OpenapiJsClient.EligibilityChecksList200Response](docs/EligibilityChecksList200Response.md)
 - [OpenapiJsClient.EobsList200Response](docs/EobsList200Response.md)
 - [OpenapiJsClient.FeeSchedulesList200Response](docs/FeeSchedulesList200Response.md)
 - [OpenapiJsClient.HcpcsCodesInner](docs/HcpcsCodesInner.md)
 - [OpenapiJsClient.ICD10Code](docs/ICD10Code.md)
 - [OpenapiJsClient.ImplantableDevice](docs/ImplantableDevice.md)
 - [OpenapiJsClient.ImplantableDevicesList200Response](docs/ImplantableDevicesList200Response.md)
 - [OpenapiJsClient.Insurance](docs/Insurance.md)
 - [OpenapiJsClient.InsurancesList200Response](docs/InsurancesList200Response.md)
 - [OpenapiJsClient.InventoryCategoriesList200Response](docs/InventoryCategoriesList200Response.md)
 - [OpenapiJsClient.InventoryCategory](docs/InventoryCategory.md)
 - [OpenapiJsClient.InventoryVaccine](docs/InventoryVaccine.md)
 - [OpenapiJsClient.InventoryVaccinesList200Response](docs/InventoryVaccinesList200Response.md)
 - [OpenapiJsClient.LabDocumentsList200Response](docs/LabDocumentsList200Response.md)
 - [OpenapiJsClient.LabOrder](docs/LabOrder.md)
 - [OpenapiJsClient.LabOrderDocument](docs/LabOrderDocument.md)
 - [OpenapiJsClient.LabOrdersList200Response](docs/LabOrdersList200Response.md)
 - [OpenapiJsClient.LabResult](docs/LabResult.md)
 - [OpenapiJsClient.LabResultsList200Response](docs/LabResultsList200Response.md)
 - [OpenapiJsClient.LabTest](docs/LabTest.md)
 - [OpenapiJsClient.LabTestsList200Response](docs/LabTestsList200Response.md)
 - [OpenapiJsClient.LabVendorLocation](docs/LabVendorLocation.md)
 - [OpenapiJsClient.LineItemTransaction](docs/LineItemTransaction.md)
 - [OpenapiJsClient.LineItemsList200Response](docs/LineItemsList200Response.md)
 - [OpenapiJsClient.MedicationsList200Response](docs/MedicationsList200Response.md)
 - [OpenapiJsClient.MessageNote](docs/MessageNote.md)
 - [OpenapiJsClient.MessagesList200Response](docs/MessagesList200Response.md)
 - [OpenapiJsClient.NdcCodeInner](docs/NdcCodeInner.md)
 - [OpenapiJsClient.Office](docs/Office.md)
 - [OpenapiJsClient.OfficeOnlineHours](docs/OfficeOnlineHours.md)
 - [OpenapiJsClient.OfficesList200Response](docs/OfficesList200Response.md)
 - [OpenapiJsClient.OpenSlot](docs/OpenSlot.md)
 - [OpenapiJsClient.Patient](docs/Patient.md)
 - [OpenapiJsClient.Patient1](docs/Patient1.md)
 - [OpenapiJsClient.PatientAllergy](docs/PatientAllergy.md)
 - [OpenapiJsClient.PatientAmendment](docs/PatientAmendment.md)
 - [OpenapiJsClient.PatientCommunication](docs/PatientCommunication.md)
 - [OpenapiJsClient.PatientCommunicationsList200Response](docs/PatientCommunicationsList200Response.md)
 - [OpenapiJsClient.PatientDrug](docs/PatientDrug.md)
 - [OpenapiJsClient.PatientFlag](docs/PatientFlag.md)
 - [OpenapiJsClient.PatientFlagType](docs/PatientFlagType.md)
 - [OpenapiJsClient.PatientFlagType1](docs/PatientFlagType1.md)
 - [OpenapiJsClient.PatientFlagTypesList200Response](docs/PatientFlagTypesList200Response.md)
 - [OpenapiJsClient.PatientIntervention](docs/PatientIntervention.md)
 - [OpenapiJsClient.PatientInterventionsList200Response](docs/PatientInterventionsList200Response.md)
 - [OpenapiJsClient.PatientLabResultSet](docs/PatientLabResultSet.md)
 - [OpenapiJsClient.PatientLabResultsList200Response](docs/PatientLabResultsList200Response.md)
 - [OpenapiJsClient.PatientMessage](docs/PatientMessage.md)
 - [OpenapiJsClient.PatientMessageAttachment](docs/PatientMessageAttachment.md)
 - [OpenapiJsClient.PatientMessagesList200Response](docs/PatientMessagesList200Response.md)
 - [OpenapiJsClient.PatientPaymentLogList200Response](docs/PatientPaymentLogList200Response.md)
 - [OpenapiJsClient.PatientPaymentsList200Response](docs/PatientPaymentsList200Response.md)
 - [OpenapiJsClient.PatientPhysicalExam](docs/PatientPhysicalExam.md)
 - [OpenapiJsClient.PatientPhysicalExamsList200Response](docs/PatientPhysicalExamsList200Response.md)
 - [OpenapiJsClient.PatientProblem](docs/PatientProblem.md)
 - [OpenapiJsClient.PatientRiskAssessment](docs/PatientRiskAssessment.md)
 - [OpenapiJsClient.PatientRiskAssessmentsList200Response](docs/PatientRiskAssessmentsList200Response.md)
 - [OpenapiJsClient.PatientVaccineRecord](docs/PatientVaccineRecord.md)
 - [OpenapiJsClient.PatientVaccineRecordsList200Response](docs/PatientVaccineRecordsList200Response.md)
 - [OpenapiJsClient.PatientsList200Response](docs/PatientsList200Response.md)
 - [OpenapiJsClient.PhoneCallLog](docs/PhoneCallLog.md)
 - [OpenapiJsClient.PrescriptionMessage](docs/PrescriptionMessage.md)
 - [OpenapiJsClient.PrescriptionMessagesList200Response](docs/PrescriptionMessagesList200Response.md)
 - [OpenapiJsClient.PrimaryInsurance](docs/PrimaryInsurance.md)
 - [OpenapiJsClient.ProblemsList200Response](docs/ProblemsList200Response.md)
 - [OpenapiJsClient.ReminderProfile](docs/ReminderProfile.md)
 - [OpenapiJsClient.ReminderProfilesList200Response](docs/ReminderProfilesList200Response.md)
 - [OpenapiJsClient.ReminderTemplate](docs/ReminderTemplate.md)
 - [OpenapiJsClient.ScannedClinicalDocument](docs/ScannedClinicalDocument.md)
 - [OpenapiJsClient.SecondaryInsurance](docs/SecondaryInsurance.md)
 - [OpenapiJsClient.SimpleReminder](docs/SimpleReminder.md)
 - [OpenapiJsClient.SoapNoteCustomReport](docs/SoapNoteCustomReport.md)
 - [OpenapiJsClient.SoapNoteCustomReport1](docs/SoapNoteCustomReport1.md)
 - [OpenapiJsClient.SoapNoteLineItemFieldType](docs/SoapNoteLineItemFieldType.md)
 - [OpenapiJsClient.SoapNoteLineItemFieldValue](docs/SoapNoteLineItemFieldValue.md)
 - [OpenapiJsClient.SublabsList200Response](docs/SublabsList200Response.md)
 - [OpenapiJsClient.SystemVitals](docs/SystemVitals.md)
 - [OpenapiJsClient.Task](docs/Task.md)
 - [OpenapiJsClient.TaskCategoriesList200Response](docs/TaskCategoriesList200Response.md)
 - [OpenapiJsClient.TaskCategory](docs/TaskCategory.md)
 - [OpenapiJsClient.TaskNote](docs/TaskNote.md)
 - [OpenapiJsClient.TaskNote1](docs/TaskNote1.md)
 - [OpenapiJsClient.TaskNotesList200Response](docs/TaskNotesList200Response.md)
 - [OpenapiJsClient.TaskReminder](docs/TaskReminder.md)
 - [OpenapiJsClient.TaskStatus](docs/TaskStatus.md)
 - [OpenapiJsClient.TaskStatusesList200Response](docs/TaskStatusesList200Response.md)
 - [OpenapiJsClient.TaskTemplate](docs/TaskTemplate.md)
 - [OpenapiJsClient.TaskTemplatesList200Response](docs/TaskTemplatesList200Response.md)
 - [OpenapiJsClient.TasksList200Response](docs/TasksList200Response.md)
 - [OpenapiJsClient.TertiaryInsurance](docs/TertiaryInsurance.md)
 - [OpenapiJsClient.TransactionsList200Response](docs/TransactionsList200Response.md)
 - [OpenapiJsClient.UserGroupsList200Response](docs/UserGroupsList200Response.md)
 - [OpenapiJsClient.UserProfile](docs/UserProfile.md)
 - [OpenapiJsClient.UserProfilesGroup](docs/UserProfilesGroup.md)
 - [OpenapiJsClient.UsersList200Response](docs/UsersList200Response.md)
 - [OpenapiJsClient.VaccineDose](docs/VaccineDose.md)
 - [OpenapiJsClient.Value](docs/Value.md)
 - [OpenapiJsClient.WorkerCompInsurance](docs/WorkerCompInsurance.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### drchrono_oauth2


- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://drchrono.com/o/authorize/
- **Scopes**: 
  - billing:patient-payment:read: View patient payment information
  - billing:patient-payment:write: Modify patient payment information
  - billing:read: View billing information.
  - billing:write: Modify billing information.
  - calendar:read: View your appointments.
  - calendar:write: Schedule appointments and modify the data associated with them.
  - clinical:read: View clinical information, such as vitals, clinical notes, medications and diagnoses.
  - clinical:write: Create and modify clinical information, such as vitals, clinical notes, medications and diagnoses.
  - labs:read: View patient lab orders and results.
  - labs:write: Create and modify patient lab orders and results.
  - messages:read: View messages in your message center.
  - messages:write: Create and modify messages in your message center.
  - patients:read: View detailed patient information.
  - patients:summary:read: View summary information about your patients. This includes patients&#39; name, chart_id, age, and gender.
  - patients:summary:write: Create new patients and set their name, chart_id, age, and gender.
  - patients:write: Create patients and modify detailed patient information.
  - settings:read: View resources that requires Settings permission, such as custom fields.
  - settings:write: Create resources that requires Settings permission, such as custom fields.
  - tasks:read: View tasks in your tasks center
  - tasks:write: Create and modify tasks in your tasks center
  - user:read: View your basic information.
  - user:write: Edit select account information, such as creating new exam rooms.

