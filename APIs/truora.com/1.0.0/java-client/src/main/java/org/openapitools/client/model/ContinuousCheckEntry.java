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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Change;

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
 * Represents to changelog entry of a continuous check
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:35.353156-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ContinuousCheckEntry {
  public static final String SERIALIZED_NAME_CHANGES = "changes";
  @SerializedName(SERIALIZED_NAME_CHANGES)
  private List<Change> changes = new ArrayList<>();

  public static final String SERIALIZED_NAME_CHECK_ID = "check_id";
  @SerializedName(SERIALIZED_NAME_CHECK_ID)
  private String checkId;

  public static final String SERIALIZED_NAME_CONTINUOUS_CHECK_ID = "continuous_check_id";
  @SerializedName(SERIALIZED_NAME_CONTINUOUS_CHECK_ID)
  private String continuousCheckId;

  public static final String SERIALIZED_NAME_CREATION_DATE = "creation_date";
  @SerializedName(SERIALIZED_NAME_CREATION_DATE)
  private LocalDate creationDate;

  public static final String SERIALIZED_NAME_PREVIOUS_CHECK_ID = "previous_check_id";
  @SerializedName(SERIALIZED_NAME_PREVIOUS_CHECK_ID)
  private String previousCheckId;

  public ContinuousCheckEntry() {
  }

  public ContinuousCheckEntry changes(List<Change> changes) {
    this.changes = changes;
    return this;
  }

  public ContinuousCheckEntry addChangesItem(Change changesItem) {
    if (this.changes == null) {
      this.changes = new ArrayList<>();
    }
    this.changes.add(changesItem);
    return this;
  }

  /**
   * Change list of background check scores
   * @return changes
   */
  @javax.annotation.Nullable
  public List<Change> getChanges() {
    return changes;
  }

  public void setChanges(List<Change> changes) {
    this.changes = changes;
  }


  public ContinuousCheckEntry checkId(String checkId) {
    this.checkId = checkId;
    return this;
  }

  /**
   * Check ID
   * @return checkId
   */
  @javax.annotation.Nullable
  public String getCheckId() {
    return checkId;
  }

  public void setCheckId(String checkId) {
    this.checkId = checkId;
  }


  public ContinuousCheckEntry continuousCheckId(String continuousCheckId) {
    this.continuousCheckId = continuousCheckId;
    return this;
  }

  /**
   * Continuous check ID
   * @return continuousCheckId
   */
  @javax.annotation.Nullable
  public String getContinuousCheckId() {
    return continuousCheckId;
  }

  public void setContinuousCheckId(String continuousCheckId) {
    this.continuousCheckId = continuousCheckId;
  }


  public ContinuousCheckEntry creationDate(LocalDate creationDate) {
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


  public ContinuousCheckEntry previousCheckId(String previousCheckId) {
    this.previousCheckId = previousCheckId;
    return this;
  }

  /**
   * Previous check ID
   * @return previousCheckId
   */
  @javax.annotation.Nullable
  public String getPreviousCheckId() {
    return previousCheckId;
  }

  public void setPreviousCheckId(String previousCheckId) {
    this.previousCheckId = previousCheckId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ContinuousCheckEntry continuousCheckEntry = (ContinuousCheckEntry) o;
    return Objects.equals(this.changes, continuousCheckEntry.changes) &&
        Objects.equals(this.checkId, continuousCheckEntry.checkId) &&
        Objects.equals(this.continuousCheckId, continuousCheckEntry.continuousCheckId) &&
        Objects.equals(this.creationDate, continuousCheckEntry.creationDate) &&
        Objects.equals(this.previousCheckId, continuousCheckEntry.previousCheckId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(changes, checkId, continuousCheckId, creationDate, previousCheckId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ContinuousCheckEntry {\n");
    sb.append("    changes: ").append(toIndentedString(changes)).append("\n");
    sb.append("    checkId: ").append(toIndentedString(checkId)).append("\n");
    sb.append("    continuousCheckId: ").append(toIndentedString(continuousCheckId)).append("\n");
    sb.append("    creationDate: ").append(toIndentedString(creationDate)).append("\n");
    sb.append("    previousCheckId: ").append(toIndentedString(previousCheckId)).append("\n");
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
    openapiFields.add("changes");
    openapiFields.add("check_id");
    openapiFields.add("continuous_check_id");
    openapiFields.add("creation_date");
    openapiFields.add("previous_check_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ContinuousCheckEntry
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ContinuousCheckEntry.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ContinuousCheckEntry is not found in the empty JSON string", ContinuousCheckEntry.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ContinuousCheckEntry.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ContinuousCheckEntry` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("changes") != null && !jsonObj.get("changes").isJsonNull()) {
        JsonArray jsonArraychanges = jsonObj.getAsJsonArray("changes");
        if (jsonArraychanges != null) {
          // ensure the json data is an array
          if (!jsonObj.get("changes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `changes` to be an array in the JSON string but got `%s`", jsonObj.get("changes").toString()));
          }

          // validate the optional field `changes` (array)
          for (int i = 0; i < jsonArraychanges.size(); i++) {
            Change.validateJsonElement(jsonArraychanges.get(i));
          };
        }
      }
      if ((jsonObj.get("check_id") != null && !jsonObj.get("check_id").isJsonNull()) && !jsonObj.get("check_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `check_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("check_id").toString()));
      }
      if ((jsonObj.get("continuous_check_id") != null && !jsonObj.get("continuous_check_id").isJsonNull()) && !jsonObj.get("continuous_check_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `continuous_check_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("continuous_check_id").toString()));
      }
      if ((jsonObj.get("previous_check_id") != null && !jsonObj.get("previous_check_id").isJsonNull()) && !jsonObj.get("previous_check_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `previous_check_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("previous_check_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ContinuousCheckEntry.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ContinuousCheckEntry' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ContinuousCheckEntry> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ContinuousCheckEntry.class));

       return (TypeAdapter<T>) new TypeAdapter<ContinuousCheckEntry>() {
           @Override
           public void write(JsonWriter out, ContinuousCheckEntry value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ContinuousCheckEntry read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ContinuousCheckEntry given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ContinuousCheckEntry
   * @throws IOException if the JSON string is invalid with respect to ContinuousCheckEntry
   */
  public static ContinuousCheckEntry fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ContinuousCheckEntry.class);
  }

  /**
   * Convert an instance of ContinuousCheckEntry to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

