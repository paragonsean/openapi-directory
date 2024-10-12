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
 * Represents changes made to a API key version
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:35.353156-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class APIKeyVersionChangelog {
  public static final String SERIALIZED_NAME_ADDED = "added";
  @SerializedName(SERIALIZED_NAME_ADDED)
  private List<String> added = new ArrayList<>();

  public static final String SERIALIZED_NAME_CHANGED = "changed";
  @SerializedName(SERIALIZED_NAME_CHANGED)
  private List<String> changed = new ArrayList<>();

  public static final String SERIALIZED_NAME_DEPRECATED = "deprecated";
  @SerializedName(SERIALIZED_NAME_DEPRECATED)
  private List<String> deprecated = new ArrayList<>();

  public static final String SERIALIZED_NAME_FIXED = "fixed";
  @SerializedName(SERIALIZED_NAME_FIXED)
  private List<String> fixed = new ArrayList<>();

  public static final String SERIALIZED_NAME_NOTES = "notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_REMOVED = "removed";
  @SerializedName(SERIALIZED_NAME_REMOVED)
  private List<String> removed = new ArrayList<>();

  public static final String SERIALIZED_NAME_SECURITY = "security";
  @SerializedName(SERIALIZED_NAME_SECURITY)
  private List<String> security = new ArrayList<>();

  public APIKeyVersionChangelog() {
  }

  public APIKeyVersionChangelog added(List<String> added) {
    this.added = added;
    return this;
  }

  public APIKeyVersionChangelog addAddedItem(String addedItem) {
    if (this.added == null) {
      this.added = new ArrayList<>();
    }
    this.added.add(addedItem);
    return this;
  }

  /**
   * List of added features
   * @return added
   */
  @javax.annotation.Nullable
  public List<String> getAdded() {
    return added;
  }

  public void setAdded(List<String> added) {
    this.added = added;
  }


  public APIKeyVersionChangelog changed(List<String> changed) {
    this.changed = changed;
    return this;
  }

  public APIKeyVersionChangelog addChangedItem(String changedItem) {
    if (this.changed == null) {
      this.changed = new ArrayList<>();
    }
    this.changed.add(changedItem);
    return this;
  }

  /**
   * List of changed features
   * @return changed
   */
  @javax.annotation.Nullable
  public List<String> getChanged() {
    return changed;
  }

  public void setChanged(List<String> changed) {
    this.changed = changed;
  }


  public APIKeyVersionChangelog deprecated(List<String> deprecated) {
    this.deprecated = deprecated;
    return this;
  }

  public APIKeyVersionChangelog addDeprecatedItem(String deprecatedItem) {
    if (this.deprecated == null) {
      this.deprecated = new ArrayList<>();
    }
    this.deprecated.add(deprecatedItem);
    return this;
  }

  /**
   * List of deprecated features
   * @return deprecated
   */
  @javax.annotation.Nullable
  public List<String> getDeprecated() {
    return deprecated;
  }

  public void setDeprecated(List<String> deprecated) {
    this.deprecated = deprecated;
  }


  public APIKeyVersionChangelog fixed(List<String> fixed) {
    this.fixed = fixed;
    return this;
  }

  public APIKeyVersionChangelog addFixedItem(String fixedItem) {
    if (this.fixed == null) {
      this.fixed = new ArrayList<>();
    }
    this.fixed.add(fixedItem);
    return this;
  }

  /**
   * List of fixed features
   * @return fixed
   */
  @javax.annotation.Nullable
  public List<String> getFixed() {
    return fixed;
  }

  public void setFixed(List<String> fixed) {
    this.fixed = fixed;
  }


  public APIKeyVersionChangelog notes(String notes) {
    this.notes = notes;
    return this;
  }

  /**
   * Additional notes
   * @return notes
   */
  @javax.annotation.Nullable
  public String getNotes() {
    return notes;
  }

  public void setNotes(String notes) {
    this.notes = notes;
  }


  public APIKeyVersionChangelog removed(List<String> removed) {
    this.removed = removed;
    return this;
  }

  public APIKeyVersionChangelog addRemovedItem(String removedItem) {
    if (this.removed == null) {
      this.removed = new ArrayList<>();
    }
    this.removed.add(removedItem);
    return this;
  }

  /**
   * List of removed features
   * @return removed
   */
  @javax.annotation.Nullable
  public List<String> getRemoved() {
    return removed;
  }

  public void setRemoved(List<String> removed) {
    this.removed = removed;
  }


  public APIKeyVersionChangelog security(List<String> security) {
    this.security = security;
    return this;
  }

  public APIKeyVersionChangelog addSecurityItem(String securityItem) {
    if (this.security == null) {
      this.security = new ArrayList<>();
    }
    this.security.add(securityItem);
    return this;
  }

  /**
   * List of security features added
   * @return security
   */
  @javax.annotation.Nullable
  public List<String> getSecurity() {
    return security;
  }

  public void setSecurity(List<String> security) {
    this.security = security;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    APIKeyVersionChangelog apIKeyVersionChangelog = (APIKeyVersionChangelog) o;
    return Objects.equals(this.added, apIKeyVersionChangelog.added) &&
        Objects.equals(this.changed, apIKeyVersionChangelog.changed) &&
        Objects.equals(this.deprecated, apIKeyVersionChangelog.deprecated) &&
        Objects.equals(this.fixed, apIKeyVersionChangelog.fixed) &&
        Objects.equals(this.notes, apIKeyVersionChangelog.notes) &&
        Objects.equals(this.removed, apIKeyVersionChangelog.removed) &&
        Objects.equals(this.security, apIKeyVersionChangelog.security);
  }

  @Override
  public int hashCode() {
    return Objects.hash(added, changed, deprecated, fixed, notes, removed, security);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class APIKeyVersionChangelog {\n");
    sb.append("    added: ").append(toIndentedString(added)).append("\n");
    sb.append("    changed: ").append(toIndentedString(changed)).append("\n");
    sb.append("    deprecated: ").append(toIndentedString(deprecated)).append("\n");
    sb.append("    fixed: ").append(toIndentedString(fixed)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    removed: ").append(toIndentedString(removed)).append("\n");
    sb.append("    security: ").append(toIndentedString(security)).append("\n");
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
    openapiFields.add("added");
    openapiFields.add("changed");
    openapiFields.add("deprecated");
    openapiFields.add("fixed");
    openapiFields.add("notes");
    openapiFields.add("removed");
    openapiFields.add("security");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to APIKeyVersionChangelog
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!APIKeyVersionChangelog.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in APIKeyVersionChangelog is not found in the empty JSON string", APIKeyVersionChangelog.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!APIKeyVersionChangelog.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `APIKeyVersionChangelog` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("added") != null && !jsonObj.get("added").isJsonNull() && !jsonObj.get("added").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `added` to be an array in the JSON string but got `%s`", jsonObj.get("added").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("changed") != null && !jsonObj.get("changed").isJsonNull() && !jsonObj.get("changed").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `changed` to be an array in the JSON string but got `%s`", jsonObj.get("changed").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("deprecated") != null && !jsonObj.get("deprecated").isJsonNull() && !jsonObj.get("deprecated").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `deprecated` to be an array in the JSON string but got `%s`", jsonObj.get("deprecated").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("fixed") != null && !jsonObj.get("fixed").isJsonNull() && !jsonObj.get("fixed").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `fixed` to be an array in the JSON string but got `%s`", jsonObj.get("fixed").toString()));
      }
      if ((jsonObj.get("notes") != null && !jsonObj.get("notes").isJsonNull()) && !jsonObj.get("notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("notes").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("removed") != null && !jsonObj.get("removed").isJsonNull() && !jsonObj.get("removed").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `removed` to be an array in the JSON string but got `%s`", jsonObj.get("removed").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("security") != null && !jsonObj.get("security").isJsonNull() && !jsonObj.get("security").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `security` to be an array in the JSON string but got `%s`", jsonObj.get("security").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!APIKeyVersionChangelog.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'APIKeyVersionChangelog' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<APIKeyVersionChangelog> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(APIKeyVersionChangelog.class));

       return (TypeAdapter<T>) new TypeAdapter<APIKeyVersionChangelog>() {
           @Override
           public void write(JsonWriter out, APIKeyVersionChangelog value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public APIKeyVersionChangelog read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of APIKeyVersionChangelog given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of APIKeyVersionChangelog
   * @throws IOException if the JSON string is invalid with respect to APIKeyVersionChangelog
   */
  public static APIKeyVersionChangelog fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, APIKeyVersionChangelog.class);
  }

  /**
   * Convert an instance of APIKeyVersionChangelog to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

