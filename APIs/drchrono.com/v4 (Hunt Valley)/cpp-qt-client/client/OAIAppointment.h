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

/*
 * OAIAppointment.h
 *
 * 
 */

#ifndef OAIAppointment_H
#define OAIAppointment_H

#include <QJsonObject>

#include "OAIAppointmentStatusTransition.h"
#include "OAIClaimBillingNotes_1.h"
#include "OAIClinicalNote_1.h"
#include "OAICustomAppointmentFieldValue.h"
#include "OAICustomVitalValue.h"
#include "OAISimpleReminder.h"
#include "OAISystemVitals.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIClaimBillingNotes_1;
class OAIClinicalNote_1;
class OAICustomAppointmentFieldValue;
class OAICustomVitalValue;
class OAISimpleReminder;
class OAIAppointmentStatusTransition;
class OAISystemVitals;

class OAIAppointment : public OAIObject {
public:
    OAIAppointment();
    OAIAppointment(QString json);
    ~OAIAppointment() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAllowOverlapping() const;
    void setAllowOverlapping(const bool &allow_overlapping);
    bool is_allow_overlapping_Set() const;
    bool is_allow_overlapping_Valid() const;

    bool isApptIsBreak() const;
    void setApptIsBreak(const bool &appt_is_break);
    bool is_appt_is_break_Set() const;
    bool is_appt_is_break_Valid() const;

    QString getBaseRecurringAppointment() const;
    void setBaseRecurringAppointment(const QString &base_recurring_appointment);
    bool is_base_recurring_appointment_Set() const;
    bool is_base_recurring_appointment_Valid() const;

    QList<OAIClaimBillingNotes_1> getBillingNotes() const;
    void setBillingNotes(const QList<OAIClaimBillingNotes_1> &billing_notes);
    bool is_billing_notes_Set() const;
    bool is_billing_notes_Valid() const;

    QString getBillingProvider() const;
    void setBillingProvider(const QString &billing_provider);
    bool is_billing_provider_Set() const;
    bool is_billing_provider_Valid() const;

    QString getBillingStatus() const;
    void setBillingStatus(const QString &billing_status);
    bool is_billing_status_Set() const;
    bool is_billing_status_Valid() const;

    OAIClinicalNote_1 getClinicalNote() const;
    void setClinicalNote(const OAIClinicalNote_1 &clinical_note);
    bool is_clinical_note_Set() const;
    bool is_clinical_note_Valid() const;

    qint32 getClonedFrom() const;
    void setClonedFrom(const qint32 &cloned_from);
    bool is_cloned_from_Set() const;
    bool is_cloned_from_Valid() const;

    QString getColor() const;
    void setColor(const QString &color);
    bool is_color_Set() const;
    bool is_color_Valid() const;

    QString getCreatedAt() const;
    void setCreatedAt(const QString &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QList<OAICustomAppointmentFieldValue> getCustomFields() const;
    void setCustomFields(const QList<OAICustomAppointmentFieldValue> &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QList<OAICustomVitalValue> getCustomVitals() const;
    void setCustomVitals(const QList<OAICustomVitalValue> &custom_vitals);
    bool is_custom_vitals_Set() const;
    bool is_custom_vitals_Valid() const;

    bool isDeletedFlag() const;
    void setDeletedFlag(const bool &deleted_flag);
    bool is_deleted_flag_Set() const;
    bool is_deleted_flag_Valid() const;

    qint32 getDoctor() const;
    void setDoctor(const qint32 &doctor);
    bool is_doctor_Set() const;
    bool is_doctor_Valid() const;

    qint32 getDuration() const;
    void setDuration(const qint32 &duration);
    bool is_duration_Set() const;
    bool is_duration_Valid() const;

    qint32 getExamRoom() const;
    void setExamRoom(const qint32 &exam_room);
    bool is_exam_room_Set() const;
    bool is_exam_room_Valid() const;

    QString getExtendedUpdatedAt() const;
    void setExtendedUpdatedAt(const QString &extended_updated_at);
    bool is_extended_updated_at_Set() const;
    bool is_extended_updated_at_Valid() const;

    QString getFirstBilledDate() const;
    void setFirstBilledDate(const QString &first_billed_date);
    bool is_first_billed_date_Set() const;
    bool is_first_billed_date_Valid() const;

    QList<QString> getIcd10Codes() const;
    void setIcd10Codes(const QList<QString> &icd10_codes);
    bool is_icd10_codes_Set() const;
    bool is_icd10_codes_Valid() const;

    QList<QString> getIcd9Codes() const;
    void setIcd9Codes(const QList<QString> &icd9_codes);
    bool is_icd9_codes_Set() const;
    bool is_icd9_codes_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getIns1Status() const;
    void setIns1Status(const QString &ins1_status);
    bool is_ins1_status_Set() const;
    bool is_ins1_status_Valid() const;

    QString getIns2Status() const;
    void setIns2Status(const QString &ins2_status);
    bool is_ins2_status_Set() const;
    bool is_ins2_status_Valid() const;

    bool isIsVirtualBase() const;
    void setIsVirtualBase(const bool &is_virtual_base);
    bool is_is_virtual_base_Set() const;
    bool is_is_virtual_base_Valid() const;

    bool isIsWalkIn() const;
    void setIsWalkIn(const bool &is_walk_in);
    bool is_is_walk_in_Set() const;
    bool is_is_walk_in_Valid() const;

    QString getLastBilledDate() const;
    void setLastBilledDate(const QString &last_billed_date);
    bool is_last_billed_date_Set() const;
    bool is_last_billed_date_Valid() const;

    QString getNotes() const;
    void setNotes(const QString &notes);
    bool is_notes_Set() const;
    bool is_notes_Valid() const;

    qint32 getOffice() const;
    void setOffice(const qint32 &office);
    bool is_office_Set() const;
    bool is_office_Valid() const;

    qint32 getPatient() const;
    void setPatient(const qint32 &patient);
    bool is_patient_Set() const;
    bool is_patient_Valid() const;

    QString getPrimaryInsuranceIdNumber() const;
    void setPrimaryInsuranceIdNumber(const QString &primary_insurance_id_number);
    bool is_primary_insurance_id_number_Set() const;
    bool is_primary_insurance_id_number_Valid() const;

    QString getPrimaryInsurerName() const;
    void setPrimaryInsurerName(const QString &primary_insurer_name);
    bool is_primary_insurer_name_Set() const;
    bool is_primary_insurer_name_Valid() const;

    QString getPrimaryInsurerPayerId() const;
    void setPrimaryInsurerPayerId(const QString &primary_insurer_payer_id);
    bool is_primary_insurer_payer_id_Set() const;
    bool is_primary_insurer_payer_id_Valid() const;

    qint32 getProfile() const;
    void setProfile(const qint32 &profile);
    bool is_profile_Set() const;
    bool is_profile_Valid() const;

    QString getReason() const;
    void setReason(const QString &reason);
    bool is_reason_Set() const;
    bool is_reason_Valid() const;

    bool isRecurringAppointment() const;
    void setRecurringAppointment(const bool &recurring_appointment);
    bool is_recurring_appointment_Set() const;
    bool is_recurring_appointment_Valid() const;

    QString getReminderProfile() const;
    void setReminderProfile(const QString &reminder_profile);
    bool is_reminder_profile_Set() const;
    bool is_reminder_profile_Valid() const;

    QList<OAISimpleReminder> getReminders() const;
    void setReminders(const QList<OAISimpleReminder> &reminders);
    bool is_reminders_Set() const;
    bool is_reminders_Valid() const;

    QString getScheduledTime() const;
    void setScheduledTime(const QString &scheduled_time);
    bool is_scheduled_time_Set() const;
    bool is_scheduled_time_Valid() const;

    QString getSecondaryInsuranceIdNumber() const;
    void setSecondaryInsuranceIdNumber(const QString &secondary_insurance_id_number);
    bool is_secondary_insurance_id_number_Set() const;
    bool is_secondary_insurance_id_number_Valid() const;

    QString getSecondaryInsurerName() const;
    void setSecondaryInsurerName(const QString &secondary_insurer_name);
    bool is_secondary_insurer_name_Set() const;
    bool is_secondary_insurer_name_Valid() const;

    QString getSecondaryInsurerPayerId() const;
    void setSecondaryInsurerPayerId(const QString &secondary_insurer_payer_id);
    bool is_secondary_insurer_payer_id_Set() const;
    bool is_secondary_insurer_payer_id_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QList<OAIAppointmentStatusTransition> getStatusTransitions() const;
    void setStatusTransitions(const QList<OAIAppointmentStatusTransition> &status_transitions);
    bool is_status_transitions_Set() const;
    bool is_status_transitions_Valid() const;

    QString getSupervisingProvider() const;
    void setSupervisingProvider(const QString &supervising_provider);
    bool is_supervising_provider_Set() const;
    bool is_supervising_provider_Valid() const;

    QString getUpdatedAt() const;
    void setUpdatedAt(const QString &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    OAISystemVitals getVitals() const;
    void setVitals(const OAISystemVitals &vitals);
    bool is_vitals_Set() const;
    bool is_vitals_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_allow_overlapping;
    bool m_allow_overlapping_isSet;
    bool m_allow_overlapping_isValid;

    bool m_appt_is_break;
    bool m_appt_is_break_isSet;
    bool m_appt_is_break_isValid;

    QString m_base_recurring_appointment;
    bool m_base_recurring_appointment_isSet;
    bool m_base_recurring_appointment_isValid;

    QList<OAIClaimBillingNotes_1> m_billing_notes;
    bool m_billing_notes_isSet;
    bool m_billing_notes_isValid;

    QString m_billing_provider;
    bool m_billing_provider_isSet;
    bool m_billing_provider_isValid;

    QString m_billing_status;
    bool m_billing_status_isSet;
    bool m_billing_status_isValid;

    OAIClinicalNote_1 m_clinical_note;
    bool m_clinical_note_isSet;
    bool m_clinical_note_isValid;

    qint32 m_cloned_from;
    bool m_cloned_from_isSet;
    bool m_cloned_from_isValid;

    QString m_color;
    bool m_color_isSet;
    bool m_color_isValid;

    QString m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QList<OAICustomAppointmentFieldValue> m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QList<OAICustomVitalValue> m_custom_vitals;
    bool m_custom_vitals_isSet;
    bool m_custom_vitals_isValid;

    bool m_deleted_flag;
    bool m_deleted_flag_isSet;
    bool m_deleted_flag_isValid;

    qint32 m_doctor;
    bool m_doctor_isSet;
    bool m_doctor_isValid;

    qint32 m_duration;
    bool m_duration_isSet;
    bool m_duration_isValid;

    qint32 m_exam_room;
    bool m_exam_room_isSet;
    bool m_exam_room_isValid;

    QString m_extended_updated_at;
    bool m_extended_updated_at_isSet;
    bool m_extended_updated_at_isValid;

    QString m_first_billed_date;
    bool m_first_billed_date_isSet;
    bool m_first_billed_date_isValid;

    QList<QString> m_icd10_codes;
    bool m_icd10_codes_isSet;
    bool m_icd10_codes_isValid;

    QList<QString> m_icd9_codes;
    bool m_icd9_codes_isSet;
    bool m_icd9_codes_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_ins1_status;
    bool m_ins1_status_isSet;
    bool m_ins1_status_isValid;

    QString m_ins2_status;
    bool m_ins2_status_isSet;
    bool m_ins2_status_isValid;

    bool m_is_virtual_base;
    bool m_is_virtual_base_isSet;
    bool m_is_virtual_base_isValid;

    bool m_is_walk_in;
    bool m_is_walk_in_isSet;
    bool m_is_walk_in_isValid;

    QString m_last_billed_date;
    bool m_last_billed_date_isSet;
    bool m_last_billed_date_isValid;

    QString m_notes;
    bool m_notes_isSet;
    bool m_notes_isValid;

    qint32 m_office;
    bool m_office_isSet;
    bool m_office_isValid;

    qint32 m_patient;
    bool m_patient_isSet;
    bool m_patient_isValid;

    QString m_primary_insurance_id_number;
    bool m_primary_insurance_id_number_isSet;
    bool m_primary_insurance_id_number_isValid;

    QString m_primary_insurer_name;
    bool m_primary_insurer_name_isSet;
    bool m_primary_insurer_name_isValid;

    QString m_primary_insurer_payer_id;
    bool m_primary_insurer_payer_id_isSet;
    bool m_primary_insurer_payer_id_isValid;

    qint32 m_profile;
    bool m_profile_isSet;
    bool m_profile_isValid;

    QString m_reason;
    bool m_reason_isSet;
    bool m_reason_isValid;

    bool m_recurring_appointment;
    bool m_recurring_appointment_isSet;
    bool m_recurring_appointment_isValid;

    QString m_reminder_profile;
    bool m_reminder_profile_isSet;
    bool m_reminder_profile_isValid;

    QList<OAISimpleReminder> m_reminders;
    bool m_reminders_isSet;
    bool m_reminders_isValid;

    QString m_scheduled_time;
    bool m_scheduled_time_isSet;
    bool m_scheduled_time_isValid;

    QString m_secondary_insurance_id_number;
    bool m_secondary_insurance_id_number_isSet;
    bool m_secondary_insurance_id_number_isValid;

    QString m_secondary_insurer_name;
    bool m_secondary_insurer_name_isSet;
    bool m_secondary_insurer_name_isValid;

    QString m_secondary_insurer_payer_id;
    bool m_secondary_insurer_payer_id_isSet;
    bool m_secondary_insurer_payer_id_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QList<OAIAppointmentStatusTransition> m_status_transitions;
    bool m_status_transitions_isSet;
    bool m_status_transitions_isValid;

    QString m_supervising_provider;
    bool m_supervising_provider_isSet;
    bool m_supervising_provider_isValid;

    QString m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;

    OAISystemVitals m_vitals;
    bool m_vitals_isSet;
    bool m_vitals_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppointment)

#endif // OAIAppointment_H
