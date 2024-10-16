/*
 * Neblio REST API Suite
 * APIs for Interacting with NTP1 Tokens & The Neblio Blockchain
 *
 * The version of the OpenAPI document: 1.3.0
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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.GetAddressInfoResponseUtxosInnerTokensInner;

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
 * GetAddressInfoResponseUtxosInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:38.969239-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetAddressInfoResponseUtxosInner {
  public static final String SERIALIZED_NAME_BLOCKHEIGHT = "blockheight";
  @SerializedName(SERIALIZED_NAME_BLOCKHEIGHT)
  private BigDecimal blockheight;

  public static final String SERIALIZED_NAME_BLOCKTIME = "blocktime";
  @SerializedName(SERIALIZED_NAME_BLOCKTIME)
  private BigDecimal blocktime;

  public static final String SERIALIZED_NAME_INDEX = "index";
  @SerializedName(SERIALIZED_NAME_INDEX)
  private BigDecimal index;

  public static final String SERIALIZED_NAME_SCRIPT_PUB_KEY = "scriptPubKey";
  @SerializedName(SERIALIZED_NAME_SCRIPT_PUB_KEY)
  private Object scriptPubKey;

  public static final String SERIALIZED_NAME_TOKENS = "tokens";
  @SerializedName(SERIALIZED_NAME_TOKENS)
  private List<GetAddressInfoResponseUtxosInnerTokensInner> tokens = new ArrayList<>();

  public static final String SERIALIZED_NAME_TXID = "txid";
  @SerializedName(SERIALIZED_NAME_TXID)
  private String txid;

  public static final String SERIALIZED_NAME_USED = "used";
  @SerializedName(SERIALIZED_NAME_USED)
  private Boolean used;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private BigDecimal value;

  public GetAddressInfoResponseUtxosInner() {
  }

  public GetAddressInfoResponseUtxosInner blockheight(BigDecimal blockheight) {
    this.blockheight = blockheight;
    return this;
  }

  /**
   * Blockheight of the UTXO
   * @return blockheight
   */
  @javax.annotation.Nullable
  public BigDecimal getBlockheight() {
    return blockheight;
  }

  public void setBlockheight(BigDecimal blockheight) {
    this.blockheight = blockheight;
  }


  public GetAddressInfoResponseUtxosInner blocktime(BigDecimal blocktime) {
    this.blocktime = blocktime;
    return this;
  }

  /**
   * Blocktime of the UTXO
   * @return blocktime
   */
  @javax.annotation.Nullable
  public BigDecimal getBlocktime() {
    return blocktime;
  }

  public void setBlocktime(BigDecimal blocktime) {
    this.blocktime = blocktime;
  }


  public GetAddressInfoResponseUtxosInner index(BigDecimal index) {
    this.index = index;
    return this;
  }

  /**
   * Index of the UTXO at this address
   * @return index
   */
  @javax.annotation.Nullable
  public BigDecimal getIndex() {
    return index;
  }

  public void setIndex(BigDecimal index) {
    this.index = index;
  }


  public GetAddressInfoResponseUtxosInner scriptPubKey(Object scriptPubKey) {
    this.scriptPubKey = scriptPubKey;
    return this;
  }

  /**
   * Object representing the scruptPubKey of the UTXO
   * @return scriptPubKey
   */
  @javax.annotation.Nullable
  public Object getScriptPubKey() {
    return scriptPubKey;
  }

  public void setScriptPubKey(Object scriptPubKey) {
    this.scriptPubKey = scriptPubKey;
  }


  public GetAddressInfoResponseUtxosInner tokens(List<GetAddressInfoResponseUtxosInnerTokensInner> tokens) {
    this.tokens = tokens;
    return this;
  }

  public GetAddressInfoResponseUtxosInner addTokensItem(GetAddressInfoResponseUtxosInnerTokensInner tokensItem) {
    if (this.tokens == null) {
      this.tokens = new ArrayList<>();
    }
    this.tokens.add(tokensItem);
    return this;
  }

  /**
   * Array of NTP1 tokens in this UTXO.
   * @return tokens
   */
  @javax.annotation.Nullable
  public List<GetAddressInfoResponseUtxosInnerTokensInner> getTokens() {
    return tokens;
  }

  public void setTokens(List<GetAddressInfoResponseUtxosInnerTokensInner> tokens) {
    this.tokens = tokens;
  }


  public GetAddressInfoResponseUtxosInner txid(String txid) {
    this.txid = txid;
    return this;
  }

  /**
   * Txid of this UTXO
   * @return txid
   */
  @javax.annotation.Nullable
  public String getTxid() {
    return txid;
  }

  public void setTxid(String txid) {
    this.txid = txid;
  }


  public GetAddressInfoResponseUtxosInner used(Boolean used) {
    this.used = used;
    return this;
  }

  /**
   * Whether the UTXO has been used
   * @return used
   */
  @javax.annotation.Nullable
  public Boolean getUsed() {
    return used;
  }

  public void setUsed(Boolean used) {
    this.used = used;
  }


  public GetAddressInfoResponseUtxosInner value(BigDecimal value) {
    this.value = value;
    return this;
  }

  /**
   * Value of the UTXO in NEBL satoshi
   * @return value
   */
  @javax.annotation.Nullable
  public BigDecimal getValue() {
    return value;
  }

  public void setValue(BigDecimal value) {
    this.value = value;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetAddressInfoResponseUtxosInner getAddressInfoResponseUtxosInner = (GetAddressInfoResponseUtxosInner) o;
    return Objects.equals(this.blockheight, getAddressInfoResponseUtxosInner.blockheight) &&
        Objects.equals(this.blocktime, getAddressInfoResponseUtxosInner.blocktime) &&
        Objects.equals(this.index, getAddressInfoResponseUtxosInner.index) &&
        Objects.equals(this.scriptPubKey, getAddressInfoResponseUtxosInner.scriptPubKey) &&
        Objects.equals(this.tokens, getAddressInfoResponseUtxosInner.tokens) &&
        Objects.equals(this.txid, getAddressInfoResponseUtxosInner.txid) &&
        Objects.equals(this.used, getAddressInfoResponseUtxosInner.used) &&
        Objects.equals(this.value, getAddressInfoResponseUtxosInner.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(blockheight, blocktime, index, scriptPubKey, tokens, txid, used, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetAddressInfoResponseUtxosInner {\n");
    sb.append("    blockheight: ").append(toIndentedString(blockheight)).append("\n");
    sb.append("    blocktime: ").append(toIndentedString(blocktime)).append("\n");
    sb.append("    index: ").append(toIndentedString(index)).append("\n");
    sb.append("    scriptPubKey: ").append(toIndentedString(scriptPubKey)).append("\n");
    sb.append("    tokens: ").append(toIndentedString(tokens)).append("\n");
    sb.append("    txid: ").append(toIndentedString(txid)).append("\n");
    sb.append("    used: ").append(toIndentedString(used)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
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
    openapiFields.add("blockheight");
    openapiFields.add("blocktime");
    openapiFields.add("index");
    openapiFields.add("scriptPubKey");
    openapiFields.add("tokens");
    openapiFields.add("txid");
    openapiFields.add("used");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetAddressInfoResponseUtxosInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetAddressInfoResponseUtxosInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetAddressInfoResponseUtxosInner is not found in the empty JSON string", GetAddressInfoResponseUtxosInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetAddressInfoResponseUtxosInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetAddressInfoResponseUtxosInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("tokens") != null && !jsonObj.get("tokens").isJsonNull()) {
        JsonArray jsonArraytokens = jsonObj.getAsJsonArray("tokens");
        if (jsonArraytokens != null) {
          // ensure the json data is an array
          if (!jsonObj.get("tokens").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `tokens` to be an array in the JSON string but got `%s`", jsonObj.get("tokens").toString()));
          }

          // validate the optional field `tokens` (array)
          for (int i = 0; i < jsonArraytokens.size(); i++) {
            GetAddressInfoResponseUtxosInnerTokensInner.validateJsonElement(jsonArraytokens.get(i));
          };
        }
      }
      if ((jsonObj.get("txid") != null && !jsonObj.get("txid").isJsonNull()) && !jsonObj.get("txid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `txid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("txid").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetAddressInfoResponseUtxosInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetAddressInfoResponseUtxosInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetAddressInfoResponseUtxosInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetAddressInfoResponseUtxosInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetAddressInfoResponseUtxosInner>() {
           @Override
           public void write(JsonWriter out, GetAddressInfoResponseUtxosInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetAddressInfoResponseUtxosInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetAddressInfoResponseUtxosInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetAddressInfoResponseUtxosInner
   * @throws IOException if the JSON string is invalid with respect to GetAddressInfoResponseUtxosInner
   */
  public static GetAddressInfoResponseUtxosInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetAddressInfoResponseUtxosInner.class);
  }

  /**
   * Convert an instance of GetAddressInfoResponseUtxosInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

