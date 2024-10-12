/**
 * 
 * This document is intended as a detailed reference for the precise behavior of the drchrono API. If this is your first time using the API, start with our <a href=\"/api-docs-old/tutorial\">tutorial</a>. If you are upgrading from a previous version, take a look at the changelog section.  # Authorization  ## Initial authorization  There are three main steps in the OAuth 2.0 authentication workflow:  1. Redirect the provider to the authorization page. 2. The provider authorizes your application and is redirected back to    your web application. 3. Your application exchanges the `authorization_code` that came with    the redirect for an `access_token` and `refresh_token`.  ### Step 1: Redirect to drchrono  The first step is redirecting your user to drchrono, typically with a button labeled \"Connect to drchrono\" or \"Login with drchrono\".  This is just a link that takes your user to the following URL:      https://drchrono.com/o/authorize/?redirect_uri=REDIRECT_URI_ENCODED&response_type=code&client_id=CLIENT_ID_ENCODED&scope=SCOPES_ENCODED  - `REDIRECT_URI_ENCODED` is the URL-encoded version of the redirect URI (as registered for your application and used in later steps). - `CLIENT_ID_ENCODED` is the URL-encoded version of your application's client ID. - `SCOPES_ENCODED` is a URL-encoded version of a space-separated list of scopes, which can be found in each endpoint or omitted to default to all scopes.  The `scope` parameter consists of an optional, space-separated list of scopes your application is requesting. If omitted, all scopes will be requested.  Scopes are of the form `BASE_SCOPE:[read|write]` where `BASE_SCOPE` is any of `user`, `calendar`, `patients`, `patients:summary`, `billing`, `clinical` and `labs`. You should request only the scopes you need. For instance, an application which sends \"Happy Birthday!\" emails to a doctor's patients on their birthdays would use the scope parameter `\"patients:summary:read\"`, while one that allows patients to schedule appointments online would need at least `\"patients:summary:read patients:summary:write calendar:read calendar:write clinical:read clinical:write\"`.  ### Step 2: Provider authorization  After logging in (if necessary), the provider will be presented with a screen with your application's name and the list of permissions you requested (via the `scope` parameter).  When they click the \"Authorize\" button, they will be redirected to your redirect URI with a `code` query parameter appended, which contains an authorization code to be used in step 3.  If they click the \"Cancel\" button, they will be redirected to your redirect URI with `error=access_denied` instead.  Note: This authorization code expires extremely quickly, so you must perform step 3 immediately, ideally before rendering the resulting page for the end user.  ### Step 3: Token exchange  The `code` obtained from step 2 is usable exactly once to obtain an access token and refresh token.  Here is an example token exchange in Python:      import datetime, pytz, requests      if 'error' in get_params:         raise ValueError('Error authorizing application: %s' % get_params[error])      response = requests.post('https://drchrono.com/o/token/', data={         'code': get_params['code'],         'grant_type': 'authorization_code',         'redirect_uri': 'http://mytestapp.com/redirect_uri',         'client_id': 'abcdefg12345',         'client_secret': 'abcdefg12345',     })     response.raise_for_status()     data = response.json()      # Save these in your database associated with the user     access_token = data['access_token']     refresh_token = data['refresh_token']     expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])  You now have all you need to make API requests authenticated as that provider. When using this access token, you'll only be able to access the data that the user has access to and that you have been granted permissions for.  ## Refreshing an access token  Access tokens only last 48 hours (given in seconds in the `'expires_in'` key in the token exchange step above), so they occasionally need to be refreshed.  It would be inconvenient to ask the user to re-authorize every time, so instead you can use the refresh token like the original authorization to obtain a new access token.  Replace the `code` parameter with `refresh_token`, change the value `grant_type` from `authorization_code` to `refresh_token`, and omit the `redirect_uri` parameter.  Example in Python:      ...     response = requests.post('https://drchrono.com/o/token/', data={         'refresh_token': get_refresh_token(),         'grant_type': 'refresh_token',         'client_id': 'abcdefg12345',         'client_secret': 'abcdefg12345',     })     ...  # Webhooks  In order to use drchrono API webhooks, you first need to have an API application on file (even if it is in Test Model). Each API webhook is associated with one API application, go to <a href=\"/api-management/\" target=\"_blank\">here</a> to set up both API applications and webhooks!  Once you registered an API application, you will see webhook section in each saved API applications. Create a webhook and register some events there and save all the changes, then you are good to go!  ## Webhooks setup  All fields under webhooks section are required.  **Callback URL** Callback URl is used to receive all hooks when subscribed events are triggered. This should be an URL under your control.  **Secret token** Secret token is used to verify webhooks, this is very important, please set something with high entropy. Also we will talk more about this later.  **Events**  Events is used to register events you want to receiver notification when they happen. Currently we support following events.  Event name | Event description ---------- | ----------------- `APPOINTMENT_CREATE` | We will deliver a hook any time an appointment is created `APPOINTMENT_MODIFY` | We will deliver a hook any time an appointment is modified `PATIENT_CREATE` | We will deliver a hook any time a patient is created `PATIENT_MODIFY` | We will deliver a hook any time a patient is modified `PATIENT_PROBLEM_CREATE` | We will deliver a hook any time a patient problem is created `PATIENT_PROBLEM_MODIFY` | We will deliver a hook any time a patient problem is modified `PATIENT_ALLERGY_CREATE` | We will deliver a hook any time a patient allergy is created `PATIENT_ALLERGY_MODIFY` | We will deliver a hook any time a patient allergy is modified `PATIENT_MEDICATION_CREATE` | We will deliver a hook any time a patient medication is created `PATIENT_MEDICATION_MODIFY` | We will deliver a hook any time a patient medication is modified `CLINICAL_NOTE_LOCK` | We will deliver a hook any time a clinical note is locked `CLINICAL_NOTE_UNLOCK` | We will deliver a hook any time a clinical note is unlocked `TASK_CREATE` | We will deliver a hook any time a task is created `TASK_MODIFY` | We will deliver a hook any time a task is modified and any time creation, modification and deletion of task notes, associated task item `TASK_DELETE` | We will deliver a hook any time a task is deleted   ## Webhooks verification  In order to make sure the callback URL in webhook is under your control, we added a verification step before we send any hooks out to you.  Verification can be done by clicking \"Verify webhook\" button in webhooks setup page. After you click the button, we will send a `GET` request to the callback URL, along with a parameter called `msg`.  Please use your webhook's secret token as hash key and SHA-256 as digest constructor, hash the `msg` value with <a href=\"https://tools.ietf.org/html/rfc2104.html\">HMAC algorithm</a>. And we expect a `200` JSON response, in JSON response body, there should be a key called `secret_token` existing, and its value should be equal to the <strong>hashed</strong> `msg`. Otherwise, verification will fail.  Here is an example webhook verification in Python:      import hashlib, hmac      def webhook_verify(request):         secret_token = hmac.new(WEBHOOK_SECRET_TOKEN, request.GET['msg'], hashlib.sha256).hexdigest()         return json_response({             'secret_token': secret_token         })  <div class=\"alert alert-warning\"> <b>Note:</b> Verification will be needed when webhook is first created and anytime callback URl is changed. </div>   ## Webhooks header and body  **Header**  Key | Value --- | ----- `X-drchrono-event` | Event that triggered this hook, could be any one event above or `PING` `X-drchrono-signature` | Secret token associated with this webhook `X-drchrono-delivery` | ID of this delivery  **Body**  Key | Value --- | ----- `receiver` | This will be an JSON representation of the webhook `object` | This will be an JSON representation of the object related to the triggered event, this would share same serializer as drchrono API  ## Webhooks ping and deliveries  Webhooks ping and deliveries will be sent as `POST` requests.  **PING**:  You can always ping your webhook to check things, by clicking the \"Ping webhook\" button in webhook setup page. And a hook with header `X-drchrono-event: PING` would be sent to the callback URL.  **Deliveries**:  You can check recent deliveries by clicking the \"deliveries\" link in webhook setup page. And you can resend a hook by clicking \"redeliver\" button after select a specific delivery.  ## Webhooks delivery mechanism  We will delivery a hook the moment a subscribed event is triggered. We will not record any response header or body you send back after you receive the hook. However we only consider the response status code. We will consider any `2xx` responses as successfully delivered. Any other responses, like `302` would be considered failing. And we will try to redeliver unsuccessfully delivered hooks 3 times, first redeliver happens at 1 hour after the initial event, second receliver happens 3 hours after the initial event, and the third redeliver happens 7 hours after the initial event. After these redeliveries, if the delivery is still unsuccessful, you have to redeliver it by hand.   ## Webhooks security  You may want to secure your webhooks to only consider requests send out from drchrono. And this is where <code>secret_token</code> is needed in request header. Try to set the <code>secret_token</code> to something with high entropy, a good example could be taking the output of <code>ruby -rsecurerandom -e 'puts SecureRandom.hex(20)'</code>. After this, you might want to verify all request headers you received on your server with this token.   # iframe integration  Some API apps provide additional functionality for interacting with patient data not offered by drchrono, and can benefit by being incorporated into drchrono's patient information page via iframe.  We have created a simple API to make this possible.  To make an existing API application accessible via an iframe on the patient page, you need to update either \"Patient iframe\" or \"Clinical note iframe\" section in API management page, to make the iframe to appear on (either the patient page or the clinical note page), with the URL that the iframe will use for each page, and the height it should have. The application will be reviewed before it is approved to ensure that it is functional and secure.  ## Register a Doctor  iframe applications will appear as choices on the left-hand menu of the patient page for doctors registered with your application.  To register a doctor with your application, make a `POST` request to the `/api/iframe_integration` endpoint using the access token for the corresponding doctor. This endpoint does not expect any payload.  To disable your iframe application for a doctor, make a `DELETE` request to the same endpoint.  ## Populating the iframe  There are two places where the iframe can be displayed, either within the patient detail page or the clinical note page, shown below respectively:  <img src=\"{% asset 'public/images/iframe_patient_page.png' %}\" alt=\"Iframe on the patient page\"/>  <img src=\"{% asset 'public/images/iframe_clinical_note.png' %}\" alt=\"Iframe on the clinical note page\"/>  When requesting approval for your iframe app, you must specify a URL for one or both of these pages which will serve as the base URL for your IFrame contents. When a doctor views your iframe, the source URL will have various query parameters appended to it, for example for the patient page the `src` parameter of the IFrame will be:  ``` <iframe_url>?doctor_id=<doctor_id>&patient_id=<patient_id>&practice_id=<practice_id>&iat=<iat>&jwt=<jwt> ```  The `jwt` parameter is crucial if your application transfers any sort of PHI and does not implement its own login system.  It encapsulates the other parameters in a [JSON web token (JWT)](http://jwt.io) and signs them using SHA-256 HMAC with your `client_secret` as the key.  This verifies that the iframe is being loaded within one of drchrono's pages by an authorized user.  In production, you should validate the JWT using an approved library (which are listed on the [official site](http://jwt.io)), and only use the parameters extracted from the JWT.  Using Python and Django, this might look like:      import jwt      CLIENT_SECRET = <client_secret>     MAX_TIME_DRIFT_SECONDS = 60      def validate_parameters(request):         token = request.GET['jwt']          return jwt.decode(token, CLIENT_SECRET, algorithms=['HS256'], leeway=MAX_TIME_DRIFT_SECONDS)  Modern browsers' same-origin policy means that data cannot be passed between your application and drchrono's page through the iframe.  Therefore, interaction must happen through the API, using information provided in JWT.  # Versions and deprecation  ## Stability Policy  Changes to this API version will be limited to adding endpoints, or adding fields to existing endpoints, or adding optional query parameters. Any new fields which are not read-only will be optional.  ## Deprecation Policy  The drchrono API is versioned. Versions can be in the following states:  * **Active:** This is our latest and greatest version of the API. It is actively supported by our API team and is improved upon with new features, bug fixes and optimizations that do not break backwards compatibility.  * **Deprecated:** A deprecated API version is considered second best--having been surpassed by our active API version. An API version remains in this state for one year, after which time it falls to the not supported state. A deprecated API version is passively supported; while it won't be removed until becoming unsupported, it may not receive new features but will likely be subject to security updates and performance improvements.  * **Unsupported:** An API version in the not supported state may be deactivated at any time. An application using an unsupported API version should migrate to an active API version.  ## Version Map | Version Name | Previous Name | Start Date | Deprecation Date | |--------------|---------------|------------|------------------| | v2           | v2015_08      | 08/2015    | TBA              | | v3           | v2016_06      | 06/2016    |                  | | v4           | N/A           | 09/2018    |                  |  If you are looking for documentation for an older version  - [V4(Hunt Valley)](/api-docs-old/v4/documentation) (old V4 documentation) - [V3(Sunnyvale)](/api-docs-old/v3/documentation) - [V2(Mountain View)](/api-docs-old/v2/documentation)  # Changelog  Here's changelog for different versions  - [V4 Changelog](/api-docs-old/v4/changelog) - [V3 changelog](/api-docs-old/v3/changelog)  
 *
 * The version of the OpenAPI document: v4 (Hunt Valley)
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import AllergiesList200Response from './model/AllergiesList200Response';
import AmendmentsList200Response from './model/AmendmentsList200Response';
import Appointment from './model/Appointment';
import AppointmentProfile from './model/AppointmentProfile';
import AppointmentProfilesList200Response from './model/AppointmentProfilesList200Response';
import AppointmentStatusTransition from './model/AppointmentStatusTransition';
import AppointmentTemplate from './model/AppointmentTemplate';
import AppointmentTemplatesList200Response from './model/AppointmentTemplatesList200Response';
import AppointmentsList200Response from './model/AppointmentsList200Response';
import AssociatedTaskItem from './model/AssociatedTaskItem';
import AutoAccidentInsurance from './model/AutoAccidentInsurance';
import BillingLineItem from './model/BillingLineItem';
import BillingProfile from './model/BillingProfile';
import BillingProfilesList200Response from './model/BillingProfilesList200Response';
import CarePlan from './model/CarePlan';
import CarePlansList200Response from './model/CarePlansList200Response';
import CareTeamMember from './model/CareTeamMember';
import CareTeamMembersList200Response from './model/CareTeamMembersList200Response';
import CashPayment from './model/CashPayment';
import CashPaymentLog from './model/CashPaymentLog';
import ClaimBillingNotes from './model/ClaimBillingNotes';
import ClaimBillingNotes1 from './model/ClaimBillingNotes1';
import ClaimBillingNotesList200Response from './model/ClaimBillingNotesList200Response';
import ClinicalNote from './model/ClinicalNote';
import ClinicalNote1 from './model/ClinicalNote1';
import ClinicalNoteField from './model/ClinicalNoteField';
import ClinicalNoteFieldTypesList200Response from './model/ClinicalNoteFieldTypesList200Response';
import ClinicalNoteFieldValuesList200Response from './model/ClinicalNoteFieldValuesList200Response';
import ClinicalNoteSection from './model/ClinicalNoteSection';
import ClinicalNoteTemplatesList200Response from './model/ClinicalNoteTemplatesList200Response';
import ClinicalNotesList200Response from './model/ClinicalNotesList200Response';
import CommLogsList200Response from './model/CommLogsList200Response';
import ConsentForm from './model/ConsentForm';
import ConsentFormsList200Response from './model/ConsentFormsList200Response';
import Coverage from './model/Coverage';
import CptCodesInner from './model/CptCodesInner';
import CustomAppointmentFieldType from './model/CustomAppointmentFieldType';
import CustomAppointmentFieldValue from './model/CustomAppointmentFieldValue';
import CustomAppointmentFieldsList200Response from './model/CustomAppointmentFieldsList200Response';
import CustomDemographicsList200Response from './model/CustomDemographicsList200Response';
import CustomInsurancePlanName from './model/CustomInsurancePlanName';
import CustomInsurancePlanNamesList200Response from './model/CustomInsurancePlanNamesList200Response';
import CustomPatientFieldType from './model/CustomPatientFieldType';
import CustomPatientFieldValue from './model/CustomPatientFieldValue';
import CustomProcedureCodesInner from './model/CustomProcedureCodesInner';
import CustomVitalType from './model/CustomVitalType';
import CustomVitalValue from './model/CustomVitalValue';
import CustomVitalsList200Response from './model/CustomVitalsList200Response';
import Doctor from './model/Doctor';
import DoctorFeeSchedule from './model/DoctorFeeSchedule';
import DoctorMessage from './model/DoctorMessage';
import DoctorsList200Response from './model/DoctorsList200Response';
import DocumentsList200Response from './model/DocumentsList200Response';
import EOBObject from './model/EOBObject';
import EligibilityChecksList200Response from './model/EligibilityChecksList200Response';
import EobsList200Response from './model/EobsList200Response';
import FeeSchedulesList200Response from './model/FeeSchedulesList200Response';
import HcpcsCodesInner from './model/HcpcsCodesInner';
import ICD10Code from './model/ICD10Code';
import ImplantableDevice from './model/ImplantableDevice';
import ImplantableDevicesList200Response from './model/ImplantableDevicesList200Response';
import Insurance from './model/Insurance';
import InsurancesList200Response from './model/InsurancesList200Response';
import InventoryCategoriesList200Response from './model/InventoryCategoriesList200Response';
import InventoryCategory from './model/InventoryCategory';
import InventoryVaccine from './model/InventoryVaccine';
import InventoryVaccinesList200Response from './model/InventoryVaccinesList200Response';
import LabDocumentsList200Response from './model/LabDocumentsList200Response';
import LabOrder from './model/LabOrder';
import LabOrderDocument from './model/LabOrderDocument';
import LabOrdersList200Response from './model/LabOrdersList200Response';
import LabResult from './model/LabResult';
import LabResultsList200Response from './model/LabResultsList200Response';
import LabTest from './model/LabTest';
import LabTestsList200Response from './model/LabTestsList200Response';
import LabVendorLocation from './model/LabVendorLocation';
import LineItemTransaction from './model/LineItemTransaction';
import LineItemsList200Response from './model/LineItemsList200Response';
import MedicationsList200Response from './model/MedicationsList200Response';
import MessageNote from './model/MessageNote';
import MessagesList200Response from './model/MessagesList200Response';
import NdcCodeInner from './model/NdcCodeInner';
import Office from './model/Office';
import OfficeOnlineHours from './model/OfficeOnlineHours';
import OfficesList200Response from './model/OfficesList200Response';
import OpenSlot from './model/OpenSlot';
import Patient from './model/Patient';
import Patient1 from './model/Patient1';
import PatientAllergy from './model/PatientAllergy';
import PatientAmendment from './model/PatientAmendment';
import PatientCommunication from './model/PatientCommunication';
import PatientCommunicationsList200Response from './model/PatientCommunicationsList200Response';
import PatientDrug from './model/PatientDrug';
import PatientFlag from './model/PatientFlag';
import PatientFlagType from './model/PatientFlagType';
import PatientFlagType1 from './model/PatientFlagType1';
import PatientFlagTypesList200Response from './model/PatientFlagTypesList200Response';
import PatientIntervention from './model/PatientIntervention';
import PatientInterventionsList200Response from './model/PatientInterventionsList200Response';
import PatientLabResultSet from './model/PatientLabResultSet';
import PatientLabResultsList200Response from './model/PatientLabResultsList200Response';
import PatientMessage from './model/PatientMessage';
import PatientMessageAttachment from './model/PatientMessageAttachment';
import PatientMessagesList200Response from './model/PatientMessagesList200Response';
import PatientPaymentLogList200Response from './model/PatientPaymentLogList200Response';
import PatientPaymentsList200Response from './model/PatientPaymentsList200Response';
import PatientPhysicalExam from './model/PatientPhysicalExam';
import PatientPhysicalExamsList200Response from './model/PatientPhysicalExamsList200Response';
import PatientProblem from './model/PatientProblem';
import PatientRiskAssessment from './model/PatientRiskAssessment';
import PatientRiskAssessmentsList200Response from './model/PatientRiskAssessmentsList200Response';
import PatientVaccineRecord from './model/PatientVaccineRecord';
import PatientVaccineRecordsList200Response from './model/PatientVaccineRecordsList200Response';
import PatientsList200Response from './model/PatientsList200Response';
import PhoneCallLog from './model/PhoneCallLog';
import PrescriptionMessage from './model/PrescriptionMessage';
import PrescriptionMessagesList200Response from './model/PrescriptionMessagesList200Response';
import PrimaryInsurance from './model/PrimaryInsurance';
import ProblemsList200Response from './model/ProblemsList200Response';
import ReminderProfile from './model/ReminderProfile';
import ReminderProfilesList200Response from './model/ReminderProfilesList200Response';
import ReminderTemplate from './model/ReminderTemplate';
import ScannedClinicalDocument from './model/ScannedClinicalDocument';
import SecondaryInsurance from './model/SecondaryInsurance';
import SimpleReminder from './model/SimpleReminder';
import SoapNoteCustomReport from './model/SoapNoteCustomReport';
import SoapNoteCustomReport1 from './model/SoapNoteCustomReport1';
import SoapNoteLineItemFieldType from './model/SoapNoteLineItemFieldType';
import SoapNoteLineItemFieldValue from './model/SoapNoteLineItemFieldValue';
import SublabsList200Response from './model/SublabsList200Response';
import SystemVitals from './model/SystemVitals';
import Task from './model/Task';
import TaskCategoriesList200Response from './model/TaskCategoriesList200Response';
import TaskCategory from './model/TaskCategory';
import TaskNote from './model/TaskNote';
import TaskNote1 from './model/TaskNote1';
import TaskNotesList200Response from './model/TaskNotesList200Response';
import TaskReminder from './model/TaskReminder';
import TaskStatus from './model/TaskStatus';
import TaskStatusesList200Response from './model/TaskStatusesList200Response';
import TaskTemplate from './model/TaskTemplate';
import TaskTemplatesList200Response from './model/TaskTemplatesList200Response';
import TasksList200Response from './model/TasksList200Response';
import TertiaryInsurance from './model/TertiaryInsurance';
import TransactionsList200Response from './model/TransactionsList200Response';
import UserGroupsList200Response from './model/UserGroupsList200Response';
import UserProfile from './model/UserProfile';
import UserProfilesGroup from './model/UserProfilesGroup';
import UsersList200Response from './model/UsersList200Response';
import VaccineDose from './model/VaccineDose';
import Value from './model/Value';
import WorkerCompInsurance from './model/WorkerCompInsurance';
import AdministrativeApi from './api/AdministrativeApi';
import BillingApi from './api/BillingApi';
import ClinicalApi from './api/ClinicalApi';
import PracticeManagementApi from './api/PracticeManagementApi';


/**
* This document is intended as a detailed reference for the precise behavior of the drchrono API. If this is your first time using the API, start with our &lt;a href&#x3D;\&quot;/api-docs-old/tutorial\&quot;&gt;tutorial&lt;/a&gt;. If you are upgrading from a previous version, take a look at the changelog section.  # Authorization  ## Initial authorization  There are three main steps in the OAuth 2.0 authentication workflow:  1. Redirect the provider to the authorization page. 2. The provider authorizes your application and is redirected back to    your web application. 3. Your application exchanges the &#x60;authorization_code&#x60; that came with    the redirect for an &#x60;access_token&#x60; and &#x60;refresh_token&#x60;.  ### Step 1: Redirect to drchrono  The first step is redirecting your user to drchrono, typically with a button labeled \&quot;Connect to drchrono\&quot; or \&quot;Login with drchrono\&quot;.  This is just a link that takes your user to the following URL:      https://drchrono.com/o/authorize/?redirect_uri&#x3D;REDIRECT_URI_ENCODED&amp;response_type&#x3D;code&amp;client_id&#x3D;CLIENT_ID_ENCODED&amp;scope&#x3D;SCOPES_ENCODED  - &#x60;REDIRECT_URI_ENCODED&#x60; is the URL-encoded version of the redirect URI (as registered for your application and used in later steps). - &#x60;CLIENT_ID_ENCODED&#x60; is the URL-encoded version of your application&#39;s client ID. - &#x60;SCOPES_ENCODED&#x60; is a URL-encoded version of a space-separated list of scopes, which can be found in each endpoint or omitted to default to all scopes.  The &#x60;scope&#x60; parameter consists of an optional, space-separated list of scopes your application is requesting. If omitted, all scopes will be requested.  Scopes are of the form &#x60;BASE_SCOPE:[read|write]&#x60; where &#x60;BASE_SCOPE&#x60; is any of &#x60;user&#x60;, &#x60;calendar&#x60;, &#x60;patients&#x60;, &#x60;patients:summary&#x60;, &#x60;billing&#x60;, &#x60;clinical&#x60; and &#x60;labs&#x60;. You should request only the scopes you need. For instance, an application which sends \&quot;Happy Birthday!\&quot; emails to a doctor&#39;s patients on their birthdays would use the scope parameter &#x60;\&quot;patients:summary:read\&quot;&#x60;, while one that allows patients to schedule appointments online would need at least &#x60;\&quot;patients:summary:read patients:summary:write calendar:read calendar:write clinical:read clinical:write\&quot;&#x60;.  ### Step 2: Provider authorization  After logging in (if necessary), the provider will be presented with a screen with your application&#39;s name and the list of permissions you requested (via the &#x60;scope&#x60; parameter).  When they click the \&quot;Authorize\&quot; button, they will be redirected to your redirect URI with a &#x60;code&#x60; query parameter appended, which contains an authorization code to be used in step 3.  If they click the \&quot;Cancel\&quot; button, they will be redirected to your redirect URI with &#x60;error&#x3D;access_denied&#x60; instead.  Note: This authorization code expires extremely quickly, so you must perform step 3 immediately, ideally before rendering the resulting page for the end user.  ### Step 3: Token exchange  The &#x60;code&#x60; obtained from step 2 is usable exactly once to obtain an access token and refresh token.  Here is an example token exchange in Python:      import datetime, pytz, requests      if &#39;error&#39; in get_params:         raise ValueError(&#39;Error authorizing application: %s&#39; % get_params[error])      response &#x3D; requests.post(&#39;https://drchrono.com/o/token/&#39;, data&#x3D;{         &#39;code&#39;: get_params[&#39;code&#39;],         &#39;grant_type&#39;: &#39;authorization_code&#39;,         &#39;redirect_uri&#39;: &#39;http://mytestapp.com/redirect_uri&#39;,         &#39;client_id&#39;: &#39;abcdefg12345&#39;,         &#39;client_secret&#39;: &#39;abcdefg12345&#39;,     })     response.raise_for_status()     data &#x3D; response.json()      # Save these in your database associated with the user     access_token &#x3D; data[&#39;access_token&#39;]     refresh_token &#x3D; data[&#39;refresh_token&#39;]     expires_timestamp &#x3D; datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds&#x3D;data[&#39;expires_in&#39;])  You now have all you need to make API requests authenticated as that provider. When using this access token, you&#39;ll only be able to access the data that the user has access to and that you have been granted permissions for.  ## Refreshing an access token  Access tokens only last 48 hours (given in seconds in the &#x60;&#39;expires_in&#39;&#x60; key in the token exchange step above), so they occasionally need to be refreshed.  It would be inconvenient to ask the user to re-authorize every time, so instead you can use the refresh token like the original authorization to obtain a new access token.  Replace the &#x60;code&#x60; parameter with &#x60;refresh_token&#x60;, change the value &#x60;grant_type&#x60; from &#x60;authorization_code&#x60; to &#x60;refresh_token&#x60;, and omit the &#x60;redirect_uri&#x60; parameter.  Example in Python:      ...     response &#x3D; requests.post(&#39;https://drchrono.com/o/token/&#39;, data&#x3D;{         &#39;refresh_token&#39;: get_refresh_token(),         &#39;grant_type&#39;: &#39;refresh_token&#39;,         &#39;client_id&#39;: &#39;abcdefg12345&#39;,         &#39;client_secret&#39;: &#39;abcdefg12345&#39;,     })     ...  # Webhooks  In order to use drchrono API webhooks, you first need to have an API application on file (even if it is in Test Model). Each API webhook is associated with one API application, go to &lt;a href&#x3D;\&quot;/api-management/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt; to set up both API applications and webhooks!  Once you registered an API application, you will see webhook section in each saved API applications. Create a webhook and register some events there and save all the changes, then you are good to go!  ## Webhooks setup  All fields under webhooks section are required.  **Callback URL** Callback URl is used to receive all hooks when subscribed events are triggered. This should be an URL under your control.  **Secret token** Secret token is used to verify webhooks, this is very important, please set something with high entropy. Also we will talk more about this later.  **Events**  Events is used to register events you want to receiver notification when they happen. Currently we support following events.  Event name | Event description ---------- | ----------------- &#x60;APPOINTMENT_CREATE&#x60; | We will deliver a hook any time an appointment is created &#x60;APPOINTMENT_MODIFY&#x60; | We will deliver a hook any time an appointment is modified &#x60;PATIENT_CREATE&#x60; | We will deliver a hook any time a patient is created &#x60;PATIENT_MODIFY&#x60; | We will deliver a hook any time a patient is modified &#x60;PATIENT_PROBLEM_CREATE&#x60; | We will deliver a hook any time a patient problem is created &#x60;PATIENT_PROBLEM_MODIFY&#x60; | We will deliver a hook any time a patient problem is modified &#x60;PATIENT_ALLERGY_CREATE&#x60; | We will deliver a hook any time a patient allergy is created &#x60;PATIENT_ALLERGY_MODIFY&#x60; | We will deliver a hook any time a patient allergy is modified &#x60;PATIENT_MEDICATION_CREATE&#x60; | We will deliver a hook any time a patient medication is created &#x60;PATIENT_MEDICATION_MODIFY&#x60; | We will deliver a hook any time a patient medication is modified &#x60;CLINICAL_NOTE_LOCK&#x60; | We will deliver a hook any time a clinical note is locked &#x60;CLINICAL_NOTE_UNLOCK&#x60; | We will deliver a hook any time a clinical note is unlocked &#x60;TASK_CREATE&#x60; | We will deliver a hook any time a task is created &#x60;TASK_MODIFY&#x60; | We will deliver a hook any time a task is modified and any time creation, modification and deletion of task notes, associated task item &#x60;TASK_DELETE&#x60; | We will deliver a hook any time a task is deleted   ## Webhooks verification  In order to make sure the callback URL in webhook is under your control, we added a verification step before we send any hooks out to you.  Verification can be done by clicking \&quot;Verify webhook\&quot; button in webhooks setup page. After you click the button, we will send a &#x60;GET&#x60; request to the callback URL, along with a parameter called &#x60;msg&#x60;.  Please use your webhook&#39;s secret token as hash key and SHA-256 as digest constructor, hash the &#x60;msg&#x60; value with &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc2104.html\&quot;&gt;HMAC algorithm&lt;/a&gt;. And we expect a &#x60;200&#x60; JSON response, in JSON response body, there should be a key called &#x60;secret_token&#x60; existing, and its value should be equal to the &lt;strong&gt;hashed&lt;/strong&gt; &#x60;msg&#x60;. Otherwise, verification will fail.  Here is an example webhook verification in Python:      import hashlib, hmac      def webhook_verify(request):         secret_token &#x3D; hmac.new(WEBHOOK_SECRET_TOKEN, request.GET[&#39;msg&#39;], hashlib.sha256).hexdigest()         return json_response({             &#39;secret_token&#39;: secret_token         })  &lt;div class&#x3D;\&quot;alert alert-warning\&quot;&gt; &lt;b&gt;Note:&lt;/b&gt; Verification will be needed when webhook is first created and anytime callback URl is changed. &lt;/div&gt;   ## Webhooks header and body  **Header**  Key | Value --- | ----- &#x60;X-drchrono-event&#x60; | Event that triggered this hook, could be any one event above or &#x60;PING&#x60; &#x60;X-drchrono-signature&#x60; | Secret token associated with this webhook &#x60;X-drchrono-delivery&#x60; | ID of this delivery  **Body**  Key | Value --- | ----- &#x60;receiver&#x60; | This will be an JSON representation of the webhook &#x60;object&#x60; | This will be an JSON representation of the object related to the triggered event, this would share same serializer as drchrono API  ## Webhooks ping and deliveries  Webhooks ping and deliveries will be sent as &#x60;POST&#x60; requests.  **PING**:  You can always ping your webhook to check things, by clicking the \&quot;Ping webhook\&quot; button in webhook setup page. And a hook with header &#x60;X-drchrono-event: PING&#x60; would be sent to the callback URL.  **Deliveries**:  You can check recent deliveries by clicking the \&quot;deliveries\&quot; link in webhook setup page. And you can resend a hook by clicking \&quot;redeliver\&quot; button after select a specific delivery.  ## Webhooks delivery mechanism  We will delivery a hook the moment a subscribed event is triggered. We will not record any response header or body you send back after you receive the hook. However we only consider the response status code. We will consider any &#x60;2xx&#x60; responses as successfully delivered. Any other responses, like &#x60;302&#x60; would be considered failing. And we will try to redeliver unsuccessfully delivered hooks 3 times, first redeliver happens at 1 hour after the initial event, second receliver happens 3 hours after the initial event, and the third redeliver happens 7 hours after the initial event. After these redeliveries, if the delivery is still unsuccessful, you have to redeliver it by hand.   ## Webhooks security  You may want to secure your webhooks to only consider requests send out from drchrono. And this is where &lt;code&gt;secret_token&lt;/code&gt; is needed in request header. Try to set the &lt;code&gt;secret_token&lt;/code&gt; to something with high entropy, a good example could be taking the output of &lt;code&gt;ruby -rsecurerandom -e &#39;puts SecureRandom.hex(20)&#39;&lt;/code&gt;. After this, you might want to verify all request headers you received on your server with this token.   # iframe integration  Some API apps provide additional functionality for interacting with patient data not offered by drchrono, and can benefit by being incorporated into drchrono&#39;s patient information page via iframe.  We have created a simple API to make this possible.  To make an existing API application accessible via an iframe on the patient page, you need to update either \&quot;Patient iframe\&quot; or \&quot;Clinical note iframe\&quot; section in API management page, to make the iframe to appear on (either the patient page or the clinical note page), with the URL that the iframe will use for each page, and the height it should have. The application will be reviewed before it is approved to ensure that it is functional and secure.  ## Register a Doctor  iframe applications will appear as choices on the left-hand menu of the patient page for doctors registered with your application.  To register a doctor with your application, make a &#x60;POST&#x60; request to the &#x60;/api/iframe_integration&#x60; endpoint using the access token for the corresponding doctor. This endpoint does not expect any payload.  To disable your iframe application for a doctor, make a &#x60;DELETE&#x60; request to the same endpoint.  ## Populating the iframe  There are two places where the iframe can be displayed, either within the patient detail page or the clinical note page, shown below respectively:  &lt;img src&#x3D;\&quot;{% asset &#39;public/images/iframe_patient_page.png&#39; %}\&quot; alt&#x3D;\&quot;Iframe on the patient page\&quot;/&gt;  &lt;img src&#x3D;\&quot;{% asset &#39;public/images/iframe_clinical_note.png&#39; %}\&quot; alt&#x3D;\&quot;Iframe on the clinical note page\&quot;/&gt;  When requesting approval for your iframe app, you must specify a URL for one or both of these pages which will serve as the base URL for your IFrame contents. When a doctor views your iframe, the source URL will have various query parameters appended to it, for example for the patient page the &#x60;src&#x60; parameter of the IFrame will be:  &#x60;&#x60;&#x60; &lt;iframe_url&gt;?doctor_id&#x3D;&lt;doctor_id&gt;&amp;patient_id&#x3D;&lt;patient_id&gt;&amp;practice_id&#x3D;&lt;practice_id&gt;&amp;iat&#x3D;&lt;iat&gt;&amp;jwt&#x3D;&lt;jwt&gt; &#x60;&#x60;&#x60;  The &#x60;jwt&#x60; parameter is crucial if your application transfers any sort of PHI and does not implement its own login system.  It encapsulates the other parameters in a [JSON web token (JWT)](http://jwt.io) and signs them using SHA-256 HMAC with your &#x60;client_secret&#x60; as the key.  This verifies that the iframe is being loaded within one of drchrono&#39;s pages by an authorized user.  In production, you should validate the JWT using an approved library (which are listed on the [official site](http://jwt.io)), and only use the parameters extracted from the JWT.  Using Python and Django, this might look like:      import jwt      CLIENT_SECRET &#x3D; &lt;client_secret&gt;     MAX_TIME_DRIFT_SECONDS &#x3D; 60      def validate_parameters(request):         token &#x3D; request.GET[&#39;jwt&#39;]          return jwt.decode(token, CLIENT_SECRET, algorithms&#x3D;[&#39;HS256&#39;], leeway&#x3D;MAX_TIME_DRIFT_SECONDS)  Modern browsers&#39; same-origin policy means that data cannot be passed between your application and drchrono&#39;s page through the iframe.  Therefore, interaction must happen through the API, using information provided in JWT.  # Versions and deprecation  ## Stability Policy  Changes to this API version will be limited to adding endpoints, or adding fields to existing endpoints, or adding optional query parameters. Any new fields which are not read-only will be optional.  ## Deprecation Policy  The drchrono API is versioned. Versions can be in the following states:  * **Active:** This is our latest and greatest version of the API. It is actively supported by our API team and is improved upon with new features, bug fixes and optimizations that do not break backwards compatibility.  * **Deprecated:** A deprecated API version is considered second best--having been surpassed by our active API version. An API version remains in this state for one year, after which time it falls to the not supported state. A deprecated API version is passively supported; while it won&#39;t be removed until becoming unsupported, it may not receive new features but will likely be subject to security updates and performance improvements.  * **Unsupported:** An API version in the not supported state may be deactivated at any time. An application using an unsupported API version should migrate to an active API version.  ## Version Map | Version Name | Previous Name | Start Date | Deprecation Date | |--------------|---------------|------------|------------------| | v2           | v2015_08      | 08/2015    | TBA              | | v3           | v2016_06      | 06/2016    |                  | | v4           | N/A           | 09/2018    |                  |  If you are looking for documentation for an older version  - [V4(Hunt Valley)](/api-docs-old/v4/documentation) (old V4 documentation) - [V3(Sunnyvale)](/api-docs-old/v3/documentation) - [V2(Mountain View)](/api-docs-old/v2/documentation)  # Changelog  Here&#39;s changelog for different versions  - [V4 Changelog](/api-docs-old/v4/changelog) - [V3 changelog](/api-docs-old/v3/changelog)  .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var OpenapiJsClient = require('index'); // See note below*.
* var xxxSvc = new OpenapiJsClient.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new OpenapiJsClient.Yyy(); // Construct a model instance.
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
* var xxxSvc = new OpenapiJsClient.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new OpenapiJsClient.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version v4 (Hunt Valley)
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AllergiesList200Response model constructor.
     * @property {module:model/AllergiesList200Response}
     */
    AllergiesList200Response,

    /**
     * The AmendmentsList200Response model constructor.
     * @property {module:model/AmendmentsList200Response}
     */
    AmendmentsList200Response,

    /**
     * The Appointment model constructor.
     * @property {module:model/Appointment}
     */
    Appointment,

    /**
     * The AppointmentProfile model constructor.
     * @property {module:model/AppointmentProfile}
     */
    AppointmentProfile,

    /**
     * The AppointmentProfilesList200Response model constructor.
     * @property {module:model/AppointmentProfilesList200Response}
     */
    AppointmentProfilesList200Response,

    /**
     * The AppointmentStatusTransition model constructor.
     * @property {module:model/AppointmentStatusTransition}
     */
    AppointmentStatusTransition,

    /**
     * The AppointmentTemplate model constructor.
     * @property {module:model/AppointmentTemplate}
     */
    AppointmentTemplate,

    /**
     * The AppointmentTemplatesList200Response model constructor.
     * @property {module:model/AppointmentTemplatesList200Response}
     */
    AppointmentTemplatesList200Response,

    /**
     * The AppointmentsList200Response model constructor.
     * @property {module:model/AppointmentsList200Response}
     */
    AppointmentsList200Response,

    /**
     * The AssociatedTaskItem model constructor.
     * @property {module:model/AssociatedTaskItem}
     */
    AssociatedTaskItem,

    /**
     * The AutoAccidentInsurance model constructor.
     * @property {module:model/AutoAccidentInsurance}
     */
    AutoAccidentInsurance,

    /**
     * The BillingLineItem model constructor.
     * @property {module:model/BillingLineItem}
     */
    BillingLineItem,

    /**
     * The BillingProfile model constructor.
     * @property {module:model/BillingProfile}
     */
    BillingProfile,

    /**
     * The BillingProfilesList200Response model constructor.
     * @property {module:model/BillingProfilesList200Response}
     */
    BillingProfilesList200Response,

    /**
     * The CarePlan model constructor.
     * @property {module:model/CarePlan}
     */
    CarePlan,

    /**
     * The CarePlansList200Response model constructor.
     * @property {module:model/CarePlansList200Response}
     */
    CarePlansList200Response,

    /**
     * The CareTeamMember model constructor.
     * @property {module:model/CareTeamMember}
     */
    CareTeamMember,

    /**
     * The CareTeamMembersList200Response model constructor.
     * @property {module:model/CareTeamMembersList200Response}
     */
    CareTeamMembersList200Response,

    /**
     * The CashPayment model constructor.
     * @property {module:model/CashPayment}
     */
    CashPayment,

    /**
     * The CashPaymentLog model constructor.
     * @property {module:model/CashPaymentLog}
     */
    CashPaymentLog,

    /**
     * The ClaimBillingNotes model constructor.
     * @property {module:model/ClaimBillingNotes}
     */
    ClaimBillingNotes,

    /**
     * The ClaimBillingNotes1 model constructor.
     * @property {module:model/ClaimBillingNotes1}
     */
    ClaimBillingNotes1,

    /**
     * The ClaimBillingNotesList200Response model constructor.
     * @property {module:model/ClaimBillingNotesList200Response}
     */
    ClaimBillingNotesList200Response,

    /**
     * The ClinicalNote model constructor.
     * @property {module:model/ClinicalNote}
     */
    ClinicalNote,

    /**
     * The ClinicalNote1 model constructor.
     * @property {module:model/ClinicalNote1}
     */
    ClinicalNote1,

    /**
     * The ClinicalNoteField model constructor.
     * @property {module:model/ClinicalNoteField}
     */
    ClinicalNoteField,

    /**
     * The ClinicalNoteFieldTypesList200Response model constructor.
     * @property {module:model/ClinicalNoteFieldTypesList200Response}
     */
    ClinicalNoteFieldTypesList200Response,

    /**
     * The ClinicalNoteFieldValuesList200Response model constructor.
     * @property {module:model/ClinicalNoteFieldValuesList200Response}
     */
    ClinicalNoteFieldValuesList200Response,

    /**
     * The ClinicalNoteSection model constructor.
     * @property {module:model/ClinicalNoteSection}
     */
    ClinicalNoteSection,

    /**
     * The ClinicalNoteTemplatesList200Response model constructor.
     * @property {module:model/ClinicalNoteTemplatesList200Response}
     */
    ClinicalNoteTemplatesList200Response,

    /**
     * The ClinicalNotesList200Response model constructor.
     * @property {module:model/ClinicalNotesList200Response}
     */
    ClinicalNotesList200Response,

    /**
     * The CommLogsList200Response model constructor.
     * @property {module:model/CommLogsList200Response}
     */
    CommLogsList200Response,

    /**
     * The ConsentForm model constructor.
     * @property {module:model/ConsentForm}
     */
    ConsentForm,

    /**
     * The ConsentFormsList200Response model constructor.
     * @property {module:model/ConsentFormsList200Response}
     */
    ConsentFormsList200Response,

    /**
     * The Coverage model constructor.
     * @property {module:model/Coverage}
     */
    Coverage,

    /**
     * The CptCodesInner model constructor.
     * @property {module:model/CptCodesInner}
     */
    CptCodesInner,

    /**
     * The CustomAppointmentFieldType model constructor.
     * @property {module:model/CustomAppointmentFieldType}
     */
    CustomAppointmentFieldType,

    /**
     * The CustomAppointmentFieldValue model constructor.
     * @property {module:model/CustomAppointmentFieldValue}
     */
    CustomAppointmentFieldValue,

    /**
     * The CustomAppointmentFieldsList200Response model constructor.
     * @property {module:model/CustomAppointmentFieldsList200Response}
     */
    CustomAppointmentFieldsList200Response,

    /**
     * The CustomDemographicsList200Response model constructor.
     * @property {module:model/CustomDemographicsList200Response}
     */
    CustomDemographicsList200Response,

    /**
     * The CustomInsurancePlanName model constructor.
     * @property {module:model/CustomInsurancePlanName}
     */
    CustomInsurancePlanName,

    /**
     * The CustomInsurancePlanNamesList200Response model constructor.
     * @property {module:model/CustomInsurancePlanNamesList200Response}
     */
    CustomInsurancePlanNamesList200Response,

    /**
     * The CustomPatientFieldType model constructor.
     * @property {module:model/CustomPatientFieldType}
     */
    CustomPatientFieldType,

    /**
     * The CustomPatientFieldValue model constructor.
     * @property {module:model/CustomPatientFieldValue}
     */
    CustomPatientFieldValue,

    /**
     * The CustomProcedureCodesInner model constructor.
     * @property {module:model/CustomProcedureCodesInner}
     */
    CustomProcedureCodesInner,

    /**
     * The CustomVitalType model constructor.
     * @property {module:model/CustomVitalType}
     */
    CustomVitalType,

    /**
     * The CustomVitalValue model constructor.
     * @property {module:model/CustomVitalValue}
     */
    CustomVitalValue,

    /**
     * The CustomVitalsList200Response model constructor.
     * @property {module:model/CustomVitalsList200Response}
     */
    CustomVitalsList200Response,

    /**
     * The Doctor model constructor.
     * @property {module:model/Doctor}
     */
    Doctor,

    /**
     * The DoctorFeeSchedule model constructor.
     * @property {module:model/DoctorFeeSchedule}
     */
    DoctorFeeSchedule,

    /**
     * The DoctorMessage model constructor.
     * @property {module:model/DoctorMessage}
     */
    DoctorMessage,

    /**
     * The DoctorsList200Response model constructor.
     * @property {module:model/DoctorsList200Response}
     */
    DoctorsList200Response,

    /**
     * The DocumentsList200Response model constructor.
     * @property {module:model/DocumentsList200Response}
     */
    DocumentsList200Response,

    /**
     * The EOBObject model constructor.
     * @property {module:model/EOBObject}
     */
    EOBObject,

    /**
     * The EligibilityChecksList200Response model constructor.
     * @property {module:model/EligibilityChecksList200Response}
     */
    EligibilityChecksList200Response,

    /**
     * The EobsList200Response model constructor.
     * @property {module:model/EobsList200Response}
     */
    EobsList200Response,

    /**
     * The FeeSchedulesList200Response model constructor.
     * @property {module:model/FeeSchedulesList200Response}
     */
    FeeSchedulesList200Response,

    /**
     * The HcpcsCodesInner model constructor.
     * @property {module:model/HcpcsCodesInner}
     */
    HcpcsCodesInner,

    /**
     * The ICD10Code model constructor.
     * @property {module:model/ICD10Code}
     */
    ICD10Code,

    /**
     * The ImplantableDevice model constructor.
     * @property {module:model/ImplantableDevice}
     */
    ImplantableDevice,

    /**
     * The ImplantableDevicesList200Response model constructor.
     * @property {module:model/ImplantableDevicesList200Response}
     */
    ImplantableDevicesList200Response,

    /**
     * The Insurance model constructor.
     * @property {module:model/Insurance}
     */
    Insurance,

    /**
     * The InsurancesList200Response model constructor.
     * @property {module:model/InsurancesList200Response}
     */
    InsurancesList200Response,

    /**
     * The InventoryCategoriesList200Response model constructor.
     * @property {module:model/InventoryCategoriesList200Response}
     */
    InventoryCategoriesList200Response,

    /**
     * The InventoryCategory model constructor.
     * @property {module:model/InventoryCategory}
     */
    InventoryCategory,

    /**
     * The InventoryVaccine model constructor.
     * @property {module:model/InventoryVaccine}
     */
    InventoryVaccine,

    /**
     * The InventoryVaccinesList200Response model constructor.
     * @property {module:model/InventoryVaccinesList200Response}
     */
    InventoryVaccinesList200Response,

    /**
     * The LabDocumentsList200Response model constructor.
     * @property {module:model/LabDocumentsList200Response}
     */
    LabDocumentsList200Response,

    /**
     * The LabOrder model constructor.
     * @property {module:model/LabOrder}
     */
    LabOrder,

    /**
     * The LabOrderDocument model constructor.
     * @property {module:model/LabOrderDocument}
     */
    LabOrderDocument,

    /**
     * The LabOrdersList200Response model constructor.
     * @property {module:model/LabOrdersList200Response}
     */
    LabOrdersList200Response,

    /**
     * The LabResult model constructor.
     * @property {module:model/LabResult}
     */
    LabResult,

    /**
     * The LabResultsList200Response model constructor.
     * @property {module:model/LabResultsList200Response}
     */
    LabResultsList200Response,

    /**
     * The LabTest model constructor.
     * @property {module:model/LabTest}
     */
    LabTest,

    /**
     * The LabTestsList200Response model constructor.
     * @property {module:model/LabTestsList200Response}
     */
    LabTestsList200Response,

    /**
     * The LabVendorLocation model constructor.
     * @property {module:model/LabVendorLocation}
     */
    LabVendorLocation,

    /**
     * The LineItemTransaction model constructor.
     * @property {module:model/LineItemTransaction}
     */
    LineItemTransaction,

    /**
     * The LineItemsList200Response model constructor.
     * @property {module:model/LineItemsList200Response}
     */
    LineItemsList200Response,

    /**
     * The MedicationsList200Response model constructor.
     * @property {module:model/MedicationsList200Response}
     */
    MedicationsList200Response,

    /**
     * The MessageNote model constructor.
     * @property {module:model/MessageNote}
     */
    MessageNote,

    /**
     * The MessagesList200Response model constructor.
     * @property {module:model/MessagesList200Response}
     */
    MessagesList200Response,

    /**
     * The NdcCodeInner model constructor.
     * @property {module:model/NdcCodeInner}
     */
    NdcCodeInner,

    /**
     * The Office model constructor.
     * @property {module:model/Office}
     */
    Office,

    /**
     * The OfficeOnlineHours model constructor.
     * @property {module:model/OfficeOnlineHours}
     */
    OfficeOnlineHours,

    /**
     * The OfficesList200Response model constructor.
     * @property {module:model/OfficesList200Response}
     */
    OfficesList200Response,

    /**
     * The OpenSlot model constructor.
     * @property {module:model/OpenSlot}
     */
    OpenSlot,

    /**
     * The Patient model constructor.
     * @property {module:model/Patient}
     */
    Patient,

    /**
     * The Patient1 model constructor.
     * @property {module:model/Patient1}
     */
    Patient1,

    /**
     * The PatientAllergy model constructor.
     * @property {module:model/PatientAllergy}
     */
    PatientAllergy,

    /**
     * The PatientAmendment model constructor.
     * @property {module:model/PatientAmendment}
     */
    PatientAmendment,

    /**
     * The PatientCommunication model constructor.
     * @property {module:model/PatientCommunication}
     */
    PatientCommunication,

    /**
     * The PatientCommunicationsList200Response model constructor.
     * @property {module:model/PatientCommunicationsList200Response}
     */
    PatientCommunicationsList200Response,

    /**
     * The PatientDrug model constructor.
     * @property {module:model/PatientDrug}
     */
    PatientDrug,

    /**
     * The PatientFlag model constructor.
     * @property {module:model/PatientFlag}
     */
    PatientFlag,

    /**
     * The PatientFlagType model constructor.
     * @property {module:model/PatientFlagType}
     */
    PatientFlagType,

    /**
     * The PatientFlagType1 model constructor.
     * @property {module:model/PatientFlagType1}
     */
    PatientFlagType1,

    /**
     * The PatientFlagTypesList200Response model constructor.
     * @property {module:model/PatientFlagTypesList200Response}
     */
    PatientFlagTypesList200Response,

    /**
     * The PatientIntervention model constructor.
     * @property {module:model/PatientIntervention}
     */
    PatientIntervention,

    /**
     * The PatientInterventionsList200Response model constructor.
     * @property {module:model/PatientInterventionsList200Response}
     */
    PatientInterventionsList200Response,

    /**
     * The PatientLabResultSet model constructor.
     * @property {module:model/PatientLabResultSet}
     */
    PatientLabResultSet,

    /**
     * The PatientLabResultsList200Response model constructor.
     * @property {module:model/PatientLabResultsList200Response}
     */
    PatientLabResultsList200Response,

    /**
     * The PatientMessage model constructor.
     * @property {module:model/PatientMessage}
     */
    PatientMessage,

    /**
     * The PatientMessageAttachment model constructor.
     * @property {module:model/PatientMessageAttachment}
     */
    PatientMessageAttachment,

    /**
     * The PatientMessagesList200Response model constructor.
     * @property {module:model/PatientMessagesList200Response}
     */
    PatientMessagesList200Response,

    /**
     * The PatientPaymentLogList200Response model constructor.
     * @property {module:model/PatientPaymentLogList200Response}
     */
    PatientPaymentLogList200Response,

    /**
     * The PatientPaymentsList200Response model constructor.
     * @property {module:model/PatientPaymentsList200Response}
     */
    PatientPaymentsList200Response,

    /**
     * The PatientPhysicalExam model constructor.
     * @property {module:model/PatientPhysicalExam}
     */
    PatientPhysicalExam,

    /**
     * The PatientPhysicalExamsList200Response model constructor.
     * @property {module:model/PatientPhysicalExamsList200Response}
     */
    PatientPhysicalExamsList200Response,

    /**
     * The PatientProblem model constructor.
     * @property {module:model/PatientProblem}
     */
    PatientProblem,

    /**
     * The PatientRiskAssessment model constructor.
     * @property {module:model/PatientRiskAssessment}
     */
    PatientRiskAssessment,

    /**
     * The PatientRiskAssessmentsList200Response model constructor.
     * @property {module:model/PatientRiskAssessmentsList200Response}
     */
    PatientRiskAssessmentsList200Response,

    /**
     * The PatientVaccineRecord model constructor.
     * @property {module:model/PatientVaccineRecord}
     */
    PatientVaccineRecord,

    /**
     * The PatientVaccineRecordsList200Response model constructor.
     * @property {module:model/PatientVaccineRecordsList200Response}
     */
    PatientVaccineRecordsList200Response,

    /**
     * The PatientsList200Response model constructor.
     * @property {module:model/PatientsList200Response}
     */
    PatientsList200Response,

    /**
     * The PhoneCallLog model constructor.
     * @property {module:model/PhoneCallLog}
     */
    PhoneCallLog,

    /**
     * The PrescriptionMessage model constructor.
     * @property {module:model/PrescriptionMessage}
     */
    PrescriptionMessage,

    /**
     * The PrescriptionMessagesList200Response model constructor.
     * @property {module:model/PrescriptionMessagesList200Response}
     */
    PrescriptionMessagesList200Response,

    /**
     * The PrimaryInsurance model constructor.
     * @property {module:model/PrimaryInsurance}
     */
    PrimaryInsurance,

    /**
     * The ProblemsList200Response model constructor.
     * @property {module:model/ProblemsList200Response}
     */
    ProblemsList200Response,

    /**
     * The ReminderProfile model constructor.
     * @property {module:model/ReminderProfile}
     */
    ReminderProfile,

    /**
     * The ReminderProfilesList200Response model constructor.
     * @property {module:model/ReminderProfilesList200Response}
     */
    ReminderProfilesList200Response,

    /**
     * The ReminderTemplate model constructor.
     * @property {module:model/ReminderTemplate}
     */
    ReminderTemplate,

    /**
     * The ScannedClinicalDocument model constructor.
     * @property {module:model/ScannedClinicalDocument}
     */
    ScannedClinicalDocument,

    /**
     * The SecondaryInsurance model constructor.
     * @property {module:model/SecondaryInsurance}
     */
    SecondaryInsurance,

    /**
     * The SimpleReminder model constructor.
     * @property {module:model/SimpleReminder}
     */
    SimpleReminder,

    /**
     * The SoapNoteCustomReport model constructor.
     * @property {module:model/SoapNoteCustomReport}
     */
    SoapNoteCustomReport,

    /**
     * The SoapNoteCustomReport1 model constructor.
     * @property {module:model/SoapNoteCustomReport1}
     */
    SoapNoteCustomReport1,

    /**
     * The SoapNoteLineItemFieldType model constructor.
     * @property {module:model/SoapNoteLineItemFieldType}
     */
    SoapNoteLineItemFieldType,

    /**
     * The SoapNoteLineItemFieldValue model constructor.
     * @property {module:model/SoapNoteLineItemFieldValue}
     */
    SoapNoteLineItemFieldValue,

    /**
     * The SublabsList200Response model constructor.
     * @property {module:model/SublabsList200Response}
     */
    SublabsList200Response,

    /**
     * The SystemVitals model constructor.
     * @property {module:model/SystemVitals}
     */
    SystemVitals,

    /**
     * The Task model constructor.
     * @property {module:model/Task}
     */
    Task,

    /**
     * The TaskCategoriesList200Response model constructor.
     * @property {module:model/TaskCategoriesList200Response}
     */
    TaskCategoriesList200Response,

    /**
     * The TaskCategory model constructor.
     * @property {module:model/TaskCategory}
     */
    TaskCategory,

    /**
     * The TaskNote model constructor.
     * @property {module:model/TaskNote}
     */
    TaskNote,

    /**
     * The TaskNote1 model constructor.
     * @property {module:model/TaskNote1}
     */
    TaskNote1,

    /**
     * The TaskNotesList200Response model constructor.
     * @property {module:model/TaskNotesList200Response}
     */
    TaskNotesList200Response,

    /**
     * The TaskReminder model constructor.
     * @property {module:model/TaskReminder}
     */
    TaskReminder,

    /**
     * The TaskStatus model constructor.
     * @property {module:model/TaskStatus}
     */
    TaskStatus,

    /**
     * The TaskStatusesList200Response model constructor.
     * @property {module:model/TaskStatusesList200Response}
     */
    TaskStatusesList200Response,

    /**
     * The TaskTemplate model constructor.
     * @property {module:model/TaskTemplate}
     */
    TaskTemplate,

    /**
     * The TaskTemplatesList200Response model constructor.
     * @property {module:model/TaskTemplatesList200Response}
     */
    TaskTemplatesList200Response,

    /**
     * The TasksList200Response model constructor.
     * @property {module:model/TasksList200Response}
     */
    TasksList200Response,

    /**
     * The TertiaryInsurance model constructor.
     * @property {module:model/TertiaryInsurance}
     */
    TertiaryInsurance,

    /**
     * The TransactionsList200Response model constructor.
     * @property {module:model/TransactionsList200Response}
     */
    TransactionsList200Response,

    /**
     * The UserGroupsList200Response model constructor.
     * @property {module:model/UserGroupsList200Response}
     */
    UserGroupsList200Response,

    /**
     * The UserProfile model constructor.
     * @property {module:model/UserProfile}
     */
    UserProfile,

    /**
     * The UserProfilesGroup model constructor.
     * @property {module:model/UserProfilesGroup}
     */
    UserProfilesGroup,

    /**
     * The UsersList200Response model constructor.
     * @property {module:model/UsersList200Response}
     */
    UsersList200Response,

    /**
     * The VaccineDose model constructor.
     * @property {module:model/VaccineDose}
     */
    VaccineDose,

    /**
     * The Value model constructor.
     * @property {module:model/Value}
     */
    Value,

    /**
     * The WorkerCompInsurance model constructor.
     * @property {module:model/WorkerCompInsurance}
     */
    WorkerCompInsurance,

    /**
    * The AdministrativeApi service constructor.
    * @property {module:api/AdministrativeApi}
    */
    AdministrativeApi,

    /**
    * The BillingApi service constructor.
    * @property {module:api/BillingApi}
    */
    BillingApi,

    /**
    * The ClinicalApi service constructor.
    * @property {module:api/ClinicalApi}
    */
    ClinicalApi,

    /**
    * The PracticeManagementApi service constructor.
    * @property {module:api/PracticeManagementApi}
    */
    PracticeManagementApi
};
