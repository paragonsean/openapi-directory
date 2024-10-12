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

#ifndef OAI_OAIClinicalApi_H
#define OAI_OAIClinicalApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAllergies_list_200_response.h"
#include "OAIAmendments_list_200_response.h"
#include "OAIAppointment.h"
#include "OAIAppointmentProfile.h"
#include "OAIAppointmentTemplate.h"
#include "OAIAppointment_profiles_list_200_response.h"
#include "OAIAppointment_templates_list_200_response.h"
#include "OAIAppointments_list_200_response.h"
#include "OAICarePlan.h"
#include "OAICareTeamMember.h"
#include "OAICare_plans_list_200_response.h"
#include "OAICare_team_members_list_200_response.h"
#include "OAIClaimBillingNotes.h"
#include "OAIClaim_billing_notes_list_200_response.h"
#include "OAIClinicalNote.h"
#include "OAIClinical_note_field_types_list_200_response.h"
#include "OAIClinical_note_field_values_list_200_response.h"
#include "OAIClinical_note_templates_list_200_response.h"
#include "OAIClinical_notes_list_200_response.h"
#include "OAIConsentForm.h"
#include "OAIConsent_forms_list_200_response.h"
#include "OAICustomAppointmentFieldType.h"
#include "OAICustomPatientFieldType.h"
#include "OAICustomVitalType.h"
#include "OAICustom_appointment_fields_list_200_response.h"
#include "OAICustom_demographics_list_200_response.h"
#include "OAICustom_vitals_list_200_response.h"
#include "OAIDoctorFeeSchedule.h"
#include "OAIDocuments_list_200_response.h"
#include "OAIEOBObject.h"
#include "OAIEobs_list_200_response.h"
#include "OAIFee_schedules_list_200_response.h"
#include "OAIImplantableDevice.h"
#include "OAIImplantable_devices_list_200_response.h"
#include "OAIInsurance.h"
#include "OAIInsurances_list_200_response.h"
#include "OAILabOrder.h"
#include "OAILabOrderDocument.h"
#include "OAILabResult.h"
#include "OAILabTest.h"
#include "OAILabVendorLocation.h"
#include "OAILab_documents_list_200_response.h"
#include "OAILab_orders_list_200_response.h"
#include "OAILab_results_list_200_response.h"
#include "OAILab_tests_list_200_response.h"
#include "OAIMedications_list_200_response.h"
#include "OAIObject.h"
#include "OAIPatient.h"
#include "OAIPatientAllergy.h"
#include "OAIPatientAmendment.h"
#include "OAIPatientCommunication.h"
#include "OAIPatientDrug.h"
#include "OAIPatientFlagType.h"
#include "OAIPatientIntervention.h"
#include "OAIPatientLabResultSet.h"
#include "OAIPatientMessage.h"
#include "OAIPatientPhysicalExam.h"
#include "OAIPatientProblem.h"
#include "OAIPatientRiskAssessment.h"
#include "OAIPatientVaccineRecord.h"
#include "OAIPatient_communications_list_200_response.h"
#include "OAIPatient_flag_types_list_200_response.h"
#include "OAIPatient_interventions_list_200_response.h"
#include "OAIPatient_lab_results_list_200_response.h"
#include "OAIPatient_messages_list_200_response.h"
#include "OAIPatient_physical_exams_list_200_response.h"
#include "OAIPatient_risk_assessments_list_200_response.h"
#include "OAIPatient_vaccine_records_list_200_response.h"
#include "OAIPatients_list_200_response.h"
#include "OAIPrescriptionMessage.h"
#include "OAIPrescription_messages_list_200_response.h"
#include "OAIProblems_list_200_response.h"
#include "OAIReminderProfile.h"
#include "OAIReminder_profiles_list_200_response.h"
#include "OAIScannedClinicalDocument.h"
#include "OAISoapNoteCustomReport.h"
#include "OAISoapNoteLineItemFieldType.h"
#include "OAISoapNoteLineItemFieldValue.h"
#include "OAISublabs_list_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIClinicalApi : public QObject {
    Q_OBJECT

public:
    OAIClinicalApi(const int timeOut = 0);
    ~OAIClinicalApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void allergiesCreate(const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void allergiesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void allergiesPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void allergiesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void allergiesUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  appointment qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void amendmentsCreate(const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void amendmentsDelete(const QString &id, const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void amendmentsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void amendmentsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void amendmentsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void amendmentsUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  doctor qint32 [optional]
    */
    virtual void appointmentProfilesCreate(const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void appointmentProfilesDelete(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void appointmentProfilesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void appointmentProfilesPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void appointmentProfilesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void appointmentProfilesUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  profile qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void appointmentTemplatesCreate(const ::OpenAPI::OptionalParam<qint32> &profile = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  profile qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void appointmentTemplatesDelete(const QString &id, const ::OpenAPI::OptionalParam<qint32> &profile = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  profile qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void appointmentTemplatesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &profile = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  profile qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void appointmentTemplatesPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &profile = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  profile qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void appointmentTemplatesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &profile = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  profile qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void appointmentTemplatesUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &profile = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  status QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_range QString [optional]
    * @param[in]  date QString [optional]
    */
    virtual void appointmentsCreate(const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  status QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_range QString [optional]
    * @param[in]  date QString [optional]
    */
    virtual void appointmentsDelete(const QString &id, const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  status QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_range QString [optional]
    * @param[in]  date QString [optional]
    */
    virtual void appointmentsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  status QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_range QString [optional]
    * @param[in]  date QString [optional]
    */
    virtual void appointmentsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  status QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_range QString [optional]
    * @param[in]  date QString [optional]
    */
    virtual void appointmentsRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  status QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_range QString [optional]
    * @param[in]  date QString [optional]
    */
    virtual void appointmentsUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  plan_type qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void carePlansList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &plan_type = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  plan_type qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void carePlansRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &plan_type = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void careTeamMembersList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void careTeamMembersRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  appointment qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void claimBillingNotesCreate(const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void claimBillingNotesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void claimBillingNotesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  clinical_note_template qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void clinicalNoteFieldTypesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &clinical_note_template = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  clinical_note_template qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void clinicalNoteFieldTypesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &clinical_note_template = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  clinical_note_field qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  clinical_note_template qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void clinicalNoteFieldValuesCreate(const ::OpenAPI::OptionalParam<qint32> &clinical_note_field = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &clinical_note_template = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  clinical_note_field qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  clinical_note_template qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void clinicalNoteFieldValuesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &clinical_note_field = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &clinical_note_template = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  clinical_note_field qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  clinical_note_template qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void clinicalNoteFieldValuesPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &clinical_note_field = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &clinical_note_template = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  clinical_note_field qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  clinical_note_template qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void clinicalNoteFieldValuesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &clinical_note_field = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &clinical_note_template = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  clinical_note_field qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  clinical_note_template qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void clinicalNoteFieldValuesUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &clinical_note_field = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &clinical_note_template = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void clinicalNoteTemplatesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void clinicalNoteTemplatesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_range QString [optional]
    * @param[in]  date QString [optional]
    */
    virtual void clinicalNotesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_range QString [optional]
    * @param[in]  date QString [optional]
    */
    virtual void clinicalNotesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void consentFormsApplyToAppointment(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  doctor qint32 [optional]
    */
    virtual void consentFormsCreate(const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void consentFormsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void consentFormsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void consentFormsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void consentFormsUnapplyFromAppointment(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void consentFormsUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  doctor qint32 [optional]
    */
    virtual void customAppointmentFieldsCreate(const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void customAppointmentFieldsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void customAppointmentFieldsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void customAppointmentFieldsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void customAppointmentFieldsUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  doctor qint32 [optional]
    */
    virtual void customDemographicsCreate(const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void customDemographicsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void customDemographicsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void customDemographicsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void customDemographicsUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void customVitalsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void customVitalsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void documentsCreate(const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void documentsDelete(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void documentsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void documentsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void documentsRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void documentsUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  doctor qint32 [optional]
    */
    virtual void eobsCreate(const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void eobsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void eobsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  code QString [optional]
    * @param[in]  code_type QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  payer_id QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void feeSchedulesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &code_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &payer_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  code QString [optional]
    * @param[in]  code_type QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  payer_id QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void feeSchedulesRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &code_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &payer_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  mu_date QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  mu_date_range QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void implantableDevicesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &mu_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &mu_date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  mu_date QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  mu_date_range QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void implantableDevicesRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &mu_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &mu_date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  payer_type QString [required]
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  term QString [optional]
    */
    virtual void insurancesList(const QString &payer_type, const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &term = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  payer_type QString [required]
    * @param[in]  term QString [optional]
    */
    virtual void insurancesRead(const QString &id, const QString &payer_type, const ::OpenAPI::OptionalParam<QString> &term = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labDocumentsCreate(const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labDocumentsDelete(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labDocumentsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labDocumentsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labDocumentsRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labDocumentsUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labOrdersCreate(const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labOrdersDelete(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labOrdersList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labOrdersPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labOrdersRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labOrdersSummaryList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labOrdersSummaryRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labOrdersUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  order qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labResultsCreate(const ::OpenAPI::OptionalParam<qint32> &order = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  order qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labResultsDelete(const QString &id, const ::OpenAPI::OptionalParam<qint32> &order = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  order qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labResultsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &order = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  order qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labResultsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &order = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  order qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labResultsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &order = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  order qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labResultsUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &order = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  order qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labTestsCreate(const ::OpenAPI::OptionalParam<qint32> &order = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  order qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labTestsDelete(const QString &id, const ::OpenAPI::OptionalParam<qint32> &order = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  order qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labTestsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &order = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  order qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labTestsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &order = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  order qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labTestsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &order = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  order qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void labTestsUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &order = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void medicationsAppendToPharmacyNote(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void medicationsCreate(const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void medicationsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void medicationsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void medicationsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void medicationsUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientCommunicationsCreate(const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientCommunicationsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientCommunicationsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientCommunicationsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientCommunicationsUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientFlagTypesCreate(const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientFlagTypesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientFlagTypesPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientFlagTypesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientFlagTypesUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientInterventionsCreate(const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientInterventionsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientInterventionsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientInterventionsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientInterventionsUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  ordering_doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientLabResultsCreate(const ::OpenAPI::OptionalParam<qint32> &ordering_doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  ordering_doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientLabResultsDelete(const QString &id, const ::OpenAPI::OptionalParam<qint32> &ordering_doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  ordering_doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientLabResultsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &ordering_doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  ordering_doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientLabResultsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &ordering_doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  ordering_doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientLabResultsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &ordering_doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  ordering_doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientLabResultsUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &ordering_doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientMessagesCreate(const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientMessagesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientMessagesPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientMessagesRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientMessagesUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientPhysicalExamsCreate(const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientPhysicalExamsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientPhysicalExamsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientPhysicalExamsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientPhysicalExamsUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientRiskAssessmentsCreate(const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientRiskAssessmentsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientRiskAssessmentsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientRiskAssessmentsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientRiskAssessmentsUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cvx_code QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientVaccineRecordsCreate(const ::OpenAPI::OptionalParam<QString> &cvx_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  cvx_code QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientVaccineRecordsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &cvx_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  cvx_code QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientVaccineRecordsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &cvx_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  cvx_code QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientVaccineRecordsRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &cvx_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  cvx_code QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientVaccineRecordsUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &cvx_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  preferred_language QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    * @param[in]  race QString [optional]
    * @param[in]  chart_id QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  ethnicity QString [optional]
    */
    virtual void patientsCcda(const QString &id, const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &preferred_language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &race = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &chart_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ethnicity = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  preferred_language QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    * @param[in]  race QString [optional]
    * @param[in]  chart_id QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  ethnicity QString [optional]
    */
    virtual void patientsCreate(const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &preferred_language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &race = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &chart_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ethnicity = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  preferred_language QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    * @param[in]  race QString [optional]
    * @param[in]  chart_id QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  ethnicity QString [optional]
    */
    virtual void patientsDelete(const QString &id, const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &preferred_language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &race = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &chart_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ethnicity = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  preferred_language QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    * @param[in]  race QString [optional]
    * @param[in]  chart_id QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  ethnicity QString [optional]
    */
    virtual void patientsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &preferred_language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &race = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &chart_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ethnicity = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  preferred_language QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    * @param[in]  race QString [optional]
    * @param[in]  chart_id QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  ethnicity QString [optional]
    */
    virtual void patientsOnpatientAccessCreate(const QString &id, const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &preferred_language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &race = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &chart_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ethnicity = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  preferred_language QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    * @param[in]  race QString [optional]
    * @param[in]  chart_id QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  ethnicity QString [optional]
    */
    virtual void patientsOnpatientAccessDelete(const QString &id, const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &preferred_language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &race = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &chart_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ethnicity = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  preferred_language QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    * @param[in]  race QString [optional]
    * @param[in]  chart_id QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  ethnicity QString [optional]
    */
    virtual void patientsOnpatientAccessRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &preferred_language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &race = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &chart_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ethnicity = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  preferred_language QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    * @param[in]  race QString [optional]
    * @param[in]  chart_id QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  ethnicity QString [optional]
    */
    virtual void patientsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &preferred_language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &race = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &chart_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ethnicity = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  preferred_language QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    * @param[in]  race QString [optional]
    * @param[in]  chart_id QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  ethnicity QString [optional]
    */
    virtual void patientsQrda1(const QString &id, const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &preferred_language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &race = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &chart_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ethnicity = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  preferred_language QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    * @param[in]  race QString [optional]
    * @param[in]  chart_id QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  ethnicity QString [optional]
    */
    virtual void patientsRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &preferred_language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &race = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &chart_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ethnicity = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    */
    virtual void patientsSummaryCreate(const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    */
    virtual void patientsSummaryDelete(const QString &id, const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    */
    virtual void patientsSummaryList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    */
    virtual void patientsSummaryPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    */
    virtual void patientsSummaryRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    */
    virtual void patientsSummaryUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  first_name QString [optional]
    * @param[in]  last_name QString [optional]
    * @param[in]  preferred_language QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  gender QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  date_of_birth QString [optional]
    * @param[in]  race QString [optional]
    * @param[in]  chart_id QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  ethnicity QString [optional]
    */
    virtual void patientsUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &first_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &last_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &preferred_language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &gender = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_of_birth = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &race = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &chart_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &ethnicity = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  parent_message qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void prescriptionMessagesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &parent_message = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  parent_message qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void prescriptionMessagesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &parent_message = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void problemsCreate(const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void problemsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void problemsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void problemsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void problemsUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  doctor qint32 [optional]
    */
    virtual void reminderProfilesCreate(const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void reminderProfilesDelete(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void reminderProfilesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void reminderProfilesPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void reminderProfilesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void reminderProfilesUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());


    virtual void sublabsCreate();

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void sublabsDelete(const qint32 &id);

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void sublabsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void sublabsPartialUpdate(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void sublabsRead(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void sublabsUpdate(const qint32 &id);


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void allergiesCreateCallback(OAIHttpRequestWorker *worker);
    void allergiesListCallback(OAIHttpRequestWorker *worker);
    void allergiesPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void allergiesReadCallback(OAIHttpRequestWorker *worker);
    void allergiesUpdateCallback(OAIHttpRequestWorker *worker);
    void amendmentsCreateCallback(OAIHttpRequestWorker *worker);
    void amendmentsDeleteCallback(OAIHttpRequestWorker *worker);
    void amendmentsListCallback(OAIHttpRequestWorker *worker);
    void amendmentsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void amendmentsReadCallback(OAIHttpRequestWorker *worker);
    void amendmentsUpdateCallback(OAIHttpRequestWorker *worker);
    void appointmentProfilesCreateCallback(OAIHttpRequestWorker *worker);
    void appointmentProfilesDeleteCallback(OAIHttpRequestWorker *worker);
    void appointmentProfilesListCallback(OAIHttpRequestWorker *worker);
    void appointmentProfilesPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void appointmentProfilesReadCallback(OAIHttpRequestWorker *worker);
    void appointmentProfilesUpdateCallback(OAIHttpRequestWorker *worker);
    void appointmentTemplatesCreateCallback(OAIHttpRequestWorker *worker);
    void appointmentTemplatesDeleteCallback(OAIHttpRequestWorker *worker);
    void appointmentTemplatesListCallback(OAIHttpRequestWorker *worker);
    void appointmentTemplatesPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void appointmentTemplatesReadCallback(OAIHttpRequestWorker *worker);
    void appointmentTemplatesUpdateCallback(OAIHttpRequestWorker *worker);
    void appointmentsCreateCallback(OAIHttpRequestWorker *worker);
    void appointmentsDeleteCallback(OAIHttpRequestWorker *worker);
    void appointmentsListCallback(OAIHttpRequestWorker *worker);
    void appointmentsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void appointmentsReadCallback(OAIHttpRequestWorker *worker);
    void appointmentsUpdateCallback(OAIHttpRequestWorker *worker);
    void carePlansListCallback(OAIHttpRequestWorker *worker);
    void carePlansReadCallback(OAIHttpRequestWorker *worker);
    void careTeamMembersListCallback(OAIHttpRequestWorker *worker);
    void careTeamMembersReadCallback(OAIHttpRequestWorker *worker);
    void claimBillingNotesCreateCallback(OAIHttpRequestWorker *worker);
    void claimBillingNotesListCallback(OAIHttpRequestWorker *worker);
    void claimBillingNotesReadCallback(OAIHttpRequestWorker *worker);
    void clinicalNoteFieldTypesListCallback(OAIHttpRequestWorker *worker);
    void clinicalNoteFieldTypesReadCallback(OAIHttpRequestWorker *worker);
    void clinicalNoteFieldValuesCreateCallback(OAIHttpRequestWorker *worker);
    void clinicalNoteFieldValuesListCallback(OAIHttpRequestWorker *worker);
    void clinicalNoteFieldValuesPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void clinicalNoteFieldValuesReadCallback(OAIHttpRequestWorker *worker);
    void clinicalNoteFieldValuesUpdateCallback(OAIHttpRequestWorker *worker);
    void clinicalNoteTemplatesListCallback(OAIHttpRequestWorker *worker);
    void clinicalNoteTemplatesReadCallback(OAIHttpRequestWorker *worker);
    void clinicalNotesListCallback(OAIHttpRequestWorker *worker);
    void clinicalNotesReadCallback(OAIHttpRequestWorker *worker);
    void consentFormsApplyToAppointmentCallback(OAIHttpRequestWorker *worker);
    void consentFormsCreateCallback(OAIHttpRequestWorker *worker);
    void consentFormsListCallback(OAIHttpRequestWorker *worker);
    void consentFormsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void consentFormsReadCallback(OAIHttpRequestWorker *worker);
    void consentFormsUnapplyFromAppointmentCallback(OAIHttpRequestWorker *worker);
    void consentFormsUpdateCallback(OAIHttpRequestWorker *worker);
    void customAppointmentFieldsCreateCallback(OAIHttpRequestWorker *worker);
    void customAppointmentFieldsListCallback(OAIHttpRequestWorker *worker);
    void customAppointmentFieldsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void customAppointmentFieldsReadCallback(OAIHttpRequestWorker *worker);
    void customAppointmentFieldsUpdateCallback(OAIHttpRequestWorker *worker);
    void customDemographicsCreateCallback(OAIHttpRequestWorker *worker);
    void customDemographicsListCallback(OAIHttpRequestWorker *worker);
    void customDemographicsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void customDemographicsReadCallback(OAIHttpRequestWorker *worker);
    void customDemographicsUpdateCallback(OAIHttpRequestWorker *worker);
    void customVitalsListCallback(OAIHttpRequestWorker *worker);
    void customVitalsReadCallback(OAIHttpRequestWorker *worker);
    void documentsCreateCallback(OAIHttpRequestWorker *worker);
    void documentsDeleteCallback(OAIHttpRequestWorker *worker);
    void documentsListCallback(OAIHttpRequestWorker *worker);
    void documentsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void documentsReadCallback(OAIHttpRequestWorker *worker);
    void documentsUpdateCallback(OAIHttpRequestWorker *worker);
    void eobsCreateCallback(OAIHttpRequestWorker *worker);
    void eobsListCallback(OAIHttpRequestWorker *worker);
    void eobsReadCallback(OAIHttpRequestWorker *worker);
    void feeSchedulesListCallback(OAIHttpRequestWorker *worker);
    void feeSchedulesReadCallback(OAIHttpRequestWorker *worker);
    void implantableDevicesListCallback(OAIHttpRequestWorker *worker);
    void implantableDevicesReadCallback(OAIHttpRequestWorker *worker);
    void insurancesListCallback(OAIHttpRequestWorker *worker);
    void insurancesReadCallback(OAIHttpRequestWorker *worker);
    void labDocumentsCreateCallback(OAIHttpRequestWorker *worker);
    void labDocumentsDeleteCallback(OAIHttpRequestWorker *worker);
    void labDocumentsListCallback(OAIHttpRequestWorker *worker);
    void labDocumentsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void labDocumentsReadCallback(OAIHttpRequestWorker *worker);
    void labDocumentsUpdateCallback(OAIHttpRequestWorker *worker);
    void labOrdersCreateCallback(OAIHttpRequestWorker *worker);
    void labOrdersDeleteCallback(OAIHttpRequestWorker *worker);
    void labOrdersListCallback(OAIHttpRequestWorker *worker);
    void labOrdersPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void labOrdersReadCallback(OAIHttpRequestWorker *worker);
    void labOrdersSummaryListCallback(OAIHttpRequestWorker *worker);
    void labOrdersSummaryReadCallback(OAIHttpRequestWorker *worker);
    void labOrdersUpdateCallback(OAIHttpRequestWorker *worker);
    void labResultsCreateCallback(OAIHttpRequestWorker *worker);
    void labResultsDeleteCallback(OAIHttpRequestWorker *worker);
    void labResultsListCallback(OAIHttpRequestWorker *worker);
    void labResultsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void labResultsReadCallback(OAIHttpRequestWorker *worker);
    void labResultsUpdateCallback(OAIHttpRequestWorker *worker);
    void labTestsCreateCallback(OAIHttpRequestWorker *worker);
    void labTestsDeleteCallback(OAIHttpRequestWorker *worker);
    void labTestsListCallback(OAIHttpRequestWorker *worker);
    void labTestsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void labTestsReadCallback(OAIHttpRequestWorker *worker);
    void labTestsUpdateCallback(OAIHttpRequestWorker *worker);
    void medicationsAppendToPharmacyNoteCallback(OAIHttpRequestWorker *worker);
    void medicationsCreateCallback(OAIHttpRequestWorker *worker);
    void medicationsListCallback(OAIHttpRequestWorker *worker);
    void medicationsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void medicationsReadCallback(OAIHttpRequestWorker *worker);
    void medicationsUpdateCallback(OAIHttpRequestWorker *worker);
    void patientCommunicationsCreateCallback(OAIHttpRequestWorker *worker);
    void patientCommunicationsListCallback(OAIHttpRequestWorker *worker);
    void patientCommunicationsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void patientCommunicationsReadCallback(OAIHttpRequestWorker *worker);
    void patientCommunicationsUpdateCallback(OAIHttpRequestWorker *worker);
    void patientFlagTypesCreateCallback(OAIHttpRequestWorker *worker);
    void patientFlagTypesListCallback(OAIHttpRequestWorker *worker);
    void patientFlagTypesPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void patientFlagTypesReadCallback(OAIHttpRequestWorker *worker);
    void patientFlagTypesUpdateCallback(OAIHttpRequestWorker *worker);
    void patientInterventionsCreateCallback(OAIHttpRequestWorker *worker);
    void patientInterventionsListCallback(OAIHttpRequestWorker *worker);
    void patientInterventionsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void patientInterventionsReadCallback(OAIHttpRequestWorker *worker);
    void patientInterventionsUpdateCallback(OAIHttpRequestWorker *worker);
    void patientLabResultsCreateCallback(OAIHttpRequestWorker *worker);
    void patientLabResultsDeleteCallback(OAIHttpRequestWorker *worker);
    void patientLabResultsListCallback(OAIHttpRequestWorker *worker);
    void patientLabResultsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void patientLabResultsReadCallback(OAIHttpRequestWorker *worker);
    void patientLabResultsUpdateCallback(OAIHttpRequestWorker *worker);
    void patientMessagesCreateCallback(OAIHttpRequestWorker *worker);
    void patientMessagesListCallback(OAIHttpRequestWorker *worker);
    void patientMessagesPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void patientMessagesReadCallback(OAIHttpRequestWorker *worker);
    void patientMessagesUpdateCallback(OAIHttpRequestWorker *worker);
    void patientPhysicalExamsCreateCallback(OAIHttpRequestWorker *worker);
    void patientPhysicalExamsListCallback(OAIHttpRequestWorker *worker);
    void patientPhysicalExamsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void patientPhysicalExamsReadCallback(OAIHttpRequestWorker *worker);
    void patientPhysicalExamsUpdateCallback(OAIHttpRequestWorker *worker);
    void patientRiskAssessmentsCreateCallback(OAIHttpRequestWorker *worker);
    void patientRiskAssessmentsListCallback(OAIHttpRequestWorker *worker);
    void patientRiskAssessmentsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void patientRiskAssessmentsReadCallback(OAIHttpRequestWorker *worker);
    void patientRiskAssessmentsUpdateCallback(OAIHttpRequestWorker *worker);
    void patientVaccineRecordsCreateCallback(OAIHttpRequestWorker *worker);
    void patientVaccineRecordsListCallback(OAIHttpRequestWorker *worker);
    void patientVaccineRecordsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void patientVaccineRecordsReadCallback(OAIHttpRequestWorker *worker);
    void patientVaccineRecordsUpdateCallback(OAIHttpRequestWorker *worker);
    void patientsCcdaCallback(OAIHttpRequestWorker *worker);
    void patientsCreateCallback(OAIHttpRequestWorker *worker);
    void patientsDeleteCallback(OAIHttpRequestWorker *worker);
    void patientsListCallback(OAIHttpRequestWorker *worker);
    void patientsOnpatientAccessCreateCallback(OAIHttpRequestWorker *worker);
    void patientsOnpatientAccessDeleteCallback(OAIHttpRequestWorker *worker);
    void patientsOnpatientAccessReadCallback(OAIHttpRequestWorker *worker);
    void patientsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void patientsQrda1Callback(OAIHttpRequestWorker *worker);
    void patientsReadCallback(OAIHttpRequestWorker *worker);
    void patientsSummaryCreateCallback(OAIHttpRequestWorker *worker);
    void patientsSummaryDeleteCallback(OAIHttpRequestWorker *worker);
    void patientsSummaryListCallback(OAIHttpRequestWorker *worker);
    void patientsSummaryPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void patientsSummaryReadCallback(OAIHttpRequestWorker *worker);
    void patientsSummaryUpdateCallback(OAIHttpRequestWorker *worker);
    void patientsUpdateCallback(OAIHttpRequestWorker *worker);
    void prescriptionMessagesListCallback(OAIHttpRequestWorker *worker);
    void prescriptionMessagesReadCallback(OAIHttpRequestWorker *worker);
    void problemsCreateCallback(OAIHttpRequestWorker *worker);
    void problemsListCallback(OAIHttpRequestWorker *worker);
    void problemsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void problemsReadCallback(OAIHttpRequestWorker *worker);
    void problemsUpdateCallback(OAIHttpRequestWorker *worker);
    void reminderProfilesCreateCallback(OAIHttpRequestWorker *worker);
    void reminderProfilesDeleteCallback(OAIHttpRequestWorker *worker);
    void reminderProfilesListCallback(OAIHttpRequestWorker *worker);
    void reminderProfilesPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void reminderProfilesReadCallback(OAIHttpRequestWorker *worker);
    void reminderProfilesUpdateCallback(OAIHttpRequestWorker *worker);
    void sublabsCreateCallback(OAIHttpRequestWorker *worker);
    void sublabsDeleteCallback(OAIHttpRequestWorker *worker);
    void sublabsListCallback(OAIHttpRequestWorker *worker);
    void sublabsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void sublabsReadCallback(OAIHttpRequestWorker *worker);
    void sublabsUpdateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void allergiesCreateSignal(OAIPatientAllergy summary);
    void allergiesListSignal(OAIAllergies_list_200_response summary);
    void allergiesPartialUpdateSignal();
    void allergiesReadSignal(OAIPatientAllergy summary);
    void allergiesUpdateSignal();
    void amendmentsCreateSignal(OAIPatientAmendment summary);
    void amendmentsDeleteSignal();
    void amendmentsListSignal(OAIAmendments_list_200_response summary);
    void amendmentsPartialUpdateSignal();
    void amendmentsReadSignal(OAIPatientAmendment summary);
    void amendmentsUpdateSignal();
    void appointmentProfilesCreateSignal(OAIAppointmentProfile summary);
    void appointmentProfilesDeleteSignal();
    void appointmentProfilesListSignal(OAIAppointment_profiles_list_200_response summary);
    void appointmentProfilesPartialUpdateSignal();
    void appointmentProfilesReadSignal(OAIAppointmentProfile summary);
    void appointmentProfilesUpdateSignal();
    void appointmentTemplatesCreateSignal(OAIAppointmentTemplate summary);
    void appointmentTemplatesDeleteSignal();
    void appointmentTemplatesListSignal(OAIAppointment_templates_list_200_response summary);
    void appointmentTemplatesPartialUpdateSignal();
    void appointmentTemplatesReadSignal(OAIAppointmentTemplate summary);
    void appointmentTemplatesUpdateSignal();
    void appointmentsCreateSignal(OAIAppointment summary);
    void appointmentsDeleteSignal();
    void appointmentsListSignal(OAIAppointments_list_200_response summary);
    void appointmentsPartialUpdateSignal();
    void appointmentsReadSignal(OAIAppointment summary);
    void appointmentsUpdateSignal();
    void carePlansListSignal(OAICare_plans_list_200_response summary);
    void carePlansReadSignal(OAICarePlan summary);
    void careTeamMembersListSignal(OAICare_team_members_list_200_response summary);
    void careTeamMembersReadSignal(OAICareTeamMember summary);
    void claimBillingNotesCreateSignal(OAIClaimBillingNotes summary);
    void claimBillingNotesListSignal(OAIClaim_billing_notes_list_200_response summary);
    void claimBillingNotesReadSignal(OAIClaimBillingNotes summary);
    void clinicalNoteFieldTypesListSignal(OAIClinical_note_field_types_list_200_response summary);
    void clinicalNoteFieldTypesReadSignal(OAISoapNoteLineItemFieldType summary);
    void clinicalNoteFieldValuesCreateSignal(OAISoapNoteLineItemFieldValue summary);
    void clinicalNoteFieldValuesListSignal(OAIClinical_note_field_values_list_200_response summary);
    void clinicalNoteFieldValuesPartialUpdateSignal();
    void clinicalNoteFieldValuesReadSignal(OAISoapNoteLineItemFieldValue summary);
    void clinicalNoteFieldValuesUpdateSignal();
    void clinicalNoteTemplatesListSignal(OAIClinical_note_templates_list_200_response summary);
    void clinicalNoteTemplatesReadSignal(OAISoapNoteCustomReport summary);
    void clinicalNotesListSignal(OAIClinical_notes_list_200_response summary);
    void clinicalNotesReadSignal(OAIClinicalNote summary);
    void consentFormsApplyToAppointmentSignal();
    void consentFormsCreateSignal(OAIConsentForm summary);
    void consentFormsListSignal(OAIConsent_forms_list_200_response summary);
    void consentFormsPartialUpdateSignal();
    void consentFormsReadSignal(OAIConsentForm summary);
    void consentFormsUnapplyFromAppointmentSignal();
    void consentFormsUpdateSignal();
    void customAppointmentFieldsCreateSignal(OAICustomAppointmentFieldType summary);
    void customAppointmentFieldsListSignal(OAICustom_appointment_fields_list_200_response summary);
    void customAppointmentFieldsPartialUpdateSignal();
    void customAppointmentFieldsReadSignal(OAICustomAppointmentFieldType summary);
    void customAppointmentFieldsUpdateSignal();
    void customDemographicsCreateSignal(OAICustomPatientFieldType summary);
    void customDemographicsListSignal(OAICustom_demographics_list_200_response summary);
    void customDemographicsPartialUpdateSignal();
    void customDemographicsReadSignal(OAICustomPatientFieldType summary);
    void customDemographicsUpdateSignal();
    void customVitalsListSignal(OAICustom_vitals_list_200_response summary);
    void customVitalsReadSignal(OAICustomVitalType summary);
    void documentsCreateSignal(OAIScannedClinicalDocument summary);
    void documentsDeleteSignal();
    void documentsListSignal(OAIDocuments_list_200_response summary);
    void documentsPartialUpdateSignal();
    void documentsReadSignal(OAIScannedClinicalDocument summary);
    void documentsUpdateSignal();
    void eobsCreateSignal(OAIEOBObject summary);
    void eobsListSignal(OAIEobs_list_200_response summary);
    void eobsReadSignal(OAIEOBObject summary);
    void feeSchedulesListSignal(OAIFee_schedules_list_200_response summary);
    void feeSchedulesReadSignal(OAIDoctorFeeSchedule summary);
    void implantableDevicesListSignal(OAIImplantable_devices_list_200_response summary);
    void implantableDevicesReadSignal(OAIImplantableDevice summary);
    void insurancesListSignal(OAIInsurances_list_200_response summary);
    void insurancesReadSignal(OAIInsurance summary);
    void labDocumentsCreateSignal(OAILabOrderDocument summary);
    void labDocumentsDeleteSignal();
    void labDocumentsListSignal(OAILab_documents_list_200_response summary);
    void labDocumentsPartialUpdateSignal();
    void labDocumentsReadSignal(OAILabOrderDocument summary);
    void labDocumentsUpdateSignal();
    void labOrdersCreateSignal(OAILabOrder summary);
    void labOrdersDeleteSignal();
    void labOrdersListSignal(OAILab_orders_list_200_response summary);
    void labOrdersPartialUpdateSignal();
    void labOrdersReadSignal(OAILabOrder summary);
    void labOrdersSummaryListSignal(OAILab_orders_list_200_response summary);
    void labOrdersSummaryReadSignal(OAILabOrder summary);
    void labOrdersUpdateSignal();
    void labResultsCreateSignal(OAILabResult summary);
    void labResultsDeleteSignal();
    void labResultsListSignal(OAILab_results_list_200_response summary);
    void labResultsPartialUpdateSignal();
    void labResultsReadSignal(OAILabResult summary);
    void labResultsUpdateSignal();
    void labTestsCreateSignal(OAILabTest summary);
    void labTestsDeleteSignal();
    void labTestsListSignal(OAILab_tests_list_200_response summary);
    void labTestsPartialUpdateSignal();
    void labTestsReadSignal(OAILabTest summary);
    void labTestsUpdateSignal();
    void medicationsAppendToPharmacyNoteSignal();
    void medicationsCreateSignal(OAIPatientDrug summary);
    void medicationsListSignal(OAIMedications_list_200_response summary);
    void medicationsPartialUpdateSignal();
    void medicationsReadSignal(OAIPatientDrug summary);
    void medicationsUpdateSignal();
    void patientCommunicationsCreateSignal(OAIPatientCommunication summary);
    void patientCommunicationsListSignal(OAIPatient_communications_list_200_response summary);
    void patientCommunicationsPartialUpdateSignal();
    void patientCommunicationsReadSignal(OAIPatientCommunication summary);
    void patientCommunicationsUpdateSignal();
    void patientFlagTypesCreateSignal(OAIPatientFlagType summary);
    void patientFlagTypesListSignal(OAIPatient_flag_types_list_200_response summary);
    void patientFlagTypesPartialUpdateSignal();
    void patientFlagTypesReadSignal(OAIPatientFlagType summary);
    void patientFlagTypesUpdateSignal();
    void patientInterventionsCreateSignal(OAIPatientIntervention summary);
    void patientInterventionsListSignal(OAIPatient_interventions_list_200_response summary);
    void patientInterventionsPartialUpdateSignal();
    void patientInterventionsReadSignal(OAIPatientIntervention summary);
    void patientInterventionsUpdateSignal();
    void patientLabResultsCreateSignal(OAIPatientLabResultSet summary);
    void patientLabResultsDeleteSignal();
    void patientLabResultsListSignal(OAIPatient_lab_results_list_200_response summary);
    void patientLabResultsPartialUpdateSignal();
    void patientLabResultsReadSignal(OAIPatientLabResultSet summary);
    void patientLabResultsUpdateSignal();
    void patientMessagesCreateSignal(OAIPatientMessage summary);
    void patientMessagesListSignal(OAIPatient_messages_list_200_response summary);
    void patientMessagesPartialUpdateSignal();
    void patientMessagesReadSignal(OAIPatientMessage summary);
    void patientMessagesUpdateSignal();
    void patientPhysicalExamsCreateSignal(OAIPatientPhysicalExam summary);
    void patientPhysicalExamsListSignal(OAIPatient_physical_exams_list_200_response summary);
    void patientPhysicalExamsPartialUpdateSignal();
    void patientPhysicalExamsReadSignal(OAIPatientPhysicalExam summary);
    void patientPhysicalExamsUpdateSignal();
    void patientRiskAssessmentsCreateSignal(OAIPatientRiskAssessment summary);
    void patientRiskAssessmentsListSignal(OAIPatient_risk_assessments_list_200_response summary);
    void patientRiskAssessmentsPartialUpdateSignal();
    void patientRiskAssessmentsReadSignal(OAIPatientRiskAssessment summary);
    void patientRiskAssessmentsUpdateSignal();
    void patientVaccineRecordsCreateSignal(OAIPatientVaccineRecord summary);
    void patientVaccineRecordsListSignal(OAIPatient_vaccine_records_list_200_response summary);
    void patientVaccineRecordsPartialUpdateSignal();
    void patientVaccineRecordsReadSignal(OAIPatientVaccineRecord summary);
    void patientVaccineRecordsUpdateSignal();
    void patientsCcdaSignal(OAIObject summary);
    void patientsCreateSignal(OAIPatient summary);
    void patientsDeleteSignal();
    void patientsListSignal(OAIPatients_list_200_response summary);
    void patientsOnpatientAccessCreateSignal(OAIPatient summary);
    void patientsOnpatientAccessDeleteSignal();
    void patientsOnpatientAccessReadSignal(OAIPatient summary);
    void patientsPartialUpdateSignal();
    void patientsQrda1Signal(OAIObject summary);
    void patientsReadSignal(OAIPatient summary);
    void patientsSummaryCreateSignal(OAIPatient summary);
    void patientsSummaryDeleteSignal();
    void patientsSummaryListSignal(OAIPatients_list_200_response summary);
    void patientsSummaryPartialUpdateSignal();
    void patientsSummaryReadSignal(OAIPatient summary);
    void patientsSummaryUpdateSignal();
    void patientsUpdateSignal();
    void prescriptionMessagesListSignal(OAIPrescription_messages_list_200_response summary);
    void prescriptionMessagesReadSignal(OAIPrescriptionMessage summary);
    void problemsCreateSignal(OAIPatientProblem summary);
    void problemsListSignal(OAIProblems_list_200_response summary);
    void problemsPartialUpdateSignal();
    void problemsReadSignal(OAIPatientProblem summary);
    void problemsUpdateSignal();
    void reminderProfilesCreateSignal(OAIReminderProfile summary);
    void reminderProfilesDeleteSignal();
    void reminderProfilesListSignal(OAIReminder_profiles_list_200_response summary);
    void reminderProfilesPartialUpdateSignal();
    void reminderProfilesReadSignal(OAIReminderProfile summary);
    void reminderProfilesUpdateSignal();
    void sublabsCreateSignal(OAILabVendorLocation summary);
    void sublabsDeleteSignal();
    void sublabsListSignal(OAISublabs_list_200_response summary);
    void sublabsPartialUpdateSignal();
    void sublabsReadSignal(OAILabVendorLocation summary);
    void sublabsUpdateSignal();


    void allergiesCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatientAllergy summary);
    void allergiesListSignalFull(OAIHttpRequestWorker *worker, OAIAllergies_list_200_response summary);
    void allergiesPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void allergiesReadSignalFull(OAIHttpRequestWorker *worker, OAIPatientAllergy summary);
    void allergiesUpdateSignalFull(OAIHttpRequestWorker *worker);
    void amendmentsCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatientAmendment summary);
    void amendmentsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void amendmentsListSignalFull(OAIHttpRequestWorker *worker, OAIAmendments_list_200_response summary);
    void amendmentsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void amendmentsReadSignalFull(OAIHttpRequestWorker *worker, OAIPatientAmendment summary);
    void amendmentsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void appointmentProfilesCreateSignalFull(OAIHttpRequestWorker *worker, OAIAppointmentProfile summary);
    void appointmentProfilesDeleteSignalFull(OAIHttpRequestWorker *worker);
    void appointmentProfilesListSignalFull(OAIHttpRequestWorker *worker, OAIAppointment_profiles_list_200_response summary);
    void appointmentProfilesPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void appointmentProfilesReadSignalFull(OAIHttpRequestWorker *worker, OAIAppointmentProfile summary);
    void appointmentProfilesUpdateSignalFull(OAIHttpRequestWorker *worker);
    void appointmentTemplatesCreateSignalFull(OAIHttpRequestWorker *worker, OAIAppointmentTemplate summary);
    void appointmentTemplatesDeleteSignalFull(OAIHttpRequestWorker *worker);
    void appointmentTemplatesListSignalFull(OAIHttpRequestWorker *worker, OAIAppointment_templates_list_200_response summary);
    void appointmentTemplatesPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void appointmentTemplatesReadSignalFull(OAIHttpRequestWorker *worker, OAIAppointmentTemplate summary);
    void appointmentTemplatesUpdateSignalFull(OAIHttpRequestWorker *worker);
    void appointmentsCreateSignalFull(OAIHttpRequestWorker *worker, OAIAppointment summary);
    void appointmentsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void appointmentsListSignalFull(OAIHttpRequestWorker *worker, OAIAppointments_list_200_response summary);
    void appointmentsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void appointmentsReadSignalFull(OAIHttpRequestWorker *worker, OAIAppointment summary);
    void appointmentsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void carePlansListSignalFull(OAIHttpRequestWorker *worker, OAICare_plans_list_200_response summary);
    void carePlansReadSignalFull(OAIHttpRequestWorker *worker, OAICarePlan summary);
    void careTeamMembersListSignalFull(OAIHttpRequestWorker *worker, OAICare_team_members_list_200_response summary);
    void careTeamMembersReadSignalFull(OAIHttpRequestWorker *worker, OAICareTeamMember summary);
    void claimBillingNotesCreateSignalFull(OAIHttpRequestWorker *worker, OAIClaimBillingNotes summary);
    void claimBillingNotesListSignalFull(OAIHttpRequestWorker *worker, OAIClaim_billing_notes_list_200_response summary);
    void claimBillingNotesReadSignalFull(OAIHttpRequestWorker *worker, OAIClaimBillingNotes summary);
    void clinicalNoteFieldTypesListSignalFull(OAIHttpRequestWorker *worker, OAIClinical_note_field_types_list_200_response summary);
    void clinicalNoteFieldTypesReadSignalFull(OAIHttpRequestWorker *worker, OAISoapNoteLineItemFieldType summary);
    void clinicalNoteFieldValuesCreateSignalFull(OAIHttpRequestWorker *worker, OAISoapNoteLineItemFieldValue summary);
    void clinicalNoteFieldValuesListSignalFull(OAIHttpRequestWorker *worker, OAIClinical_note_field_values_list_200_response summary);
    void clinicalNoteFieldValuesPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void clinicalNoteFieldValuesReadSignalFull(OAIHttpRequestWorker *worker, OAISoapNoteLineItemFieldValue summary);
    void clinicalNoteFieldValuesUpdateSignalFull(OAIHttpRequestWorker *worker);
    void clinicalNoteTemplatesListSignalFull(OAIHttpRequestWorker *worker, OAIClinical_note_templates_list_200_response summary);
    void clinicalNoteTemplatesReadSignalFull(OAIHttpRequestWorker *worker, OAISoapNoteCustomReport summary);
    void clinicalNotesListSignalFull(OAIHttpRequestWorker *worker, OAIClinical_notes_list_200_response summary);
    void clinicalNotesReadSignalFull(OAIHttpRequestWorker *worker, OAIClinicalNote summary);
    void consentFormsApplyToAppointmentSignalFull(OAIHttpRequestWorker *worker);
    void consentFormsCreateSignalFull(OAIHttpRequestWorker *worker, OAIConsentForm summary);
    void consentFormsListSignalFull(OAIHttpRequestWorker *worker, OAIConsent_forms_list_200_response summary);
    void consentFormsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void consentFormsReadSignalFull(OAIHttpRequestWorker *worker, OAIConsentForm summary);
    void consentFormsUnapplyFromAppointmentSignalFull(OAIHttpRequestWorker *worker);
    void consentFormsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void customAppointmentFieldsCreateSignalFull(OAIHttpRequestWorker *worker, OAICustomAppointmentFieldType summary);
    void customAppointmentFieldsListSignalFull(OAIHttpRequestWorker *worker, OAICustom_appointment_fields_list_200_response summary);
    void customAppointmentFieldsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void customAppointmentFieldsReadSignalFull(OAIHttpRequestWorker *worker, OAICustomAppointmentFieldType summary);
    void customAppointmentFieldsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void customDemographicsCreateSignalFull(OAIHttpRequestWorker *worker, OAICustomPatientFieldType summary);
    void customDemographicsListSignalFull(OAIHttpRequestWorker *worker, OAICustom_demographics_list_200_response summary);
    void customDemographicsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void customDemographicsReadSignalFull(OAIHttpRequestWorker *worker, OAICustomPatientFieldType summary);
    void customDemographicsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void customVitalsListSignalFull(OAIHttpRequestWorker *worker, OAICustom_vitals_list_200_response summary);
    void customVitalsReadSignalFull(OAIHttpRequestWorker *worker, OAICustomVitalType summary);
    void documentsCreateSignalFull(OAIHttpRequestWorker *worker, OAIScannedClinicalDocument summary);
    void documentsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void documentsListSignalFull(OAIHttpRequestWorker *worker, OAIDocuments_list_200_response summary);
    void documentsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void documentsReadSignalFull(OAIHttpRequestWorker *worker, OAIScannedClinicalDocument summary);
    void documentsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void eobsCreateSignalFull(OAIHttpRequestWorker *worker, OAIEOBObject summary);
    void eobsListSignalFull(OAIHttpRequestWorker *worker, OAIEobs_list_200_response summary);
    void eobsReadSignalFull(OAIHttpRequestWorker *worker, OAIEOBObject summary);
    void feeSchedulesListSignalFull(OAIHttpRequestWorker *worker, OAIFee_schedules_list_200_response summary);
    void feeSchedulesReadSignalFull(OAIHttpRequestWorker *worker, OAIDoctorFeeSchedule summary);
    void implantableDevicesListSignalFull(OAIHttpRequestWorker *worker, OAIImplantable_devices_list_200_response summary);
    void implantableDevicesReadSignalFull(OAIHttpRequestWorker *worker, OAIImplantableDevice summary);
    void insurancesListSignalFull(OAIHttpRequestWorker *worker, OAIInsurances_list_200_response summary);
    void insurancesReadSignalFull(OAIHttpRequestWorker *worker, OAIInsurance summary);
    void labDocumentsCreateSignalFull(OAIHttpRequestWorker *worker, OAILabOrderDocument summary);
    void labDocumentsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void labDocumentsListSignalFull(OAIHttpRequestWorker *worker, OAILab_documents_list_200_response summary);
    void labDocumentsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void labDocumentsReadSignalFull(OAIHttpRequestWorker *worker, OAILabOrderDocument summary);
    void labDocumentsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void labOrdersCreateSignalFull(OAIHttpRequestWorker *worker, OAILabOrder summary);
    void labOrdersDeleteSignalFull(OAIHttpRequestWorker *worker);
    void labOrdersListSignalFull(OAIHttpRequestWorker *worker, OAILab_orders_list_200_response summary);
    void labOrdersPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void labOrdersReadSignalFull(OAIHttpRequestWorker *worker, OAILabOrder summary);
    void labOrdersSummaryListSignalFull(OAIHttpRequestWorker *worker, OAILab_orders_list_200_response summary);
    void labOrdersSummaryReadSignalFull(OAIHttpRequestWorker *worker, OAILabOrder summary);
    void labOrdersUpdateSignalFull(OAIHttpRequestWorker *worker);
    void labResultsCreateSignalFull(OAIHttpRequestWorker *worker, OAILabResult summary);
    void labResultsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void labResultsListSignalFull(OAIHttpRequestWorker *worker, OAILab_results_list_200_response summary);
    void labResultsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void labResultsReadSignalFull(OAIHttpRequestWorker *worker, OAILabResult summary);
    void labResultsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void labTestsCreateSignalFull(OAIHttpRequestWorker *worker, OAILabTest summary);
    void labTestsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void labTestsListSignalFull(OAIHttpRequestWorker *worker, OAILab_tests_list_200_response summary);
    void labTestsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void labTestsReadSignalFull(OAIHttpRequestWorker *worker, OAILabTest summary);
    void labTestsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void medicationsAppendToPharmacyNoteSignalFull(OAIHttpRequestWorker *worker);
    void medicationsCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatientDrug summary);
    void medicationsListSignalFull(OAIHttpRequestWorker *worker, OAIMedications_list_200_response summary);
    void medicationsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void medicationsReadSignalFull(OAIHttpRequestWorker *worker, OAIPatientDrug summary);
    void medicationsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientCommunicationsCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatientCommunication summary);
    void patientCommunicationsListSignalFull(OAIHttpRequestWorker *worker, OAIPatient_communications_list_200_response summary);
    void patientCommunicationsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientCommunicationsReadSignalFull(OAIHttpRequestWorker *worker, OAIPatientCommunication summary);
    void patientCommunicationsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientFlagTypesCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatientFlagType summary);
    void patientFlagTypesListSignalFull(OAIHttpRequestWorker *worker, OAIPatient_flag_types_list_200_response summary);
    void patientFlagTypesPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientFlagTypesReadSignalFull(OAIHttpRequestWorker *worker, OAIPatientFlagType summary);
    void patientFlagTypesUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientInterventionsCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatientIntervention summary);
    void patientInterventionsListSignalFull(OAIHttpRequestWorker *worker, OAIPatient_interventions_list_200_response summary);
    void patientInterventionsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientInterventionsReadSignalFull(OAIHttpRequestWorker *worker, OAIPatientIntervention summary);
    void patientInterventionsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientLabResultsCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatientLabResultSet summary);
    void patientLabResultsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void patientLabResultsListSignalFull(OAIHttpRequestWorker *worker, OAIPatient_lab_results_list_200_response summary);
    void patientLabResultsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientLabResultsReadSignalFull(OAIHttpRequestWorker *worker, OAIPatientLabResultSet summary);
    void patientLabResultsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientMessagesCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatientMessage summary);
    void patientMessagesListSignalFull(OAIHttpRequestWorker *worker, OAIPatient_messages_list_200_response summary);
    void patientMessagesPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientMessagesReadSignalFull(OAIHttpRequestWorker *worker, OAIPatientMessage summary);
    void patientMessagesUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientPhysicalExamsCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatientPhysicalExam summary);
    void patientPhysicalExamsListSignalFull(OAIHttpRequestWorker *worker, OAIPatient_physical_exams_list_200_response summary);
    void patientPhysicalExamsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientPhysicalExamsReadSignalFull(OAIHttpRequestWorker *worker, OAIPatientPhysicalExam summary);
    void patientPhysicalExamsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientRiskAssessmentsCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatientRiskAssessment summary);
    void patientRiskAssessmentsListSignalFull(OAIHttpRequestWorker *worker, OAIPatient_risk_assessments_list_200_response summary);
    void patientRiskAssessmentsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientRiskAssessmentsReadSignalFull(OAIHttpRequestWorker *worker, OAIPatientRiskAssessment summary);
    void patientRiskAssessmentsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientVaccineRecordsCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatientVaccineRecord summary);
    void patientVaccineRecordsListSignalFull(OAIHttpRequestWorker *worker, OAIPatient_vaccine_records_list_200_response summary);
    void patientVaccineRecordsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientVaccineRecordsReadSignalFull(OAIHttpRequestWorker *worker, OAIPatientVaccineRecord summary);
    void patientVaccineRecordsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientsCcdaSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void patientsCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatient summary);
    void patientsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void patientsListSignalFull(OAIHttpRequestWorker *worker, OAIPatients_list_200_response summary);
    void patientsOnpatientAccessCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatient summary);
    void patientsOnpatientAccessDeleteSignalFull(OAIHttpRequestWorker *worker);
    void patientsOnpatientAccessReadSignalFull(OAIHttpRequestWorker *worker, OAIPatient summary);
    void patientsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientsQrda1SignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void patientsReadSignalFull(OAIHttpRequestWorker *worker, OAIPatient summary);
    void patientsSummaryCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatient summary);
    void patientsSummaryDeleteSignalFull(OAIHttpRequestWorker *worker);
    void patientsSummaryListSignalFull(OAIHttpRequestWorker *worker, OAIPatients_list_200_response summary);
    void patientsSummaryPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientsSummaryReadSignalFull(OAIHttpRequestWorker *worker, OAIPatient summary);
    void patientsSummaryUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void prescriptionMessagesListSignalFull(OAIHttpRequestWorker *worker, OAIPrescription_messages_list_200_response summary);
    void prescriptionMessagesReadSignalFull(OAIHttpRequestWorker *worker, OAIPrescriptionMessage summary);
    void problemsCreateSignalFull(OAIHttpRequestWorker *worker, OAIPatientProblem summary);
    void problemsListSignalFull(OAIHttpRequestWorker *worker, OAIProblems_list_200_response summary);
    void problemsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void problemsReadSignalFull(OAIHttpRequestWorker *worker, OAIPatientProblem summary);
    void problemsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void reminderProfilesCreateSignalFull(OAIHttpRequestWorker *worker, OAIReminderProfile summary);
    void reminderProfilesDeleteSignalFull(OAIHttpRequestWorker *worker);
    void reminderProfilesListSignalFull(OAIHttpRequestWorker *worker, OAIReminder_profiles_list_200_response summary);
    void reminderProfilesPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void reminderProfilesReadSignalFull(OAIHttpRequestWorker *worker, OAIReminderProfile summary);
    void reminderProfilesUpdateSignalFull(OAIHttpRequestWorker *worker);
    void sublabsCreateSignalFull(OAIHttpRequestWorker *worker, OAILabVendorLocation summary);
    void sublabsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void sublabsListSignalFull(OAIHttpRequestWorker *worker, OAISublabs_list_200_response summary);
    void sublabsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void sublabsReadSignalFull(OAIHttpRequestWorker *worker, OAILabVendorLocation summary);
    void sublabsUpdateSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use allergiesCreateSignalError() instead")
    void allergiesCreateSignalE(OAIPatientAllergy summary, QNetworkReply::NetworkError error_type, QString error_str);
    void allergiesCreateSignalError(OAIPatientAllergy summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use allergiesListSignalError() instead")
    void allergiesListSignalE(OAIAllergies_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void allergiesListSignalError(OAIAllergies_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use allergiesPartialUpdateSignalError() instead")
    void allergiesPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void allergiesPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use allergiesReadSignalError() instead")
    void allergiesReadSignalE(OAIPatientAllergy summary, QNetworkReply::NetworkError error_type, QString error_str);
    void allergiesReadSignalError(OAIPatientAllergy summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use allergiesUpdateSignalError() instead")
    void allergiesUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void allergiesUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use amendmentsCreateSignalError() instead")
    void amendmentsCreateSignalE(OAIPatientAmendment summary, QNetworkReply::NetworkError error_type, QString error_str);
    void amendmentsCreateSignalError(OAIPatientAmendment summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use amendmentsDeleteSignalError() instead")
    void amendmentsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void amendmentsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use amendmentsListSignalError() instead")
    void amendmentsListSignalE(OAIAmendments_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void amendmentsListSignalError(OAIAmendments_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use amendmentsPartialUpdateSignalError() instead")
    void amendmentsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void amendmentsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use amendmentsReadSignalError() instead")
    void amendmentsReadSignalE(OAIPatientAmendment summary, QNetworkReply::NetworkError error_type, QString error_str);
    void amendmentsReadSignalError(OAIPatientAmendment summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use amendmentsUpdateSignalError() instead")
    void amendmentsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void amendmentsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentProfilesCreateSignalError() instead")
    void appointmentProfilesCreateSignalE(OAIAppointmentProfile summary, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentProfilesCreateSignalError(OAIAppointmentProfile summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentProfilesDeleteSignalError() instead")
    void appointmentProfilesDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentProfilesDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentProfilesListSignalError() instead")
    void appointmentProfilesListSignalE(OAIAppointment_profiles_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentProfilesListSignalError(OAIAppointment_profiles_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentProfilesPartialUpdateSignalError() instead")
    void appointmentProfilesPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentProfilesPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentProfilesReadSignalError() instead")
    void appointmentProfilesReadSignalE(OAIAppointmentProfile summary, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentProfilesReadSignalError(OAIAppointmentProfile summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentProfilesUpdateSignalError() instead")
    void appointmentProfilesUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentProfilesUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentTemplatesCreateSignalError() instead")
    void appointmentTemplatesCreateSignalE(OAIAppointmentTemplate summary, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentTemplatesCreateSignalError(OAIAppointmentTemplate summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentTemplatesDeleteSignalError() instead")
    void appointmentTemplatesDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentTemplatesDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentTemplatesListSignalError() instead")
    void appointmentTemplatesListSignalE(OAIAppointment_templates_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentTemplatesListSignalError(OAIAppointment_templates_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentTemplatesPartialUpdateSignalError() instead")
    void appointmentTemplatesPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentTemplatesPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentTemplatesReadSignalError() instead")
    void appointmentTemplatesReadSignalE(OAIAppointmentTemplate summary, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentTemplatesReadSignalError(OAIAppointmentTemplate summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentTemplatesUpdateSignalError() instead")
    void appointmentTemplatesUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentTemplatesUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentsCreateSignalError() instead")
    void appointmentsCreateSignalE(OAIAppointment summary, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentsCreateSignalError(OAIAppointment summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentsDeleteSignalError() instead")
    void appointmentsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentsListSignalError() instead")
    void appointmentsListSignalE(OAIAppointments_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentsListSignalError(OAIAppointments_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentsPartialUpdateSignalError() instead")
    void appointmentsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentsReadSignalError() instead")
    void appointmentsReadSignalE(OAIAppointment summary, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentsReadSignalError(OAIAppointment summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentsUpdateSignalError() instead")
    void appointmentsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use carePlansListSignalError() instead")
    void carePlansListSignalE(OAICare_plans_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void carePlansListSignalError(OAICare_plans_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use carePlansReadSignalError() instead")
    void carePlansReadSignalE(OAICarePlan summary, QNetworkReply::NetworkError error_type, QString error_str);
    void carePlansReadSignalError(OAICarePlan summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use careTeamMembersListSignalError() instead")
    void careTeamMembersListSignalE(OAICare_team_members_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void careTeamMembersListSignalError(OAICare_team_members_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use careTeamMembersReadSignalError() instead")
    void careTeamMembersReadSignalE(OAICareTeamMember summary, QNetworkReply::NetworkError error_type, QString error_str);
    void careTeamMembersReadSignalError(OAICareTeamMember summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use claimBillingNotesCreateSignalError() instead")
    void claimBillingNotesCreateSignalE(OAIClaimBillingNotes summary, QNetworkReply::NetworkError error_type, QString error_str);
    void claimBillingNotesCreateSignalError(OAIClaimBillingNotes summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use claimBillingNotesListSignalError() instead")
    void claimBillingNotesListSignalE(OAIClaim_billing_notes_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void claimBillingNotesListSignalError(OAIClaim_billing_notes_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use claimBillingNotesReadSignalError() instead")
    void claimBillingNotesReadSignalE(OAIClaimBillingNotes summary, QNetworkReply::NetworkError error_type, QString error_str);
    void claimBillingNotesReadSignalError(OAIClaimBillingNotes summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteFieldTypesListSignalError() instead")
    void clinicalNoteFieldTypesListSignalE(OAIClinical_note_field_types_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteFieldTypesListSignalError(OAIClinical_note_field_types_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteFieldTypesReadSignalError() instead")
    void clinicalNoteFieldTypesReadSignalE(OAISoapNoteLineItemFieldType summary, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteFieldTypesReadSignalError(OAISoapNoteLineItemFieldType summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteFieldValuesCreateSignalError() instead")
    void clinicalNoteFieldValuesCreateSignalE(OAISoapNoteLineItemFieldValue summary, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteFieldValuesCreateSignalError(OAISoapNoteLineItemFieldValue summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteFieldValuesListSignalError() instead")
    void clinicalNoteFieldValuesListSignalE(OAIClinical_note_field_values_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteFieldValuesListSignalError(OAIClinical_note_field_values_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteFieldValuesPartialUpdateSignalError() instead")
    void clinicalNoteFieldValuesPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteFieldValuesPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteFieldValuesReadSignalError() instead")
    void clinicalNoteFieldValuesReadSignalE(OAISoapNoteLineItemFieldValue summary, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteFieldValuesReadSignalError(OAISoapNoteLineItemFieldValue summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteFieldValuesUpdateSignalError() instead")
    void clinicalNoteFieldValuesUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteFieldValuesUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteTemplatesListSignalError() instead")
    void clinicalNoteTemplatesListSignalE(OAIClinical_note_templates_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteTemplatesListSignalError(OAIClinical_note_templates_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteTemplatesReadSignalError() instead")
    void clinicalNoteTemplatesReadSignalE(OAISoapNoteCustomReport summary, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteTemplatesReadSignalError(OAISoapNoteCustomReport summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNotesListSignalError() instead")
    void clinicalNotesListSignalE(OAIClinical_notes_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNotesListSignalError(OAIClinical_notes_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNotesReadSignalError() instead")
    void clinicalNotesReadSignalE(OAIClinicalNote summary, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNotesReadSignalError(OAIClinicalNote summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consentFormsApplyToAppointmentSignalError() instead")
    void consentFormsApplyToAppointmentSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void consentFormsApplyToAppointmentSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consentFormsCreateSignalError() instead")
    void consentFormsCreateSignalE(OAIConsentForm summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consentFormsCreateSignalError(OAIConsentForm summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consentFormsListSignalError() instead")
    void consentFormsListSignalE(OAIConsent_forms_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consentFormsListSignalError(OAIConsent_forms_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consentFormsPartialUpdateSignalError() instead")
    void consentFormsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void consentFormsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consentFormsReadSignalError() instead")
    void consentFormsReadSignalE(OAIConsentForm summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consentFormsReadSignalError(OAIConsentForm summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consentFormsUnapplyFromAppointmentSignalError() instead")
    void consentFormsUnapplyFromAppointmentSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void consentFormsUnapplyFromAppointmentSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consentFormsUpdateSignalError() instead")
    void consentFormsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void consentFormsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customAppointmentFieldsCreateSignalError() instead")
    void customAppointmentFieldsCreateSignalE(OAICustomAppointmentFieldType summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customAppointmentFieldsCreateSignalError(OAICustomAppointmentFieldType summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customAppointmentFieldsListSignalError() instead")
    void customAppointmentFieldsListSignalE(OAICustom_appointment_fields_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customAppointmentFieldsListSignalError(OAICustom_appointment_fields_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customAppointmentFieldsPartialUpdateSignalError() instead")
    void customAppointmentFieldsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void customAppointmentFieldsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customAppointmentFieldsReadSignalError() instead")
    void customAppointmentFieldsReadSignalE(OAICustomAppointmentFieldType summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customAppointmentFieldsReadSignalError(OAICustomAppointmentFieldType summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customAppointmentFieldsUpdateSignalError() instead")
    void customAppointmentFieldsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void customAppointmentFieldsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customDemographicsCreateSignalError() instead")
    void customDemographicsCreateSignalE(OAICustomPatientFieldType summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customDemographicsCreateSignalError(OAICustomPatientFieldType summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customDemographicsListSignalError() instead")
    void customDemographicsListSignalE(OAICustom_demographics_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customDemographicsListSignalError(OAICustom_demographics_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customDemographicsPartialUpdateSignalError() instead")
    void customDemographicsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void customDemographicsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customDemographicsReadSignalError() instead")
    void customDemographicsReadSignalE(OAICustomPatientFieldType summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customDemographicsReadSignalError(OAICustomPatientFieldType summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customDemographicsUpdateSignalError() instead")
    void customDemographicsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void customDemographicsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customVitalsListSignalError() instead")
    void customVitalsListSignalE(OAICustom_vitals_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customVitalsListSignalError(OAICustom_vitals_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customVitalsReadSignalError() instead")
    void customVitalsReadSignalE(OAICustomVitalType summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customVitalsReadSignalError(OAICustomVitalType summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsCreateSignalError() instead")
    void documentsCreateSignalE(OAIScannedClinicalDocument summary, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsCreateSignalError(OAIScannedClinicalDocument summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsDeleteSignalError() instead")
    void documentsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void documentsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsListSignalError() instead")
    void documentsListSignalE(OAIDocuments_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsListSignalError(OAIDocuments_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsPartialUpdateSignalError() instead")
    void documentsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void documentsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsReadSignalError() instead")
    void documentsReadSignalE(OAIScannedClinicalDocument summary, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsReadSignalError(OAIScannedClinicalDocument summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsUpdateSignalError() instead")
    void documentsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void documentsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eobsCreateSignalError() instead")
    void eobsCreateSignalE(OAIEOBObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void eobsCreateSignalError(OAIEOBObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eobsListSignalError() instead")
    void eobsListSignalE(OAIEobs_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void eobsListSignalError(OAIEobs_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eobsReadSignalError() instead")
    void eobsReadSignalE(OAIEOBObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void eobsReadSignalError(OAIEOBObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use feeSchedulesListSignalError() instead")
    void feeSchedulesListSignalE(OAIFee_schedules_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void feeSchedulesListSignalError(OAIFee_schedules_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use feeSchedulesReadSignalError() instead")
    void feeSchedulesReadSignalE(OAIDoctorFeeSchedule summary, QNetworkReply::NetworkError error_type, QString error_str);
    void feeSchedulesReadSignalError(OAIDoctorFeeSchedule summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use implantableDevicesListSignalError() instead")
    void implantableDevicesListSignalE(OAIImplantable_devices_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void implantableDevicesListSignalError(OAIImplantable_devices_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use implantableDevicesReadSignalError() instead")
    void implantableDevicesReadSignalE(OAIImplantableDevice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void implantableDevicesReadSignalError(OAIImplantableDevice summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use insurancesListSignalError() instead")
    void insurancesListSignalE(OAIInsurances_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void insurancesListSignalError(OAIInsurances_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use insurancesReadSignalError() instead")
    void insurancesReadSignalE(OAIInsurance summary, QNetworkReply::NetworkError error_type, QString error_str);
    void insurancesReadSignalError(OAIInsurance summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labDocumentsCreateSignalError() instead")
    void labDocumentsCreateSignalE(OAILabOrderDocument summary, QNetworkReply::NetworkError error_type, QString error_str);
    void labDocumentsCreateSignalError(OAILabOrderDocument summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labDocumentsDeleteSignalError() instead")
    void labDocumentsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void labDocumentsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labDocumentsListSignalError() instead")
    void labDocumentsListSignalE(OAILab_documents_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void labDocumentsListSignalError(OAILab_documents_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labDocumentsPartialUpdateSignalError() instead")
    void labDocumentsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void labDocumentsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labDocumentsReadSignalError() instead")
    void labDocumentsReadSignalE(OAILabOrderDocument summary, QNetworkReply::NetworkError error_type, QString error_str);
    void labDocumentsReadSignalError(OAILabOrderDocument summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labDocumentsUpdateSignalError() instead")
    void labDocumentsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void labDocumentsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersCreateSignalError() instead")
    void labOrdersCreateSignalE(OAILabOrder summary, QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersCreateSignalError(OAILabOrder summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersDeleteSignalError() instead")
    void labOrdersDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersListSignalError() instead")
    void labOrdersListSignalE(OAILab_orders_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersListSignalError(OAILab_orders_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersPartialUpdateSignalError() instead")
    void labOrdersPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersReadSignalError() instead")
    void labOrdersReadSignalE(OAILabOrder summary, QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersReadSignalError(OAILabOrder summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersSummaryListSignalError() instead")
    void labOrdersSummaryListSignalE(OAILab_orders_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersSummaryListSignalError(OAILab_orders_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersSummaryReadSignalError() instead")
    void labOrdersSummaryReadSignalE(OAILabOrder summary, QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersSummaryReadSignalError(OAILabOrder summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersUpdateSignalError() instead")
    void labOrdersUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labResultsCreateSignalError() instead")
    void labResultsCreateSignalE(OAILabResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void labResultsCreateSignalError(OAILabResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labResultsDeleteSignalError() instead")
    void labResultsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void labResultsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labResultsListSignalError() instead")
    void labResultsListSignalE(OAILab_results_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void labResultsListSignalError(OAILab_results_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labResultsPartialUpdateSignalError() instead")
    void labResultsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void labResultsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labResultsReadSignalError() instead")
    void labResultsReadSignalE(OAILabResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void labResultsReadSignalError(OAILabResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labResultsUpdateSignalError() instead")
    void labResultsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void labResultsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labTestsCreateSignalError() instead")
    void labTestsCreateSignalE(OAILabTest summary, QNetworkReply::NetworkError error_type, QString error_str);
    void labTestsCreateSignalError(OAILabTest summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labTestsDeleteSignalError() instead")
    void labTestsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void labTestsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labTestsListSignalError() instead")
    void labTestsListSignalE(OAILab_tests_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void labTestsListSignalError(OAILab_tests_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labTestsPartialUpdateSignalError() instead")
    void labTestsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void labTestsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labTestsReadSignalError() instead")
    void labTestsReadSignalE(OAILabTest summary, QNetworkReply::NetworkError error_type, QString error_str);
    void labTestsReadSignalError(OAILabTest summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labTestsUpdateSignalError() instead")
    void labTestsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void labTestsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use medicationsAppendToPharmacyNoteSignalError() instead")
    void medicationsAppendToPharmacyNoteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void medicationsAppendToPharmacyNoteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use medicationsCreateSignalError() instead")
    void medicationsCreateSignalE(OAIPatientDrug summary, QNetworkReply::NetworkError error_type, QString error_str);
    void medicationsCreateSignalError(OAIPatientDrug summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use medicationsListSignalError() instead")
    void medicationsListSignalE(OAIMedications_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void medicationsListSignalError(OAIMedications_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use medicationsPartialUpdateSignalError() instead")
    void medicationsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void medicationsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use medicationsReadSignalError() instead")
    void medicationsReadSignalE(OAIPatientDrug summary, QNetworkReply::NetworkError error_type, QString error_str);
    void medicationsReadSignalError(OAIPatientDrug summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use medicationsUpdateSignalError() instead")
    void medicationsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void medicationsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientCommunicationsCreateSignalError() instead")
    void patientCommunicationsCreateSignalE(OAIPatientCommunication summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientCommunicationsCreateSignalError(OAIPatientCommunication summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientCommunicationsListSignalError() instead")
    void patientCommunicationsListSignalE(OAIPatient_communications_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientCommunicationsListSignalError(OAIPatient_communications_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientCommunicationsPartialUpdateSignalError() instead")
    void patientCommunicationsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientCommunicationsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientCommunicationsReadSignalError() instead")
    void patientCommunicationsReadSignalE(OAIPatientCommunication summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientCommunicationsReadSignalError(OAIPatientCommunication summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientCommunicationsUpdateSignalError() instead")
    void patientCommunicationsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientCommunicationsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientFlagTypesCreateSignalError() instead")
    void patientFlagTypesCreateSignalE(OAIPatientFlagType summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientFlagTypesCreateSignalError(OAIPatientFlagType summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientFlagTypesListSignalError() instead")
    void patientFlagTypesListSignalE(OAIPatient_flag_types_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientFlagTypesListSignalError(OAIPatient_flag_types_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientFlagTypesPartialUpdateSignalError() instead")
    void patientFlagTypesPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientFlagTypesPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientFlagTypesReadSignalError() instead")
    void patientFlagTypesReadSignalE(OAIPatientFlagType summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientFlagTypesReadSignalError(OAIPatientFlagType summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientFlagTypesUpdateSignalError() instead")
    void patientFlagTypesUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientFlagTypesUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientInterventionsCreateSignalError() instead")
    void patientInterventionsCreateSignalE(OAIPatientIntervention summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientInterventionsCreateSignalError(OAIPatientIntervention summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientInterventionsListSignalError() instead")
    void patientInterventionsListSignalE(OAIPatient_interventions_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientInterventionsListSignalError(OAIPatient_interventions_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientInterventionsPartialUpdateSignalError() instead")
    void patientInterventionsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientInterventionsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientInterventionsReadSignalError() instead")
    void patientInterventionsReadSignalE(OAIPatientIntervention summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientInterventionsReadSignalError(OAIPatientIntervention summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientInterventionsUpdateSignalError() instead")
    void patientInterventionsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientInterventionsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientLabResultsCreateSignalError() instead")
    void patientLabResultsCreateSignalE(OAIPatientLabResultSet summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientLabResultsCreateSignalError(OAIPatientLabResultSet summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientLabResultsDeleteSignalError() instead")
    void patientLabResultsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientLabResultsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientLabResultsListSignalError() instead")
    void patientLabResultsListSignalE(OAIPatient_lab_results_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientLabResultsListSignalError(OAIPatient_lab_results_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientLabResultsPartialUpdateSignalError() instead")
    void patientLabResultsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientLabResultsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientLabResultsReadSignalError() instead")
    void patientLabResultsReadSignalE(OAIPatientLabResultSet summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientLabResultsReadSignalError(OAIPatientLabResultSet summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientLabResultsUpdateSignalError() instead")
    void patientLabResultsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientLabResultsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientMessagesCreateSignalError() instead")
    void patientMessagesCreateSignalE(OAIPatientMessage summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientMessagesCreateSignalError(OAIPatientMessage summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientMessagesListSignalError() instead")
    void patientMessagesListSignalE(OAIPatient_messages_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientMessagesListSignalError(OAIPatient_messages_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientMessagesPartialUpdateSignalError() instead")
    void patientMessagesPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientMessagesPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientMessagesReadSignalError() instead")
    void patientMessagesReadSignalE(OAIPatientMessage summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientMessagesReadSignalError(OAIPatientMessage summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientMessagesUpdateSignalError() instead")
    void patientMessagesUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientMessagesUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPhysicalExamsCreateSignalError() instead")
    void patientPhysicalExamsCreateSignalE(OAIPatientPhysicalExam summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPhysicalExamsCreateSignalError(OAIPatientPhysicalExam summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPhysicalExamsListSignalError() instead")
    void patientPhysicalExamsListSignalE(OAIPatient_physical_exams_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPhysicalExamsListSignalError(OAIPatient_physical_exams_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPhysicalExamsPartialUpdateSignalError() instead")
    void patientPhysicalExamsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientPhysicalExamsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPhysicalExamsReadSignalError() instead")
    void patientPhysicalExamsReadSignalE(OAIPatientPhysicalExam summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPhysicalExamsReadSignalError(OAIPatientPhysicalExam summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPhysicalExamsUpdateSignalError() instead")
    void patientPhysicalExamsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientPhysicalExamsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientRiskAssessmentsCreateSignalError() instead")
    void patientRiskAssessmentsCreateSignalE(OAIPatientRiskAssessment summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientRiskAssessmentsCreateSignalError(OAIPatientRiskAssessment summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientRiskAssessmentsListSignalError() instead")
    void patientRiskAssessmentsListSignalE(OAIPatient_risk_assessments_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientRiskAssessmentsListSignalError(OAIPatient_risk_assessments_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientRiskAssessmentsPartialUpdateSignalError() instead")
    void patientRiskAssessmentsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientRiskAssessmentsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientRiskAssessmentsReadSignalError() instead")
    void patientRiskAssessmentsReadSignalE(OAIPatientRiskAssessment summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientRiskAssessmentsReadSignalError(OAIPatientRiskAssessment summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientRiskAssessmentsUpdateSignalError() instead")
    void patientRiskAssessmentsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientRiskAssessmentsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientVaccineRecordsCreateSignalError() instead")
    void patientVaccineRecordsCreateSignalE(OAIPatientVaccineRecord summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientVaccineRecordsCreateSignalError(OAIPatientVaccineRecord summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientVaccineRecordsListSignalError() instead")
    void patientVaccineRecordsListSignalE(OAIPatient_vaccine_records_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientVaccineRecordsListSignalError(OAIPatient_vaccine_records_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientVaccineRecordsPartialUpdateSignalError() instead")
    void patientVaccineRecordsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientVaccineRecordsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientVaccineRecordsReadSignalError() instead")
    void patientVaccineRecordsReadSignalE(OAIPatientVaccineRecord summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientVaccineRecordsReadSignalError(OAIPatientVaccineRecord summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientVaccineRecordsUpdateSignalError() instead")
    void patientVaccineRecordsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientVaccineRecordsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsCcdaSignalError() instead")
    void patientsCcdaSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsCcdaSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsCreateSignalError() instead")
    void patientsCreateSignalE(OAIPatient summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsCreateSignalError(OAIPatient summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsDeleteSignalError() instead")
    void patientsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsListSignalError() instead")
    void patientsListSignalE(OAIPatients_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsListSignalError(OAIPatients_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsOnpatientAccessCreateSignalError() instead")
    void patientsOnpatientAccessCreateSignalE(OAIPatient summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsOnpatientAccessCreateSignalError(OAIPatient summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsOnpatientAccessDeleteSignalError() instead")
    void patientsOnpatientAccessDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientsOnpatientAccessDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsOnpatientAccessReadSignalError() instead")
    void patientsOnpatientAccessReadSignalE(OAIPatient summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsOnpatientAccessReadSignalError(OAIPatient summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsPartialUpdateSignalError() instead")
    void patientsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsQrda1SignalError() instead")
    void patientsQrda1SignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsQrda1SignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsReadSignalError() instead")
    void patientsReadSignalE(OAIPatient summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsReadSignalError(OAIPatient summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsSummaryCreateSignalError() instead")
    void patientsSummaryCreateSignalE(OAIPatient summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsSummaryCreateSignalError(OAIPatient summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsSummaryDeleteSignalError() instead")
    void patientsSummaryDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientsSummaryDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsSummaryListSignalError() instead")
    void patientsSummaryListSignalE(OAIPatients_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsSummaryListSignalError(OAIPatients_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsSummaryPartialUpdateSignalError() instead")
    void patientsSummaryPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientsSummaryPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsSummaryReadSignalError() instead")
    void patientsSummaryReadSignalE(OAIPatient summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsSummaryReadSignalError(OAIPatient summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsSummaryUpdateSignalError() instead")
    void patientsSummaryUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientsSummaryUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsUpdateSignalError() instead")
    void patientsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void patientsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use prescriptionMessagesListSignalError() instead")
    void prescriptionMessagesListSignalE(OAIPrescription_messages_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void prescriptionMessagesListSignalError(OAIPrescription_messages_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use prescriptionMessagesReadSignalError() instead")
    void prescriptionMessagesReadSignalE(OAIPrescriptionMessage summary, QNetworkReply::NetworkError error_type, QString error_str);
    void prescriptionMessagesReadSignalError(OAIPrescriptionMessage summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use problemsCreateSignalError() instead")
    void problemsCreateSignalE(OAIPatientProblem summary, QNetworkReply::NetworkError error_type, QString error_str);
    void problemsCreateSignalError(OAIPatientProblem summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use problemsListSignalError() instead")
    void problemsListSignalE(OAIProblems_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void problemsListSignalError(OAIProblems_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use problemsPartialUpdateSignalError() instead")
    void problemsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void problemsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use problemsReadSignalError() instead")
    void problemsReadSignalE(OAIPatientProblem summary, QNetworkReply::NetworkError error_type, QString error_str);
    void problemsReadSignalError(OAIPatientProblem summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use problemsUpdateSignalError() instead")
    void problemsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void problemsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reminderProfilesCreateSignalError() instead")
    void reminderProfilesCreateSignalE(OAIReminderProfile summary, QNetworkReply::NetworkError error_type, QString error_str);
    void reminderProfilesCreateSignalError(OAIReminderProfile summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reminderProfilesDeleteSignalError() instead")
    void reminderProfilesDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void reminderProfilesDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reminderProfilesListSignalError() instead")
    void reminderProfilesListSignalE(OAIReminder_profiles_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void reminderProfilesListSignalError(OAIReminder_profiles_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reminderProfilesPartialUpdateSignalError() instead")
    void reminderProfilesPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void reminderProfilesPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reminderProfilesReadSignalError() instead")
    void reminderProfilesReadSignalE(OAIReminderProfile summary, QNetworkReply::NetworkError error_type, QString error_str);
    void reminderProfilesReadSignalError(OAIReminderProfile summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reminderProfilesUpdateSignalError() instead")
    void reminderProfilesUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void reminderProfilesUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sublabsCreateSignalError() instead")
    void sublabsCreateSignalE(OAILabVendorLocation summary, QNetworkReply::NetworkError error_type, QString error_str);
    void sublabsCreateSignalError(OAILabVendorLocation summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sublabsDeleteSignalError() instead")
    void sublabsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void sublabsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sublabsListSignalError() instead")
    void sublabsListSignalE(OAISublabs_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void sublabsListSignalError(OAISublabs_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sublabsPartialUpdateSignalError() instead")
    void sublabsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void sublabsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sublabsReadSignalError() instead")
    void sublabsReadSignalE(OAILabVendorLocation summary, QNetworkReply::NetworkError error_type, QString error_str);
    void sublabsReadSignalError(OAILabVendorLocation summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sublabsUpdateSignalError() instead")
    void sublabsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void sublabsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use allergiesCreateSignalErrorFull() instead")
    void allergiesCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void allergiesCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use allergiesListSignalErrorFull() instead")
    void allergiesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void allergiesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use allergiesPartialUpdateSignalErrorFull() instead")
    void allergiesPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void allergiesPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use allergiesReadSignalErrorFull() instead")
    void allergiesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void allergiesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use allergiesUpdateSignalErrorFull() instead")
    void allergiesUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void allergiesUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use amendmentsCreateSignalErrorFull() instead")
    void amendmentsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void amendmentsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use amendmentsDeleteSignalErrorFull() instead")
    void amendmentsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void amendmentsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use amendmentsListSignalErrorFull() instead")
    void amendmentsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void amendmentsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use amendmentsPartialUpdateSignalErrorFull() instead")
    void amendmentsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void amendmentsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use amendmentsReadSignalErrorFull() instead")
    void amendmentsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void amendmentsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use amendmentsUpdateSignalErrorFull() instead")
    void amendmentsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void amendmentsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentProfilesCreateSignalErrorFull() instead")
    void appointmentProfilesCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentProfilesCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentProfilesDeleteSignalErrorFull() instead")
    void appointmentProfilesDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentProfilesDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentProfilesListSignalErrorFull() instead")
    void appointmentProfilesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentProfilesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentProfilesPartialUpdateSignalErrorFull() instead")
    void appointmentProfilesPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentProfilesPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentProfilesReadSignalErrorFull() instead")
    void appointmentProfilesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentProfilesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentProfilesUpdateSignalErrorFull() instead")
    void appointmentProfilesUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentProfilesUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentTemplatesCreateSignalErrorFull() instead")
    void appointmentTemplatesCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentTemplatesCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentTemplatesDeleteSignalErrorFull() instead")
    void appointmentTemplatesDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentTemplatesDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentTemplatesListSignalErrorFull() instead")
    void appointmentTemplatesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentTemplatesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentTemplatesPartialUpdateSignalErrorFull() instead")
    void appointmentTemplatesPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentTemplatesPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentTemplatesReadSignalErrorFull() instead")
    void appointmentTemplatesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentTemplatesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentTemplatesUpdateSignalErrorFull() instead")
    void appointmentTemplatesUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentTemplatesUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentsCreateSignalErrorFull() instead")
    void appointmentsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentsDeleteSignalErrorFull() instead")
    void appointmentsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentsListSignalErrorFull() instead")
    void appointmentsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentsPartialUpdateSignalErrorFull() instead")
    void appointmentsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentsReadSignalErrorFull() instead")
    void appointmentsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use appointmentsUpdateSignalErrorFull() instead")
    void appointmentsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void appointmentsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use carePlansListSignalErrorFull() instead")
    void carePlansListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void carePlansListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use carePlansReadSignalErrorFull() instead")
    void carePlansReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void carePlansReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use careTeamMembersListSignalErrorFull() instead")
    void careTeamMembersListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void careTeamMembersListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use careTeamMembersReadSignalErrorFull() instead")
    void careTeamMembersReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void careTeamMembersReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use claimBillingNotesCreateSignalErrorFull() instead")
    void claimBillingNotesCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void claimBillingNotesCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use claimBillingNotesListSignalErrorFull() instead")
    void claimBillingNotesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void claimBillingNotesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use claimBillingNotesReadSignalErrorFull() instead")
    void claimBillingNotesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void claimBillingNotesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteFieldTypesListSignalErrorFull() instead")
    void clinicalNoteFieldTypesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteFieldTypesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteFieldTypesReadSignalErrorFull() instead")
    void clinicalNoteFieldTypesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteFieldTypesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteFieldValuesCreateSignalErrorFull() instead")
    void clinicalNoteFieldValuesCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteFieldValuesCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteFieldValuesListSignalErrorFull() instead")
    void clinicalNoteFieldValuesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteFieldValuesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteFieldValuesPartialUpdateSignalErrorFull() instead")
    void clinicalNoteFieldValuesPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteFieldValuesPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteFieldValuesReadSignalErrorFull() instead")
    void clinicalNoteFieldValuesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteFieldValuesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteFieldValuesUpdateSignalErrorFull() instead")
    void clinicalNoteFieldValuesUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteFieldValuesUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteTemplatesListSignalErrorFull() instead")
    void clinicalNoteTemplatesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteTemplatesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNoteTemplatesReadSignalErrorFull() instead")
    void clinicalNoteTemplatesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNoteTemplatesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNotesListSignalErrorFull() instead")
    void clinicalNotesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNotesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use clinicalNotesReadSignalErrorFull() instead")
    void clinicalNotesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void clinicalNotesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consentFormsApplyToAppointmentSignalErrorFull() instead")
    void consentFormsApplyToAppointmentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consentFormsApplyToAppointmentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consentFormsCreateSignalErrorFull() instead")
    void consentFormsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consentFormsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consentFormsListSignalErrorFull() instead")
    void consentFormsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consentFormsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consentFormsPartialUpdateSignalErrorFull() instead")
    void consentFormsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consentFormsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consentFormsReadSignalErrorFull() instead")
    void consentFormsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consentFormsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consentFormsUnapplyFromAppointmentSignalErrorFull() instead")
    void consentFormsUnapplyFromAppointmentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consentFormsUnapplyFromAppointmentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consentFormsUpdateSignalErrorFull() instead")
    void consentFormsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consentFormsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customAppointmentFieldsCreateSignalErrorFull() instead")
    void customAppointmentFieldsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customAppointmentFieldsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customAppointmentFieldsListSignalErrorFull() instead")
    void customAppointmentFieldsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customAppointmentFieldsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customAppointmentFieldsPartialUpdateSignalErrorFull() instead")
    void customAppointmentFieldsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customAppointmentFieldsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customAppointmentFieldsReadSignalErrorFull() instead")
    void customAppointmentFieldsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customAppointmentFieldsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customAppointmentFieldsUpdateSignalErrorFull() instead")
    void customAppointmentFieldsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customAppointmentFieldsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customDemographicsCreateSignalErrorFull() instead")
    void customDemographicsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customDemographicsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customDemographicsListSignalErrorFull() instead")
    void customDemographicsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customDemographicsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customDemographicsPartialUpdateSignalErrorFull() instead")
    void customDemographicsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customDemographicsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customDemographicsReadSignalErrorFull() instead")
    void customDemographicsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customDemographicsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customDemographicsUpdateSignalErrorFull() instead")
    void customDemographicsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customDemographicsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customVitalsListSignalErrorFull() instead")
    void customVitalsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customVitalsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customVitalsReadSignalErrorFull() instead")
    void customVitalsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customVitalsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsCreateSignalErrorFull() instead")
    void documentsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsDeleteSignalErrorFull() instead")
    void documentsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsListSignalErrorFull() instead")
    void documentsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsPartialUpdateSignalErrorFull() instead")
    void documentsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsReadSignalErrorFull() instead")
    void documentsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsUpdateSignalErrorFull() instead")
    void documentsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eobsCreateSignalErrorFull() instead")
    void eobsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void eobsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eobsListSignalErrorFull() instead")
    void eobsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void eobsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eobsReadSignalErrorFull() instead")
    void eobsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void eobsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use feeSchedulesListSignalErrorFull() instead")
    void feeSchedulesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void feeSchedulesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use feeSchedulesReadSignalErrorFull() instead")
    void feeSchedulesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void feeSchedulesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use implantableDevicesListSignalErrorFull() instead")
    void implantableDevicesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void implantableDevicesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use implantableDevicesReadSignalErrorFull() instead")
    void implantableDevicesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void implantableDevicesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use insurancesListSignalErrorFull() instead")
    void insurancesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void insurancesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use insurancesReadSignalErrorFull() instead")
    void insurancesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void insurancesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labDocumentsCreateSignalErrorFull() instead")
    void labDocumentsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labDocumentsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labDocumentsDeleteSignalErrorFull() instead")
    void labDocumentsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labDocumentsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labDocumentsListSignalErrorFull() instead")
    void labDocumentsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labDocumentsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labDocumentsPartialUpdateSignalErrorFull() instead")
    void labDocumentsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labDocumentsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labDocumentsReadSignalErrorFull() instead")
    void labDocumentsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labDocumentsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labDocumentsUpdateSignalErrorFull() instead")
    void labDocumentsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labDocumentsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersCreateSignalErrorFull() instead")
    void labOrdersCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersDeleteSignalErrorFull() instead")
    void labOrdersDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersListSignalErrorFull() instead")
    void labOrdersListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersPartialUpdateSignalErrorFull() instead")
    void labOrdersPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersReadSignalErrorFull() instead")
    void labOrdersReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersSummaryListSignalErrorFull() instead")
    void labOrdersSummaryListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersSummaryListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersSummaryReadSignalErrorFull() instead")
    void labOrdersSummaryReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersSummaryReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labOrdersUpdateSignalErrorFull() instead")
    void labOrdersUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labOrdersUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labResultsCreateSignalErrorFull() instead")
    void labResultsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labResultsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labResultsDeleteSignalErrorFull() instead")
    void labResultsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labResultsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labResultsListSignalErrorFull() instead")
    void labResultsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labResultsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labResultsPartialUpdateSignalErrorFull() instead")
    void labResultsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labResultsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labResultsReadSignalErrorFull() instead")
    void labResultsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labResultsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labResultsUpdateSignalErrorFull() instead")
    void labResultsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labResultsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labTestsCreateSignalErrorFull() instead")
    void labTestsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labTestsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labTestsDeleteSignalErrorFull() instead")
    void labTestsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labTestsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labTestsListSignalErrorFull() instead")
    void labTestsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labTestsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labTestsPartialUpdateSignalErrorFull() instead")
    void labTestsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labTestsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labTestsReadSignalErrorFull() instead")
    void labTestsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labTestsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use labTestsUpdateSignalErrorFull() instead")
    void labTestsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void labTestsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use medicationsAppendToPharmacyNoteSignalErrorFull() instead")
    void medicationsAppendToPharmacyNoteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void medicationsAppendToPharmacyNoteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use medicationsCreateSignalErrorFull() instead")
    void medicationsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void medicationsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use medicationsListSignalErrorFull() instead")
    void medicationsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void medicationsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use medicationsPartialUpdateSignalErrorFull() instead")
    void medicationsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void medicationsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use medicationsReadSignalErrorFull() instead")
    void medicationsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void medicationsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use medicationsUpdateSignalErrorFull() instead")
    void medicationsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void medicationsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientCommunicationsCreateSignalErrorFull() instead")
    void patientCommunicationsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientCommunicationsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientCommunicationsListSignalErrorFull() instead")
    void patientCommunicationsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientCommunicationsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientCommunicationsPartialUpdateSignalErrorFull() instead")
    void patientCommunicationsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientCommunicationsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientCommunicationsReadSignalErrorFull() instead")
    void patientCommunicationsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientCommunicationsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientCommunicationsUpdateSignalErrorFull() instead")
    void patientCommunicationsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientCommunicationsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientFlagTypesCreateSignalErrorFull() instead")
    void patientFlagTypesCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientFlagTypesCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientFlagTypesListSignalErrorFull() instead")
    void patientFlagTypesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientFlagTypesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientFlagTypesPartialUpdateSignalErrorFull() instead")
    void patientFlagTypesPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientFlagTypesPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientFlagTypesReadSignalErrorFull() instead")
    void patientFlagTypesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientFlagTypesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientFlagTypesUpdateSignalErrorFull() instead")
    void patientFlagTypesUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientFlagTypesUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientInterventionsCreateSignalErrorFull() instead")
    void patientInterventionsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientInterventionsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientInterventionsListSignalErrorFull() instead")
    void patientInterventionsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientInterventionsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientInterventionsPartialUpdateSignalErrorFull() instead")
    void patientInterventionsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientInterventionsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientInterventionsReadSignalErrorFull() instead")
    void patientInterventionsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientInterventionsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientInterventionsUpdateSignalErrorFull() instead")
    void patientInterventionsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientInterventionsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientLabResultsCreateSignalErrorFull() instead")
    void patientLabResultsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientLabResultsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientLabResultsDeleteSignalErrorFull() instead")
    void patientLabResultsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientLabResultsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientLabResultsListSignalErrorFull() instead")
    void patientLabResultsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientLabResultsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientLabResultsPartialUpdateSignalErrorFull() instead")
    void patientLabResultsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientLabResultsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientLabResultsReadSignalErrorFull() instead")
    void patientLabResultsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientLabResultsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientLabResultsUpdateSignalErrorFull() instead")
    void patientLabResultsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientLabResultsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientMessagesCreateSignalErrorFull() instead")
    void patientMessagesCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientMessagesCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientMessagesListSignalErrorFull() instead")
    void patientMessagesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientMessagesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientMessagesPartialUpdateSignalErrorFull() instead")
    void patientMessagesPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientMessagesPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientMessagesReadSignalErrorFull() instead")
    void patientMessagesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientMessagesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientMessagesUpdateSignalErrorFull() instead")
    void patientMessagesUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientMessagesUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPhysicalExamsCreateSignalErrorFull() instead")
    void patientPhysicalExamsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPhysicalExamsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPhysicalExamsListSignalErrorFull() instead")
    void patientPhysicalExamsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPhysicalExamsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPhysicalExamsPartialUpdateSignalErrorFull() instead")
    void patientPhysicalExamsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPhysicalExamsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPhysicalExamsReadSignalErrorFull() instead")
    void patientPhysicalExamsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPhysicalExamsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPhysicalExamsUpdateSignalErrorFull() instead")
    void patientPhysicalExamsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPhysicalExamsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientRiskAssessmentsCreateSignalErrorFull() instead")
    void patientRiskAssessmentsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientRiskAssessmentsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientRiskAssessmentsListSignalErrorFull() instead")
    void patientRiskAssessmentsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientRiskAssessmentsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientRiskAssessmentsPartialUpdateSignalErrorFull() instead")
    void patientRiskAssessmentsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientRiskAssessmentsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientRiskAssessmentsReadSignalErrorFull() instead")
    void patientRiskAssessmentsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientRiskAssessmentsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientRiskAssessmentsUpdateSignalErrorFull() instead")
    void patientRiskAssessmentsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientRiskAssessmentsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientVaccineRecordsCreateSignalErrorFull() instead")
    void patientVaccineRecordsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientVaccineRecordsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientVaccineRecordsListSignalErrorFull() instead")
    void patientVaccineRecordsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientVaccineRecordsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientVaccineRecordsPartialUpdateSignalErrorFull() instead")
    void patientVaccineRecordsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientVaccineRecordsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientVaccineRecordsReadSignalErrorFull() instead")
    void patientVaccineRecordsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientVaccineRecordsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientVaccineRecordsUpdateSignalErrorFull() instead")
    void patientVaccineRecordsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientVaccineRecordsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsCcdaSignalErrorFull() instead")
    void patientsCcdaSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsCcdaSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsCreateSignalErrorFull() instead")
    void patientsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsDeleteSignalErrorFull() instead")
    void patientsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsListSignalErrorFull() instead")
    void patientsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsOnpatientAccessCreateSignalErrorFull() instead")
    void patientsOnpatientAccessCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsOnpatientAccessCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsOnpatientAccessDeleteSignalErrorFull() instead")
    void patientsOnpatientAccessDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsOnpatientAccessDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsOnpatientAccessReadSignalErrorFull() instead")
    void patientsOnpatientAccessReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsOnpatientAccessReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsPartialUpdateSignalErrorFull() instead")
    void patientsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsQrda1SignalErrorFull() instead")
    void patientsQrda1SignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsQrda1SignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsReadSignalErrorFull() instead")
    void patientsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsSummaryCreateSignalErrorFull() instead")
    void patientsSummaryCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsSummaryCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsSummaryDeleteSignalErrorFull() instead")
    void patientsSummaryDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsSummaryDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsSummaryListSignalErrorFull() instead")
    void patientsSummaryListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsSummaryListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsSummaryPartialUpdateSignalErrorFull() instead")
    void patientsSummaryPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsSummaryPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsSummaryReadSignalErrorFull() instead")
    void patientsSummaryReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsSummaryReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsSummaryUpdateSignalErrorFull() instead")
    void patientsSummaryUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsSummaryUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientsUpdateSignalErrorFull() instead")
    void patientsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use prescriptionMessagesListSignalErrorFull() instead")
    void prescriptionMessagesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void prescriptionMessagesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use prescriptionMessagesReadSignalErrorFull() instead")
    void prescriptionMessagesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void prescriptionMessagesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use problemsCreateSignalErrorFull() instead")
    void problemsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void problemsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use problemsListSignalErrorFull() instead")
    void problemsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void problemsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use problemsPartialUpdateSignalErrorFull() instead")
    void problemsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void problemsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use problemsReadSignalErrorFull() instead")
    void problemsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void problemsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use problemsUpdateSignalErrorFull() instead")
    void problemsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void problemsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reminderProfilesCreateSignalErrorFull() instead")
    void reminderProfilesCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reminderProfilesCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reminderProfilesDeleteSignalErrorFull() instead")
    void reminderProfilesDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reminderProfilesDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reminderProfilesListSignalErrorFull() instead")
    void reminderProfilesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reminderProfilesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reminderProfilesPartialUpdateSignalErrorFull() instead")
    void reminderProfilesPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reminderProfilesPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reminderProfilesReadSignalErrorFull() instead")
    void reminderProfilesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reminderProfilesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reminderProfilesUpdateSignalErrorFull() instead")
    void reminderProfilesUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reminderProfilesUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sublabsCreateSignalErrorFull() instead")
    void sublabsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sublabsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sublabsDeleteSignalErrorFull() instead")
    void sublabsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sublabsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sublabsListSignalErrorFull() instead")
    void sublabsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sublabsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sublabsPartialUpdateSignalErrorFull() instead")
    void sublabsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sublabsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sublabsReadSignalErrorFull() instead")
    void sublabsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sublabsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sublabsUpdateSignalErrorFull() instead")
    void sublabsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sublabsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
