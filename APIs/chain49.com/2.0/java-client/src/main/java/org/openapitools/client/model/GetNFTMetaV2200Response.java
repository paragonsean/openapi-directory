/*
 * Chain49 API
 * Kickstart your next crypto project - extended trezor/blockbook API with 10+ blockchains available instantly and 50+ possible on request running on the finest hardware in Germany's best datacenters at Hetzner  Websocket only via api.chain49.com endpoint possible (RapidAPI does not support it yet)
 *
 * The version of the OpenAPI document: 2.0
 * Contact: contact@chain49.com
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
import org.openapitools.client.model.GetNFTMetaV2200ResponseContractInfo;

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
 * GetNFTMetaV2200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:48.868561-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetNFTMetaV2200Response {
  public static final String SERIALIZED_NAME_CONTRACT_INFO = "contractInfo";
  @SerializedName(SERIALIZED_NAME_CONTRACT_INFO)
  private GetNFTMetaV2200ResponseContractInfo contractInfo;

  public static final String SERIALIZED_NAME_TOKEN_ID = "tokenId";
  @SerializedName(SERIALIZED_NAME_TOKEN_ID)
  private String tokenId;

  public static final String SERIALIZED_NAME_URI = "uri";
  @SerializedName(SERIALIZED_NAME_URI)
  private String uri;

  public GetNFTMetaV2200Response() {
  }

  public GetNFTMetaV2200Response contractInfo(GetNFTMetaV2200ResponseContractInfo contractInfo) {
    this.contractInfo = contractInfo;
    return this;
  }

  /**
   * Get contractInfo
   * @return contractInfo
   */
  @javax.annotation.Nullable
  public GetNFTMetaV2200ResponseContractInfo getContractInfo() {
    return contractInfo;
  }

  public void setContractInfo(GetNFTMetaV2200ResponseContractInfo contractInfo) {
    this.contractInfo = contractInfo;
  }


  public GetNFTMetaV2200Response tokenId(String tokenId) {
    this.tokenId = tokenId;
    return this;
  }

  /**
   * Get tokenId
   * @return tokenId
   */
  @javax.annotation.Nullable
  public String getTokenId() {
    return tokenId;
  }

  public void setTokenId(String tokenId) {
    this.tokenId = tokenId;
  }


  public GetNFTMetaV2200Response uri(String uri) {
    this.uri = uri;
    return this;
  }

  /**
   * Get uri
   * @return uri
   */
  @javax.annotation.Nullable
  public String getUri() {
    return uri;
  }

  public void setUri(String uri) {
    this.uri = uri;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetNFTMetaV2200Response getNFTMetaV2200Response = (GetNFTMetaV2200Response) o;
    return Objects.equals(this.contractInfo, getNFTMetaV2200Response.contractInfo) &&
        Objects.equals(this.tokenId, getNFTMetaV2200Response.tokenId) &&
        Objects.equals(this.uri, getNFTMetaV2200Response.uri);
  }

  @Override
  public int hashCode() {
    return Objects.hash(contractInfo, tokenId, uri);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetNFTMetaV2200Response {\n");
    sb.append("    contractInfo: ").append(toIndentedString(contractInfo)).append("\n");
    sb.append("    tokenId: ").append(toIndentedString(tokenId)).append("\n");
    sb.append("    uri: ").append(toIndentedString(uri)).append("\n");
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
    openapiFields.add("contractInfo");
    openapiFields.add("tokenId");
    openapiFields.add("uri");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetNFTMetaV2200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetNFTMetaV2200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetNFTMetaV2200Response is not found in the empty JSON string", GetNFTMetaV2200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetNFTMetaV2200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetNFTMetaV2200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `contractInfo`
      if (jsonObj.get("contractInfo") != null && !jsonObj.get("contractInfo").isJsonNull()) {
        GetNFTMetaV2200ResponseContractInfo.validateJsonElement(jsonObj.get("contractInfo"));
      }
      if ((jsonObj.get("tokenId") != null && !jsonObj.get("tokenId").isJsonNull()) && !jsonObj.get("tokenId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tokenId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tokenId").toString()));
      }
      if ((jsonObj.get("uri") != null && !jsonObj.get("uri").isJsonNull()) && !jsonObj.get("uri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uri").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetNFTMetaV2200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetNFTMetaV2200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetNFTMetaV2200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetNFTMetaV2200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<GetNFTMetaV2200Response>() {
           @Override
           public void write(JsonWriter out, GetNFTMetaV2200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetNFTMetaV2200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetNFTMetaV2200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetNFTMetaV2200Response
   * @throws IOException if the JSON string is invalid with respect to GetNFTMetaV2200Response
   */
  public static GetNFTMetaV2200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetNFTMetaV2200Response.class);
  }

  /**
   * Convert an instance of GetNFTMetaV2200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

