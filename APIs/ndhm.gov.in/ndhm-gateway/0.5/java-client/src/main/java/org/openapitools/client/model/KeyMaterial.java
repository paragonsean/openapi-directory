/*
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
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
import org.openapitools.client.model.KeyObject;

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
 * KeyMaterial
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:45.290770-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class KeyMaterial {
  public static final String SERIALIZED_NAME_CRYPTO_ALG = "cryptoAlg";
  @SerializedName(SERIALIZED_NAME_CRYPTO_ALG)
  private String cryptoAlg;

  public static final String SERIALIZED_NAME_CURVE = "curve";
  @SerializedName(SERIALIZED_NAME_CURVE)
  private String curve;

  public static final String SERIALIZED_NAME_DH_PUBLIC_KEY = "dhPublicKey";
  @SerializedName(SERIALIZED_NAME_DH_PUBLIC_KEY)
  private KeyObject dhPublicKey;

  public static final String SERIALIZED_NAME_NONCE = "nonce";
  @SerializedName(SERIALIZED_NAME_NONCE)
  private String nonce;

  public KeyMaterial() {
  }

  public KeyMaterial cryptoAlg(String cryptoAlg) {
    this.cryptoAlg = cryptoAlg;
    return this;
  }

  /**
   * Get cryptoAlg
   * @return cryptoAlg
   */
  @javax.annotation.Nonnull
  public String getCryptoAlg() {
    return cryptoAlg;
  }

  public void setCryptoAlg(String cryptoAlg) {
    this.cryptoAlg = cryptoAlg;
  }


  public KeyMaterial curve(String curve) {
    this.curve = curve;
    return this;
  }

  /**
   * Get curve
   * @return curve
   */
  @javax.annotation.Nonnull
  public String getCurve() {
    return curve;
  }

  public void setCurve(String curve) {
    this.curve = curve;
  }


  public KeyMaterial dhPublicKey(KeyObject dhPublicKey) {
    this.dhPublicKey = dhPublicKey;
    return this;
  }

  /**
   * Get dhPublicKey
   * @return dhPublicKey
   */
  @javax.annotation.Nonnull
  public KeyObject getDhPublicKey() {
    return dhPublicKey;
  }

  public void setDhPublicKey(KeyObject dhPublicKey) {
    this.dhPublicKey = dhPublicKey;
  }


  public KeyMaterial nonce(String nonce) {
    this.nonce = nonce;
    return this;
  }

  /**
   * Get nonce
   * @return nonce
   */
  @javax.annotation.Nonnull
  public String getNonce() {
    return nonce;
  }

  public void setNonce(String nonce) {
    this.nonce = nonce;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    KeyMaterial keyMaterial = (KeyMaterial) o;
    return Objects.equals(this.cryptoAlg, keyMaterial.cryptoAlg) &&
        Objects.equals(this.curve, keyMaterial.curve) &&
        Objects.equals(this.dhPublicKey, keyMaterial.dhPublicKey) &&
        Objects.equals(this.nonce, keyMaterial.nonce);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cryptoAlg, curve, dhPublicKey, nonce);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class KeyMaterial {\n");
    sb.append("    cryptoAlg: ").append(toIndentedString(cryptoAlg)).append("\n");
    sb.append("    curve: ").append(toIndentedString(curve)).append("\n");
    sb.append("    dhPublicKey: ").append(toIndentedString(dhPublicKey)).append("\n");
    sb.append("    nonce: ").append(toIndentedString(nonce)).append("\n");
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
    openapiFields.add("cryptoAlg");
    openapiFields.add("curve");
    openapiFields.add("dhPublicKey");
    openapiFields.add("nonce");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("cryptoAlg");
    openapiRequiredFields.add("curve");
    openapiRequiredFields.add("dhPublicKey");
    openapiRequiredFields.add("nonce");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to KeyMaterial
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!KeyMaterial.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in KeyMaterial is not found in the empty JSON string", KeyMaterial.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!KeyMaterial.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `KeyMaterial` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : KeyMaterial.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("cryptoAlg").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cryptoAlg` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cryptoAlg").toString()));
      }
      if (!jsonObj.get("curve").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `curve` to be a primitive type in the JSON string but got `%s`", jsonObj.get("curve").toString()));
      }
      // validate the required field `dhPublicKey`
      KeyObject.validateJsonElement(jsonObj.get("dhPublicKey"));
      if (!jsonObj.get("nonce").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nonce` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nonce").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!KeyMaterial.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'KeyMaterial' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<KeyMaterial> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(KeyMaterial.class));

       return (TypeAdapter<T>) new TypeAdapter<KeyMaterial>() {
           @Override
           public void write(JsonWriter out, KeyMaterial value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public KeyMaterial read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of KeyMaterial given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of KeyMaterial
   * @throws IOException if the JSON string is invalid with respect to KeyMaterial
   */
  public static KeyMaterial fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, KeyMaterial.class);
  }

  /**
   * Convert an instance of KeyMaterial to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

