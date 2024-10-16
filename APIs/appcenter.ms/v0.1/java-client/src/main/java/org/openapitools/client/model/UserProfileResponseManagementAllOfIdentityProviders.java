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
 * UserProfileResponseManagementAllOfIdentityProviders
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UserProfileResponseManagementAllOfIdentityProviders {
  public static final String SERIALIZED_NAME_ORIGIN = "origin";
  @SerializedName(SERIALIZED_NAME_ORIGIN)
  private String origin;

  /**
   * The name of the identity provider type
   */
  @JsonAdapter(ProviderNameEnum.Adapter.class)
  public enum ProviderNameEnum {
    GITHUB("github"),
    
    AAD("aad"),
    
    FACEBOOK("facebook"),
    
    GOOGLE("google");

    private String value;

    ProviderNameEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ProviderNameEnum fromValue(String value) {
      for (ProviderNameEnum b : ProviderNameEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ProviderNameEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ProviderNameEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ProviderNameEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ProviderNameEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ProviderNameEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PROVIDER_NAME = "provider_name";
  @SerializedName(SERIALIZED_NAME_PROVIDER_NAME)
  private ProviderNameEnum providerName;

  public UserProfileResponseManagementAllOfIdentityProviders() {
  }

  public UserProfileResponseManagementAllOfIdentityProviders origin(String origin) {
    this.origin = origin;
    return this;
  }

  /**
   * Whether the identity provider originated in HockeyApp or App Center
   * @return origin
   */
  @javax.annotation.Nullable
  public String getOrigin() {
    return origin;
  }

  public void setOrigin(String origin) {
    this.origin = origin;
  }


  public UserProfileResponseManagementAllOfIdentityProviders providerName(ProviderNameEnum providerName) {
    this.providerName = providerName;
    return this;
  }

  /**
   * The name of the identity provider type
   * @return providerName
   */
  @javax.annotation.Nullable
  public ProviderNameEnum getProviderName() {
    return providerName;
  }

  public void setProviderName(ProviderNameEnum providerName) {
    this.providerName = providerName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UserProfileResponseManagementAllOfIdentityProviders userProfileResponseManagementAllOfIdentityProviders = (UserProfileResponseManagementAllOfIdentityProviders) o;
    return Objects.equals(this.origin, userProfileResponseManagementAllOfIdentityProviders.origin) &&
        Objects.equals(this.providerName, userProfileResponseManagementAllOfIdentityProviders.providerName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(origin, providerName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UserProfileResponseManagementAllOfIdentityProviders {\n");
    sb.append("    origin: ").append(toIndentedString(origin)).append("\n");
    sb.append("    providerName: ").append(toIndentedString(providerName)).append("\n");
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
    openapiFields.add("origin");
    openapiFields.add("provider_name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UserProfileResponseManagementAllOfIdentityProviders
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UserProfileResponseManagementAllOfIdentityProviders.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UserProfileResponseManagementAllOfIdentityProviders is not found in the empty JSON string", UserProfileResponseManagementAllOfIdentityProviders.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UserProfileResponseManagementAllOfIdentityProviders.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UserProfileResponseManagementAllOfIdentityProviders` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("origin") != null && !jsonObj.get("origin").isJsonNull()) && !jsonObj.get("origin").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `origin` to be a primitive type in the JSON string but got `%s`", jsonObj.get("origin").toString()));
      }
      if ((jsonObj.get("provider_name") != null && !jsonObj.get("provider_name").isJsonNull()) && !jsonObj.get("provider_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `provider_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("provider_name").toString()));
      }
      // validate the optional field `provider_name`
      if (jsonObj.get("provider_name") != null && !jsonObj.get("provider_name").isJsonNull()) {
        ProviderNameEnum.validateJsonElement(jsonObj.get("provider_name"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UserProfileResponseManagementAllOfIdentityProviders.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UserProfileResponseManagementAllOfIdentityProviders' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UserProfileResponseManagementAllOfIdentityProviders> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UserProfileResponseManagementAllOfIdentityProviders.class));

       return (TypeAdapter<T>) new TypeAdapter<UserProfileResponseManagementAllOfIdentityProviders>() {
           @Override
           public void write(JsonWriter out, UserProfileResponseManagementAllOfIdentityProviders value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UserProfileResponseManagementAllOfIdentityProviders read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UserProfileResponseManagementAllOfIdentityProviders given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UserProfileResponseManagementAllOfIdentityProviders
   * @throws IOException if the JSON string is invalid with respect to UserProfileResponseManagementAllOfIdentityProviders
   */
  public static UserProfileResponseManagementAllOfIdentityProviders fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UserProfileResponseManagementAllOfIdentityProviders.class);
  }

  /**
   * Convert an instance of UserProfileResponseManagementAllOfIdentityProviders to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

