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
import org.openapitools.client.model.BookingFieldItem;
import org.openapitools.client.model.CustomFieldInputModel;
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
 * AppointmentReserveModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:57.922898-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AppointmentReserveModel {
  public static final String SERIALIZED_NAME_APPOINTMENT_BOOKING_FIELDS = "appointmentBookingFields";
  @SerializedName(SERIALIZED_NAME_APPOINTMENT_BOOKING_FIELDS)
  private List<BookingFieldItem> appointmentBookingFields;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "customFields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private CustomFieldInputModel customFields;

  public static final String SERIALIZED_NAME_CUSTOMER_BOOKING_FIELDS = "customerBookingFields";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_BOOKING_FIELDS)
  private List<BookingFieldItem> customerBookingFields;

  public static final String SERIALIZED_NAME_CUSTOMER_MESSAGE = "customerMessage";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_MESSAGE)
  private String customerMessage;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NOTES = "notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_PHONE = "phone";
  @SerializedName(SERIALIZED_NAME_PHONE)
  private String phone;

  public static final String SERIALIZED_NAME_PHONE_EXT = "phoneExt";
  @SerializedName(SERIALIZED_NAME_PHONE_EXT)
  private String phoneExt;

  public static final String SERIALIZED_NAME_PHONE_TYPE = "phoneType";
  @SerializedName(SERIALIZED_NAME_PHONE_TYPE)
  private String phoneType;

  public AppointmentReserveModel() {
  }

  public AppointmentReserveModel appointmentBookingFields(List<BookingFieldItem> appointmentBookingFields) {
    this.appointmentBookingFields = appointmentBookingFields;
    return this;
  }

  public AppointmentReserveModel addAppointmentBookingFieldsItem(BookingFieldItem appointmentBookingFieldsItem) {
    if (this.appointmentBookingFields == null) {
      this.appointmentBookingFields = new ArrayList<>();
    }
    this.appointmentBookingFields.add(appointmentBookingFieldsItem);
    return this;
  }

  /**
   * Get appointmentBookingFields
   * @return appointmentBookingFields
   */
  @javax.annotation.Nullable
  public List<BookingFieldItem> getAppointmentBookingFields() {
    return appointmentBookingFields;
  }

  public void setAppointmentBookingFields(List<BookingFieldItem> appointmentBookingFields) {
    this.appointmentBookingFields = appointmentBookingFields;
  }


  public AppointmentReserveModel customFields(CustomFieldInputModel customFields) {
    this.customFields = customFields;
    return this;
  }

  /**
   * Get customFields
   * @return customFields
   */
  @javax.annotation.Nullable
  public CustomFieldInputModel getCustomFields() {
    return customFields;
  }

  public void setCustomFields(CustomFieldInputModel customFields) {
    this.customFields = customFields;
  }


  public AppointmentReserveModel customerBookingFields(List<BookingFieldItem> customerBookingFields) {
    this.customerBookingFields = customerBookingFields;
    return this;
  }

  public AppointmentReserveModel addCustomerBookingFieldsItem(BookingFieldItem customerBookingFieldsItem) {
    if (this.customerBookingFields == null) {
      this.customerBookingFields = new ArrayList<>();
    }
    this.customerBookingFields.add(customerBookingFieldsItem);
    return this;
  }

  /**
   * Get customerBookingFields
   * @return customerBookingFields
   */
  @javax.annotation.Nullable
  public List<BookingFieldItem> getCustomerBookingFields() {
    return customerBookingFields;
  }

  public void setCustomerBookingFields(List<BookingFieldItem> customerBookingFields) {
    this.customerBookingFields = customerBookingFields;
  }


  public AppointmentReserveModel customerMessage(String customerMessage) {
    this.customerMessage = customerMessage;
    return this;
  }

  /**
   * Get customerMessage
   * @return customerMessage
   */
  @javax.annotation.Nullable
  public String getCustomerMessage() {
    return customerMessage;
  }

  public void setCustomerMessage(String customerMessage) {
    this.customerMessage = customerMessage;
  }


  public AppointmentReserveModel email(String email) {
    this.email = email;
    return this;
  }

  /**
   * Get email
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public AppointmentReserveModel name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public AppointmentReserveModel notes(String notes) {
    this.notes = notes;
    return this;
  }

  /**
   * Get notes
   * @return notes
   */
  @javax.annotation.Nullable
  public String getNotes() {
    return notes;
  }

  public void setNotes(String notes) {
    this.notes = notes;
  }


  public AppointmentReserveModel phone(String phone) {
    this.phone = phone;
    return this;
  }

  /**
   * Get phone
   * @return phone
   */
  @javax.annotation.Nullable
  public String getPhone() {
    return phone;
  }

  public void setPhone(String phone) {
    this.phone = phone;
  }


  public AppointmentReserveModel phoneExt(String phoneExt) {
    this.phoneExt = phoneExt;
    return this;
  }

  /**
   * Get phoneExt
   * @return phoneExt
   */
  @javax.annotation.Nullable
  public String getPhoneExt() {
    return phoneExt;
  }

  public void setPhoneExt(String phoneExt) {
    this.phoneExt = phoneExt;
  }


  public AppointmentReserveModel phoneType(String phoneType) {
    this.phoneType = phoneType;
    return this;
  }

  /**
   * Get phoneType
   * @return phoneType
   */
  @javax.annotation.Nullable
  public String getPhoneType() {
    return phoneType;
  }

  public void setPhoneType(String phoneType) {
    this.phoneType = phoneType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AppointmentReserveModel appointmentReserveModel = (AppointmentReserveModel) o;
    return Objects.equals(this.appointmentBookingFields, appointmentReserveModel.appointmentBookingFields) &&
        Objects.equals(this.customFields, appointmentReserveModel.customFields) &&
        Objects.equals(this.customerBookingFields, appointmentReserveModel.customerBookingFields) &&
        Objects.equals(this.customerMessage, appointmentReserveModel.customerMessage) &&
        Objects.equals(this.email, appointmentReserveModel.email) &&
        Objects.equals(this.name, appointmentReserveModel.name) &&
        Objects.equals(this.notes, appointmentReserveModel.notes) &&
        Objects.equals(this.phone, appointmentReserveModel.phone) &&
        Objects.equals(this.phoneExt, appointmentReserveModel.phoneExt) &&
        Objects.equals(this.phoneType, appointmentReserveModel.phoneType);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(appointmentBookingFields, customFields, customerBookingFields, customerMessage, email, name, notes, phone, phoneExt, phoneType);
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
    sb.append("class AppointmentReserveModel {\n");
    sb.append("    appointmentBookingFields: ").append(toIndentedString(appointmentBookingFields)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    customerBookingFields: ").append(toIndentedString(customerBookingFields)).append("\n");
    sb.append("    customerMessage: ").append(toIndentedString(customerMessage)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    phone: ").append(toIndentedString(phone)).append("\n");
    sb.append("    phoneExt: ").append(toIndentedString(phoneExt)).append("\n");
    sb.append("    phoneType: ").append(toIndentedString(phoneType)).append("\n");
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
    openapiFields.add("appointmentBookingFields");
    openapiFields.add("customFields");
    openapiFields.add("customerBookingFields");
    openapiFields.add("customerMessage");
    openapiFields.add("email");
    openapiFields.add("name");
    openapiFields.add("notes");
    openapiFields.add("phone");
    openapiFields.add("phoneExt");
    openapiFields.add("phoneType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AppointmentReserveModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AppointmentReserveModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AppointmentReserveModel is not found in the empty JSON string", AppointmentReserveModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AppointmentReserveModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AppointmentReserveModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("appointmentBookingFields") != null && !jsonObj.get("appointmentBookingFields").isJsonNull()) {
        JsonArray jsonArrayappointmentBookingFields = jsonObj.getAsJsonArray("appointmentBookingFields");
        if (jsonArrayappointmentBookingFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("appointmentBookingFields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `appointmentBookingFields` to be an array in the JSON string but got `%s`", jsonObj.get("appointmentBookingFields").toString()));
          }

          // validate the optional field `appointmentBookingFields` (array)
          for (int i = 0; i < jsonArrayappointmentBookingFields.size(); i++) {
            BookingFieldItem.validateJsonElement(jsonArrayappointmentBookingFields.get(i));
          };
        }
      }
      // validate the optional field `customFields`
      if (jsonObj.get("customFields") != null && !jsonObj.get("customFields").isJsonNull()) {
        CustomFieldInputModel.validateJsonElement(jsonObj.get("customFields"));
      }
      if (jsonObj.get("customerBookingFields") != null && !jsonObj.get("customerBookingFields").isJsonNull()) {
        JsonArray jsonArraycustomerBookingFields = jsonObj.getAsJsonArray("customerBookingFields");
        if (jsonArraycustomerBookingFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("customerBookingFields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `customerBookingFields` to be an array in the JSON string but got `%s`", jsonObj.get("customerBookingFields").toString()));
          }

          // validate the optional field `customerBookingFields` (array)
          for (int i = 0; i < jsonArraycustomerBookingFields.size(); i++) {
            BookingFieldItem.validateJsonElement(jsonArraycustomerBookingFields.get(i));
          };
        }
      }
      if ((jsonObj.get("customerMessage") != null && !jsonObj.get("customerMessage").isJsonNull()) && !jsonObj.get("customerMessage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customerMessage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customerMessage").toString()));
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("notes") != null && !jsonObj.get("notes").isJsonNull()) && !jsonObj.get("notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("notes").toString()));
      }
      if ((jsonObj.get("phone") != null && !jsonObj.get("phone").isJsonNull()) && !jsonObj.get("phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phone").toString()));
      }
      if ((jsonObj.get("phoneExt") != null && !jsonObj.get("phoneExt").isJsonNull()) && !jsonObj.get("phoneExt").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phoneExt` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phoneExt").toString()));
      }
      if ((jsonObj.get("phoneType") != null && !jsonObj.get("phoneType").isJsonNull()) && !jsonObj.get("phoneType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phoneType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phoneType").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AppointmentReserveModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AppointmentReserveModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AppointmentReserveModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AppointmentReserveModel.class));

       return (TypeAdapter<T>) new TypeAdapter<AppointmentReserveModel>() {
           @Override
           public void write(JsonWriter out, AppointmentReserveModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AppointmentReserveModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AppointmentReserveModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AppointmentReserveModel
   * @throws IOException if the JSON string is invalid with respect to AppointmentReserveModel
   */
  public static AppointmentReserveModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AppointmentReserveModel.class);
  }

  /**
   * Convert an instance of AppointmentReserveModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

