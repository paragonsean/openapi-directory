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
 * Settings for describing which kinds of admins this policy applies to.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationBrandingPolicies200ResponseInnerAdminSettings {
  /**
   * Which kinds of admins this policy applies to. Can be one of &#39;All organization admins&#39;, &#39;All enterprise admins&#39;, &#39;All network admins&#39;, &#39;All admins of networks...&#39;, &#39;All admins of networks tagged...&#39;, &#39;Specific admins...&#39;, &#39;All admins&#39; or &#39;All SAML admins&#39;.
   */
  @JsonAdapter(AppliesToEnum.Adapter.class)
  public enum AppliesToEnum {
    ALL_SAML_ADMINS("All SAML admins"),
    
    ALL_ADMINS("All admins"),
    
    ALL_ADMINS_OF_NETWORKS_TAGGED_("All admins of networks tagged..."),
    
    ALL_ADMINS_OF_NETWORKS_("All admins of networks..."),
    
    ALL_ENTERPRISE_ADMINS("All enterprise admins"),
    
    ALL_NETWORK_ADMINS("All network admins"),
    
    ALL_ORGANIZATION_ADMINS("All organization admins"),
    
    SPECIFIC_ADMINS_("Specific admins...");

    private String value;

    AppliesToEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AppliesToEnum fromValue(String value) {
      for (AppliesToEnum b : AppliesToEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AppliesToEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AppliesToEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AppliesToEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AppliesToEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AppliesToEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_APPLIES_TO = "appliesTo";
  @SerializedName(SERIALIZED_NAME_APPLIES_TO)
  private AppliesToEnum appliesTo;

  public static final String SERIALIZED_NAME_VALUES = "values";
  @SerializedName(SERIALIZED_NAME_VALUES)
  private List<String> values = new ArrayList<>();

  public GetOrganizationBrandingPolicies200ResponseInnerAdminSettings() {
  }

  public GetOrganizationBrandingPolicies200ResponseInnerAdminSettings appliesTo(AppliesToEnum appliesTo) {
    this.appliesTo = appliesTo;
    return this;
  }

  /**
   * Which kinds of admins this policy applies to. Can be one of &#39;All organization admins&#39;, &#39;All enterprise admins&#39;, &#39;All network admins&#39;, &#39;All admins of networks...&#39;, &#39;All admins of networks tagged...&#39;, &#39;Specific admins...&#39;, &#39;All admins&#39; or &#39;All SAML admins&#39;.
   * @return appliesTo
   */
  @javax.annotation.Nullable
  public AppliesToEnum getAppliesTo() {
    return appliesTo;
  }

  public void setAppliesTo(AppliesToEnum appliesTo) {
    this.appliesTo = appliesTo;
  }


  public GetOrganizationBrandingPolicies200ResponseInnerAdminSettings values(List<String> values) {
    this.values = values;
    return this;
  }

  public GetOrganizationBrandingPolicies200ResponseInnerAdminSettings addValuesItem(String valuesItem) {
    if (this.values == null) {
      this.values = new ArrayList<>();
    }
    this.values.add(valuesItem);
    return this;
  }

  /**
   *       If &#39;appliesTo&#39; is set to one of &#39;Specific admins...&#39;, &#39;All admins of networks...&#39; or &#39;All admins of networks tagged...&#39;, then you must specify this &#39;values&#39; property to provide the set of       entities to apply the branding policy to. For &#39;Specific admins...&#39;, specify an array of admin IDs. For &#39;All admins of       networks...&#39;, specify an array of network IDs and/or configuration template IDs. For &#39;All admins of networks tagged...&#39;,       specify an array of tag names. 
   * @return values
   */
  @javax.annotation.Nullable
  public List<String> getValues() {
    return values;
  }

  public void setValues(List<String> values) {
    this.values = values;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetOrganizationBrandingPolicies200ResponseInnerAdminSettings getOrganizationBrandingPolicies200ResponseInnerAdminSettings = (GetOrganizationBrandingPolicies200ResponseInnerAdminSettings) o;
    return Objects.equals(this.appliesTo, getOrganizationBrandingPolicies200ResponseInnerAdminSettings.appliesTo) &&
        Objects.equals(this.values, getOrganizationBrandingPolicies200ResponseInnerAdminSettings.values);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appliesTo, values);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationBrandingPolicies200ResponseInnerAdminSettings {\n");
    sb.append("    appliesTo: ").append(toIndentedString(appliesTo)).append("\n");
    sb.append("    values: ").append(toIndentedString(values)).append("\n");
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
    openapiFields.add("appliesTo");
    openapiFields.add("values");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationBrandingPolicies200ResponseInnerAdminSettings
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationBrandingPolicies200ResponseInnerAdminSettings.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationBrandingPolicies200ResponseInnerAdminSettings is not found in the empty JSON string", GetOrganizationBrandingPolicies200ResponseInnerAdminSettings.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationBrandingPolicies200ResponseInnerAdminSettings.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationBrandingPolicies200ResponseInnerAdminSettings` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("appliesTo") != null && !jsonObj.get("appliesTo").isJsonNull()) && !jsonObj.get("appliesTo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appliesTo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appliesTo").toString()));
      }
      // validate the optional field `appliesTo`
      if (jsonObj.get("appliesTo") != null && !jsonObj.get("appliesTo").isJsonNull()) {
        AppliesToEnum.validateJsonElement(jsonObj.get("appliesTo"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("values") != null && !jsonObj.get("values").isJsonNull() && !jsonObj.get("values").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `values` to be an array in the JSON string but got `%s`", jsonObj.get("values").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationBrandingPolicies200ResponseInnerAdminSettings.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationBrandingPolicies200ResponseInnerAdminSettings' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationBrandingPolicies200ResponseInnerAdminSettings> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationBrandingPolicies200ResponseInnerAdminSettings.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationBrandingPolicies200ResponseInnerAdminSettings>() {
           @Override
           public void write(JsonWriter out, GetOrganizationBrandingPolicies200ResponseInnerAdminSettings value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationBrandingPolicies200ResponseInnerAdminSettings read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationBrandingPolicies200ResponseInnerAdminSettings given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationBrandingPolicies200ResponseInnerAdminSettings
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationBrandingPolicies200ResponseInnerAdminSettings
   */
  public static GetOrganizationBrandingPolicies200ResponseInnerAdminSettings fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationBrandingPolicies200ResponseInnerAdminSettings.class);
  }

  /**
   * Convert an instance of GetOrganizationBrandingPolicies200ResponseInnerAdminSettings to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

