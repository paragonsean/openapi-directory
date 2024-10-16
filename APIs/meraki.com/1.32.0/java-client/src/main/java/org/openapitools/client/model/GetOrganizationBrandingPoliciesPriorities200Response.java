/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
 * GetOrganizationBrandingPoliciesPriorities200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationBrandingPoliciesPriorities200Response {
  public static final String SERIALIZED_NAME_BRANDING_POLICY_IDS = "brandingPolicyIds";
  @SerializedName(SERIALIZED_NAME_BRANDING_POLICY_IDS)
  private List<String> brandingPolicyIds = new ArrayList<>();

  public GetOrganizationBrandingPoliciesPriorities200Response() {
  }

  public GetOrganizationBrandingPoliciesPriorities200Response brandingPolicyIds(List<String> brandingPolicyIds) {
    this.brandingPolicyIds = brandingPolicyIds;
    return this;
  }

  public GetOrganizationBrandingPoliciesPriorities200Response addBrandingPolicyIdsItem(String brandingPolicyIdsItem) {
    if (this.brandingPolicyIds == null) {
      this.brandingPolicyIds = new ArrayList<>();
    }
    this.brandingPolicyIds.add(brandingPolicyIdsItem);
    return this;
  }

  /**
   *       An ordered list of branding policy IDs that determines the priority order of how to apply the policies 
   * @return brandingPolicyIds
   */
  @javax.annotation.Nullable
  public List<String> getBrandingPolicyIds() {
    return brandingPolicyIds;
  }

  public void setBrandingPolicyIds(List<String> brandingPolicyIds) {
    this.brandingPolicyIds = brandingPolicyIds;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetOrganizationBrandingPoliciesPriorities200Response getOrganizationBrandingPoliciesPriorities200Response = (GetOrganizationBrandingPoliciesPriorities200Response) o;
    return Objects.equals(this.brandingPolicyIds, getOrganizationBrandingPoliciesPriorities200Response.brandingPolicyIds);
  }

  @Override
  public int hashCode() {
    return Objects.hash(brandingPolicyIds);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationBrandingPoliciesPriorities200Response {\n");
    sb.append("    brandingPolicyIds: ").append(toIndentedString(brandingPolicyIds)).append("\n");
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
    openapiFields.add("brandingPolicyIds");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationBrandingPoliciesPriorities200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationBrandingPoliciesPriorities200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationBrandingPoliciesPriorities200Response is not found in the empty JSON string", GetOrganizationBrandingPoliciesPriorities200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationBrandingPoliciesPriorities200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationBrandingPoliciesPriorities200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("brandingPolicyIds") != null && !jsonObj.get("brandingPolicyIds").isJsonNull() && !jsonObj.get("brandingPolicyIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `brandingPolicyIds` to be an array in the JSON string but got `%s`", jsonObj.get("brandingPolicyIds").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationBrandingPoliciesPriorities200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationBrandingPoliciesPriorities200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationBrandingPoliciesPriorities200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationBrandingPoliciesPriorities200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationBrandingPoliciesPriorities200Response>() {
           @Override
           public void write(JsonWriter out, GetOrganizationBrandingPoliciesPriorities200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationBrandingPoliciesPriorities200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationBrandingPoliciesPriorities200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationBrandingPoliciesPriorities200Response
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationBrandingPoliciesPriorities200Response
   */
  public static GetOrganizationBrandingPoliciesPriorities200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationBrandingPoliciesPriorities200Response.class);
  }

  /**
   * Convert an instance of GetOrganizationBrandingPoliciesPriorities200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

