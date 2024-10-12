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
public class WorkerCompInsurance {
  public static final String SERIALIZED_NAME_PROPERTY_AND_CASUALTY_AGENCY_CLAIM_NUMBER = "property_and_casualty_agency_claim_number";
  @SerializedName(SERIALIZED_NAME_PROPERTY_AND_CASUALTY_AGENCY_CLAIM_NUMBER)
  private String propertyAndCasualtyAgencyClaimNumber;

  public static final String SERIALIZED_NAME_WORKERS_COMP_CARRIER_CODE = "workers_comp_carrier_code";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_CARRIER_CODE)
  private String workersCompCarrierCode;

  public static final String SERIALIZED_NAME_WORKERS_COMP_CASE_NUMBER = "workers_comp_case_number";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_CASE_NUMBER)
  private String workersCompCaseNumber;

  public static final String SERIALIZED_NAME_WORKERS_COMP_COMPANY = "workers_comp_company";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_COMPANY)
  private String workersCompCompany;

  public static final String SERIALIZED_NAME_WORKERS_COMP_DATE_OF_ACCIDENT = "workers_comp_date_of_accident";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_DATE_OF_ACCIDENT)
  private String workersCompDateOfAccident;

  public static final String SERIALIZED_NAME_WORKERS_COMP_GROUP_NAME = "workers_comp_group_name";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_GROUP_NAME)
  private String workersCompGroupName;

  public static final String SERIALIZED_NAME_WORKERS_COMP_GROUP_NUMBER = "workers_comp_group_number";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_GROUP_NUMBER)
  private String workersCompGroupNumber;

  public static final String SERIALIZED_NAME_WORKERS_COMP_NOTES = "workers_comp_notes";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_NOTES)
  private String workersCompNotes;

  public static final String SERIALIZED_NAME_WORKERS_COMP_PAYER_ADDRESS = "workers_comp_payer_address";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_PAYER_ADDRESS)
  private String workersCompPayerAddress;

  public static final String SERIALIZED_NAME_WORKERS_COMP_PAYER_CITY = "workers_comp_payer_city";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_PAYER_CITY)
  private String workersCompPayerCity;

  public static final String SERIALIZED_NAME_WORKERS_COMP_PAYER_ID = "workers_comp_payer_id";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_PAYER_ID)
  private String workersCompPayerId;

  /**
   * 
   */
  @JsonAdapter(WorkersCompPayerStateEnum.Adapter.class)
  public enum WorkersCompPayerStateEnum {
    AL("AL"),
    
    AK("AK"),
    
    AS("AS"),
    
    AZ("AZ"),
    
    AR("AR"),
    
    AA("AA"),
    
    AE("AE"),
    
    AP("AP"),
    
    CA("CA"),
    
    CO("CO"),
    
    CT("CT"),
    
    DE("DE"),
    
    DC("DC"),
    
    FL("FL"),
    
    GA("GA"),
    
    GU("GU"),
    
    HI("HI"),
    
    ID("ID"),
    
    IL("IL"),
    
    IN("IN"),
    
    IA("IA"),
    
    KS("KS"),
    
    KY("KY"),
    
    LA("LA"),
    
    ME("ME"),
    
    MD("MD"),
    
    MA("MA"),
    
    MI("MI"),
    
    MN("MN"),
    
    MS("MS"),
    
    MO("MO"),
    
    MT("MT"),
    
    NE("NE"),
    
    NV("NV"),
    
    NH("NH"),
    
    NJ("NJ"),
    
    NM("NM"),
    
    NY("NY"),
    
    NC("NC"),
    
    ND("ND"),
    
    MP("MP"),
    
    OH("OH"),
    
    OK("OK"),
    
    OR("OR"),
    
    PA("PA"),
    
    PR("PR"),
    
    RI("RI"),
    
    SC("SC"),
    
    SD("SD"),
    
    TN("TN"),
    
    TX("TX"),
    
    UT("UT"),
    
    VT("VT"),
    
    VI("VI"),
    
    VA("VA"),
    
    WA("WA"),
    
    WV("WV"),
    
    WI("WI"),
    
    WY("WY");

    private String value;

    WorkersCompPayerStateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static WorkersCompPayerStateEnum fromValue(String value) {
      for (WorkersCompPayerStateEnum b : WorkersCompPayerStateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<WorkersCompPayerStateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final WorkersCompPayerStateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public WorkersCompPayerStateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return WorkersCompPayerStateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      WorkersCompPayerStateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_WORKERS_COMP_PAYER_STATE = "workers_comp_payer_state";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_PAYER_STATE)
  private WorkersCompPayerStateEnum workersCompPayerState;

  public static final String SERIALIZED_NAME_WORKERS_COMP_PAYER_ZIP = "workers_comp_payer_zip";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_PAYER_ZIP)
  private String workersCompPayerZip;

  /**
   * 
   */
  @JsonAdapter(WorkersCompStateOfOccurrenceEnum.Adapter.class)
  public enum WorkersCompStateOfOccurrenceEnum {
    AL("AL"),
    
    AK("AK"),
    
    AS("AS"),
    
    AZ("AZ"),
    
    AR("AR"),
    
    AA("AA"),
    
    AE("AE"),
    
    AP("AP"),
    
    CA("CA"),
    
    CO("CO"),
    
    CT("CT"),
    
    DE("DE"),
    
    DC("DC"),
    
    FL("FL"),
    
    GA("GA"),
    
    GU("GU"),
    
    HI("HI"),
    
    ID("ID"),
    
    IL("IL"),
    
    IN("IN"),
    
    IA("IA"),
    
    KS("KS"),
    
    KY("KY"),
    
    LA("LA"),
    
    ME("ME"),
    
    MD("MD"),
    
    MA("MA"),
    
    MI("MI"),
    
    MN("MN"),
    
    MS("MS"),
    
    MO("MO"),
    
    MT("MT"),
    
    NE("NE"),
    
    NV("NV"),
    
    NH("NH"),
    
    NJ("NJ"),
    
    NM("NM"),
    
    NY("NY"),
    
    NC("NC"),
    
    ND("ND"),
    
    MP("MP"),
    
    OH("OH"),
    
    OK("OK"),
    
    OR("OR"),
    
    PA("PA"),
    
    PR("PR"),
    
    RI("RI"),
    
    SC("SC"),
    
    SD("SD"),
    
    TN("TN"),
    
    TX("TX"),
    
    UT("UT"),
    
    VT("VT"),
    
    VI("VI"),
    
    VA("VA"),
    
    WA("WA"),
    
    WV("WV"),
    
    WI("WI"),
    
    WY("WY");

    private String value;

    WorkersCompStateOfOccurrenceEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static WorkersCompStateOfOccurrenceEnum fromValue(String value) {
      for (WorkersCompStateOfOccurrenceEnum b : WorkersCompStateOfOccurrenceEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<WorkersCompStateOfOccurrenceEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final WorkersCompStateOfOccurrenceEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public WorkersCompStateOfOccurrenceEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return WorkersCompStateOfOccurrenceEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      WorkersCompStateOfOccurrenceEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_WORKERS_COMP_STATE_OF_OCCURRENCE = "workers_comp_state_of_occurrence";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_STATE_OF_OCCURRENCE)
  private WorkersCompStateOfOccurrenceEnum workersCompStateOfOccurrence;

  public static final String SERIALIZED_NAME_WORKERS_COMP_WCB = "workers_comp_wcb";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_WCB)
  private String workersCompWcb;

  public static final String SERIALIZED_NAME_WORKERS_COMP_WCB_RATING_CODE = "workers_comp_wcb_rating_code";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_WCB_RATING_CODE)
  private String workersCompWcbRatingCode;

  public WorkerCompInsurance() {
  }

  public WorkerCompInsurance propertyAndCasualtyAgencyClaimNumber(String propertyAndCasualtyAgencyClaimNumber) {
    this.propertyAndCasualtyAgencyClaimNumber = propertyAndCasualtyAgencyClaimNumber;
    return this;
  }

  /**
   * 
   * @return propertyAndCasualtyAgencyClaimNumber
   */
  @javax.annotation.Nullable
  public String getPropertyAndCasualtyAgencyClaimNumber() {
    return propertyAndCasualtyAgencyClaimNumber;
  }

  public void setPropertyAndCasualtyAgencyClaimNumber(String propertyAndCasualtyAgencyClaimNumber) {
    this.propertyAndCasualtyAgencyClaimNumber = propertyAndCasualtyAgencyClaimNumber;
  }


  public WorkerCompInsurance workersCompCarrierCode(String workersCompCarrierCode) {
    this.workersCompCarrierCode = workersCompCarrierCode;
    return this;
  }

  /**
   * 
   * @return workersCompCarrierCode
   */
  @javax.annotation.Nullable
  public String getWorkersCompCarrierCode() {
    return workersCompCarrierCode;
  }

  public void setWorkersCompCarrierCode(String workersCompCarrierCode) {
    this.workersCompCarrierCode = workersCompCarrierCode;
  }


  public WorkerCompInsurance workersCompCaseNumber(String workersCompCaseNumber) {
    this.workersCompCaseNumber = workersCompCaseNumber;
    return this;
  }

  /**
   * 
   * @return workersCompCaseNumber
   */
  @javax.annotation.Nullable
  public String getWorkersCompCaseNumber() {
    return workersCompCaseNumber;
  }

  public void setWorkersCompCaseNumber(String workersCompCaseNumber) {
    this.workersCompCaseNumber = workersCompCaseNumber;
  }


  public WorkerCompInsurance workersCompCompany(String workersCompCompany) {
    this.workersCompCompany = workersCompCompany;
    return this;
  }

  /**
   * 
   * @return workersCompCompany
   */
  @javax.annotation.Nullable
  public String getWorkersCompCompany() {
    return workersCompCompany;
  }

  public void setWorkersCompCompany(String workersCompCompany) {
    this.workersCompCompany = workersCompCompany;
  }


  public WorkerCompInsurance workersCompDateOfAccident(String workersCompDateOfAccident) {
    this.workersCompDateOfAccident = workersCompDateOfAccident;
    return this;
  }

  /**
   * 
   * @return workersCompDateOfAccident
   */
  @javax.annotation.Nullable
  public String getWorkersCompDateOfAccident() {
    return workersCompDateOfAccident;
  }

  public void setWorkersCompDateOfAccident(String workersCompDateOfAccident) {
    this.workersCompDateOfAccident = workersCompDateOfAccident;
  }


  public WorkerCompInsurance workersCompGroupName(String workersCompGroupName) {
    this.workersCompGroupName = workersCompGroupName;
    return this;
  }

  /**
   * 
   * @return workersCompGroupName
   */
  @javax.annotation.Nullable
  public String getWorkersCompGroupName() {
    return workersCompGroupName;
  }

  public void setWorkersCompGroupName(String workersCompGroupName) {
    this.workersCompGroupName = workersCompGroupName;
  }


  public WorkerCompInsurance workersCompGroupNumber(String workersCompGroupNumber) {
    this.workersCompGroupNumber = workersCompGroupNumber;
    return this;
  }

  /**
   * 
   * @return workersCompGroupNumber
   */
  @javax.annotation.Nullable
  public String getWorkersCompGroupNumber() {
    return workersCompGroupNumber;
  }

  public void setWorkersCompGroupNumber(String workersCompGroupNumber) {
    this.workersCompGroupNumber = workersCompGroupNumber;
  }


  public WorkerCompInsurance workersCompNotes(String workersCompNotes) {
    this.workersCompNotes = workersCompNotes;
    return this;
  }

  /**
   * 
   * @return workersCompNotes
   */
  @javax.annotation.Nullable
  public String getWorkersCompNotes() {
    return workersCompNotes;
  }

  public void setWorkersCompNotes(String workersCompNotes) {
    this.workersCompNotes = workersCompNotes;
  }


  public WorkerCompInsurance workersCompPayerAddress(String workersCompPayerAddress) {
    this.workersCompPayerAddress = workersCompPayerAddress;
    return this;
  }

  /**
   * 
   * @return workersCompPayerAddress
   */
  @javax.annotation.Nullable
  public String getWorkersCompPayerAddress() {
    return workersCompPayerAddress;
  }

  public void setWorkersCompPayerAddress(String workersCompPayerAddress) {
    this.workersCompPayerAddress = workersCompPayerAddress;
  }


  public WorkerCompInsurance workersCompPayerCity(String workersCompPayerCity) {
    this.workersCompPayerCity = workersCompPayerCity;
    return this;
  }

  /**
   * 
   * @return workersCompPayerCity
   */
  @javax.annotation.Nullable
  public String getWorkersCompPayerCity() {
    return workersCompPayerCity;
  }

  public void setWorkersCompPayerCity(String workersCompPayerCity) {
    this.workersCompPayerCity = workersCompPayerCity;
  }


  public WorkerCompInsurance workersCompPayerId(String workersCompPayerId) {
    this.workersCompPayerId = workersCompPayerId;
    return this;
  }

  /**
   * 
   * @return workersCompPayerId
   */
  @javax.annotation.Nullable
  public String getWorkersCompPayerId() {
    return workersCompPayerId;
  }

  public void setWorkersCompPayerId(String workersCompPayerId) {
    this.workersCompPayerId = workersCompPayerId;
  }


  public WorkerCompInsurance workersCompPayerState(WorkersCompPayerStateEnum workersCompPayerState) {
    this.workersCompPayerState = workersCompPayerState;
    return this;
  }

  /**
   * 
   * @return workersCompPayerState
   */
  @javax.annotation.Nullable
  public WorkersCompPayerStateEnum getWorkersCompPayerState() {
    return workersCompPayerState;
  }

  public void setWorkersCompPayerState(WorkersCompPayerStateEnum workersCompPayerState) {
    this.workersCompPayerState = workersCompPayerState;
  }


  public WorkerCompInsurance workersCompPayerZip(String workersCompPayerZip) {
    this.workersCompPayerZip = workersCompPayerZip;
    return this;
  }

  /**
   * 
   * @return workersCompPayerZip
   */
  @javax.annotation.Nullable
  public String getWorkersCompPayerZip() {
    return workersCompPayerZip;
  }

  public void setWorkersCompPayerZip(String workersCompPayerZip) {
    this.workersCompPayerZip = workersCompPayerZip;
  }


  public WorkerCompInsurance workersCompStateOfOccurrence(WorkersCompStateOfOccurrenceEnum workersCompStateOfOccurrence) {
    this.workersCompStateOfOccurrence = workersCompStateOfOccurrence;
    return this;
  }

  /**
   * 
   * @return workersCompStateOfOccurrence
   */
  @javax.annotation.Nullable
  public WorkersCompStateOfOccurrenceEnum getWorkersCompStateOfOccurrence() {
    return workersCompStateOfOccurrence;
  }

  public void setWorkersCompStateOfOccurrence(WorkersCompStateOfOccurrenceEnum workersCompStateOfOccurrence) {
    this.workersCompStateOfOccurrence = workersCompStateOfOccurrence;
  }


  public WorkerCompInsurance workersCompWcb(String workersCompWcb) {
    this.workersCompWcb = workersCompWcb;
    return this;
  }

  /**
   * 
   * @return workersCompWcb
   */
  @javax.annotation.Nullable
  public String getWorkersCompWcb() {
    return workersCompWcb;
  }

  public void setWorkersCompWcb(String workersCompWcb) {
    this.workersCompWcb = workersCompWcb;
  }


  public WorkerCompInsurance workersCompWcbRatingCode(String workersCompWcbRatingCode) {
    this.workersCompWcbRatingCode = workersCompWcbRatingCode;
    return this;
  }

  /**
   * 
   * @return workersCompWcbRatingCode
   */
  @javax.annotation.Nullable
  public String getWorkersCompWcbRatingCode() {
    return workersCompWcbRatingCode;
  }

  public void setWorkersCompWcbRatingCode(String workersCompWcbRatingCode) {
    this.workersCompWcbRatingCode = workersCompWcbRatingCode;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    WorkerCompInsurance workerCompInsurance = (WorkerCompInsurance) o;
    return Objects.equals(this.propertyAndCasualtyAgencyClaimNumber, workerCompInsurance.propertyAndCasualtyAgencyClaimNumber) &&
        Objects.equals(this.workersCompCarrierCode, workerCompInsurance.workersCompCarrierCode) &&
        Objects.equals(this.workersCompCaseNumber, workerCompInsurance.workersCompCaseNumber) &&
        Objects.equals(this.workersCompCompany, workerCompInsurance.workersCompCompany) &&
        Objects.equals(this.workersCompDateOfAccident, workerCompInsurance.workersCompDateOfAccident) &&
        Objects.equals(this.workersCompGroupName, workerCompInsurance.workersCompGroupName) &&
        Objects.equals(this.workersCompGroupNumber, workerCompInsurance.workersCompGroupNumber) &&
        Objects.equals(this.workersCompNotes, workerCompInsurance.workersCompNotes) &&
        Objects.equals(this.workersCompPayerAddress, workerCompInsurance.workersCompPayerAddress) &&
        Objects.equals(this.workersCompPayerCity, workerCompInsurance.workersCompPayerCity) &&
        Objects.equals(this.workersCompPayerId, workerCompInsurance.workersCompPayerId) &&
        Objects.equals(this.workersCompPayerState, workerCompInsurance.workersCompPayerState) &&
        Objects.equals(this.workersCompPayerZip, workerCompInsurance.workersCompPayerZip) &&
        Objects.equals(this.workersCompStateOfOccurrence, workerCompInsurance.workersCompStateOfOccurrence) &&
        Objects.equals(this.workersCompWcb, workerCompInsurance.workersCompWcb) &&
        Objects.equals(this.workersCompWcbRatingCode, workerCompInsurance.workersCompWcbRatingCode);
  }

  @Override
  public int hashCode() {
    return Objects.hash(propertyAndCasualtyAgencyClaimNumber, workersCompCarrierCode, workersCompCaseNumber, workersCompCompany, workersCompDateOfAccident, workersCompGroupName, workersCompGroupNumber, workersCompNotes, workersCompPayerAddress, workersCompPayerCity, workersCompPayerId, workersCompPayerState, workersCompPayerZip, workersCompStateOfOccurrence, workersCompWcb, workersCompWcbRatingCode);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class WorkerCompInsurance {\n");
    sb.append("    propertyAndCasualtyAgencyClaimNumber: ").append(toIndentedString(propertyAndCasualtyAgencyClaimNumber)).append("\n");
    sb.append("    workersCompCarrierCode: ").append(toIndentedString(workersCompCarrierCode)).append("\n");
    sb.append("    workersCompCaseNumber: ").append(toIndentedString(workersCompCaseNumber)).append("\n");
    sb.append("    workersCompCompany: ").append(toIndentedString(workersCompCompany)).append("\n");
    sb.append("    workersCompDateOfAccident: ").append(toIndentedString(workersCompDateOfAccident)).append("\n");
    sb.append("    workersCompGroupName: ").append(toIndentedString(workersCompGroupName)).append("\n");
    sb.append("    workersCompGroupNumber: ").append(toIndentedString(workersCompGroupNumber)).append("\n");
    sb.append("    workersCompNotes: ").append(toIndentedString(workersCompNotes)).append("\n");
    sb.append("    workersCompPayerAddress: ").append(toIndentedString(workersCompPayerAddress)).append("\n");
    sb.append("    workersCompPayerCity: ").append(toIndentedString(workersCompPayerCity)).append("\n");
    sb.append("    workersCompPayerId: ").append(toIndentedString(workersCompPayerId)).append("\n");
    sb.append("    workersCompPayerState: ").append(toIndentedString(workersCompPayerState)).append("\n");
    sb.append("    workersCompPayerZip: ").append(toIndentedString(workersCompPayerZip)).append("\n");
    sb.append("    workersCompStateOfOccurrence: ").append(toIndentedString(workersCompStateOfOccurrence)).append("\n");
    sb.append("    workersCompWcb: ").append(toIndentedString(workersCompWcb)).append("\n");
    sb.append("    workersCompWcbRatingCode: ").append(toIndentedString(workersCompWcbRatingCode)).append("\n");
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
    openapiFields.add("property_and_casualty_agency_claim_number");
    openapiFields.add("workers_comp_carrier_code");
    openapiFields.add("workers_comp_case_number");
    openapiFields.add("workers_comp_company");
    openapiFields.add("workers_comp_date_of_accident");
    openapiFields.add("workers_comp_group_name");
    openapiFields.add("workers_comp_group_number");
    openapiFields.add("workers_comp_notes");
    openapiFields.add("workers_comp_payer_address");
    openapiFields.add("workers_comp_payer_city");
    openapiFields.add("workers_comp_payer_id");
    openapiFields.add("workers_comp_payer_state");
    openapiFields.add("workers_comp_payer_zip");
    openapiFields.add("workers_comp_state_of_occurrence");
    openapiFields.add("workers_comp_wcb");
    openapiFields.add("workers_comp_wcb_rating_code");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to WorkerCompInsurance
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!WorkerCompInsurance.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in WorkerCompInsurance is not found in the empty JSON string", WorkerCompInsurance.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!WorkerCompInsurance.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `WorkerCompInsurance` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("property_and_casualty_agency_claim_number") != null && !jsonObj.get("property_and_casualty_agency_claim_number").isJsonNull()) && !jsonObj.get("property_and_casualty_agency_claim_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `property_and_casualty_agency_claim_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("property_and_casualty_agency_claim_number").toString()));
      }
      if ((jsonObj.get("workers_comp_carrier_code") != null && !jsonObj.get("workers_comp_carrier_code").isJsonNull()) && !jsonObj.get("workers_comp_carrier_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_carrier_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_carrier_code").toString()));
      }
      if ((jsonObj.get("workers_comp_case_number") != null && !jsonObj.get("workers_comp_case_number").isJsonNull()) && !jsonObj.get("workers_comp_case_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_case_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_case_number").toString()));
      }
      if ((jsonObj.get("workers_comp_company") != null && !jsonObj.get("workers_comp_company").isJsonNull()) && !jsonObj.get("workers_comp_company").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_company` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_company").toString()));
      }
      if ((jsonObj.get("workers_comp_date_of_accident") != null && !jsonObj.get("workers_comp_date_of_accident").isJsonNull()) && !jsonObj.get("workers_comp_date_of_accident").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_date_of_accident` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_date_of_accident").toString()));
      }
      if ((jsonObj.get("workers_comp_group_name") != null && !jsonObj.get("workers_comp_group_name").isJsonNull()) && !jsonObj.get("workers_comp_group_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_group_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_group_name").toString()));
      }
      if ((jsonObj.get("workers_comp_group_number") != null && !jsonObj.get("workers_comp_group_number").isJsonNull()) && !jsonObj.get("workers_comp_group_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_group_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_group_number").toString()));
      }
      if ((jsonObj.get("workers_comp_notes") != null && !jsonObj.get("workers_comp_notes").isJsonNull()) && !jsonObj.get("workers_comp_notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_notes").toString()));
      }
      if ((jsonObj.get("workers_comp_payer_address") != null && !jsonObj.get("workers_comp_payer_address").isJsonNull()) && !jsonObj.get("workers_comp_payer_address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_payer_address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_payer_address").toString()));
      }
      if ((jsonObj.get("workers_comp_payer_city") != null && !jsonObj.get("workers_comp_payer_city").isJsonNull()) && !jsonObj.get("workers_comp_payer_city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_payer_city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_payer_city").toString()));
      }
      if ((jsonObj.get("workers_comp_payer_id") != null && !jsonObj.get("workers_comp_payer_id").isJsonNull()) && !jsonObj.get("workers_comp_payer_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_payer_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_payer_id").toString()));
      }
      if ((jsonObj.get("workers_comp_payer_state") != null && !jsonObj.get("workers_comp_payer_state").isJsonNull()) && !jsonObj.get("workers_comp_payer_state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_payer_state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_payer_state").toString()));
      }
      // validate the optional field `workers_comp_payer_state`
      if (jsonObj.get("workers_comp_payer_state") != null && !jsonObj.get("workers_comp_payer_state").isJsonNull()) {
        WorkersCompPayerStateEnum.validateJsonElement(jsonObj.get("workers_comp_payer_state"));
      }
      if ((jsonObj.get("workers_comp_payer_zip") != null && !jsonObj.get("workers_comp_payer_zip").isJsonNull()) && !jsonObj.get("workers_comp_payer_zip").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_payer_zip` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_payer_zip").toString()));
      }
      if ((jsonObj.get("workers_comp_state_of_occurrence") != null && !jsonObj.get("workers_comp_state_of_occurrence").isJsonNull()) && !jsonObj.get("workers_comp_state_of_occurrence").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_state_of_occurrence` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_state_of_occurrence").toString()));
      }
      // validate the optional field `workers_comp_state_of_occurrence`
      if (jsonObj.get("workers_comp_state_of_occurrence") != null && !jsonObj.get("workers_comp_state_of_occurrence").isJsonNull()) {
        WorkersCompStateOfOccurrenceEnum.validateJsonElement(jsonObj.get("workers_comp_state_of_occurrence"));
      }
      if ((jsonObj.get("workers_comp_wcb") != null && !jsonObj.get("workers_comp_wcb").isJsonNull()) && !jsonObj.get("workers_comp_wcb").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_wcb` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_wcb").toString()));
      }
      if ((jsonObj.get("workers_comp_wcb_rating_code") != null && !jsonObj.get("workers_comp_wcb_rating_code").isJsonNull()) && !jsonObj.get("workers_comp_wcb_rating_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workers_comp_wcb_rating_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workers_comp_wcb_rating_code").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!WorkerCompInsurance.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'WorkerCompInsurance' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<WorkerCompInsurance> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(WorkerCompInsurance.class));

       return (TypeAdapter<T>) new TypeAdapter<WorkerCompInsurance>() {
           @Override
           public void write(JsonWriter out, WorkerCompInsurance value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public WorkerCompInsurance read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of WorkerCompInsurance given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of WorkerCompInsurance
   * @throws IOException if the JSON string is invalid with respect to WorkerCompInsurance
   */
  public static WorkerCompInsurance fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, WorkerCompInsurance.class);
  }

  /**
   * Convert an instance of WorkerCompInsurance to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

