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
 * Represents the data contained in an API key
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:35.353156-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class APIKey {
  public static final String SERIALIZED_NAME_API_KEY_PREVIOUS_VERSION = "api_key_previous_version";
  @SerializedName(SERIALIZED_NAME_API_KEY_PREVIOUS_VERSION)
  private String apiKeyPreviousVersion;

  public static final String SERIALIZED_NAME_API_KEY_VERSION = "api_key_version";
  @SerializedName(SERIALIZED_NAME_API_KEY_VERSION)
  private String apiKeyVersion;

  public static final String SERIALIZED_NAME_CLIENT_ID = "client_id";
  @SerializedName(SERIALIZED_NAME_CLIENT_ID)
  private String clientId;

  public static final String SERIALIZED_NAME_CREATION_DATE = "creation_date";
  @SerializedName(SERIALIZED_NAME_CREATION_DATE)
  private LocalDate creationDate;

  public static final String SERIALIZED_NAME_EXPIRATION_DATE = "expiration_date";
  @SerializedName(SERIALIZED_NAME_EXPIRATION_DATE)
  private LocalDate expirationDate;

  public static final String SERIALIZED_NAME_KEY_NAME = "key_name";
  @SerializedName(SERIALIZED_NAME_KEY_NAME)
  private String keyName;

  public static final String SERIALIZED_NAME_UPDATE_DATE = "update_date";
  @SerializedName(SERIALIZED_NAME_UPDATE_DATE)
  private LocalDate updateDate;

  public static final String SERIALIZED_NAME_USER_KEY_NAME = "user_key_name";
  @SerializedName(SERIALIZED_NAME_USER_KEY_NAME)
  private String userKeyName;

  public APIKey() {
  }

  public APIKey apiKeyPreviousVersion(String apiKeyPreviousVersion) {
    this.apiKeyPreviousVersion = apiKeyPreviousVersion;
    return this;
  }

  /**
   * Previous version of the API key
   * @return apiKeyPreviousVersion
   */
  @javax.annotation.Nullable
  public String getApiKeyPreviousVersion() {
    return apiKeyPreviousVersion;
  }

  public void setApiKeyPreviousVersion(String apiKeyPreviousVersion) {
    this.apiKeyPreviousVersion = apiKeyPreviousVersion;
  }


  public APIKey apiKeyVersion(String apiKeyVersion) {
    this.apiKeyVersion = apiKeyVersion;
    return this;
  }

  /**
   * API key version
   * @return apiKeyVersion
   */
  @javax.annotation.Nullable
  public String getApiKeyVersion() {
    return apiKeyVersion;
  }

  public void setApiKeyVersion(String apiKeyVersion) {
    this.apiKeyVersion = apiKeyVersion;
  }


  public APIKey clientId(String clientId) {
    this.clientId = clientId;
    return this;
  }

  /**
   * Client ID of the API Key
   * @return clientId
   */
  @javax.annotation.Nullable
  public String getClientId() {
    return clientId;
  }

  public void setClientId(String clientId) {
    this.clientId = clientId;
  }


  public APIKey creationDate(LocalDate creationDate) {
    this.creationDate = creationDate;
    return this;
  }

  /**
   * API key creation date
   * @return creationDate
   */
  @javax.annotation.Nullable
  public LocalDate getCreationDate() {
    return creationDate;
  }

  public void setCreationDate(LocalDate creationDate) {
    this.creationDate = creationDate;
  }


  public APIKey expirationDate(LocalDate expirationDate) {
    this.expirationDate = expirationDate;
    return this;
  }

  /**
   * Expiration date of the API key
   * @return expirationDate
   */
  @javax.annotation.Nullable
  public LocalDate getExpirationDate() {
    return expirationDate;
  }

  public void setExpirationDate(LocalDate expirationDate) {
    this.expirationDate = expirationDate;
  }


  public APIKey keyName(String keyName) {
    this.keyName = keyName;
    return this;
  }

  /**
   * Key name, equals user_key_name normalized
   * @return keyName
   */
  @javax.annotation.Nullable
  public String getKeyName() {
    return keyName;
  }

  public void setKeyName(String keyName) {
    this.keyName = keyName;
  }


  public APIKey updateDate(LocalDate updateDate) {
    this.updateDate = updateDate;
    return this;
  }

  /**
   * Date when the API key version was changed
   * @return updateDate
   */
  @javax.annotation.Nullable
  public LocalDate getUpdateDate() {
    return updateDate;
  }

  public void setUpdateDate(LocalDate updateDate) {
    this.updateDate = updateDate;
  }


  public APIKey userKeyName(String userKeyName) {
    this.userKeyName = userKeyName;
    return this;
  }

  /**
   * User name of the API key
   * @return userKeyName
   */
  @javax.annotation.Nullable
  public String getUserKeyName() {
    return userKeyName;
  }

  public void setUserKeyName(String userKeyName) {
    this.userKeyName = userKeyName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    APIKey apIKey = (APIKey) o;
    return Objects.equals(this.apiKeyPreviousVersion, apIKey.apiKeyPreviousVersion) &&
        Objects.equals(this.apiKeyVersion, apIKey.apiKeyVersion) &&
        Objects.equals(this.clientId, apIKey.clientId) &&
        Objects.equals(this.creationDate, apIKey.creationDate) &&
        Objects.equals(this.expirationDate, apIKey.expirationDate) &&
        Objects.equals(this.keyName, apIKey.keyName) &&
        Objects.equals(this.updateDate, apIKey.updateDate) &&
        Objects.equals(this.userKeyName, apIKey.userKeyName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(apiKeyPreviousVersion, apiKeyVersion, clientId, creationDate, expirationDate, keyName, updateDate, userKeyName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class APIKey {\n");
    sb.append("    apiKeyPreviousVersion: ").append(toIndentedString(apiKeyPreviousVersion)).append("\n");
    sb.append("    apiKeyVersion: ").append(toIndentedString(apiKeyVersion)).append("\n");
    sb.append("    clientId: ").append(toIndentedString(clientId)).append("\n");
    sb.append("    creationDate: ").append(toIndentedString(creationDate)).append("\n");
    sb.append("    expirationDate: ").append(toIndentedString(expirationDate)).append("\n");
    sb.append("    keyName: ").append(toIndentedString(keyName)).append("\n");
    sb.append("    updateDate: ").append(toIndentedString(updateDate)).append("\n");
    sb.append("    userKeyName: ").append(toIndentedString(userKeyName)).append("\n");
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
    openapiFields.add("api_key_previous_version");
    openapiFields.add("api_key_version");
    openapiFields.add("client_id");
    openapiFields.add("creation_date");
    openapiFields.add("expiration_date");
    openapiFields.add("key_name");
    openapiFields.add("update_date");
    openapiFields.add("user_key_name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to APIKey
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!APIKey.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in APIKey is not found in the empty JSON string", APIKey.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!APIKey.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `APIKey` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("api_key_previous_version") != null && !jsonObj.get("api_key_previous_version").isJsonNull()) && !jsonObj.get("api_key_previous_version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `api_key_previous_version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("api_key_previous_version").toString()));
      }
      if ((jsonObj.get("api_key_version") != null && !jsonObj.get("api_key_version").isJsonNull()) && !jsonObj.get("api_key_version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `api_key_version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("api_key_version").toString()));
      }
      if ((jsonObj.get("client_id") != null && !jsonObj.get("client_id").isJsonNull()) && !jsonObj.get("client_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `client_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("client_id").toString()));
      }
      if ((jsonObj.get("key_name") != null && !jsonObj.get("key_name").isJsonNull()) && !jsonObj.get("key_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `key_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("key_name").toString()));
      }
      if ((jsonObj.get("user_key_name") != null && !jsonObj.get("user_key_name").isJsonNull()) && !jsonObj.get("user_key_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `user_key_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("user_key_name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!APIKey.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'APIKey' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<APIKey> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(APIKey.class));

       return (TypeAdapter<T>) new TypeAdapter<APIKey>() {
           @Override
           public void write(JsonWriter out, APIKey value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public APIKey read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of APIKey given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of APIKey
   * @throws IOException if the JSON string is invalid with respect to APIKey
   */
  public static APIKey fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, APIKey.class);
  }

  /**
   * Convert an instance of APIKey to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

