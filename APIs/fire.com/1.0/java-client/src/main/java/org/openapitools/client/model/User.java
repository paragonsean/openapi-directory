/*
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
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
import org.openapitools.client.model.MobileApplication;

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
 * User
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:07.131817-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class User {
  public static final String SERIALIZED_NAME_EMAIL_ADDRESS = "emailAddress";
  @SerializedName(SERIALIZED_NAME_EMAIL_ADDRESS)
  private String emailAddress;

  public static final String SERIALIZED_NAME_FIRST_NAME = "firstName";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_LAST_NAME = "lastName";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_LASTLOGIN = "lastlogin";
  @SerializedName(SERIALIZED_NAME_LASTLOGIN)
  private String lastlogin;

  public static final String SERIALIZED_NAME_MOBILE_APPLICATION_DETAILS = "mobileApplicationDetails";
  @SerializedName(SERIALIZED_NAME_MOBILE_APPLICATION_DETAILS)
  private MobileApplication mobileApplicationDetails;

  public static final String SERIALIZED_NAME_MOBILE_NUMBER = "mobileNumber";
  @SerializedName(SERIALIZED_NAME_MOBILE_NUMBER)
  private String mobileNumber;

  /**
   * User role
   */
  @JsonAdapter(RoleEnum.Adapter.class)
  public enum RoleEnum {
    ADMIN("ADMIN"),
    
    FULL_USER("FULL_USER"),
    
    READ_ONLY("READ_ONLY"),
    
    CARD_ONLY("CARD_ONLY");

    private String value;

    RoleEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RoleEnum fromValue(String value) {
      for (RoleEnum b : RoleEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RoleEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RoleEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RoleEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RoleEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RoleEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ROLE = "role";
  @SerializedName(SERIALIZED_NAME_ROLE)
  private RoleEnum role;

  /**
   * Status of user
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    LIVE("LIVE"),
    
    CLOSED("CLOSED"),
    
    FROZEN("FROZEN"),
    
    INVITE_SENT("INVITE_SENT"),
    
    SMS_CODE_SENT("SMS_CODE_SENT");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_USER_CVL = "userCvl";
  @SerializedName(SERIALIZED_NAME_USER_CVL)
  private String userCvl;

  public User() {
  }

  public User emailAddress(String emailAddress) {
    this.emailAddress = emailAddress;
    return this;
  }

  /**
   * email address for user
   * @return emailAddress
   */
  @javax.annotation.Nullable
  public String getEmailAddress() {
    return emailAddress;
  }

  public void setEmailAddress(String emailAddress) {
    this.emailAddress = emailAddress;
  }


  public User firstName(String firstName) {
    this.firstName = firstName;
    return this;
  }

  /**
   * User first name
   * @return firstName
   */
  @javax.annotation.Nullable
  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  public User id(Long id) {
    this.id = id;
    return this;
  }

  /**
   * The User ID for this User
   * @return id
   */
  @javax.annotation.Nullable
  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }


  public User lastName(String lastName) {
    this.lastName = lastName;
    return this;
  }

  /**
   * User second name
   * @return lastName
   */
  @javax.annotation.Nullable
  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }


  public User lastlogin(String lastlogin) {
    this.lastlogin = lastlogin;
    return this;
  }

  /**
   * Timestamp on when user last logged in.
   * @return lastlogin
   */
  @javax.annotation.Nullable
  public String getLastlogin() {
    return lastlogin;
  }

  public void setLastlogin(String lastlogin) {
    this.lastlogin = lastlogin;
  }


  public User mobileApplicationDetails(MobileApplication mobileApplicationDetails) {
    this.mobileApplicationDetails = mobileApplicationDetails;
    return this;
  }

  /**
   * Get mobileApplicationDetails
   * @return mobileApplicationDetails
   */
  @javax.annotation.Nullable
  public MobileApplication getMobileApplicationDetails() {
    return mobileApplicationDetails;
  }

  public void setMobileApplicationDetails(MobileApplication mobileApplicationDetails) {
    this.mobileApplicationDetails = mobileApplicationDetails;
  }


  public User mobileNumber(String mobileNumber) {
    this.mobileNumber = mobileNumber;
    return this;
  }

  /**
   * User mobile number
   * @return mobileNumber
   */
  @javax.annotation.Nullable
  public String getMobileNumber() {
    return mobileNumber;
  }

  public void setMobileNumber(String mobileNumber) {
    this.mobileNumber = mobileNumber;
  }


  public User role(RoleEnum role) {
    this.role = role;
    return this;
  }

  /**
   * User role
   * @return role
   */
  @javax.annotation.Nullable
  public RoleEnum getRole() {
    return role;
  }

  public void setRole(RoleEnum role) {
    this.role = role;
  }


  public User status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Status of user
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public User userCvl(String userCvl) {
    this.userCvl = userCvl;
    return this;
  }

  /**
   * Users Cvl type ID (shows up when status is LIVE)
   * @return userCvl
   */
  @javax.annotation.Nullable
  public String getUserCvl() {
    return userCvl;
  }

  public void setUserCvl(String userCvl) {
    this.userCvl = userCvl;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    User user = (User) o;
    return Objects.equals(this.emailAddress, user.emailAddress) &&
        Objects.equals(this.firstName, user.firstName) &&
        Objects.equals(this.id, user.id) &&
        Objects.equals(this.lastName, user.lastName) &&
        Objects.equals(this.lastlogin, user.lastlogin) &&
        Objects.equals(this.mobileApplicationDetails, user.mobileApplicationDetails) &&
        Objects.equals(this.mobileNumber, user.mobileNumber) &&
        Objects.equals(this.role, user.role) &&
        Objects.equals(this.status, user.status) &&
        Objects.equals(this.userCvl, user.userCvl);
  }

  @Override
  public int hashCode() {
    return Objects.hash(emailAddress, firstName, id, lastName, lastlogin, mobileApplicationDetails, mobileNumber, role, status, userCvl);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class User {\n");
    sb.append("    emailAddress: ").append(toIndentedString(emailAddress)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    lastlogin: ").append(toIndentedString(lastlogin)).append("\n");
    sb.append("    mobileApplicationDetails: ").append(toIndentedString(mobileApplicationDetails)).append("\n");
    sb.append("    mobileNumber: ").append(toIndentedString(mobileNumber)).append("\n");
    sb.append("    role: ").append(toIndentedString(role)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    userCvl: ").append(toIndentedString(userCvl)).append("\n");
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
    openapiFields.add("emailAddress");
    openapiFields.add("firstName");
    openapiFields.add("id");
    openapiFields.add("lastName");
    openapiFields.add("lastlogin");
    openapiFields.add("mobileApplicationDetails");
    openapiFields.add("mobileNumber");
    openapiFields.add("role");
    openapiFields.add("status");
    openapiFields.add("userCvl");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to User
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!User.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in User is not found in the empty JSON string", User.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!User.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `User` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("emailAddress") != null && !jsonObj.get("emailAddress").isJsonNull()) && !jsonObj.get("emailAddress").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `emailAddress` to be a primitive type in the JSON string but got `%s`", jsonObj.get("emailAddress").toString()));
      }
      if ((jsonObj.get("firstName") != null && !jsonObj.get("firstName").isJsonNull()) && !jsonObj.get("firstName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `firstName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("firstName").toString()));
      }
      if ((jsonObj.get("lastName") != null && !jsonObj.get("lastName").isJsonNull()) && !jsonObj.get("lastName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastName").toString()));
      }
      if ((jsonObj.get("lastlogin") != null && !jsonObj.get("lastlogin").isJsonNull()) && !jsonObj.get("lastlogin").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastlogin` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastlogin").toString()));
      }
      // validate the optional field `mobileApplicationDetails`
      if (jsonObj.get("mobileApplicationDetails") != null && !jsonObj.get("mobileApplicationDetails").isJsonNull()) {
        MobileApplication.validateJsonElement(jsonObj.get("mobileApplicationDetails"));
      }
      if ((jsonObj.get("mobileNumber") != null && !jsonObj.get("mobileNumber").isJsonNull()) && !jsonObj.get("mobileNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mobileNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mobileNumber").toString()));
      }
      if ((jsonObj.get("role") != null && !jsonObj.get("role").isJsonNull()) && !jsonObj.get("role").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `role` to be a primitive type in the JSON string but got `%s`", jsonObj.get("role").toString()));
      }
      // validate the optional field `role`
      if (jsonObj.get("role") != null && !jsonObj.get("role").isJsonNull()) {
        RoleEnum.validateJsonElement(jsonObj.get("role"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if ((jsonObj.get("userCvl") != null && !jsonObj.get("userCvl").isJsonNull()) && !jsonObj.get("userCvl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userCvl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userCvl").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!User.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'User' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<User> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(User.class));

       return (TypeAdapter<T>) new TypeAdapter<User>() {
           @Override
           public void write(JsonWriter out, User value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public User read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of User given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of User
   * @throws IOException if the JSON string is invalid with respect to User
   */
  public static User fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, User.class);
  }

  /**
   * Convert an instance of User to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

