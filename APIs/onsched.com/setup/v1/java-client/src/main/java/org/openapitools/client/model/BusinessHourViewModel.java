/*
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
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
 * BusinessHourViewModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:58.890429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BusinessHourViewModel {
  public static final String SERIALIZED_NAME_END_TIME = "endTime";
  @SerializedName(SERIALIZED_NAME_END_TIME)
  private Integer endTime;

  public static final String SERIALIZED_NAME_IS24_HOURS = "is24Hours";
  @SerializedName(SERIALIZED_NAME_IS24_HOURS)
  private Boolean is24Hours;

  public static final String SERIALIZED_NAME_IS_OPEN = "isOpen";
  @SerializedName(SERIALIZED_NAME_IS_OPEN)
  private Boolean isOpen;

  public static final String SERIALIZED_NAME_START_TIME = "startTime";
  @SerializedName(SERIALIZED_NAME_START_TIME)
  private Integer startTime;

  public BusinessHourViewModel() {
  }

  public BusinessHourViewModel endTime(Integer endTime) {
    this.endTime = endTime;
    return this;
  }

  /**
   * Get endTime
   * @return endTime
   */
  @javax.annotation.Nullable
  public Integer getEndTime() {
    return endTime;
  }

  public void setEndTime(Integer endTime) {
    this.endTime = endTime;
  }


  public BusinessHourViewModel is24Hours(Boolean is24Hours) {
    this.is24Hours = is24Hours;
    return this;
  }

  /**
   * Get is24Hours
   * @return is24Hours
   */
  @javax.annotation.Nullable
  public Boolean getIs24Hours() {
    return is24Hours;
  }

  public void setIs24Hours(Boolean is24Hours) {
    this.is24Hours = is24Hours;
  }


  public BusinessHourViewModel isOpen(Boolean isOpen) {
    this.isOpen = isOpen;
    return this;
  }

  /**
   * Get isOpen
   * @return isOpen
   */
  @javax.annotation.Nullable
  public Boolean getIsOpen() {
    return isOpen;
  }

  public void setIsOpen(Boolean isOpen) {
    this.isOpen = isOpen;
  }


  public BusinessHourViewModel startTime(Integer startTime) {
    this.startTime = startTime;
    return this;
  }

  /**
   * Get startTime
   * @return startTime
   */
  @javax.annotation.Nullable
  public Integer getStartTime() {
    return startTime;
  }

  public void setStartTime(Integer startTime) {
    this.startTime = startTime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BusinessHourViewModel businessHourViewModel = (BusinessHourViewModel) o;
    return Objects.equals(this.endTime, businessHourViewModel.endTime) &&
        Objects.equals(this.is24Hours, businessHourViewModel.is24Hours) &&
        Objects.equals(this.isOpen, businessHourViewModel.isOpen) &&
        Objects.equals(this.startTime, businessHourViewModel.startTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(endTime, is24Hours, isOpen, startTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BusinessHourViewModel {\n");
    sb.append("    endTime: ").append(toIndentedString(endTime)).append("\n");
    sb.append("    is24Hours: ").append(toIndentedString(is24Hours)).append("\n");
    sb.append("    isOpen: ").append(toIndentedString(isOpen)).append("\n");
    sb.append("    startTime: ").append(toIndentedString(startTime)).append("\n");
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
    openapiFields.add("endTime");
    openapiFields.add("is24Hours");
    openapiFields.add("isOpen");
    openapiFields.add("startTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BusinessHourViewModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BusinessHourViewModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BusinessHourViewModel is not found in the empty JSON string", BusinessHourViewModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BusinessHourViewModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BusinessHourViewModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BusinessHourViewModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BusinessHourViewModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BusinessHourViewModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BusinessHourViewModel.class));

       return (TypeAdapter<T>) new TypeAdapter<BusinessHourViewModel>() {
           @Override
           public void write(JsonWriter out, BusinessHourViewModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BusinessHourViewModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BusinessHourViewModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BusinessHourViewModel
   * @throws IOException if the JSON string is invalid with respect to BusinessHourViewModel
   */
  public static BusinessHourViewModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BusinessHourViewModel.class);
  }

  /**
   * Convert an instance of BusinessHourViewModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

