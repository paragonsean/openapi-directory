/*
 * ManagedNetworkManagementClient
 * The Microsoft Azure Managed Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to programmatically view, control, change, and monitor your entire Azure network centrally and with ease.
 *
 * The version of the OpenAPI document: 2019-06-01-preview
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
import org.openapitools.client.model.ResourceId;

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
 * Properties of a Mesh Peering Policy
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:25:05.083066-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class MeshPeeringPolicyProperties {
  public static final String SERIALIZED_NAME_MESH = "mesh";
  @SerializedName(SERIALIZED_NAME_MESH)
  private List<ResourceId> mesh = new ArrayList<>();

  public static final String SERIALIZED_NAME_HUB = "hub";
  @SerializedName(SERIALIZED_NAME_HUB)
  private ResourceId hub;

  public static final String SERIALIZED_NAME_SPOKES = "spokes";
  @SerializedName(SERIALIZED_NAME_SPOKES)
  private List<ResourceId> spokes = new ArrayList<>();

  /**
   * Gets or sets the connectivity type of a network structure policy
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    HUB_AND_SPOKE_TOPOLOGY("HubAndSpokeTopology"),
    
    MESH_TOPOLOGY("MeshTopology");

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

  public static final String SERIALIZED_NAME_ETAG = "etag";
  @SerializedName(SERIALIZED_NAME_ETAG)
  private String etag;

  /**
   * Provisioning state of the ManagedNetwork resource.
   */
  @JsonAdapter(ProvisioningStateEnum.Adapter.class)
  public enum ProvisioningStateEnum {
    UPDATING("Updating"),
    
    DELETING("Deleting"),
    
    FAILED("Failed"),
    
    SUCCEEDED("Succeeded");

    private String value;

    ProvisioningStateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ProvisioningStateEnum fromValue(String value) {
      for (ProvisioningStateEnum b : ProvisioningStateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ProvisioningStateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ProvisioningStateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ProvisioningStateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ProvisioningStateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ProvisioningStateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PROVISIONING_STATE = "provisioningState";
  @SerializedName(SERIALIZED_NAME_PROVISIONING_STATE)
  private ProvisioningStateEnum provisioningState;

  public MeshPeeringPolicyProperties() {
  }

  public MeshPeeringPolicyProperties(
     String etag, 
     ProvisioningStateEnum provisioningState
  ) {
    this();
    this.etag = etag;
    this.provisioningState = provisioningState;
  }

  public MeshPeeringPolicyProperties mesh(List<ResourceId> mesh) {
    this.mesh = mesh;
    return this;
  }

  public MeshPeeringPolicyProperties addMeshItem(ResourceId meshItem) {
    if (this.mesh == null) {
      this.mesh = new ArrayList<>();
    }
    this.mesh.add(meshItem);
    return this;
  }

  /**
   * Gets or sets the mesh group IDs
   * @return mesh
   */
  @javax.annotation.Nullable
  public List<ResourceId> getMesh() {
    return mesh;
  }

  public void setMesh(List<ResourceId> mesh) {
    this.mesh = mesh;
  }


  public MeshPeeringPolicyProperties hub(ResourceId hub) {
    this.hub = hub;
    return this;
  }

  /**
   * Get hub
   * @return hub
   */
  @javax.annotation.Nullable
  public ResourceId getHub() {
    return hub;
  }

  public void setHub(ResourceId hub) {
    this.hub = hub;
  }


  public MeshPeeringPolicyProperties spokes(List<ResourceId> spokes) {
    this.spokes = spokes;
    return this;
  }

  public MeshPeeringPolicyProperties addSpokesItem(ResourceId spokesItem) {
    if (this.spokes == null) {
      this.spokes = new ArrayList<>();
    }
    this.spokes.add(spokesItem);
    return this;
  }

  /**
   * Gets or sets the spokes group IDs
   * @return spokes
   */
  @javax.annotation.Nullable
  public List<ResourceId> getSpokes() {
    return spokes;
  }

  public void setSpokes(List<ResourceId> spokes) {
    this.spokes = spokes;
  }


  public MeshPeeringPolicyProperties type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Gets or sets the connectivity type of a network structure policy
   * @return type
   */
  @javax.annotation.Nonnull
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }


  /**
   * A unique read-only string that changes whenever the resource is updated.
   * @return etag
   */
  @javax.annotation.Nullable
  public String getEtag() {
    return etag;
  }



  /**
   * Provisioning state of the ManagedNetwork resource.
   * @return provisioningState
   */
  @javax.annotation.Nullable
  public ProvisioningStateEnum getProvisioningState() {
    return provisioningState;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MeshPeeringPolicyProperties meshPeeringPolicyProperties = (MeshPeeringPolicyProperties) o;
    return Objects.equals(this.mesh, meshPeeringPolicyProperties.mesh) &&
        Objects.equals(this.hub, meshPeeringPolicyProperties.hub) &&
        Objects.equals(this.spokes, meshPeeringPolicyProperties.spokes) &&
        Objects.equals(this.type, meshPeeringPolicyProperties.type) &&
        Objects.equals(this.etag, meshPeeringPolicyProperties.etag) &&
        Objects.equals(this.provisioningState, meshPeeringPolicyProperties.provisioningState);
  }

  @Override
  public int hashCode() {
    return Objects.hash(mesh, hub, spokes, type, etag, provisioningState);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MeshPeeringPolicyProperties {\n");
    sb.append("    mesh: ").append(toIndentedString(mesh)).append("\n");
    sb.append("    hub: ").append(toIndentedString(hub)).append("\n");
    sb.append("    spokes: ").append(toIndentedString(spokes)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    etag: ").append(toIndentedString(etag)).append("\n");
    sb.append("    provisioningState: ").append(toIndentedString(provisioningState)).append("\n");
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
    openapiFields.add("hub");
    openapiFields.add("mesh");
    openapiFields.add("spokes");
    openapiFields.add("type");
    openapiFields.add("etag");
    openapiFields.add("provisioningState");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to MeshPeeringPolicyProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!MeshPeeringPolicyProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in MeshPeeringPolicyProperties is not found in the empty JSON string", MeshPeeringPolicyProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!MeshPeeringPolicyProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `MeshPeeringPolicyProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : MeshPeeringPolicyProperties.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("mesh") != null && !jsonObj.get("mesh").isJsonNull()) {
        JsonArray jsonArraymesh = jsonObj.getAsJsonArray("mesh");
        if (jsonArraymesh != null) {
          // ensure the json data is an array
          if (!jsonObj.get("mesh").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `mesh` to be an array in the JSON string but got `%s`", jsonObj.get("mesh").toString()));
          }

          // validate the optional field `mesh` (array)
          for (int i = 0; i < jsonArraymesh.size(); i++) {
            ResourceId.validateJsonElement(jsonArraymesh.get(i));
          };
        }
      }
      // validate the optional field `hub`
      if (jsonObj.get("hub") != null && !jsonObj.get("hub").isJsonNull()) {
        ResourceId.validateJsonElement(jsonObj.get("hub"));
      }
      if (jsonObj.get("spokes") != null && !jsonObj.get("spokes").isJsonNull()) {
        JsonArray jsonArrayspokes = jsonObj.getAsJsonArray("spokes");
        if (jsonArrayspokes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("spokes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `spokes` to be an array in the JSON string but got `%s`", jsonObj.get("spokes").toString()));
          }

          // validate the optional field `spokes` (array)
          for (int i = 0; i < jsonArrayspokes.size(); i++) {
            ResourceId.validateJsonElement(jsonArrayspokes.get(i));
          };
        }
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the required field `type`
      TypeEnum.validateJsonElement(jsonObj.get("type"));
      if ((jsonObj.get("etag") != null && !jsonObj.get("etag").isJsonNull()) && !jsonObj.get("etag").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `etag` to be a primitive type in the JSON string but got `%s`", jsonObj.get("etag").toString()));
      }
      if ((jsonObj.get("provisioningState") != null && !jsonObj.get("provisioningState").isJsonNull()) && !jsonObj.get("provisioningState").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `provisioningState` to be a primitive type in the JSON string but got `%s`", jsonObj.get("provisioningState").toString()));
      }
      // validate the optional field `provisioningState`
      if (jsonObj.get("provisioningState") != null && !jsonObj.get("provisioningState").isJsonNull()) {
        ProvisioningStateEnum.validateJsonElement(jsonObj.get("provisioningState"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!MeshPeeringPolicyProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'MeshPeeringPolicyProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<MeshPeeringPolicyProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(MeshPeeringPolicyProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<MeshPeeringPolicyProperties>() {
           @Override
           public void write(JsonWriter out, MeshPeeringPolicyProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public MeshPeeringPolicyProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of MeshPeeringPolicyProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of MeshPeeringPolicyProperties
   * @throws IOException if the JSON string is invalid with respect to MeshPeeringPolicyProperties
   */
  public static MeshPeeringPolicyProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, MeshPeeringPolicyProperties.class);
  }

  /**
   * Convert an instance of MeshPeeringPolicyProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

