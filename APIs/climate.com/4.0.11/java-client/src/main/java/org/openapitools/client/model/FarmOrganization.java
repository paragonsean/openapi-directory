/*
 * Climate FieldView Platform APIs
 * **Last Modified**: Wed Jan  4 12:47:29 UTC 2023   All endpoints are only accessible via HTTPS.  * All API endpoints are located at `https://platform.climate.com` (e.g. `https://platform.climate.com/v4/fields`).  * The authorization token endpoint is located at `https://api.climate.com/api/oauth/token`.  ## Troubleshooting  `X-Http-Request-Id` response header will be returned on every call, successful or not. If you experience an issue with our api and need to contact technical support, please supply the value of the `X-Http-Request-Id` header along with an approximate time of when the request was made.  ## Request Limits  When you’re onboarded to Climate’s API platform, your `x-api-key` is assigned a custom usage plan. Usage plans are unique to each partner and have the following key attributes:   1. Throttling information     * burstLimit: Maximum rate limit over a period ranging from 1 second to a few seconds     * rateLimit: A steady-state rate limit  2. Quota information     * Limit: The maximum number of requests that can be made in a given month  When the request rate threshold is exceeded, a `429` response code is returned. Optionally, the [`Retry-After`](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.37) header may be returned:   Following are examples of rate limit errors:  1. Rate limit exceeded:  <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 32     {\"message\":\"Too Many Requests\"}  2. Quota exhausted: <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 29      {\"message\":\"Limit Exceeded\"}  ## Pagination  Pagination is performed via headers. Any request which returns a `\"results\"` array may be paginated. The following figure shows how query results are laid out with X-Limit=4 and no filter applied.  <img style=\"width:70%;height:auto;\" src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/paging.png\">  * If there are no results, a response code of `304` will be returned.  * If the response is the last set of results, a response code of `200` or `206` will be returned.  * If there are more results, a response code of `206` will be returned.  * If `X-Next-Token` is provided in the request headers but the token has expired, a response code of `409` will be returned. This is only applicable for some endpoints; see specific endpoint documentation below.  #### X-Limit  The page size can be controlled with the `X-Limit` header. Valid values are `1-100` and defaults to `100`.  #### X-Next-Token  If the results are paginated, a response header of `X-Next-Token` will be returned. Use the associated value in the subsequent request (via the `X-Next-Token` request header) to retrieve the next page. The following sequence diagram shows how to use `X-Next-Token` to fetch all the records.  <img src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/x-next-token.svg\">   ## Chunked Uploads  Uploads larger than `5MiB` (`5242880 bytes`) must be done in `5MiB` chunks (with the exception of the final chunk). Each chunk request MUST contain a `Content-Range` header specifying the portion of the upload, and a `Content-Type` header specifying binary content type (`application/octet-stream`). Range uploads must be contiguous. The maximum upload size is capped at `500MiB` (`524288000 bytes`).  ## Chunked Downloads  Downloads larger than `5MiB` (`5242880 bytes`) must be done in `1-5MiB` chunks (with the exception of the final chunk, which may be less than `1MiB`). Each chunk request MUST contain a `Range` header specifying the requested portion of the download, and an `Accept` header specifying binary and json content types  (`application/octet-stream,application/json`) or all content types (`*_/_*`).  ## Drivers  If you need drivers to process agronomic data, download the ADAPT plugin below. We only support the plugin in the Windows environment, minimum is Windows 7 SP1.  For asPlanted, asHarvested and asApplied data: * [ADAPT Plugin](https://dev.fieldview.com/drivers/ClimateADAPTPlugin_latest.exe) <br>Release notes can be found [here](https://dev.fieldview.com/drivers/adapt-release-notes.txt). <br>Download and use of the ADAPT plugin means that you agree to the EULA for use of the ADAPT plugin.  <br>Please review the [EULA](https://dev.fieldview.com/EULA/ADAPT%20Plugin%20EULA-06-19.pdf) (last updated on June 6th, 2019) before download and use of the ADAPT plugin. <br>For more information, please refer to:   * [ADAPT Resources](https://adaptframework.org/)   * [ADAPT Overview](https://aggateway.atlassian.net/wiki/spaces/ADM/overview)   * [ADAPT FAQ](https://aggateway.atlassian.net/wiki/spaces/ADM/pages/165942474/ADAPT+Frequently-Asked+Questions+FAQ)   * [ADAPT Videos](https://adaptframework.org/adapt-videos/)  ## Sample Test Data  Sample agronomic data: * [asPlanted and asHarvested data](https://dev.fieldview.com/sample-agronomic-data/Planting_Harvesting_data_04_18_2018_21_46_18.zip) * [asApplied data set 1](https://dev.fieldview.com/sample-agronomic-data/as-applied-data1.zip) * [asApplied data set 2](https://dev.fieldview.com/sample-agronomic-data/as-applied-data2.zip) <br>To upload the sample data to your account, please follow the instructions in this [link](https://support.climate.com/kt#/kA02A000000AaxzSAC/en_US).  Sample soil data: * [Sample soil data](https://dev.fieldview.com/sample-soil-data/soil-sample.xml) --- 
 *
 * The version of the OpenAPI document: 4.0.11
 * Contact: developer@climate.com
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
import java.util.UUID;

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
 * Logical representation of a farm organization with a name and type.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:32.334271-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FarmOrganization {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  /**
   * Type of the farm organization.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    FARM("farm");

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

  public FarmOrganization() {
  }

  public FarmOrganization id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * Unique identifier for a farm organization.
   * @return id
   */
  @javax.annotation.Nonnull
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public FarmOrganization name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of the farm organization.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public FarmOrganization type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Type of the farm organization.
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
    FarmOrganization farmOrganization = (FarmOrganization) o;
    return Objects.equals(this.id, farmOrganization.id) &&
        Objects.equals(this.name, farmOrganization.name) &&
        Objects.equals(this.type, farmOrganization.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, name, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FarmOrganization {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FarmOrganization
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FarmOrganization.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FarmOrganization is not found in the empty JSON string", FarmOrganization.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FarmOrganization.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FarmOrganization` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : FarmOrganization.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the required field `type`
      TypeEnum.validateJsonElement(jsonObj.get("type"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FarmOrganization.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FarmOrganization' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FarmOrganization> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FarmOrganization.class));

       return (TypeAdapter<T>) new TypeAdapter<FarmOrganization>() {
           @Override
           public void write(JsonWriter out, FarmOrganization value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FarmOrganization read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FarmOrganization given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FarmOrganization
   * @throws IOException if the JSON string is invalid with respect to FarmOrganization
   */
  public static FarmOrganization fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FarmOrganization.class);
  }

  /**
   * Convert an instance of FarmOrganization to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

