/*
 * nextAuth API
 * API for the nextAuth server
 *
 * The version of the OpenAPI document: 2.2
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
 * Server
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:02.089808-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Server {
  public static final String SERIALIZED_NAME_ACCOUNT_COUNT = "accountCount";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_COUNT)
  private Integer accountCount;

  public static final String SERIALIZED_NAME_APPANDROID = "appandroid";
  @SerializedName(SERIALIZED_NAME_APPANDROID)
  private String appandroid;

  public static final String SERIALIZED_NAME_APPIOS = "appios";
  @SerializedName(SERIALIZED_NAME_APPIOS)
  private String appios;

  public static final String SERIALIZED_NAME_APPNAME = "appname";
  @SerializedName(SERIALIZED_NAME_APPNAME)
  private String appname;

  public static final String SERIALIZED_NAME_APPURL = "appurl";
  @SerializedName(SERIALIZED_NAME_APPURL)
  private String appurl;

  public static final String SERIALIZED_NAME_LAST_LOGIN = "lastLogin";
  @SerializedName(SERIALIZED_NAME_LAST_LOGIN)
  private Long lastLogin;

  public static final String SERIALIZED_NAME_LOGO = "logo";
  @SerializedName(SERIALIZED_NAME_LOGO)
  private String logo;

  public static final String SERIALIZED_NAME_OWNER = "owner";
  @SerializedName(SERIALIZED_NAME_OWNER)
  private Integer owner;

  public static final String SERIALIZED_NAME_PIN_TIMEOUT = "pinTimeout";
  @SerializedName(SERIALIZED_NAME_PIN_TIMEOUT)
  private Integer pinTimeout;

  public static final String SERIALIZED_NAME_PIN_TRANS_TIMEOUT = "pinTransTimeout";
  @SerializedName(SERIALIZED_NAME_PIN_TRANS_TIMEOUT)
  private Integer pinTransTimeout;

  public static final String SERIALIZED_NAME_PING_TIME = "pingTime";
  @SerializedName(SERIALIZED_NAME_PING_TIME)
  private Integer pingTime;

  public static final String SERIALIZED_NAME_SERVER_FLAGS = "serverFlags";
  @SerializedName(SERIALIZED_NAME_SERVER_FLAGS)
  private List<String> serverFlags = new ArrayList<>();

  public static final String SERIALIZED_NAME_SERVER_NAME = "serverName";
  @SerializedName(SERIALIZED_NAME_SERVER_NAME)
  private String serverName;

  public static final String SERIALIZED_NAME_SERVERID = "serverid";
  @SerializedName(SERIALIZED_NAME_SERVERID)
  private String serverid;

  public static final String SERIALIZED_NAME_SERVERPK = "serverpk";
  @SerializedName(SERIALIZED_NAME_SERVERPK)
  private String serverpk;

  public static final String SERIALIZED_NAME_SITEURL = "siteurl";
  @SerializedName(SERIALIZED_NAME_SITEURL)
  private String siteurl;

  public static final String SERIALIZED_NAME_WSURL = "wsurl";
  @SerializedName(SERIALIZED_NAME_WSURL)
  private String wsurl;

  public Server() {
  }

  public Server accountCount(Integer accountCount) {
    this.accountCount = accountCount;
    return this;
  }

  /**
   * Number of accounts registered with this server
   * @return accountCount
   */
  @javax.annotation.Nullable
  public Integer getAccountCount() {
    return accountCount;
  }

  public void setAccountCount(Integer accountCount) {
    this.accountCount = accountCount;
  }


  public Server appandroid(String appandroid) {
    this.appandroid = appandroid;
    return this;
  }

  /**
   * URL of the app in Google Play
   * @return appandroid
   */
  @javax.annotation.Nullable
  public String getAppandroid() {
    return appandroid;
  }

  public void setAppandroid(String appandroid) {
    this.appandroid = appandroid;
  }


  public Server appios(String appios) {
    this.appios = appios;
    return this;
  }

  /**
   * URL of the app in the App Store
   * @return appios
   */
  @javax.annotation.Nullable
  public String getAppios() {
    return appios;
  }

  public void setAppios(String appios) {
    this.appios = appios;
  }


  public Server appname(String appname) {
    this.appname = appname;
    return this;
  }

  /**
   * name of the app
   * @return appname
   */
  @javax.annotation.Nullable
  public String getAppname() {
    return appname;
  }

  public void setAppname(String appname) {
    this.appname = appname;
  }


  public Server appurl(String appurl) {
    this.appurl = appurl;
    return this;
  }

  /**
   * URL (prefix) to launch the app
   * @return appurl
   */
  @javax.annotation.Nullable
  public String getAppurl() {
    return appurl;
  }

  public void setAppurl(String appurl) {
    this.appurl = appurl;
  }


  public Server lastLogin(Long lastLogin) {
    this.lastLogin = lastLogin;
    return this;
  }

  /**
   * Last login on this server
   * @return lastLogin
   */
  @javax.annotation.Nullable
  public Long getLastLogin() {
    return lastLogin;
  }

  public void setLastLogin(Long lastLogin) {
    this.lastLogin = lastLogin;
  }


  public Server logo(String logo) {
    this.logo = logo;
    return this;
  }

  /**
   * Base 64 encoded logo
   * @return logo
   */
  @javax.annotation.Nonnull
  public String getLogo() {
    return logo;
  }

  public void setLogo(String logo) {
    this.logo = logo;
  }


  public Server owner(Integer owner) {
    this.owner = owner;
    return this;
  }

  /**
   * Owner id
   * @return owner
   */
  @javax.annotation.Nullable
  public Integer getOwner() {
    return owner;
  }

  public void setOwner(Integer owner) {
    this.owner = owner;
  }


  public Server pinTimeout(Integer pinTimeout) {
    this.pinTimeout = pinTimeout;
    return this;
  }

  /**
   * Time (minutes) since the last time the user entered his PIN, that the user is not requested a PIN at login. -1 means that the user is never asked for a PIN before logging in, 0 means that the user is asked every time he wants to login
   * @return pinTimeout
   */
  @javax.annotation.Nonnull
  public Integer getPinTimeout() {
    return pinTimeout;
  }

  public void setPinTimeout(Integer pinTimeout) {
    this.pinTimeout = pinTimeout;
  }


  public Server pinTransTimeout(Integer pinTransTimeout) {
    this.pinTransTimeout = pinTransTimeout;
    return this;
  }

  /**
   * Time (minutes) since the last time the user entered his PIN, that the user is not requested a PIN at transaction approval. -1 means that the user is never asked for a PIN before approving a transaction, 0 means that the user is asked every time he wants to approve a transaction
   * @return pinTransTimeout
   */
  @javax.annotation.Nonnull
  public Integer getPinTransTimeout() {
    return pinTransTimeout;
  }

  public void setPinTransTimeout(Integer pinTransTimeout) {
    this.pinTransTimeout = pinTransTimeout;
  }


  public Server pingTime(Integer pingTime) {
    this.pingTime = pingTime;
    return this;
  }

  /**
   * Time (seconds) that the nextAuth app has before it needs to reply to a ping request from the nextAuth server (continuous authentication)
   * @return pingTime
   */
  @javax.annotation.Nonnull
  public Integer getPingTime() {
    return pingTime;
  }

  public void setPingTime(Integer pingTime) {
    this.pingTime = pingTime;
  }


  public Server serverFlags(List<String> serverFlags) {
    this.serverFlags = serverFlags;
    return this;
  }

  public Server addServerFlagsItem(String serverFlagsItem) {
    if (this.serverFlags == null) {
      this.serverFlags = new ArrayList<>();
    }
    this.serverFlags.add(serverFlagsItem);
    return this;
  }

  /**
   * Server flags
   * @return serverFlags
   */
  @javax.annotation.Nonnull
  public List<String> getServerFlags() {
    return serverFlags;
  }

  public void setServerFlags(List<String> serverFlags) {
    this.serverFlags = serverFlags;
  }


  public Server serverName(String serverName) {
    this.serverName = serverName;
    return this;
  }

  /**
   * Server name
   * @return serverName
   */
  @javax.annotation.Nonnull
  public String getServerName() {
    return serverName;
  }

  public void setServerName(String serverName) {
    this.serverName = serverName;
  }


  public Server serverid(String serverid) {
    this.serverid = serverid;
    return this;
  }

  /**
   * Base64 encoded id of the nextAuth server
   * @return serverid
   */
  @javax.annotation.Nonnull
  public String getServerid() {
    return serverid;
  }

  public void setServerid(String serverid) {
    this.serverid = serverid;
  }


  public Server serverpk(String serverpk) {
    this.serverpk = serverpk;
    return this;
  }

  /**
   * Base64 encoded public key of the nextAuth server
   * @return serverpk
   */
  @javax.annotation.Nonnull
  public String getServerpk() {
    return serverpk;
  }

  public void setServerpk(String serverpk) {
    this.serverpk = serverpk;
  }


  public Server siteurl(String siteurl) {
    this.siteurl = siteurl;
    return this;
  }

  /**
   * URL of the main website
   * @return siteurl
   */
  @javax.annotation.Nullable
  public String getSiteurl() {
    return siteurl;
  }

  public void setSiteurl(String siteurl) {
    this.siteurl = siteurl;
  }


  public Server wsurl(String wsurl) {
    this.wsurl = wsurl;
    return this;
  }

  /**
   * Websocket URL
   * @return wsurl
   */
  @javax.annotation.Nullable
  public String getWsurl() {
    return wsurl;
  }

  public void setWsurl(String wsurl) {
    this.wsurl = wsurl;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Server server = (Server) o;
    return Objects.equals(this.accountCount, server.accountCount) &&
        Objects.equals(this.appandroid, server.appandroid) &&
        Objects.equals(this.appios, server.appios) &&
        Objects.equals(this.appname, server.appname) &&
        Objects.equals(this.appurl, server.appurl) &&
        Objects.equals(this.lastLogin, server.lastLogin) &&
        Objects.equals(this.logo, server.logo) &&
        Objects.equals(this.owner, server.owner) &&
        Objects.equals(this.pinTimeout, server.pinTimeout) &&
        Objects.equals(this.pinTransTimeout, server.pinTransTimeout) &&
        Objects.equals(this.pingTime, server.pingTime) &&
        Objects.equals(this.serverFlags, server.serverFlags) &&
        Objects.equals(this.serverName, server.serverName) &&
        Objects.equals(this.serverid, server.serverid) &&
        Objects.equals(this.serverpk, server.serverpk) &&
        Objects.equals(this.siteurl, server.siteurl) &&
        Objects.equals(this.wsurl, server.wsurl);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountCount, appandroid, appios, appname, appurl, lastLogin, logo, owner, pinTimeout, pinTransTimeout, pingTime, serverFlags, serverName, serverid, serverpk, siteurl, wsurl);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Server {\n");
    sb.append("    accountCount: ").append(toIndentedString(accountCount)).append("\n");
    sb.append("    appandroid: ").append(toIndentedString(appandroid)).append("\n");
    sb.append("    appios: ").append(toIndentedString(appios)).append("\n");
    sb.append("    appname: ").append(toIndentedString(appname)).append("\n");
    sb.append("    appurl: ").append(toIndentedString(appurl)).append("\n");
    sb.append("    lastLogin: ").append(toIndentedString(lastLogin)).append("\n");
    sb.append("    logo: ").append(toIndentedString(logo)).append("\n");
    sb.append("    owner: ").append(toIndentedString(owner)).append("\n");
    sb.append("    pinTimeout: ").append(toIndentedString(pinTimeout)).append("\n");
    sb.append("    pinTransTimeout: ").append(toIndentedString(pinTransTimeout)).append("\n");
    sb.append("    pingTime: ").append(toIndentedString(pingTime)).append("\n");
    sb.append("    serverFlags: ").append(toIndentedString(serverFlags)).append("\n");
    sb.append("    serverName: ").append(toIndentedString(serverName)).append("\n");
    sb.append("    serverid: ").append(toIndentedString(serverid)).append("\n");
    sb.append("    serverpk: ").append(toIndentedString(serverpk)).append("\n");
    sb.append("    siteurl: ").append(toIndentedString(siteurl)).append("\n");
    sb.append("    wsurl: ").append(toIndentedString(wsurl)).append("\n");
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
    openapiFields.add("accountCount");
    openapiFields.add("appandroid");
    openapiFields.add("appios");
    openapiFields.add("appname");
    openapiFields.add("appurl");
    openapiFields.add("lastLogin");
    openapiFields.add("logo");
    openapiFields.add("owner");
    openapiFields.add("pinTimeout");
    openapiFields.add("pinTransTimeout");
    openapiFields.add("pingTime");
    openapiFields.add("serverFlags");
    openapiFields.add("serverName");
    openapiFields.add("serverid");
    openapiFields.add("serverpk");
    openapiFields.add("siteurl");
    openapiFields.add("wsurl");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("logo");
    openapiRequiredFields.add("pinTimeout");
    openapiRequiredFields.add("pinTransTimeout");
    openapiRequiredFields.add("pingTime");
    openapiRequiredFields.add("serverFlags");
    openapiRequiredFields.add("serverName");
    openapiRequiredFields.add("serverid");
    openapiRequiredFields.add("serverpk");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Server
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Server.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Server is not found in the empty JSON string", Server.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Server.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Server` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Server.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("appandroid") != null && !jsonObj.get("appandroid").isJsonNull()) && !jsonObj.get("appandroid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appandroid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appandroid").toString()));
      }
      if ((jsonObj.get("appios") != null && !jsonObj.get("appios").isJsonNull()) && !jsonObj.get("appios").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appios` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appios").toString()));
      }
      if ((jsonObj.get("appname") != null && !jsonObj.get("appname").isJsonNull()) && !jsonObj.get("appname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appname").toString()));
      }
      if ((jsonObj.get("appurl") != null && !jsonObj.get("appurl").isJsonNull()) && !jsonObj.get("appurl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appurl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appurl").toString()));
      }
      if (!jsonObj.get("logo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `logo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("logo").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("serverFlags") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("serverFlags").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `serverFlags` to be an array in the JSON string but got `%s`", jsonObj.get("serverFlags").toString()));
      }
      if (!jsonObj.get("serverName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `serverName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("serverName").toString()));
      }
      if (!jsonObj.get("serverid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `serverid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("serverid").toString()));
      }
      if (!jsonObj.get("serverpk").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `serverpk` to be a primitive type in the JSON string but got `%s`", jsonObj.get("serverpk").toString()));
      }
      if ((jsonObj.get("siteurl") != null && !jsonObj.get("siteurl").isJsonNull()) && !jsonObj.get("siteurl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `siteurl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("siteurl").toString()));
      }
      if ((jsonObj.get("wsurl") != null && !jsonObj.get("wsurl").isJsonNull()) && !jsonObj.get("wsurl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `wsurl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("wsurl").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Server.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Server' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Server> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Server.class));

       return (TypeAdapter<T>) new TypeAdapter<Server>() {
           @Override
           public void write(JsonWriter out, Server value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Server read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Server given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Server
   * @throws IOException if the JSON string is invalid with respect to Server
   */
  public static Server fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Server.class);
  }

  /**
   * Convert an instance of Server to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

