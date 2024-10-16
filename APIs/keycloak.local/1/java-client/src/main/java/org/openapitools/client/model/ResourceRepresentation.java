/*
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
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
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.ScopeRepresentation;

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
 * ResourceRepresentation
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.227825-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ResourceRepresentation {
  public static final String SERIALIZED_NAME_ATTRIBUTES = "attributes";
  @SerializedName(SERIALIZED_NAME_ATTRIBUTES)
  private Map<String, Object> attributes = new HashMap<>();

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "displayName";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public static final String SERIALIZED_NAME_ICON_URI = "icon_uri";
  @SerializedName(SERIALIZED_NAME_ICON_URI)
  private String iconUri;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OWNER_MANAGED_ACCESS = "ownerManagedAccess";
  @SerializedName(SERIALIZED_NAME_OWNER_MANAGED_ACCESS)
  private Boolean ownerManagedAccess;

  public static final String SERIALIZED_NAME_SCOPES = "scopes";
  @SerializedName(SERIALIZED_NAME_SCOPES)
  private List<ScopeRepresentation> scopes = new ArrayList<>();

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public static final String SERIALIZED_NAME_URIS = "uris";
  @SerializedName(SERIALIZED_NAME_URIS)
  private List<String> uris = new ArrayList<>();

  public ResourceRepresentation() {
  }

  public ResourceRepresentation attributes(Map<String, Object> attributes) {
    this.attributes = attributes;
    return this;
  }

  public ResourceRepresentation putAttributesItem(String key, Object attributesItem) {
    if (this.attributes == null) {
      this.attributes = new HashMap<>();
    }
    this.attributes.put(key, attributesItem);
    return this;
  }

  /**
   * Get attributes
   * @return attributes
   */
  @javax.annotation.Nullable
  public Map<String, Object> getAttributes() {
    return attributes;
  }

  public void setAttributes(Map<String, Object> attributes) {
    this.attributes = attributes;
  }


  public ResourceRepresentation displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * Get displayName
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }


  public ResourceRepresentation iconUri(String iconUri) {
    this.iconUri = iconUri;
    return this;
  }

  /**
   * Get iconUri
   * @return iconUri
   */
  @javax.annotation.Nullable
  public String getIconUri() {
    return iconUri;
  }

  public void setIconUri(String iconUri) {
    this.iconUri = iconUri;
  }


  public ResourceRepresentation id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public ResourceRepresentation name(String name) {
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


  public ResourceRepresentation ownerManagedAccess(Boolean ownerManagedAccess) {
    this.ownerManagedAccess = ownerManagedAccess;
    return this;
  }

  /**
   * Get ownerManagedAccess
   * @return ownerManagedAccess
   */
  @javax.annotation.Nullable
  public Boolean getOwnerManagedAccess() {
    return ownerManagedAccess;
  }

  public void setOwnerManagedAccess(Boolean ownerManagedAccess) {
    this.ownerManagedAccess = ownerManagedAccess;
  }


  public ResourceRepresentation scopes(List<ScopeRepresentation> scopes) {
    this.scopes = scopes;
    return this;
  }

  public ResourceRepresentation addScopesItem(ScopeRepresentation scopesItem) {
    if (this.scopes == null) {
      this.scopes = new ArrayList<>();
    }
    this.scopes.add(scopesItem);
    return this;
  }

  /**
   * Get scopes
   * @return scopes
   */
  @javax.annotation.Nullable
  public List<ScopeRepresentation> getScopes() {
    return scopes;
  }

  public void setScopes(List<ScopeRepresentation> scopes) {
    this.scopes = scopes;
  }


  public ResourceRepresentation type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }


  public ResourceRepresentation uris(List<String> uris) {
    this.uris = uris;
    return this;
  }

  public ResourceRepresentation addUrisItem(String urisItem) {
    if (this.uris == null) {
      this.uris = new ArrayList<>();
    }
    this.uris.add(urisItem);
    return this;
  }

  /**
   * Get uris
   * @return uris
   */
  @javax.annotation.Nullable
  public List<String> getUris() {
    return uris;
  }

  public void setUris(List<String> uris) {
    this.uris = uris;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ResourceRepresentation resourceRepresentation = (ResourceRepresentation) o;
    return Objects.equals(this.attributes, resourceRepresentation.attributes) &&
        Objects.equals(this.displayName, resourceRepresentation.displayName) &&
        Objects.equals(this.iconUri, resourceRepresentation.iconUri) &&
        Objects.equals(this.id, resourceRepresentation.id) &&
        Objects.equals(this.name, resourceRepresentation.name) &&
        Objects.equals(this.ownerManagedAccess, resourceRepresentation.ownerManagedAccess) &&
        Objects.equals(this.scopes, resourceRepresentation.scopes) &&
        Objects.equals(this.type, resourceRepresentation.type) &&
        Objects.equals(this.uris, resourceRepresentation.uris);
  }

  @Override
  public int hashCode() {
    return Objects.hash(attributes, displayName, iconUri, id, name, ownerManagedAccess, scopes, type, uris);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ResourceRepresentation {\n");
    sb.append("    attributes: ").append(toIndentedString(attributes)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    iconUri: ").append(toIndentedString(iconUri)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    ownerManagedAccess: ").append(toIndentedString(ownerManagedAccess)).append("\n");
    sb.append("    scopes: ").append(toIndentedString(scopes)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    uris: ").append(toIndentedString(uris)).append("\n");
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
    openapiFields.add("attributes");
    openapiFields.add("displayName");
    openapiFields.add("icon_uri");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("ownerManagedAccess");
    openapiFields.add("scopes");
    openapiFields.add("type");
    openapiFields.add("uris");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ResourceRepresentation
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ResourceRepresentation.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ResourceRepresentation is not found in the empty JSON string", ResourceRepresentation.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ResourceRepresentation.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ResourceRepresentation` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("displayName") != null && !jsonObj.get("displayName").isJsonNull()) && !jsonObj.get("displayName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `displayName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("displayName").toString()));
      }
      if ((jsonObj.get("icon_uri") != null && !jsonObj.get("icon_uri").isJsonNull()) && !jsonObj.get("icon_uri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `icon_uri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("icon_uri").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (jsonObj.get("scopes") != null && !jsonObj.get("scopes").isJsonNull()) {
        JsonArray jsonArrayscopes = jsonObj.getAsJsonArray("scopes");
        if (jsonArrayscopes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("scopes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `scopes` to be an array in the JSON string but got `%s`", jsonObj.get("scopes").toString()));
          }

          // validate the optional field `scopes` (array)
          for (int i = 0; i < jsonArrayscopes.size(); i++) {
            ScopeRepresentation.validateJsonElement(jsonArrayscopes.get(i));
          };
        }
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("uris") != null && !jsonObj.get("uris").isJsonNull() && !jsonObj.get("uris").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `uris` to be an array in the JSON string but got `%s`", jsonObj.get("uris").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ResourceRepresentation.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ResourceRepresentation' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ResourceRepresentation> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ResourceRepresentation.class));

       return (TypeAdapter<T>) new TypeAdapter<ResourceRepresentation>() {
           @Override
           public void write(JsonWriter out, ResourceRepresentation value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ResourceRepresentation read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ResourceRepresentation given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ResourceRepresentation
   * @throws IOException if the JSON string is invalid with respect to ResourceRepresentation
   */
  public static ResourceRepresentation fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ResourceRepresentation.class);
  }

  /**
   * Convert an instance of ResourceRepresentation to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

