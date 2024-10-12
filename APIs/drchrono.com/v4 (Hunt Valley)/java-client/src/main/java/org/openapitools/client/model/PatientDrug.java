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
 * PatientDrug
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PatientDrug {
  public static final String SERIALIZED_NAME_APPOINTMENT = "appointment";
  @SerializedName(SERIALIZED_NAME_APPOINTMENT)
  private Integer appointment;

  public static final String SERIALIZED_NAME_DATE_PRESCRIBED = "date_prescribed";
  @SerializedName(SERIALIZED_NAME_DATE_PRESCRIBED)
  private String datePrescribed;

  public static final String SERIALIZED_NAME_DATE_STARTED_TAKING = "date_started_taking";
  @SerializedName(SERIALIZED_NAME_DATE_STARTED_TAKING)
  private String dateStartedTaking;

  public static final String SERIALIZED_NAME_DATE_STOPPED_TAKING = "date_stopped_taking";
  @SerializedName(SERIALIZED_NAME_DATE_STOPPED_TAKING)
  private String dateStoppedTaking;

  public static final String SERIALIZED_NAME_DAW = "daw";
  @SerializedName(SERIALIZED_NAME_DAW)
  private Boolean daw;

  public static final String SERIALIZED_NAME_DISPENSE_QUANTITY = "dispense_quantity";
  @SerializedName(SERIALIZED_NAME_DISPENSE_QUANTITY)
  private BigDecimal dispenseQuantity;

  public static final String SERIALIZED_NAME_DOCTOR = "doctor";
  @SerializedName(SERIALIZED_NAME_DOCTOR)
  private Integer doctor;

  public static final String SERIALIZED_NAME_DOSAGE_QUANTITY = "dosage_quantity";
  @SerializedName(SERIALIZED_NAME_DOSAGE_QUANTITY)
  private String dosageQuantity;

  public static final String SERIALIZED_NAME_DOSAGE_UNITS = "dosage_units";
  @SerializedName(SERIALIZED_NAME_DOSAGE_UNITS)
  private String dosageUnits;

  public static final String SERIALIZED_NAME_FREQUENCY = "frequency";
  @SerializedName(SERIALIZED_NAME_FREQUENCY)
  private String frequency;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_INDICATION = "indication";
  @SerializedName(SERIALIZED_NAME_INDICATION)
  private String indication;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NDC = "ndc";
  @SerializedName(SERIALIZED_NAME_NDC)
  private String ndc;

  public static final String SERIALIZED_NAME_NOTES = "notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_NUMBER_REFILLS = "number_refills";
  @SerializedName(SERIALIZED_NAME_NUMBER_REFILLS)
  private Integer numberRefills;

  /**
   * One of &#x60;\&quot;\&quot;&#x60;, &#x60;\&quot;Ordered\&quot;&#x60;, &#x60;\&quot;Administered during visit\&quot;&#x60;, &#x60;\&quot;Electronic eRx Sent\&quot;&#x60;, &#x60;\&quot;Phoned into Pharmacy\&quot;&#x60;, &#x60;\&quot;Faxed to Pharmacy\&quot;&#x60;, &#x60;\&quot;Paper Rx\&quot;&#x60;, &#x60;\&quot;Prescription Printed\&quot;&#x60;, &#x60;\&quot;Discontinued\&quot;&#x60;, &#x60;\&quot;Prescribed by other Dr\&quot;&#x60; or &#x60;\&quot;Over the Counter\&quot;&#x60;. If omitted in writing, default to &#x60;\&quot;\&quot;&#x60;
   */
  @JsonAdapter(OrderStatusEnum.Adapter.class)
  public enum OrderStatusEnum {
    EMPTY(""),
    
    ORDERED("Ordered"),
    
    ADMINISTERED_DURING_VISIT("Administered during visit"),
    
    ELECTRONIC_E_RX_SENT("Electronic eRx Sent"),
    
    PHONED_INTO_PHARMACY("Phoned into Pharmacy"),
    
    FAXED_TO_PHARMACY("Faxed to Pharmacy"),
    
    PAPER_RX("Paper Rx"),
    
    PRESCRIPTION_PRINTED("Prescription Printed"),
    
    DISCONTINUED("Discontinued"),
    
    PRESCRIBED_BY_OTHER_DR("Prescribed by other Dr"),
    
    OVER_THE_COUNTER("Over the Counter");

    private String value;

    OrderStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static OrderStatusEnum fromValue(String value) {
      for (OrderStatusEnum b : OrderStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<OrderStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final OrderStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public OrderStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return OrderStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      OrderStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ORDER_STATUS = "order_status";
  @SerializedName(SERIALIZED_NAME_ORDER_STATUS)
  private OrderStatusEnum orderStatus;

  public static final String SERIALIZED_NAME_PATIENT = "patient";
  @SerializedName(SERIALIZED_NAME_PATIENT)
  private Integer patient;

  public static final String SERIALIZED_NAME_PHARMACY_NOTE = "pharmacy_note";
  @SerializedName(SERIALIZED_NAME_PHARMACY_NOTE)
  private String pharmacyNote;

  public static final String SERIALIZED_NAME_PRN = "prn";
  @SerializedName(SERIALIZED_NAME_PRN)
  private Boolean prn;

  public static final String SERIALIZED_NAME_ROUTE = "route";
  @SerializedName(SERIALIZED_NAME_ROUTE)
  private String route;

  public static final String SERIALIZED_NAME_RXNORM = "rxnorm";
  @SerializedName(SERIALIZED_NAME_RXNORM)
  private String rxnorm;

  public static final String SERIALIZED_NAME_SIGNATURE_NOTE = "signature_note";
  @SerializedName(SERIALIZED_NAME_SIGNATURE_NOTE)
  private String signatureNote;

  /**
   * If present, one of &#x60;\&quot;active\&quot;&#x60; or &#x60;\&quot;inactive\&quot;&#x60;. If omitted in writing, default to &#x60;\&quot;active\&quot;&#x60;
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    ACTIVE("active"),
    
    INACTIVE("inactive");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public PatientDrug() {
  }

  public PatientDrug(
     Integer id
  ) {
    this();
    this.id = id;
  }

  public PatientDrug appointment(Integer appointment) {
    this.appointment = appointment;
    return this;
  }

  /**
   * Appointment ID corresponding to the initial prescription
   * @return appointment
   */
  @javax.annotation.Nullable
  public Integer getAppointment() {
    return appointment;
  }

  public void setAppointment(Integer appointment) {
    this.appointment = appointment;
  }


  public PatientDrug datePrescribed(String datePrescribed) {
    this.datePrescribed = datePrescribed;
    return this;
  }

  /**
   * 
   * @return datePrescribed
   */
  @javax.annotation.Nullable
  public String getDatePrescribed() {
    return datePrescribed;
  }

  public void setDatePrescribed(String datePrescribed) {
    this.datePrescribed = datePrescribed;
  }


  public PatientDrug dateStartedTaking(String dateStartedTaking) {
    this.dateStartedTaking = dateStartedTaking;
    return this;
  }

  /**
   * 
   * @return dateStartedTaking
   */
  @javax.annotation.Nullable
  public String getDateStartedTaking() {
    return dateStartedTaking;
  }

  public void setDateStartedTaking(String dateStartedTaking) {
    this.dateStartedTaking = dateStartedTaking;
  }


  public PatientDrug dateStoppedTaking(String dateStoppedTaking) {
    this.dateStoppedTaking = dateStoppedTaking;
    return this;
  }

  /**
   * 
   * @return dateStoppedTaking
   */
  @javax.annotation.Nullable
  public String getDateStoppedTaking() {
    return dateStoppedTaking;
  }

  public void setDateStoppedTaking(String dateStoppedTaking) {
    this.dateStoppedTaking = dateStoppedTaking;
  }


  public PatientDrug daw(Boolean daw) {
    this.daw = daw;
    return this;
  }

  /**
   * If true, the prescription should be dispensed as written and not substituted
   * @return daw
   */
  @javax.annotation.Nullable
  public Boolean getDaw() {
    return daw;
  }

  public void setDaw(Boolean daw) {
    this.daw = daw;
  }


  public PatientDrug dispenseQuantity(BigDecimal dispenseQuantity) {
    this.dispenseQuantity = dispenseQuantity;
    return this;
  }

  /**
   * 
   * @return dispenseQuantity
   */
  @javax.annotation.Nullable
  public BigDecimal getDispenseQuantity() {
    return dispenseQuantity;
  }

  public void setDispenseQuantity(BigDecimal dispenseQuantity) {
    this.dispenseQuantity = dispenseQuantity;
  }


  public PatientDrug doctor(Integer doctor) {
    this.doctor = doctor;
    return this;
  }

  /**
   * Prescribing doctor ID
   * @return doctor
   */
  @javax.annotation.Nonnull
  public Integer getDoctor() {
    return doctor;
  }

  public void setDoctor(Integer doctor) {
    this.doctor = doctor;
  }


  public PatientDrug dosageQuantity(String dosageQuantity) {
    this.dosageQuantity = dosageQuantity;
    return this;
  }

  /**
   * Please note, this used to be an decimal field, you can still pass decimal value to it. Or you can pass in some formatted string if needed.
   * @return dosageQuantity
   */
  @javax.annotation.Nullable
  public String getDosageQuantity() {
    return dosageQuantity;
  }

  public void setDosageQuantity(String dosageQuantity) {
    this.dosageQuantity = dosageQuantity;
  }


  public PatientDrug dosageUnits(String dosageUnits) {
    this.dosageUnits = dosageUnits;
    return this;
  }

  /**
   * 
   * @return dosageUnits
   */
  @javax.annotation.Nullable
  public String getDosageUnits() {
    return dosageUnits;
  }

  public void setDosageUnits(String dosageUnits) {
    this.dosageUnits = dosageUnits;
  }


  public PatientDrug frequency(String frequency) {
    this.frequency = frequency;
    return this;
  }

  /**
   * Frequency pf administration
   * @return frequency
   */
  @javax.annotation.Nullable
  public String getFrequency() {
    return frequency;
  }

  public void setFrequency(String frequency) {
    this.frequency = frequency;
  }


  /**
   * 
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  public PatientDrug indication(String indication) {
    this.indication = indication;
    return this;
  }

  /**
   * 
   * @return indication
   */
  @javax.annotation.Nullable
  public String getIndication() {
    return indication;
  }

  public void setIndication(String indication) {
    this.indication = indication;
  }


  public PatientDrug name(String name) {
    this.name = name;
    return this;
  }

  /**
   * 
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public PatientDrug ndc(String ndc) {
    this.ndc = ndc;
    return this;
  }

  /**
   * 
   * @return ndc
   */
  @javax.annotation.Nullable
  public String getNdc() {
    return ndc;
  }

  public void setNdc(String ndc) {
    this.ndc = ndc;
  }


  public PatientDrug notes(String notes) {
    this.notes = notes;
    return this;
  }

  /**
   * Any additional notes from the provider
   * @return notes
   */
  @javax.annotation.Nullable
  public String getNotes() {
    return notes;
  }

  public void setNotes(String notes) {
    this.notes = notes;
  }


  public PatientDrug numberRefills(Integer numberRefills) {
    this.numberRefills = numberRefills;
    return this;
  }

  /**
   * 
   * @return numberRefills
   */
  @javax.annotation.Nullable
  public Integer getNumberRefills() {
    return numberRefills;
  }

  public void setNumberRefills(Integer numberRefills) {
    this.numberRefills = numberRefills;
  }


  public PatientDrug orderStatus(OrderStatusEnum orderStatus) {
    this.orderStatus = orderStatus;
    return this;
  }

  /**
   * One of &#x60;\&quot;\&quot;&#x60;, &#x60;\&quot;Ordered\&quot;&#x60;, &#x60;\&quot;Administered during visit\&quot;&#x60;, &#x60;\&quot;Electronic eRx Sent\&quot;&#x60;, &#x60;\&quot;Phoned into Pharmacy\&quot;&#x60;, &#x60;\&quot;Faxed to Pharmacy\&quot;&#x60;, &#x60;\&quot;Paper Rx\&quot;&#x60;, &#x60;\&quot;Prescription Printed\&quot;&#x60;, &#x60;\&quot;Discontinued\&quot;&#x60;, &#x60;\&quot;Prescribed by other Dr\&quot;&#x60; or &#x60;\&quot;Over the Counter\&quot;&#x60;. If omitted in writing, default to &#x60;\&quot;\&quot;&#x60;
   * @return orderStatus
   */
  @javax.annotation.Nullable
  public OrderStatusEnum getOrderStatus() {
    return orderStatus;
  }

  public void setOrderStatus(OrderStatusEnum orderStatus) {
    this.orderStatus = orderStatus;
  }


  public PatientDrug patient(Integer patient) {
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


  public PatientDrug pharmacyNote(String pharmacyNote) {
    this.pharmacyNote = pharmacyNote;
    return this;
  }

  /**
   * 
   * @return pharmacyNote
   */
  @javax.annotation.Nullable
  public String getPharmacyNote() {
    return pharmacyNote;
  }

  public void setPharmacyNote(String pharmacyNote) {
    this.pharmacyNote = pharmacyNote;
  }


  public PatientDrug prn(Boolean prn) {
    this.prn = prn;
    return this;
  }

  /**
   * If &#x60;True&#x60;, the medication should be taken when necessary
   * @return prn
   */
  @javax.annotation.Nullable
  public Boolean getPrn() {
    return prn;
  }

  public void setPrn(Boolean prn) {
    this.prn = prn;
  }


  public PatientDrug route(String route) {
    this.route = route;
    return this;
  }

  /**
   * Route of administration
   * @return route
   */
  @javax.annotation.Nullable
  public String getRoute() {
    return route;
  }

  public void setRoute(String route) {
    this.route = route;
  }


  public PatientDrug rxnorm(String rxnorm) {
    this.rxnorm = rxnorm;
    return this;
  }

  /**
   * RxNorm code for the medication
   * @return rxnorm
   */
  @javax.annotation.Nullable
  public String getRxnorm() {
    return rxnorm;
  }

  public void setRxnorm(String rxnorm) {
    this.rxnorm = rxnorm;
  }


  public PatientDrug signatureNote(String signatureNote) {
    this.signatureNote = signatureNote;
    return this;
  }

  /**
   * 
   * @return signatureNote
   */
  @javax.annotation.Nullable
  public String getSignatureNote() {
    return signatureNote;
  }

  public void setSignatureNote(String signatureNote) {
    this.signatureNote = signatureNote;
  }


  public PatientDrug status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * If present, one of &#x60;\&quot;active\&quot;&#x60; or &#x60;\&quot;inactive\&quot;&#x60;. If omitted in writing, default to &#x60;\&quot;active\&quot;&#x60;
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PatientDrug patientDrug = (PatientDrug) o;
    return Objects.equals(this.appointment, patientDrug.appointment) &&
        Objects.equals(this.datePrescribed, patientDrug.datePrescribed) &&
        Objects.equals(this.dateStartedTaking, patientDrug.dateStartedTaking) &&
        Objects.equals(this.dateStoppedTaking, patientDrug.dateStoppedTaking) &&
        Objects.equals(this.daw, patientDrug.daw) &&
        Objects.equals(this.dispenseQuantity, patientDrug.dispenseQuantity) &&
        Objects.equals(this.doctor, patientDrug.doctor) &&
        Objects.equals(this.dosageQuantity, patientDrug.dosageQuantity) &&
        Objects.equals(this.dosageUnits, patientDrug.dosageUnits) &&
        Objects.equals(this.frequency, patientDrug.frequency) &&
        Objects.equals(this.id, patientDrug.id) &&
        Objects.equals(this.indication, patientDrug.indication) &&
        Objects.equals(this.name, patientDrug.name) &&
        Objects.equals(this.ndc, patientDrug.ndc) &&
        Objects.equals(this.notes, patientDrug.notes) &&
        Objects.equals(this.numberRefills, patientDrug.numberRefills) &&
        Objects.equals(this.orderStatus, patientDrug.orderStatus) &&
        Objects.equals(this.patient, patientDrug.patient) &&
        Objects.equals(this.pharmacyNote, patientDrug.pharmacyNote) &&
        Objects.equals(this.prn, patientDrug.prn) &&
        Objects.equals(this.route, patientDrug.route) &&
        Objects.equals(this.rxnorm, patientDrug.rxnorm) &&
        Objects.equals(this.signatureNote, patientDrug.signatureNote) &&
        Objects.equals(this.status, patientDrug.status);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appointment, datePrescribed, dateStartedTaking, dateStoppedTaking, daw, dispenseQuantity, doctor, dosageQuantity, dosageUnits, frequency, id, indication, name, ndc, notes, numberRefills, orderStatus, patient, pharmacyNote, prn, route, rxnorm, signatureNote, status);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PatientDrug {\n");
    sb.append("    appointment: ").append(toIndentedString(appointment)).append("\n");
    sb.append("    datePrescribed: ").append(toIndentedString(datePrescribed)).append("\n");
    sb.append("    dateStartedTaking: ").append(toIndentedString(dateStartedTaking)).append("\n");
    sb.append("    dateStoppedTaking: ").append(toIndentedString(dateStoppedTaking)).append("\n");
    sb.append("    daw: ").append(toIndentedString(daw)).append("\n");
    sb.append("    dispenseQuantity: ").append(toIndentedString(dispenseQuantity)).append("\n");
    sb.append("    doctor: ").append(toIndentedString(doctor)).append("\n");
    sb.append("    dosageQuantity: ").append(toIndentedString(dosageQuantity)).append("\n");
    sb.append("    dosageUnits: ").append(toIndentedString(dosageUnits)).append("\n");
    sb.append("    frequency: ").append(toIndentedString(frequency)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    indication: ").append(toIndentedString(indication)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    ndc: ").append(toIndentedString(ndc)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    numberRefills: ").append(toIndentedString(numberRefills)).append("\n");
    sb.append("    orderStatus: ").append(toIndentedString(orderStatus)).append("\n");
    sb.append("    patient: ").append(toIndentedString(patient)).append("\n");
    sb.append("    pharmacyNote: ").append(toIndentedString(pharmacyNote)).append("\n");
    sb.append("    prn: ").append(toIndentedString(prn)).append("\n");
    sb.append("    route: ").append(toIndentedString(route)).append("\n");
    sb.append("    rxnorm: ").append(toIndentedString(rxnorm)).append("\n");
    sb.append("    signatureNote: ").append(toIndentedString(signatureNote)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
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
    openapiFields.add("appointment");
    openapiFields.add("date_prescribed");
    openapiFields.add("date_started_taking");
    openapiFields.add("date_stopped_taking");
    openapiFields.add("daw");
    openapiFields.add("dispense_quantity");
    openapiFields.add("doctor");
    openapiFields.add("dosage_quantity");
    openapiFields.add("dosage_units");
    openapiFields.add("frequency");
    openapiFields.add("id");
    openapiFields.add("indication");
    openapiFields.add("name");
    openapiFields.add("ndc");
    openapiFields.add("notes");
    openapiFields.add("number_refills");
    openapiFields.add("order_status");
    openapiFields.add("patient");
    openapiFields.add("pharmacy_note");
    openapiFields.add("prn");
    openapiFields.add("route");
    openapiFields.add("rxnorm");
    openapiFields.add("signature_note");
    openapiFields.add("status");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("doctor");
    openapiRequiredFields.add("patient");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PatientDrug
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PatientDrug.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PatientDrug is not found in the empty JSON string", PatientDrug.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PatientDrug.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PatientDrug` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PatientDrug.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("date_prescribed") != null && !jsonObj.get("date_prescribed").isJsonNull()) && !jsonObj.get("date_prescribed").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date_prescribed` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date_prescribed").toString()));
      }
      if ((jsonObj.get("date_started_taking") != null && !jsonObj.get("date_started_taking").isJsonNull()) && !jsonObj.get("date_started_taking").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date_started_taking` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date_started_taking").toString()));
      }
      if ((jsonObj.get("date_stopped_taking") != null && !jsonObj.get("date_stopped_taking").isJsonNull()) && !jsonObj.get("date_stopped_taking").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date_stopped_taking` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date_stopped_taking").toString()));
      }
      if ((jsonObj.get("dosage_quantity") != null && !jsonObj.get("dosage_quantity").isJsonNull()) && !jsonObj.get("dosage_quantity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dosage_quantity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dosage_quantity").toString()));
      }
      if ((jsonObj.get("dosage_units") != null && !jsonObj.get("dosage_units").isJsonNull()) && !jsonObj.get("dosage_units").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dosage_units` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dosage_units").toString()));
      }
      if ((jsonObj.get("frequency") != null && !jsonObj.get("frequency").isJsonNull()) && !jsonObj.get("frequency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `frequency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("frequency").toString()));
      }
      if ((jsonObj.get("indication") != null && !jsonObj.get("indication").isJsonNull()) && !jsonObj.get("indication").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `indication` to be a primitive type in the JSON string but got `%s`", jsonObj.get("indication").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("ndc") != null && !jsonObj.get("ndc").isJsonNull()) && !jsonObj.get("ndc").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ndc` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ndc").toString()));
      }
      if ((jsonObj.get("notes") != null && !jsonObj.get("notes").isJsonNull()) && !jsonObj.get("notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("notes").toString()));
      }
      if ((jsonObj.get("order_status") != null && !jsonObj.get("order_status").isJsonNull()) && !jsonObj.get("order_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_status").toString()));
      }
      // validate the optional field `order_status`
      if (jsonObj.get("order_status") != null && !jsonObj.get("order_status").isJsonNull()) {
        OrderStatusEnum.validateJsonElement(jsonObj.get("order_status"));
      }
      if ((jsonObj.get("pharmacy_note") != null && !jsonObj.get("pharmacy_note").isJsonNull()) && !jsonObj.get("pharmacy_note").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pharmacy_note` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pharmacy_note").toString()));
      }
      if ((jsonObj.get("route") != null && !jsonObj.get("route").isJsonNull()) && !jsonObj.get("route").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `route` to be a primitive type in the JSON string but got `%s`", jsonObj.get("route").toString()));
      }
      if ((jsonObj.get("rxnorm") != null && !jsonObj.get("rxnorm").isJsonNull()) && !jsonObj.get("rxnorm").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rxnorm` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rxnorm").toString()));
      }
      if ((jsonObj.get("signature_note") != null && !jsonObj.get("signature_note").isJsonNull()) && !jsonObj.get("signature_note").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `signature_note` to be a primitive type in the JSON string but got `%s`", jsonObj.get("signature_note").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PatientDrug.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PatientDrug' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PatientDrug> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PatientDrug.class));

       return (TypeAdapter<T>) new TypeAdapter<PatientDrug>() {
           @Override
           public void write(JsonWriter out, PatientDrug value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PatientDrug read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PatientDrug given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PatientDrug
   * @throws IOException if the JSON string is invalid with respect to PatientDrug
   */
  public static PatientDrug fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PatientDrug.class);
  }

  /**
   * Convert an instance of PatientDrug to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

