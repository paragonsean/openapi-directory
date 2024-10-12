/*
 * Checks API
 * **NOTE:** This is a preview of the API and it is not considered stable since refinements are still being made.  # Introduction  Welcome to the  **Truora Check** [**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) reference. You may also want to check out our [**Validations API docs**](https://docs.validations.truora.com/) or our [**Signals API docs**](https://docs.signals.truora.com/).  Truora Check API allows performing full background checks on people, vehicles and companies. There are three main types of background checks:  - **Personal background check**: Verifies national IDs in multiple databases of public and legal entities in the LATAM region. For every national ID, returns information on: personal identity, criminal records, international background check, and professional background.  - **Vehicle background check**: Verifies the vehicle documents and the owner identity in multiple databases of public and legal entities in the LATAM region. For every vehicle and owner type, returns information on: personal identity, driving records, criminal records, and vehicle information.    - **Company background check**: Verifies the tax ID or a company name in multiple databases of public and legal entities in the LATAM region. For every company, returns the associated: business status, legal and criminal records, and media reports.  # API Key V1 is live!  API key version 1 is now live. Users with version 0 API keys are not immediately required to upgrade to V1 but should plan to do so at their earliest convenience. The changes for integration with API keys v1 are as follows:  - The field ``user_authorized`` is now required to perform person checks. This field indicates the API user has authorization to perform the check in compliance with data protection law. - The field ``homonym_scores`` is no longer included in our person check response as its results are already included in the body of the check and keeping them duplicated is generating unnecessary confusion.   # API composition  ## Endpoints  - **Check endpoints**: Provide an easy way to create and search for a background check. They also allow inserting groups of checks into reports. Each check contains scores, datasets and databases.   ```plain https://api.truora.com/v1/checks ```  - **Report endpoints**: Support batch uploads and grouping multiple checks together. Excel and .csv files are supported for batch uploads.   ```plain https://api.truora.com/v1/reports ```  - **Configuration endpoints**: Allows personalizing data sets and scores for customized background checks.  ```plain https://api.truora.com/v1/config ```  - **Continuous check endpoints**: Allows creating recurring checks and get notified whenever a change in the check score occurs.  ```plain https://api.truora.com/v1/continuous_checks ```  - **Behavior endpoints**: Allows sharing anonymous feedback about a person behavior when interacting with the company.  ```plain https://api.truora.com/v1/behaviour ```  - **Hooks endpoints**: Allows sending notifications via requests to your service or another third-party service whenever certain events occur.  ```plain https://api.truora.com/v1/hooks ```  ## Datasets  Categories that group the resulting information for background checks from databases are called datasets. Datasets are divided in:  - **Personal identity**: Corroborates the existence and validates personal identity documents.   - **Criminal record**: Checks for crimes according to each country penal code or criminal code. Keep in mind that data aged less than 10 years is usually more consistent.  - **Legal background**: Checks for lawsuits filed. Keep in mind that data aged less than 10 years is usually more consistent.  - **International background**: Checks international lists for crimes related to identity theft, money laundering, terrorist financing, and high crimes.  - **Professional background**: Checks professional regulatory entities for relevant information.  - **Affiliations and insurances**: Checks the history and status of social security affiliations.  - **Alert in media**: Checks major media agencies for relevant news related to violent actions.      - **Vehicle information**: Checks for the physical characteristics of the vehicle, technical status, insurance history, and other relevant information.  - **Traffic fines**: Checks for outstanding traffic fines.  - **Driving licenses**: Shows information relevant to the driver. Such as license status and driver certificates.  - **Business background**: Checks for business status, legal and criminal history, and other relevant information.  - **Taxes and Finances**: Checks for the information related to personal finances, liabilities, and taxes.  ## Requests Format  The POST requests receive a body that must be encoded in `www-x-form-urlencoded`, for instance:  ```plain type=person&national_id=123456&country=CO ```  The responses are always encoded in `JSON` format.  ## Errors  Whenever there is an error, a JSON with the following format is returned:  ```json {     \"code\": <Truora error code>,     \"http_code\": <The HTTP status of the response>,     \"message\": <The error message> } ```  for instance:  ```json {     \"code\": 10404,     \"http_code\": 404,     \"message\": \"The Check was not found\" } ```  ## SDKs  If your favorite language was not on the next list, You can use our [OpenAPI 3 spec](https://docs.truora.com/openapi.json) to generate it using the [Open API Generator](https://openapi-generator.tech/docs/installation).  To download the SDK click on the desired programming language:  - [C# .Net Core](https://truora-sdk.s3.amazonaws.com/checks/checks_csharp-netcore_latest.zip)  - [Elixir](https://truora-sdk.s3.amazonaws.com/checks/checks_elixir_latest.zip)  - [Go](https://truora-sdk.s3.amazonaws.com/checks/checks_go_latest.zip)  - [Java](https://truora-sdk.s3.amazonaws.com/checks/checks_java_latest.zip)  - [JavaScript](https://truora-sdk.s3.amazonaws.com/checks/checks_javascript_latest.zip)  - [Objc](https://truora-sdk.s3.amazonaws.com/checks/checks_objc_latest.zip)  - [Php](https://truora-sdk.s3.amazonaws.com/checks/checks_php_latest.zip)  - [Python](https://truora-sdk.s3.amazonaws.com/checks/checks_python_latest.zip)  - [Ruby](https://truora-sdk.s3.amazonaws.com/checks/checks_ruby_latest.zip)  You can see the full list of supported platforms here:  https://openapi-generator.tech/docs/generators   
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: api@truora.com
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
import java.time.LocalDate;
import java.util.Arrays;
import org.openapitools.client.model.Check;
import org.openapitools.client.model.ContinuousCheckEntry;

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
 * Continuous check allows for background checks to be performed on the same people or vehicles periodically and notifies if new information is found. Allowing companies to keep an eye on their workforce or vehicle fleet for any recent wrongdoing they might be involved in.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:35.353156-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ContinuousCheck {
  public static final String SERIALIZED_NAME_CONTINUOUS_CHECK_I_D = "ContinuousCheckID";
  @SerializedName(SERIALIZED_NAME_CONTINUOUS_CHECK_I_D)
  private String continuousCheckID;

  /**
   * Shows whether the background check score rose, fell, stood the same or was just created
   */
  @JsonAdapter(ContinuousCheckStatusEnum.Adapter.class)
  public enum ContinuousCheckStatusEnum {
    NEW("new"),
    
    UP("up"),
    
    DOWN("down"),
    
    SAME("same");

    private String value;

    ContinuousCheckStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ContinuousCheckStatusEnum fromValue(String value) {
      for (ContinuousCheckStatusEnum b : ContinuousCheckStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ContinuousCheckStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ContinuousCheckStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ContinuousCheckStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ContinuousCheckStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ContinuousCheckStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CONTINUOUS_CHECK_STATUS = "ContinuousCheckStatus";
  @SerializedName(SERIALIZED_NAME_CONTINUOUS_CHECK_STATUS)
  private ContinuousCheckStatusEnum continuousCheckStatus;

  public static final String SERIALIZED_NAME_CREATION_DATE = "CreationDate";
  @SerializedName(SERIALIZED_NAME_CREATION_DATE)
  private LocalDate creationDate;

  public static final String SERIALIZED_NAME_ENABLED = "Enabled";
  @SerializedName(SERIALIZED_NAME_ENABLED)
  private Boolean enabled;

  public static final String SERIALIZED_NAME_FREQUENCY = "Frequency";
  @SerializedName(SERIALIZED_NAME_FREQUENCY)
  private String frequency;

  public static final String SERIALIZED_NAME_HISTORY = "History";
  @SerializedName(SERIALIZED_NAME_HISTORY)
  private ContinuousCheckEntry history;

  public static final String SERIALIZED_NAME_LAST_CHECK_I_D = "LastCheckID";
  @SerializedName(SERIALIZED_NAME_LAST_CHECK_I_D)
  private String lastCheckID;

  public static final String SERIALIZED_NAME_NEXT_RUN_DATE = "NextRunDate";
  @SerializedName(SERIALIZED_NAME_NEXT_RUN_DATE)
  private LocalDate nextRunDate;

  public static final String SERIALIZED_NAME_ORIGINAL_CHECK = "OriginalCheck";
  @SerializedName(SERIALIZED_NAME_ORIGINAL_CHECK)
  private Check originalCheck;

  public static final String SERIALIZED_NAME_UPDATE_DATE = "UpdateDate";
  @SerializedName(SERIALIZED_NAME_UPDATE_DATE)
  private LocalDate updateDate;

  public ContinuousCheck() {
  }

  public ContinuousCheck continuousCheckID(String continuousCheckID) {
    this.continuousCheckID = continuousCheckID;
    return this;
  }

  /**
   * Continuous check ID [partition key and sort key]
   * @return continuousCheckID
   */
  @javax.annotation.Nullable
  public String getContinuousCheckID() {
    return continuousCheckID;
  }

  public void setContinuousCheckID(String continuousCheckID) {
    this.continuousCheckID = continuousCheckID;
  }


  public ContinuousCheck continuousCheckStatus(ContinuousCheckStatusEnum continuousCheckStatus) {
    this.continuousCheckStatus = continuousCheckStatus;
    return this;
  }

  /**
   * Shows whether the background check score rose, fell, stood the same or was just created
   * @return continuousCheckStatus
   */
  @javax.annotation.Nonnull
  public ContinuousCheckStatusEnum getContinuousCheckStatus() {
    return continuousCheckStatus;
  }

  public void setContinuousCheckStatus(ContinuousCheckStatusEnum continuousCheckStatus) {
    this.continuousCheckStatus = continuousCheckStatus;
  }


  public ContinuousCheck creationDate(LocalDate creationDate) {
    this.creationDate = creationDate;
    return this;
  }

  /**
   * Continuous check creation date in RFC3339 format
   * @return creationDate
   */
  @javax.annotation.Nullable
  public LocalDate getCreationDate() {
    return creationDate;
  }

  public void setCreationDate(LocalDate creationDate) {
    this.creationDate = creationDate;
  }


  public ContinuousCheck enabled(Boolean enabled) {
    this.enabled = enabled;
    return this;
  }

  /**
   * Indicates whether continuous check is enabled
   * @return enabled
   */
  @javax.annotation.Nullable
  public Boolean getEnabled() {
    return enabled;
  }

  public void setEnabled(Boolean enabled) {
    this.enabled = enabled;
  }


  public ContinuousCheck frequency(String frequency) {
    this.frequency = frequency;
    return this;
  }

  /**
   * Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks
   * @return frequency
   */
  @javax.annotation.Nonnull
  public String getFrequency() {
    return frequency;
  }

  public void setFrequency(String frequency) {
    this.frequency = frequency;
  }


  public ContinuousCheck history(ContinuousCheckEntry history) {
    this.history = history;
    return this;
  }

  /**
   * Get history
   * @return history
   */
  @javax.annotation.Nullable
  public ContinuousCheckEntry getHistory() {
    return history;
  }

  public void setHistory(ContinuousCheckEntry history) {
    this.history = history;
  }


  public ContinuousCheck lastCheckID(String lastCheckID) {
    this.lastCheckID = lastCheckID;
    return this;
  }

  /**
   * Last check ID
   * @return lastCheckID
   */
  @javax.annotation.Nonnull
  public String getLastCheckID() {
    return lastCheckID;
  }

  public void setLastCheckID(String lastCheckID) {
    this.lastCheckID = lastCheckID;
  }


  public ContinuousCheck nextRunDate(LocalDate nextRunDate) {
    this.nextRunDate = nextRunDate;
    return this;
  }

  /**
   * Next background check date, in RFC3339 format (without time)
   * @return nextRunDate
   */
  @javax.annotation.Nullable
  public LocalDate getNextRunDate() {
    return nextRunDate;
  }

  public void setNextRunDate(LocalDate nextRunDate) {
    this.nextRunDate = nextRunDate;
  }


  public ContinuousCheck originalCheck(Check originalCheck) {
    this.originalCheck = originalCheck;
    return this;
  }

  /**
   * Get originalCheck
   * @return originalCheck
   */
  @javax.annotation.Nullable
  public Check getOriginalCheck() {
    return originalCheck;
  }

  public void setOriginalCheck(Check originalCheck) {
    this.originalCheck = originalCheck;
  }


  public ContinuousCheck updateDate(LocalDate updateDate) {
    this.updateDate = updateDate;
    return this;
  }

  /**
   * Continuous check update date in RFC3339 format
   * @return updateDate
   */
  @javax.annotation.Nullable
  public LocalDate getUpdateDate() {
    return updateDate;
  }

  public void setUpdateDate(LocalDate updateDate) {
    this.updateDate = updateDate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ContinuousCheck continuousCheck = (ContinuousCheck) o;
    return Objects.equals(this.continuousCheckID, continuousCheck.continuousCheckID) &&
        Objects.equals(this.continuousCheckStatus, continuousCheck.continuousCheckStatus) &&
        Objects.equals(this.creationDate, continuousCheck.creationDate) &&
        Objects.equals(this.enabled, continuousCheck.enabled) &&
        Objects.equals(this.frequency, continuousCheck.frequency) &&
        Objects.equals(this.history, continuousCheck.history) &&
        Objects.equals(this.lastCheckID, continuousCheck.lastCheckID) &&
        Objects.equals(this.nextRunDate, continuousCheck.nextRunDate) &&
        Objects.equals(this.originalCheck, continuousCheck.originalCheck) &&
        Objects.equals(this.updateDate, continuousCheck.updateDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(continuousCheckID, continuousCheckStatus, creationDate, enabled, frequency, history, lastCheckID, nextRunDate, originalCheck, updateDate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ContinuousCheck {\n");
    sb.append("    continuousCheckID: ").append(toIndentedString(continuousCheckID)).append("\n");
    sb.append("    continuousCheckStatus: ").append(toIndentedString(continuousCheckStatus)).append("\n");
    sb.append("    creationDate: ").append(toIndentedString(creationDate)).append("\n");
    sb.append("    enabled: ").append(toIndentedString(enabled)).append("\n");
    sb.append("    frequency: ").append(toIndentedString(frequency)).append("\n");
    sb.append("    history: ").append(toIndentedString(history)).append("\n");
    sb.append("    lastCheckID: ").append(toIndentedString(lastCheckID)).append("\n");
    sb.append("    nextRunDate: ").append(toIndentedString(nextRunDate)).append("\n");
    sb.append("    originalCheck: ").append(toIndentedString(originalCheck)).append("\n");
    sb.append("    updateDate: ").append(toIndentedString(updateDate)).append("\n");
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
    openapiFields.add("ContinuousCheckID");
    openapiFields.add("ContinuousCheckStatus");
    openapiFields.add("CreationDate");
    openapiFields.add("Enabled");
    openapiFields.add("Frequency");
    openapiFields.add("History");
    openapiFields.add("LastCheckID");
    openapiFields.add("NextRunDate");
    openapiFields.add("OriginalCheck");
    openapiFields.add("UpdateDate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("ContinuousCheckStatus");
    openapiRequiredFields.add("Frequency");
    openapiRequiredFields.add("LastCheckID");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ContinuousCheck
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ContinuousCheck.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ContinuousCheck is not found in the empty JSON string", ContinuousCheck.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ContinuousCheck.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ContinuousCheck` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ContinuousCheck.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("ContinuousCheckID") != null && !jsonObj.get("ContinuousCheckID").isJsonNull()) && !jsonObj.get("ContinuousCheckID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ContinuousCheckID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ContinuousCheckID").toString()));
      }
      if (!jsonObj.get("ContinuousCheckStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ContinuousCheckStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ContinuousCheckStatus").toString()));
      }
      // validate the required field `ContinuousCheckStatus`
      ContinuousCheckStatusEnum.validateJsonElement(jsonObj.get("ContinuousCheckStatus"));
      if (!jsonObj.get("Frequency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Frequency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Frequency").toString()));
      }
      // validate the optional field `History`
      if (jsonObj.get("History") != null && !jsonObj.get("History").isJsonNull()) {
        ContinuousCheckEntry.validateJsonElement(jsonObj.get("History"));
      }
      if (!jsonObj.get("LastCheckID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `LastCheckID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("LastCheckID").toString()));
      }
      // validate the optional field `OriginalCheck`
      if (jsonObj.get("OriginalCheck") != null && !jsonObj.get("OriginalCheck").isJsonNull()) {
        Check.validateJsonElement(jsonObj.get("OriginalCheck"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ContinuousCheck.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ContinuousCheck' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ContinuousCheck> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ContinuousCheck.class));

       return (TypeAdapter<T>) new TypeAdapter<ContinuousCheck>() {
           @Override
           public void write(JsonWriter out, ContinuousCheck value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ContinuousCheck read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ContinuousCheck given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ContinuousCheck
   * @throws IOException if the JSON string is invalid with respect to ContinuousCheck
   */
  public static ContinuousCheck fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ContinuousCheck.class);
  }

  /**
   * Convert an instance of ContinuousCheck to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

