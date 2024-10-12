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
 * PatientLabResultSet
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PatientLabResultSet {
  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_DATE_TEST_PERFORMED = "date_test_performed";
  @SerializedName(SERIALIZED_NAME_DATE_TEST_PERFORMED)
  private String dateTestPerformed;

  public static final String SERIALIZED_NAME_DOCTOR_COMMENTS = "doctor_comments";
  @SerializedName(SERIALIZED_NAME_DOCTOR_COMMENTS)
  private String doctorComments;

  public static final String SERIALIZED_NAME_DOCTOR_SIGNOFF = "doctor_signoff";
  @SerializedName(SERIALIZED_NAME_DOCTOR_SIGNOFF)
  private Boolean doctorSignoff;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  /**
   * HL7 codified abnormal flag for the result.
   */
  @JsonAdapter(LabAbnormalFlagEnum.Adapter.class)
  public enum LabAbnormalFlagEnum {
    EMPTY(""),
    
    L("L"),
    
    H("H"),
    
    LL("LL"),
    
    HH("HH"),
    
    LESS_THAN("<"),
    
    GREATER_THAN(">"),
    
    N("N"),
    
    A("A"),
    
    AA("AA"),
    
    NULL("null"),
    
    U("U"),
    
    D("D"),
    
    B("B"),
    
    W("W"),
    
    S("S"),
    
    R("R"),
    
    I("I"),
    
    MS("MS"),
    
    VS("VS");

    private String value;

    LabAbnormalFlagEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static LabAbnormalFlagEnum fromValue(String value) {
      for (LabAbnormalFlagEnum b : LabAbnormalFlagEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<LabAbnormalFlagEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final LabAbnormalFlagEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public LabAbnormalFlagEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return LabAbnormalFlagEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      LabAbnormalFlagEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_LAB_ABNORMAL_FLAG = "lab_abnormal_flag";
  @SerializedName(SERIALIZED_NAME_LAB_ABNORMAL_FLAG)
  private LabAbnormalFlagEnum labAbnormalFlag;

  public static final String SERIALIZED_NAME_LAB_IMPORTED_FROM_CCR = "lab_imported_from_ccr";
  @SerializedName(SERIALIZED_NAME_LAB_IMPORTED_FROM_CCR)
  private String labImportedFromCcr;

  public static final String SERIALIZED_NAME_LAB_NORMAL_RANGE = "lab_normal_range";
  @SerializedName(SERIALIZED_NAME_LAB_NORMAL_RANGE)
  private String labNormalRange;

  public static final String SERIALIZED_NAME_LAB_NORMAL_RANGE_UNITS = "lab_normal_range_units";
  @SerializedName(SERIALIZED_NAME_LAB_NORMAL_RANGE_UNITS)
  private String labNormalRangeUnits;

  /**
   * Status of the lab order.
   */
  @JsonAdapter(LabOrderStatusEnum.Adapter.class)
  public enum LabOrderStatusEnum {
    EMPTY(""),
    
    ORDER_ENTERED("Order Entered"),
    
    DISCONTINUED("Discontinued"),
    
    IN_PROGRESS("In Progress"),
    
    RESULTS_RECEIVED("Results Received"),
    
    RESULTS_REVIEWED_WITH_PATIENT("Results Reviewed with Patient"),
    
    PAPER_ORDER("Paper Order");

    private String value;

    LabOrderStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static LabOrderStatusEnum fromValue(String value) {
      for (LabOrderStatusEnum b : LabOrderStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<LabOrderStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final LabOrderStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public LabOrderStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return LabOrderStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      LabOrderStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_LAB_ORDER_STATUS = "lab_order_status";
  @SerializedName(SERIALIZED_NAME_LAB_ORDER_STATUS)
  private LabOrderStatusEnum labOrderStatus;

  public static final String SERIALIZED_NAME_LAB_RESULT_VALUE = "lab_result_value";
  @SerializedName(SERIALIZED_NAME_LAB_RESULT_VALUE)
  private String labResultValue;

  public static final String SERIALIZED_NAME_LAB_RESULT_VALUE_AS_FLOAT = "lab_result_value_as_float";
  @SerializedName(SERIALIZED_NAME_LAB_RESULT_VALUE_AS_FLOAT)
  private BigDecimal labResultValueAsFloat;

  public static final String SERIALIZED_NAME_LAB_RESULT_VALUE_UNITS = "lab_result_value_units";
  @SerializedName(SERIALIZED_NAME_LAB_RESULT_VALUE_UNITS)
  private String labResultValueUnits;

  public static final String SERIALIZED_NAME_LOINC_CODE = "loinc_code";
  @SerializedName(SERIALIZED_NAME_LOINC_CODE)
  private String loincCode;

  public static final String SERIALIZED_NAME_ORDERING_DOCTOR = "ordering_doctor";
  @SerializedName(SERIALIZED_NAME_ORDERING_DOCTOR)
  private Integer orderingDoctor;

  public static final String SERIALIZED_NAME_PATIENT = "patient";
  @SerializedName(SERIALIZED_NAME_PATIENT)
  private Integer patient;

  public static final String SERIALIZED_NAME_SCANNED_IN_RESULT = "scanned_in_result";
  @SerializedName(SERIALIZED_NAME_SCANNED_IN_RESULT)
  private String scannedInResult;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private String updatedAt;

  public PatientLabResultSet() {
  }

  public PatientLabResultSet(
     String createdAt, 
     Integer id, 
     String labImportedFromCcr, 
     String scannedInResult, 
     String updatedAt
  ) {
    this();
    this.createdAt = createdAt;
    this.id = id;
    this.labImportedFromCcr = labImportedFromCcr;
    this.scannedInResult = scannedInResult;
    this.updatedAt = updatedAt;
  }

  /**
   * 
   * @return createdAt
   */
  @javax.annotation.Nullable
  public String getCreatedAt() {
    return createdAt;
  }



  public PatientLabResultSet dateTestPerformed(String dateTestPerformed) {
    this.dateTestPerformed = dateTestPerformed;
    return this;
  }

  /**
   * Date of lab test.
   * @return dateTestPerformed
   */
  @javax.annotation.Nullable
  public String getDateTestPerformed() {
    return dateTestPerformed;
  }

  public void setDateTestPerformed(String dateTestPerformed) {
    this.dateTestPerformed = dateTestPerformed;
  }


  public PatientLabResultSet doctorComments(String doctorComments) {
    this.doctorComments = doctorComments;
    return this;
  }

  /**
   * Comment from the doctor on lab result.
   * @return doctorComments
   */
  @javax.annotation.Nullable
  public String getDoctorComments() {
    return doctorComments;
  }

  public void setDoctorComments(String doctorComments) {
    this.doctorComments = doctorComments;
  }


  public PatientLabResultSet doctorSignoff(Boolean doctorSignoff) {
    this.doctorSignoff = doctorSignoff;
    return this;
  }

  /**
   * Check this box when the doctor has reviewed the lab result and taken appropriate action.
   * @return doctorSignoff
   */
  @javax.annotation.Nullable
  public Boolean getDoctorSignoff() {
    return doctorSignoff;
  }

  public void setDoctorSignoff(Boolean doctorSignoff) {
    this.doctorSignoff = doctorSignoff;
  }


  /**
   * 
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  public PatientLabResultSet labAbnormalFlag(LabAbnormalFlagEnum labAbnormalFlag) {
    this.labAbnormalFlag = labAbnormalFlag;
    return this;
  }

  /**
   * HL7 codified abnormal flag for the result.
   * @return labAbnormalFlag
   */
  @javax.annotation.Nullable
  public LabAbnormalFlagEnum getLabAbnormalFlag() {
    return labAbnormalFlag;
  }

  public void setLabAbnormalFlag(LabAbnormalFlagEnum labAbnormalFlag) {
    this.labAbnormalFlag = labAbnormalFlag;
  }


  /**
   * Imported CCR document that contains lab results.
   * @return labImportedFromCcr
   */
  @javax.annotation.Nullable
  public String getLabImportedFromCcr() {
    return labImportedFromCcr;
  }



  public PatientLabResultSet labNormalRange(String labNormalRange) {
    this.labNormalRange = labNormalRange;
    return this;
  }

  /**
   * 
   * @return labNormalRange
   */
  @javax.annotation.Nullable
  public String getLabNormalRange() {
    return labNormalRange;
  }

  public void setLabNormalRange(String labNormalRange) {
    this.labNormalRange = labNormalRange;
  }


  public PatientLabResultSet labNormalRangeUnits(String labNormalRangeUnits) {
    this.labNormalRangeUnits = labNormalRangeUnits;
    return this;
  }

  /**
   * 
   * @return labNormalRangeUnits
   */
  @javax.annotation.Nullable
  public String getLabNormalRangeUnits() {
    return labNormalRangeUnits;
  }

  public void setLabNormalRangeUnits(String labNormalRangeUnits) {
    this.labNormalRangeUnits = labNormalRangeUnits;
  }


  public PatientLabResultSet labOrderStatus(LabOrderStatusEnum labOrderStatus) {
    this.labOrderStatus = labOrderStatus;
    return this;
  }

  /**
   * Status of the lab order.
   * @return labOrderStatus
   */
  @javax.annotation.Nullable
  public LabOrderStatusEnum getLabOrderStatus() {
    return labOrderStatus;
  }

  public void setLabOrderStatus(LabOrderStatusEnum labOrderStatus) {
    this.labOrderStatus = labOrderStatus;
  }


  public PatientLabResultSet labResultValue(String labResultValue) {
    this.labResultValue = labResultValue;
    return this;
  }

  /**
   * 
   * @return labResultValue
   */
  @javax.annotation.Nullable
  public String getLabResultValue() {
    return labResultValue;
  }

  public void setLabResultValue(String labResultValue) {
    this.labResultValue = labResultValue;
  }


  public PatientLabResultSet labResultValueAsFloat(BigDecimal labResultValueAsFloat) {
    this.labResultValueAsFloat = labResultValueAsFloat;
    return this;
  }

  /**
   * 
   * @return labResultValueAsFloat
   */
  @javax.annotation.Nullable
  public BigDecimal getLabResultValueAsFloat() {
    return labResultValueAsFloat;
  }

  public void setLabResultValueAsFloat(BigDecimal labResultValueAsFloat) {
    this.labResultValueAsFloat = labResultValueAsFloat;
  }


  public PatientLabResultSet labResultValueUnits(String labResultValueUnits) {
    this.labResultValueUnits = labResultValueUnits;
    return this;
  }

  /**
   * 
   * @return labResultValueUnits
   */
  @javax.annotation.Nullable
  public String getLabResultValueUnits() {
    return labResultValueUnits;
  }

  public void setLabResultValueUnits(String labResultValueUnits) {
    this.labResultValueUnits = labResultValueUnits;
  }


  public PatientLabResultSet loincCode(String loincCode) {
    this.loincCode = loincCode;
    return this;
  }

  /**
   * 
   * @return loincCode
   */
  @javax.annotation.Nullable
  public String getLoincCode() {
    return loincCode;
  }

  public void setLoincCode(String loincCode) {
    this.loincCode = loincCode;
  }


  public PatientLabResultSet orderingDoctor(Integer orderingDoctor) {
    this.orderingDoctor = orderingDoctor;
    return this;
  }

  /**
   * 
   * @return orderingDoctor
   */
  @javax.annotation.Nonnull
  public Integer getOrderingDoctor() {
    return orderingDoctor;
  }

  public void setOrderingDoctor(Integer orderingDoctor) {
    this.orderingDoctor = orderingDoctor;
  }


  public PatientLabResultSet patient(Integer patient) {
    this.patient = patient;
    return this;
  }

  /**
   * 
   * @return patient
   */
  @javax.annotation.Nonnull
  public Integer getPatient() {
    return patient;
  }

  public void setPatient(Integer patient) {
    this.patient = patient;
  }


  /**
   * Scanned in PDF for this lab result (optional).
   * @return scannedInResult
   */
  @javax.annotation.Nullable
  public String getScannedInResult() {
    return scannedInResult;
  }



  public PatientLabResultSet title(String title) {
    this.title = title;
    return this;
  }

  /**
   * 
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
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
    PatientLabResultSet patientLabResultSet = (PatientLabResultSet) o;
    return Objects.equals(this.createdAt, patientLabResultSet.createdAt) &&
        Objects.equals(this.dateTestPerformed, patientLabResultSet.dateTestPerformed) &&
        Objects.equals(this.doctorComments, patientLabResultSet.doctorComments) &&
        Objects.equals(this.doctorSignoff, patientLabResultSet.doctorSignoff) &&
        Objects.equals(this.id, patientLabResultSet.id) &&
        Objects.equals(this.labAbnormalFlag, patientLabResultSet.labAbnormalFlag) &&
        Objects.equals(this.labImportedFromCcr, patientLabResultSet.labImportedFromCcr) &&
        Objects.equals(this.labNormalRange, patientLabResultSet.labNormalRange) &&
        Objects.equals(this.labNormalRangeUnits, patientLabResultSet.labNormalRangeUnits) &&
        Objects.equals(this.labOrderStatus, patientLabResultSet.labOrderStatus) &&
        Objects.equals(this.labResultValue, patientLabResultSet.labResultValue) &&
        Objects.equals(this.labResultValueAsFloat, patientLabResultSet.labResultValueAsFloat) &&
        Objects.equals(this.labResultValueUnits, patientLabResultSet.labResultValueUnits) &&
        Objects.equals(this.loincCode, patientLabResultSet.loincCode) &&
        Objects.equals(this.orderingDoctor, patientLabResultSet.orderingDoctor) &&
        Objects.equals(this.patient, patientLabResultSet.patient) &&
        Objects.equals(this.scannedInResult, patientLabResultSet.scannedInResult) &&
        Objects.equals(this.title, patientLabResultSet.title) &&
        Objects.equals(this.updatedAt, patientLabResultSet.updatedAt);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdAt, dateTestPerformed, doctorComments, doctorSignoff, id, labAbnormalFlag, labImportedFromCcr, labNormalRange, labNormalRangeUnits, labOrderStatus, labResultValue, labResultValueAsFloat, labResultValueUnits, loincCode, orderingDoctor, patient, scannedInResult, title, updatedAt);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PatientLabResultSet {\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    dateTestPerformed: ").append(toIndentedString(dateTestPerformed)).append("\n");
    sb.append("    doctorComments: ").append(toIndentedString(doctorComments)).append("\n");
    sb.append("    doctorSignoff: ").append(toIndentedString(doctorSignoff)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    labAbnormalFlag: ").append(toIndentedString(labAbnormalFlag)).append("\n");
    sb.append("    labImportedFromCcr: ").append(toIndentedString(labImportedFromCcr)).append("\n");
    sb.append("    labNormalRange: ").append(toIndentedString(labNormalRange)).append("\n");
    sb.append("    labNormalRangeUnits: ").append(toIndentedString(labNormalRangeUnits)).append("\n");
    sb.append("    labOrderStatus: ").append(toIndentedString(labOrderStatus)).append("\n");
    sb.append("    labResultValue: ").append(toIndentedString(labResultValue)).append("\n");
    sb.append("    labResultValueAsFloat: ").append(toIndentedString(labResultValueAsFloat)).append("\n");
    sb.append("    labResultValueUnits: ").append(toIndentedString(labResultValueUnits)).append("\n");
    sb.append("    loincCode: ").append(toIndentedString(loincCode)).append("\n");
    sb.append("    orderingDoctor: ").append(toIndentedString(orderingDoctor)).append("\n");
    sb.append("    patient: ").append(toIndentedString(patient)).append("\n");
    sb.append("    scannedInResult: ").append(toIndentedString(scannedInResult)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
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
    openapiFields.add("created_at");
    openapiFields.add("date_test_performed");
    openapiFields.add("doctor_comments");
    openapiFields.add("doctor_signoff");
    openapiFields.add("id");
    openapiFields.add("lab_abnormal_flag");
    openapiFields.add("lab_imported_from_ccr");
    openapiFields.add("lab_normal_range");
    openapiFields.add("lab_normal_range_units");
    openapiFields.add("lab_order_status");
    openapiFields.add("lab_result_value");
    openapiFields.add("lab_result_value_as_float");
    openapiFields.add("lab_result_value_units");
    openapiFields.add("loinc_code");
    openapiFields.add("ordering_doctor");
    openapiFields.add("patient");
    openapiFields.add("scanned_in_result");
    openapiFields.add("title");
    openapiFields.add("updated_at");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("ordering_doctor");
    openapiRequiredFields.add("patient");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PatientLabResultSet
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PatientLabResultSet.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PatientLabResultSet is not found in the empty JSON string", PatientLabResultSet.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PatientLabResultSet.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PatientLabResultSet` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PatientLabResultSet.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("created_at") != null && !jsonObj.get("created_at").isJsonNull()) && !jsonObj.get("created_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_at").toString()));
      }
      if ((jsonObj.get("date_test_performed") != null && !jsonObj.get("date_test_performed").isJsonNull()) && !jsonObj.get("date_test_performed").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date_test_performed` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date_test_performed").toString()));
      }
      if ((jsonObj.get("doctor_comments") != null && !jsonObj.get("doctor_comments").isJsonNull()) && !jsonObj.get("doctor_comments").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `doctor_comments` to be a primitive type in the JSON string but got `%s`", jsonObj.get("doctor_comments").toString()));
      }
      if ((jsonObj.get("lab_abnormal_flag") != null && !jsonObj.get("lab_abnormal_flag").isJsonNull()) && !jsonObj.get("lab_abnormal_flag").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lab_abnormal_flag` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lab_abnormal_flag").toString()));
      }
      // validate the optional field `lab_abnormal_flag`
      if (jsonObj.get("lab_abnormal_flag") != null && !jsonObj.get("lab_abnormal_flag").isJsonNull()) {
        LabAbnormalFlagEnum.validateJsonElement(jsonObj.get("lab_abnormal_flag"));
      }
      if ((jsonObj.get("lab_imported_from_ccr") != null && !jsonObj.get("lab_imported_from_ccr").isJsonNull()) && !jsonObj.get("lab_imported_from_ccr").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lab_imported_from_ccr` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lab_imported_from_ccr").toString()));
      }
      if ((jsonObj.get("lab_normal_range") != null && !jsonObj.get("lab_normal_range").isJsonNull()) && !jsonObj.get("lab_normal_range").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lab_normal_range` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lab_normal_range").toString()));
      }
      if ((jsonObj.get("lab_normal_range_units") != null && !jsonObj.get("lab_normal_range_units").isJsonNull()) && !jsonObj.get("lab_normal_range_units").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lab_normal_range_units` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lab_normal_range_units").toString()));
      }
      if ((jsonObj.get("lab_order_status") != null && !jsonObj.get("lab_order_status").isJsonNull()) && !jsonObj.get("lab_order_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lab_order_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lab_order_status").toString()));
      }
      // validate the optional field `lab_order_status`
      if (jsonObj.get("lab_order_status") != null && !jsonObj.get("lab_order_status").isJsonNull()) {
        LabOrderStatusEnum.validateJsonElement(jsonObj.get("lab_order_status"));
      }
      if ((jsonObj.get("lab_result_value") != null && !jsonObj.get("lab_result_value").isJsonNull()) && !jsonObj.get("lab_result_value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lab_result_value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lab_result_value").toString()));
      }
      if ((jsonObj.get("lab_result_value_units") != null && !jsonObj.get("lab_result_value_units").isJsonNull()) && !jsonObj.get("lab_result_value_units").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lab_result_value_units` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lab_result_value_units").toString()));
      }
      if ((jsonObj.get("loinc_code") != null && !jsonObj.get("loinc_code").isJsonNull()) && !jsonObj.get("loinc_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `loinc_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("loinc_code").toString()));
      }
      if ((jsonObj.get("scanned_in_result") != null && !jsonObj.get("scanned_in_result").isJsonNull()) && !jsonObj.get("scanned_in_result").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `scanned_in_result` to be a primitive type in the JSON string but got `%s`", jsonObj.get("scanned_in_result").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("updated_at") != null && !jsonObj.get("updated_at").isJsonNull()) && !jsonObj.get("updated_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_at").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PatientLabResultSet.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PatientLabResultSet' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PatientLabResultSet> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PatientLabResultSet.class));

       return (TypeAdapter<T>) new TypeAdapter<PatientLabResultSet>() {
           @Override
           public void write(JsonWriter out, PatientLabResultSet value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PatientLabResultSet read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PatientLabResultSet given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PatientLabResultSet
   * @throws IOException if the JSON string is invalid with respect to PatientLabResultSet
   */
  public static PatientLabResultSet fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PatientLabResultSet.class);
  }

  /**
   * Convert an instance of PatientLabResultSet to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

