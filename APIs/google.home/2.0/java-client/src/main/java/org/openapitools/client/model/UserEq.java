/*
 * Google Home
 * # Google Home Local API This is an unofficial documentation of the local API used by the Home app to communicate with GH devices. [GitHub Repo](https://github.com/rithvikvibhu/GHLocalApi)  [![GitHub stars](https://img.shields.io/github/stars/rithvikvibhu/GHLocalApi)](https://github.com/rithvikvibhu/GHLocalApi/stargazers) [![GitHub license](https://img.shields.io/github/license/rithvikvibhu/GHLocalApi)](https://github.com/rithvikvibhu/GHLocalApi/blob/master/LICENSE.md)  ## Getting Started  Requests must be made over HTTPS, port 8443, so the base URL for these endpoints is: `https://<google-home-ip>:8443/setup/`  Get the IP of Google Home from the Google Home app (Device Settings -> End of the list) or from your router.  GET requests are simple, in the browser kind.   POST requests need to set the header (when there's a body): `content-type: application/json`  ## Authentication  Since June 2019, most requests (with exceptions like `/setup/eureka_info`) need a local authorization token.  There are 3 kinds of tokens involved here:  ### Local Authorization Token This token must be sent in all requests in the header `cast-local-authorization-token`. It is short-lived (~1 day) and may change unexpectedly (with a sync, change in homegraph, etc.) ##### Get this token - With access to an android device, [get this token directly by either method](https://gist.github.com/rithvikvibhu/1a0f4937af957ef6a78453e3be482c1f). - Without a device, or to integrate it with a script, use an access token to get the homegraph and extract the token. To get an access token, read the next section. Check the example section for more info.  ### Access Token This is a standard google oauth2 access token. It is in the form `ya29.***`. This gives access to the Google Home Foyer API. These expire in an hour. Use this to get the homegraph (and then the local authorization token above). ##### Get this token To get this access token, either a Google account username/password or a Google Master Token is needed. More info in the gist. Use the script [from this gist](https://gist.github.com/rithvikvibhu/952f83ea656c6782fbd0f1645059055d).  ### Master Token This is in the form `aas_et/_***` and can be used to request access tokens. ##### Get this token The same [script in the gist](https://gist.github.com/rithvikvibhu/952f83ea656c6782fbd0f1645059055d) that gets the access token can also get the master token. Needs Google account creds.  ## Example  Here's the whole flow from just a pair of username/password to using the local API.  Prerequisites: - [grpcurl](https://github.com/fullstorydev/grpcurl) - [Proto files](https://drive.google.com/drive/folders/1RvnN3y-G23pd2SWHmfV_7sef8QU5GNF4?usp=sharing) (preserve folder structure)  ### 1. Get an access token with the script - Download get_tokens.py - Fill in username and password ```sh python3 get_tokens.py # Note down the access token printed. ```  ### 2. Use the access token and get home graph - This prints the json and uses jq to parse and filter out the fields deviceName and localAuthToken - This will give a list of all devices and their local auth tokens ```sh ./grpcurl -H 'authorization: Bearer ya29.a0Af****' \\  -import-path /path/to/protos \\  -proto /path/to/protos/google/internal/home/foyer/v1.proto \\  googlehomefoyer-pa.googleapis.com:443 \\  google.internal.home.foyer.v1.StructuresService/GetHomeGraph | jq '.home.devices[] | {deviceName, localAuthToken}' # Note down the local auth token for the device you want. ```  ### 3. Make the call to the local device using the local auth token ```sh curl -H \"cast-local-authorization-token: LOCAL_AUTH_TOKEN\" --verbose --insecure https://192.168.0.18:8443/setup/bluetooth/status ```
 *
 * The version of the OpenAPI document: 2.0
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
import org.openapitools.client.model.HighShelf;
import org.openapitools.client.model.LowShelf;

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
 * UserEq
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:31.661536-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UserEq {
  public static final String SERIALIZED_NAME_HIGH_SHELF = "high_shelf";
  @SerializedName(SERIALIZED_NAME_HIGH_SHELF)
  private HighShelf highShelf;

  public static final String SERIALIZED_NAME_LOW_SHELF = "low_shelf";
  @SerializedName(SERIALIZED_NAME_LOW_SHELF)
  private LowShelf lowShelf;

  public static final String SERIALIZED_NAME_MAX_PEAKING_EQS = "max_peaking_eqs";
  @SerializedName(SERIALIZED_NAME_MAX_PEAKING_EQS)
  private Integer maxPeakingEqs;

  public static final String SERIALIZED_NAME_PEAKING_EQS = "peaking_eqs";
  @SerializedName(SERIALIZED_NAME_PEAKING_EQS)
  private List<String> peakingEqs = new ArrayList<>();

  public UserEq() {
  }

  public UserEq highShelf(HighShelf highShelf) {
    this.highShelf = highShelf;
    return this;
  }

  /**
   * Get highShelf
   * @return highShelf
   */
  @javax.annotation.Nonnull
  public HighShelf getHighShelf() {
    return highShelf;
  }

  public void setHighShelf(HighShelf highShelf) {
    this.highShelf = highShelf;
  }


  public UserEq lowShelf(LowShelf lowShelf) {
    this.lowShelf = lowShelf;
    return this;
  }

  /**
   * Get lowShelf
   * @return lowShelf
   */
  @javax.annotation.Nonnull
  public LowShelf getLowShelf() {
    return lowShelf;
  }

  public void setLowShelf(LowShelf lowShelf) {
    this.lowShelf = lowShelf;
  }


  public UserEq maxPeakingEqs(Integer maxPeakingEqs) {
    this.maxPeakingEqs = maxPeakingEqs;
    return this;
  }

  /**
   * Get maxPeakingEqs
   * @return maxPeakingEqs
   */
  @javax.annotation.Nonnull
  public Integer getMaxPeakingEqs() {
    return maxPeakingEqs;
  }

  public void setMaxPeakingEqs(Integer maxPeakingEqs) {
    this.maxPeakingEqs = maxPeakingEqs;
  }


  public UserEq peakingEqs(List<String> peakingEqs) {
    this.peakingEqs = peakingEqs;
    return this;
  }

  public UserEq addPeakingEqsItem(String peakingEqsItem) {
    if (this.peakingEqs == null) {
      this.peakingEqs = new ArrayList<>();
    }
    this.peakingEqs.add(peakingEqsItem);
    return this;
  }

  /**
   * Get peakingEqs
   * @return peakingEqs
   */
  @javax.annotation.Nonnull
  public List<String> getPeakingEqs() {
    return peakingEqs;
  }

  public void setPeakingEqs(List<String> peakingEqs) {
    this.peakingEqs = peakingEqs;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UserEq userEq = (UserEq) o;
    return Objects.equals(this.highShelf, userEq.highShelf) &&
        Objects.equals(this.lowShelf, userEq.lowShelf) &&
        Objects.equals(this.maxPeakingEqs, userEq.maxPeakingEqs) &&
        Objects.equals(this.peakingEqs, userEq.peakingEqs);
  }

  @Override
  public int hashCode() {
    return Objects.hash(highShelf, lowShelf, maxPeakingEqs, peakingEqs);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UserEq {\n");
    sb.append("    highShelf: ").append(toIndentedString(highShelf)).append("\n");
    sb.append("    lowShelf: ").append(toIndentedString(lowShelf)).append("\n");
    sb.append("    maxPeakingEqs: ").append(toIndentedString(maxPeakingEqs)).append("\n");
    sb.append("    peakingEqs: ").append(toIndentedString(peakingEqs)).append("\n");
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
    openapiFields.add("high_shelf");
    openapiFields.add("low_shelf");
    openapiFields.add("max_peaking_eqs");
    openapiFields.add("peaking_eqs");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("high_shelf");
    openapiRequiredFields.add("low_shelf");
    openapiRequiredFields.add("max_peaking_eqs");
    openapiRequiredFields.add("peaking_eqs");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UserEq
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UserEq.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UserEq is not found in the empty JSON string", UserEq.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UserEq.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UserEq` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UserEq.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `high_shelf`
      HighShelf.validateJsonElement(jsonObj.get("high_shelf"));
      // validate the required field `low_shelf`
      LowShelf.validateJsonElement(jsonObj.get("low_shelf"));
      // ensure the required json array is present
      if (jsonObj.get("peaking_eqs") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("peaking_eqs").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `peaking_eqs` to be an array in the JSON string but got `%s`", jsonObj.get("peaking_eqs").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UserEq.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UserEq' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UserEq> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UserEq.class));

       return (TypeAdapter<T>) new TypeAdapter<UserEq>() {
           @Override
           public void write(JsonWriter out, UserEq value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UserEq read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UserEq given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UserEq
   * @throws IOException if the JSON string is invalid with respect to UserEq
   */
  public static UserEq fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UserEq.class);
  }

  /**
   * Convert an instance of UserEq to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

