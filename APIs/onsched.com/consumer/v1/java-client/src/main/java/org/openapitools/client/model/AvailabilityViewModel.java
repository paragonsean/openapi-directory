/*
 * OnSched Consumer API
 * Build secure and scalable custom apps for Online Booking. Our flexible API provides many options for availability and booking.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AvailableDayViewModel;
import org.openapitools.client.model.AvailableTimeViewModel;
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
 * AvailabilityViewModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:57.922898-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AvailabilityViewModel {
  public static final String SERIALIZED_NAME_AVAILABLE_DAYS = "availableDays";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_DAYS)
  private List<AvailableDayViewModel> availableDays;

  public static final String SERIALIZED_NAME_AVAILABLE_TIMES = "availableTimes";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_TIMES)
  private List<AvailableTimeViewModel> availableTimes;

  public static final String SERIALIZED_NAME_BUSINESS_NAME = "businessName";
  @SerializedName(SERIALIZED_NAME_BUSINESS_NAME)
  private String businessName;

  public static final String SERIALIZED_NAME_CALENDAR_ID = "calendarId";
  @SerializedName(SERIALIZED_NAME_CALENDAR_ID)
  private String calendarId;

  public static final String SERIALIZED_NAME_CALENDAR_RESOURCE_GROUP_ID = "calendarResourceGroupId";
  @SerializedName(SERIALIZED_NAME_CALENDAR_RESOURCE_GROUP_ID)
  private String calendarResourceGroupId;

  public static final String SERIALIZED_NAME_END_DATE = "endDate";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private String endDate;

  public static final String SERIALIZED_NAME_FIRST_AVAILABLE_DATE = "firstAvailableDate";
  @SerializedName(SERIALIZED_NAME_FIRST_AVAILABLE_DATE)
  private String firstAvailableDate;

  public static final String SERIALIZED_NAME_LOCATION_ID = "locationId";
  @SerializedName(SERIALIZED_NAME_LOCATION_ID)
  private String locationId;

  public static final String SERIALIZED_NAME_OBJECT = "object";
  @SerializedName(SERIALIZED_NAME_OBJECT)
  private String _object;

  public static final String SERIALIZED_NAME_RESOURCE_DESCRIPTION = "resourceDescription";
  @SerializedName(SERIALIZED_NAME_RESOURCE_DESCRIPTION)
  private String resourceDescription;

  public static final String SERIALIZED_NAME_RESOURCE_ID = "resourceId";
  @SerializedName(SERIALIZED_NAME_RESOURCE_ID)
  private String resourceId;

  public static final String SERIALIZED_NAME_RESOURCE_IDS = "resourceIds";
  @SerializedName(SERIALIZED_NAME_RESOURCE_IDS)
  private String resourceIds;

  public static final String SERIALIZED_NAME_RESOURCE_NAME = "resourceName";
  @SerializedName(SERIALIZED_NAME_RESOURCE_NAME)
  private String resourceName;

  public static final String SERIALIZED_NAME_SERVICE_DESCRIPTION = "serviceDescription";
  @SerializedName(SERIALIZED_NAME_SERVICE_DESCRIPTION)
  private String serviceDescription;

  public static final String SERIALIZED_NAME_SERVICE_DURATION = "serviceDuration";
  @SerializedName(SERIALIZED_NAME_SERVICE_DURATION)
  private Integer serviceDuration;

  public static final String SERIALIZED_NAME_SERVICE_ID = "serviceId";
  @SerializedName(SERIALIZED_NAME_SERVICE_ID)
  private String serviceId;

  public static final String SERIALIZED_NAME_SERVICE_NAME = "serviceName";
  @SerializedName(SERIALIZED_NAME_SERVICE_NAME)
  private String serviceName;

  public static final String SERIALIZED_NAME_START_DATE = "startDate";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private String startDate;

  public static final String SERIALIZED_NAME_TIMEZONE_NAME = "timezoneName";
  @SerializedName(SERIALIZED_NAME_TIMEZONE_NAME)
  private String timezoneName;

  public static final String SERIALIZED_NAME_TZ_REQUESTED = "tzRequested";
  @SerializedName(SERIALIZED_NAME_TZ_REQUESTED)
  private Integer tzRequested;

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  public AvailabilityViewModel() {
  }

  public AvailabilityViewModel availableDays(List<AvailableDayViewModel> availableDays) {
    this.availableDays = availableDays;
    return this;
  }

  public AvailabilityViewModel addAvailableDaysItem(AvailableDayViewModel availableDaysItem) {
    if (this.availableDays == null) {
      this.availableDays = new ArrayList<>();
    }
    this.availableDays.add(availableDaysItem);
    return this;
  }

  /**
   * Get availableDays
   * @return availableDays
   */
  @javax.annotation.Nullable
  public List<AvailableDayViewModel> getAvailableDays() {
    return availableDays;
  }

  public void setAvailableDays(List<AvailableDayViewModel> availableDays) {
    this.availableDays = availableDays;
  }


  public AvailabilityViewModel availableTimes(List<AvailableTimeViewModel> availableTimes) {
    this.availableTimes = availableTimes;
    return this;
  }

  public AvailabilityViewModel addAvailableTimesItem(AvailableTimeViewModel availableTimesItem) {
    if (this.availableTimes == null) {
      this.availableTimes = new ArrayList<>();
    }
    this.availableTimes.add(availableTimesItem);
    return this;
  }

  /**
   * Get availableTimes
   * @return availableTimes
   */
  @javax.annotation.Nullable
  public List<AvailableTimeViewModel> getAvailableTimes() {
    return availableTimes;
  }

  public void setAvailableTimes(List<AvailableTimeViewModel> availableTimes) {
    this.availableTimes = availableTimes;
  }


  public AvailabilityViewModel businessName(String businessName) {
    this.businessName = businessName;
    return this;
  }

  /**
   * Get businessName
   * @return businessName
   */
  @javax.annotation.Nullable
  public String getBusinessName() {
    return businessName;
  }

  public void setBusinessName(String businessName) {
    this.businessName = businessName;
  }


  public AvailabilityViewModel calendarId(String calendarId) {
    this.calendarId = calendarId;
    return this;
  }

  /**
   * Get calendarId
   * @return calendarId
   */
  @javax.annotation.Nullable
  public String getCalendarId() {
    return calendarId;
  }

  public void setCalendarId(String calendarId) {
    this.calendarId = calendarId;
  }


  public AvailabilityViewModel calendarResourceGroupId(String calendarResourceGroupId) {
    this.calendarResourceGroupId = calendarResourceGroupId;
    return this;
  }

  /**
   * Get calendarResourceGroupId
   * @return calendarResourceGroupId
   */
  @javax.annotation.Nullable
  public String getCalendarResourceGroupId() {
    return calendarResourceGroupId;
  }

  public void setCalendarResourceGroupId(String calendarResourceGroupId) {
    this.calendarResourceGroupId = calendarResourceGroupId;
  }


  public AvailabilityViewModel endDate(String endDate) {
    this.endDate = endDate;
    return this;
  }

  /**
   * Get endDate
   * @return endDate
   */
  @javax.annotation.Nullable
  public String getEndDate() {
    return endDate;
  }

  public void setEndDate(String endDate) {
    this.endDate = endDate;
  }


  public AvailabilityViewModel firstAvailableDate(String firstAvailableDate) {
    this.firstAvailableDate = firstAvailableDate;
    return this;
  }

  /**
   * Get firstAvailableDate
   * @return firstAvailableDate
   */
  @javax.annotation.Nullable
  public String getFirstAvailableDate() {
    return firstAvailableDate;
  }

  public void setFirstAvailableDate(String firstAvailableDate) {
    this.firstAvailableDate = firstAvailableDate;
  }


  public AvailabilityViewModel locationId(String locationId) {
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


  public AvailabilityViewModel _object(String _object) {
    this._object = _object;
    return this;
  }

  /**
   * Get _object
   * @return _object
   */
  @javax.annotation.Nullable
  public String getObject() {
    return _object;
  }

  public void setObject(String _object) {
    this._object = _object;
  }


  public AvailabilityViewModel resourceDescription(String resourceDescription) {
    this.resourceDescription = resourceDescription;
    return this;
  }

  /**
   * Get resourceDescription
   * @return resourceDescription
   */
  @javax.annotation.Nullable
  public String getResourceDescription() {
    return resourceDescription;
  }

  public void setResourceDescription(String resourceDescription) {
    this.resourceDescription = resourceDescription;
  }


  public AvailabilityViewModel resourceId(String resourceId) {
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


  public AvailabilityViewModel resourceIds(String resourceIds) {
    this.resourceIds = resourceIds;
    return this;
  }

  /**
   * Get resourceIds
   * @return resourceIds
   */
  @javax.annotation.Nullable
  public String getResourceIds() {
    return resourceIds;
  }

  public void setResourceIds(String resourceIds) {
    this.resourceIds = resourceIds;
  }


  public AvailabilityViewModel resourceName(String resourceName) {
    this.resourceName = resourceName;
    return this;
  }

  /**
   * Get resourceName
   * @return resourceName
   */
  @javax.annotation.Nullable
  public String getResourceName() {
    return resourceName;
  }

  public void setResourceName(String resourceName) {
    this.resourceName = resourceName;
  }


  public AvailabilityViewModel serviceDescription(String serviceDescription) {
    this.serviceDescription = serviceDescription;
    return this;
  }

  /**
   * Get serviceDescription
   * @return serviceDescription
   */
  @javax.annotation.Nullable
  public String getServiceDescription() {
    return serviceDescription;
  }

  public void setServiceDescription(String serviceDescription) {
    this.serviceDescription = serviceDescription;
  }


  public AvailabilityViewModel serviceDuration(Integer serviceDuration) {
    this.serviceDuration = serviceDuration;
    return this;
  }

  /**
   * Get serviceDuration
   * @return serviceDuration
   */
  @javax.annotation.Nullable
  public Integer getServiceDuration() {
    return serviceDuration;
  }

  public void setServiceDuration(Integer serviceDuration) {
    this.serviceDuration = serviceDuration;
  }


  public AvailabilityViewModel serviceId(String serviceId) {
    this.serviceId = serviceId;
    return this;
  }

  /**
   * Get serviceId
   * @return serviceId
   */
  @javax.annotation.Nullable
  public String getServiceId() {
    return serviceId;
  }

  public void setServiceId(String serviceId) {
    this.serviceId = serviceId;
  }


  public AvailabilityViewModel serviceName(String serviceName) {
    this.serviceName = serviceName;
    return this;
  }

  /**
   * Get serviceName
   * @return serviceName
   */
  @javax.annotation.Nullable
  public String getServiceName() {
    return serviceName;
  }

  public void setServiceName(String serviceName) {
    this.serviceName = serviceName;
  }


  public AvailabilityViewModel startDate(String startDate) {
    this.startDate = startDate;
    return this;
  }

  /**
   * Get startDate
   * @return startDate
   */
  @javax.annotation.Nullable
  public String getStartDate() {
    return startDate;
  }

  public void setStartDate(String startDate) {
    this.startDate = startDate;
  }


  public AvailabilityViewModel timezoneName(String timezoneName) {
    this.timezoneName = timezoneName;
    return this;
  }

  /**
   * Returns the Timezone Name in IANA format if a TimezoneName was passed into an Availability call; otherwise this property is hidden
   * @return timezoneName
   */
  @javax.annotation.Nullable
  public String getTimezoneName() {
    return timezoneName;
  }

  public void setTimezoneName(String timezoneName) {
    this.timezoneName = timezoneName;
  }


  public AvailabilityViewModel tzRequested(Integer tzRequested) {
    this.tzRequested = tzRequested;
    return this;
  }

  /**
   * Returns the timezone offset if a tzOffset was supplied into an Availability call; null if a TimezoneName was passed; otherwise the Business timezone offset is returned
   * @return tzRequested
   */
  @javax.annotation.Nullable
  public Integer getTzRequested() {
    return tzRequested;
  }

  public void setTzRequested(Integer tzRequested) {
    this.tzRequested = tzRequested;
  }


  public AvailabilityViewModel url(String url) {
    this.url = url;
    return this;
  }

  /**
   * Get url
   * @return url
   */
  @javax.annotation.Nullable
  public String getUrl() {
    return url;
  }

  public void setUrl(String url) {
    this.url = url;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AvailabilityViewModel availabilityViewModel = (AvailabilityViewModel) o;
    return Objects.equals(this.availableDays, availabilityViewModel.availableDays) &&
        Objects.equals(this.availableTimes, availabilityViewModel.availableTimes) &&
        Objects.equals(this.businessName, availabilityViewModel.businessName) &&
        Objects.equals(this.calendarId, availabilityViewModel.calendarId) &&
        Objects.equals(this.calendarResourceGroupId, availabilityViewModel.calendarResourceGroupId) &&
        Objects.equals(this.endDate, availabilityViewModel.endDate) &&
        Objects.equals(this.firstAvailableDate, availabilityViewModel.firstAvailableDate) &&
        Objects.equals(this.locationId, availabilityViewModel.locationId) &&
        Objects.equals(this._object, availabilityViewModel._object) &&
        Objects.equals(this.resourceDescription, availabilityViewModel.resourceDescription) &&
        Objects.equals(this.resourceId, availabilityViewModel.resourceId) &&
        Objects.equals(this.resourceIds, availabilityViewModel.resourceIds) &&
        Objects.equals(this.resourceName, availabilityViewModel.resourceName) &&
        Objects.equals(this.serviceDescription, availabilityViewModel.serviceDescription) &&
        Objects.equals(this.serviceDuration, availabilityViewModel.serviceDuration) &&
        Objects.equals(this.serviceId, availabilityViewModel.serviceId) &&
        Objects.equals(this.serviceName, availabilityViewModel.serviceName) &&
        Objects.equals(this.startDate, availabilityViewModel.startDate) &&
        Objects.equals(this.timezoneName, availabilityViewModel.timezoneName) &&
        Objects.equals(this.tzRequested, availabilityViewModel.tzRequested) &&
        Objects.equals(this.url, availabilityViewModel.url);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(availableDays, availableTimes, businessName, calendarId, calendarResourceGroupId, endDate, firstAvailableDate, locationId, _object, resourceDescription, resourceId, resourceIds, resourceName, serviceDescription, serviceDuration, serviceId, serviceName, startDate, timezoneName, tzRequested, url);
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
    sb.append("class AvailabilityViewModel {\n");
    sb.append("    availableDays: ").append(toIndentedString(availableDays)).append("\n");
    sb.append("    availableTimes: ").append(toIndentedString(availableTimes)).append("\n");
    sb.append("    businessName: ").append(toIndentedString(businessName)).append("\n");
    sb.append("    calendarId: ").append(toIndentedString(calendarId)).append("\n");
    sb.append("    calendarResourceGroupId: ").append(toIndentedString(calendarResourceGroupId)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    firstAvailableDate: ").append(toIndentedString(firstAvailableDate)).append("\n");
    sb.append("    locationId: ").append(toIndentedString(locationId)).append("\n");
    sb.append("    _object: ").append(toIndentedString(_object)).append("\n");
    sb.append("    resourceDescription: ").append(toIndentedString(resourceDescription)).append("\n");
    sb.append("    resourceId: ").append(toIndentedString(resourceId)).append("\n");
    sb.append("    resourceIds: ").append(toIndentedString(resourceIds)).append("\n");
    sb.append("    resourceName: ").append(toIndentedString(resourceName)).append("\n");
    sb.append("    serviceDescription: ").append(toIndentedString(serviceDescription)).append("\n");
    sb.append("    serviceDuration: ").append(toIndentedString(serviceDuration)).append("\n");
    sb.append("    serviceId: ").append(toIndentedString(serviceId)).append("\n");
    sb.append("    serviceName: ").append(toIndentedString(serviceName)).append("\n");
    sb.append("    startDate: ").append(toIndentedString(startDate)).append("\n");
    sb.append("    timezoneName: ").append(toIndentedString(timezoneName)).append("\n");
    sb.append("    tzRequested: ").append(toIndentedString(tzRequested)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
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
    openapiFields.add("availableDays");
    openapiFields.add("availableTimes");
    openapiFields.add("businessName");
    openapiFields.add("calendarId");
    openapiFields.add("calendarResourceGroupId");
    openapiFields.add("endDate");
    openapiFields.add("firstAvailableDate");
    openapiFields.add("locationId");
    openapiFields.add("object");
    openapiFields.add("resourceDescription");
    openapiFields.add("resourceId");
    openapiFields.add("resourceIds");
    openapiFields.add("resourceName");
    openapiFields.add("serviceDescription");
    openapiFields.add("serviceDuration");
    openapiFields.add("serviceId");
    openapiFields.add("serviceName");
    openapiFields.add("startDate");
    openapiFields.add("timezoneName");
    openapiFields.add("tzRequested");
    openapiFields.add("url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AvailabilityViewModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AvailabilityViewModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AvailabilityViewModel is not found in the empty JSON string", AvailabilityViewModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AvailabilityViewModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AvailabilityViewModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("availableDays") != null && !jsonObj.get("availableDays").isJsonNull()) {
        JsonArray jsonArrayavailableDays = jsonObj.getAsJsonArray("availableDays");
        if (jsonArrayavailableDays != null) {
          // ensure the json data is an array
          if (!jsonObj.get("availableDays").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `availableDays` to be an array in the JSON string but got `%s`", jsonObj.get("availableDays").toString()));
          }

          // validate the optional field `availableDays` (array)
          for (int i = 0; i < jsonArrayavailableDays.size(); i++) {
            AvailableDayViewModel.validateJsonElement(jsonArrayavailableDays.get(i));
          };
        }
      }
      if (jsonObj.get("availableTimes") != null && !jsonObj.get("availableTimes").isJsonNull()) {
        JsonArray jsonArrayavailableTimes = jsonObj.getAsJsonArray("availableTimes");
        if (jsonArrayavailableTimes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("availableTimes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `availableTimes` to be an array in the JSON string but got `%s`", jsonObj.get("availableTimes").toString()));
          }

          // validate the optional field `availableTimes` (array)
          for (int i = 0; i < jsonArrayavailableTimes.size(); i++) {
            AvailableTimeViewModel.validateJsonElement(jsonArrayavailableTimes.get(i));
          };
        }
      }
      if ((jsonObj.get("businessName") != null && !jsonObj.get("businessName").isJsonNull()) && !jsonObj.get("businessName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `businessName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("businessName").toString()));
      }
      if ((jsonObj.get("calendarId") != null && !jsonObj.get("calendarId").isJsonNull()) && !jsonObj.get("calendarId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `calendarId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("calendarId").toString()));
      }
      if ((jsonObj.get("calendarResourceGroupId") != null && !jsonObj.get("calendarResourceGroupId").isJsonNull()) && !jsonObj.get("calendarResourceGroupId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `calendarResourceGroupId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("calendarResourceGroupId").toString()));
      }
      if ((jsonObj.get("endDate") != null && !jsonObj.get("endDate").isJsonNull()) && !jsonObj.get("endDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `endDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("endDate").toString()));
      }
      if ((jsonObj.get("firstAvailableDate") != null && !jsonObj.get("firstAvailableDate").isJsonNull()) && !jsonObj.get("firstAvailableDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `firstAvailableDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("firstAvailableDate").toString()));
      }
      if ((jsonObj.get("locationId") != null && !jsonObj.get("locationId").isJsonNull()) && !jsonObj.get("locationId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `locationId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("locationId").toString()));
      }
      if ((jsonObj.get("object") != null && !jsonObj.get("object").isJsonNull()) && !jsonObj.get("object").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `object` to be a primitive type in the JSON string but got `%s`", jsonObj.get("object").toString()));
      }
      if ((jsonObj.get("resourceDescription") != null && !jsonObj.get("resourceDescription").isJsonNull()) && !jsonObj.get("resourceDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `resourceDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("resourceDescription").toString()));
      }
      if ((jsonObj.get("resourceId") != null && !jsonObj.get("resourceId").isJsonNull()) && !jsonObj.get("resourceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `resourceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("resourceId").toString()));
      }
      if ((jsonObj.get("resourceIds") != null && !jsonObj.get("resourceIds").isJsonNull()) && !jsonObj.get("resourceIds").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `resourceIds` to be a primitive type in the JSON string but got `%s`", jsonObj.get("resourceIds").toString()));
      }
      if ((jsonObj.get("resourceName") != null && !jsonObj.get("resourceName").isJsonNull()) && !jsonObj.get("resourceName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `resourceName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("resourceName").toString()));
      }
      if ((jsonObj.get("serviceDescription") != null && !jsonObj.get("serviceDescription").isJsonNull()) && !jsonObj.get("serviceDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `serviceDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("serviceDescription").toString()));
      }
      if ((jsonObj.get("serviceId") != null && !jsonObj.get("serviceId").isJsonNull()) && !jsonObj.get("serviceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `serviceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("serviceId").toString()));
      }
      if ((jsonObj.get("serviceName") != null && !jsonObj.get("serviceName").isJsonNull()) && !jsonObj.get("serviceName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `serviceName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("serviceName").toString()));
      }
      if ((jsonObj.get("startDate") != null && !jsonObj.get("startDate").isJsonNull()) && !jsonObj.get("startDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `startDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("startDate").toString()));
      }
      if ((jsonObj.get("timezoneName") != null && !jsonObj.get("timezoneName").isJsonNull()) && !jsonObj.get("timezoneName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timezoneName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timezoneName").toString()));
      }
      if ((jsonObj.get("url") != null && !jsonObj.get("url").isJsonNull()) && !jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AvailabilityViewModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AvailabilityViewModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AvailabilityViewModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AvailabilityViewModel.class));

       return (TypeAdapter<T>) new TypeAdapter<AvailabilityViewModel>() {
           @Override
           public void write(JsonWriter out, AvailabilityViewModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AvailabilityViewModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AvailabilityViewModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AvailabilityViewModel
   * @throws IOException if the JSON string is invalid with respect to AvailabilityViewModel
   */
  public static AvailabilityViewModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AvailabilityViewModel.class);
  }

  /**
   * Convert an instance of AvailabilityViewModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

