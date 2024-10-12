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
 * PatientProblem
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PatientProblem {
  public static final String SERIALIZED_NAME_DATE_CHANGED = "date_changed";
  @SerializedName(SERIALIZED_NAME_DATE_CHANGED)
  private String dateChanged;

  public static final String SERIALIZED_NAME_DATE_DIAGNOSIS = "date_diagnosis";
  @SerializedName(SERIALIZED_NAME_DATE_DIAGNOSIS)
  private String dateDiagnosis;

  public static final String SERIALIZED_NAME_DATE_ONSET = "date_onset";
  @SerializedName(SERIALIZED_NAME_DATE_ONSET)
  private String dateOnset;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DOCTOR = "doctor";
  @SerializedName(SERIALIZED_NAME_DOCTOR)
  private Integer doctor;

  public static final String SERIALIZED_NAME_ICD_CODE = "icd_code";
  @SerializedName(SERIALIZED_NAME_ICD_CODE)
  private String icdCode;

  /**
   * Either &#x60;9&#x60; or &#x60;10&#x60;. If omitted in writing, default to 10.
   */
  @JsonAdapter(IcdVersionEnum.Adapter.class)
  public enum IcdVersionEnum {
    _9("9"),
    
    _10("10");

    private String value;

    IcdVersionEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static IcdVersionEnum fromValue(String value) {
      for (IcdVersionEnum b : IcdVersionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<IcdVersionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final IcdVersionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public IcdVersionEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return IcdVersionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      IcdVersionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ICD_VERSION = "icd_version";
  @SerializedName(SERIALIZED_NAME_ICD_VERSION)
  private IcdVersionEnum icdVersion;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_INFO_URL = "info_url";
  @SerializedName(SERIALIZED_NAME_INFO_URL)
  private String infoUrl;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NOTES = "notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_PATIENT = "patient";
  @SerializedName(SERIALIZED_NAME_PATIENT)
  private Integer patient;

  public static final String SERIALIZED_NAME_SNOMED_CT_CODE = "snomed_ct_code";
  @SerializedName(SERIALIZED_NAME_SNOMED_CT_CODE)
  private String snomedCtCode;

  /**
   * Either &#x60;active&#x60;, &#x60;inactive&#x60; or &#x60;resolved&#x60;. If omitted in writing, default to &#x60;active&#x60;
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    ACTIVE("active"),
    
    INACTIVE("inactive"),
    
    RESOLVED("resolved");

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

  public PatientProblem() {
  }

  public PatientProblem(
     Integer id, 
     String infoUrl
  ) {
    this();
    this.id = id;
    this.infoUrl = infoUrl;
  }

  public PatientProblem dateChanged(String dateChanged) {
    this.dateChanged = dateChanged;
    return this;
  }

  /**
   * 
   * @return dateChanged
   */
  @javax.annotation.Nullable
  public String getDateChanged() {
    return dateChanged;
  }

  public void setDateChanged(String dateChanged) {
    this.dateChanged = dateChanged;
  }


  public PatientProblem dateDiagnosis(String dateDiagnosis) {
    this.dateDiagnosis = dateDiagnosis;
    return this;
  }

  /**
   * 
   * @return dateDiagnosis
   */
  @javax.annotation.Nullable
  public String getDateDiagnosis() {
    return dateDiagnosis;
  }

  public void setDateDiagnosis(String dateDiagnosis) {
    this.dateDiagnosis = dateDiagnosis;
  }


  public PatientProblem dateOnset(String dateOnset) {
    this.dateOnset = dateOnset;
    return this;
  }

  /**
   * 
   * @return dateOnset
   */
  @javax.annotation.Nullable
  public String getDateOnset() {
    return dateOnset;
  }

  public void setDateOnset(String dateOnset) {
    this.dateOnset = dateOnset;
  }


  public PatientProblem description(String description) {
    this.description = description;
    return this;
  }

  /**
   * 
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public PatientProblem doctor(Integer doctor) {
    this.doctor = doctor;
    return this;
  }

  /**
   * 
   * @return doctor
   */
  @javax.annotation.Nonnull
  public Integer getDoctor() {
    return doctor;
  }

  public void setDoctor(Integer doctor) {
    this.doctor = doctor;
  }


  public PatientProblem icdCode(String icdCode) {
    this.icdCode = icdCode;
    return this;
  }

  /**
   * ICD9 or ICD10 code for the problem
   * @return icdCode
   */
  @javax.annotation.Nullable
  public String getIcdCode() {
    return icdCode;
  }

  public void setIcdCode(String icdCode) {
    this.icdCode = icdCode;
  }


  public PatientProblem icdVersion(IcdVersionEnum icdVersion) {
    this.icdVersion = icdVersion;
    return this;
  }

  /**
   * Either &#x60;9&#x60; or &#x60;10&#x60;. If omitted in writing, default to 10.
   * @return icdVersion
   */
  @javax.annotation.Nullable
  public IcdVersionEnum getIcdVersion() {
    return icdVersion;
  }

  public void setIcdVersion(IcdVersionEnum icdVersion) {
    this.icdVersion = icdVersion;
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
   * External URL with more information about the problem, intended for patient education
   * @return infoUrl
   */
  @javax.annotation.Nullable
  public String getInfoUrl() {
    return infoUrl;
  }



  public PatientProblem name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of the problem
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public PatientProblem notes(String notes) {
    this.notes = notes;
    return this;
  }

  /**
   * Any additional notes by the provider
   * @return notes
   */
  @javax.annotation.Nullable
  public String getNotes() {
    return notes;
  }

  public void setNotes(String notes) {
    this.notes = notes;
  }


  public PatientProblem patient(Integer patient) {
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


  public PatientProblem snomedCtCode(String snomedCtCode) {
    this.snomedCtCode = snomedCtCode;
    return this;
  }

  /**
   * SnoMED code for the problem
   * @return snomedCtCode
   */
  @javax.annotation.Nullable
  public String getSnomedCtCode() {
    return snomedCtCode;
  }

  public void setSnomedCtCode(String snomedCtCode) {
    this.snomedCtCode = snomedCtCode;
  }


  public PatientProblem status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Either &#x60;active&#x60;, &#x60;inactive&#x60; or &#x60;resolved&#x60;. If omitted in writing, default to &#x60;active&#x60;
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
    PatientProblem patientProblem = (PatientProblem) o;
    return Objects.equals(this.dateChanged, patientProblem.dateChanged) &&
        Objects.equals(this.dateDiagnosis, patientProblem.dateDiagnosis) &&
        Objects.equals(this.dateOnset, patientProblem.dateOnset) &&
        Objects.equals(this.description, patientProblem.description) &&
        Objects.equals(this.doctor, patientProblem.doctor) &&
        Objects.equals(this.icdCode, patientProblem.icdCode) &&
        Objects.equals(this.icdVersion, patientProblem.icdVersion) &&
        Objects.equals(this.id, patientProblem.id) &&
        Objects.equals(this.infoUrl, patientProblem.infoUrl) &&
        Objects.equals(this.name, patientProblem.name) &&
        Objects.equals(this.notes, patientProblem.notes) &&
        Objects.equals(this.patient, patientProblem.patient) &&
        Objects.equals(this.snomedCtCode, patientProblem.snomedCtCode) &&
        Objects.equals(this.status, patientProblem.status);
  }

  @Override
  public int hashCode() {
    return Objects.hash(dateChanged, dateDiagnosis, dateOnset, description, doctor, icdCode, icdVersion, id, infoUrl, name, notes, patient, snomedCtCode, status);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PatientProblem {\n");
    sb.append("    dateChanged: ").append(toIndentedString(dateChanged)).append("\n");
    sb.append("    dateDiagnosis: ").append(toIndentedString(dateDiagnosis)).append("\n");
    sb.append("    dateOnset: ").append(toIndentedString(dateOnset)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    doctor: ").append(toIndentedString(doctor)).append("\n");
    sb.append("    icdCode: ").append(toIndentedString(icdCode)).append("\n");
    sb.append("    icdVersion: ").append(toIndentedString(icdVersion)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    infoUrl: ").append(toIndentedString(infoUrl)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    patient: ").append(toIndentedString(patient)).append("\n");
    sb.append("    snomedCtCode: ").append(toIndentedString(snomedCtCode)).append("\n");
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
    openapiFields.add("date_changed");
    openapiFields.add("date_diagnosis");
    openapiFields.add("date_onset");
    openapiFields.add("description");
    openapiFields.add("doctor");
    openapiFields.add("icd_code");
    openapiFields.add("icd_version");
    openapiFields.add("id");
    openapiFields.add("info_url");
    openapiFields.add("name");
    openapiFields.add("notes");
    openapiFields.add("patient");
    openapiFields.add("snomed_ct_code");
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
   * @throws IOException if the JSON Element is invalid with respect to PatientProblem
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PatientProblem.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PatientProblem is not found in the empty JSON string", PatientProblem.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PatientProblem.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PatientProblem` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PatientProblem.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("date_changed") != null && !jsonObj.get("date_changed").isJsonNull()) && !jsonObj.get("date_changed").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date_changed` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date_changed").toString()));
      }
      if ((jsonObj.get("date_diagnosis") != null && !jsonObj.get("date_diagnosis").isJsonNull()) && !jsonObj.get("date_diagnosis").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date_diagnosis` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date_diagnosis").toString()));
      }
      if ((jsonObj.get("date_onset") != null && !jsonObj.get("date_onset").isJsonNull()) && !jsonObj.get("date_onset").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date_onset` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date_onset").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("icd_code") != null && !jsonObj.get("icd_code").isJsonNull()) && !jsonObj.get("icd_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `icd_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("icd_code").toString()));
      }
      if ((jsonObj.get("icd_version") != null && !jsonObj.get("icd_version").isJsonNull()) && !jsonObj.get("icd_version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `icd_version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("icd_version").toString()));
      }
      // validate the optional field `icd_version`
      if (jsonObj.get("icd_version") != null && !jsonObj.get("icd_version").isJsonNull()) {
        IcdVersionEnum.validateJsonElement(jsonObj.get("icd_version"));
      }
      if ((jsonObj.get("info_url") != null && !jsonObj.get("info_url").isJsonNull()) && !jsonObj.get("info_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `info_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("info_url").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("notes") != null && !jsonObj.get("notes").isJsonNull()) && !jsonObj.get("notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("notes").toString()));
      }
      if ((jsonObj.get("snomed_ct_code") != null && !jsonObj.get("snomed_ct_code").isJsonNull()) && !jsonObj.get("snomed_ct_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `snomed_ct_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("snomed_ct_code").toString()));
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
       if (!PatientProblem.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PatientProblem' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PatientProblem> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PatientProblem.class));

       return (TypeAdapter<T>) new TypeAdapter<PatientProblem>() {
           @Override
           public void write(JsonWriter out, PatientProblem value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PatientProblem read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PatientProblem given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PatientProblem
   * @throws IOException if the JSON string is invalid with respect to PatientProblem
   */
  public static PatientProblem fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PatientProblem.class);
  }

  /**
   * Convert an instance of PatientProblem to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

