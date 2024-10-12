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
 * Represents the summary of a vehicle background check
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:35.353156-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VehicleSummary {
  public static final String SERIALIZED_NAME_CAPACITY = "capacity";
  @SerializedName(SERIALIZED_NAME_CAPACITY)
  private Integer capacity;

  public static final String SERIALIZED_NAME_COLOR = "color";
  @SerializedName(SERIALIZED_NAME_COLOR)
  private String color;

  public static final String SERIALIZED_NAME_LICENSE_PLATE = "license_plate";
  @SerializedName(SERIALIZED_NAME_LICENSE_PLATE)
  private String licensePlate;

  public static final String SERIALIZED_NAME_MANUFACTURER = "manufacturer";
  @SerializedName(SERIALIZED_NAME_MANUFACTURER)
  private String manufacturer;

  public static final String SERIALIZED_NAME_MODEL = "model";
  @SerializedName(SERIALIZED_NAME_MODEL)
  private String model;

  public static final String SERIALIZED_NAME_NUMBER_OF_DOORS = "number_of_doors";
  @SerializedName(SERIALIZED_NAME_NUMBER_OF_DOORS)
  private Integer numberOfDoors;

  public static final String SERIALIZED_NAME_OBLIGATORY_INSURANCE_EXPIRATION_DATE = "obligatory_insurance_expiration_date";
  @SerializedName(SERIALIZED_NAME_OBLIGATORY_INSURANCE_EXPIRATION_DATE)
  private LocalDate obligatoryInsuranceExpirationDate;

  public static final String SERIALIZED_NAME_OBLIGATORY_INSURANCE_STATUS = "obligatory_insurance_status";
  @SerializedName(SERIALIZED_NAME_OBLIGATORY_INSURANCE_STATUS)
  private String obligatoryInsuranceStatus;

  public static final String SERIALIZED_NAME_SERVICE_TYPE = "service_type";
  @SerializedName(SERIALIZED_NAME_SERVICE_TYPE)
  private String serviceType;

  public static final String SERIALIZED_NAME_VEHICLE_CATEGORY = "vehicle_category";
  @SerializedName(SERIALIZED_NAME_VEHICLE_CATEGORY)
  private String vehicleCategory;

  public static final String SERIALIZED_NAME_VEHICLE_ID = "vehicle_id";
  @SerializedName(SERIALIZED_NAME_VEHICLE_ID)
  private String vehicleId;

  public static final String SERIALIZED_NAME_VEHICLE_TYPE = "vehicle_type";
  @SerializedName(SERIALIZED_NAME_VEHICLE_TYPE)
  private String vehicleType;

  public static final String SERIALIZED_NAME_YEAR = "year";
  @SerializedName(SERIALIZED_NAME_YEAR)
  private Integer year;

  public VehicleSummary() {
  }

  public VehicleSummary capacity(Integer capacity) {
    this.capacity = capacity;
    return this;
  }

  /**
   * Number of passengers allowed to travel in the vehicle
   * @return capacity
   */
  @javax.annotation.Nullable
  public Integer getCapacity() {
    return capacity;
  }

  public void setCapacity(Integer capacity) {
    this.capacity = capacity;
  }


  public VehicleSummary color(String color) {
    this.color = color;
    return this;
  }

  /**
   * Vehicle color
   * @return color
   */
  @javax.annotation.Nullable
  public String getColor() {
    return color;
  }

  public void setColor(String color) {
    this.color = color;
  }


  public VehicleSummary licensePlate(String licensePlate) {
    this.licensePlate = licensePlate;
    return this;
  }

  /**
   * Vehicle license plate
   * @return licensePlate
   */
  @javax.annotation.Nullable
  public String getLicensePlate() {
    return licensePlate;
  }

  public void setLicensePlate(String licensePlate) {
    this.licensePlate = licensePlate;
  }


  public VehicleSummary manufacturer(String manufacturer) {
    this.manufacturer = manufacturer;
    return this;
  }

  /**
   * Vehicle manufacturer
   * @return manufacturer
   */
  @javax.annotation.Nullable
  public String getManufacturer() {
    return manufacturer;
  }

  public void setManufacturer(String manufacturer) {
    this.manufacturer = manufacturer;
  }


  public VehicleSummary model(String model) {
    this.model = model;
    return this;
  }

  /**
   * Vehicle model
   * @return model
   */
  @javax.annotation.Nullable
  public String getModel() {
    return model;
  }

  public void setModel(String model) {
    this.model = model;
  }


  public VehicleSummary numberOfDoors(Integer numberOfDoors) {
    this.numberOfDoors = numberOfDoors;
    return this;
  }

  /**
   * Vehicle door count
   * @return numberOfDoors
   */
  @javax.annotation.Nullable
  public Integer getNumberOfDoors() {
    return numberOfDoors;
  }

  public void setNumberOfDoors(Integer numberOfDoors) {
    this.numberOfDoors = numberOfDoors;
  }


  public VehicleSummary obligatoryInsuranceExpirationDate(LocalDate obligatoryInsuranceExpirationDate) {
    this.obligatoryInsuranceExpirationDate = obligatoryInsuranceExpirationDate;
    return this;
  }

  /**
   * Expiration date of the vehicle compulsory insurance 
   * @return obligatoryInsuranceExpirationDate
   */
  @javax.annotation.Nullable
  public LocalDate getObligatoryInsuranceExpirationDate() {
    return obligatoryInsuranceExpirationDate;
  }

  public void setObligatoryInsuranceExpirationDate(LocalDate obligatoryInsuranceExpirationDate) {
    this.obligatoryInsuranceExpirationDate = obligatoryInsuranceExpirationDate;
  }


  public VehicleSummary obligatoryInsuranceStatus(String obligatoryInsuranceStatus) {
    this.obligatoryInsuranceStatus = obligatoryInsuranceStatus;
    return this;
  }

  /**
   * Status of the vehicle compulsory insurances
   * @return obligatoryInsuranceStatus
   */
  @javax.annotation.Nullable
  public String getObligatoryInsuranceStatus() {
    return obligatoryInsuranceStatus;
  }

  public void setObligatoryInsuranceStatus(String obligatoryInsuranceStatus) {
    this.obligatoryInsuranceStatus = obligatoryInsuranceStatus;
  }


  public VehicleSummary serviceType(String serviceType) {
    this.serviceType = serviceType;
    return this;
  }

  /**
   * Vehicle service type
   * @return serviceType
   */
  @javax.annotation.Nullable
  public String getServiceType() {
    return serviceType;
  }

  public void setServiceType(String serviceType) {
    this.serviceType = serviceType;
  }


  public VehicleSummary vehicleCategory(String vehicleCategory) {
    this.vehicleCategory = vehicleCategory;
    return this;
  }

  /**
   * Vehicle category
   * @return vehicleCategory
   */
  @javax.annotation.Nullable
  public String getVehicleCategory() {
    return vehicleCategory;
  }

  public void setVehicleCategory(String vehicleCategory) {
    this.vehicleCategory = vehicleCategory;
  }


  public VehicleSummary vehicleId(String vehicleId) {
    this.vehicleId = vehicleId;
    return this;
  }

  /**
   * Vehicle ID
   * @return vehicleId
   */
  @javax.annotation.Nullable
  public String getVehicleId() {
    return vehicleId;
  }

  public void setVehicleId(String vehicleId) {
    this.vehicleId = vehicleId;
  }


  public VehicleSummary vehicleType(String vehicleType) {
    this.vehicleType = vehicleType;
    return this;
  }

  /**
   * Vehicle type
   * @return vehicleType
   */
  @javax.annotation.Nullable
  public String getVehicleType() {
    return vehicleType;
  }

  public void setVehicleType(String vehicleType) {
    this.vehicleType = vehicleType;
  }


  public VehicleSummary year(Integer year) {
    this.year = year;
    return this;
  }

  /**
   * Vehicle model year
   * @return year
   */
  @javax.annotation.Nullable
  public Integer getYear() {
    return year;
  }

  public void setYear(Integer year) {
    this.year = year;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VehicleSummary vehicleSummary = (VehicleSummary) o;
    return Objects.equals(this.capacity, vehicleSummary.capacity) &&
        Objects.equals(this.color, vehicleSummary.color) &&
        Objects.equals(this.licensePlate, vehicleSummary.licensePlate) &&
        Objects.equals(this.manufacturer, vehicleSummary.manufacturer) &&
        Objects.equals(this.model, vehicleSummary.model) &&
        Objects.equals(this.numberOfDoors, vehicleSummary.numberOfDoors) &&
        Objects.equals(this.obligatoryInsuranceExpirationDate, vehicleSummary.obligatoryInsuranceExpirationDate) &&
        Objects.equals(this.obligatoryInsuranceStatus, vehicleSummary.obligatoryInsuranceStatus) &&
        Objects.equals(this.serviceType, vehicleSummary.serviceType) &&
        Objects.equals(this.vehicleCategory, vehicleSummary.vehicleCategory) &&
        Objects.equals(this.vehicleId, vehicleSummary.vehicleId) &&
        Objects.equals(this.vehicleType, vehicleSummary.vehicleType) &&
        Objects.equals(this.year, vehicleSummary.year);
  }

  @Override
  public int hashCode() {
    return Objects.hash(capacity, color, licensePlate, manufacturer, model, numberOfDoors, obligatoryInsuranceExpirationDate, obligatoryInsuranceStatus, serviceType, vehicleCategory, vehicleId, vehicleType, year);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VehicleSummary {\n");
    sb.append("    capacity: ").append(toIndentedString(capacity)).append("\n");
    sb.append("    color: ").append(toIndentedString(color)).append("\n");
    sb.append("    licensePlate: ").append(toIndentedString(licensePlate)).append("\n");
    sb.append("    manufacturer: ").append(toIndentedString(manufacturer)).append("\n");
    sb.append("    model: ").append(toIndentedString(model)).append("\n");
    sb.append("    numberOfDoors: ").append(toIndentedString(numberOfDoors)).append("\n");
    sb.append("    obligatoryInsuranceExpirationDate: ").append(toIndentedString(obligatoryInsuranceExpirationDate)).append("\n");
    sb.append("    obligatoryInsuranceStatus: ").append(toIndentedString(obligatoryInsuranceStatus)).append("\n");
    sb.append("    serviceType: ").append(toIndentedString(serviceType)).append("\n");
    sb.append("    vehicleCategory: ").append(toIndentedString(vehicleCategory)).append("\n");
    sb.append("    vehicleId: ").append(toIndentedString(vehicleId)).append("\n");
    sb.append("    vehicleType: ").append(toIndentedString(vehicleType)).append("\n");
    sb.append("    year: ").append(toIndentedString(year)).append("\n");
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
    openapiFields.add("capacity");
    openapiFields.add("color");
    openapiFields.add("license_plate");
    openapiFields.add("manufacturer");
    openapiFields.add("model");
    openapiFields.add("number_of_doors");
    openapiFields.add("obligatory_insurance_expiration_date");
    openapiFields.add("obligatory_insurance_status");
    openapiFields.add("service_type");
    openapiFields.add("vehicle_category");
    openapiFields.add("vehicle_id");
    openapiFields.add("vehicle_type");
    openapiFields.add("year");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VehicleSummary
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VehicleSummary.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VehicleSummary is not found in the empty JSON string", VehicleSummary.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VehicleSummary.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VehicleSummary` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("color") != null && !jsonObj.get("color").isJsonNull()) && !jsonObj.get("color").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `color` to be a primitive type in the JSON string but got `%s`", jsonObj.get("color").toString()));
      }
      if ((jsonObj.get("license_plate") != null && !jsonObj.get("license_plate").isJsonNull()) && !jsonObj.get("license_plate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `license_plate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("license_plate").toString()));
      }
      if ((jsonObj.get("manufacturer") != null && !jsonObj.get("manufacturer").isJsonNull()) && !jsonObj.get("manufacturer").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `manufacturer` to be a primitive type in the JSON string but got `%s`", jsonObj.get("manufacturer").toString()));
      }
      if ((jsonObj.get("model") != null && !jsonObj.get("model").isJsonNull()) && !jsonObj.get("model").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `model` to be a primitive type in the JSON string but got `%s`", jsonObj.get("model").toString()));
      }
      if ((jsonObj.get("obligatory_insurance_status") != null && !jsonObj.get("obligatory_insurance_status").isJsonNull()) && !jsonObj.get("obligatory_insurance_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `obligatory_insurance_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("obligatory_insurance_status").toString()));
      }
      if ((jsonObj.get("service_type") != null && !jsonObj.get("service_type").isJsonNull()) && !jsonObj.get("service_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service_type").toString()));
      }
      if ((jsonObj.get("vehicle_category") != null && !jsonObj.get("vehicle_category").isJsonNull()) && !jsonObj.get("vehicle_category").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vehicle_category` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vehicle_category").toString()));
      }
      if ((jsonObj.get("vehicle_id") != null && !jsonObj.get("vehicle_id").isJsonNull()) && !jsonObj.get("vehicle_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vehicle_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vehicle_id").toString()));
      }
      if ((jsonObj.get("vehicle_type") != null && !jsonObj.get("vehicle_type").isJsonNull()) && !jsonObj.get("vehicle_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vehicle_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vehicle_type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VehicleSummary.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VehicleSummary' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VehicleSummary> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VehicleSummary.class));

       return (TypeAdapter<T>) new TypeAdapter<VehicleSummary>() {
           @Override
           public void write(JsonWriter out, VehicleSummary value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VehicleSummary read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VehicleSummary given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VehicleSummary
   * @throws IOException if the JSON string is invalid with respect to VehicleSummary
   */
  public static VehicleSummary fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VehicleSummary.class);
  }

  /**
   * Convert an instance of VehicleSummary to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

