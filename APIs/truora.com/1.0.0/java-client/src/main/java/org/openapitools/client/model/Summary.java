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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.NameFound;

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
 * Represents a background check summary
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:35.353156-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Summary {
  public static final String SERIALIZED_NAME_DATE_OF_BIRTH = "date_of_birth";
  @SerializedName(SERIALIZED_NAME_DATE_OF_BIRTH)
  private OffsetDateTime dateOfBirth;

  public static final String SERIALIZED_NAME_DEATH_DATE = "death_date";
  @SerializedName(SERIALIZED_NAME_DEATH_DATE)
  private OffsetDateTime deathDate;

  public static final String SERIALIZED_NAME_DRIVERS_LICENSE = "drivers_license";
  @SerializedName(SERIALIZED_NAME_DRIVERS_LICENSE)
  private String driversLicense;

  /**
   * Person gender
   */
  @JsonAdapter(GenderEnum.Adapter.class)
  public enum GenderEnum {
    MALE("male"),
    
    FEMALE("female");

    private String value;

    GenderEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static GenderEnum fromValue(String value) {
      for (GenderEnum b : GenderEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<GenderEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final GenderEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public GenderEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return GenderEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      GenderEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_GENDER = "gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private GenderEnum gender;

  /**
   * Indicates whether a person was found, found as dead or not found at all
   */
  @JsonAdapter(IdentityStatusEnum.Adapter.class)
  public enum IdentityStatusEnum {
    FOUND("found"),
    
    NOT_FOUND("not_found"),
    
    DEAD("dead");

    private String value;

    IdentityStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static IdentityStatusEnum fromValue(String value) {
      for (IdentityStatusEnum b : IdentityStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<IdentityStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final IdentityStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public IdentityStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return IdentityStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      IdentityStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_IDENTITY_STATUS = "identity_status";
  @SerializedName(SERIALIZED_NAME_IDENTITY_STATUS)
  private IdentityStatusEnum identityStatus;

  public static final String SERIALIZED_NAME_NAMES_FOUND = "names_found";
  @SerializedName(SERIALIZED_NAME_NAMES_FOUND)
  private List<NameFound> namesFound = new ArrayList<>();

  public static final String SERIALIZED_NAME_NSS = "nss";
  @SerializedName(SERIALIZED_NAME_NSS)
  private String nss;

  public static final String SERIALIZED_NAME_RFC = "rfc";
  @SerializedName(SERIALIZED_NAME_RFC)
  private String rfc;

  public Summary() {
  }

  public Summary dateOfBirth(OffsetDateTime dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
    return this;
  }

  /**
   * Person date of birth in RFC3339 format
   * @return dateOfBirth
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateOfBirth() {
    return dateOfBirth;
  }

  public void setDateOfBirth(OffsetDateTime dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
  }


  public Summary deathDate(OffsetDateTime deathDate) {
    this.deathDate = deathDate;
    return this;
  }

  /**
   * Person date of death
   * @return deathDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDeathDate() {
    return deathDate;
  }

  public void setDeathDate(OffsetDateTime deathDate) {
    this.deathDate = deathDate;
  }


  public Summary driversLicense(String driversLicense) {
    this.driversLicense = driversLicense;
    return this;
  }

  /**
   * Person driver&#39;s license
   * @return driversLicense
   */
  @javax.annotation.Nullable
  public String getDriversLicense() {
    return driversLicense;
  }

  public void setDriversLicense(String driversLicense) {
    this.driversLicense = driversLicense;
  }


  public Summary gender(GenderEnum gender) {
    this.gender = gender;
    return this;
  }

  /**
   * Person gender
   * @return gender
   */
  @javax.annotation.Nullable
  public GenderEnum getGender() {
    return gender;
  }

  public void setGender(GenderEnum gender) {
    this.gender = gender;
  }


  public Summary identityStatus(IdentityStatusEnum identityStatus) {
    this.identityStatus = identityStatus;
    return this;
  }

  /**
   * Indicates whether a person was found, found as dead or not found at all
   * @return identityStatus
   */
  @javax.annotation.Nullable
  public IdentityStatusEnum getIdentityStatus() {
    return identityStatus;
  }

  public void setIdentityStatus(IdentityStatusEnum identityStatus) {
    this.identityStatus = identityStatus;
  }


  public Summary namesFound(List<NameFound> namesFound) {
    this.namesFound = namesFound;
    return this;
  }

  public Summary addNamesFoundItem(NameFound namesFoundItem) {
    if (this.namesFound == null) {
      this.namesFound = new ArrayList<>();
    }
    this.namesFound.add(namesFoundItem);
    return this;
  }

  /**
   * Names found during the background check process
   * @return namesFound
   */
  @javax.annotation.Nonnull
  public List<NameFound> getNamesFound() {
    return namesFound;
  }

  public void setNamesFound(List<NameFound> namesFound) {
    this.namesFound = namesFound;
  }


  public Summary nss(String nss) {
    this.nss = nss;
    return this;
  }

  /**
   * Social security number of the person (Mexico)
   * @return nss
   */
  @javax.annotation.Nullable
  public String getNss() {
    return nss;
  }

  public void setNss(String nss) {
    this.nss = nss;
  }


  public Summary rfc(String rfc) {
    this.rfc = rfc;
    return this;
  }

  /**
   * Federal taxpayer registration number of the person
   * @return rfc
   */
  @javax.annotation.Nullable
  public String getRfc() {
    return rfc;
  }

  public void setRfc(String rfc) {
    this.rfc = rfc;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Summary summary = (Summary) o;
    return Objects.equals(this.dateOfBirth, summary.dateOfBirth) &&
        Objects.equals(this.deathDate, summary.deathDate) &&
        Objects.equals(this.driversLicense, summary.driversLicense) &&
        Objects.equals(this.gender, summary.gender) &&
        Objects.equals(this.identityStatus, summary.identityStatus) &&
        Objects.equals(this.namesFound, summary.namesFound) &&
        Objects.equals(this.nss, summary.nss) &&
        Objects.equals(this.rfc, summary.rfc);
  }

  @Override
  public int hashCode() {
    return Objects.hash(dateOfBirth, deathDate, driversLicense, gender, identityStatus, namesFound, nss, rfc);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Summary {\n");
    sb.append("    dateOfBirth: ").append(toIndentedString(dateOfBirth)).append("\n");
    sb.append("    deathDate: ").append(toIndentedString(deathDate)).append("\n");
    sb.append("    driversLicense: ").append(toIndentedString(driversLicense)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    identityStatus: ").append(toIndentedString(identityStatus)).append("\n");
    sb.append("    namesFound: ").append(toIndentedString(namesFound)).append("\n");
    sb.append("    nss: ").append(toIndentedString(nss)).append("\n");
    sb.append("    rfc: ").append(toIndentedString(rfc)).append("\n");
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
    openapiFields.add("date_of_birth");
    openapiFields.add("death_date");
    openapiFields.add("drivers_license");
    openapiFields.add("gender");
    openapiFields.add("identity_status");
    openapiFields.add("names_found");
    openapiFields.add("nss");
    openapiFields.add("rfc");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("names_found");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Summary
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Summary.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Summary is not found in the empty JSON string", Summary.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Summary.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Summary` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Summary.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("drivers_license") != null && !jsonObj.get("drivers_license").isJsonNull()) && !jsonObj.get("drivers_license").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `drivers_license` to be a primitive type in the JSON string but got `%s`", jsonObj.get("drivers_license").toString()));
      }
      if ((jsonObj.get("gender") != null && !jsonObj.get("gender").isJsonNull()) && !jsonObj.get("gender").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gender` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gender").toString()));
      }
      // validate the optional field `gender`
      if (jsonObj.get("gender") != null && !jsonObj.get("gender").isJsonNull()) {
        GenderEnum.validateJsonElement(jsonObj.get("gender"));
      }
      if ((jsonObj.get("identity_status") != null && !jsonObj.get("identity_status").isJsonNull()) && !jsonObj.get("identity_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `identity_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("identity_status").toString()));
      }
      // validate the optional field `identity_status`
      if (jsonObj.get("identity_status") != null && !jsonObj.get("identity_status").isJsonNull()) {
        IdentityStatusEnum.validateJsonElement(jsonObj.get("identity_status"));
      }
      // ensure the json data is an array
      if (!jsonObj.get("names_found").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `names_found` to be an array in the JSON string but got `%s`", jsonObj.get("names_found").toString()));
      }

      JsonArray jsonArraynamesFound = jsonObj.getAsJsonArray("names_found");
      // validate the required field `names_found` (array)
      for (int i = 0; i < jsonArraynamesFound.size(); i++) {
        NameFound.validateJsonElement(jsonArraynamesFound.get(i));
      };
      if ((jsonObj.get("nss") != null && !jsonObj.get("nss").isJsonNull()) && !jsonObj.get("nss").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nss` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nss").toString()));
      }
      if ((jsonObj.get("rfc") != null && !jsonObj.get("rfc").isJsonNull()) && !jsonObj.get("rfc").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rfc` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rfc").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Summary.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Summary' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Summary> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Summary.class));

       return (TypeAdapter<T>) new TypeAdapter<Summary>() {
           @Override
           public void write(JsonWriter out, Summary value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Summary read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Summary given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Summary
   * @throws IOException if the JSON string is invalid with respect to Summary
   */
  public static Summary fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Summary.class);
  }

  /**
   * Convert an instance of Summary to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

