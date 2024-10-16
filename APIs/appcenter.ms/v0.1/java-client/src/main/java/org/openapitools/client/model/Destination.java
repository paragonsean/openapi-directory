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
 * Destination
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Destination {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_IS_LATEST = "is_latest";
  @SerializedName(SERIALIZED_NAME_IS_LATEST)
  private Boolean isLatest;

  public static final String SERIALIZED_NAME_PUBLISHING_STATUS = "publishing_status";
  @SerializedName(SERIALIZED_NAME_PUBLISHING_STATUS)
  private String publishingStatus;

  /**
   * type of the distribution store currently stores type can be intune, googleplay or windows.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    INTUNE("intune"),
    
    GOOGLEPLAY("googleplay"),
    
    APPLE("apple"),
    
    NONE("none");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  /**
   * Destination can be either store or group.
   */
  @JsonAdapter(DestinationTypeEnum.Adapter.class)
  public enum DestinationTypeEnum {
    GROUP("group"),
    
    STORE("store"),
    
    TESTER("tester");

    private String value;

    DestinationTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static DestinationTypeEnum fromValue(String value) {
      for (DestinationTypeEnum b : DestinationTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<DestinationTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final DestinationTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public DestinationTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return DestinationTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      DestinationTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_DESTINATION_TYPE = "destination_type";
  @SerializedName(SERIALIZED_NAME_DESTINATION_TYPE)
  private DestinationTypeEnum destinationType;

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "display_name";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public Destination() {
  }

  public Destination id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Id of a distribution group / store. The release will be associated with this distribution group / store. If the distribution group / store doesn&#39;t exist a 400 is returned. If both distribution group / store name and id are passed, the id is taking precedence.
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public Destination name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of a distribution group / distribution store. The release will be associated with this distribution group or store. If the distribution group / store doesn&#39;t exist a 400 is returned. If both distribution group / store name and id are passed, the id is taking precedence.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Destination isLatest(Boolean isLatest) {
    this.isLatest = isLatest;
    return this;
  }

  /**
   * Is the containing release the latest one in this distribution store.
   * @return isLatest
   */
  @javax.annotation.Nullable
  public Boolean getIsLatest() {
    return isLatest;
  }

  public void setIsLatest(Boolean isLatest) {
    this.isLatest = isLatest;
  }


  public Destination publishingStatus(String publishingStatus) {
    this.publishingStatus = publishingStatus;
    return this;
  }

  /**
   * publishing status of the release in the store.
   * @return publishingStatus
   */
  @javax.annotation.Nullable
  public String getPublishingStatus() {
    return publishingStatus;
  }

  public void setPublishingStatus(String publishingStatus) {
    this.publishingStatus = publishingStatus;
  }


  public Destination type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * type of the distribution store currently stores type can be intune, googleplay or windows.
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }


  public Destination destinationType(DestinationTypeEnum destinationType) {
    this.destinationType = destinationType;
    return this;
  }

  /**
   * Destination can be either store or group.
   * @return destinationType
   */
  @javax.annotation.Nullable
  public DestinationTypeEnum getDestinationType() {
    return destinationType;
  }

  public void setDestinationType(DestinationTypeEnum destinationType) {
    this.destinationType = destinationType;
  }


  public Destination displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * Display name for the group or tester
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Destination destination = (Destination) o;
    return Objects.equals(this.id, destination.id) &&
        Objects.equals(this.name, destination.name) &&
        Objects.equals(this.isLatest, destination.isLatest) &&
        Objects.equals(this.publishingStatus, destination.publishingStatus) &&
        Objects.equals(this.type, destination.type) &&
        Objects.equals(this.destinationType, destination.destinationType) &&
        Objects.equals(this.displayName, destination.displayName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, name, isLatest, publishingStatus, type, destinationType, displayName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Destination {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    isLatest: ").append(toIndentedString(isLatest)).append("\n");
    sb.append("    publishingStatus: ").append(toIndentedString(publishingStatus)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    destinationType: ").append(toIndentedString(destinationType)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("is_latest");
    openapiFields.add("publishing_status");
    openapiFields.add("type");
    openapiFields.add("destination_type");
    openapiFields.add("display_name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Destination
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Destination.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Destination is not found in the empty JSON string", Destination.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Destination.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Destination` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Destination.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("publishing_status") != null && !jsonObj.get("publishing_status").isJsonNull()) && !jsonObj.get("publishing_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publishing_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publishing_status").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
      if ((jsonObj.get("destination_type") != null && !jsonObj.get("destination_type").isJsonNull()) && !jsonObj.get("destination_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `destination_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("destination_type").toString()));
      }
      // validate the optional field `destination_type`
      if (jsonObj.get("destination_type") != null && !jsonObj.get("destination_type").isJsonNull()) {
        DestinationTypeEnum.validateJsonElement(jsonObj.get("destination_type"));
      }
      if ((jsonObj.get("display_name") != null && !jsonObj.get("display_name").isJsonNull()) && !jsonObj.get("display_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `display_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("display_name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Destination.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Destination' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Destination> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Destination.class));

       return (TypeAdapter<T>) new TypeAdapter<Destination>() {
           @Override
           public void write(JsonWriter out, Destination value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Destination read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Destination given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Destination
   * @throws IOException if the JSON string is invalid with respect to Destination
   */
  public static Destination fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Destination.class);
  }

  /**
   * Convert an instance of Destination to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

