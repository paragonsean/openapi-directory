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
 * Represents a database as well as an hourly status
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:35.353156-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Database {
  public static final String SERIALIZED_NAME_DATA_SETS = "data_sets";
  @SerializedName(SERIALIZED_NAME_DATA_SETS)
  private List<String> dataSets = new ArrayList<>();

  public static final String SERIALIZED_NAME_DATABASE_ID = "database_id";
  @SerializedName(SERIALIZED_NAME_DATABASE_ID)
  private String databaseId;

  public static final String SERIALIZED_NAME_DATABASE_NAME = "database_name";
  @SerializedName(SERIALIZED_NAME_DATABASE_NAME)
  private String databaseName;

  public static final String SERIALIZED_NAME_HOURLY_STATUS = "hourly_status";
  @SerializedName(SERIALIZED_NAME_HOURLY_STATUS)
  private List<String> hourlyStatus = new ArrayList<>();

  public Database() {
  }

  public Database dataSets(List<String> dataSets) {
    this.dataSets = dataSets;
    return this;
  }

  public Database addDataSetsItem(String dataSetsItem) {
    if (this.dataSets == null) {
      this.dataSets = new ArrayList<>();
    }
    this.dataSets.add(dataSetsItem);
    return this;
  }

  /**
   * List of data sets fed by the database. It can contain &#x60;&#x60;affiliations_and_insurances&#x60;&#x60;, &#x60;&#x60;alert_in:media&#x60;&#x60;, &#x60;&#x60;business_background&#x60;&#x60;, &#x60;&#x60;criminal_record&#x60;&#x60;, &#x60;&#x60;driving_licenses&#x60;&#x60;, &#x60;&#x60;international_background&#x60;&#x60;, &#x60;&#x60;legal_background&#x60;&#x60;, &#x60;&#x60;personal_identity&#x60;&#x60;, &#x60;&#x60;permiso_de_circulación_covid-19&#x60;&#x60;, &#x60;&#x60;professional_background&#x60;&#x60;, &#x60;&#x60;traffic_fines&#x60;&#x60;, &#x60;&#x60;vehicle_information&#x60;&#x60;, &#x60;&#x60;vehicle_permits&#x60;&#x60;, &#x60;&#x60;behaviour_and_reputation&#x60;&#x60;, or &#x60;&#x60;taxes_and_finances&#x60;&#x60;
   * @return dataSets
   */
  @javax.annotation.Nullable
  public List<String> getDataSets() {
    return dataSets;
  }

  public void setDataSets(List<String> dataSets) {
    this.dataSets = dataSets;
  }


  public Database databaseId(String databaseId) {
    this.databaseId = databaseId;
    return this;
  }

  /**
   * Database identifier
   * @return databaseId
   */
  @javax.annotation.Nullable
  public String getDatabaseId() {
    return databaseId;
  }

  public void setDatabaseId(String databaseId) {
    this.databaseId = databaseId;
  }


  public Database databaseName(String databaseName) {
    this.databaseName = databaseName;
    return this;
  }

  /**
   * Database name. Do not use this field to identify the database as it might change, use database_id instead
   * @return databaseName
   */
  @javax.annotation.Nullable
  public String getDatabaseName() {
    return databaseName;
  }

  public void setDatabaseName(String databaseName) {
    this.databaseName = databaseName;
  }


  public Database hourlyStatus(List<String> hourlyStatus) {
    this.hourlyStatus = hourlyStatus;
    return this;
  }

  public Database addHourlyStatusItem(String hourlyStatusItem) {
    if (this.hourlyStatus == null) {
      this.hourlyStatus = new ArrayList<>();
    }
    this.hourlyStatus.add(hourlyStatusItem);
    return this;
  }

  /**
   * An hourly list of the database statuses. The &#x60;&#x60;operational&#x60;&#x60; status means the database executions were at least 90% successful, &#x60;&#x60;degraded_performance&#x60;&#x60; means the database executions were from 50 to 90% successful, &#x60;&#x60;partial_outage&#x60;&#x60; means the database executions were from 10 to 50% sucessful, &#x60;&#x60;major_outage&#x60;&#x60; means the database executions were under 10% successful. &#x60;&#x60;under_maintenance&#x60;&#x60; means the database is temporarily out of service for maintenance, &#x60;&#x60;deprecated&#x60;&#x60; means the database is permanently out of service, &#x60;&#x60;undetermined&#x60;&#x60; means there was no enough data to assess the database status
   * @return hourlyStatus
   */
  @javax.annotation.Nullable
  public List<String> getHourlyStatus() {
    return hourlyStatus;
  }

  public void setHourlyStatus(List<String> hourlyStatus) {
    this.hourlyStatus = hourlyStatus;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Database database = (Database) o;
    return Objects.equals(this.dataSets, database.dataSets) &&
        Objects.equals(this.databaseId, database.databaseId) &&
        Objects.equals(this.databaseName, database.databaseName) &&
        Objects.equals(this.hourlyStatus, database.hourlyStatus);
  }

  @Override
  public int hashCode() {
    return Objects.hash(dataSets, databaseId, databaseName, hourlyStatus);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Database {\n");
    sb.append("    dataSets: ").append(toIndentedString(dataSets)).append("\n");
    sb.append("    databaseId: ").append(toIndentedString(databaseId)).append("\n");
    sb.append("    databaseName: ").append(toIndentedString(databaseName)).append("\n");
    sb.append("    hourlyStatus: ").append(toIndentedString(hourlyStatus)).append("\n");
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
    openapiFields.add("data_sets");
    openapiFields.add("database_id");
    openapiFields.add("database_name");
    openapiFields.add("hourly_status");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Database
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Database.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Database is not found in the empty JSON string", Database.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Database.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Database` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("data_sets") != null && !jsonObj.get("data_sets").isJsonNull() && !jsonObj.get("data_sets").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `data_sets` to be an array in the JSON string but got `%s`", jsonObj.get("data_sets").toString()));
      }
      if ((jsonObj.get("database_id") != null && !jsonObj.get("database_id").isJsonNull()) && !jsonObj.get("database_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `database_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("database_id").toString()));
      }
      if ((jsonObj.get("database_name") != null && !jsonObj.get("database_name").isJsonNull()) && !jsonObj.get("database_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `database_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("database_name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("hourly_status") != null && !jsonObj.get("hourly_status").isJsonNull() && !jsonObj.get("hourly_status").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `hourly_status` to be an array in the JSON string but got `%s`", jsonObj.get("hourly_status").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Database.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Database' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Database> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Database.class));

       return (TypeAdapter<T>) new TypeAdapter<Database>() {
           @Override
           public void write(JsonWriter out, Database value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Database read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Database given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Database
   * @throws IOException if the JSON string is invalid with respect to Database
   */
  public static Database fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Database.class);
  }

  /**
   * Convert an instance of Database to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

