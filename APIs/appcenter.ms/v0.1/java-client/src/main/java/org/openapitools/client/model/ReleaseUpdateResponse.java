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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ReleasesUpdateDetails200ResponseDestinationsInner;

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
 * Response for updating a release
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ReleaseUpdateResponse {
  public static final String SERIALIZED_NAME_DESTINATIONS = "destinations";
  @SerializedName(SERIALIZED_NAME_DESTINATIONS)
  private List<ReleasesUpdateDetails200ResponseDestinationsInner> destinations = new ArrayList<>();

  public static final String SERIALIZED_NAME_ENABLED = "enabled";
  @SerializedName(SERIALIZED_NAME_ENABLED)
  private Boolean enabled;

  public static final String SERIALIZED_NAME_MANDATORY_UPDATE = "mandatory_update";
  @SerializedName(SERIALIZED_NAME_MANDATORY_UPDATE)
  private Boolean mandatoryUpdate;

  public static final String SERIALIZED_NAME_PROVISIONING_STATUS_URL = "provisioning_status_url";
  @SerializedName(SERIALIZED_NAME_PROVISIONING_STATUS_URL)
  private String provisioningStatusUrl;

  public static final String SERIALIZED_NAME_RELEASE_NOTES = "release_notes";
  @SerializedName(SERIALIZED_NAME_RELEASE_NOTES)
  private String releaseNotes;

  public ReleaseUpdateResponse() {
  }

  public ReleaseUpdateResponse destinations(List<ReleasesUpdateDetails200ResponseDestinationsInner> destinations) {
    this.destinations = destinations;
    return this;
  }

  public ReleaseUpdateResponse addDestinationsItem(ReleasesUpdateDetails200ResponseDestinationsInner destinationsItem) {
    if (this.destinations == null) {
      this.destinations = new ArrayList<>();
    }
    this.destinations.add(destinationsItem);
    return this;
  }

  /**
   * Get destinations
   * @return destinations
   */
  @javax.annotation.Nullable
  public List<ReleasesUpdateDetails200ResponseDestinationsInner> getDestinations() {
    return destinations;
  }

  public void setDestinations(List<ReleasesUpdateDetails200ResponseDestinationsInner> destinations) {
    this.destinations = destinations;
  }


  public ReleaseUpdateResponse enabled(Boolean enabled) {
    this.enabled = enabled;
    return this;
  }

  /**
   * Get enabled
   * @return enabled
   */
  @javax.annotation.Nullable
  public Boolean getEnabled() {
    return enabled;
  }

  public void setEnabled(Boolean enabled) {
    this.enabled = enabled;
  }


  public ReleaseUpdateResponse mandatoryUpdate(Boolean mandatoryUpdate) {
    this.mandatoryUpdate = mandatoryUpdate;
    return this;
  }

  /**
   * Get mandatoryUpdate
   * @return mandatoryUpdate
   */
  @javax.annotation.Nullable
  public Boolean getMandatoryUpdate() {
    return mandatoryUpdate;
  }

  public void setMandatoryUpdate(Boolean mandatoryUpdate) {
    this.mandatoryUpdate = mandatoryUpdate;
  }


  public ReleaseUpdateResponse provisioningStatusUrl(String provisioningStatusUrl) {
    this.provisioningStatusUrl = provisioningStatusUrl;
    return this;
  }

  /**
   * Get provisioningStatusUrl
   * @return provisioningStatusUrl
   */
  @javax.annotation.Nullable
  public String getProvisioningStatusUrl() {
    return provisioningStatusUrl;
  }

  public void setProvisioningStatusUrl(String provisioningStatusUrl) {
    this.provisioningStatusUrl = provisioningStatusUrl;
  }


  public ReleaseUpdateResponse releaseNotes(String releaseNotes) {
    this.releaseNotes = releaseNotes;
    return this;
  }

  /**
   * Get releaseNotes
   * @return releaseNotes
   */
  @javax.annotation.Nullable
  public String getReleaseNotes() {
    return releaseNotes;
  }

  public void setReleaseNotes(String releaseNotes) {
    this.releaseNotes = releaseNotes;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ReleaseUpdateResponse releaseUpdateResponse = (ReleaseUpdateResponse) o;
    return Objects.equals(this.destinations, releaseUpdateResponse.destinations) &&
        Objects.equals(this.enabled, releaseUpdateResponse.enabled) &&
        Objects.equals(this.mandatoryUpdate, releaseUpdateResponse.mandatoryUpdate) &&
        Objects.equals(this.provisioningStatusUrl, releaseUpdateResponse.provisioningStatusUrl) &&
        Objects.equals(this.releaseNotes, releaseUpdateResponse.releaseNotes);
  }

  @Override
  public int hashCode() {
    return Objects.hash(destinations, enabled, mandatoryUpdate, provisioningStatusUrl, releaseNotes);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ReleaseUpdateResponse {\n");
    sb.append("    destinations: ").append(toIndentedString(destinations)).append("\n");
    sb.append("    enabled: ").append(toIndentedString(enabled)).append("\n");
    sb.append("    mandatoryUpdate: ").append(toIndentedString(mandatoryUpdate)).append("\n");
    sb.append("    provisioningStatusUrl: ").append(toIndentedString(provisioningStatusUrl)).append("\n");
    sb.append("    releaseNotes: ").append(toIndentedString(releaseNotes)).append("\n");
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
    openapiFields.add("destinations");
    openapiFields.add("enabled");
    openapiFields.add("mandatory_update");
    openapiFields.add("provisioning_status_url");
    openapiFields.add("release_notes");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ReleaseUpdateResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ReleaseUpdateResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ReleaseUpdateResponse is not found in the empty JSON string", ReleaseUpdateResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ReleaseUpdateResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ReleaseUpdateResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("destinations") != null && !jsonObj.get("destinations").isJsonNull()) {
        JsonArray jsonArraydestinations = jsonObj.getAsJsonArray("destinations");
        if (jsonArraydestinations != null) {
          // ensure the json data is an array
          if (!jsonObj.get("destinations").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `destinations` to be an array in the JSON string but got `%s`", jsonObj.get("destinations").toString()));
          }

          // validate the optional field `destinations` (array)
          for (int i = 0; i < jsonArraydestinations.size(); i++) {
            ReleasesUpdateDetails200ResponseDestinationsInner.validateJsonElement(jsonArraydestinations.get(i));
          };
        }
      }
      if ((jsonObj.get("provisioning_status_url") != null && !jsonObj.get("provisioning_status_url").isJsonNull()) && !jsonObj.get("provisioning_status_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `provisioning_status_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("provisioning_status_url").toString()));
      }
      if ((jsonObj.get("release_notes") != null && !jsonObj.get("release_notes").isJsonNull()) && !jsonObj.get("release_notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `release_notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("release_notes").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ReleaseUpdateResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ReleaseUpdateResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ReleaseUpdateResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ReleaseUpdateResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<ReleaseUpdateResponse>() {
           @Override
           public void write(JsonWriter out, ReleaseUpdateResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ReleaseUpdateResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ReleaseUpdateResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ReleaseUpdateResponse
   * @throws IOException if the JSON string is invalid with respect to ReleaseUpdateResponse
   */
  public static ReleaseUpdateResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ReleaseUpdateResponse.class);
  }

  /**
   * Convert an instance of ReleaseUpdateResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

