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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
 * BillingLineItem
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BillingLineItem {
  public static final String SERIALIZED_NAME_ADJUSTMENT = "adjustment";
  @SerializedName(SERIALIZED_NAME_ADJUSTMENT)
  private BigDecimal adjustment;

  public static final String SERIALIZED_NAME_ALLOWED = "allowed";
  @SerializedName(SERIALIZED_NAME_ALLOWED)
  private BigDecimal allowed;

  public static final String SERIALIZED_NAME_APPOINTMENT = "appointment";
  @SerializedName(SERIALIZED_NAME_APPOINTMENT)
  private Integer appointment;

  public static final String SERIALIZED_NAME_BALANCE_INS = "balance_ins";
  @SerializedName(SERIALIZED_NAME_BALANCE_INS)
  private BigDecimal balanceIns;

  public static final String SERIALIZED_NAME_BALANCE_PT = "balance_pt";
  @SerializedName(SERIALIZED_NAME_BALANCE_PT)
  private BigDecimal balancePt;

  public static final String SERIALIZED_NAME_BALANCE_TOTAL = "balance_total";
  @SerializedName(SERIALIZED_NAME_BALANCE_TOTAL)
  private String balanceTotal;

  public static final String SERIALIZED_NAME_BILLED = "billed";
  @SerializedName(SERIALIZED_NAME_BILLED)
  private BigDecimal billed;

  /**
   * One of &#x60;\&quot;\&quot;&#x60;, &#x60;\&quot;Incomplete Information\&quot;&#x60;, &#x60;\&quot;In Process Emdeon\&quot;&#x60;, &#x60;\&quot;In Process iHCFA\&quot;&#x60;, &#x60;\&quot;In Process Gateway\&quot;&#x60;, &#x60;\&quot;Rejected Emdeon\&quot;&#x60;, &#x60;\&quot;Rejected iHCFA\&quot;&#x60;, &#x60;\&quot;Rejected Gateway\&quot;&#x60;, &#x60;\&quot;In Process Payer\&quot;&#x60;, &#x60;\&quot;Payer Acknowledged\&quot;&#x60;, &#x60;\&quot;Rejected Payer\&quot;&#x60;, &#x60;\&quot;Paid in Full\&quot;&#x60;,  &#x60;\&quot;Partially Paid\&quot;&#x60;,  &#x60;\&quot;Coordination of Benefits\&quot;&#x60;,  &#x60;\&quot;ERA Received\&quot;&#x60;,  &#x60;\&quot;ERA Denied\&quot;&#x60;
   */
  @JsonAdapter(BillingStatusEnum.Adapter.class)
  public enum BillingStatusEnum {
    EMPTY(""),
    
    INCOMPLETE_INFORMATION("Incomplete Information"),
    
    IN_PROCESS_EMDEON("In Process Emdeon"),
    
    IN_PROCESS_I_HCFA("In Process iHCFA"),
    
    IN_PROCESS_GATEWAY("In Process Gateway"),
    
    IN_PROCESS_JOPARI("In Process Jopari"),
    
    IN_PROCESS_WAYSTAR("In Process Waystar"),
    
    REJECTED_EMDEON("Rejected Emdeon"),
    
    REJECTED_I_HCFA("Rejected iHCFA"),
    
    REJECTED_GATEWAY("Rejected Gateway"),
    
    REJECTED_JOPARI("Rejected Jopari"),
    
    REJECTED_WAYSTAR("Rejected Waystar"),
    
    IN_PROCESS_PAYER("In Process Payer"),
    
    PAYER_ACKNOWLEDGED("Payer Acknowledged"),
    
    REJECTED_PAYER("Rejected Payer"),
    
    PAID_IN_FULL("Paid in Full"),
    
    PARTIALLY_PAID("Partially Paid"),
    
    COORDINATION_OF_BENEFITS("Coordination of Benefits"),
    
    ERA_RECEIVED("ERA Received"),
    
    ERA_DENIED("ERA Denied");

    private String value;

    BillingStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static BillingStatusEnum fromValue(String value) {
      for (BillingStatusEnum b : BillingStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<BillingStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final BillingStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public BillingStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return BillingStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      BillingStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_BILLING_STATUS = "billing_status";
  @SerializedName(SERIALIZED_NAME_BILLING_STATUS)
  private BillingStatusEnum billingStatus;

  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_DENIED_FLAG = "denied_flag";
  @SerializedName(SERIALIZED_NAME_DENIED_FLAG)
  private Boolean deniedFlag;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DIAGNOSIS_POINTERS = "diagnosis_pointers";
  @SerializedName(SERIALIZED_NAME_DIAGNOSIS_POINTERS)
  private List<String> diagnosisPointers = new ArrayList<>();

  public static final String SERIALIZED_NAME_DOCTOR = "doctor";
  @SerializedName(SERIALIZED_NAME_DOCTOR)
  private String doctor;

  public static final String SERIALIZED_NAME_EXPECTED_REIMBURSEMENT = "expected_reimbursement";
  @SerializedName(SERIALIZED_NAME_EXPECTED_REIMBURSEMENT)
  private BigDecimal expectedReimbursement;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_INS1_PAID = "ins1_paid";
  @SerializedName(SERIALIZED_NAME_INS1_PAID)
  private BigDecimal ins1Paid;

  public static final String SERIALIZED_NAME_INS2_PAID = "ins2_paid";
  @SerializedName(SERIALIZED_NAME_INS2_PAID)
  private BigDecimal ins2Paid;

  public static final String SERIALIZED_NAME_INS3_PAID = "ins3_paid";
  @SerializedName(SERIALIZED_NAME_INS3_PAID)
  private BigDecimal ins3Paid;

  public static final String SERIALIZED_NAME_INS_TOTAL = "ins_total";
  @SerializedName(SERIALIZED_NAME_INS_TOTAL)
  private String insTotal;

  public static final String SERIALIZED_NAME_INSURANCE_STATUS = "insurance_status";
  @SerializedName(SERIALIZED_NAME_INSURANCE_STATUS)
  private String insuranceStatus;

  public static final String SERIALIZED_NAME_MODIFIERS = "modifiers";
  @SerializedName(SERIALIZED_NAME_MODIFIERS)
  private List<String> modifiers = new ArrayList<>();

  public static final String SERIALIZED_NAME_PAID_TOTAL = "paid_total";
  @SerializedName(SERIALIZED_NAME_PAID_TOTAL)
  private String paidTotal;

  public static final String SERIALIZED_NAME_PATIENT = "patient";
  @SerializedName(SERIALIZED_NAME_PATIENT)
  private String patient;

  public static final String SERIALIZED_NAME_POSTED_DATE = "posted_date";
  @SerializedName(SERIALIZED_NAME_POSTED_DATE)
  private String postedDate;

  public static final String SERIALIZED_NAME_PRICE = "price";
  @SerializedName(SERIALIZED_NAME_PRICE)
  private BigDecimal price;

  /**
   * One of &#x60;\&quot;CPT(C)\&quot;&#x60;, &#x60;\&quot;HCPCS(H)\&quot;&#x60;, &#x60;\&quot;Custom(U)\&quot;&#x60;, use 1 character identifier when using &#x60;POST&#x60;
   */
  @JsonAdapter(ProcedureTypeEnum.Adapter.class)
  public enum ProcedureTypeEnum {
    C("C"),
    
    H("H"),
    
    U("U"),
    
    S("S");

    private String value;

    ProcedureTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ProcedureTypeEnum fromValue(String value) {
      for (ProcedureTypeEnum b : ProcedureTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ProcedureTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ProcedureTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ProcedureTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ProcedureTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ProcedureTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PROCEDURE_TYPE = "procedure_type";
  @SerializedName(SERIALIZED_NAME_PROCEDURE_TYPE)
  private ProcedureTypeEnum procedureType;

  public static final String SERIALIZED_NAME_PT_PAID = "pt_paid";
  @SerializedName(SERIALIZED_NAME_PT_PAID)
  private BigDecimal ptPaid;

  public static final String SERIALIZED_NAME_QUANTITY = "quantity";
  @SerializedName(SERIALIZED_NAME_QUANTITY)
  private BigDecimal quantity;

  public static final String SERIALIZED_NAME_SERVICE_DATE = "service_date";
  @SerializedName(SERIALIZED_NAME_SERVICE_DATE)
  private String serviceDate;

  public static final String SERIALIZED_NAME_UNITS = "units";
  @SerializedName(SERIALIZED_NAME_UNITS)
  private String units;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private String updatedAt;

  public BillingLineItem() {
  }

  public BillingLineItem(
     BigDecimal adjustment, 
     BigDecimal allowed, 
     BigDecimal balancePt, 
     String balanceTotal, 
     BigDecimal billed, 
     BillingStatusEnum billingStatus, 
     Boolean deniedFlag, 
     String description, 
     String doctor, 
     BigDecimal expectedReimbursement, 
     Integer id, 
     BigDecimal ins1Paid, 
     BigDecimal ins2Paid, 
     BigDecimal ins3Paid, 
     String insTotal, 
     String insuranceStatus, 
     String paidTotal, 
     String patient, 
     String postedDate, 
     String serviceDate, 
     String updatedAt
  ) {
    this();
    this.adjustment = adjustment;
    this.allowed = allowed;
    this.balancePt = balancePt;
    this.balanceTotal = balanceTotal;
    this.billed = billed;
    this.billingStatus = billingStatus;
    this.deniedFlag = deniedFlag;
    this.description = description;
    this.doctor = doctor;
    this.expectedReimbursement = expectedReimbursement;
    this.id = id;
    this.ins1Paid = ins1Paid;
    this.ins2Paid = ins2Paid;
    this.ins3Paid = ins3Paid;
    this.insTotal = insTotal;
    this.insuranceStatus = insuranceStatus;
    this.paidTotal = paidTotal;
    this.patient = patient;
    this.postedDate = postedDate;
    this.serviceDate = serviceDate;
    this.updatedAt = updatedAt;
  }

  /**
   * Adjustment from total billed
   * @return adjustment
   */
  @javax.annotation.Nullable
  public BigDecimal getAdjustment() {
    return adjustment;
  }



  /**
   * Amount allowed by insurance
   * @return allowed
   */
  @javax.annotation.Nullable
  public BigDecimal getAllowed() {
    return allowed;
  }



  public BillingLineItem appointment(Integer appointment) {
    this.appointment = appointment;
    return this;
  }

  /**
   * Appointment ID
   * @return appointment
   */
  @javax.annotation.Nonnull
  public Integer getAppointment() {
    return appointment;
  }

  public void setAppointment(Integer appointment) {
    this.appointment = appointment;
  }


  public BillingLineItem balanceIns(BigDecimal balanceIns) {
    this.balanceIns = balanceIns;
    return this;
  }

  /**
   * Insurance balance
   * @return balanceIns
   */
  @javax.annotation.Nullable
  public BigDecimal getBalanceIns() {
    return balanceIns;
  }

  public void setBalanceIns(BigDecimal balanceIns) {
    this.balanceIns = balanceIns;
  }


  /**
   * Patient balance
   * @return balancePt
   */
  @javax.annotation.Nullable
  public BigDecimal getBalancePt() {
    return balancePt;
  }



  /**
   * Total balance
   * @return balanceTotal
   */
  @javax.annotation.Nullable
  public String getBalanceTotal() {
    return balanceTotal;
  }



  /**
   * Total billed
   * @return billed
   */
  @javax.annotation.Nullable
  public BigDecimal getBilled() {
    return billed;
  }



  /**
   * One of &#x60;\&quot;\&quot;&#x60;, &#x60;\&quot;Incomplete Information\&quot;&#x60;, &#x60;\&quot;In Process Emdeon\&quot;&#x60;, &#x60;\&quot;In Process iHCFA\&quot;&#x60;, &#x60;\&quot;In Process Gateway\&quot;&#x60;, &#x60;\&quot;Rejected Emdeon\&quot;&#x60;, &#x60;\&quot;Rejected iHCFA\&quot;&#x60;, &#x60;\&quot;Rejected Gateway\&quot;&#x60;, &#x60;\&quot;In Process Payer\&quot;&#x60;, &#x60;\&quot;Payer Acknowledged\&quot;&#x60;, &#x60;\&quot;Rejected Payer\&quot;&#x60;, &#x60;\&quot;Paid in Full\&quot;&#x60;,  &#x60;\&quot;Partially Paid\&quot;&#x60;,  &#x60;\&quot;Coordination of Benefits\&quot;&#x60;,  &#x60;\&quot;ERA Received\&quot;&#x60;,  &#x60;\&quot;ERA Denied\&quot;&#x60;
   * @return billingStatus
   */
  @javax.annotation.Nullable
  public BillingStatusEnum getBillingStatus() {
    return billingStatus;
  }



  public BillingLineItem code(String code) {
    this.code = code;
    return this;
  }

  /**
   * 
   * @return code
   */
  @javax.annotation.Nonnull
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  /**
   * 
   * @return deniedFlag
   */
  @javax.annotation.Nullable
  public Boolean getDeniedFlag() {
    return deniedFlag;
  }



  /**
   * 
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }



  public BillingLineItem diagnosisPointers(List<String> diagnosisPointers) {
    this.diagnosisPointers = diagnosisPointers;
    return this;
  }

  public BillingLineItem addDiagnosisPointersItem(String diagnosisPointersItem) {
    if (this.diagnosisPointers == null) {
      this.diagnosisPointers = new ArrayList<>();
    }
    this.diagnosisPointers.add(diagnosisPointersItem);
    return this;
  }

  /**
   * List of 4 diagnosis pointers
   * @return diagnosisPointers
   */
  @javax.annotation.Nonnull
  public List<String> getDiagnosisPointers() {
    return diagnosisPointers;
  }

  public void setDiagnosisPointers(List<String> diagnosisPointers) {
    this.diagnosisPointers = diagnosisPointers;
  }


  /**
   * Doctor ID
   * @return doctor
   */
  @javax.annotation.Nullable
  public String getDoctor() {
    return doctor;
  }



  /**
   * 
   * @return expectedReimbursement
   */
  @javax.annotation.Nullable
  public BigDecimal getExpectedReimbursement() {
    return expectedReimbursement;
  }



  /**
   * 
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  /**
   * Amount paid by patient&#39;s primary insurer
   * @return ins1Paid
   */
  @javax.annotation.Nullable
  public BigDecimal getIns1Paid() {
    return ins1Paid;
  }



  /**
   * Amount paid by patient&#39;s secondary insurer
   * @return ins2Paid
   */
  @javax.annotation.Nullable
  public BigDecimal getIns2Paid() {
    return ins2Paid;
  }



  /**
   * Amount paid by patinet&#39;s tertiary insurer
   * @return ins3Paid
   */
  @javax.annotation.Nullable
  public BigDecimal getIns3Paid() {
    return ins3Paid;
  }



  /**
   * Total amount paid by patient&#39;s insurers
   * @return insTotal
   */
  @javax.annotation.Nullable
  public String getInsTotal() {
    return insTotal;
  }



  /**
   * This corresponds to the \&quot;Status/Adj Type\&quot; from billing detail screen
   * @return insuranceStatus
   */
  @javax.annotation.Nullable
  public String getInsuranceStatus() {
    return insuranceStatus;
  }



  public BillingLineItem modifiers(List<String> modifiers) {
    this.modifiers = modifiers;
    return this;
  }

  public BillingLineItem addModifiersItem(String modifiersItem) {
    if (this.modifiers == null) {
      this.modifiers = new ArrayList<>();
    }
    this.modifiers.add(modifiersItem);
    return this;
  }

  /**
   * List of 4 code modifiers
   * @return modifiers
   */
  @javax.annotation.Nullable
  public List<String> getModifiers() {
    return modifiers;
  }

  public void setModifiers(List<String> modifiers) {
    this.modifiers = modifiers;
  }


  /**
   * Total amount paid
   * @return paidTotal
   */
  @javax.annotation.Nullable
  public String getPaidTotal() {
    return paidTotal;
  }



  /**
   * Patient ID
   * @return patient
   */
  @javax.annotation.Nullable
  public String getPatient() {
    return patient;
  }



  /**
   * 
   * @return postedDate
   */
  @javax.annotation.Nullable
  public String getPostedDate() {
    return postedDate;
  }



  public BillingLineItem price(BigDecimal price) {
    this.price = price;
    return this;
  }

  /**
   * Price of procedure
   * @return price
   */
  @javax.annotation.Nullable
  public BigDecimal getPrice() {
    return price;
  }

  public void setPrice(BigDecimal price) {
    this.price = price;
  }


  public BillingLineItem procedureType(ProcedureTypeEnum procedureType) {
    this.procedureType = procedureType;
    return this;
  }

  /**
   * One of &#x60;\&quot;CPT(C)\&quot;&#x60;, &#x60;\&quot;HCPCS(H)\&quot;&#x60;, &#x60;\&quot;Custom(U)\&quot;&#x60;, use 1 character identifier when using &#x60;POST&#x60;
   * @return procedureType
   */
  @javax.annotation.Nonnull
  public ProcedureTypeEnum getProcedureType() {
    return procedureType;
  }

  public void setProcedureType(ProcedureTypeEnum procedureType) {
    this.procedureType = procedureType;
  }


  public BillingLineItem ptPaid(BigDecimal ptPaid) {
    this.ptPaid = ptPaid;
    return this;
  }

  /**
   * Amount paid by patient
   * @return ptPaid
   */
  @javax.annotation.Nullable
  public BigDecimal getPtPaid() {
    return ptPaid;
  }

  public void setPtPaid(BigDecimal ptPaid) {
    this.ptPaid = ptPaid;
  }


  public BillingLineItem quantity(BigDecimal quantity) {
    this.quantity = quantity;
    return this;
  }

  /**
   * 
   * @return quantity
   */
  @javax.annotation.Nullable
  public BigDecimal getQuantity() {
    return quantity;
  }

  public void setQuantity(BigDecimal quantity) {
    this.quantity = quantity;
  }


  /**
   * Date on which the service was rendered
   * @return serviceDate
   */
  @javax.annotation.Nullable
  public String getServiceDate() {
    return serviceDate;
  }



  public BillingLineItem units(String units) {
    this.units = units;
    return this;
  }

  /**
   * Default to \&quot;UN\&quot;
   * @return units
   */
  @javax.annotation.Nullable
  public String getUnits() {
    return units;
  }

  public void setUnits(String units) {
    this.units = units;
  }


  /**
   * 
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public String getUpdatedAt() {
    return updatedAt;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BillingLineItem billingLineItem = (BillingLineItem) o;
    return Objects.equals(this.adjustment, billingLineItem.adjustment) &&
        Objects.equals(this.allowed, billingLineItem.allowed) &&
        Objects.equals(this.appointment, billingLineItem.appointment) &&
        Objects.equals(this.balanceIns, billingLineItem.balanceIns) &&
        Objects.equals(this.balancePt, billingLineItem.balancePt) &&
        Objects.equals(this.balanceTotal, billingLineItem.balanceTotal) &&
        Objects.equals(this.billed, billingLineItem.billed) &&
        Objects.equals(this.billingStatus, billingLineItem.billingStatus) &&
        Objects.equals(this.code, billingLineItem.code) &&
        Objects.equals(this.deniedFlag, billingLineItem.deniedFlag) &&
        Objects.equals(this.description, billingLineItem.description) &&
        Objects.equals(this.diagnosisPointers, billingLineItem.diagnosisPointers) &&
        Objects.equals(this.doctor, billingLineItem.doctor) &&
        Objects.equals(this.expectedReimbursement, billingLineItem.expectedReimbursement) &&
        Objects.equals(this.id, billingLineItem.id) &&
        Objects.equals(this.ins1Paid, billingLineItem.ins1Paid) &&
        Objects.equals(this.ins2Paid, billingLineItem.ins2Paid) &&
        Objects.equals(this.ins3Paid, billingLineItem.ins3Paid) &&
        Objects.equals(this.insTotal, billingLineItem.insTotal) &&
        Objects.equals(this.insuranceStatus, billingLineItem.insuranceStatus) &&
        Objects.equals(this.modifiers, billingLineItem.modifiers) &&
        Objects.equals(this.paidTotal, billingLineItem.paidTotal) &&
        Objects.equals(this.patient, billingLineItem.patient) &&
        Objects.equals(this.postedDate, billingLineItem.postedDate) &&
        Objects.equals(this.price, billingLineItem.price) &&
        Objects.equals(this.procedureType, billingLineItem.procedureType) &&
        Objects.equals(this.ptPaid, billingLineItem.ptPaid) &&
        Objects.equals(this.quantity, billingLineItem.quantity) &&
        Objects.equals(this.serviceDate, billingLineItem.serviceDate) &&
        Objects.equals(this.units, billingLineItem.units) &&
        Objects.equals(this.updatedAt, billingLineItem.updatedAt);
  }

  @Override
  public int hashCode() {
    return Objects.hash(adjustment, allowed, appointment, balanceIns, balancePt, balanceTotal, billed, billingStatus, code, deniedFlag, description, diagnosisPointers, doctor, expectedReimbursement, id, ins1Paid, ins2Paid, ins3Paid, insTotal, insuranceStatus, modifiers, paidTotal, patient, postedDate, price, procedureType, ptPaid, quantity, serviceDate, units, updatedAt);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BillingLineItem {\n");
    sb.append("    adjustment: ").append(toIndentedString(adjustment)).append("\n");
    sb.append("    allowed: ").append(toIndentedString(allowed)).append("\n");
    sb.append("    appointment: ").append(toIndentedString(appointment)).append("\n");
    sb.append("    balanceIns: ").append(toIndentedString(balanceIns)).append("\n");
    sb.append("    balancePt: ").append(toIndentedString(balancePt)).append("\n");
    sb.append("    balanceTotal: ").append(toIndentedString(balanceTotal)).append("\n");
    sb.append("    billed: ").append(toIndentedString(billed)).append("\n");
    sb.append("    billingStatus: ").append(toIndentedString(billingStatus)).append("\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    deniedFlag: ").append(toIndentedString(deniedFlag)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    diagnosisPointers: ").append(toIndentedString(diagnosisPointers)).append("\n");
    sb.append("    doctor: ").append(toIndentedString(doctor)).append("\n");
    sb.append("    expectedReimbursement: ").append(toIndentedString(expectedReimbursement)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    ins1Paid: ").append(toIndentedString(ins1Paid)).append("\n");
    sb.append("    ins2Paid: ").append(toIndentedString(ins2Paid)).append("\n");
    sb.append("    ins3Paid: ").append(toIndentedString(ins3Paid)).append("\n");
    sb.append("    insTotal: ").append(toIndentedString(insTotal)).append("\n");
    sb.append("    insuranceStatus: ").append(toIndentedString(insuranceStatus)).append("\n");
    sb.append("    modifiers: ").append(toIndentedString(modifiers)).append("\n");
    sb.append("    paidTotal: ").append(toIndentedString(paidTotal)).append("\n");
    sb.append("    patient: ").append(toIndentedString(patient)).append("\n");
    sb.append("    postedDate: ").append(toIndentedString(postedDate)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    procedureType: ").append(toIndentedString(procedureType)).append("\n");
    sb.append("    ptPaid: ").append(toIndentedString(ptPaid)).append("\n");
    sb.append("    quantity: ").append(toIndentedString(quantity)).append("\n");
    sb.append("    serviceDate: ").append(toIndentedString(serviceDate)).append("\n");
    sb.append("    units: ").append(toIndentedString(units)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
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
    openapiFields.add("adjustment");
    openapiFields.add("allowed");
    openapiFields.add("appointment");
    openapiFields.add("balance_ins");
    openapiFields.add("balance_pt");
    openapiFields.add("balance_total");
    openapiFields.add("billed");
    openapiFields.add("billing_status");
    openapiFields.add("code");
    openapiFields.add("denied_flag");
    openapiFields.add("description");
    openapiFields.add("diagnosis_pointers");
    openapiFields.add("doctor");
    openapiFields.add("expected_reimbursement");
    openapiFields.add("id");
    openapiFields.add("ins1_paid");
    openapiFields.add("ins2_paid");
    openapiFields.add("ins3_paid");
    openapiFields.add("ins_total");
    openapiFields.add("insurance_status");
    openapiFields.add("modifiers");
    openapiFields.add("paid_total");
    openapiFields.add("patient");
    openapiFields.add("posted_date");
    openapiFields.add("price");
    openapiFields.add("procedure_type");
    openapiFields.add("pt_paid");
    openapiFields.add("quantity");
    openapiFields.add("service_date");
    openapiFields.add("units");
    openapiFields.add("updated_at");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("appointment");
    openapiRequiredFields.add("code");
    openapiRequiredFields.add("diagnosis_pointers");
    openapiRequiredFields.add("procedure_type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BillingLineItem
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BillingLineItem.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BillingLineItem is not found in the empty JSON string", BillingLineItem.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BillingLineItem.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BillingLineItem` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : BillingLineItem.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("balance_total") != null && !jsonObj.get("balance_total").isJsonNull()) && !jsonObj.get("balance_total").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `balance_total` to be a primitive type in the JSON string but got `%s`", jsonObj.get("balance_total").toString()));
      }
      if ((jsonObj.get("billing_status") != null && !jsonObj.get("billing_status").isJsonNull()) && !jsonObj.get("billing_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `billing_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("billing_status").toString()));
      }
      // validate the optional field `billing_status`
      if (jsonObj.get("billing_status") != null && !jsonObj.get("billing_status").isJsonNull()) {
        BillingStatusEnum.validateJsonElement(jsonObj.get("billing_status"));
      }
      if (!jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("diagnosis_pointers") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("diagnosis_pointers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `diagnosis_pointers` to be an array in the JSON string but got `%s`", jsonObj.get("diagnosis_pointers").toString()));
      }
      if ((jsonObj.get("doctor") != null && !jsonObj.get("doctor").isJsonNull()) && !jsonObj.get("doctor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `doctor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("doctor").toString()));
      }
      if ((jsonObj.get("ins_total") != null && !jsonObj.get("ins_total").isJsonNull()) && !jsonObj.get("ins_total").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ins_total` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ins_total").toString()));
      }
      if ((jsonObj.get("insurance_status") != null && !jsonObj.get("insurance_status").isJsonNull()) && !jsonObj.get("insurance_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `insurance_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("insurance_status").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("modifiers") != null && !jsonObj.get("modifiers").isJsonNull() && !jsonObj.get("modifiers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `modifiers` to be an array in the JSON string but got `%s`", jsonObj.get("modifiers").toString()));
      }
      if ((jsonObj.get("paid_total") != null && !jsonObj.get("paid_total").isJsonNull()) && !jsonObj.get("paid_total").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `paid_total` to be a primitive type in the JSON string but got `%s`", jsonObj.get("paid_total").toString()));
      }
      if ((jsonObj.get("patient") != null && !jsonObj.get("patient").isJsonNull()) && !jsonObj.get("patient").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `patient` to be a primitive type in the JSON string but got `%s`", jsonObj.get("patient").toString()));
      }
      if ((jsonObj.get("posted_date") != null && !jsonObj.get("posted_date").isJsonNull()) && !jsonObj.get("posted_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `posted_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("posted_date").toString()));
      }
      if (!jsonObj.get("procedure_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `procedure_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("procedure_type").toString()));
      }
      // validate the required field `procedure_type`
      ProcedureTypeEnum.validateJsonElement(jsonObj.get("procedure_type"));
      if ((jsonObj.get("service_date") != null && !jsonObj.get("service_date").isJsonNull()) && !jsonObj.get("service_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service_date").toString()));
      }
      if ((jsonObj.get("units") != null && !jsonObj.get("units").isJsonNull()) && !jsonObj.get("units").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `units` to be a primitive type in the JSON string but got `%s`", jsonObj.get("units").toString()));
      }
      if ((jsonObj.get("updated_at") != null && !jsonObj.get("updated_at").isJsonNull()) && !jsonObj.get("updated_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_at").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BillingLineItem.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BillingLineItem' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BillingLineItem> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BillingLineItem.class));

       return (TypeAdapter<T>) new TypeAdapter<BillingLineItem>() {
           @Override
           public void write(JsonWriter out, BillingLineItem value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BillingLineItem read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BillingLineItem given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BillingLineItem
   * @throws IOException if the JSON string is invalid with respect to BillingLineItem
   */
  public static BillingLineItem fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BillingLineItem.class);
  }

  /**
   * Convert an instance of BillingLineItem to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

