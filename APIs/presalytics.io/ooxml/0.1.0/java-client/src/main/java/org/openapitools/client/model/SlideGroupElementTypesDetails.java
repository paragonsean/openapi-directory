/*
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
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
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.UUID;
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
 * SlideGroupElementTypesDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:20.731713-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SlideGroupElementTypesDetails {
  public static final String SERIALIZED_NAME_DATE_CREATED = "dateCreated";
  @SerializedName(SERIALIZED_NAME_DATE_CREATED)
  private OffsetDateTime dateCreated;

  public static final String SERIALIZED_NAME_DATE_MODIFIED = "dateModified";
  @SerializedName(SERIALIZED_NAME_DATE_MODIFIED)
  private OffsetDateTime dateModified;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_TYPE_ID = "typeId";
  @SerializedName(SERIALIZED_NAME_TYPE_ID)
  private Integer typeId;

  public static final String SERIALIZED_NAME_USER_CREATED = "userCreated";
  @SerializedName(SERIALIZED_NAME_USER_CREATED)
  private UUID userCreated;

  public static final String SERIALIZED_NAME_USER_MODIFIED = "userModified";
  @SerializedName(SERIALIZED_NAME_USER_MODIFIED)
  private UUID userModified;

  public SlideGroupElementTypesDetails() {
  }

  public SlideGroupElementTypesDetails dateCreated(OffsetDateTime dateCreated) {
    this.dateCreated = dateCreated;
    return this;
  }

  /**
   * Get dateCreated
   * @return dateCreated
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateCreated() {
    return dateCreated;
  }

  public void setDateCreated(OffsetDateTime dateCreated) {
    this.dateCreated = dateCreated;
  }


  public SlideGroupElementTypesDetails dateModified(OffsetDateTime dateModified) {
    this.dateModified = dateModified;
    return this;
  }

  /**
   * Get dateModified
   * @return dateModified
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateModified() {
    return dateModified;
  }

  public void setDateModified(OffsetDateTime dateModified) {
    this.dateModified = dateModified;
  }


  public SlideGroupElementTypesDetails description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public SlideGroupElementTypesDetails id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public SlideGroupElementTypesDetails name(String name) {
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


  public SlideGroupElementTypesDetails typeId(Integer typeId) {
    this.typeId = typeId;
    return this;
  }

  /**
   * Get typeId
   * @return typeId
   */
  @javax.annotation.Nullable
  public Integer getTypeId() {
    return typeId;
  }

  public void setTypeId(Integer typeId) {
    this.typeId = typeId;
  }


  public SlideGroupElementTypesDetails userCreated(UUID userCreated) {
    this.userCreated = userCreated;
    return this;
  }

  /**
   * Get userCreated
   * @return userCreated
   */
  @javax.annotation.Nullable
  public UUID getUserCreated() {
    return userCreated;
  }

  public void setUserCreated(UUID userCreated) {
    this.userCreated = userCreated;
  }


  public SlideGroupElementTypesDetails userModified(UUID userModified) {
    this.userModified = userModified;
    return this;
  }

  /**
   * Get userModified
   * @return userModified
   */
  @javax.annotation.Nullable
  public UUID getUserModified() {
    return userModified;
  }

  public void setUserModified(UUID userModified) {
    this.userModified = userModified;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SlideGroupElementTypesDetails slideGroupElementTypesDetails = (SlideGroupElementTypesDetails) o;
    return Objects.equals(this.dateCreated, slideGroupElementTypesDetails.dateCreated) &&
        Objects.equals(this.dateModified, slideGroupElementTypesDetails.dateModified) &&
        Objects.equals(this.description, slideGroupElementTypesDetails.description) &&
        Objects.equals(this.id, slideGroupElementTypesDetails.id) &&
        Objects.equals(this.name, slideGroupElementTypesDetails.name) &&
        Objects.equals(this.typeId, slideGroupElementTypesDetails.typeId) &&
        Objects.equals(this.userCreated, slideGroupElementTypesDetails.userCreated) &&
        Objects.equals(this.userModified, slideGroupElementTypesDetails.userModified);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(dateCreated, dateModified, description, id, name, typeId, userCreated, userModified);
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
    sb.append("class SlideGroupElementTypesDetails {\n");
    sb.append("    dateCreated: ").append(toIndentedString(dateCreated)).append("\n");
    sb.append("    dateModified: ").append(toIndentedString(dateModified)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    typeId: ").append(toIndentedString(typeId)).append("\n");
    sb.append("    userCreated: ").append(toIndentedString(userCreated)).append("\n");
    sb.append("    userModified: ").append(toIndentedString(userModified)).append("\n");
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
    openapiFields.add("dateCreated");
    openapiFields.add("dateModified");
    openapiFields.add("description");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("typeId");
    openapiFields.add("userCreated");
    openapiFields.add("userModified");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SlideGroupElementTypesDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SlideGroupElementTypesDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SlideGroupElementTypesDetails is not found in the empty JSON string", SlideGroupElementTypesDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SlideGroupElementTypesDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SlideGroupElementTypesDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("userCreated") != null && !jsonObj.get("userCreated").isJsonNull()) && !jsonObj.get("userCreated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userCreated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userCreated").toString()));
      }
      if ((jsonObj.get("userModified") != null && !jsonObj.get("userModified").isJsonNull()) && !jsonObj.get("userModified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userModified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userModified").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SlideGroupElementTypesDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SlideGroupElementTypesDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SlideGroupElementTypesDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SlideGroupElementTypesDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<SlideGroupElementTypesDetails>() {
           @Override
           public void write(JsonWriter out, SlideGroupElementTypesDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SlideGroupElementTypesDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SlideGroupElementTypesDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SlideGroupElementTypesDetails
   * @throws IOException if the JSON string is invalid with respect to SlideGroupElementTypesDetails
   */
  public static SlideGroupElementTypesDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SlideGroupElementTypesDetails.class);
  }

  /**
   * Convert an instance of SlideGroupElementTypesDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

