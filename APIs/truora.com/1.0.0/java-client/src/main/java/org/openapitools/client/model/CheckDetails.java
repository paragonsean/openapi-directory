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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Table;

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
 * Represents background check details
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:35.353156-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CheckDetails {
  public static final String SERIALIZED_NAME_CHECK_ID = "check_id";
  @SerializedName(SERIALIZED_NAME_CHECK_ID)
  private String checkId;

  public static final String SERIALIZED_NAME_DATA_SET = "data_set";
  @SerializedName(SERIALIZED_NAME_DATA_SET)
  private String dataSet;

  public static final String SERIALIZED_NAME_DATABASE_NAME = "database_name";
  @SerializedName(SERIALIZED_NAME_DATABASE_NAME)
  private String databaseName;

  /**
   * table group type
   */
  @JsonAdapter(GroupEnum.Adapter.class)
  public enum GroupEnum {
    PROFILE("profile"),
    
    LEGAL("legal"),
    
    AFFILIATIONS("affiliations"),
    
    VEHICLE("vehicle"),
    
    GLOBAL("global"),
    
    MEDIA("media"),
    
    UNKNOWN("unknown");

    private String value;

    GroupEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static GroupEnum fromValue(String value) {
      for (GroupEnum b : GroupEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<GroupEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final GroupEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public GroupEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return GroupEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      GroupEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_GROUP = "group";
  @SerializedName(SERIALIZED_NAME_GROUP)
  private GroupEnum group;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  /**
   * Database result
   */
  @JsonAdapter(ResultEnum.Adapter.class)
  public enum ResultEnum {
    PENDING("pending"),
    
    FOUND("found"),
    
    NOT_FOUND("not_found"),
    
    ERROR("error");

    private String value;

    ResultEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ResultEnum fromValue(String value) {
      for (ResultEnum b : ResultEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ResultEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ResultEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ResultEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ResultEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ResultEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_RESULT = "result";
  @SerializedName(SERIALIZED_NAME_RESULT)
  private ResultEnum result;

  public static final String SERIALIZED_NAME_SCORE = "score";
  @SerializedName(SERIALIZED_NAME_SCORE)
  private BigDecimal score;

  public static final String SERIALIZED_NAME_TABLES = "tables";
  @SerializedName(SERIALIZED_NAME_TABLES)
  private List<Table> tables = new ArrayList<>();

  public CheckDetails() {
  }

  public CheckDetails checkId(String checkId) {
    this.checkId = checkId;
    return this;
  }

  /**
   * Associated background check ID
   * @return checkId
   */
  @javax.annotation.Nonnull
  public String getCheckId() {
    return checkId;
  }

  public void setCheckId(String checkId) {
    this.checkId = checkId;
  }


  public CheckDetails dataSet(String dataSet) {
    this.dataSet = dataSet;
    return this;
  }

  /**
   * Details dataset
   * @return dataSet
   */
  @javax.annotation.Nonnull
  public String getDataSet() {
    return dataSet;
  }

  public void setDataSet(String dataSet) {
    this.dataSet = dataSet;
  }


  public CheckDetails databaseName(String databaseName) {
    this.databaseName = databaseName;
    return this;
  }

  /**
   * Database name. Do not use this field to identify the database as its value may vary as the check is completed
   * @return databaseName
   */
  @javax.annotation.Nonnull
  public String getDatabaseName() {
    return databaseName;
  }

  public void setDatabaseName(String databaseName) {
    this.databaseName = databaseName;
  }


  public CheckDetails group(GroupEnum group) {
    this.group = group;
    return this;
  }

  /**
   * table group type
   * @return group
   */
  @javax.annotation.Nonnull
  public GroupEnum getGroup() {
    return group;
  }

  public void setGroup(GroupEnum group) {
    this.group = group;
  }


  public CheckDetails id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Detail ID
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public CheckDetails result(ResultEnum result) {
    this.result = result;
    return this;
  }

  /**
   * Database result
   * @return result
   */
  @javax.annotation.Nonnull
  public ResultEnum getResult() {
    return result;
  }

  public void setResult(ResultEnum result) {
    this.result = result;
  }


  public CheckDetails score(BigDecimal score) {
    this.score = score;
    return this;
  }

  /**
   * Partial detail score. Scores are aggregated later in the background check
   * @return score
   */
  @javax.annotation.Nonnull
  public BigDecimal getScore() {
    return score;
  }

  public void setScore(BigDecimal score) {
    this.score = score;
  }


  public CheckDetails tables(List<Table> tables) {
    this.tables = tables;
    return this;
  }

  public CheckDetails addTablesItem(Table tablesItem) {
    if (this.tables == null) {
      this.tables = new ArrayList<>();
    }
    this.tables.add(tablesItem);
    return this;
  }

  /**
   * Query detailed information
   * @return tables
   */
  @javax.annotation.Nonnull
  public List<Table> getTables() {
    return tables;
  }

  public void setTables(List<Table> tables) {
    this.tables = tables;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CheckDetails checkDetails = (CheckDetails) o;
    return Objects.equals(this.checkId, checkDetails.checkId) &&
        Objects.equals(this.dataSet, checkDetails.dataSet) &&
        Objects.equals(this.databaseName, checkDetails.databaseName) &&
        Objects.equals(this.group, checkDetails.group) &&
        Objects.equals(this.id, checkDetails.id) &&
        Objects.equals(this.result, checkDetails.result) &&
        Objects.equals(this.score, checkDetails.score) &&
        Objects.equals(this.tables, checkDetails.tables);
  }

  @Override
  public int hashCode() {
    return Objects.hash(checkId, dataSet, databaseName, group, id, result, score, tables);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CheckDetails {\n");
    sb.append("    checkId: ").append(toIndentedString(checkId)).append("\n");
    sb.append("    dataSet: ").append(toIndentedString(dataSet)).append("\n");
    sb.append("    databaseName: ").append(toIndentedString(databaseName)).append("\n");
    sb.append("    group: ").append(toIndentedString(group)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    result: ").append(toIndentedString(result)).append("\n");
    sb.append("    score: ").append(toIndentedString(score)).append("\n");
    sb.append("    tables: ").append(toIndentedString(tables)).append("\n");
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
    openapiFields.add("check_id");
    openapiFields.add("data_set");
    openapiFields.add("database_name");
    openapiFields.add("group");
    openapiFields.add("id");
    openapiFields.add("result");
    openapiFields.add("score");
    openapiFields.add("tables");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("check_id");
    openapiRequiredFields.add("data_set");
    openapiRequiredFields.add("database_name");
    openapiRequiredFields.add("group");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("result");
    openapiRequiredFields.add("score");
    openapiRequiredFields.add("tables");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CheckDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CheckDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CheckDetails is not found in the empty JSON string", CheckDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CheckDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CheckDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CheckDetails.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("check_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `check_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("check_id").toString()));
      }
      if (!jsonObj.get("data_set").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `data_set` to be a primitive type in the JSON string but got `%s`", jsonObj.get("data_set").toString()));
      }
      if (!jsonObj.get("database_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `database_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("database_name").toString()));
      }
      if (!jsonObj.get("group").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `group` to be a primitive type in the JSON string but got `%s`", jsonObj.get("group").toString()));
      }
      // validate the required field `group`
      GroupEnum.validateJsonElement(jsonObj.get("group"));
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("result").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `result` to be a primitive type in the JSON string but got `%s`", jsonObj.get("result").toString()));
      }
      // validate the required field `result`
      ResultEnum.validateJsonElement(jsonObj.get("result"));
      // ensure the json data is an array
      if (!jsonObj.get("tables").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tables` to be an array in the JSON string but got `%s`", jsonObj.get("tables").toString()));
      }

      JsonArray jsonArraytables = jsonObj.getAsJsonArray("tables");
      // validate the required field `tables` (array)
      for (int i = 0; i < jsonArraytables.size(); i++) {
        Table.validateJsonElement(jsonArraytables.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CheckDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CheckDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CheckDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CheckDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<CheckDetails>() {
           @Override
           public void write(JsonWriter out, CheckDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CheckDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CheckDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CheckDetails
   * @throws IOException if the JSON string is invalid with respect to CheckDetails
   */
  public static CheckDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CheckDetails.class);
  }

  /**
   * Convert an instance of CheckDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

