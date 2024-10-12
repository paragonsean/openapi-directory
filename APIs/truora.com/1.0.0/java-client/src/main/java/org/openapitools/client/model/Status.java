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
 * Represents the status of databases used to generate background checks
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:35.353156-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Status {
  /**
   * Background check dataset
   */
  @JsonAdapter(DataSetEnum.Adapter.class)
  public enum DataSetEnum {
    AFFILIATIONS_AND_INSURANCES("affiliations_and_insurances"),
    
    ALERT_IN_MEDIA("alert_in_media"),
    
    BEHAVIOR("behavior"),
    
    BUSINESS_BACKGROUND("business_background"),
    
    CRIMINAL_RECORD("criminal_record"),
    
    DRIVING_LICENSES("driving_licenses"),
    
    INTERNATIONAL_BACKGROUND("international_background"),
    
    LEGAL_BACKGROUND("legal_background"),
    
    PERSONAL_IDENTITY("personal_identity"),
    
    PROFESSIONAL_BACKGROUND("professional_background"),
    
    TRAFFIC_FINES("traffic_fines"),
    
    VEHICLE_INFORMATION("vehicle_information"),
    
    VEHICLE_PERMITS("vehicle_permits"),
    
    TAXES_AND_FINANCES("taxes_and_finances");

    private String value;

    DataSetEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static DataSetEnum fromValue(String value) {
      for (DataSetEnum b : DataSetEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<DataSetEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final DataSetEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public DataSetEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return DataSetEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      DataSetEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_DATA_SET = "data_set";
  @SerializedName(SERIALIZED_NAME_DATA_SET)
  private DataSetEnum dataSet;

  public static final String SERIALIZED_NAME_DATABASE_ID = "database_id";
  @SerializedName(SERIALIZED_NAME_DATABASE_ID)
  private String databaseId;

  public static final String SERIALIZED_NAME_DATABASE_NAME = "database_name";
  @SerializedName(SERIALIZED_NAME_DATABASE_NAME)
  private String databaseName;

  public static final String SERIALIZED_NAME_INVALID_INPUTS = "invalid_inputs";
  @SerializedName(SERIALIZED_NAME_INVALID_INPUTS)
  private List<String> invalidInputs = new ArrayList<>();

  /**
   * Result status of the background check. **Not_started** means the background check is still in queue, since there is a limit of background checks that can be processed simultaneously, **completed** means the search finished successfully, **error** means the search failed, **expired** means the search took too long to finish and therefore failed, **skipped** means the search failed because a wrong number or type of parameters was provided, **delayed** means the search is waiting for an additional requirement to be met and can last up to 3 days
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    NOT_STARTED("not_started"),
    
    COMPLETED("completed"),
    
    EXPIRED("expired"),
    
    ERROR("error"),
    
    DELAYED("delayed"),
    
    SKIPPED("skipped");

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

  public Status() {
  }

  public Status dataSet(DataSetEnum dataSet) {
    this.dataSet = dataSet;
    return this;
  }

  /**
   * Background check dataset
   * @return dataSet
   */
  @javax.annotation.Nullable
  public DataSetEnum getDataSet() {
    return dataSet;
  }

  public void setDataSet(DataSetEnum dataSet) {
    this.dataSet = dataSet;
  }


  public Status databaseId(String databaseId) {
    this.databaseId = databaseId;
    return this;
  }

  /**
   * Database ID. Can be used to verify the database status
   * @return databaseId
   */
  @javax.annotation.Nullable
  public String getDatabaseId() {
    return databaseId;
  }

  public void setDatabaseId(String databaseId) {
    this.databaseId = databaseId;
  }


  public Status databaseName(String databaseName) {
    this.databaseName = databaseName;
    return this;
  }

  /**
   * Background check database name. Do not use this field to identify the database as it may change during the check execution. Use database_id instead
   * @return databaseName
   */
  @javax.annotation.Nullable
  public String getDatabaseName() {
    return databaseName;
  }

  public void setDatabaseName(String databaseName) {
    this.databaseName = databaseName;
  }


  public Status invalidInputs(List<String> invalidInputs) {
    this.invalidInputs = invalidInputs;
    return this;
  }

  public Status addInvalidInputsItem(String invalidInputsItem) {
    if (this.invalidInputs == null) {
      this.invalidInputs = new ArrayList<>();
    }
    this.invalidInputs.add(invalidInputsItem);
    return this;
  }

  /**
   * List of missing or invalid inputs
   * @return invalidInputs
   */
  @javax.annotation.Nullable
  public List<String> getInvalidInputs() {
    return invalidInputs;
  }

  public void setInvalidInputs(List<String> invalidInputs) {
    this.invalidInputs = invalidInputs;
  }


  public Status status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Result status of the background check. **Not_started** means the background check is still in queue, since there is a limit of background checks that can be processed simultaneously, **completed** means the search finished successfully, **error** means the search failed, **expired** means the search took too long to finish and therefore failed, **skipped** means the search failed because a wrong number or type of parameters was provided, **delayed** means the search is waiting for an additional requirement to be met and can last up to 3 days
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
    Status status = (Status) o;
    return Objects.equals(this.dataSet, status.dataSet) &&
        Objects.equals(this.databaseId, status.databaseId) &&
        Objects.equals(this.databaseName, status.databaseName) &&
        Objects.equals(this.invalidInputs, status.invalidInputs) &&
        Objects.equals(this.status, status.status);
  }

  @Override
  public int hashCode() {
    return Objects.hash(dataSet, databaseId, databaseName, invalidInputs, status);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Status {\n");
    sb.append("    dataSet: ").append(toIndentedString(dataSet)).append("\n");
    sb.append("    databaseId: ").append(toIndentedString(databaseId)).append("\n");
    sb.append("    databaseName: ").append(toIndentedString(databaseName)).append("\n");
    sb.append("    invalidInputs: ").append(toIndentedString(invalidInputs)).append("\n");
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
    openapiFields.add("data_set");
    openapiFields.add("database_id");
    openapiFields.add("database_name");
    openapiFields.add("invalid_inputs");
    openapiFields.add("status");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Status
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Status.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Status is not found in the empty JSON string", Status.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Status.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Status` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("data_set") != null && !jsonObj.get("data_set").isJsonNull()) && !jsonObj.get("data_set").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `data_set` to be a primitive type in the JSON string but got `%s`", jsonObj.get("data_set").toString()));
      }
      // validate the optional field `data_set`
      if (jsonObj.get("data_set") != null && !jsonObj.get("data_set").isJsonNull()) {
        DataSetEnum.validateJsonElement(jsonObj.get("data_set"));
      }
      if ((jsonObj.get("database_id") != null && !jsonObj.get("database_id").isJsonNull()) && !jsonObj.get("database_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `database_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("database_id").toString()));
      }
      if ((jsonObj.get("database_name") != null && !jsonObj.get("database_name").isJsonNull()) && !jsonObj.get("database_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `database_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("database_name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("invalid_inputs") != null && !jsonObj.get("invalid_inputs").isJsonNull() && !jsonObj.get("invalid_inputs").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `invalid_inputs` to be an array in the JSON string but got `%s`", jsonObj.get("invalid_inputs").toString()));
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
       if (!Status.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Status' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Status> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Status.class));

       return (TypeAdapter<T>) new TypeAdapter<Status>() {
           @Override
           public void write(JsonWriter out, Status value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Status read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Status given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Status
   * @throws IOException if the JSON string is invalid with respect to Status
   */
  public static Status fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Status.class);
  }

  /**
   * Convert an instance of Status to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

