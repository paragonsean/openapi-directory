/**
 * 
 * This document is intended as a detailed reference for the precise behavior of the drchrono API. If this is your first time using the API, start with our <a href=\"/api-docs-old/tutorial\">tutorial</a>. If you are upgrading from a previous version, take a look at the changelog section.  # Authorization  ## Initial authorization  There are three main steps in the OAuth 2.0 authentication workflow:  1. Redirect the provider to the authorization page. 2. The provider authorizes your application and is redirected back to    your web application. 3. Your application exchanges the `authorization_code` that came with    the redirect for an `access_token` and `refresh_token`.  ### Step 1: Redirect to drchrono  The first step is redirecting your user to drchrono, typically with a button labeled \"Connect to drchrono\" or \"Login with drchrono\".  This is just a link that takes your user to the following URL:      https://drchrono.com/o/authorize/?redirect_uri=REDIRECT_URI_ENCODED&response_type=code&client_id=CLIENT_ID_ENCODED&scope=SCOPES_ENCODED  - `REDIRECT_URI_ENCODED` is the URL-encoded version of the redirect URI (as registered for your application and used in later steps). - `CLIENT_ID_ENCODED` is the URL-encoded version of your application's client ID. - `SCOPES_ENCODED` is a URL-encoded version of a space-separated list of scopes, which can be found in each endpoint or omitted to default to all scopes.  The `scope` parameter consists of an optional, space-separated list of scopes your application is requesting. If omitted, all scopes will be requested.  Scopes are of the form `BASE_SCOPE:[read|write]` where `BASE_SCOPE` is any of `user`, `calendar`, `patients`, `patients:summary`, `billing`, `clinical` and `labs`. You should request only the scopes you need. For instance, an application which sends \"Happy Birthday!\" emails to a doctor's patients on their birthdays would use the scope parameter `\"patients:summary:read\"`, while one that allows patients to schedule appointments online would need at least `\"patients:summary:read patients:summary:write calendar:read calendar:write clinical:read clinical:write\"`.  ### Step 2: Provider authorization  After logging in (if necessary), the provider will be presented with a screen with your application's name and the list of permissions you requested (via the `scope` parameter).  When they click the \"Authorize\" button, they will be redirected to your redirect URI with a `code` query parameter appended, which contains an authorization code to be used in step 3.  If they click the \"Cancel\" button, they will be redirected to your redirect URI with `error=access_denied` instead.  Note: This authorization code expires extremely quickly, so you must perform step 3 immediately, ideally before rendering the resulting page for the end user.  ### Step 3: Token exchange  The `code` obtained from step 2 is usable exactly once to obtain an access token and refresh token.  Here is an example token exchange in Python:      import datetime, pytz, requests      if 'error' in get_params:         raise ValueError('Error authorizing application: %s' % get_params[error])      response = requests.post('https://drchrono.com/o/token/', data={         'code': get_params['code'],         'grant_type': 'authorization_code',         'redirect_uri': 'http://mytestapp.com/redirect_uri',         'client_id': 'abcdefg12345',         'client_secret': 'abcdefg12345',     })     response.raise_for_status()     data = response.json()      # Save these in your database associated with the user     access_token = data['access_token']     refresh_token = data['refresh_token']     expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])  You now have all you need to make API requests authenticated as that provider. When using this access token, you'll only be able to access the data that the user has access to and that you have been granted permissions for.  ## Refreshing an access token  Access tokens only last 48 hours (given in seconds in the `'expires_in'` key in the token exchange step above), so they occasionally need to be refreshed.  It would be inconvenient to ask the user to re-authorize every time, so instead you can use the refresh token like the original authorization to obtain a new access token.  Replace the `code` parameter with `refresh_token`, change the value `grant_type` from `authorization_code` to `refresh_token`, and omit the `redirect_uri` parameter.  Example in Python:      ...     response = requests.post('https://drchrono.com/o/token/', data={         'refresh_token': get_refresh_token(),         'grant_type': 'refresh_token',         'client_id': 'abcdefg12345',         'client_secret': 'abcdefg12345',     })     ...  # Webhooks  In order to use drchrono API webhooks, you first need to have an API application on file (even if it is in Test Model). Each API webhook is associated with one API application, go to <a href=\"/api-management/\" target=\"_blank\">here</a> to set up both API applications and webhooks!  Once you registered an API application, you will see webhook section in each saved API applications. Create a webhook and register some events there and save all the changes, then you are good to go!  ## Webhooks setup  All fields under webhooks section are required.  **Callback URL** Callback URl is used to receive all hooks when subscribed events are triggered. This should be an URL under your control.  **Secret token** Secret token is used to verify webhooks, this is very important, please set something with high entropy. Also we will talk more about this later.  **Events**  Events is used to register events you want to receiver notification when they happen. Currently we support following events.  Event name | Event description ---------- | ----------------- `APPOINTMENT_CREATE` | We will deliver a hook any time an appointment is created `APPOINTMENT_MODIFY` | We will deliver a hook any time an appointment is modified `PATIENT_CREATE` | We will deliver a hook any time a patient is created `PATIENT_MODIFY` | We will deliver a hook any time a patient is modified `PATIENT_PROBLEM_CREATE` | We will deliver a hook any time a patient problem is created `PATIENT_PROBLEM_MODIFY` | We will deliver a hook any time a patient problem is modified `PATIENT_ALLERGY_CREATE` | We will deliver a hook any time a patient allergy is created `PATIENT_ALLERGY_MODIFY` | We will deliver a hook any time a patient allergy is modified `PATIENT_MEDICATION_CREATE` | We will deliver a hook any time a patient medication is created `PATIENT_MEDICATION_MODIFY` | We will deliver a hook any time a patient medication is modified `CLINICAL_NOTE_LOCK` | We will deliver a hook any time a clinical note is locked `CLINICAL_NOTE_UNLOCK` | We will deliver a hook any time a clinical note is unlocked `TASK_CREATE` | We will deliver a hook any time a task is created `TASK_MODIFY` | We will deliver a hook any time a task is modified and any time creation, modification and deletion of task notes, associated task item `TASK_DELETE` | We will deliver a hook any time a task is deleted   ## Webhooks verification  In order to make sure the callback URL in webhook is under your control, we added a verification step before we send any hooks out to you.  Verification can be done by clicking \"Verify webhook\" button in webhooks setup page. After you click the button, we will send a `GET` request to the callback URL, along with a parameter called `msg`.  Please use your webhook's secret token as hash key and SHA-256 as digest constructor, hash the `msg` value with <a href=\"https://tools.ietf.org/html/rfc2104.html\">HMAC algorithm</a>. And we expect a `200` JSON response, in JSON response body, there should be a key called `secret_token` existing, and its value should be equal to the <strong>hashed</strong> `msg`. Otherwise, verification will fail.  Here is an example webhook verification in Python:      import hashlib, hmac      def webhook_verify(request):         secret_token = hmac.new(WEBHOOK_SECRET_TOKEN, request.GET['msg'], hashlib.sha256).hexdigest()         return json_response({             'secret_token': secret_token         })  <div class=\"alert alert-warning\"> <b>Note:</b> Verification will be needed when webhook is first created and anytime callback URl is changed. </div>   ## Webhooks header and body  **Header**  Key | Value --- | ----- `X-drchrono-event` | Event that triggered this hook, could be any one event above or `PING` `X-drchrono-signature` | Secret token associated with this webhook `X-drchrono-delivery` | ID of this delivery  **Body**  Key | Value --- | ----- `receiver` | This will be an JSON representation of the webhook `object` | This will be an JSON representation of the object related to the triggered event, this would share same serializer as drchrono API  ## Webhooks ping and deliveries  Webhooks ping and deliveries will be sent as `POST` requests.  **PING**:  You can always ping your webhook to check things, by clicking the \"Ping webhook\" button in webhook setup page. And a hook with header `X-drchrono-event: PING` would be sent to the callback URL.  **Deliveries**:  You can check recent deliveries by clicking the \"deliveries\" link in webhook setup page. And you can resend a hook by clicking \"redeliver\" button after select a specific delivery.  ## Webhooks delivery mechanism  We will delivery a hook the moment a subscribed event is triggered. We will not record any response header or body you send back after you receive the hook. However we only consider the response status code. We will consider any `2xx` responses as successfully delivered. Any other responses, like `302` would be considered failing. And we will try to redeliver unsuccessfully delivered hooks 3 times, first redeliver happens at 1 hour after the initial event, second receliver happens 3 hours after the initial event, and the third redeliver happens 7 hours after the initial event. After these redeliveries, if the delivery is still unsuccessful, you have to redeliver it by hand.   ## Webhooks security  You may want to secure your webhooks to only consider requests send out from drchrono. And this is where <code>secret_token</code> is needed in request header. Try to set the <code>secret_token</code> to something with high entropy, a good example could be taking the output of <code>ruby -rsecurerandom -e 'puts SecureRandom.hex(20)'</code>. After this, you might want to verify all request headers you received on your server with this token.   # iframe integration  Some API apps provide additional functionality for interacting with patient data not offered by drchrono, and can benefit by being incorporated into drchrono's patient information page via iframe.  We have created a simple API to make this possible.  To make an existing API application accessible via an iframe on the patient page, you need to update either \"Patient iframe\" or \"Clinical note iframe\" section in API management page, to make the iframe to appear on (either the patient page or the clinical note page), with the URL that the iframe will use for each page, and the height it should have. The application will be reviewed before it is approved to ensure that it is functional and secure.  ## Register a Doctor  iframe applications will appear as choices on the left-hand menu of the patient page for doctors registered with your application.  To register a doctor with your application, make a `POST` request to the `/api/iframe_integration` endpoint using the access token for the corresponding doctor. This endpoint does not expect any payload.  To disable your iframe application for a doctor, make a `DELETE` request to the same endpoint.  ## Populating the iframe  There are two places where the iframe can be displayed, either within the patient detail page or the clinical note page, shown below respectively:  <img src=\"{% asset 'public/images/iframe_patient_page.png' %}\" alt=\"Iframe on the patient page\"/>  <img src=\"{% asset 'public/images/iframe_clinical_note.png' %}\" alt=\"Iframe on the clinical note page\"/>  When requesting approval for your iframe app, you must specify a URL for one or both of these pages which will serve as the base URL for your IFrame contents. When a doctor views your iframe, the source URL will have various query parameters appended to it, for example for the patient page the `src` parameter of the IFrame will be:  ``` <iframe_url>?doctor_id=<doctor_id>&patient_id=<patient_id>&practice_id=<practice_id>&iat=<iat>&jwt=<jwt> ```  The `jwt` parameter is crucial if your application transfers any sort of PHI and does not implement its own login system.  It encapsulates the other parameters in a [JSON web token (JWT)](http://jwt.io) and signs them using SHA-256 HMAC with your `client_secret` as the key.  This verifies that the iframe is being loaded within one of drchrono's pages by an authorized user.  In production, you should validate the JWT using an approved library (which are listed on the [official site](http://jwt.io)), and only use the parameters extracted from the JWT.  Using Python and Django, this might look like:      import jwt      CLIENT_SECRET = <client_secret>     MAX_TIME_DRIFT_SECONDS = 60      def validate_parameters(request):         token = request.GET['jwt']          return jwt.decode(token, CLIENT_SECRET, algorithms=['HS256'], leeway=MAX_TIME_DRIFT_SECONDS)  Modern browsers' same-origin policy means that data cannot be passed between your application and drchrono's page through the iframe.  Therefore, interaction must happen through the API, using information provided in JWT.  # Versions and deprecation  ## Stability Policy  Changes to this API version will be limited to adding endpoints, or adding fields to existing endpoints, or adding optional query parameters. Any new fields which are not read-only will be optional.  ## Deprecation Policy  The drchrono API is versioned. Versions can be in the following states:  * **Active:** This is our latest and greatest version of the API. It is actively supported by our API team and is improved upon with new features, bug fixes and optimizations that do not break backwards compatibility.  * **Deprecated:** A deprecated API version is considered second best--having been surpassed by our active API version. An API version remains in this state for one year, after which time it falls to the not supported state. A deprecated API version is passively supported; while it won't be removed until becoming unsupported, it may not receive new features but will likely be subject to security updates and performance improvements.  * **Unsupported:** An API version in the not supported state may be deactivated at any time. An application using an unsupported API version should migrate to an active API version.  ## Version Map | Version Name | Previous Name | Start Date | Deprecation Date | |--------------|---------------|------------|------------------| | v2           | v2015_08      | 08/2015    | TBA              | | v3           | v2016_06      | 06/2016    |                  | | v4           | N/A           | 09/2018    |                  |  If you are looking for documentation for an older version  - [V4(Hunt Valley)](/api-docs-old/v4/documentation) (old V4 documentation) - [V3(Sunnyvale)](/api-docs-old/v3/documentation) - [V2(Mountain View)](/api-docs-old/v2/documentation)  # Changelog  Here's changelog for different versions  - [V4 Changelog](/api-docs-old/v4/changelog) - [V3 changelog](/api-docs-old/v3/changelog)  
 *
 * The version of the OpenAPI document: v4 (Hunt Valley)
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBillingLineItem.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBillingLineItem::OAIBillingLineItem(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBillingLineItem::OAIBillingLineItem() {
    this->initializeModel();
}

OAIBillingLineItem::~OAIBillingLineItem() {}

void OAIBillingLineItem::initializeModel() {

    m_adjustment_isSet = false;
    m_adjustment_isValid = false;

    m_allowed_isSet = false;
    m_allowed_isValid = false;

    m_appointment_isSet = false;
    m_appointment_isValid = false;

    m_balance_ins_isSet = false;
    m_balance_ins_isValid = false;

    m_balance_pt_isSet = false;
    m_balance_pt_isValid = false;

    m_balance_total_isSet = false;
    m_balance_total_isValid = false;

    m_billed_isSet = false;
    m_billed_isValid = false;

    m_billing_status_isSet = false;
    m_billing_status_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;

    m_denied_flag_isSet = false;
    m_denied_flag_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_diagnosis_pointers_isSet = false;
    m_diagnosis_pointers_isValid = false;

    m_doctor_isSet = false;
    m_doctor_isValid = false;

    m_expected_reimbursement_isSet = false;
    m_expected_reimbursement_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_ins1_paid_isSet = false;
    m_ins1_paid_isValid = false;

    m_ins2_paid_isSet = false;
    m_ins2_paid_isValid = false;

    m_ins3_paid_isSet = false;
    m_ins3_paid_isValid = false;

    m_ins_total_isSet = false;
    m_ins_total_isValid = false;

    m_insurance_status_isSet = false;
    m_insurance_status_isValid = false;

    m_modifiers_isSet = false;
    m_modifiers_isValid = false;

    m_paid_total_isSet = false;
    m_paid_total_isValid = false;

    m_patient_isSet = false;
    m_patient_isValid = false;

    m_posted_date_isSet = false;
    m_posted_date_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_procedure_type_isSet = false;
    m_procedure_type_isValid = false;

    m_pt_paid_isSet = false;
    m_pt_paid_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_service_date_isSet = false;
    m_service_date_isValid = false;

    m_units_isSet = false;
    m_units_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;
}

void OAIBillingLineItem::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBillingLineItem::fromJsonObject(QJsonObject json) {

    m_adjustment_isValid = ::OpenAPI::fromJsonValue(m_adjustment, json[QString("adjustment")]);
    m_adjustment_isSet = !json[QString("adjustment")].isNull() && m_adjustment_isValid;

    m_allowed_isValid = ::OpenAPI::fromJsonValue(m_allowed, json[QString("allowed")]);
    m_allowed_isSet = !json[QString("allowed")].isNull() && m_allowed_isValid;

    m_appointment_isValid = ::OpenAPI::fromJsonValue(m_appointment, json[QString("appointment")]);
    m_appointment_isSet = !json[QString("appointment")].isNull() && m_appointment_isValid;

    m_balance_ins_isValid = ::OpenAPI::fromJsonValue(m_balance_ins, json[QString("balance_ins")]);
    m_balance_ins_isSet = !json[QString("balance_ins")].isNull() && m_balance_ins_isValid;

    m_balance_pt_isValid = ::OpenAPI::fromJsonValue(m_balance_pt, json[QString("balance_pt")]);
    m_balance_pt_isSet = !json[QString("balance_pt")].isNull() && m_balance_pt_isValid;

    m_balance_total_isValid = ::OpenAPI::fromJsonValue(m_balance_total, json[QString("balance_total")]);
    m_balance_total_isSet = !json[QString("balance_total")].isNull() && m_balance_total_isValid;

    m_billed_isValid = ::OpenAPI::fromJsonValue(m_billed, json[QString("billed")]);
    m_billed_isSet = !json[QString("billed")].isNull() && m_billed_isValid;

    m_billing_status_isValid = ::OpenAPI::fromJsonValue(m_billing_status, json[QString("billing_status")]);
    m_billing_status_isSet = !json[QString("billing_status")].isNull() && m_billing_status_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_denied_flag_isValid = ::OpenAPI::fromJsonValue(m_denied_flag, json[QString("denied_flag")]);
    m_denied_flag_isSet = !json[QString("denied_flag")].isNull() && m_denied_flag_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_diagnosis_pointers_isValid = ::OpenAPI::fromJsonValue(m_diagnosis_pointers, json[QString("diagnosis_pointers")]);
    m_diagnosis_pointers_isSet = !json[QString("diagnosis_pointers")].isNull() && m_diagnosis_pointers_isValid;

    m_doctor_isValid = ::OpenAPI::fromJsonValue(m_doctor, json[QString("doctor")]);
    m_doctor_isSet = !json[QString("doctor")].isNull() && m_doctor_isValid;

    m_expected_reimbursement_isValid = ::OpenAPI::fromJsonValue(m_expected_reimbursement, json[QString("expected_reimbursement")]);
    m_expected_reimbursement_isSet = !json[QString("expected_reimbursement")].isNull() && m_expected_reimbursement_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_ins1_paid_isValid = ::OpenAPI::fromJsonValue(m_ins1_paid, json[QString("ins1_paid")]);
    m_ins1_paid_isSet = !json[QString("ins1_paid")].isNull() && m_ins1_paid_isValid;

    m_ins2_paid_isValid = ::OpenAPI::fromJsonValue(m_ins2_paid, json[QString("ins2_paid")]);
    m_ins2_paid_isSet = !json[QString("ins2_paid")].isNull() && m_ins2_paid_isValid;

    m_ins3_paid_isValid = ::OpenAPI::fromJsonValue(m_ins3_paid, json[QString("ins3_paid")]);
    m_ins3_paid_isSet = !json[QString("ins3_paid")].isNull() && m_ins3_paid_isValid;

    m_ins_total_isValid = ::OpenAPI::fromJsonValue(m_ins_total, json[QString("ins_total")]);
    m_ins_total_isSet = !json[QString("ins_total")].isNull() && m_ins_total_isValid;

    m_insurance_status_isValid = ::OpenAPI::fromJsonValue(m_insurance_status, json[QString("insurance_status")]);
    m_insurance_status_isSet = !json[QString("insurance_status")].isNull() && m_insurance_status_isValid;

    m_modifiers_isValid = ::OpenAPI::fromJsonValue(m_modifiers, json[QString("modifiers")]);
    m_modifiers_isSet = !json[QString("modifiers")].isNull() && m_modifiers_isValid;

    m_paid_total_isValid = ::OpenAPI::fromJsonValue(m_paid_total, json[QString("paid_total")]);
    m_paid_total_isSet = !json[QString("paid_total")].isNull() && m_paid_total_isValid;

    m_patient_isValid = ::OpenAPI::fromJsonValue(m_patient, json[QString("patient")]);
    m_patient_isSet = !json[QString("patient")].isNull() && m_patient_isValid;

    m_posted_date_isValid = ::OpenAPI::fromJsonValue(m_posted_date, json[QString("posted_date")]);
    m_posted_date_isSet = !json[QString("posted_date")].isNull() && m_posted_date_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_procedure_type_isValid = ::OpenAPI::fromJsonValue(m_procedure_type, json[QString("procedure_type")]);
    m_procedure_type_isSet = !json[QString("procedure_type")].isNull() && m_procedure_type_isValid;

    m_pt_paid_isValid = ::OpenAPI::fromJsonValue(m_pt_paid, json[QString("pt_paid")]);
    m_pt_paid_isSet = !json[QString("pt_paid")].isNull() && m_pt_paid_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;

    m_service_date_isValid = ::OpenAPI::fromJsonValue(m_service_date, json[QString("service_date")]);
    m_service_date_isSet = !json[QString("service_date")].isNull() && m_service_date_isValid;

    m_units_isValid = ::OpenAPI::fromJsonValue(m_units, json[QString("units")]);
    m_units_isSet = !json[QString("units")].isNull() && m_units_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;
}

QString OAIBillingLineItem::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBillingLineItem::asJsonObject() const {
    QJsonObject obj;
    if (m_adjustment_isSet) {
        obj.insert(QString("adjustment"), ::OpenAPI::toJsonValue(m_adjustment));
    }
    if (m_allowed_isSet) {
        obj.insert(QString("allowed"), ::OpenAPI::toJsonValue(m_allowed));
    }
    if (m_appointment_isSet) {
        obj.insert(QString("appointment"), ::OpenAPI::toJsonValue(m_appointment));
    }
    if (m_balance_ins_isSet) {
        obj.insert(QString("balance_ins"), ::OpenAPI::toJsonValue(m_balance_ins));
    }
    if (m_balance_pt_isSet) {
        obj.insert(QString("balance_pt"), ::OpenAPI::toJsonValue(m_balance_pt));
    }
    if (m_balance_total_isSet) {
        obj.insert(QString("balance_total"), ::OpenAPI::toJsonValue(m_balance_total));
    }
    if (m_billed_isSet) {
        obj.insert(QString("billed"), ::OpenAPI::toJsonValue(m_billed));
    }
    if (m_billing_status_isSet) {
        obj.insert(QString("billing_status"), ::OpenAPI::toJsonValue(m_billing_status));
    }
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_denied_flag_isSet) {
        obj.insert(QString("denied_flag"), ::OpenAPI::toJsonValue(m_denied_flag));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_diagnosis_pointers.size() > 0) {
        obj.insert(QString("diagnosis_pointers"), ::OpenAPI::toJsonValue(m_diagnosis_pointers));
    }
    if (m_doctor_isSet) {
        obj.insert(QString("doctor"), ::OpenAPI::toJsonValue(m_doctor));
    }
    if (m_expected_reimbursement_isSet) {
        obj.insert(QString("expected_reimbursement"), ::OpenAPI::toJsonValue(m_expected_reimbursement));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_ins1_paid_isSet) {
        obj.insert(QString("ins1_paid"), ::OpenAPI::toJsonValue(m_ins1_paid));
    }
    if (m_ins2_paid_isSet) {
        obj.insert(QString("ins2_paid"), ::OpenAPI::toJsonValue(m_ins2_paid));
    }
    if (m_ins3_paid_isSet) {
        obj.insert(QString("ins3_paid"), ::OpenAPI::toJsonValue(m_ins3_paid));
    }
    if (m_ins_total_isSet) {
        obj.insert(QString("ins_total"), ::OpenAPI::toJsonValue(m_ins_total));
    }
    if (m_insurance_status_isSet) {
        obj.insert(QString("insurance_status"), ::OpenAPI::toJsonValue(m_insurance_status));
    }
    if (m_modifiers.size() > 0) {
        obj.insert(QString("modifiers"), ::OpenAPI::toJsonValue(m_modifiers));
    }
    if (m_paid_total_isSet) {
        obj.insert(QString("paid_total"), ::OpenAPI::toJsonValue(m_paid_total));
    }
    if (m_patient_isSet) {
        obj.insert(QString("patient"), ::OpenAPI::toJsonValue(m_patient));
    }
    if (m_posted_date_isSet) {
        obj.insert(QString("posted_date"), ::OpenAPI::toJsonValue(m_posted_date));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_procedure_type_isSet) {
        obj.insert(QString("procedure_type"), ::OpenAPI::toJsonValue(m_procedure_type));
    }
    if (m_pt_paid_isSet) {
        obj.insert(QString("pt_paid"), ::OpenAPI::toJsonValue(m_pt_paid));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_service_date_isSet) {
        obj.insert(QString("service_date"), ::OpenAPI::toJsonValue(m_service_date));
    }
    if (m_units_isSet) {
        obj.insert(QString("units"), ::OpenAPI::toJsonValue(m_units));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    return obj;
}

double OAIBillingLineItem::getAdjustment() const {
    return m_adjustment;
}
void OAIBillingLineItem::setAdjustment(const double &adjustment) {
    m_adjustment = adjustment;
    m_adjustment_isSet = true;
}

bool OAIBillingLineItem::is_adjustment_Set() const{
    return m_adjustment_isSet;
}

bool OAIBillingLineItem::is_adjustment_Valid() const{
    return m_adjustment_isValid;
}

double OAIBillingLineItem::getAllowed() const {
    return m_allowed;
}
void OAIBillingLineItem::setAllowed(const double &allowed) {
    m_allowed = allowed;
    m_allowed_isSet = true;
}

bool OAIBillingLineItem::is_allowed_Set() const{
    return m_allowed_isSet;
}

bool OAIBillingLineItem::is_allowed_Valid() const{
    return m_allowed_isValid;
}

qint32 OAIBillingLineItem::getAppointment() const {
    return m_appointment;
}
void OAIBillingLineItem::setAppointment(const qint32 &appointment) {
    m_appointment = appointment;
    m_appointment_isSet = true;
}

bool OAIBillingLineItem::is_appointment_Set() const{
    return m_appointment_isSet;
}

bool OAIBillingLineItem::is_appointment_Valid() const{
    return m_appointment_isValid;
}

double OAIBillingLineItem::getBalanceIns() const {
    return m_balance_ins;
}
void OAIBillingLineItem::setBalanceIns(const double &balance_ins) {
    m_balance_ins = balance_ins;
    m_balance_ins_isSet = true;
}

bool OAIBillingLineItem::is_balance_ins_Set() const{
    return m_balance_ins_isSet;
}

bool OAIBillingLineItem::is_balance_ins_Valid() const{
    return m_balance_ins_isValid;
}

double OAIBillingLineItem::getBalancePt() const {
    return m_balance_pt;
}
void OAIBillingLineItem::setBalancePt(const double &balance_pt) {
    m_balance_pt = balance_pt;
    m_balance_pt_isSet = true;
}

bool OAIBillingLineItem::is_balance_pt_Set() const{
    return m_balance_pt_isSet;
}

bool OAIBillingLineItem::is_balance_pt_Valid() const{
    return m_balance_pt_isValid;
}

QString OAIBillingLineItem::getBalanceTotal() const {
    return m_balance_total;
}
void OAIBillingLineItem::setBalanceTotal(const QString &balance_total) {
    m_balance_total = balance_total;
    m_balance_total_isSet = true;
}

bool OAIBillingLineItem::is_balance_total_Set() const{
    return m_balance_total_isSet;
}

bool OAIBillingLineItem::is_balance_total_Valid() const{
    return m_balance_total_isValid;
}

double OAIBillingLineItem::getBilled() const {
    return m_billed;
}
void OAIBillingLineItem::setBilled(const double &billed) {
    m_billed = billed;
    m_billed_isSet = true;
}

bool OAIBillingLineItem::is_billed_Set() const{
    return m_billed_isSet;
}

bool OAIBillingLineItem::is_billed_Valid() const{
    return m_billed_isValid;
}

QString OAIBillingLineItem::getBillingStatus() const {
    return m_billing_status;
}
void OAIBillingLineItem::setBillingStatus(const QString &billing_status) {
    m_billing_status = billing_status;
    m_billing_status_isSet = true;
}

bool OAIBillingLineItem::is_billing_status_Set() const{
    return m_billing_status_isSet;
}

bool OAIBillingLineItem::is_billing_status_Valid() const{
    return m_billing_status_isValid;
}

QString OAIBillingLineItem::getCode() const {
    return m_code;
}
void OAIBillingLineItem::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIBillingLineItem::is_code_Set() const{
    return m_code_isSet;
}

bool OAIBillingLineItem::is_code_Valid() const{
    return m_code_isValid;
}

bool OAIBillingLineItem::isDeniedFlag() const {
    return m_denied_flag;
}
void OAIBillingLineItem::setDeniedFlag(const bool &denied_flag) {
    m_denied_flag = denied_flag;
    m_denied_flag_isSet = true;
}

bool OAIBillingLineItem::is_denied_flag_Set() const{
    return m_denied_flag_isSet;
}

bool OAIBillingLineItem::is_denied_flag_Valid() const{
    return m_denied_flag_isValid;
}

QString OAIBillingLineItem::getDescription() const {
    return m_description;
}
void OAIBillingLineItem::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIBillingLineItem::is_description_Set() const{
    return m_description_isSet;
}

bool OAIBillingLineItem::is_description_Valid() const{
    return m_description_isValid;
}

QList<QString> OAIBillingLineItem::getDiagnosisPointers() const {
    return m_diagnosis_pointers;
}
void OAIBillingLineItem::setDiagnosisPointers(const QList<QString> &diagnosis_pointers) {
    m_diagnosis_pointers = diagnosis_pointers;
    m_diagnosis_pointers_isSet = true;
}

bool OAIBillingLineItem::is_diagnosis_pointers_Set() const{
    return m_diagnosis_pointers_isSet;
}

bool OAIBillingLineItem::is_diagnosis_pointers_Valid() const{
    return m_diagnosis_pointers_isValid;
}

QString OAIBillingLineItem::getDoctor() const {
    return m_doctor;
}
void OAIBillingLineItem::setDoctor(const QString &doctor) {
    m_doctor = doctor;
    m_doctor_isSet = true;
}

bool OAIBillingLineItem::is_doctor_Set() const{
    return m_doctor_isSet;
}

bool OAIBillingLineItem::is_doctor_Valid() const{
    return m_doctor_isValid;
}

double OAIBillingLineItem::getExpectedReimbursement() const {
    return m_expected_reimbursement;
}
void OAIBillingLineItem::setExpectedReimbursement(const double &expected_reimbursement) {
    m_expected_reimbursement = expected_reimbursement;
    m_expected_reimbursement_isSet = true;
}

bool OAIBillingLineItem::is_expected_reimbursement_Set() const{
    return m_expected_reimbursement_isSet;
}

bool OAIBillingLineItem::is_expected_reimbursement_Valid() const{
    return m_expected_reimbursement_isValid;
}

qint32 OAIBillingLineItem::getId() const {
    return m_id;
}
void OAIBillingLineItem::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIBillingLineItem::is_id_Set() const{
    return m_id_isSet;
}

bool OAIBillingLineItem::is_id_Valid() const{
    return m_id_isValid;
}

double OAIBillingLineItem::getIns1Paid() const {
    return m_ins1_paid;
}
void OAIBillingLineItem::setIns1Paid(const double &ins1_paid) {
    m_ins1_paid = ins1_paid;
    m_ins1_paid_isSet = true;
}

bool OAIBillingLineItem::is_ins1_paid_Set() const{
    return m_ins1_paid_isSet;
}

bool OAIBillingLineItem::is_ins1_paid_Valid() const{
    return m_ins1_paid_isValid;
}

double OAIBillingLineItem::getIns2Paid() const {
    return m_ins2_paid;
}
void OAIBillingLineItem::setIns2Paid(const double &ins2_paid) {
    m_ins2_paid = ins2_paid;
    m_ins2_paid_isSet = true;
}

bool OAIBillingLineItem::is_ins2_paid_Set() const{
    return m_ins2_paid_isSet;
}

bool OAIBillingLineItem::is_ins2_paid_Valid() const{
    return m_ins2_paid_isValid;
}

double OAIBillingLineItem::getIns3Paid() const {
    return m_ins3_paid;
}
void OAIBillingLineItem::setIns3Paid(const double &ins3_paid) {
    m_ins3_paid = ins3_paid;
    m_ins3_paid_isSet = true;
}

bool OAIBillingLineItem::is_ins3_paid_Set() const{
    return m_ins3_paid_isSet;
}

bool OAIBillingLineItem::is_ins3_paid_Valid() const{
    return m_ins3_paid_isValid;
}

QString OAIBillingLineItem::getInsTotal() const {
    return m_ins_total;
}
void OAIBillingLineItem::setInsTotal(const QString &ins_total) {
    m_ins_total = ins_total;
    m_ins_total_isSet = true;
}

bool OAIBillingLineItem::is_ins_total_Set() const{
    return m_ins_total_isSet;
}

bool OAIBillingLineItem::is_ins_total_Valid() const{
    return m_ins_total_isValid;
}

QString OAIBillingLineItem::getInsuranceStatus() const {
    return m_insurance_status;
}
void OAIBillingLineItem::setInsuranceStatus(const QString &insurance_status) {
    m_insurance_status = insurance_status;
    m_insurance_status_isSet = true;
}

bool OAIBillingLineItem::is_insurance_status_Set() const{
    return m_insurance_status_isSet;
}

bool OAIBillingLineItem::is_insurance_status_Valid() const{
    return m_insurance_status_isValid;
}

QList<QString> OAIBillingLineItem::getModifiers() const {
    return m_modifiers;
}
void OAIBillingLineItem::setModifiers(const QList<QString> &modifiers) {
    m_modifiers = modifiers;
    m_modifiers_isSet = true;
}

bool OAIBillingLineItem::is_modifiers_Set() const{
    return m_modifiers_isSet;
}

bool OAIBillingLineItem::is_modifiers_Valid() const{
    return m_modifiers_isValid;
}

QString OAIBillingLineItem::getPaidTotal() const {
    return m_paid_total;
}
void OAIBillingLineItem::setPaidTotal(const QString &paid_total) {
    m_paid_total = paid_total;
    m_paid_total_isSet = true;
}

bool OAIBillingLineItem::is_paid_total_Set() const{
    return m_paid_total_isSet;
}

bool OAIBillingLineItem::is_paid_total_Valid() const{
    return m_paid_total_isValid;
}

QString OAIBillingLineItem::getPatient() const {
    return m_patient;
}
void OAIBillingLineItem::setPatient(const QString &patient) {
    m_patient = patient;
    m_patient_isSet = true;
}

bool OAIBillingLineItem::is_patient_Set() const{
    return m_patient_isSet;
}

bool OAIBillingLineItem::is_patient_Valid() const{
    return m_patient_isValid;
}

QString OAIBillingLineItem::getPostedDate() const {
    return m_posted_date;
}
void OAIBillingLineItem::setPostedDate(const QString &posted_date) {
    m_posted_date = posted_date;
    m_posted_date_isSet = true;
}

bool OAIBillingLineItem::is_posted_date_Set() const{
    return m_posted_date_isSet;
}

bool OAIBillingLineItem::is_posted_date_Valid() const{
    return m_posted_date_isValid;
}

double OAIBillingLineItem::getPrice() const {
    return m_price;
}
void OAIBillingLineItem::setPrice(const double &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAIBillingLineItem::is_price_Set() const{
    return m_price_isSet;
}

bool OAIBillingLineItem::is_price_Valid() const{
    return m_price_isValid;
}

QString OAIBillingLineItem::getProcedureType() const {
    return m_procedure_type;
}
void OAIBillingLineItem::setProcedureType(const QString &procedure_type) {
    m_procedure_type = procedure_type;
    m_procedure_type_isSet = true;
}

bool OAIBillingLineItem::is_procedure_type_Set() const{
    return m_procedure_type_isSet;
}

bool OAIBillingLineItem::is_procedure_type_Valid() const{
    return m_procedure_type_isValid;
}

double OAIBillingLineItem::getPtPaid() const {
    return m_pt_paid;
}
void OAIBillingLineItem::setPtPaid(const double &pt_paid) {
    m_pt_paid = pt_paid;
    m_pt_paid_isSet = true;
}

bool OAIBillingLineItem::is_pt_paid_Set() const{
    return m_pt_paid_isSet;
}

bool OAIBillingLineItem::is_pt_paid_Valid() const{
    return m_pt_paid_isValid;
}

double OAIBillingLineItem::getQuantity() const {
    return m_quantity;
}
void OAIBillingLineItem::setQuantity(const double &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAIBillingLineItem::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAIBillingLineItem::is_quantity_Valid() const{
    return m_quantity_isValid;
}

QString OAIBillingLineItem::getServiceDate() const {
    return m_service_date;
}
void OAIBillingLineItem::setServiceDate(const QString &service_date) {
    m_service_date = service_date;
    m_service_date_isSet = true;
}

bool OAIBillingLineItem::is_service_date_Set() const{
    return m_service_date_isSet;
}

bool OAIBillingLineItem::is_service_date_Valid() const{
    return m_service_date_isValid;
}

QString OAIBillingLineItem::getUnits() const {
    return m_units;
}
void OAIBillingLineItem::setUnits(const QString &units) {
    m_units = units;
    m_units_isSet = true;
}

bool OAIBillingLineItem::is_units_Set() const{
    return m_units_isSet;
}

bool OAIBillingLineItem::is_units_Valid() const{
    return m_units_isValid;
}

QString OAIBillingLineItem::getUpdatedAt() const {
    return m_updated_at;
}
void OAIBillingLineItem::setUpdatedAt(const QString &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIBillingLineItem::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIBillingLineItem::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

bool OAIBillingLineItem::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_adjustment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_allowed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_appointment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_balance_ins_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_balance_pt_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_balance_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_billed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_denied_flag_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_diagnosis_pointers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_doctor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expected_reimbursement_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ins1_paid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ins2_paid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ins3_paid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ins_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_insurance_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modifiers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_paid_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_posted_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_procedure_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pt_paid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_units_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBillingLineItem::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_appointment_isValid && m_code_isValid && m_diagnosis_pointers_isValid && m_procedure_type_isValid && true;
}

} // namespace OpenAPI
