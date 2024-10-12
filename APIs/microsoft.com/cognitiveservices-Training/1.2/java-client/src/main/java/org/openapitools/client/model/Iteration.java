/*
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.2
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
 * Iteration model to be sent over JSON
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:06.339817-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Iteration {
  public static final String SERIALIZED_NAME_CREATED = "Created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private OffsetDateTime created;

  public static final String SERIALIZED_NAME_DOMAIN_ID = "DomainId";
  @SerializedName(SERIALIZED_NAME_DOMAIN_ID)
  private UUID domainId;

  public static final String SERIALIZED_NAME_EXPORTABLE = "Exportable";
  @SerializedName(SERIALIZED_NAME_EXPORTABLE)
  private Boolean exportable;

  public static final String SERIALIZED_NAME_ID = "Id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_IS_DEFAULT = "IsDefault";
  @SerializedName(SERIALIZED_NAME_IS_DEFAULT)
  private Boolean isDefault;

  public static final String SERIALIZED_NAME_LAST_MODIFIED = "LastModified";
  @SerializedName(SERIALIZED_NAME_LAST_MODIFIED)
  private OffsetDateTime lastModified;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PROJECT_ID = "ProjectId";
  @SerializedName(SERIALIZED_NAME_PROJECT_ID)
  private UUID projectId;

  public static final String SERIALIZED_NAME_STATUS = "Status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_TRAINED_AT = "TrainedAt";
  @SerializedName(SERIALIZED_NAME_TRAINED_AT)
  private OffsetDateTime trainedAt;

  public Iteration() {
  }

  public Iteration(
     OffsetDateTime created, 
     UUID domainId, 
     Boolean exportable, 
     UUID id, 
     OffsetDateTime lastModified, 
     UUID projectId, 
     String status, 
     OffsetDateTime trainedAt
  ) {
    this();
    this.created = created;
    this.domainId = domainId;
    this.exportable = exportable;
    this.id = id;
    this.lastModified = lastModified;
    this.projectId = projectId;
    this.status = status;
    this.trainedAt = trainedAt;
  }

  /**
   * Gets the time this iteration was completed
   * @return created
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreated() {
    return created;
  }



  /**
   * Get or sets a guid of the domain the iteration has been trained on
   * @return domainId
   */
  @javax.annotation.Nullable
  public UUID getDomainId() {
    return domainId;
  }



  /**
   * Whether the iteration can be exported to another format for download
   * @return exportable
   */
  @javax.annotation.Nullable
  public Boolean getExportable() {
    return exportable;
  }



  /**
   * Gets the id of the iteration
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }



  public Iteration isDefault(Boolean isDefault) {
    this.isDefault = isDefault;
    return this;
  }

  /**
   * Gets or sets a value indicating whether the iteration is the default iteration for the project
   * @return isDefault
   */
  @javax.annotation.Nullable
  public Boolean getIsDefault() {
    return isDefault;
  }

  public void setIsDefault(Boolean isDefault) {
    this.isDefault = isDefault;
  }


  /**
   * Gets the time this iteration was last modified
   * @return lastModified
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastModified() {
    return lastModified;
  }



  public Iteration name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Gets or sets the name of the iteration
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  /**
   * Gets the project id of the iteration
   * @return projectId
   */
  @javax.annotation.Nullable
  public UUID getProjectId() {
    return projectId;
  }



  /**
   * Gets the current iteration status
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }



  /**
   * Gets the time this iteration was last modified
   * @return trainedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getTrainedAt() {
    return trainedAt;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Iteration iteration = (Iteration) o;
    return Objects.equals(this.created, iteration.created) &&
        Objects.equals(this.domainId, iteration.domainId) &&
        Objects.equals(this.exportable, iteration.exportable) &&
        Objects.equals(this.id, iteration.id) &&
        Objects.equals(this.isDefault, iteration.isDefault) &&
        Objects.equals(this.lastModified, iteration.lastModified) &&
        Objects.equals(this.name, iteration.name) &&
        Objects.equals(this.projectId, iteration.projectId) &&
        Objects.equals(this.status, iteration.status) &&
        Objects.equals(this.trainedAt, iteration.trainedAt);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(created, domainId, exportable, id, isDefault, lastModified, name, projectId, status, trainedAt);
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
    sb.append("class Iteration {\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    domainId: ").append(toIndentedString(domainId)).append("\n");
    sb.append("    exportable: ").append(toIndentedString(exportable)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isDefault: ").append(toIndentedString(isDefault)).append("\n");
    sb.append("    lastModified: ").append(toIndentedString(lastModified)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    projectId: ").append(toIndentedString(projectId)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    trainedAt: ").append(toIndentedString(trainedAt)).append("\n");
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
    openapiFields.add("Created");
    openapiFields.add("DomainId");
    openapiFields.add("Exportable");
    openapiFields.add("Id");
    openapiFields.add("IsDefault");
    openapiFields.add("LastModified");
    openapiFields.add("Name");
    openapiFields.add("ProjectId");
    openapiFields.add("Status");
    openapiFields.add("TrainedAt");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Iteration
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Iteration.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Iteration is not found in the empty JSON string", Iteration.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Iteration.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Iteration` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("DomainId") != null && !jsonObj.get("DomainId").isJsonNull()) && !jsonObj.get("DomainId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DomainId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DomainId").toString()));
      }
      if ((jsonObj.get("Id") != null && !jsonObj.get("Id").isJsonNull()) && !jsonObj.get("Id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Id").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("ProjectId") != null && !jsonObj.get("ProjectId").isJsonNull()) && !jsonObj.get("ProjectId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProjectId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProjectId").toString()));
      }
      if ((jsonObj.get("Status") != null && !jsonObj.get("Status").isJsonNull()) && !jsonObj.get("Status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Status").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Iteration.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Iteration' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Iteration> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Iteration.class));

       return (TypeAdapter<T>) new TypeAdapter<Iteration>() {
           @Override
           public void write(JsonWriter out, Iteration value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Iteration read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Iteration given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Iteration
   * @throws IOException if the JSON string is invalid with respect to Iteration
   */
  public static Iteration fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Iteration.class);
  }

  /**
   * Convert an instance of Iteration to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

