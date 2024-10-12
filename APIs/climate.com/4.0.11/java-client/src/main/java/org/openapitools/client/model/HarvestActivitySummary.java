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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
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
 * HarvestActivitySummary
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:32.334271-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class HarvestActivitySummary {
  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_END_TIME = "endTime";
  @SerializedName(SERIALIZED_NAME_END_TIME)
  private OffsetDateTime endTime;

  public static final String SERIALIZED_NAME_FIELD_IDS = "fieldIds";
  @SerializedName(SERIALIZED_NAME_FIELD_IDS)
  private List<String> fieldIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_LENGTH = "length";
  @SerializedName(SERIALIZED_NAME_LENGTH)
  private Long length;

  public static final String SERIALIZED_NAME_START_TIME = "startTime";
  @SerializedName(SERIALIZED_NAME_START_TIME)
  private OffsetDateTime startTime;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updatedAt";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public HarvestActivitySummary() {
  }

  public HarvestActivitySummary createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * The time the harvest activity was created. Time in ISO 8601 format with UTC timezone, 3 fractional seconds. (https://tools.ietf.org/html/rfc3339).
   * @return createdAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public HarvestActivitySummary endTime(OffsetDateTime endTime) {
    this.endTime = endTime;
    return this;
  }

  /**
   * The start time of the harvest activity. Time in ISO 8601 format with UTC timezone, 3 fractional seconds (https://tools.ietf.org/html/rfc3339).
   * @return endTime
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getEndTime() {
    return endTime;
  }

  public void setEndTime(OffsetDateTime endTime) {
    this.endTime = endTime;
  }


  public HarvestActivitySummary fieldIds(List<String> fieldIds) {
    this.fieldIds = fieldIds;
    return this;
  }

  public HarvestActivitySummary addFieldIdsItem(String fieldIdsItem) {
    if (this.fieldIds == null) {
      this.fieldIds = new ArrayList<>();
    }
    this.fieldIds.add(fieldIdsItem);
    return this;
  }

  /**
   * Array of field ids associated the harvest activity.
   * @return fieldIds
   */
  @javax.annotation.Nonnull
  public List<String> getFieldIds() {
    return fieldIds;
  }

  public void setFieldIds(List<String> fieldIds) {
    this.fieldIds = fieldIds;
  }


  public HarvestActivitySummary id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * The id of a harvest activity.
   * @return id
   */
  @javax.annotation.Nonnull
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public HarvestActivitySummary length(Long length) {
    this.length = length;
    return this;
  }

  /**
   * The size in bytes of the raw harvest activity file.
   * @return length
   */
  @javax.annotation.Nonnull
  public Long getLength() {
    return length;
  }

  public void setLength(Long length) {
    this.length = length;
  }


  public HarvestActivitySummary startTime(OffsetDateTime startTime) {
    this.startTime = startTime;
    return this;
  }

  /**
   * The start time of the harvest activity. Time in ISO 8601 format with UTC timezone, 3 fractional seconds (https://tools.ietf.org/html/rfc3339).
   * @return startTime
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getStartTime() {
    return startTime;
  }

  public void setStartTime(OffsetDateTime startTime) {
    this.startTime = startTime;
  }


  public HarvestActivitySummary updatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

  /**
   * The time the harvest activity was last updated. Time in ISO 8601 format with UTC timezone, 3 fractional seconds. (https://tools.ietf.org/html/rfc3339).
   * @return updatedAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HarvestActivitySummary harvestActivitySummary = (HarvestActivitySummary) o;
    return Objects.equals(this.createdAt, harvestActivitySummary.createdAt) &&
        Objects.equals(this.endTime, harvestActivitySummary.endTime) &&
        Objects.equals(this.fieldIds, harvestActivitySummary.fieldIds) &&
        Objects.equals(this.id, harvestActivitySummary.id) &&
        Objects.equals(this.length, harvestActivitySummary.length) &&
        Objects.equals(this.startTime, harvestActivitySummary.startTime) &&
        Objects.equals(this.updatedAt, harvestActivitySummary.updatedAt);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdAt, endTime, fieldIds, id, length, startTime, updatedAt);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HarvestActivitySummary {\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    endTime: ").append(toIndentedString(endTime)).append("\n");
    sb.append("    fieldIds: ").append(toIndentedString(fieldIds)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    length: ").append(toIndentedString(length)).append("\n");
    sb.append("    startTime: ").append(toIndentedString(startTime)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
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
    openapiFields.add("createdAt");
    openapiFields.add("endTime");
    openapiFields.add("fieldIds");
    openapiFields.add("id");
    openapiFields.add("length");
    openapiFields.add("startTime");
    openapiFields.add("updatedAt");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("createdAt");
    openapiRequiredFields.add("endTime");
    openapiRequiredFields.add("fieldIds");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("length");
    openapiRequiredFields.add("startTime");
    openapiRequiredFields.add("updatedAt");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to HarvestActivitySummary
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!HarvestActivitySummary.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HarvestActivitySummary is not found in the empty JSON string", HarvestActivitySummary.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!HarvestActivitySummary.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `HarvestActivitySummary` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : HarvestActivitySummary.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the required json array is present
      if (jsonObj.get("fieldIds") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("fieldIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `fieldIds` to be an array in the JSON string but got `%s`", jsonObj.get("fieldIds").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!HarvestActivitySummary.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HarvestActivitySummary' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HarvestActivitySummary> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HarvestActivitySummary.class));

       return (TypeAdapter<T>) new TypeAdapter<HarvestActivitySummary>() {
           @Override
           public void write(JsonWriter out, HarvestActivitySummary value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public HarvestActivitySummary read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of HarvestActivitySummary given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of HarvestActivitySummary
   * @throws IOException if the JSON string is invalid with respect to HarvestActivitySummary
   */
  public static HarvestActivitySummary fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HarvestActivitySummary.class);
  }

  /**
   * Convert an instance of HarvestActivitySummary to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

