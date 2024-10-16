/*
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
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
import org.openapitools.client.model.UserRelationshipsHomeResource;
import org.openapitools.client.model.UserRelationshipsOwnerAccount;

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
 * Home resource and owner account relationship data for the user. 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:39.505408-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UserRelationships {
  public static final String SERIALIZED_NAME_HOME_RESOURCE = "homeResource";
  @SerializedName(SERIALIZED_NAME_HOME_RESOURCE)
  private UserRelationshipsHomeResource homeResource;

  public static final String SERIALIZED_NAME_OWNER_ACCOUNT = "ownerAccount";
  @SerializedName(SERIALIZED_NAME_OWNER_ACCOUNT)
  private UserRelationshipsOwnerAccount ownerAccount;

  public UserRelationships() {
  }

  public UserRelationships homeResource(UserRelationshipsHomeResource homeResource) {
    this.homeResource = homeResource;
    return this;
  }

  /**
   * Get homeResource
   * @return homeResource
   */
  @javax.annotation.Nullable
  public UserRelationshipsHomeResource getHomeResource() {
    return homeResource;
  }

  public void setHomeResource(UserRelationshipsHomeResource homeResource) {
    this.homeResource = homeResource;
  }


  public UserRelationships ownerAccount(UserRelationshipsOwnerAccount ownerAccount) {
    this.ownerAccount = ownerAccount;
    return this;
  }

  /**
   * Get ownerAccount
   * @return ownerAccount
   */
  @javax.annotation.Nonnull
  public UserRelationshipsOwnerAccount getOwnerAccount() {
    return ownerAccount;
  }

  public void setOwnerAccount(UserRelationshipsOwnerAccount ownerAccount) {
    this.ownerAccount = ownerAccount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UserRelationships userRelationships = (UserRelationships) o;
    return Objects.equals(this.homeResource, userRelationships.homeResource) &&
        Objects.equals(this.ownerAccount, userRelationships.ownerAccount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(homeResource, ownerAccount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UserRelationships {\n");
    sb.append("    homeResource: ").append(toIndentedString(homeResource)).append("\n");
    sb.append("    ownerAccount: ").append(toIndentedString(ownerAccount)).append("\n");
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
    openapiFields.add("homeResource");
    openapiFields.add("ownerAccount");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("ownerAccount");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UserRelationships
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UserRelationships.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UserRelationships is not found in the empty JSON string", UserRelationships.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UserRelationships.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UserRelationships` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UserRelationships.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `homeResource`
      if (jsonObj.get("homeResource") != null && !jsonObj.get("homeResource").isJsonNull()) {
        UserRelationshipsHomeResource.validateJsonElement(jsonObj.get("homeResource"));
      }
      // validate the required field `ownerAccount`
      UserRelationshipsOwnerAccount.validateJsonElement(jsonObj.get("ownerAccount"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UserRelationships.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UserRelationships' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UserRelationships> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UserRelationships.class));

       return (TypeAdapter<T>) new TypeAdapter<UserRelationships>() {
           @Override
           public void write(JsonWriter out, UserRelationships value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UserRelationships read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UserRelationships given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UserRelationships
   * @throws IOException if the JSON string is invalid with respect to UserRelationships
   */
  public static UserRelationships fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UserRelationships.class);
  }

  /**
   * Convert an instance of UserRelationships to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

