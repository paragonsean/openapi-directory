/*
 * 
 * This document is intended as a detailed reference for the precise behavior of the drchrono API. If this is your first time using the API, start with our <a href=\"/api-docs-old/tutorial\">tutorial</a>. If you are upgrading from a previous version, take a look at the changelog section.  # Authorization  ## Initial authorization  There are three main steps in the OAuth 2.0 authentication workflow:  1. Redirect the provider to the authorization page. 2. The provider authorizes your application and is redirected back to    your web application. 3. Your application exchanges the `authorization_code` that came with    the redirect for an `access_token` and `refresh_token`.  ### Step 1: Redirect to drchrono  The first step is redirecting your user to drchrono, typically with a button labeled \"Connect to drchrono\" or \"Login with drchrono\".  This is just a link that takes your user to the following URL:      https://drchrono.com/o/authorize/?redirect_uri=REDIRECT_URI_ENCODED&response_type=code&client_id=CLIENT_ID_ENCODED&scope=SCOPES_ENCODED  - `REDIRECT_URI_ENCODED` is the URL-encoded version of the redirect URI (as registered for your application and used in later steps). - `CLIENT_ID_ENCODED` is the URL-encoded version of your application's client ID. - `SCOPES_ENCODED` is a URL-encoded version of a space-separated list of scopes, which can be found in each endpoint or omitted to default to all scopes.  The `scope` parameter consists of an optional, space-separated list of scopes your application is requesting. If omitted, all scopes will be requested.  Scopes are of the form `BASE_SCOPE:[read|write]` where `BASE_SCOPE` is any of `user`, `calendar`, `patients`, `patients:summary`, `billing`, `clinical` and `labs`. You should request only the scopes you need. For instance, an application which sends \"Happy Birthday!\" emails to a doctor's patients on their birthdays would use the scope parameter `\"patients:summary:read\"`, while one that allows patients to schedule appointments online would need at least `\"patients:summary:read patients:summary:write calendar:read calendar:write clinical:read clinical:write\"`.  ### Step 2: Provider authorization  After logging in (if necessary), the provider will be presented with a screen with your application's name and the list of permissions you requested (via the `scope` parameter).  When they click the \"Authorize\" button, they will be redirected to your redirect URI with a `code` query parameter appended, which contains an authorization code to be used in step 3.  If they click the \"Cancel\" button, they will be redirected to your redirect URI with `error=access_denied` instead.  Note: This authorization code expires extremely quickly, so you must perform step 3 immediately, ideally before rendering the resulting page for the end user.  ### Step 3: Token exchange  The `code` obtained from step 2 is usable exactly once to obtain an access token and refresh token.  Here is an example token exchange in Python:      import datetime, pytz, requests      if 'error' in get_params:         raise ValueError('Error authorizing application: %s' % get_params[error])      response = requests.post('https://drchrono.com/o/token/', data={         'code': get_params['code'],         'grant_type': 'authorization_code',         'redirect_uri': 'http://mytestapp.com/redirect_uri',         'client_id': 'abcdefg12345',         'client_secret': 'abcdefg12345',     })     response.raise_for_status()     data = response.json()      # Save these in your database associated with the user     access_token = data['access_token']     refresh_token = data['refresh_token']     expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])  You now have all you need to make API requests authenticated as that provider. When using this access token, you'll only be able to access the data that the user has access to and that you have been granted permissions for.  ## Refreshing an access token  Access tokens only last 48 hours (given in seconds in the `'expires_in'` key in the token exchange step above), so they occasionally need to be refreshed.  It would be inconvenient to ask the user to re-authorize every time, so instead you can use the refresh token like the original authorization to obtain a new access token.  Replace the `code` parameter with `refresh_token`, change the value `grant_type` from `authorization_code` to `refresh_token`, and omit the `redirect_uri` parameter.  Example in Python:      ...     response = requests.post('https://drchrono.com/o/token/', data={         'refresh_token': get_refresh_token(),         'grant_type': 'refresh_token',         'client_id': 'abcdefg12345',         'client_secret': 'abcdefg12345',     })     ...  # Webhooks  In order to use drchrono API webhooks, you first need to have an API application on file (even if it is in Test Model). Each API webhook is associated with one API application, go to <a href=\"/api-management/\" target=\"_blank\">here</a> to set up both API applications and webhooks!  Once you registered an API application, you will see webhook section in each saved API applications. Create a webhook and register some events there and save all the changes, then you are good to go!  ## Webhooks setup  All fields under webhooks section are required.  **Callback URL** Callback URl is used to receive all hooks when subscribed events are triggered. This should be an URL under your control.  **Secret token** Secret token is used to verify webhooks, this is very important, please set something with high entropy. Also we will talk more about this later.  **Events**  Events is used to register events you want to receiver notification when they happen. Currently we support following events.  Event name | Event description ---------- | ----------------- `APPOINTMENT_CREATE` | We will deliver a hook any time an appointment is created `APPOINTMENT_MODIFY` | We will deliver a hook any time an appointment is modified `PATIENT_CREATE` | We will deliver a hook any time a patient is created `PATIENT_MODIFY` | We will deliver a hook any time a patient is modified `PATIENT_PROBLEM_CREATE` | We will deliver a hook any time a patient problem is created `PATIENT_PROBLEM_MODIFY` | We will deliver a hook any time a patient problem is modified `PATIENT_ALLERGY_CREATE` | We will deliver a hook any time a patient allergy is created `PATIENT_ALLERGY_MODIFY` | We will deliver a hook any time a patient allergy is modified `PATIENT_MEDICATION_CREATE` | We will deliver a hook any time a patient medication is created `PATIENT_MEDICATION_MODIFY` | We will deliver a hook any time a patient medication is modified `CLINICAL_NOTE_LOCK` | We will deliver a hook any time a clinical note is locked `CLINICAL_NOTE_UNLOCK` | We will deliver a hook any time a clinical note is unlocked `TASK_CREATE` | We will deliver a hook any time a task is created `TASK_MODIFY` | We will deliver a hook any time a task is modified and any time creation, modification and deletion of task notes, associated task item `TASK_DELETE` | We will deliver a hook any time a task is deleted   ## Webhooks verification  In order to make sure the callback URL in webhook is under your control, we added a verification step before we send any hooks out to you.  Verification can be done by clicking \"Verify webhook\" button in webhooks setup page. After you click the button, we will send a `GET` request to the callback URL, along with a parameter called `msg`.  Please use your webhook's secret token as hash key and SHA-256 as digest constructor, hash the `msg` value with <a href=\"https://tools.ietf.org/html/rfc2104.html\">HMAC algorithm</a>. And we expect a `200` JSON response, in JSON response body, there should be a key called `secret_token` existing, and its value should be equal to the <strong>hashed</strong> `msg`. Otherwise, verification will fail.  Here is an example webhook verification in Python:      import hashlib, hmac      def webhook_verify(request):         secret_token = hmac.new(WEBHOOK_SECRET_TOKEN, request.GET['msg'], hashlib.sha256).hexdigest()         return json_response({             'secret_token': secret_token         })  <div class=\"alert alert-warning\"> <b>Note:</b> Verification will be needed when webhook is first created and anytime callback URl is changed. </div>   ## Webhooks header and body  **Header**  Key | Value --- | ----- `X-drchrono-event` | Event that triggered this hook, could be any one event above or `PING` `X-drchrono-signature` | Secret token associated with this webhook `X-drchrono-delivery` | ID of this delivery  **Body**  Key | Value --- | ----- `receiver` | This will be an JSON representation of the webhook `object` | This will be an JSON representation of the object related to the triggered event, this would share same serializer as drchrono API  ## Webhooks ping and deliveries  Webhooks ping and deliveries will be sent as `POST` requests.  **PING**:  You can always ping your webhook to check things, by clicking the \"Ping webhook\" button in webhook setup page. And a hook with header `X-drchrono-event: PING` would be sent to the callback URL.  **Deliveries**:  You can check recent deliveries by clicking the \"deliveries\" link in webhook setup page. And you can resend a hook by clicking \"redeliver\" button after select a specific delivery.  ## Webhooks delivery mechanism  We will delivery a hook the moment a subscribed event is triggered. We will not record any response header or body you send back after you receive the hook. However we only consider the response status code. We will consider any `2xx` responses as successfully delivered. Any other responses, like `302` would be considered failing. And we will try to redeliver unsuccessfully delivered hooks 3 times, first redeliver happens at 1 hour after the initial event, second receliver happens 3 hours after the initial event, and the third redeliver happens 7 hours after the initial event. After these redeliveries, if the delivery is still unsuccessful, you have to redeliver it by hand.   ## Webhooks security  You may want to secure your webhooks to only consider requests send out from drchrono. And this is where <code>secret_token</code> is needed in request header. Try to set the <code>secret_token</code> to something with high entropy, a good example could be taking the output of <code>ruby -rsecurerandom -e 'puts SecureRandom.hex(20)'</code>. After this, you might want to verify all request headers you received on your server with this token.   # iframe integration  Some API apps provide additional functionality for interacting with patient data not offered by drchrono, and can benefit by being incorporated into drchrono's patient information page via iframe.  We have created a simple API to make this possible.  To make an existing API application accessible via an iframe on the patient page, you need to update either \"Patient iframe\" or \"Clinical note iframe\" section in API management page, to make the iframe to appear on (either the patient page or the clinical note page), with the URL that the iframe will use for each page, and the height it should have. The application will be reviewed before it is approved to ensure that it is functional and secure.  ## Register a Doctor  iframe applications will appear as choices on the left-hand menu of the patient page for doctors registered with your application.  To register a doctor with your application, make a `POST` request to the `/api/iframe_integration` endpoint using the access token for the corresponding doctor. This endpoint does not expect any payload.  To disable your iframe application for a doctor, make a `DELETE` request to the same endpoint.  ## Populating the iframe  There are two places where the iframe can be displayed, either within the patient detail page or the clinical note page, shown below respectively:  <img src=\"{% asset 'public/images/iframe_patient_page.png' %}\" alt=\"Iframe on the patient page\"/>  <img src=\"{% asset 'public/images/iframe_clinical_note.png' %}\" alt=\"Iframe on the clinical note page\"/>  When requesting approval for your iframe app, you must specify a URL for one or both of these pages which will serve as the base URL for your IFrame contents. When a doctor views your iframe, the source URL will have various query parameters appended to it, for example for the patient page the `src` parameter of the IFrame will be:  ``` <iframe_url>?doctor_id=<doctor_id>&patient_id=<patient_id>&practice_id=<practice_id>&iat=<iat>&jwt=<jwt> ```  The `jwt` parameter is crucial if your application transfers any sort of PHI and does not implement its own login system.  It encapsulates the other parameters in a [JSON web token (JWT)](http://jwt.io) and signs them using SHA-256 HMAC with your `client_secret` as the key.  This verifies that the iframe is being loaded within one of drchrono's pages by an authorized user.  In production, you should validate the JWT using an approved library (which are listed on the [official site](http://jwt.io)), and only use the parameters extracted from the JWT.  Using Python and Django, this might look like:      import jwt      CLIENT_SECRET = <client_secret>     MAX_TIME_DRIFT_SECONDS = 60      def validate_parameters(request):         token = request.GET['jwt']          return jwt.decode(token, CLIENT_SECRET, algorithms=['HS256'], leeway=MAX_TIME_DRIFT_SECONDS)  Modern browsers' same-origin policy means that data cannot be passed between your application and drchrono's page through the iframe.  Therefore, interaction must happen through the API, using information provided in JWT.  # Versions and deprecation  ## Stability Policy  Changes to this API version will be limited to adding endpoints, or adding fields to existing endpoints, or adding optional query parameters. Any new fields which are not read-only will be optional.  ## Deprecation Policy  The drchrono API is versioned. Versions can be in the following states:  * **Active:** This is our latest and greatest version of the API. It is actively supported by our API team and is improved upon with new features, bug fixes and optimizations that do not break backwards compatibility.  * **Deprecated:** A deprecated API version is considered second best--having been surpassed by our active API version. An API version remains in this state for one year, after which time it falls to the not supported state. A deprecated API version is passively supported; while it won't be removed until becoming unsupported, it may not receive new features but will likely be subject to security updates and performance improvements.  * **Unsupported:** An API version in the not supported state may be deactivated at any time. An application using an unsupported API version should migrate to an active API version.  ## Version Map | Version Name | Previous Name | Start Date | Deprecation Date | |--------------|---------------|------------|------------------| | v2           | v2015_08      | 08/2015    | TBA              | | v3           | v2016_06      | 06/2016    |                  | | v4           | N/A           | 09/2018    |                  |  If you are looking for documentation for an older version  - [V4(Hunt Valley)](/api-docs-old/v4/documentation) (old V4 documentation) - [V3(Sunnyvale)](/api-docs-old/v3/documentation) - [V2(Mountain View)](/api-docs-old/v2/documentation)  # Changelog  Here's changelog for different versions  - [V4 Changelog](/api-docs-old/v4/changelog) - [V3 changelog](/api-docs-old/v3/changelog)  
 *
 * The version of the OpenAPI document: v4 (Hunt Valley)
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.Arrays;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Patient1 {
  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private String address;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_FAX = "fax";
  @SerializedName(SERIALIZED_NAME_FAX)
  private String fax;

  public static final String SERIALIZED_NAME_FIRST_NAME = "first_name";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_LAST_NAME = "last_name";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_MIDDLE_NAME = "middle_name";
  @SerializedName(SERIALIZED_NAME_MIDDLE_NAME)
  private String middleName;

  public static final String SERIALIZED_NAME_NPI = "npi";
  @SerializedName(SERIALIZED_NAME_NPI)
  private String npi;

  public static final String SERIALIZED_NAME_PHONE = "phone";
  @SerializedName(SERIALIZED_NAME_PHONE)
  private String phone;

  public static final String SERIALIZED_NAME_PROVIDER_NUMBER = "provider_number";
  @SerializedName(SERIALIZED_NAME_PROVIDER_NUMBER)
  private String providerNumber;

  /**
   * Can be one of following, &#x60;&#39;&#39;&#x60;, &#x60;&#39;0B&#39;&#x60;(State License #), &#x60;&#39;1G&#39;&#x60;(Provider UPIN #), &#x60;&#39;G2&#39;&#x60;(Provider Commercial #)
   */
  @JsonAdapter(ProviderQualifierEnum.Adapter.class)
  public enum ProviderQualifierEnum {
    EMPTY(""),
    
    _0_B("0B"),
    
    _1_G("1G"),
    
    G2("G2");

    private String value;

    ProviderQualifierEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ProviderQualifierEnum fromValue(String value) {
      for (ProviderQualifierEnum b : ProviderQualifierEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ProviderQualifierEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ProviderQualifierEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ProviderQualifierEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ProviderQualifierEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ProviderQualifierEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PROVIDER_QUALIFIER = "provider_qualifier";
  @SerializedName(SERIALIZED_NAME_PROVIDER_QUALIFIER)
  private ProviderQualifierEnum providerQualifier;

  /**
   * Can be one of following, &#x60;&#39;&#39;&#x60;, &#x60;&#39;Acupuncture&#39;&#x60;, &#x60;&#39;Advanced Practice Midwife&#39;&#x60;, &#x60;&#39;Aesthetic Medicine&#39;&#x60;, &#x60;&#39;Aesthetician&#39;&#x60;, &#x60;&#39;Allergist/Immunologist&#39;&#x60;, &#x60;&#39;Anesthesiologist&#39;&#x60;, &#x60;&#39;Cardiac Electrophysiologist&#39;&#x60;, &#x60;&#39;Cardiologist&#39;&#x60;, &#x60;&#39;Cardiothoracic Surgeon&#39;&#x60;, &#x60;&#39;Child/Adolescent Psychiatry&#39;&#x60;, &#x60;&#39;Chiropractor&#39;&#x60;, &#x60;&#39;Clinical Social Worker&#39;&#x60;, &#x60;&#39;Colorectal Surgeon&#39;&#x60;, &#x60;&#39;Correactology&#39;&#x60;, &#x60;&#39;Cosmetic Medicine&#39;&#x60;, &#x60;&#39;Counselor Mental Health&#39;&#x60;, &#x60;&#39;Counselor Professional&#39;&#x60;, &#x60;&#39;Counselor&#39;&#x60;, &#x60;&#39;Dentist&#39;&#x60;, &#x60;&#39;Diabetology&#39;&#x60;, &#x60;&#39;Dermatologist&#39;&#x60;, &#x60;&#39;Diagnostic Medical Sonographer&#39;&#x60;, &#x60;&#39;Dietitian, Registered&#39;&#x60;, &#x60;&#39;Ear-Nose-Throat Specialist (ENT)&#39;&#x60;, &#x60;&#39;Emergency Medicine Physician&#39;&#x60;, &#x60;&#39;Endocrinologist&#39;&#x60;, &#x60;&#39;Endodontist&#39;&#x60;, &#x60;&#39;Epidemiologist&#39;&#x60;, &#x60;&#39;Family Practitioner&#39;&#x60;, &#x60;&#39;Gastroenterologist&#39;&#x60;, &#x60;&#39;General Practice&#39;&#x60;, &#x60;&#39;General Surgeon&#39;&#x60;, &#x60;&#39;Geneticist&#39;&#x60;, &#x60;&#39;Geriatrician&#39;&#x60;, &#x60;&#39;Gerontologist&#39;&#x60;, &#x60;&#39;Gynecologist (no OB)&#39;&#x60;, &#x60;&#39;Gynegologic Oncologist&#39;&#x60;, &#x60;&#39;Hand Surgeon&#39;&#x60;, &#x60;&#39;Hematologist&#39;&#x60;, &#x60;&#39;Home Care&#39;&#x60;, &#x60;&#39;Hospice&#39;&#x60;, &#x60;&#39;Hospitalist&#39;&#x60;, &#x60;&#39;Infectious Disease Specialist&#39;&#x60;, &#x60;&#39;Integrative and Functional Medicine&#39;&#x60;, &#x60;&#39;Integrative Medicine&#39;&#x60;, &#x60;&#39;Internist&#39;&#x60;, &#x60;&#39;Interventional Radiology&#39;&#x60;, &#x60;&#39;Laboratory Medicine Specialist&#39;&#x60;, &#x60;&#39;Laser Surgery&#39;&#x60;, &#x60;&#39;Massage Therapist&#39;&#x60;, &#x60;&#39;Naturopathic Physician&#39;&#x60;, &#x60;&#39;Neonatologist&#39;&#x60;, &#x60;&#39;Nephrologist&#39;&#x60;, &#x60;&#39;Neurologist&#39;&#x60;, &#x60;&#39;Neuropsychology&#39;&#x60;, &#x60;&#39;Neurosurgeon&#39;&#x60;, &#x60;&#39;Not Actively Practicing&#39;&#x60;, &#x60;&#39;Nuclear Medicine Specialist&#39;&#x60;, &#x60;&#39;Nurse Practitioner&#39;&#x60;, &#x60;&#39;Nursing&#39;&#x60;, &#x60;&#39;Nutritionist&#39;&#x60;, &#x60;&#39;Obstetrician/Gynecologist&#39;&#x60;, &#x60;&#39;Occupational Medicine&#39;&#x60;, &#x60;&#39;Occupational Therapist&#39;&#x60;, &#x60;&#39;Oncologist&#39;&#x60;, &#x60;&#39;Ophthalmologist&#39;&#x60;, &#x60;&#39;Optometrist&#39;&#x60;, &#x60;&#39;Oral Surgeon&#39;&#x60;, &#x60;&#39;Orofacial Pain&#39;&#x60;, &#x60;&#39;Orthodontist&#39;&#x60;, &#x60;&#39;Orthopedic Surgeon&#39;&#x60;, &#x60;&#39;Orthotist&#39;&#x60;, &#x60;&#39;Other&#39;&#x60;, &#x60;&#39;Pain Management Specialist&#39;&#x60;, &#x60;&#39;Pathologist&#39;&#x60;, &#x60;&#39;Pediatric Dentist&#39;&#x60;, &#x60;&#39;Pediatric Gastroenterology&#39;&#x60;, &#x60;&#39;Pediatric Surgeon&#39;&#x60;, &#x60;&#39;Pediatrician&#39;&#x60;, &#x60;&#39;Perinatologist&#39;&#x60;, &#x60;&#39;Periodontist&#39;&#x60;, &#x60;&#39;Physical Medicine and Rehab Specialist&#39;&#x60;, &#x60;&#39;Physical Therapist&#39;&#x60;, &#x60;&#39;Physician Assistant&#39;&#x60;, &#x60;&#39;Plastic Surgeon&#39;&#x60;, &#x60;&#39;Podiatrist&#39;&#x60;, &#x60;&#39;Preventive-Aging Medicine&#39;&#x60;, &#x60;&#39;Preventive Medicine/Occupational-Environmental Medicine&#39;&#x60;, &#x60;&#39;Primary Care Physician&#39;&#x60;, &#x60;&#39;Prosthetist&#39;&#x60;, &#x60;&#39;Prosthodontist&#39;&#x60;, &#x60;&#39;Psychiatrist&#39;&#x60;, &#x60;&#39;Psychologist&#39;&#x60;, &#x60;&#39;Public Health Professional&#39;&#x60;, &#x60;&#39;Pulmonologist&#39;&#x60;, &#x60;&#39;Radiation Oncologist&#39;&#x60;, &#x60;&#39;Radiologist&#39;&#x60;, &#x60;&#39;Registered Nurse&#39;&#x60;, &#x60;&#39;Religious Nonmedical Practitioner&#39;&#x60;, &#x60;&#39;Reproductive Endocrinologist&#39;&#x60;, &#x60;&#39;Reproductive Medicine&#39;&#x60;, &#x60;&#39;Rheumatologist&#39;&#x60;, &#x60;&#39;Sleep Medicine&#39;&#x60;, &#x60;&#39;Speech-Language Pathologist&#39;&#x60;, &#x60;&#39;Sports Medicine Specialist&#39;&#x60;, &#x60;&#39;Urologist&#39;&#x60;, &#x60;&#39;Urgent Care&#39;&#x60;, &#x60;&#39;Vascular Surgeon&#39;&#x60;
   */
  @JsonAdapter(SpecialtyEnum.Adapter.class)
  public enum SpecialtyEnum {
    EMPTY(""),
    
    ACUPUNCTURE("Acupuncture"),
    
    ADVANCED_PRACTICE_MIDWIFE("Advanced Practice Midwife"),
    
    AESTHETIC_MEDICINE("Aesthetic Medicine"),
    
    AESTHETICIAN("Aesthetician"),
    
    ALLERGIST_IMMUNOLOGIST("Allergist/Immunologist"),
    
    ANESTHESIOLOGIST("Anesthesiologist"),
    
    CARDIAC_ELECTROPHYSIOLOGIST("Cardiac Electrophysiologist"),
    
    CARDIOLOGIST("Cardiologist"),
    
    CARDIOTHORACIC_SURGEON("Cardiothoracic Surgeon"),
    
    CHILD_ADOLESCENT_PSYCHIATRY("Child/Adolescent Psychiatry"),
    
    CHIROPRACTOR("Chiropractor"),
    
    CLINICAL_SOCIAL_WORKER("Clinical Social Worker"),
    
    COLORECTAL_SURGEON("Colorectal Surgeon"),
    
    CORREACTOLOGY("Correactology"),
    
    COSMETIC_MEDICINE("Cosmetic Medicine"),
    
    COUNSELOR_MENTAL_HEALTH("Counselor Mental Health"),
    
    COUNSELOR_PROFESSIONAL("Counselor Professional"),
    
    COUNSELOR("Counselor"),
    
    DENTIST("Dentist"),
    
    DIABETOLOGY("Diabetology"),
    
    DERMATOLOGIST("Dermatologist"),
    
    DIAGNOSTIC_MEDICAL_SONOGRAPHER("Diagnostic Medical Sonographer"),
    
    DIETITIAN_REGISTERED("Dietitian, Registered"),
    
    EAR_NOSE_THROAT_SPECIALIST_ENT_("Ear-Nose-Throat Specialist (ENT)"),
    
    EMERGENCY_MEDICINE_PHYSICIAN("Emergency Medicine Physician"),
    
    ENDOCRINOLOGIST("Endocrinologist"),
    
    ENDODONTIST("Endodontist"),
    
    EPIDEMIOLOGIST("Epidemiologist"),
    
    FAMILY_PRACTITIONER("Family Practitioner"),
    
    GASTROENTEROLOGIST("Gastroenterologist"),
    
    GENERAL_PRACTICE("General Practice"),
    
    GENERAL_SURGEON("General Surgeon"),
    
    GENETICIST("Geneticist"),
    
    GERIATRICIAN("Geriatrician"),
    
    GERONTOLOGIST("Gerontologist"),
    
    GYNECOLOGIST_NO_OB_("Gynecologist (no OB)"),
    
    GYNEGOLOGIC_ONCOLOGIST("Gynegologic Oncologist"),
    
    HAND_SURGEON("Hand Surgeon"),
    
    HEMATOLOGIST("Hematologist"),
    
    HOME_CARE("Home Care"),
    
    HOSPICE("Hospice"),
    
    HOSPITALIST("Hospitalist"),
    
    INFECTIOUS_DISEASE_SPECIALIST("Infectious Disease Specialist"),
    
    INTEGRATIVE_AND_FUNCTIONAL_MEDICINE("Integrative and Functional Medicine"),
    
    INTEGRATIVE_MEDICINE("Integrative Medicine"),
    
    INTERNIST("Internist"),
    
    INTERVENTIONAL_RADIOLOGY("Interventional Radiology"),
    
    LABORATORY_MEDICINE_SPECIALIST("Laboratory Medicine Specialist"),
    
    LASER_SURGERY("Laser Surgery"),
    
    MASSAGE_THERAPIST("Massage Therapist"),
    
    NATUROPATHIC_PHYSICIAN("Naturopathic Physician"),
    
    NEONATOLOGIST("Neonatologist"),
    
    NEPHROLOGIST("Nephrologist"),
    
    NEUROLOGIST("Neurologist"),
    
    NEUROPSYCHOLOGY("Neuropsychology"),
    
    NEUROSURGEON("Neurosurgeon"),
    
    NOT_ACTIVELY_PRACTICING("Not Actively Practicing"),
    
    NUCLEAR_MEDICINE_SPECIALIST("Nuclear Medicine Specialist"),
    
    NURSE_PRACTITIONER("Nurse Practitioner"),
    
    NURSING("Nursing"),
    
    NUTRITIONIST("Nutritionist"),
    
    OBSTETRICIAN_GYNECOLOGIST("Obstetrician/Gynecologist"),
    
    OCCUPATIONAL_MEDICINE("Occupational Medicine"),
    
    OCCUPATIONAL_THERAPIST("Occupational Therapist"),
    
    ONCOLOGIST("Oncologist"),
    
    OPHTHALMOLOGIST("Ophthalmologist"),
    
    OPTOMETRIST("Optometrist"),
    
    ORAL_SURGEON("Oral Surgeon"),
    
    OROFACIAL_PAIN("Orofacial Pain"),
    
    ORTHODONTIST("Orthodontist"),
    
    ORTHOPEDIC_SURGEON("Orthopedic Surgeon"),
    
    ORTHOTIST("Orthotist"),
    
    OTHER("Other"),
    
    PAIN_MANAGEMENT_SPECIALIST("Pain Management Specialist"),
    
    PATHOLOGIST("Pathologist"),
    
    PEDIATRIC_DENTIST("Pediatric Dentist"),
    
    PEDIATRIC_GASTROENTEROLOGY("Pediatric Gastroenterology"),
    
    PEDIATRIC_SURGEON("Pediatric Surgeon"),
    
    PEDIATRICIAN("Pediatrician"),
    
    PERINATOLOGIST("Perinatologist"),
    
    PERIODONTIST("Periodontist"),
    
    PHYSICAL_MEDICINE_AND_REHAB_SPECIALIST("Physical Medicine and Rehab Specialist"),
    
    PHYSICAL_THERAPIST("Physical Therapist"),
    
    PHYSICIAN_ASSISTANT("Physician Assistant"),
    
    PLASTIC_SURGEON("Plastic Surgeon"),
    
    PODIATRIST("Podiatrist"),
    
    PREVENTIVE_AGING_MEDICINE("Preventive-Aging Medicine"),
    
    PREVENTIVE_MEDICINE_OCCUPATIONAL_ENVIRONMENTAL_MEDICINE("Preventive Medicine/Occupational-Environmental Medicine"),
    
    PRIMARY_CARE_PHYSICIAN("Primary Care Physician"),
    
    PROSTHETIST("Prosthetist"),
    
    PROSTHODONTIST("Prosthodontist"),
    
    PSYCHIATRIST("Psychiatrist"),
    
    PSYCHOLOGIST("Psychologist"),
    
    PUBLIC_HEALTH_PROFESSIONAL("Public Health Professional"),
    
    PULMONOLOGIST("Pulmonologist"),
    
    RADIATION_ONCOLOGIST("Radiation Oncologist"),
    
    RADIOLOGIST("Radiologist"),
    
    REGISTERED_NURSE("Registered Nurse"),
    
    RELIGIOUS_NONMEDICAL_PRACTITIONER("Religious Nonmedical Practitioner"),
    
    REPRODUCTIVE_ENDOCRINOLOGIST("Reproductive Endocrinologist"),
    
    REPRODUCTIVE_MEDICINE("Reproductive Medicine"),
    
    RHEUMATOLOGIST("Rheumatologist"),
    
    SLEEP_MEDICINE("Sleep Medicine"),
    
    SPEECH_LANGUAGE_PATHOLOGIST("Speech-Language Pathologist"),
    
    SPORTS_MEDICINE_SPECIALIST("Sports Medicine Specialist"),
    
    UROLOGIST("Urologist"),
    
    URGENT_CARE("Urgent Care"),
    
    VASCULAR_SURGEON("Vascular Surgeon");

    private String value;

    SpecialtyEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SpecialtyEnum fromValue(String value) {
      for (SpecialtyEnum b : SpecialtyEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<SpecialtyEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SpecialtyEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SpecialtyEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return SpecialtyEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      SpecialtyEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SPECIALTY = "specialty";
  @SerializedName(SERIALIZED_NAME_SPECIALTY)
  private SpecialtyEnum specialty;

  public static final String SERIALIZED_NAME_SUFFIX = "suffix";
  @SerializedName(SERIALIZED_NAME_SUFFIX)
  private String suffix;

  public Patient1() {
  }

  public Patient1 address(String address) {
    this.address = address;
    return this;
  }

  /**
   * 
   * @return address
   */
  @javax.annotation.Nullable
  public String getAddress() {
    return address;
  }

  public void setAddress(String address) {
    this.address = address;
  }


  public Patient1 email(String email) {
    this.email = email;
    return this;
  }

  /**
   * 
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public Patient1 fax(String fax) {
    this.fax = fax;
    return this;
  }

  /**
   * Should follow format \&quot;xxx-xx-xxxx\&quot;
   * @return fax
   */
  @javax.annotation.Nullable
  public String getFax() {
    return fax;
  }

  public void setFax(String fax) {
    this.fax = fax;
  }


  public Patient1 firstName(String firstName) {
    this.firstName = firstName;
    return this;
  }

  /**
   * 
   * @return firstName
   */
  @javax.annotation.Nullable
  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  public Patient1 lastName(String lastName) {
    this.lastName = lastName;
    return this;
  }

  /**
   * 
   * @return lastName
   */
  @javax.annotation.Nullable
  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }


  public Patient1 middleName(String middleName) {
    this.middleName = middleName;
    return this;
  }

  /**
   * 
   * @return middleName
   */
  @javax.annotation.Nullable
  public String getMiddleName() {
    return middleName;
  }

  public void setMiddleName(String middleName) {
    this.middleName = middleName;
  }


  public Patient1 npi(String npi) {
    this.npi = npi;
    return this;
  }

  /**
   * 
   * @return npi
   */
  @javax.annotation.Nullable
  public String getNpi() {
    return npi;
  }

  public void setNpi(String npi) {
    this.npi = npi;
  }


  public Patient1 phone(String phone) {
    this.phone = phone;
    return this;
  }

  /**
   * Should follow format \&quot;xxx-xx-xxxx\&quot;
   * @return phone
   */
  @javax.annotation.Nullable
  public String getPhone() {
    return phone;
  }

  public void setPhone(String phone) {
    this.phone = phone;
  }


  public Patient1 providerNumber(String providerNumber) {
    this.providerNumber = providerNumber;
    return this;
  }

  /**
   * 
   * @return providerNumber
   */
  @javax.annotation.Nullable
  public String getProviderNumber() {
    return providerNumber;
  }

  public void setProviderNumber(String providerNumber) {
    this.providerNumber = providerNumber;
  }


  public Patient1 providerQualifier(ProviderQualifierEnum providerQualifier) {
    this.providerQualifier = providerQualifier;
    return this;
  }

  /**
   * Can be one of following, &#x60;&#39;&#39;&#x60;, &#x60;&#39;0B&#39;&#x60;(State License #), &#x60;&#39;1G&#39;&#x60;(Provider UPIN #), &#x60;&#39;G2&#39;&#x60;(Provider Commercial #)
   * @return providerQualifier
   */
  @javax.annotation.Nullable
  public ProviderQualifierEnum getProviderQualifier() {
    return providerQualifier;
  }

  public void setProviderQualifier(ProviderQualifierEnum providerQualifier) {
    this.providerQualifier = providerQualifier;
  }


  public Patient1 specialty(SpecialtyEnum specialty) {
    this.specialty = specialty;
    return this;
  }

  /**
   * Can be one of following, &#x60;&#39;&#39;&#x60;, &#x60;&#39;Acupuncture&#39;&#x60;, &#x60;&#39;Advanced Practice Midwife&#39;&#x60;, &#x60;&#39;Aesthetic Medicine&#39;&#x60;, &#x60;&#39;Aesthetician&#39;&#x60;, &#x60;&#39;Allergist/Immunologist&#39;&#x60;, &#x60;&#39;Anesthesiologist&#39;&#x60;, &#x60;&#39;Cardiac Electrophysiologist&#39;&#x60;, &#x60;&#39;Cardiologist&#39;&#x60;, &#x60;&#39;Cardiothoracic Surgeon&#39;&#x60;, &#x60;&#39;Child/Adolescent Psychiatry&#39;&#x60;, &#x60;&#39;Chiropractor&#39;&#x60;, &#x60;&#39;Clinical Social Worker&#39;&#x60;, &#x60;&#39;Colorectal Surgeon&#39;&#x60;, &#x60;&#39;Correactology&#39;&#x60;, &#x60;&#39;Cosmetic Medicine&#39;&#x60;, &#x60;&#39;Counselor Mental Health&#39;&#x60;, &#x60;&#39;Counselor Professional&#39;&#x60;, &#x60;&#39;Counselor&#39;&#x60;, &#x60;&#39;Dentist&#39;&#x60;, &#x60;&#39;Diabetology&#39;&#x60;, &#x60;&#39;Dermatologist&#39;&#x60;, &#x60;&#39;Diagnostic Medical Sonographer&#39;&#x60;, &#x60;&#39;Dietitian, Registered&#39;&#x60;, &#x60;&#39;Ear-Nose-Throat Specialist (ENT)&#39;&#x60;, &#x60;&#39;Emergency Medicine Physician&#39;&#x60;, &#x60;&#39;Endocrinologist&#39;&#x60;, &#x60;&#39;Endodontist&#39;&#x60;, &#x60;&#39;Epidemiologist&#39;&#x60;, &#x60;&#39;Family Practitioner&#39;&#x60;, &#x60;&#39;Gastroenterologist&#39;&#x60;, &#x60;&#39;General Practice&#39;&#x60;, &#x60;&#39;General Surgeon&#39;&#x60;, &#x60;&#39;Geneticist&#39;&#x60;, &#x60;&#39;Geriatrician&#39;&#x60;, &#x60;&#39;Gerontologist&#39;&#x60;, &#x60;&#39;Gynecologist (no OB)&#39;&#x60;, &#x60;&#39;Gynegologic Oncologist&#39;&#x60;, &#x60;&#39;Hand Surgeon&#39;&#x60;, &#x60;&#39;Hematologist&#39;&#x60;, &#x60;&#39;Home Care&#39;&#x60;, &#x60;&#39;Hospice&#39;&#x60;, &#x60;&#39;Hospitalist&#39;&#x60;, &#x60;&#39;Infectious Disease Specialist&#39;&#x60;, &#x60;&#39;Integrative and Functional Medicine&#39;&#x60;, &#x60;&#39;Integrative Medicine&#39;&#x60;, &#x60;&#39;Internist&#39;&#x60;, &#x60;&#39;Interventional Radiology&#39;&#x60;, &#x60;&#39;Laboratory Medicine Specialist&#39;&#x60;, &#x60;&#39;Laser Surgery&#39;&#x60;, &#x60;&#39;Massage Therapist&#39;&#x60;, &#x60;&#39;Naturopathic Physician&#39;&#x60;, &#x60;&#39;Neonatologist&#39;&#x60;, &#x60;&#39;Nephrologist&#39;&#x60;, &#x60;&#39;Neurologist&#39;&#x60;, &#x60;&#39;Neuropsychology&#39;&#x60;, &#x60;&#39;Neurosurgeon&#39;&#x60;, &#x60;&#39;Not Actively Practicing&#39;&#x60;, &#x60;&#39;Nuclear Medicine Specialist&#39;&#x60;, &#x60;&#39;Nurse Practitioner&#39;&#x60;, &#x60;&#39;Nursing&#39;&#x60;, &#x60;&#39;Nutritionist&#39;&#x60;, &#x60;&#39;Obstetrician/Gynecologist&#39;&#x60;, &#x60;&#39;Occupational Medicine&#39;&#x60;, &#x60;&#39;Occupational Therapist&#39;&#x60;, &#x60;&#39;Oncologist&#39;&#x60;, &#x60;&#39;Ophthalmologist&#39;&#x60;, &#x60;&#39;Optometrist&#39;&#x60;, &#x60;&#39;Oral Surgeon&#39;&#x60;, &#x60;&#39;Orofacial Pain&#39;&#x60;, &#x60;&#39;Orthodontist&#39;&#x60;, &#x60;&#39;Orthopedic Surgeon&#39;&#x60;, &#x60;&#39;Orthotist&#39;&#x60;, &#x60;&#39;Other&#39;&#x60;, &#x60;&#39;Pain Management Specialist&#39;&#x60;, &#x60;&#39;Pathologist&#39;&#x60;, &#x60;&#39;Pediatric Dentist&#39;&#x60;, &#x60;&#39;Pediatric Gastroenterology&#39;&#x60;, &#x60;&#39;Pediatric Surgeon&#39;&#x60;, &#x60;&#39;Pediatrician&#39;&#x60;, &#x60;&#39;Perinatologist&#39;&#x60;, &#x60;&#39;Periodontist&#39;&#x60;, &#x60;&#39;Physical Medicine and Rehab Specialist&#39;&#x60;, &#x60;&#39;Physical Therapist&#39;&#x60;, &#x60;&#39;Physician Assistant&#39;&#x60;, &#x60;&#39;Plastic Surgeon&#39;&#x60;, &#x60;&#39;Podiatrist&#39;&#x60;, &#x60;&#39;Preventive-Aging Medicine&#39;&#x60;, &#x60;&#39;Preventive Medicine/Occupational-Environmental Medicine&#39;&#x60;, &#x60;&#39;Primary Care Physician&#39;&#x60;, &#x60;&#39;Prosthetist&#39;&#x60;, &#x60;&#39;Prosthodontist&#39;&#x60;, &#x60;&#39;Psychiatrist&#39;&#x60;, &#x60;&#39;Psychologist&#39;&#x60;, &#x60;&#39;Public Health Professional&#39;&#x60;, &#x60;&#39;Pulmonologist&#39;&#x60;, &#x60;&#39;Radiation Oncologist&#39;&#x60;, &#x60;&#39;Radiologist&#39;&#x60;, &#x60;&#39;Registered Nurse&#39;&#x60;, &#x60;&#39;Religious Nonmedical Practitioner&#39;&#x60;, &#x60;&#39;Reproductive Endocrinologist&#39;&#x60;, &#x60;&#39;Reproductive Medicine&#39;&#x60;, &#x60;&#39;Rheumatologist&#39;&#x60;, &#x60;&#39;Sleep Medicine&#39;&#x60;, &#x60;&#39;Speech-Language Pathologist&#39;&#x60;, &#x60;&#39;Sports Medicine Specialist&#39;&#x60;, &#x60;&#39;Urologist&#39;&#x60;, &#x60;&#39;Urgent Care&#39;&#x60;, &#x60;&#39;Vascular Surgeon&#39;&#x60;
   * @return specialty
   */
  @javax.annotation.Nullable
  public SpecialtyEnum getSpecialty() {
    return specialty;
  }

  public void setSpecialty(SpecialtyEnum specialty) {
    this.specialty = specialty;
  }


  public Patient1 suffix(String suffix) {
    this.suffix = suffix;
    return this;
  }

  /**
   * 
   * @return suffix
   */
  @javax.annotation.Nullable
  public String getSuffix() {
    return suffix;
  }

  public void setSuffix(String suffix) {
    this.suffix = suffix;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Patient1 patient1 = (Patient1) o;
    return Objects.equals(this.address, patient1.address) &&
        Objects.equals(this.email, patient1.email) &&
        Objects.equals(this.fax, patient1.fax) &&
        Objects.equals(this.firstName, patient1.firstName) &&
        Objects.equals(this.lastName, patient1.lastName) &&
        Objects.equals(this.middleName, patient1.middleName) &&
        Objects.equals(this.npi, patient1.npi) &&
        Objects.equals(this.phone, patient1.phone) &&
        Objects.equals(this.providerNumber, patient1.providerNumber) &&
        Objects.equals(this.providerQualifier, patient1.providerQualifier) &&
        Objects.equals(this.specialty, patient1.specialty) &&
        Objects.equals(this.suffix, patient1.suffix);
  }

  @Override
  public int hashCode() {
    return Objects.hash(address, email, fax, firstName, lastName, middleName, npi, phone, providerNumber, providerQualifier, specialty, suffix);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Patient1 {\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    fax: ").append(toIndentedString(fax)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    middleName: ").append(toIndentedString(middleName)).append("\n");
    sb.append("    npi: ").append(toIndentedString(npi)).append("\n");
    sb.append("    phone: ").append(toIndentedString(phone)).append("\n");
    sb.append("    providerNumber: ").append(toIndentedString(providerNumber)).append("\n");
    sb.append("    providerQualifier: ").append(toIndentedString(providerQualifier)).append("\n");
    sb.append("    specialty: ").append(toIndentedString(specialty)).append("\n");
    sb.append("    suffix: ").append(toIndentedString(suffix)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("address");
    openapiFields.add("email");
    openapiFields.add("fax");
    openapiFields.add("first_name");
    openapiFields.add("last_name");
    openapiFields.add("middle_name");
    openapiFields.add("npi");
    openapiFields.add("phone");
    openapiFields.add("provider_number");
    openapiFields.add("provider_qualifier");
    openapiFields.add("specialty");
    openapiFields.add("suffix");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Patient1
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Patient1.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Patient1 is not found in the empty JSON string", Patient1.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Patient1.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Patient1` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull()) && !jsonObj.get("address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address").toString()));
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if ((jsonObj.get("fax") != null && !jsonObj.get("fax").isJsonNull()) && !jsonObj.get("fax").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fax` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fax").toString()));
      }
      if ((jsonObj.get("first_name") != null && !jsonObj.get("first_name").isJsonNull()) && !jsonObj.get("first_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_name").toString()));
      }
      if ((jsonObj.get("last_name") != null && !jsonObj.get("last_name").isJsonNull()) && !jsonObj.get("last_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `last_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("last_name").toString()));
      }
      if ((jsonObj.get("middle_name") != null && !jsonObj.get("middle_name").isJsonNull()) && !jsonObj.get("middle_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `middle_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("middle_name").toString()));
      }
      if ((jsonObj.get("npi") != null && !jsonObj.get("npi").isJsonNull()) && !jsonObj.get("npi").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `npi` to be a primitive type in the JSON string but got `%s`", jsonObj.get("npi").toString()));
      }
      if ((jsonObj.get("phone") != null && !jsonObj.get("phone").isJsonNull()) && !jsonObj.get("phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phone").toString()));
      }
      if ((jsonObj.get("provider_number") != null && !jsonObj.get("provider_number").isJsonNull()) && !jsonObj.get("provider_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `provider_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("provider_number").toString()));
      }
      if ((jsonObj.get("provider_qualifier") != null && !jsonObj.get("provider_qualifier").isJsonNull()) && !jsonObj.get("provider_qualifier").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `provider_qualifier` to be a primitive type in the JSON string but got `%s`", jsonObj.get("provider_qualifier").toString()));
      }
      // validate the optional field `provider_qualifier`
      if (jsonObj.get("provider_qualifier") != null && !jsonObj.get("provider_qualifier").isJsonNull()) {
        ProviderQualifierEnum.validateJsonElement(jsonObj.get("provider_qualifier"));
      }
      if ((jsonObj.get("specialty") != null && !jsonObj.get("specialty").isJsonNull()) && !jsonObj.get("specialty").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `specialty` to be a primitive type in the JSON string but got `%s`", jsonObj.get("specialty").toString()));
      }
      // validate the optional field `specialty`
      if (jsonObj.get("specialty") != null && !jsonObj.get("specialty").isJsonNull()) {
        SpecialtyEnum.validateJsonElement(jsonObj.get("specialty"));
      }
      if ((jsonObj.get("suffix") != null && !jsonObj.get("suffix").isJsonNull()) && !jsonObj.get("suffix").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `suffix` to be a primitive type in the JSON string but got `%s`", jsonObj.get("suffix").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Patient1.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Patient1' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Patient1> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Patient1.class));

       return (TypeAdapter<T>) new TypeAdapter<Patient1>() {
           @Override
           public void write(JsonWriter out, Patient1 value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Patient1 read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Patient1 given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Patient1
   * @throws IOException if the JSON string is invalid with respect to Patient1
   */
  public static Patient1 fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Patient1.class);
  }

  /**
   * Convert an instance of Patient1 to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

