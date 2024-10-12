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

#ifndef OAI_OAIPracticeManagementApi_H
#define OAI_OAIPracticeManagementApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIDoctorMessage.h"
#include "OAIInventoryCategory.h"
#include "OAIInventoryVaccine.h"
#include "OAIInventory_categories_list_200_response.h"
#include "OAIInventory_vaccines_list_200_response.h"
#include "OAIMessages_list_200_response.h"
#include "OAIOffice.h"
#include "OAIOffices_list_200_response.h"
#include "OAITask.h"
#include "OAITaskCategory.h"
#include "OAITaskNote.h"
#include "OAITaskStatus.h"
#include "OAITaskTemplate.h"
#include "OAITask_categories_list_200_response.h"
#include "OAITask_notes_list_200_response.h"
#include "OAITask_statuses_list_200_response.h"
#include "OAITask_templates_list_200_response.h"
#include "OAITasks_list_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIPracticeManagementApi : public QObject {
    Q_OBJECT

public:
    OAIPracticeManagementApi(const int timeOut = 0);
    ~OAIPracticeManagementApi();

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
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void inventoryCategoriesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void inventoryCategoriesRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  status QString [optional]
    * @param[in]  cvx_code QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void inventoryVaccinesCreate(const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &cvx_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  status QString [optional]
    * @param[in]  cvx_code QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void inventoryVaccinesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &cvx_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  status QString [optional]
    * @param[in]  cvx_code QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void inventoryVaccinesRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &cvx_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  responsible_user qint32 [optional]
    * @param[in]  updated_since QString [optional]
    * @param[in]  received_since QString [optional]
    * @param[in]  owner qint32 [optional]
    * @param[in]  type QString [optional]
    */
    virtual void messagesCreate(const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &responsible_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &updated_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &received_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &owner = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &type = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  responsible_user qint32 [optional]
    * @param[in]  updated_since QString [optional]
    * @param[in]  received_since QString [optional]
    * @param[in]  owner qint32 [optional]
    * @param[in]  type QString [optional]
    */
    virtual void messagesDelete(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &responsible_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &updated_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &received_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &owner = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &type = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  responsible_user qint32 [optional]
    * @param[in]  updated_since QString [optional]
    * @param[in]  received_since QString [optional]
    * @param[in]  owner qint32 [optional]
    * @param[in]  type QString [optional]
    */
    virtual void messagesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &responsible_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &updated_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &received_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &owner = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &type = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  responsible_user qint32 [optional]
    * @param[in]  updated_since QString [optional]
    * @param[in]  received_since QString [optional]
    * @param[in]  owner qint32 [optional]
    * @param[in]  type QString [optional]
    */
    virtual void messagesPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &responsible_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &updated_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &received_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &owner = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &type = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  responsible_user qint32 [optional]
    * @param[in]  updated_since QString [optional]
    * @param[in]  received_since QString [optional]
    * @param[in]  owner qint32 [optional]
    * @param[in]  type QString [optional]
    */
    virtual void messagesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &responsible_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &updated_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &received_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &owner = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &type = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  patient qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    * @param[in]  responsible_user qint32 [optional]
    * @param[in]  updated_since QString [optional]
    * @param[in]  received_since QString [optional]
    * @param[in]  owner qint32 [optional]
    * @param[in]  type QString [optional]
    */
    virtual void messagesUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &patient = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &responsible_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &updated_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &received_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &owner = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &type = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void officesAddExamRoom(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void officesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void officesPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void officesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  doctor qint32 [optional]
    */
    virtual void officesUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &doctor = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  since QString [optional]
    */
    virtual void taskCategoriesCreate(const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  since QString [optional]
    */
    virtual void taskCategoriesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    */
    virtual void taskCategoriesPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    */
    virtual void taskCategoriesRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    */
    virtual void taskCategoriesUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  task qint32 [optional]
    * @param[in]  since QString [optional]
    */
    virtual void taskNotesCreate(const ::OpenAPI::OptionalParam<qint32> &task = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  task qint32 [optional]
    * @param[in]  since QString [optional]
    */
    virtual void taskNotesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &task = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  task qint32 [optional]
    * @param[in]  since QString [optional]
    */
    virtual void taskNotesPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &task = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  task qint32 [optional]
    * @param[in]  since QString [optional]
    */
    virtual void taskNotesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &task = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  task qint32 [optional]
    * @param[in]  since QString [optional]
    */
    virtual void taskNotesUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &task = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  since QString [optional]
    */
    virtual void taskStatusesCreate(const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  since QString [optional]
    */
    virtual void taskStatusesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    */
    virtual void taskStatusesPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    */
    virtual void taskStatusesRead(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  since QString [optional]
    */
    virtual void taskStatusesUpdate(const QString &id, const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  assignee_user qint32 [optional]
    * @param[in]  status qint32 [optional]
    * @param[in]  assignee_group qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  category qint32 [optional]
    */
    virtual void taskTemplatesCreate(const ::OpenAPI::OptionalParam<qint32> &assignee_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &status = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &assignee_group = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &category = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  assignee_user qint32 [optional]
    * @param[in]  status qint32 [optional]
    * @param[in]  assignee_group qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  category qint32 [optional]
    */
    virtual void taskTemplatesList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &assignee_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &status = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &assignee_group = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &category = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  assignee_user qint32 [optional]
    * @param[in]  status qint32 [optional]
    * @param[in]  assignee_group qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  category qint32 [optional]
    */
    virtual void taskTemplatesPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &assignee_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &status = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &assignee_group = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &category = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  assignee_user qint32 [optional]
    * @param[in]  status qint32 [optional]
    * @param[in]  assignee_group qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  category qint32 [optional]
    */
    virtual void taskTemplatesRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &assignee_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &status = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &assignee_group = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &category = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  assignee_user qint32 [optional]
    * @param[in]  status qint32 [optional]
    * @param[in]  assignee_group qint32 [optional]
    * @param[in]  since QString [optional]
    * @param[in]  category qint32 [optional]
    */
    virtual void taskTemplatesUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &assignee_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &status = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &assignee_group = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &category = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  status qint32 [optional]
    * @param[in]  category qint32 [optional]
    * @param[in]  due_at_date QString [optional]
    * @param[in]  due_at_unknown QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  due_at_since QString [optional]
    * @param[in]  assignee_user qint32 [optional]
    * @param[in]  assignee_group qint32 [optional]
    * @param[in]  due_at_range QString [optional]
    */
    virtual void tasksCreate(const ::OpenAPI::OptionalParam<qint32> &status = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &category = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &due_at_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &due_at_unknown = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &due_at_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &assignee_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &assignee_group = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &due_at_range = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  cursor QString [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  status qint32 [optional]
    * @param[in]  category qint32 [optional]
    * @param[in]  due_at_date QString [optional]
    * @param[in]  due_at_unknown QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  due_at_since QString [optional]
    * @param[in]  assignee_user qint32 [optional]
    * @param[in]  assignee_group qint32 [optional]
    * @param[in]  due_at_range QString [optional]
    */
    virtual void tasksList(const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &status = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &category = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &due_at_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &due_at_unknown = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &due_at_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &assignee_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &assignee_group = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &due_at_range = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  status qint32 [optional]
    * @param[in]  category qint32 [optional]
    * @param[in]  due_at_date QString [optional]
    * @param[in]  due_at_unknown QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  due_at_since QString [optional]
    * @param[in]  assignee_user qint32 [optional]
    * @param[in]  assignee_group qint32 [optional]
    * @param[in]  due_at_range QString [optional]
    */
    virtual void tasksPartialUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &status = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &category = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &due_at_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &due_at_unknown = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &due_at_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &assignee_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &assignee_group = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &due_at_range = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  status qint32 [optional]
    * @param[in]  category qint32 [optional]
    * @param[in]  due_at_date QString [optional]
    * @param[in]  due_at_unknown QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  due_at_since QString [optional]
    * @param[in]  assignee_user qint32 [optional]
    * @param[in]  assignee_group qint32 [optional]
    * @param[in]  due_at_range QString [optional]
    */
    virtual void tasksRead(const QString &id, const ::OpenAPI::OptionalParam<qint32> &status = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &category = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &due_at_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &due_at_unknown = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &due_at_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &assignee_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &assignee_group = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &due_at_range = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  status qint32 [optional]
    * @param[in]  category qint32 [optional]
    * @param[in]  due_at_date QString [optional]
    * @param[in]  due_at_unknown QString [optional]
    * @param[in]  since QString [optional]
    * @param[in]  due_at_since QString [optional]
    * @param[in]  assignee_user qint32 [optional]
    * @param[in]  assignee_group qint32 [optional]
    * @param[in]  due_at_range QString [optional]
    */
    virtual void tasksUpdate(const QString &id, const ::OpenAPI::OptionalParam<qint32> &status = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &category = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &due_at_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &due_at_unknown = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &due_at_since = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &assignee_user = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &assignee_group = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &due_at_range = ::OpenAPI::OptionalParam<QString>());


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

    void inventoryCategoriesListCallback(OAIHttpRequestWorker *worker);
    void inventoryCategoriesReadCallback(OAIHttpRequestWorker *worker);
    void inventoryVaccinesCreateCallback(OAIHttpRequestWorker *worker);
    void inventoryVaccinesListCallback(OAIHttpRequestWorker *worker);
    void inventoryVaccinesReadCallback(OAIHttpRequestWorker *worker);
    void messagesCreateCallback(OAIHttpRequestWorker *worker);
    void messagesDeleteCallback(OAIHttpRequestWorker *worker);
    void messagesListCallback(OAIHttpRequestWorker *worker);
    void messagesPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void messagesReadCallback(OAIHttpRequestWorker *worker);
    void messagesUpdateCallback(OAIHttpRequestWorker *worker);
    void officesAddExamRoomCallback(OAIHttpRequestWorker *worker);
    void officesListCallback(OAIHttpRequestWorker *worker);
    void officesPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void officesReadCallback(OAIHttpRequestWorker *worker);
    void officesUpdateCallback(OAIHttpRequestWorker *worker);
    void taskCategoriesCreateCallback(OAIHttpRequestWorker *worker);
    void taskCategoriesListCallback(OAIHttpRequestWorker *worker);
    void taskCategoriesPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void taskCategoriesReadCallback(OAIHttpRequestWorker *worker);
    void taskCategoriesUpdateCallback(OAIHttpRequestWorker *worker);
    void taskNotesCreateCallback(OAIHttpRequestWorker *worker);
    void taskNotesListCallback(OAIHttpRequestWorker *worker);
    void taskNotesPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void taskNotesReadCallback(OAIHttpRequestWorker *worker);
    void taskNotesUpdateCallback(OAIHttpRequestWorker *worker);
    void taskStatusesCreateCallback(OAIHttpRequestWorker *worker);
    void taskStatusesListCallback(OAIHttpRequestWorker *worker);
    void taskStatusesPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void taskStatusesReadCallback(OAIHttpRequestWorker *worker);
    void taskStatusesUpdateCallback(OAIHttpRequestWorker *worker);
    void taskTemplatesCreateCallback(OAIHttpRequestWorker *worker);
    void taskTemplatesListCallback(OAIHttpRequestWorker *worker);
    void taskTemplatesPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void taskTemplatesReadCallback(OAIHttpRequestWorker *worker);
    void taskTemplatesUpdateCallback(OAIHttpRequestWorker *worker);
    void tasksCreateCallback(OAIHttpRequestWorker *worker);
    void tasksListCallback(OAIHttpRequestWorker *worker);
    void tasksPartialUpdateCallback(OAIHttpRequestWorker *worker);
    void tasksReadCallback(OAIHttpRequestWorker *worker);
    void tasksUpdateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void inventoryCategoriesListSignal(OAIInventory_categories_list_200_response summary);
    void inventoryCategoriesReadSignal(OAIInventoryCategory summary);
    void inventoryVaccinesCreateSignal(OAIInventoryVaccine summary);
    void inventoryVaccinesListSignal(OAIInventory_vaccines_list_200_response summary);
    void inventoryVaccinesReadSignal(OAIInventoryVaccine summary);
    void messagesCreateSignal(OAIDoctorMessage summary);
    void messagesDeleteSignal();
    void messagesListSignal(OAIMessages_list_200_response summary);
    void messagesPartialUpdateSignal();
    void messagesReadSignal(OAIDoctorMessage summary);
    void messagesUpdateSignal();
    void officesAddExamRoomSignal(OAIOffice summary);
    void officesListSignal(OAIOffices_list_200_response summary);
    void officesPartialUpdateSignal();
    void officesReadSignal(OAIOffice summary);
    void officesUpdateSignal();
    void taskCategoriesCreateSignal(OAITaskCategory summary);
    void taskCategoriesListSignal(OAITask_categories_list_200_response summary);
    void taskCategoriesPartialUpdateSignal();
    void taskCategoriesReadSignal(OAITaskCategory summary);
    void taskCategoriesUpdateSignal();
    void taskNotesCreateSignal(OAITaskNote summary);
    void taskNotesListSignal(OAITask_notes_list_200_response summary);
    void taskNotesPartialUpdateSignal();
    void taskNotesReadSignal(OAITaskNote summary);
    void taskNotesUpdateSignal();
    void taskStatusesCreateSignal(OAITaskStatus summary);
    void taskStatusesListSignal(OAITask_statuses_list_200_response summary);
    void taskStatusesPartialUpdateSignal();
    void taskStatusesReadSignal(OAITaskStatus summary);
    void taskStatusesUpdateSignal();
    void taskTemplatesCreateSignal(OAITaskTemplate summary);
    void taskTemplatesListSignal(OAITask_templates_list_200_response summary);
    void taskTemplatesPartialUpdateSignal();
    void taskTemplatesReadSignal(OAITaskTemplate summary);
    void taskTemplatesUpdateSignal();
    void tasksCreateSignal(OAITask summary);
    void tasksListSignal(OAITasks_list_200_response summary);
    void tasksPartialUpdateSignal();
    void tasksReadSignal(OAITask summary);
    void tasksUpdateSignal();


    void inventoryCategoriesListSignalFull(OAIHttpRequestWorker *worker, OAIInventory_categories_list_200_response summary);
    void inventoryCategoriesReadSignalFull(OAIHttpRequestWorker *worker, OAIInventoryCategory summary);
    void inventoryVaccinesCreateSignalFull(OAIHttpRequestWorker *worker, OAIInventoryVaccine summary);
    void inventoryVaccinesListSignalFull(OAIHttpRequestWorker *worker, OAIInventory_vaccines_list_200_response summary);
    void inventoryVaccinesReadSignalFull(OAIHttpRequestWorker *worker, OAIInventoryVaccine summary);
    void messagesCreateSignalFull(OAIHttpRequestWorker *worker, OAIDoctorMessage summary);
    void messagesDeleteSignalFull(OAIHttpRequestWorker *worker);
    void messagesListSignalFull(OAIHttpRequestWorker *worker, OAIMessages_list_200_response summary);
    void messagesPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void messagesReadSignalFull(OAIHttpRequestWorker *worker, OAIDoctorMessage summary);
    void messagesUpdateSignalFull(OAIHttpRequestWorker *worker);
    void officesAddExamRoomSignalFull(OAIHttpRequestWorker *worker, OAIOffice summary);
    void officesListSignalFull(OAIHttpRequestWorker *worker, OAIOffices_list_200_response summary);
    void officesPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void officesReadSignalFull(OAIHttpRequestWorker *worker, OAIOffice summary);
    void officesUpdateSignalFull(OAIHttpRequestWorker *worker);
    void taskCategoriesCreateSignalFull(OAIHttpRequestWorker *worker, OAITaskCategory summary);
    void taskCategoriesListSignalFull(OAIHttpRequestWorker *worker, OAITask_categories_list_200_response summary);
    void taskCategoriesPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void taskCategoriesReadSignalFull(OAIHttpRequestWorker *worker, OAITaskCategory summary);
    void taskCategoriesUpdateSignalFull(OAIHttpRequestWorker *worker);
    void taskNotesCreateSignalFull(OAIHttpRequestWorker *worker, OAITaskNote summary);
    void taskNotesListSignalFull(OAIHttpRequestWorker *worker, OAITask_notes_list_200_response summary);
    void taskNotesPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void taskNotesReadSignalFull(OAIHttpRequestWorker *worker, OAITaskNote summary);
    void taskNotesUpdateSignalFull(OAIHttpRequestWorker *worker);
    void taskStatusesCreateSignalFull(OAIHttpRequestWorker *worker, OAITaskStatus summary);
    void taskStatusesListSignalFull(OAIHttpRequestWorker *worker, OAITask_statuses_list_200_response summary);
    void taskStatusesPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void taskStatusesReadSignalFull(OAIHttpRequestWorker *worker, OAITaskStatus summary);
    void taskStatusesUpdateSignalFull(OAIHttpRequestWorker *worker);
    void taskTemplatesCreateSignalFull(OAIHttpRequestWorker *worker, OAITaskTemplate summary);
    void taskTemplatesListSignalFull(OAIHttpRequestWorker *worker, OAITask_templates_list_200_response summary);
    void taskTemplatesPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void taskTemplatesReadSignalFull(OAIHttpRequestWorker *worker, OAITaskTemplate summary);
    void taskTemplatesUpdateSignalFull(OAIHttpRequestWorker *worker);
    void tasksCreateSignalFull(OAIHttpRequestWorker *worker, OAITask summary);
    void tasksListSignalFull(OAIHttpRequestWorker *worker, OAITasks_list_200_response summary);
    void tasksPartialUpdateSignalFull(OAIHttpRequestWorker *worker);
    void tasksReadSignalFull(OAIHttpRequestWorker *worker, OAITask summary);
    void tasksUpdateSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use inventoryCategoriesListSignalError() instead")
    void inventoryCategoriesListSignalE(OAIInventory_categories_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void inventoryCategoriesListSignalError(OAIInventory_categories_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use inventoryCategoriesReadSignalError() instead")
    void inventoryCategoriesReadSignalE(OAIInventoryCategory summary, QNetworkReply::NetworkError error_type, QString error_str);
    void inventoryCategoriesReadSignalError(OAIInventoryCategory summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use inventoryVaccinesCreateSignalError() instead")
    void inventoryVaccinesCreateSignalE(OAIInventoryVaccine summary, QNetworkReply::NetworkError error_type, QString error_str);
    void inventoryVaccinesCreateSignalError(OAIInventoryVaccine summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use inventoryVaccinesListSignalError() instead")
    void inventoryVaccinesListSignalE(OAIInventory_vaccines_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void inventoryVaccinesListSignalError(OAIInventory_vaccines_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use inventoryVaccinesReadSignalError() instead")
    void inventoryVaccinesReadSignalE(OAIInventoryVaccine summary, QNetworkReply::NetworkError error_type, QString error_str);
    void inventoryVaccinesReadSignalError(OAIInventoryVaccine summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use messagesCreateSignalError() instead")
    void messagesCreateSignalE(OAIDoctorMessage summary, QNetworkReply::NetworkError error_type, QString error_str);
    void messagesCreateSignalError(OAIDoctorMessage summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use messagesDeleteSignalError() instead")
    void messagesDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void messagesDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use messagesListSignalError() instead")
    void messagesListSignalE(OAIMessages_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void messagesListSignalError(OAIMessages_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use messagesPartialUpdateSignalError() instead")
    void messagesPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void messagesPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use messagesReadSignalError() instead")
    void messagesReadSignalE(OAIDoctorMessage summary, QNetworkReply::NetworkError error_type, QString error_str);
    void messagesReadSignalError(OAIDoctorMessage summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use messagesUpdateSignalError() instead")
    void messagesUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void messagesUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use officesAddExamRoomSignalError() instead")
    void officesAddExamRoomSignalE(OAIOffice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void officesAddExamRoomSignalError(OAIOffice summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use officesListSignalError() instead")
    void officesListSignalE(OAIOffices_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void officesListSignalError(OAIOffices_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use officesPartialUpdateSignalError() instead")
    void officesPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void officesPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use officesReadSignalError() instead")
    void officesReadSignalE(OAIOffice summary, QNetworkReply::NetworkError error_type, QString error_str);
    void officesReadSignalError(OAIOffice summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use officesUpdateSignalError() instead")
    void officesUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void officesUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskCategoriesCreateSignalError() instead")
    void taskCategoriesCreateSignalE(OAITaskCategory summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskCategoriesCreateSignalError(OAITaskCategory summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskCategoriesListSignalError() instead")
    void taskCategoriesListSignalE(OAITask_categories_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskCategoriesListSignalError(OAITask_categories_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskCategoriesPartialUpdateSignalError() instead")
    void taskCategoriesPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void taskCategoriesPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskCategoriesReadSignalError() instead")
    void taskCategoriesReadSignalE(OAITaskCategory summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskCategoriesReadSignalError(OAITaskCategory summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskCategoriesUpdateSignalError() instead")
    void taskCategoriesUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void taskCategoriesUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskNotesCreateSignalError() instead")
    void taskNotesCreateSignalE(OAITaskNote summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskNotesCreateSignalError(OAITaskNote summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskNotesListSignalError() instead")
    void taskNotesListSignalE(OAITask_notes_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskNotesListSignalError(OAITask_notes_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskNotesPartialUpdateSignalError() instead")
    void taskNotesPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void taskNotesPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskNotesReadSignalError() instead")
    void taskNotesReadSignalE(OAITaskNote summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskNotesReadSignalError(OAITaskNote summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskNotesUpdateSignalError() instead")
    void taskNotesUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void taskNotesUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskStatusesCreateSignalError() instead")
    void taskStatusesCreateSignalE(OAITaskStatus summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskStatusesCreateSignalError(OAITaskStatus summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskStatusesListSignalError() instead")
    void taskStatusesListSignalE(OAITask_statuses_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskStatusesListSignalError(OAITask_statuses_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskStatusesPartialUpdateSignalError() instead")
    void taskStatusesPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void taskStatusesPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskStatusesReadSignalError() instead")
    void taskStatusesReadSignalE(OAITaskStatus summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskStatusesReadSignalError(OAITaskStatus summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskStatusesUpdateSignalError() instead")
    void taskStatusesUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void taskStatusesUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskTemplatesCreateSignalError() instead")
    void taskTemplatesCreateSignalE(OAITaskTemplate summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskTemplatesCreateSignalError(OAITaskTemplate summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskTemplatesListSignalError() instead")
    void taskTemplatesListSignalE(OAITask_templates_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskTemplatesListSignalError(OAITask_templates_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskTemplatesPartialUpdateSignalError() instead")
    void taskTemplatesPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void taskTemplatesPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskTemplatesReadSignalError() instead")
    void taskTemplatesReadSignalE(OAITaskTemplate summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskTemplatesReadSignalError(OAITaskTemplate summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskTemplatesUpdateSignalError() instead")
    void taskTemplatesUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void taskTemplatesUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tasksCreateSignalError() instead")
    void tasksCreateSignalE(OAITask summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tasksCreateSignalError(OAITask summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tasksListSignalError() instead")
    void tasksListSignalE(OAITasks_list_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tasksListSignalError(OAITasks_list_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tasksPartialUpdateSignalError() instead")
    void tasksPartialUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void tasksPartialUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tasksReadSignalError() instead")
    void tasksReadSignalE(OAITask summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tasksReadSignalError(OAITask summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tasksUpdateSignalError() instead")
    void tasksUpdateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void tasksUpdateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use inventoryCategoriesListSignalErrorFull() instead")
    void inventoryCategoriesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void inventoryCategoriesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use inventoryCategoriesReadSignalErrorFull() instead")
    void inventoryCategoriesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void inventoryCategoriesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use inventoryVaccinesCreateSignalErrorFull() instead")
    void inventoryVaccinesCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void inventoryVaccinesCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use inventoryVaccinesListSignalErrorFull() instead")
    void inventoryVaccinesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void inventoryVaccinesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use inventoryVaccinesReadSignalErrorFull() instead")
    void inventoryVaccinesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void inventoryVaccinesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use messagesCreateSignalErrorFull() instead")
    void messagesCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void messagesCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use messagesDeleteSignalErrorFull() instead")
    void messagesDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void messagesDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use messagesListSignalErrorFull() instead")
    void messagesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void messagesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use messagesPartialUpdateSignalErrorFull() instead")
    void messagesPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void messagesPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use messagesReadSignalErrorFull() instead")
    void messagesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void messagesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use messagesUpdateSignalErrorFull() instead")
    void messagesUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void messagesUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use officesAddExamRoomSignalErrorFull() instead")
    void officesAddExamRoomSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void officesAddExamRoomSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use officesListSignalErrorFull() instead")
    void officesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void officesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use officesPartialUpdateSignalErrorFull() instead")
    void officesPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void officesPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use officesReadSignalErrorFull() instead")
    void officesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void officesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use officesUpdateSignalErrorFull() instead")
    void officesUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void officesUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskCategoriesCreateSignalErrorFull() instead")
    void taskCategoriesCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskCategoriesCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskCategoriesListSignalErrorFull() instead")
    void taskCategoriesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskCategoriesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskCategoriesPartialUpdateSignalErrorFull() instead")
    void taskCategoriesPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskCategoriesPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskCategoriesReadSignalErrorFull() instead")
    void taskCategoriesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskCategoriesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskCategoriesUpdateSignalErrorFull() instead")
    void taskCategoriesUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskCategoriesUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskNotesCreateSignalErrorFull() instead")
    void taskNotesCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskNotesCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskNotesListSignalErrorFull() instead")
    void taskNotesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskNotesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskNotesPartialUpdateSignalErrorFull() instead")
    void taskNotesPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskNotesPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskNotesReadSignalErrorFull() instead")
    void taskNotesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskNotesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskNotesUpdateSignalErrorFull() instead")
    void taskNotesUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskNotesUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskStatusesCreateSignalErrorFull() instead")
    void taskStatusesCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskStatusesCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskStatusesListSignalErrorFull() instead")
    void taskStatusesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskStatusesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskStatusesPartialUpdateSignalErrorFull() instead")
    void taskStatusesPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskStatusesPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskStatusesReadSignalErrorFull() instead")
    void taskStatusesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskStatusesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskStatusesUpdateSignalErrorFull() instead")
    void taskStatusesUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskStatusesUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskTemplatesCreateSignalErrorFull() instead")
    void taskTemplatesCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskTemplatesCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskTemplatesListSignalErrorFull() instead")
    void taskTemplatesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskTemplatesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskTemplatesPartialUpdateSignalErrorFull() instead")
    void taskTemplatesPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskTemplatesPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskTemplatesReadSignalErrorFull() instead")
    void taskTemplatesReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskTemplatesReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskTemplatesUpdateSignalErrorFull() instead")
    void taskTemplatesUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskTemplatesUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tasksCreateSignalErrorFull() instead")
    void tasksCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tasksCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tasksListSignalErrorFull() instead")
    void tasksListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tasksListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tasksPartialUpdateSignalErrorFull() instead")
    void tasksPartialUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tasksPartialUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tasksReadSignalErrorFull() instead")
    void tasksReadSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tasksReadSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tasksUpdateSignalErrorFull() instead")
    void tasksUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tasksUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
