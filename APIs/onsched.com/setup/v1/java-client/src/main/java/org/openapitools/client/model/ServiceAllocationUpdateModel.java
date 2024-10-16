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
import java.time.LocalDate;
import java.util.Arrays;
import org.openapitools.client.model.RepeatInputModel;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * ServiceAllocationUpdateModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:58.890429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ServiceAllocationUpdateModel {
  public static final String SERIALIZED_NAME_BOOKING_LIMIT = "bookingLimit";
  @SerializedName(SERIALIZED_NAME_BOOKING_LIMIT)
  private Integer bookingLimit;

  public static final String SERIALIZED_NAME_END_DATE = "endDate";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private LocalDate endDate;

  public static final String SERIALIZED_NAME_END_TIME = "endTime";
  @SerializedName(SERIALIZED_NAME_END_TIME)
  private Integer endTime;

  public static final String SERIALIZED_NAME_LOCATION_ID = "locationId";
  @SerializedName(SERIALIZED_NAME_LOCATION_ID)
  private String locationId;

  public static final String SERIALIZED_NAME_REASON = "reason";
  @SerializedName(SERIALIZED_NAME_REASON)
  private String reason;

  public static final String SERIALIZED_NAME_REPEAT = "repeat";
  @SerializedName(SERIALIZED_NAME_REPEAT)
  private RepeatInputModel repeat;

  public static final String SERIALIZED_NAME_REPEATS = "repeats";
  @SerializedName(SERIALIZED_NAME_REPEATS)
  private Boolean repeats;

  public static final String SERIALIZED_NAME_RESOURCE_ID = "resourceId";
  @SerializedName(SERIALIZED_NAME_RESOURCE_ID)
  private String resourceId;

  public static final String SERIALIZED_NAME_START_DATE = "startDate";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private LocalDate startDate;

  public static final String SERIALIZED_NAME_START_TIME = "startTime";
  @SerializedName(SERIALIZED_NAME_START_TIME)
  private Integer startTime;

  public ServiceAllocationUpdateModel() {
  }

  public ServiceAllocationUpdateModel bookingLimit(Integer bookingLimit) {
    this.bookingLimit = bookingLimit;
    return this;
  }

  /**
   * Get bookingLimit
   * @return bookingLimit
   */
  @javax.annotation.Nullable
  public Integer getBookingLimit() {
    return bookingLimit;
  }

  public void setBookingLimit(Integer bookingLimit) {
    this.bookingLimit = bookingLimit;
  }


  public ServiceAllocationUpdateModel endDate(LocalDate endDate) {
    this.endDate = endDate;
    return this;
  }

  /**
   * Get endDate
   * @return endDate
   */
  @javax.annotation.Nullable
  public LocalDate getEndDate() {
    return endDate;
  }

  public void setEndDate(LocalDate endDate) {
    this.endDate = endDate;
  }


  public ServiceAllocationUpdateModel endTime(Integer endTime) {
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


  public ServiceAllocationUpdateModel locationId(String locationId) {
    this.locationId = locationId;
    return this;
  }

  /**
   * Get locationId
   * @return locationId
   */
  @javax.annotation.Nullable
  public String getLocationId() {
    return locationId;
  }

  public void setLocationId(String locationId) {
    this.locationId = locationId;
  }


  public ServiceAllocationUpdateModel reason(String reason) {
    this.reason = reason;
    return this;
  }

  /**
   * Get reason
   * @return reason
   */
  @javax.annotation.Nullable
  public String getReason() {
    return reason;
  }

  public void setReason(String reason) {
    this.reason = reason;
  }


  public ServiceAllocationUpdateModel repeat(RepeatInputModel repeat) {
    this.repeat = repeat;
    return this;
  }

  /**
   * Get repeat
   * @return repeat
   */
  @javax.annotation.Nullable
  public RepeatInputModel getRepeat() {
    return repeat;
  }

  public void setRepeat(RepeatInputModel repeat) {
    this.repeat = repeat;
  }


  public ServiceAllocationUpdateModel repeats(Boolean repeats) {
    this.repeats = repeats;
    return this;
  }

  /**
   * Get repeats
   * @return repeats
   */
  @javax.annotation.Nullable
  public Boolean getRepeats() {
    return repeats;
  }

  public void setRepeats(Boolean repeats) {
    this.repeats = repeats;
  }


  public ServiceAllocationUpdateModel resourceId(String resourceId) {
    this.resourceId = resourceId;
    return this;
  }

  /**
   * Get resourceId
   * @return resourceId
   */
  @javax.annotation.Nullable
  public String getResourceId() {
    return resourceId;
  }

  public void setResourceId(String resourceId) {
    this.resourceId = resourceId;
  }


  public ServiceAllocationUpdateModel startDate(LocalDate startDate) {
    this.startDate = startDate;
    return this;
  }

  /**
   * Get startDate
   * @return startDate
   */
  @javax.annotation.Nullable
  public LocalDate getStartDate() {
    return startDate;
  }

  public void setStartDate(LocalDate startDate) {
    this.startDate = startDate;
  }


  public ServiceAllocationUpdateModel startTime(Integer startTime) {
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
    ServiceAllocationUpdateModel serviceAllocationUpdateModel = (ServiceAllocationUpdateModel) o;
    return Objects.equals(this.bookingLimit, serviceAllocationUpdateModel.bookingLimit) &&
        Objects.equals(this.endDate, serviceAllocationUpdateModel.endDate) &&
        Objects.equals(this.endTime, serviceAllocationUpdateModel.endTime) &&
        Objects.equals(this.locationId, serviceAllocationUpdateModel.locationId) &&
        Objects.equals(this.reason, serviceAllocationUpdateModel.reason) &&
        Objects.equals(this.repeat, serviceAllocationUpdateModel.repeat) &&
        Objects.equals(this.repeats, serviceAllocationUpdateModel.repeats) &&
        Objects.equals(this.resourceId, serviceAllocationUpdateModel.resourceId) &&
        Objects.equals(this.startDate, serviceAllocationUpdateModel.startDate) &&
        Objects.equals(this.startTime, serviceAllocationUpdateModel.startTime);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(bookingLimit, endDate, endTime, locationId, reason, repeat, repeats, resourceId, startDate, startTime);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ServiceAllocationUpdateModel {\n");
    sb.append("    bookingLimit: ").append(toIndentedString(bookingLimit)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    endTime: ").append(toIndentedString(endTime)).append("\n");
    sb.append("    locationId: ").append(toIndentedString(locationId)).append("\n");
    sb.append("    reason: ").append(toIndentedString(reason)).append("\n");
    sb.append("    repeat: ").append(toIndentedString(repeat)).append("\n");
    sb.append("    repeats: ").append(toIndentedString(repeats)).append("\n");
    sb.append("    resourceId: ").append(toIndentedString(resourceId)).append("\n");
    sb.append("    startDate: ").append(toIndentedString(startDate)).append("\n");
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
    openapiFields.add("bookingLimit");
    openapiFields.add("endDate");
    openapiFields.add("endTime");
    openapiFields.add("locationId");
    openapiFields.add("reason");
    openapiFields.add("repeat");
    openapiFields.add("repeats");
    openapiFields.add("resourceId");
    openapiFields.add("startDate");
    openapiFields.add("startTime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ServiceAllocationUpdateModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ServiceAllocationUpdateModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ServiceAllocationUpdateModel is not found in the empty JSON string", ServiceAllocationUpdateModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ServiceAllocationUpdateModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ServiceAllocationUpdateModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("locationId") != null && !jsonObj.get("locationId").isJsonNull()) && !jsonObj.get("locationId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `locationId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("locationId").toString()));
      }
      if ((jsonObj.get("reason") != null && !jsonObj.get("reason").isJsonNull()) && !jsonObj.get("reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reason").toString()));
      }
      // validate the optional field `repeat`
      if (jsonObj.get("repeat") != null && !jsonObj.get("repeat").isJsonNull()) {
        RepeatInputModel.validateJsonElement(jsonObj.get("repeat"));
      }
      if ((jsonObj.get("resourceId") != null && !jsonObj.get("resourceId").isJsonNull()) && !jsonObj.get("resourceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `resourceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("resourceId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ServiceAllocationUpdateModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ServiceAllocationUpdateModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ServiceAllocationUpdateModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ServiceAllocationUpdateModel.class));

       return (TypeAdapter<T>) new TypeAdapter<ServiceAllocationUpdateModel>() {
           @Override
           public void write(JsonWriter out, ServiceAllocationUpdateModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ServiceAllocationUpdateModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ServiceAllocationUpdateModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ServiceAllocationUpdateModel
   * @throws IOException if the JSON string is invalid with respect to ServiceAllocationUpdateModel
   */
  public static ServiceAllocationUpdateModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ServiceAllocationUpdateModel.class);
  }

  /**
   * Convert an instance of ServiceAllocationUpdateModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

