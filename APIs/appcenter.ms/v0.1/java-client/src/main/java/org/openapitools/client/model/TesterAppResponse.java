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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.UUID;
import org.openapitools.client.model.AppsList200ResponseInnerAllOfOwner;

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
 * TesterAppResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TesterAppResponse {
  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "display_name";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public static final String SERIALIZED_NAME_ICON_SOURCE = "icon_source";
  @SerializedName(SERIALIZED_NAME_ICON_SOURCE)
  private String iconSource;

  public static final String SERIALIZED_NAME_ICON_URL = "icon_url";
  @SerializedName(SERIALIZED_NAME_ICON_URL)
  private String iconUrl;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  /**
   * The OS the app will be running on
   */
  @JsonAdapter(OsEnum.Adapter.class)
  public enum OsEnum {
    ANDROID("Android"),
    
    I_OS("iOS"),
    
    MAC_OS("macOS"),
    
    TIZEN("Tizen"),
    
    TV_OS("tvOS"),
    
    WINDOWS("Windows"),
    
    LINUX("Linux"),
    
    CUSTOM("Custom");

    private String value;

    OsEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static OsEnum fromValue(String value) {
      for (OsEnum b : OsEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<OsEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final OsEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public OsEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return OsEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      OsEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_OS = "os";
  @SerializedName(SERIALIZED_NAME_OS)
  private OsEnum os;

  public static final String SERIALIZED_NAME_OWNER = "owner";
  @SerializedName(SERIALIZED_NAME_OWNER)
  private AppsList200ResponseInnerAllOfOwner owner;

  public static final String SERIALIZED_NAME_RELEASE_TYPE = "release_type";
  @SerializedName(SERIALIZED_NAME_RELEASE_TYPE)
  private String releaseType;

  public static final String SERIALIZED_NAME_MICROSOFT_INTERNAL = "microsoft_internal";
  @SerializedName(SERIALIZED_NAME_MICROSOFT_INTERNAL)
  private Boolean microsoftInternal;

  /**
   * Gets or Sets permissions
   */
  @JsonAdapter(PermissionsEnum.Adapter.class)
  public enum PermissionsEnum {
    CAN_REMOVE_FROM_APP("can_remove_from_app");

    private String value;

    PermissionsEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PermissionsEnum fromValue(String value) {
      for (PermissionsEnum b : PermissionsEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PermissionsEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PermissionsEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PermissionsEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PermissionsEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PermissionsEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PERMISSIONS = "permissions";
  @SerializedName(SERIALIZED_NAME_PERMISSIONS)
  private List<PermissionsEnum> permissions = new ArrayList<>();

  public TesterAppResponse() {
  }

  public TesterAppResponse description(String description) {
    this.description = description;
    return this;
  }

  /**
   * The description of the app
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public TesterAppResponse displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * The display name of the app
   * @return displayName
   */
  @javax.annotation.Nonnull
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }


  public TesterAppResponse iconSource(String iconSource) {
    this.iconSource = iconSource;
    return this;
  }

  /**
   * The string representation of the source of the app&#39;s icon
   * @return iconSource
   */
  @javax.annotation.Nullable
  public String getIconSource() {
    return iconSource;
  }

  public void setIconSource(String iconSource) {
    this.iconSource = iconSource;
  }


  public TesterAppResponse iconUrl(String iconUrl) {
    this.iconUrl = iconUrl;
    return this;
  }

  /**
   * The string representation of the URL pointing to the app&#39;s icon
   * @return iconUrl
   */
  @javax.annotation.Nullable
  public String getIconUrl() {
    return iconUrl;
  }

  public void setIconUrl(String iconUrl) {
    this.iconUrl = iconUrl;
  }


  public TesterAppResponse id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * The unique ID (UUID) of the app
   * @return id
   */
  @javax.annotation.Nonnull
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public TesterAppResponse name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the app used in URLs
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public TesterAppResponse os(OsEnum os) {
    this.os = os;
    return this;
  }

  /**
   * The OS the app will be running on
   * @return os
   */
  @javax.annotation.Nonnull
  public OsEnum getOs() {
    return os;
  }

  public void setOs(OsEnum os) {
    this.os = os;
  }


  public TesterAppResponse owner(AppsList200ResponseInnerAllOfOwner owner) {
    this.owner = owner;
    return this;
  }

  /**
   * Get owner
   * @return owner
   */
  @javax.annotation.Nonnull
  public AppsList200ResponseInnerAllOfOwner getOwner() {
    return owner;
  }

  public void setOwner(AppsList200ResponseInnerAllOfOwner owner) {
    this.owner = owner;
  }


  public TesterAppResponse releaseType(String releaseType) {
    this.releaseType = releaseType;
    return this;
  }

  /**
   * A one-word descriptive release-type value that starts with a capital letter but is otherwise lowercase
   * @return releaseType
   */
  @javax.annotation.Nullable
  public String getReleaseType() {
    return releaseType;
  }

  public void setReleaseType(String releaseType) {
    this.releaseType = releaseType;
  }


  public TesterAppResponse microsoftInternal(Boolean microsoftInternal) {
    this.microsoftInternal = microsoftInternal;
    return this;
  }

  /**
   * it indicates if the app is microsoft internal
   * @return microsoftInternal
   */
  @javax.annotation.Nullable
  public Boolean getMicrosoftInternal() {
    return microsoftInternal;
  }

  public void setMicrosoftInternal(Boolean microsoftInternal) {
    this.microsoftInternal = microsoftInternal;
  }


  public TesterAppResponse permissions(List<PermissionsEnum> permissions) {
    this.permissions = permissions;
    return this;
  }

  public TesterAppResponse addPermissionsItem(PermissionsEnum permissionsItem) {
    if (this.permissions == null) {
      this.permissions = new ArrayList<>();
    }
    this.permissions.add(permissionsItem);
    return this;
  }

  /**
   * The permissions associated with the app
   * @return permissions
   */
  @javax.annotation.Nullable
  public List<PermissionsEnum> getPermissions() {
    return permissions;
  }

  public void setPermissions(List<PermissionsEnum> permissions) {
    this.permissions = permissions;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TesterAppResponse testerAppResponse = (TesterAppResponse) o;
    return Objects.equals(this.description, testerAppResponse.description) &&
        Objects.equals(this.displayName, testerAppResponse.displayName) &&
        Objects.equals(this.iconSource, testerAppResponse.iconSource) &&
        Objects.equals(this.iconUrl, testerAppResponse.iconUrl) &&
        Objects.equals(this.id, testerAppResponse.id) &&
        Objects.equals(this.name, testerAppResponse.name) &&
        Objects.equals(this.os, testerAppResponse.os) &&
        Objects.equals(this.owner, testerAppResponse.owner) &&
        Objects.equals(this.releaseType, testerAppResponse.releaseType) &&
        Objects.equals(this.microsoftInternal, testerAppResponse.microsoftInternal) &&
        Objects.equals(this.permissions, testerAppResponse.permissions);
  }

  @Override
  public int hashCode() {
    return Objects.hash(description, displayName, iconSource, iconUrl, id, name, os, owner, releaseType, microsoftInternal, permissions);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TesterAppResponse {\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    iconSource: ").append(toIndentedString(iconSource)).append("\n");
    sb.append("    iconUrl: ").append(toIndentedString(iconUrl)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    os: ").append(toIndentedString(os)).append("\n");
    sb.append("    owner: ").append(toIndentedString(owner)).append("\n");
    sb.append("    releaseType: ").append(toIndentedString(releaseType)).append("\n");
    sb.append("    microsoftInternal: ").append(toIndentedString(microsoftInternal)).append("\n");
    sb.append("    permissions: ").append(toIndentedString(permissions)).append("\n");
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
    openapiFields.add("description");
    openapiFields.add("display_name");
    openapiFields.add("icon_source");
    openapiFields.add("icon_url");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("os");
    openapiFields.add("owner");
    openapiFields.add("release_type");
    openapiFields.add("microsoft_internal");
    openapiFields.add("permissions");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("display_name");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("os");
    openapiRequiredFields.add("owner");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TesterAppResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TesterAppResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TesterAppResponse is not found in the empty JSON string", TesterAppResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TesterAppResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TesterAppResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : TesterAppResponse.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if (!jsonObj.get("display_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `display_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("display_name").toString()));
      }
      if ((jsonObj.get("icon_source") != null && !jsonObj.get("icon_source").isJsonNull()) && !jsonObj.get("icon_source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `icon_source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("icon_source").toString()));
      }
      if ((jsonObj.get("icon_url") != null && !jsonObj.get("icon_url").isJsonNull()) && !jsonObj.get("icon_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `icon_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("icon_url").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (!jsonObj.get("os").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `os` to be a primitive type in the JSON string but got `%s`", jsonObj.get("os").toString()));
      }
      // validate the required field `os`
      OsEnum.validateJsonElement(jsonObj.get("os"));
      // validate the required field `owner`
      AppsList200ResponseInnerAllOfOwner.validateJsonElement(jsonObj.get("owner"));
      if ((jsonObj.get("release_type") != null && !jsonObj.get("release_type").isJsonNull()) && !jsonObj.get("release_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `release_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("release_type").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("permissions") != null && !jsonObj.get("permissions").isJsonNull() && !jsonObj.get("permissions").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `permissions` to be an array in the JSON string but got `%s`", jsonObj.get("permissions").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TesterAppResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TesterAppResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TesterAppResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TesterAppResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<TesterAppResponse>() {
           @Override
           public void write(JsonWriter out, TesterAppResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TesterAppResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TesterAppResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TesterAppResponse
   * @throws IOException if the JSON string is invalid with respect to TesterAppResponse
   */
  public static TesterAppResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TesterAppResponse.class);
  }

  /**
   * Convert an instance of TesterAppResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

