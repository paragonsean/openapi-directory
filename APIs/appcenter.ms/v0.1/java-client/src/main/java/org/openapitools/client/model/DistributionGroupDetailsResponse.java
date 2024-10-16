/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.UUID;
import org.openapitools.client.model.DistributionGroupsListUsers200ResponseInner;

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
 * DistributionGroupDetailsResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DistributionGroupDetailsResponse {
  public static final String SERIALIZED_NAME_DISPLAY_NAME = "display_name";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_IS_PUBLIC = "is_public";
  @SerializedName(SERIALIZED_NAME_IS_PUBLIC)
  private Boolean isPublic;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  /**
   * The creation origin of this distribution group
   */
  @JsonAdapter(OriginEnum.Adapter.class)
  public enum OriginEnum {
    APPCENTER("appcenter"),
    
    HOCKEYAPP("hockeyapp");

    private String value;

    OriginEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static OriginEnum fromValue(String value) {
      for (OriginEnum b : OriginEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<OriginEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final OriginEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public OriginEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return OriginEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      OriginEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ORIGIN = "origin";
  @SerializedName(SERIALIZED_NAME_ORIGIN)
  private OriginEnum origin;

  /**
   * Type of group (Default, HockeyAppDefault or MicrosoftDogfooding)
   */
  @JsonAdapter(GroupTypeEnum.Adapter.class)
  public enum GroupTypeEnum {
    DEFAULT("Default"),
    
    HOCKEY_APP_DEFAULT("HockeyAppDefault"),
    
    MICROSOFT_DOGFOODING("MicrosoftDogfooding");

    private String value;

    GroupTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static GroupTypeEnum fromValue(String value) {
      for (GroupTypeEnum b : GroupTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<GroupTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final GroupTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public GroupTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return GroupTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      GroupTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_GROUP_TYPE = "group_type";
  @SerializedName(SERIALIZED_NAME_GROUP_TYPE)
  private GroupTypeEnum groupType;

  public static final String SERIALIZED_NAME_IS_SHARED = "is_shared";
  @SerializedName(SERIALIZED_NAME_IS_SHARED)
  private Boolean isShared;

  public static final String SERIALIZED_NAME_NOTIFIED_USER_COUNT = "notified_user_count";
  @SerializedName(SERIALIZED_NAME_NOTIFIED_USER_COUNT)
  private BigDecimal notifiedUserCount;

  public static final String SERIALIZED_NAME_TOTAL_APPS_COUNT = "total_apps_count";
  @SerializedName(SERIALIZED_NAME_TOTAL_APPS_COUNT)
  private BigDecimal totalAppsCount;

  public static final String SERIALIZED_NAME_TOTAL_USER_COUNT = "total_user_count";
  @SerializedName(SERIALIZED_NAME_TOTAL_USER_COUNT)
  private BigDecimal totalUserCount;

  public static final String SERIALIZED_NAME_USERS = "users";
  @SerializedName(SERIALIZED_NAME_USERS)
  private List<DistributionGroupsListUsers200ResponseInner> users = new ArrayList<>();

  public DistributionGroupDetailsResponse() {
  }

  public DistributionGroupDetailsResponse displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * The name of the distribution group
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }


  public DistributionGroupDetailsResponse id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * The unique ID of the distribution group
   * @return id
   */
  @javax.annotation.Nonnull
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public DistributionGroupDetailsResponse isPublic(Boolean isPublic) {
    this.isPublic = isPublic;
    return this;
  }

  /**
   * Whether the distribution group is public
   * @return isPublic
   */
  @javax.annotation.Nonnull
  public Boolean getIsPublic() {
    return isPublic;
  }

  public void setIsPublic(Boolean isPublic) {
    this.isPublic = isPublic;
  }


  public DistributionGroupDetailsResponse name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the distribution group used in URLs
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public DistributionGroupDetailsResponse origin(OriginEnum origin) {
    this.origin = origin;
    return this;
  }

  /**
   * The creation origin of this distribution group
   * @return origin
   */
  @javax.annotation.Nonnull
  public OriginEnum getOrigin() {
    return origin;
  }

  public void setOrigin(OriginEnum origin) {
    this.origin = origin;
  }


  public DistributionGroupDetailsResponse groupType(GroupTypeEnum groupType) {
    this.groupType = groupType;
    return this;
  }

  /**
   * Type of group (Default, HockeyAppDefault or MicrosoftDogfooding)
   * @return groupType
   */
  @javax.annotation.Nullable
  public GroupTypeEnum getGroupType() {
    return groupType;
  }

  public void setGroupType(GroupTypeEnum groupType) {
    this.groupType = groupType;
  }


  public DistributionGroupDetailsResponse isShared(Boolean isShared) {
    this.isShared = isShared;
    return this;
  }

  /**
   * Whether the distribution group is shared group or not
   * @return isShared
   */
  @javax.annotation.Nonnull
  public Boolean getIsShared() {
    return isShared;
  }

  public void setIsShared(Boolean isShared) {
    this.isShared = isShared;
  }


  public DistributionGroupDetailsResponse notifiedUserCount(BigDecimal notifiedUserCount) {
    this.notifiedUserCount = notifiedUserCount;
    return this;
  }

  /**
   * The count of non-pending users in the distribution group who will be notified by new releases
   * @return notifiedUserCount
   */
  @javax.annotation.Nonnull
  public BigDecimal getNotifiedUserCount() {
    return notifiedUserCount;
  }

  public void setNotifiedUserCount(BigDecimal notifiedUserCount) {
    this.notifiedUserCount = notifiedUserCount;
  }


  public DistributionGroupDetailsResponse totalAppsCount(BigDecimal totalAppsCount) {
    this.totalAppsCount = totalAppsCount;
    return this;
  }

  /**
   * The count of apps associated with this distribution group
   * @return totalAppsCount
   */
  @javax.annotation.Nonnull
  public BigDecimal getTotalAppsCount() {
    return totalAppsCount;
  }

  public void setTotalAppsCount(BigDecimal totalAppsCount) {
    this.totalAppsCount = totalAppsCount;
  }


  public DistributionGroupDetailsResponse totalUserCount(BigDecimal totalUserCount) {
    this.totalUserCount = totalUserCount;
    return this;
  }

  /**
   * The count of users in the distribution group
   * @return totalUserCount
   */
  @javax.annotation.Nonnull
  public BigDecimal getTotalUserCount() {
    return totalUserCount;
  }

  public void setTotalUserCount(BigDecimal totalUserCount) {
    this.totalUserCount = totalUserCount;
  }


  public DistributionGroupDetailsResponse users(List<DistributionGroupsListUsers200ResponseInner> users) {
    this.users = users;
    return this;
  }

  public DistributionGroupDetailsResponse addUsersItem(DistributionGroupsListUsers200ResponseInner usersItem) {
    if (this.users == null) {
      this.users = new ArrayList<>();
    }
    this.users.add(usersItem);
    return this;
  }

  /**
   * The distribution group users
   * @return users
   */
  @javax.annotation.Nonnull
  public List<DistributionGroupsListUsers200ResponseInner> getUsers() {
    return users;
  }

  public void setUsers(List<DistributionGroupsListUsers200ResponseInner> users) {
    this.users = users;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DistributionGroupDetailsResponse distributionGroupDetailsResponse = (DistributionGroupDetailsResponse) o;
    return Objects.equals(this.displayName, distributionGroupDetailsResponse.displayName) &&
        Objects.equals(this.id, distributionGroupDetailsResponse.id) &&
        Objects.equals(this.isPublic, distributionGroupDetailsResponse.isPublic) &&
        Objects.equals(this.name, distributionGroupDetailsResponse.name) &&
        Objects.equals(this.origin, distributionGroupDetailsResponse.origin) &&
        Objects.equals(this.groupType, distributionGroupDetailsResponse.groupType) &&
        Objects.equals(this.isShared, distributionGroupDetailsResponse.isShared) &&
        Objects.equals(this.notifiedUserCount, distributionGroupDetailsResponse.notifiedUserCount) &&
        Objects.equals(this.totalAppsCount, distributionGroupDetailsResponse.totalAppsCount) &&
        Objects.equals(this.totalUserCount, distributionGroupDetailsResponse.totalUserCount) &&
        Objects.equals(this.users, distributionGroupDetailsResponse.users);
  }

  @Override
  public int hashCode() {
    return Objects.hash(displayName, id, isPublic, name, origin, groupType, isShared, notifiedUserCount, totalAppsCount, totalUserCount, users);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DistributionGroupDetailsResponse {\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isPublic: ").append(toIndentedString(isPublic)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    origin: ").append(toIndentedString(origin)).append("\n");
    sb.append("    groupType: ").append(toIndentedString(groupType)).append("\n");
    sb.append("    isShared: ").append(toIndentedString(isShared)).append("\n");
    sb.append("    notifiedUserCount: ").append(toIndentedString(notifiedUserCount)).append("\n");
    sb.append("    totalAppsCount: ").append(toIndentedString(totalAppsCount)).append("\n");
    sb.append("    totalUserCount: ").append(toIndentedString(totalUserCount)).append("\n");
    sb.append("    users: ").append(toIndentedString(users)).append("\n");
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
    openapiFields.add("display_name");
    openapiFields.add("id");
    openapiFields.add("is_public");
    openapiFields.add("name");
    openapiFields.add("origin");
    openapiFields.add("group_type");
    openapiFields.add("is_shared");
    openapiFields.add("notified_user_count");
    openapiFields.add("total_apps_count");
    openapiFields.add("total_user_count");
    openapiFields.add("users");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("is_public");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("origin");
    openapiRequiredFields.add("is_shared");
    openapiRequiredFields.add("notified_user_count");
    openapiRequiredFields.add("total_apps_count");
    openapiRequiredFields.add("total_user_count");
    openapiRequiredFields.add("users");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DistributionGroupDetailsResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DistributionGroupDetailsResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DistributionGroupDetailsResponse is not found in the empty JSON string", DistributionGroupDetailsResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DistributionGroupDetailsResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DistributionGroupDetailsResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DistributionGroupDetailsResponse.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("display_name") != null && !jsonObj.get("display_name").isJsonNull()) && !jsonObj.get("display_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `display_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("display_name").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (!jsonObj.get("origin").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `origin` to be a primitive type in the JSON string but got `%s`", jsonObj.get("origin").toString()));
      }
      // validate the required field `origin`
      OriginEnum.validateJsonElement(jsonObj.get("origin"));
      if ((jsonObj.get("group_type") != null && !jsonObj.get("group_type").isJsonNull()) && !jsonObj.get("group_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `group_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("group_type").toString()));
      }
      // validate the optional field `group_type`
      if (jsonObj.get("group_type") != null && !jsonObj.get("group_type").isJsonNull()) {
        GroupTypeEnum.validateJsonElement(jsonObj.get("group_type"));
      }
      // ensure the json data is an array
      if (!jsonObj.get("users").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `users` to be an array in the JSON string but got `%s`", jsonObj.get("users").toString()));
      }

      JsonArray jsonArrayusers = jsonObj.getAsJsonArray("users");
      // validate the required field `users` (array)
      for (int i = 0; i < jsonArrayusers.size(); i++) {
        DistributionGroupsListUsers200ResponseInner.validateJsonElement(jsonArrayusers.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DistributionGroupDetailsResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DistributionGroupDetailsResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DistributionGroupDetailsResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DistributionGroupDetailsResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<DistributionGroupDetailsResponse>() {
           @Override
           public void write(JsonWriter out, DistributionGroupDetailsResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DistributionGroupDetailsResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DistributionGroupDetailsResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DistributionGroupDetailsResponse
   * @throws IOException if the JSON string is invalid with respect to DistributionGroupDetailsResponse
   */
  public static DistributionGroupDetailsResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DistributionGroupDetailsResponse.class);
  }

  /**
   * Convert an instance of DistributionGroupDetailsResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

