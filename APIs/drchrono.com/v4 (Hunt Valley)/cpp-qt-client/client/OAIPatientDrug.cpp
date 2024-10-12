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

#include "OAIPatientDrug.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientDrug::OAIPatientDrug(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientDrug::OAIPatientDrug() {
    this->initializeModel();
}

OAIPatientDrug::~OAIPatientDrug() {}

void OAIPatientDrug::initializeModel() {

    m_appointment_isSet = false;
    m_appointment_isValid = false;

    m_date_prescribed_isSet = false;
    m_date_prescribed_isValid = false;

    m_date_started_taking_isSet = false;
    m_date_started_taking_isValid = false;

    m_date_stopped_taking_isSet = false;
    m_date_stopped_taking_isValid = false;

    m_daw_isSet = false;
    m_daw_isValid = false;

    m_dispense_quantity_isSet = false;
    m_dispense_quantity_isValid = false;

    m_doctor_isSet = false;
    m_doctor_isValid = false;

    m_dosage_quantity_isSet = false;
    m_dosage_quantity_isValid = false;

    m_dosage_units_isSet = false;
    m_dosage_units_isValid = false;

    m_frequency_isSet = false;
    m_frequency_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_indication_isSet = false;
    m_indication_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_ndc_isSet = false;
    m_ndc_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_number_refills_isSet = false;
    m_number_refills_isValid = false;

    m_order_status_isSet = false;
    m_order_status_isValid = false;

    m_patient_isSet = false;
    m_patient_isValid = false;

    m_pharmacy_note_isSet = false;
    m_pharmacy_note_isValid = false;

    m_prn_isSet = false;
    m_prn_isValid = false;

    m_route_isSet = false;
    m_route_isValid = false;

    m_rxnorm_isSet = false;
    m_rxnorm_isValid = false;

    m_signature_note_isSet = false;
    m_signature_note_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIPatientDrug::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientDrug::fromJsonObject(QJsonObject json) {

    m_appointment_isValid = ::OpenAPI::fromJsonValue(m_appointment, json[QString("appointment")]);
    m_appointment_isSet = !json[QString("appointment")].isNull() && m_appointment_isValid;

    m_date_prescribed_isValid = ::OpenAPI::fromJsonValue(m_date_prescribed, json[QString("date_prescribed")]);
    m_date_prescribed_isSet = !json[QString("date_prescribed")].isNull() && m_date_prescribed_isValid;

    m_date_started_taking_isValid = ::OpenAPI::fromJsonValue(m_date_started_taking, json[QString("date_started_taking")]);
    m_date_started_taking_isSet = !json[QString("date_started_taking")].isNull() && m_date_started_taking_isValid;

    m_date_stopped_taking_isValid = ::OpenAPI::fromJsonValue(m_date_stopped_taking, json[QString("date_stopped_taking")]);
    m_date_stopped_taking_isSet = !json[QString("date_stopped_taking")].isNull() && m_date_stopped_taking_isValid;

    m_daw_isValid = ::OpenAPI::fromJsonValue(m_daw, json[QString("daw")]);
    m_daw_isSet = !json[QString("daw")].isNull() && m_daw_isValid;

    m_dispense_quantity_isValid = ::OpenAPI::fromJsonValue(m_dispense_quantity, json[QString("dispense_quantity")]);
    m_dispense_quantity_isSet = !json[QString("dispense_quantity")].isNull() && m_dispense_quantity_isValid;

    m_doctor_isValid = ::OpenAPI::fromJsonValue(m_doctor, json[QString("doctor")]);
    m_doctor_isSet = !json[QString("doctor")].isNull() && m_doctor_isValid;

    m_dosage_quantity_isValid = ::OpenAPI::fromJsonValue(m_dosage_quantity, json[QString("dosage_quantity")]);
    m_dosage_quantity_isSet = !json[QString("dosage_quantity")].isNull() && m_dosage_quantity_isValid;

    m_dosage_units_isValid = ::OpenAPI::fromJsonValue(m_dosage_units, json[QString("dosage_units")]);
    m_dosage_units_isSet = !json[QString("dosage_units")].isNull() && m_dosage_units_isValid;

    m_frequency_isValid = ::OpenAPI::fromJsonValue(m_frequency, json[QString("frequency")]);
    m_frequency_isSet = !json[QString("frequency")].isNull() && m_frequency_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_indication_isValid = ::OpenAPI::fromJsonValue(m_indication, json[QString("indication")]);
    m_indication_isSet = !json[QString("indication")].isNull() && m_indication_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_ndc_isValid = ::OpenAPI::fromJsonValue(m_ndc, json[QString("ndc")]);
    m_ndc_isSet = !json[QString("ndc")].isNull() && m_ndc_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_number_refills_isValid = ::OpenAPI::fromJsonValue(m_number_refills, json[QString("number_refills")]);
    m_number_refills_isSet = !json[QString("number_refills")].isNull() && m_number_refills_isValid;

    m_order_status_isValid = ::OpenAPI::fromJsonValue(m_order_status, json[QString("order_status")]);
    m_order_status_isSet = !json[QString("order_status")].isNull() && m_order_status_isValid;

    m_patient_isValid = ::OpenAPI::fromJsonValue(m_patient, json[QString("patient")]);
    m_patient_isSet = !json[QString("patient")].isNull() && m_patient_isValid;

    m_pharmacy_note_isValid = ::OpenAPI::fromJsonValue(m_pharmacy_note, json[QString("pharmacy_note")]);
    m_pharmacy_note_isSet = !json[QString("pharmacy_note")].isNull() && m_pharmacy_note_isValid;

    m_prn_isValid = ::OpenAPI::fromJsonValue(m_prn, json[QString("prn")]);
    m_prn_isSet = !json[QString("prn")].isNull() && m_prn_isValid;

    m_route_isValid = ::OpenAPI::fromJsonValue(m_route, json[QString("route")]);
    m_route_isSet = !json[QString("route")].isNull() && m_route_isValid;

    m_rxnorm_isValid = ::OpenAPI::fromJsonValue(m_rxnorm, json[QString("rxnorm")]);
    m_rxnorm_isSet = !json[QString("rxnorm")].isNull() && m_rxnorm_isValid;

    m_signature_note_isValid = ::OpenAPI::fromJsonValue(m_signature_note, json[QString("signature_note")]);
    m_signature_note_isSet = !json[QString("signature_note")].isNull() && m_signature_note_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIPatientDrug::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientDrug::asJsonObject() const {
    QJsonObject obj;
    if (m_appointment_isSet) {
        obj.insert(QString("appointment"), ::OpenAPI::toJsonValue(m_appointment));
    }
    if (m_date_prescribed_isSet) {
        obj.insert(QString("date_prescribed"), ::OpenAPI::toJsonValue(m_date_prescribed));
    }
    if (m_date_started_taking_isSet) {
        obj.insert(QString("date_started_taking"), ::OpenAPI::toJsonValue(m_date_started_taking));
    }
    if (m_date_stopped_taking_isSet) {
        obj.insert(QString("date_stopped_taking"), ::OpenAPI::toJsonValue(m_date_stopped_taking));
    }
    if (m_daw_isSet) {
        obj.insert(QString("daw"), ::OpenAPI::toJsonValue(m_daw));
    }
    if (m_dispense_quantity_isSet) {
        obj.insert(QString("dispense_quantity"), ::OpenAPI::toJsonValue(m_dispense_quantity));
    }
    if (m_doctor_isSet) {
        obj.insert(QString("doctor"), ::OpenAPI::toJsonValue(m_doctor));
    }
    if (m_dosage_quantity_isSet) {
        obj.insert(QString("dosage_quantity"), ::OpenAPI::toJsonValue(m_dosage_quantity));
    }
    if (m_dosage_units_isSet) {
        obj.insert(QString("dosage_units"), ::OpenAPI::toJsonValue(m_dosage_units));
    }
    if (m_frequency_isSet) {
        obj.insert(QString("frequency"), ::OpenAPI::toJsonValue(m_frequency));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_indication_isSet) {
        obj.insert(QString("indication"), ::OpenAPI::toJsonValue(m_indication));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_ndc_isSet) {
        obj.insert(QString("ndc"), ::OpenAPI::toJsonValue(m_ndc));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_number_refills_isSet) {
        obj.insert(QString("number_refills"), ::OpenAPI::toJsonValue(m_number_refills));
    }
    if (m_order_status_isSet) {
        obj.insert(QString("order_status"), ::OpenAPI::toJsonValue(m_order_status));
    }
    if (m_patient_isSet) {
        obj.insert(QString("patient"), ::OpenAPI::toJsonValue(m_patient));
    }
    if (m_pharmacy_note_isSet) {
        obj.insert(QString("pharmacy_note"), ::OpenAPI::toJsonValue(m_pharmacy_note));
    }
    if (m_prn_isSet) {
        obj.insert(QString("prn"), ::OpenAPI::toJsonValue(m_prn));
    }
    if (m_route_isSet) {
        obj.insert(QString("route"), ::OpenAPI::toJsonValue(m_route));
    }
    if (m_rxnorm_isSet) {
        obj.insert(QString("rxnorm"), ::OpenAPI::toJsonValue(m_rxnorm));
    }
    if (m_signature_note_isSet) {
        obj.insert(QString("signature_note"), ::OpenAPI::toJsonValue(m_signature_note));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

qint32 OAIPatientDrug::getAppointment() const {
    return m_appointment;
}
void OAIPatientDrug::setAppointment(const qint32 &appointment) {
    m_appointment = appointment;
    m_appointment_isSet = true;
}

bool OAIPatientDrug::is_appointment_Set() const{
    return m_appointment_isSet;
}

bool OAIPatientDrug::is_appointment_Valid() const{
    return m_appointment_isValid;
}

QString OAIPatientDrug::getDatePrescribed() const {
    return m_date_prescribed;
}
void OAIPatientDrug::setDatePrescribed(const QString &date_prescribed) {
    m_date_prescribed = date_prescribed;
    m_date_prescribed_isSet = true;
}

bool OAIPatientDrug::is_date_prescribed_Set() const{
    return m_date_prescribed_isSet;
}

bool OAIPatientDrug::is_date_prescribed_Valid() const{
    return m_date_prescribed_isValid;
}

QString OAIPatientDrug::getDateStartedTaking() const {
    return m_date_started_taking;
}
void OAIPatientDrug::setDateStartedTaking(const QString &date_started_taking) {
    m_date_started_taking = date_started_taking;
    m_date_started_taking_isSet = true;
}

bool OAIPatientDrug::is_date_started_taking_Set() const{
    return m_date_started_taking_isSet;
}

bool OAIPatientDrug::is_date_started_taking_Valid() const{
    return m_date_started_taking_isValid;
}

QString OAIPatientDrug::getDateStoppedTaking() const {
    return m_date_stopped_taking;
}
void OAIPatientDrug::setDateStoppedTaking(const QString &date_stopped_taking) {
    m_date_stopped_taking = date_stopped_taking;
    m_date_stopped_taking_isSet = true;
}

bool OAIPatientDrug::is_date_stopped_taking_Set() const{
    return m_date_stopped_taking_isSet;
}

bool OAIPatientDrug::is_date_stopped_taking_Valid() const{
    return m_date_stopped_taking_isValid;
}

bool OAIPatientDrug::isDaw() const {
    return m_daw;
}
void OAIPatientDrug::setDaw(const bool &daw) {
    m_daw = daw;
    m_daw_isSet = true;
}

bool OAIPatientDrug::is_daw_Set() const{
    return m_daw_isSet;
}

bool OAIPatientDrug::is_daw_Valid() const{
    return m_daw_isValid;
}

double OAIPatientDrug::getDispenseQuantity() const {
    return m_dispense_quantity;
}
void OAIPatientDrug::setDispenseQuantity(const double &dispense_quantity) {
    m_dispense_quantity = dispense_quantity;
    m_dispense_quantity_isSet = true;
}

bool OAIPatientDrug::is_dispense_quantity_Set() const{
    return m_dispense_quantity_isSet;
}

bool OAIPatientDrug::is_dispense_quantity_Valid() const{
    return m_dispense_quantity_isValid;
}

qint32 OAIPatientDrug::getDoctor() const {
    return m_doctor;
}
void OAIPatientDrug::setDoctor(const qint32 &doctor) {
    m_doctor = doctor;
    m_doctor_isSet = true;
}

bool OAIPatientDrug::is_doctor_Set() const{
    return m_doctor_isSet;
}

bool OAIPatientDrug::is_doctor_Valid() const{
    return m_doctor_isValid;
}

QString OAIPatientDrug::getDosageQuantity() const {
    return m_dosage_quantity;
}
void OAIPatientDrug::setDosageQuantity(const QString &dosage_quantity) {
    m_dosage_quantity = dosage_quantity;
    m_dosage_quantity_isSet = true;
}

bool OAIPatientDrug::is_dosage_quantity_Set() const{
    return m_dosage_quantity_isSet;
}

bool OAIPatientDrug::is_dosage_quantity_Valid() const{
    return m_dosage_quantity_isValid;
}

QString OAIPatientDrug::getDosageUnits() const {
    return m_dosage_units;
}
void OAIPatientDrug::setDosageUnits(const QString &dosage_units) {
    m_dosage_units = dosage_units;
    m_dosage_units_isSet = true;
}

bool OAIPatientDrug::is_dosage_units_Set() const{
    return m_dosage_units_isSet;
}

bool OAIPatientDrug::is_dosage_units_Valid() const{
    return m_dosage_units_isValid;
}

QString OAIPatientDrug::getFrequency() const {
    return m_frequency;
}
void OAIPatientDrug::setFrequency(const QString &frequency) {
    m_frequency = frequency;
    m_frequency_isSet = true;
}

bool OAIPatientDrug::is_frequency_Set() const{
    return m_frequency_isSet;
}

bool OAIPatientDrug::is_frequency_Valid() const{
    return m_frequency_isValid;
}

qint32 OAIPatientDrug::getId() const {
    return m_id;
}
void OAIPatientDrug::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPatientDrug::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPatientDrug::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIPatientDrug::getIndication() const {
    return m_indication;
}
void OAIPatientDrug::setIndication(const QString &indication) {
    m_indication = indication;
    m_indication_isSet = true;
}

bool OAIPatientDrug::is_indication_Set() const{
    return m_indication_isSet;
}

bool OAIPatientDrug::is_indication_Valid() const{
    return m_indication_isValid;
}

QString OAIPatientDrug::getName() const {
    return m_name;
}
void OAIPatientDrug::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPatientDrug::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPatientDrug::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIPatientDrug::getNdc() const {
    return m_ndc;
}
void OAIPatientDrug::setNdc(const QString &ndc) {
    m_ndc = ndc;
    m_ndc_isSet = true;
}

bool OAIPatientDrug::is_ndc_Set() const{
    return m_ndc_isSet;
}

bool OAIPatientDrug::is_ndc_Valid() const{
    return m_ndc_isValid;
}

QString OAIPatientDrug::getNotes() const {
    return m_notes;
}
void OAIPatientDrug::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIPatientDrug::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIPatientDrug::is_notes_Valid() const{
    return m_notes_isValid;
}

qint32 OAIPatientDrug::getNumberRefills() const {
    return m_number_refills;
}
void OAIPatientDrug::setNumberRefills(const qint32 &number_refills) {
    m_number_refills = number_refills;
    m_number_refills_isSet = true;
}

bool OAIPatientDrug::is_number_refills_Set() const{
    return m_number_refills_isSet;
}

bool OAIPatientDrug::is_number_refills_Valid() const{
    return m_number_refills_isValid;
}

QString OAIPatientDrug::getOrderStatus() const {
    return m_order_status;
}
void OAIPatientDrug::setOrderStatus(const QString &order_status) {
    m_order_status = order_status;
    m_order_status_isSet = true;
}

bool OAIPatientDrug::is_order_status_Set() const{
    return m_order_status_isSet;
}

bool OAIPatientDrug::is_order_status_Valid() const{
    return m_order_status_isValid;
}

qint32 OAIPatientDrug::getPatient() const {
    return m_patient;
}
void OAIPatientDrug::setPatient(const qint32 &patient) {
    m_patient = patient;
    m_patient_isSet = true;
}

bool OAIPatientDrug::is_patient_Set() const{
    return m_patient_isSet;
}

bool OAIPatientDrug::is_patient_Valid() const{
    return m_patient_isValid;
}

QString OAIPatientDrug::getPharmacyNote() const {
    return m_pharmacy_note;
}
void OAIPatientDrug::setPharmacyNote(const QString &pharmacy_note) {
    m_pharmacy_note = pharmacy_note;
    m_pharmacy_note_isSet = true;
}

bool OAIPatientDrug::is_pharmacy_note_Set() const{
    return m_pharmacy_note_isSet;
}

bool OAIPatientDrug::is_pharmacy_note_Valid() const{
    return m_pharmacy_note_isValid;
}

bool OAIPatientDrug::isPrn() const {
    return m_prn;
}
void OAIPatientDrug::setPrn(const bool &prn) {
    m_prn = prn;
    m_prn_isSet = true;
}

bool OAIPatientDrug::is_prn_Set() const{
    return m_prn_isSet;
}

bool OAIPatientDrug::is_prn_Valid() const{
    return m_prn_isValid;
}

QString OAIPatientDrug::getRoute() const {
    return m_route;
}
void OAIPatientDrug::setRoute(const QString &route) {
    m_route = route;
    m_route_isSet = true;
}

bool OAIPatientDrug::is_route_Set() const{
    return m_route_isSet;
}

bool OAIPatientDrug::is_route_Valid() const{
    return m_route_isValid;
}

QString OAIPatientDrug::getRxnorm() const {
    return m_rxnorm;
}
void OAIPatientDrug::setRxnorm(const QString &rxnorm) {
    m_rxnorm = rxnorm;
    m_rxnorm_isSet = true;
}

bool OAIPatientDrug::is_rxnorm_Set() const{
    return m_rxnorm_isSet;
}

bool OAIPatientDrug::is_rxnorm_Valid() const{
    return m_rxnorm_isValid;
}

QString OAIPatientDrug::getSignatureNote() const {
    return m_signature_note;
}
void OAIPatientDrug::setSignatureNote(const QString &signature_note) {
    m_signature_note = signature_note;
    m_signature_note_isSet = true;
}

bool OAIPatientDrug::is_signature_note_Set() const{
    return m_signature_note_isSet;
}

bool OAIPatientDrug::is_signature_note_Valid() const{
    return m_signature_note_isValid;
}

QString OAIPatientDrug::getStatus() const {
    return m_status;
}
void OAIPatientDrug::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIPatientDrug::is_status_Set() const{
    return m_status_isSet;
}

bool OAIPatientDrug::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIPatientDrug::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_appointment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_prescribed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_started_taking_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_stopped_taking_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_daw_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dispense_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_doctor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dosage_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dosage_units_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_frequency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_indication_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ndc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_refills_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pharmacy_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_prn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_route_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rxnorm_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_signature_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientDrug::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_doctor_isValid && m_patient_isValid && true;
}

} // namespace OpenAPI
