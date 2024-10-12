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

#ifndef OAI_OAIBillingApi_H
#define OAI_OAIBillingApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBillingLineItem.h"
#include "OAIBillingProfile.h"
#include "OAIBilling_profiles_list_200_response.h"
#include "OAICashPayment.h"
#include "OAICashPaymentLog.h"
#include "OAIComm_logs_list_200_response.h"
#include "OAICoverage.h"
#include "OAICustomInsurancePlanName.h"
#include "OAICustom_insurance_plan_names_list_200_response.h"
#include "OAIEligibility_checks_list_200_response.h"
#include "OAILineItemTransaction.h"
#include "OAILine_items_list_200_response.h"
#include "OAIPatient_payment_log_list_200_response.h"
#include "OAIPatient_payments_list_200_response.h"
#include "OAIPhoneCallLog.h"
#include "OAITransactions_list_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIBillingApi : public QObject {
    Q_OBJECT

public:
    OAIBillingApi(const int timeOut = 0);
    ~OAIBillingApi();

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
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void billingProfilesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void billingProfilesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void commLogsCreate(const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void commLogsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void commLogsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void commLogsRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void commLogsUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  user qint32 [optional]
    * @param[in]  name QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void customInsurancePlanNamesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  user qint32 [optional]
    * @param[in]  name QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void customInsurancePlanNamesRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  appointment_date QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  query_date_range QString [optional]
    * @param[in]  appointment_date_range QString [optional]
    * @param[in]  query_date QString [optional]
    * @param[in]  patient qint32 [optional]
    */
    virtual void eligibilityChecksList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &appointment_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &query_date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &appointment_date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &query_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  appointment_date QString [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  query_date_range QString [optional]
    * @param[in]  appointment_date_range QString [optional]
    * @param[in]  query_date QString [optional]
    * @param[in]  patient qint32 [optional]
    */
    virtual void eligibilityChecksRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &appointment_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &query_date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &appointment_date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &query_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  posted_date QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  service_date QString [optional]
    */
    virtual void lineItemsCreate(const ::OpenAPI::OptionalParam<QString> &posted_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &service_date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  posted_date QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  service_date QString [optional]
    */
    virtual void lineItemsDelete(const QString &id, const ::OpenAPI::OptionalParam<QString> &posted_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &service_date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  posted_date QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  service_date QString [optional]
    */
    virtual void lineItemsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &posted_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &service_date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  posted_date QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  service_date QString [optional]
    */
    virtual void lineItemsPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &posted_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &service_date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  posted_date QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  service_date QString [optional]
    */
    virtual void lineItemsRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &posted_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &service_date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  posted_date QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  service_date QString [optional]
    */
    virtual void lineItemsUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &posted_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &service_date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientPaymentLogList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  office qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientPaymentLogRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &office = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientPaymentsCreate(const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientPaymentsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void patientPaymentsRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  mu_date QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  mu_date_range QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  service_date QString [optional]
    */
    virtual void proceduresList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &mu_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &mu_date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &service_date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  mu_date QString [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  mu_date_range QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  service_date QString [optional]
    */
    virtual void proceduresRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &mu_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &mu_date_range = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &service_date = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  line_item qint32 [optional]
    * @param[in]  posted_date QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void transactionsList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &line_item = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &posted_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  line_item qint32 [optional]
    * @param[in]  posted_date QString [optional]
    * @param[in]  appointment qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void transactionsRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &line_item = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &posted_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &appointment = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());


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

    void billingProfilesListCallback(OAIHttpRequestWorker *worker);
    void billingProfilesReadCallback(OAIHttpRequestWorker *worker);
    void commLogsCreateCallback(OAIHttpRequestWorker *worker);
    void commLogsListCallback(OAIHttpRequestWorker *worker);
    void commLogsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void commLogsReadCallback(OAIHttpRequestWorker *worker);
    void commLogsUpdateCallback(OAIHttpRequestWorker *worker);
    void customInsurancePlanNamesListCallback(OAIHttpRequestWorker *worker);
    void customInsurancePlanNamesReadCallback(OAIHttpRequestWorker *worker);
    void eligibilityChecksListCallback(OAIHttpRequestWorker *worker);
    void eligibilityChecksReadCallback(OAIHttpRequestWorker *worker);
    void lineItemsCreateCallback(OAIHttpRequestWorker *worker);
    void lineItemsDeleteCallback(OAIHttpRequestWorker *worker);
    void lineItemsListCallback(OAIHttpRequestWorker *worker);
    void lineItemsPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void lineItemsReadCallback(OAIHttpRequestWorker *worker);
    void lineItemsUpdateCallback(OAIHttpRequestWorker *worker);
    void patientPaymentLogListCallback(OAIHttpRequestWorker *worker);
    void patientPaymentLogReadCallback(OAIHttpRequestWorker *worker);
    void patientPaymentsCreateCallback(OAIHttpRequestWorker *worker);
    void patientPaymentsListCallback(OAIHttpRequestWorker *worker);
    void patientPaymentsReadCallback(OAIHttpRequestWorker *worker);
    void proceduresListCallback(OAIHttpRequestWorker *worker);
    void proceduresReadCallback(OAIHttpRequestWorker *worker);
    void transactionsListCallback(OAIHttpRequestWorker *worker);
    void transactionsReadCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void billingProfilesListSignal(OAIBilling_profiles_list_200_response summary);
    void billingProfilesReadSignal(OAIBillingProfile summary);
    void commLogsCreateSignal(OAIPhoneCallLog summary);
    void commLogsListSignal(OAIComm_logs_list_200_response summary);
    void commLogsPartialUpdateSignal();
    void commLogsReadSignal(OAIPhoneCallLog summary);
    void commLogsUpdateSignal();
    void customInsurancePlanNamesListSignal(OAICustom_insurance_plan_names_list_200_response summary);
    void customInsurancePlanNamesReadSignal(OAICustomInsurancePlanName summary);
    void eligibilityChecksListSignal(OAIEligibility_checks_list_200_response summary);
    void eligibilityChecksReadSignal(OAICoverage summary);
    void lineItemsCreateSignal(OAIBillingLineItem summary);
    void lineItemsDeleteSignal();
    void lineItemsListSignal(OAILine_items_list_200_response summary);
    void lineItemsPartialUpdateSignal();
    void lineItemsReadSignal(OAIBillingLineItem summary);
    void lineItemsUpdateSignal();
    void patientPaymentLogListSignal(OAIPatient_payment_log_list_200_response summary);
    void patientPaymentLogReadSignal(OAICashPaymentLog summary);
    void patientPaymentsCreateSignal(OAICashPayment summary);
    void patientPaymentsListSignal(OAIPatient_payments_list_200_response summary);
    void patientPaymentsReadSignal(OAICashPayment summary);
    void proceduresListSignal(OAILine_items_list_200_response summary);
    void proceduresReadSignal(OAIBillingLineItem summary);
    void transactionsListSignal(OAITransactions_list_200_response summary);
    void transactionsReadSignal(OAILineItemTransaction summary);


    void billingProfilesListSignalFull(OAIHttpRequestWorker *worker, OAIBilling_profiles_list_200_response summary);
    void billingProfilesReadSignalFull(OAIHttpRequestWorker *worker, OAIBillingProfile summary);
    void commLogsCreateSignalFull(OAIHttpRequestWorker *worker, OAIPhoneCallLog summary);
    void commLogsListSignalFull(OAIHttpRequestWorker *worker, OAIComm_logs_list_200_response summary);
    void commLogsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void commLogsReadSignalFull(OAIHttpRequestWorker *worker, OAIPhoneCallLog summary);
    void commLogsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void customInsurancePlanNamesListSignalFull(OAIHttpRequestWorker *worker, OAICustom_insurance_plan_names_list_200_response summary);
    void customInsurancePlanNamesReadSignalFull(OAIHttpRequestWorker *worker, OAICustomInsurancePlanName summary);
    void eligibilityChecksListSignalFull(OAIHttpRequestWorker *worker, OAIEligibility_checks_list_200_response summary);
    void eligibilityChecksReadSignalFull(OAIHttpRequestWorker *worker, OAICoverage summary);
    void lineItemsCreateSignalFull(OAIHttpRequestWorker *worker, OAIBillingLineItem summary);
    void lineItemsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void lineItemsListSignalFull(OAIHttpRequestWorker *worker, OAILine_items_list_200_response summary);
    void lineItemsPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void lineItemsReadSignalFull(OAIHttpRequestWorker *worker, OAIBillingLineItem summary);
    void lineItemsUpdateSignalFull(OAIHttpRequestWorker *worker);
    void patientPaymentLogListSignalFull(OAIHttpRequestWorker *worker, OAIPatient_payment_log_list_200_response summary);
    void patientPaymentLogReadSignalFull(OAIHttpRequestWorker *worker, OAICashPaymentLog summary);
    void patientPaymentsCreateSignalFull(OAIHttpRequestWorker *worker, OAICashPayment summary);
    void patientPaymentsListSignalFull(OAIHttpRequestWorker *worker, OAIPatient_payments_list_200_response summary);
    void patientPaymentsReadSignalFull(OAIHttpRequestWorker *worker, OAICashPayment summary);
    void proceduresListSignalFull(OAIHttpRequestWorker *worker, OAILine_items_list_200_response summary);
    void proceduresReadSignalFull(OAIHttpRequestWorker *worker, OAIBillingLineItem summary);
    void transactionsListSignalFull(OAIHttpRequestWorker *worker, OAITransactions_list_200_response summary);
    void transactionsReadSignalFull(OAIHttpRequestWorker *worker, OAILineItemTransaction summary);

    Q_DECL_DEPRECATED_X("Use billingProfilesListSignalError() instead")
    void billingProfilesListSignalE(OAIBilling_profiles_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void billingProfilesListSignalError(OAIBilling_profiles_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use billingProfilesReadSignalError() instead")
    void billingProfilesReadSignalE(OAIBillingProfile summary, QNetworkReply::NetworkError error_type, QString error_str);
    void billingProfilesReadSignalError(OAIBillingProfile summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use commLogsCreateSignalError() instead")
    void commLogsCreateSignalE(OAIPhoneCallLog summary, QNetworkReply::NetworkError error_type, QString error_str);
    void commLogsCreateSignalError(OAIPhoneCallLog summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use commLogsListSignalError() instead")
    void commLogsListSignalE(OAIComm_logs_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void commLogsListSignalError(OAIComm_logs_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use commLogsPartialUpdateSignalError() instead")
    void commLogsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void commLogsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use commLogsReadSignalError() instead")
    void commLogsReadSignalE(OAIPhoneCallLog summary, QNetworkReply::NetworkError error_type, QString error_str);
    void commLogsReadSignalError(OAIPhoneCallLog summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use commLogsUpdateSignalError() instead")
    void commLogsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void commLogsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customInsurancePlanNamesListSignalError() instead")
    void customInsurancePlanNamesListSignalE(OAICustom_insurance_plan_names_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customInsurancePlanNamesListSignalError(OAICustom_insurance_plan_names_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customInsurancePlanNamesReadSignalError() instead")
    void customInsurancePlanNamesReadSignalE(OAICustomInsurancePlanName summary, QNetworkReply::NetworkError error_type, QString error_str);
    void customInsurancePlanNamesReadSignalError(OAICustomInsurancePlanName summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eligibilityChecksListSignalError() instead")
    void eligibilityChecksListSignalE(OAIEligibility_checks_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void eligibilityChecksListSignalError(OAIEligibility_checks_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eligibilityChecksReadSignalError() instead")
    void eligibilityChecksReadSignalE(OAICoverage summary, QNetworkReply::NetworkError error_type, QString error_str);
    void eligibilityChecksReadSignalError(OAICoverage summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lineItemsCreateSignalError() instead")
    void lineItemsCreateSignalE(OAIBillingLineItem summary, QNetworkReply::NetworkError error_type, QString error_str);
    void lineItemsCreateSignalError(OAIBillingLineItem summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lineItemsDeleteSignalError() instead")
    void lineItemsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void lineItemsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lineItemsListSignalError() instead")
    void lineItemsListSignalE(OAILine_items_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void lineItemsListSignalError(OAILine_items_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lineItemsPartialUpdateSignalError() instead")
    void lineItemsPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void lineItemsPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lineItemsReadSignalError() instead")
    void lineItemsReadSignalE(OAIBillingLineItem summary, QNetworkReply::NetworkError error_type, QString error_str);
    void lineItemsReadSignalError(OAIBillingLineItem summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lineItemsUpdateSignalError() instead")
    void lineItemsUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void lineItemsUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPaymentLogListSignalError() instead")
    void patientPaymentLogListSignalE(OAIPatient_payment_log_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPaymentLogListSignalError(OAIPatient_payment_log_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPaymentLogReadSignalError() instead")
    void patientPaymentLogReadSignalE(OAICashPaymentLog summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPaymentLogReadSignalError(OAICashPaymentLog summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPaymentsCreateSignalError() instead")
    void patientPaymentsCreateSignalE(OAICashPayment summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPaymentsCreateSignalError(OAICashPayment summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPaymentsListSignalError() instead")
    void patientPaymentsListSignalE(OAIPatient_payments_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPaymentsListSignalError(OAIPatient_payments_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPaymentsReadSignalError() instead")
    void patientPaymentsReadSignalE(OAICashPayment summary, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPaymentsReadSignalError(OAICashPayment summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use proceduresListSignalError() instead")
    void proceduresListSignalE(OAILine_items_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void proceduresListSignalError(OAILine_items_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use proceduresReadSignalError() instead")
    void proceduresReadSignalE(OAIBillingLineItem summary, QNetworkReply::NetworkError error_type, QString error_str);
    void proceduresReadSignalError(OAIBillingLineItem summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use transactionsListSignalError() instead")
    void transactionsListSignalE(OAITransactions_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void transactionsListSignalError(OAITransactions_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use transactionsReadSignalError() instead")
    void transactionsReadSignalE(OAILineItemTransaction summary, QNetworkReply::NetworkError error_type, QString error_str);
    void transactionsReadSignalError(OAILineItemTransaction summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use billingProfilesListSignalErrorFull() instead")
    void billingProfilesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void billingProfilesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use billingProfilesReadSignalErrorFull() instead")
    void billingProfilesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void billingProfilesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use commLogsCreateSignalErrorFull() instead")
    void commLogsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void commLogsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use commLogsListSignalErrorFull() instead")
    void commLogsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void commLogsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use commLogsPartialUpdateSignalErrorFull() instead")
    void commLogsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void commLogsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use commLogsReadSignalErrorFull() instead")
    void commLogsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void commLogsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use commLogsUpdateSignalErrorFull() instead")
    void commLogsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void commLogsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customInsurancePlanNamesListSignalErrorFull() instead")
    void customInsurancePlanNamesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customInsurancePlanNamesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use customInsurancePlanNamesReadSignalErrorFull() instead")
    void customInsurancePlanNamesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void customInsurancePlanNamesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eligibilityChecksListSignalErrorFull() instead")
    void eligibilityChecksListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void eligibilityChecksListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use eligibilityChecksReadSignalErrorFull() instead")
    void eligibilityChecksReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void eligibilityChecksReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lineItemsCreateSignalErrorFull() instead")
    void lineItemsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void lineItemsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lineItemsDeleteSignalErrorFull() instead")
    void lineItemsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void lineItemsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lineItemsListSignalErrorFull() instead")
    void lineItemsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void lineItemsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lineItemsPartialUpdateSignalErrorFull() instead")
    void lineItemsPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void lineItemsPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lineItemsReadSignalErrorFull() instead")
    void lineItemsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void lineItemsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use lineItemsUpdateSignalErrorFull() instead")
    void lineItemsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void lineItemsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPaymentLogListSignalErrorFull() instead")
    void patientPaymentLogListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPaymentLogListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPaymentLogReadSignalErrorFull() instead")
    void patientPaymentLogReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPaymentLogReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPaymentsCreateSignalErrorFull() instead")
    void patientPaymentsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPaymentsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPaymentsListSignalErrorFull() instead")
    void patientPaymentsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPaymentsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use patientPaymentsReadSignalErrorFull() instead")
    void patientPaymentsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void patientPaymentsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use proceduresListSignalErrorFull() instead")
    void proceduresListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void proceduresListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use proceduresReadSignalErrorFull() instead")
    void proceduresReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void proceduresReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use transactionsListSignalErrorFull() instead")
    void transactionsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void transactionsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use transactionsReadSignalErrorFull() instead")
    void transactionsReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void transactionsReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
