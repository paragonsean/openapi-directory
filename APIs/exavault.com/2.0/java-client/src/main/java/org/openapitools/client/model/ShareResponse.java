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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Share;
import org.openapitools.client.model.ShareCollectionResponseIncludedInner;

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
 * Response object for shares.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:39.505408-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ShareResponse {
  public static final String SERIALIZED_NAME_DATA = "data";
  @SerializedName(SERIALIZED_NAME_DATA)
  private Share data;

  public static final String SERIALIZED_NAME_INCLUDED = "included";
  @SerializedName(SERIALIZED_NAME_INCLUDED)
  private List<ShareCollectionResponseIncludedInner> included = new ArrayList<>();

  public static final String SERIALIZED_NAME_RESPONSE_STATUS = "responseStatus";
  @SerializedName(SERIALIZED_NAME_RESPONSE_STATUS)
  private Integer responseStatus;

  public ShareResponse() {
  }

  public ShareResponse data(Share data) {
    this.data = data;
    return this;
  }

  /**
   * Get data
   * @return data
   */
  @javax.annotation.Nullable
  public Share getData() {
    return data;
  }

  public void setData(Share data) {
    this.data = data;
  }


  public ShareResponse included(List<ShareCollectionResponseIncludedInner> included) {
    this.included = included;
    return this;
  }

  public ShareResponse addIncludedItem(ShareCollectionResponseIncludedInner includedItem) {
    if (this.included == null) {
      this.included = new ArrayList<>();
    }
    this.included.add(includedItem);
    return this;
  }

  /**
   * Get included
   * @return included
   */
  @javax.annotation.Nullable
  public List<ShareCollectionResponseIncludedInner> getIncluded() {
    return included;
  }

  public void setIncluded(List<ShareCollectionResponseIncludedInner> included) {
    this.included = included;
  }


  public ShareResponse responseStatus(Integer responseStatus) {
    this.responseStatus = responseStatus;
    return this;
  }

  /**
   * Http status code of the response.
   * @return responseStatus
   */
  @javax.annotation.Nullable
  public Integer getResponseStatus() {
    return responseStatus;
  }

  public void setResponseStatus(Integer responseStatus) {
    this.responseStatus = responseStatus;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ShareResponse shareResponse = (ShareResponse) o;
    return Objects.equals(this.data, shareResponse.data) &&
        Objects.equals(this.included, shareResponse.included) &&
        Objects.equals(this.responseStatus, shareResponse.responseStatus);
  }

  @Override
  public int hashCode() {
    return Objects.hash(data, included, responseStatus);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ShareResponse {\n");
    sb.append("    data: ").append(toIndentedString(data)).append("\n");
    sb.append("    included: ").append(toIndentedString(included)).append("\n");
    sb.append("    responseStatus: ").append(toIndentedString(responseStatus)).append("\n");
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
    openapiFields.add("data");
    openapiFields.add("included");
    openapiFields.add("responseStatus");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ShareResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ShareResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ShareResponse is not found in the empty JSON string", ShareResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ShareResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ShareResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `data`
      if (jsonObj.get("data") != null && !jsonObj.get("data").isJsonNull()) {
        Share.validateJsonElement(jsonObj.get("data"));
      }
      if (jsonObj.get("included") != null && !jsonObj.get("included").isJsonNull()) {
        JsonArray jsonArrayincluded = jsonObj.getAsJsonArray("included");
        if (jsonArrayincluded != null) {
          // ensure the json data is an array
          if (!jsonObj.get("included").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `included` to be an array in the JSON string but got `%s`", jsonObj.get("included").toString()));
          }

          // validate the optional field `included` (array)
          for (int i = 0; i < jsonArrayincluded.size(); i++) {
            ShareCollectionResponseIncludedInner.validateJsonElement(jsonArrayincluded.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ShareResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ShareResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ShareResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ShareResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<ShareResponse>() {
           @Override
           public void write(JsonWriter out, ShareResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ShareResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ShareResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ShareResponse
   * @throws IOException if the JSON string is invalid with respect to ShareResponse
   */
  public static ShareResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ShareResponse.class);
  }

  /**
   * Convert an instance of ShareResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

