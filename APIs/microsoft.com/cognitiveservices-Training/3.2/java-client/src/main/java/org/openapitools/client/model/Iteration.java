/*
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
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
 * Iteration model to be sent over JSON.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:05.173515-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Iteration {
  /**
   * Gets the classification type of the project.
   */
  @JsonAdapter(ClassificationTypeEnum.Adapter.class)
  public enum ClassificationTypeEnum {
    MULTICLASS("Multiclass"),
    
    MULTILABEL("Multilabel");

    private String value;

    ClassificationTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ClassificationTypeEnum fromValue(String value) {
      for (ClassificationTypeEnum b : ClassificationTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<ClassificationTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ClassificationTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ClassificationTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ClassificationTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ClassificationTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CLASSIFICATION_TYPE = "classificationType";
  @SerializedName(SERIALIZED_NAME_CLASSIFICATION_TYPE)
  private ClassificationTypeEnum classificationType;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private OffsetDateTime created;

  public static final String SERIALIZED_NAME_DOMAIN_ID = "domainId";
  @SerializedName(SERIALIZED_NAME_DOMAIN_ID)
  private UUID domainId;

  public static final String SERIALIZED_NAME_EXPORTABLE = "exportable";
  @SerializedName(SERIALIZED_NAME_EXPORTABLE)
  private Boolean exportable;

  /**
   * Gets or Sets exportableTo
   */
  @JsonAdapter(ExportableToEnum.Adapter.class)
  public enum ExportableToEnum {
    CORE_ML("CoreML"),
    
    TENSOR_FLOW("TensorFlow"),
    
    DOCKER_FILE("DockerFile"),
    
    ONNX("ONNX"),
    
    VAIDK("VAIDK");

    private String value;

    ExportableToEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ExportableToEnum fromValue(String value) {
      for (ExportableToEnum b : ExportableToEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ExportableToEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ExportableToEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ExportableToEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ExportableToEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ExportableToEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_EXPORTABLE_TO = "exportableTo";
  @SerializedName(SERIALIZED_NAME_EXPORTABLE_TO)
  private List<ExportableToEnum> exportableTo = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_LAST_MODIFIED = "lastModified";
  @SerializedName(SERIALIZED_NAME_LAST_MODIFIED)
  private OffsetDateTime lastModified;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_ORIGINAL_PUBLISH_RESOURCE_ID = "originalPublishResourceId";
  @SerializedName(SERIALIZED_NAME_ORIGINAL_PUBLISH_RESOURCE_ID)
  private String originalPublishResourceId;

  public static final String SERIALIZED_NAME_PROJECT_ID = "projectId";
  @SerializedName(SERIALIZED_NAME_PROJECT_ID)
  private UUID projectId;

  public static final String SERIALIZED_NAME_PUBLISH_NAME = "publishName";
  @SerializedName(SERIALIZED_NAME_PUBLISH_NAME)
  private String publishName;

  public static final String SERIALIZED_NAME_RESERVED_BUDGET_IN_HOURS = "reservedBudgetInHours";
  @SerializedName(SERIALIZED_NAME_RESERVED_BUDGET_IN_HOURS)
  private Integer reservedBudgetInHours;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_TRAINED_AT = "trainedAt";
  @SerializedName(SERIALIZED_NAME_TRAINED_AT)
  private OffsetDateTime trainedAt;

  public static final String SERIALIZED_NAME_TRAINING_TIME_IN_MINUTES = "trainingTimeInMinutes";
  @SerializedName(SERIALIZED_NAME_TRAINING_TIME_IN_MINUTES)
  private Integer trainingTimeInMinutes;

  /**
   * Gets the training type of the iteration.
   */
  @JsonAdapter(TrainingTypeEnum.Adapter.class)
  public enum TrainingTypeEnum {
    REGULAR("Regular"),
    
    ADVANCED("Advanced");

    private String value;

    TrainingTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TrainingTypeEnum fromValue(String value) {
      for (TrainingTypeEnum b : TrainingTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TrainingTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TrainingTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TrainingTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TrainingTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TrainingTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TRAINING_TYPE = "trainingType";
  @SerializedName(SERIALIZED_NAME_TRAINING_TYPE)
  private TrainingTypeEnum trainingType;

  public Iteration() {
  }

  public Iteration(
     ClassificationTypeEnum classificationType, 
     OffsetDateTime created, 
     UUID domainId, 
     Boolean exportable, 
     List<ExportableToEnum> exportableTo, 
     UUID id, 
     OffsetDateTime lastModified, 
     String originalPublishResourceId, 
     UUID projectId, 
     String publishName, 
     Integer reservedBudgetInHours, 
     String status, 
     OffsetDateTime trainedAt, 
     Integer trainingTimeInMinutes, 
     TrainingTypeEnum trainingType
  ) {
    this();
    this.classificationType = classificationType;
    this.created = created;
    this.domainId = domainId;
    this.exportable = exportable;
    this.exportableTo = exportableTo;
    this.id = id;
    this.lastModified = lastModified;
    this.originalPublishResourceId = originalPublishResourceId;
    this.projectId = projectId;
    this.publishName = publishName;
    this.reservedBudgetInHours = reservedBudgetInHours;
    this.status = status;
    this.trainedAt = trainedAt;
    this.trainingTimeInMinutes = trainingTimeInMinutes;
    this.trainingType = trainingType;
  }

  /**
   * Gets the classification type of the project.
   * @return classificationType
   */
  @javax.annotation.Nullable
  public ClassificationTypeEnum getClassificationType() {
    return classificationType;
  }



  /**
   * Gets the time this iteration was completed.
   * @return created
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreated() {
    return created;
  }



  /**
   * Get or sets a guid of the domain the iteration has been trained on.
   * @return domainId
   */
  @javax.annotation.Nullable
  public UUID getDomainId() {
    return domainId;
  }



  /**
   * Whether the iteration can be exported to another format for download.
   * @return exportable
   */
  @javax.annotation.Nullable
  public Boolean getExportable() {
    return exportable;
  }



  /**
   * A set of platforms this iteration can export to.
   * @return exportableTo
   */
  @javax.annotation.Nullable
  public List<ExportableToEnum> getExportableTo() {
    return exportableTo;
  }



  /**
   * Gets the id of the iteration.
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }



  /**
   * Gets the time this iteration was last modified.
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
   * Gets or sets the name of the iteration.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  /**
   * Resource Provider Id this iteration was originally published to.
   * @return originalPublishResourceId
   */
  @javax.annotation.Nullable
  public String getOriginalPublishResourceId() {
    return originalPublishResourceId;
  }



  /**
   * Gets the project id of the iteration.
   * @return projectId
   */
  @javax.annotation.Nullable
  public UUID getProjectId() {
    return projectId;
  }



  /**
   * Name of the published model.
   * @return publishName
   */
  @javax.annotation.Nullable
  public String getPublishName() {
    return publishName;
  }



  /**
   * Gets the reserved advanced training budget for the iteration.
   * @return reservedBudgetInHours
   */
  @javax.annotation.Nullable
  public Integer getReservedBudgetInHours() {
    return reservedBudgetInHours;
  }



  /**
   * Gets the current iteration status.
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }



  /**
   * Gets the time this iteration was last modified.
   * @return trainedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getTrainedAt() {
    return trainedAt;
  }



  /**
   * Gets the training time for the iteration.
   * @return trainingTimeInMinutes
   */
  @javax.annotation.Nullable
  public Integer getTrainingTimeInMinutes() {
    return trainingTimeInMinutes;
  }



  /**
   * Gets the training type of the iteration.
   * @return trainingType
   */
  @javax.annotation.Nullable
  public TrainingTypeEnum getTrainingType() {
    return trainingType;
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
    return Objects.equals(this.classificationType, iteration.classificationType) &&
        Objects.equals(this.created, iteration.created) &&
        Objects.equals(this.domainId, iteration.domainId) &&
        Objects.equals(this.exportable, iteration.exportable) &&
        Objects.equals(this.exportableTo, iteration.exportableTo) &&
        Objects.equals(this.id, iteration.id) &&
        Objects.equals(this.lastModified, iteration.lastModified) &&
        Objects.equals(this.name, iteration.name) &&
        Objects.equals(this.originalPublishResourceId, iteration.originalPublishResourceId) &&
        Objects.equals(this.projectId, iteration.projectId) &&
        Objects.equals(this.publishName, iteration.publishName) &&
        Objects.equals(this.reservedBudgetInHours, iteration.reservedBudgetInHours) &&
        Objects.equals(this.status, iteration.status) &&
        Objects.equals(this.trainedAt, iteration.trainedAt) &&
        Objects.equals(this.trainingTimeInMinutes, iteration.trainingTimeInMinutes) &&
        Objects.equals(this.trainingType, iteration.trainingType);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(classificationType, created, domainId, exportable, exportableTo, id, lastModified, name, originalPublishResourceId, projectId, publishName, reservedBudgetInHours, status, trainedAt, trainingTimeInMinutes, trainingType);
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
    sb.append("    classificationType: ").append(toIndentedString(classificationType)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    domainId: ").append(toIndentedString(domainId)).append("\n");
    sb.append("    exportable: ").append(toIndentedString(exportable)).append("\n");
    sb.append("    exportableTo: ").append(toIndentedString(exportableTo)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    lastModified: ").append(toIndentedString(lastModified)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    originalPublishResourceId: ").append(toIndentedString(originalPublishResourceId)).append("\n");
    sb.append("    projectId: ").append(toIndentedString(projectId)).append("\n");
    sb.append("    publishName: ").append(toIndentedString(publishName)).append("\n");
    sb.append("    reservedBudgetInHours: ").append(toIndentedString(reservedBudgetInHours)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    trainedAt: ").append(toIndentedString(trainedAt)).append("\n");
    sb.append("    trainingTimeInMinutes: ").append(toIndentedString(trainingTimeInMinutes)).append("\n");
    sb.append("    trainingType: ").append(toIndentedString(trainingType)).append("\n");
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
    openapiFields.add("classificationType");
    openapiFields.add("created");
    openapiFields.add("domainId");
    openapiFields.add("exportable");
    openapiFields.add("exportableTo");
    openapiFields.add("id");
    openapiFields.add("lastModified");
    openapiFields.add("name");
    openapiFields.add("originalPublishResourceId");
    openapiFields.add("projectId");
    openapiFields.add("publishName");
    openapiFields.add("reservedBudgetInHours");
    openapiFields.add("status");
    openapiFields.add("trainedAt");
    openapiFields.add("trainingTimeInMinutes");
    openapiFields.add("trainingType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
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

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Iteration.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("classificationType") != null && !jsonObj.get("classificationType").isJsonNull()) && !jsonObj.get("classificationType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `classificationType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("classificationType").toString()));
      }
      // validate the optional field `classificationType`
      if (jsonObj.get("classificationType") != null && !jsonObj.get("classificationType").isJsonNull()) {
        ClassificationTypeEnum.validateJsonElement(jsonObj.get("classificationType"));
      }
      if ((jsonObj.get("domainId") != null && !jsonObj.get("domainId").isJsonNull()) && !jsonObj.get("domainId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `domainId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("domainId").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("exportableTo") != null && !jsonObj.get("exportableTo").isJsonNull() && !jsonObj.get("exportableTo").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `exportableTo` to be an array in the JSON string but got `%s`", jsonObj.get("exportableTo").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("originalPublishResourceId") != null && !jsonObj.get("originalPublishResourceId").isJsonNull()) && !jsonObj.get("originalPublishResourceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `originalPublishResourceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("originalPublishResourceId").toString()));
      }
      if ((jsonObj.get("projectId") != null && !jsonObj.get("projectId").isJsonNull()) && !jsonObj.get("projectId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `projectId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("projectId").toString()));
      }
      if ((jsonObj.get("publishName") != null && !jsonObj.get("publishName").isJsonNull()) && !jsonObj.get("publishName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publishName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publishName").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      if ((jsonObj.get("trainingType") != null && !jsonObj.get("trainingType").isJsonNull()) && !jsonObj.get("trainingType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `trainingType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("trainingType").toString()));
      }
      // validate the optional field `trainingType`
      if (jsonObj.get("trainingType") != null && !jsonObj.get("trainingType").isJsonNull()) {
        TrainingTypeEnum.validateJsonElement(jsonObj.get("trainingType"));
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

