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
 * Export configuration
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ExportConfigurationsList200ResponseValuesInnerExportConfiguration {
  public static final String SERIALIZED_NAME_BACKFILL = "backfill";
  @SerializedName(SERIALIZED_NAME_BACKFILL)
  private Boolean backfill;

  /**
   * Gets or Sets exportEntities
   */
  @JsonAdapter(ExportEntitiesEnum.Adapter.class)
  public enum ExportEntitiesEnum {
    CRASHES("crashes"),
    
    ERRORS("errors"),
    
    ATTACHMENTS("attachments"),
    
    NO_LOGS("no_logs");

    private String value;

    ExportEntitiesEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ExportEntitiesEnum fromValue(String value) {
      for (ExportEntitiesEnum b : ExportEntitiesEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ExportEntitiesEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ExportEntitiesEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ExportEntitiesEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ExportEntitiesEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ExportEntitiesEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_EXPORT_ENTITIES = "export_entities";
  @SerializedName(SERIALIZED_NAME_EXPORT_ENTITIES)
  private List<ExportEntitiesEnum> exportEntities = new ArrayList<>();

  public static final String SERIALIZED_NAME_RESOURCE_GROUP = "resource_group";
  @SerializedName(SERIALIZED_NAME_RESOURCE_GROUP)
  private String resourceGroup;

  public static final String SERIALIZED_NAME_RESOURCE_NAME = "resource_name";
  @SerializedName(SERIALIZED_NAME_RESOURCE_NAME)
  private String resourceName;

  /**
   * Type of export configuration
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    BLOB_STORAGE_CONNECTION_STRING("blob_storage_connection_string"),
    
    APPLICATION_INSIGHTS_INSTRUMENTATION_KEY("application_insights_instrumentation_key"),
    
    BLOB_STORAGE_LINKED_SUBSCRIPTION("blob_storage_linked_subscription"),
    
    APPLICATION_INSIGHTS_LINKED_SUBSCRIPTION("application_insights_linked_subscription");

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
  protected TypeEnum type;

  public ExportConfigurationsList200ResponseValuesInnerExportConfiguration() {
  }

  public ExportConfigurationsList200ResponseValuesInnerExportConfiguration backfill(Boolean backfill) {
    this.backfill = backfill;
    return this;
  }

  /**
   * Field to determine if backfilling should occur. The default value is true. If set to false export starts from date and time of config creation.
   * @return backfill
   */
  @javax.annotation.Nullable
  public Boolean getBackfill() {
    return backfill;
  }

  public void setBackfill(Boolean backfill) {
    this.backfill = backfill;
  }


  public ExportConfigurationsList200ResponseValuesInnerExportConfiguration exportEntities(List<ExportEntitiesEnum> exportEntities) {
    this.exportEntities = exportEntities;
    return this;
  }

  public ExportConfigurationsList200ResponseValuesInnerExportConfiguration addExportEntitiesItem(ExportEntitiesEnum exportEntitiesItem) {
    if (this.exportEntities == null) {
      this.exportEntities = new ArrayList<>();
    }
    this.exportEntities.add(exportEntitiesItem);
    return this;
  }

  /**
   * Get exportEntities
   * @return exportEntities
   */
  @javax.annotation.Nullable
  public List<ExportEntitiesEnum> getExportEntities() {
    return exportEntities;
  }

  public void setExportEntities(List<ExportEntitiesEnum> exportEntities) {
    this.exportEntities = exportEntities;
  }


  public ExportConfigurationsList200ResponseValuesInnerExportConfiguration resourceGroup(String resourceGroup) {
    this.resourceGroup = resourceGroup;
    return this;
  }

  /**
   * The resource group name on azure
   * @return resourceGroup
   */
  @javax.annotation.Nullable
  public String getResourceGroup() {
    return resourceGroup;
  }

  public void setResourceGroup(String resourceGroup) {
    this.resourceGroup = resourceGroup;
  }


  public ExportConfigurationsList200ResponseValuesInnerExportConfiguration resourceName(String resourceName) {
    this.resourceName = resourceName;
    return this;
  }

  /**
   * The resource name on azure
   * @return resourceName
   */
  @javax.annotation.Nullable
  public String getResourceName() {
    return resourceName;
  }

  public void setResourceName(String resourceName) {
    this.resourceName = resourceName;
  }


  public ExportConfigurationsList200ResponseValuesInnerExportConfiguration type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Type of export configuration
   * @return type
   */
  @javax.annotation.Nonnull
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ExportConfigurationsList200ResponseValuesInnerExportConfiguration exportConfigurationsList200ResponseValuesInnerExportConfiguration = (ExportConfigurationsList200ResponseValuesInnerExportConfiguration) o;
    return Objects.equals(this.backfill, exportConfigurationsList200ResponseValuesInnerExportConfiguration.backfill) &&
        Objects.equals(this.exportEntities, exportConfigurationsList200ResponseValuesInnerExportConfiguration.exportEntities) &&
        Objects.equals(this.resourceGroup, exportConfigurationsList200ResponseValuesInnerExportConfiguration.resourceGroup) &&
        Objects.equals(this.resourceName, exportConfigurationsList200ResponseValuesInnerExportConfiguration.resourceName) &&
        Objects.equals(this.type, exportConfigurationsList200ResponseValuesInnerExportConfiguration.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(backfill, exportEntities, resourceGroup, resourceName, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ExportConfigurationsList200ResponseValuesInnerExportConfiguration {\n");
    sb.append("    backfill: ").append(toIndentedString(backfill)).append("\n");
    sb.append("    exportEntities: ").append(toIndentedString(exportEntities)).append("\n");
    sb.append("    resourceGroup: ").append(toIndentedString(resourceGroup)).append("\n");
    sb.append("    resourceName: ").append(toIndentedString(resourceName)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("backfill");
    openapiFields.add("export_entities");
    openapiFields.add("resource_group");
    openapiFields.add("resource_name");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ExportConfigurationsList200ResponseValuesInnerExportConfiguration
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ExportConfigurationsList200ResponseValuesInnerExportConfiguration.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ExportConfigurationsList200ResponseValuesInnerExportConfiguration is not found in the empty JSON string", ExportConfigurationsList200ResponseValuesInnerExportConfiguration.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ExportConfigurationsList200ResponseValuesInnerExportConfiguration.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ExportConfigurationsList200ResponseValuesInnerExportConfiguration` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ExportConfigurationsList200ResponseValuesInnerExportConfiguration.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ExportConfigurationsList200ResponseValuesInnerExportConfiguration.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ExportConfigurationsList200ResponseValuesInnerExportConfiguration' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ExportConfigurationsList200ResponseValuesInnerExportConfiguration> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ExportConfigurationsList200ResponseValuesInnerExportConfiguration.class));

       return (TypeAdapter<T>) new TypeAdapter<ExportConfigurationsList200ResponseValuesInnerExportConfiguration>() {
           @Override
           public void write(JsonWriter out, ExportConfigurationsList200ResponseValuesInnerExportConfiguration value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ExportConfigurationsList200ResponseValuesInnerExportConfiguration read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ExportConfigurationsList200ResponseValuesInnerExportConfiguration given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ExportConfigurationsList200ResponseValuesInnerExportConfiguration
   * @throws IOException if the JSON string is invalid with respect to ExportConfigurationsList200ResponseValuesInnerExportConfiguration
   */
  public static ExportConfigurationsList200ResponseValuesInnerExportConfiguration fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ExportConfigurationsList200ResponseValuesInnerExportConfiguration.class);
  }

  /**
   * Convert an instance of ExportConfigurationsList200ResponseValuesInnerExportConfiguration to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

