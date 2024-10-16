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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.GetTransactionV2200ResponseVinInner;
import org.openapitools.client.model.GetTransactionV2200ResponseVoutInner;

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
 * GetTransactionV2200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:48.868561-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetTransactionV2200Response {
  public static final String SERIALIZED_NAME_BLOCK_HASH = "blockHash";
  @SerializedName(SERIALIZED_NAME_BLOCK_HASH)
  private String blockHash;

  public static final String SERIALIZED_NAME_BLOCK_HEIGHT = "blockHeight";
  @SerializedName(SERIALIZED_NAME_BLOCK_HEIGHT)
  private Integer blockHeight;

  public static final String SERIALIZED_NAME_BLOCK_TIME = "blockTime";
  @SerializedName(SERIALIZED_NAME_BLOCK_TIME)
  private Integer blockTime;

  public static final String SERIALIZED_NAME_CONFIRMATIONS = "confirmations";
  @SerializedName(SERIALIZED_NAME_CONFIRMATIONS)
  private Integer confirmations;

  public static final String SERIALIZED_NAME_FEES = "fees";
  @SerializedName(SERIALIZED_NAME_FEES)
  private String fees;

  public static final String SERIALIZED_NAME_HEX = "hex";
  @SerializedName(SERIALIZED_NAME_HEX)
  private String hex;

  public static final String SERIALIZED_NAME_SIZE = "size";
  @SerializedName(SERIALIZED_NAME_SIZE)
  private Integer size;

  public static final String SERIALIZED_NAME_TXID = "txid";
  @SerializedName(SERIALIZED_NAME_TXID)
  private String txid;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private String value;

  public static final String SERIALIZED_NAME_VALUE_IN = "valueIn";
  @SerializedName(SERIALIZED_NAME_VALUE_IN)
  private String valueIn;

  public static final String SERIALIZED_NAME_VERSION = "version";
  @SerializedName(SERIALIZED_NAME_VERSION)
  private Integer version;

  public static final String SERIALIZED_NAME_VIN = "vin";
  @SerializedName(SERIALIZED_NAME_VIN)
  private List<GetTransactionV2200ResponseVinInner> vin = new ArrayList<>();

  public static final String SERIALIZED_NAME_VOUT = "vout";
  @SerializedName(SERIALIZED_NAME_VOUT)
  private List<GetTransactionV2200ResponseVoutInner> vout = new ArrayList<>();

  public static final String SERIALIZED_NAME_VSIZE = "vsize";
  @SerializedName(SERIALIZED_NAME_VSIZE)
  private Integer vsize;

  public GetTransactionV2200Response() {
  }

  public GetTransactionV2200Response blockHash(String blockHash) {
    this.blockHash = blockHash;
    return this;
  }

  /**
   * Get blockHash
   * @return blockHash
   */
  @javax.annotation.Nullable
  public String getBlockHash() {
    return blockHash;
  }

  public void setBlockHash(String blockHash) {
    this.blockHash = blockHash;
  }


  public GetTransactionV2200Response blockHeight(Integer blockHeight) {
    this.blockHeight = blockHeight;
    return this;
  }

  /**
   * Get blockHeight
   * @return blockHeight
   */
  @javax.annotation.Nullable
  public Integer getBlockHeight() {
    return blockHeight;
  }

  public void setBlockHeight(Integer blockHeight) {
    this.blockHeight = blockHeight;
  }


  public GetTransactionV2200Response blockTime(Integer blockTime) {
    this.blockTime = blockTime;
    return this;
  }

  /**
   * Get blockTime
   * @return blockTime
   */
  @javax.annotation.Nullable
  public Integer getBlockTime() {
    return blockTime;
  }

  public void setBlockTime(Integer blockTime) {
    this.blockTime = blockTime;
  }


  public GetTransactionV2200Response confirmations(Integer confirmations) {
    this.confirmations = confirmations;
    return this;
  }

  /**
   * Get confirmations
   * @return confirmations
   */
  @javax.annotation.Nullable
  public Integer getConfirmations() {
    return confirmations;
  }

  public void setConfirmations(Integer confirmations) {
    this.confirmations = confirmations;
  }


  public GetTransactionV2200Response fees(String fees) {
    this.fees = fees;
    return this;
  }

  /**
   * Get fees
   * @return fees
   */
  @javax.annotation.Nullable
  public String getFees() {
    return fees;
  }

  public void setFees(String fees) {
    this.fees = fees;
  }


  public GetTransactionV2200Response hex(String hex) {
    this.hex = hex;
    return this;
  }

  /**
   * Get hex
   * @return hex
   */
  @javax.annotation.Nullable
  public String getHex() {
    return hex;
  }

  public void setHex(String hex) {
    this.hex = hex;
  }


  public GetTransactionV2200Response size(Integer size) {
    this.size = size;
    return this;
  }

  /**
   * Get size
   * @return size
   */
  @javax.annotation.Nullable
  public Integer getSize() {
    return size;
  }

  public void setSize(Integer size) {
    this.size = size;
  }


  public GetTransactionV2200Response txid(String txid) {
    this.txid = txid;
    return this;
  }

  /**
   * Get txid
   * @return txid
   */
  @javax.annotation.Nullable
  public String getTxid() {
    return txid;
  }

  public void setTxid(String txid) {
    this.txid = txid;
  }


  public GetTransactionV2200Response value(String value) {
    this.value = value;
    return this;
  }

  /**
   * Get value
   * @return value
   */
  @javax.annotation.Nullable
  public String getValue() {
    return value;
  }

  public void setValue(String value) {
    this.value = value;
  }


  public GetTransactionV2200Response valueIn(String valueIn) {
    this.valueIn = valueIn;
    return this;
  }

  /**
   * Get valueIn
   * @return valueIn
   */
  @javax.annotation.Nullable
  public String getValueIn() {
    return valueIn;
  }

  public void setValueIn(String valueIn) {
    this.valueIn = valueIn;
  }


  public GetTransactionV2200Response version(Integer version) {
    this.version = version;
    return this;
  }

  /**
   * Get version
   * @return version
   */
  @javax.annotation.Nullable
  public Integer getVersion() {
    return version;
  }

  public void setVersion(Integer version) {
    this.version = version;
  }


  public GetTransactionV2200Response vin(List<GetTransactionV2200ResponseVinInner> vin) {
    this.vin = vin;
    return this;
  }

  public GetTransactionV2200Response addVinItem(GetTransactionV2200ResponseVinInner vinItem) {
    if (this.vin == null) {
      this.vin = new ArrayList<>();
    }
    this.vin.add(vinItem);
    return this;
  }

  /**
   * Get vin
   * @return vin
   */
  @javax.annotation.Nullable
  public List<GetTransactionV2200ResponseVinInner> getVin() {
    return vin;
  }

  public void setVin(List<GetTransactionV2200ResponseVinInner> vin) {
    this.vin = vin;
  }


  public GetTransactionV2200Response vout(List<GetTransactionV2200ResponseVoutInner> vout) {
    this.vout = vout;
    return this;
  }

  public GetTransactionV2200Response addVoutItem(GetTransactionV2200ResponseVoutInner voutItem) {
    if (this.vout == null) {
      this.vout = new ArrayList<>();
    }
    this.vout.add(voutItem);
    return this;
  }

  /**
   * Get vout
   * @return vout
   */
  @javax.annotation.Nullable
  public List<GetTransactionV2200ResponseVoutInner> getVout() {
    return vout;
  }

  public void setVout(List<GetTransactionV2200ResponseVoutInner> vout) {
    this.vout = vout;
  }


  public GetTransactionV2200Response vsize(Integer vsize) {
    this.vsize = vsize;
    return this;
  }

  /**
   * Get vsize
   * @return vsize
   */
  @javax.annotation.Nullable
  public Integer getVsize() {
    return vsize;
  }

  public void setVsize(Integer vsize) {
    this.vsize = vsize;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetTransactionV2200Response getTransactionV2200Response = (GetTransactionV2200Response) o;
    return Objects.equals(this.blockHash, getTransactionV2200Response.blockHash) &&
        Objects.equals(this.blockHeight, getTransactionV2200Response.blockHeight) &&
        Objects.equals(this.blockTime, getTransactionV2200Response.blockTime) &&
        Objects.equals(this.confirmations, getTransactionV2200Response.confirmations) &&
        Objects.equals(this.fees, getTransactionV2200Response.fees) &&
        Objects.equals(this.hex, getTransactionV2200Response.hex) &&
        Objects.equals(this.size, getTransactionV2200Response.size) &&
        Objects.equals(this.txid, getTransactionV2200Response.txid) &&
        Objects.equals(this.value, getTransactionV2200Response.value) &&
        Objects.equals(this.valueIn, getTransactionV2200Response.valueIn) &&
        Objects.equals(this.version, getTransactionV2200Response.version) &&
        Objects.equals(this.vin, getTransactionV2200Response.vin) &&
        Objects.equals(this.vout, getTransactionV2200Response.vout) &&
        Objects.equals(this.vsize, getTransactionV2200Response.vsize);
  }

  @Override
  public int hashCode() {
    return Objects.hash(blockHash, blockHeight, blockTime, confirmations, fees, hex, size, txid, value, valueIn, version, vin, vout, vsize);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetTransactionV2200Response {\n");
    sb.append("    blockHash: ").append(toIndentedString(blockHash)).append("\n");
    sb.append("    blockHeight: ").append(toIndentedString(blockHeight)).append("\n");
    sb.append("    blockTime: ").append(toIndentedString(blockTime)).append("\n");
    sb.append("    confirmations: ").append(toIndentedString(confirmations)).append("\n");
    sb.append("    fees: ").append(toIndentedString(fees)).append("\n");
    sb.append("    hex: ").append(toIndentedString(hex)).append("\n");
    sb.append("    size: ").append(toIndentedString(size)).append("\n");
    sb.append("    txid: ").append(toIndentedString(txid)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
    sb.append("    valueIn: ").append(toIndentedString(valueIn)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
    sb.append("    vin: ").append(toIndentedString(vin)).append("\n");
    sb.append("    vout: ").append(toIndentedString(vout)).append("\n");
    sb.append("    vsize: ").append(toIndentedString(vsize)).append("\n");
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
    openapiFields.add("blockHash");
    openapiFields.add("blockHeight");
    openapiFields.add("blockTime");
    openapiFields.add("confirmations");
    openapiFields.add("fees");
    openapiFields.add("hex");
    openapiFields.add("size");
    openapiFields.add("txid");
    openapiFields.add("value");
    openapiFields.add("valueIn");
    openapiFields.add("version");
    openapiFields.add("vin");
    openapiFields.add("vout");
    openapiFields.add("vsize");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetTransactionV2200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetTransactionV2200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetTransactionV2200Response is not found in the empty JSON string", GetTransactionV2200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetTransactionV2200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetTransactionV2200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("blockHash") != null && !jsonObj.get("blockHash").isJsonNull()) && !jsonObj.get("blockHash").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `blockHash` to be a primitive type in the JSON string but got `%s`", jsonObj.get("blockHash").toString()));
      }
      if ((jsonObj.get("fees") != null && !jsonObj.get("fees").isJsonNull()) && !jsonObj.get("fees").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fees` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fees").toString()));
      }
      if ((jsonObj.get("hex") != null && !jsonObj.get("hex").isJsonNull()) && !jsonObj.get("hex").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `hex` to be a primitive type in the JSON string but got `%s`", jsonObj.get("hex").toString()));
      }
      if ((jsonObj.get("txid") != null && !jsonObj.get("txid").isJsonNull()) && !jsonObj.get("txid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `txid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("txid").toString()));
      }
      if ((jsonObj.get("value") != null && !jsonObj.get("value").isJsonNull()) && !jsonObj.get("value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("value").toString()));
      }
      if ((jsonObj.get("valueIn") != null && !jsonObj.get("valueIn").isJsonNull()) && !jsonObj.get("valueIn").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `valueIn` to be a primitive type in the JSON string but got `%s`", jsonObj.get("valueIn").toString()));
      }
      if (jsonObj.get("vin") != null && !jsonObj.get("vin").isJsonNull()) {
        JsonArray jsonArrayvin = jsonObj.getAsJsonArray("vin");
        if (jsonArrayvin != null) {
          // ensure the json data is an array
          if (!jsonObj.get("vin").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `vin` to be an array in the JSON string but got `%s`", jsonObj.get("vin").toString()));
          }

          // validate the optional field `vin` (array)
          for (int i = 0; i < jsonArrayvin.size(); i++) {
            GetTransactionV2200ResponseVinInner.validateJsonElement(jsonArrayvin.get(i));
          };
        }
      }
      if (jsonObj.get("vout") != null && !jsonObj.get("vout").isJsonNull()) {
        JsonArray jsonArrayvout = jsonObj.getAsJsonArray("vout");
        if (jsonArrayvout != null) {
          // ensure the json data is an array
          if (!jsonObj.get("vout").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `vout` to be an array in the JSON string but got `%s`", jsonObj.get("vout").toString()));
          }

          // validate the optional field `vout` (array)
          for (int i = 0; i < jsonArrayvout.size(); i++) {
            GetTransactionV2200ResponseVoutInner.validateJsonElement(jsonArrayvout.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetTransactionV2200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetTransactionV2200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetTransactionV2200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetTransactionV2200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<GetTransactionV2200Response>() {
           @Override
           public void write(JsonWriter out, GetTransactionV2200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetTransactionV2200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetTransactionV2200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetTransactionV2200Response
   * @throws IOException if the JSON string is invalid with respect to GetTransactionV2200Response
   */
  public static GetTransactionV2200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetTransactionV2200Response.class);
  }

  /**
   * Convert an instance of GetTransactionV2200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

