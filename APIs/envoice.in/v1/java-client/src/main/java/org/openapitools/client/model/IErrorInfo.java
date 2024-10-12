/*
 * API v1.0.0
 * [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/80638214aa04722c9203)  <span style='margin-left: 0.5em;'>or</span>  <a href='https://documenter.getpostman.com/view/3559821/TVeqcn2L' class='openapi-button' _ngcontent-c6>View Postman docs</a>    # Quickstart    Visit [github](https://github.com/EmitKnowledge/Envoice) to view the quickstart tutorial.    <div class='postman-tutorial'>    # Tutorial for running the API in postman    Click on \"\"Run in Postman\"\" button  <br /><br />  ![postman - tutorial - 1](/Assets/images/api/postman-tutorial/postman-tutorial-1.png)     ---     A new page will open.  Click the \"\"Postman for windows\"\" to run postman as a desktop app.  Make sure you have already [installed](https://www.getpostman.com/docs/postman/launching_postman/installation_and_updates) Postman.  <br /><br />  ![postman - tutorial - 2](/Assets/images/api/postman-tutorial/postman-tutorial-2.png)     ---     In chrome an alert might show up to set a default app for opening postman links. Click on \"\"Open Postman\"\".  <br /><br />  ![postman - tutorial - 3](/Assets/images/api/postman-tutorial/postman-tutorial-3.png)     ---     The OpenAPI specification will be imported in Postman as a new collection named \"\"Envoice api\"\"  <br /><br />  ![postman - tutorial - 4](/Assets/images/api/postman-tutorial/postman-tutorial-4.png)     ---     When testing be sure to check and modify the environment variables to suit your api key and secret. The domain is set to envoice's endpoint so you don't really need to change that.    <sub>\\*Eye button in top right corner </sub>  <br /><br />   ![postman - tutorial - 5](/Assets/images/api/postman-tutorial/postman-tutorial-5.png)  <br /><br />   ![postman - tutorial - 6](/Assets/images/api/postman-tutorial/postman-tutorial-6.png)     ---     You don't need to change the values of the header parameters, because they will be replaced automatically when you send a request with real values from the environment configured in the previous step.  <br /><br />  ![postman - tutorial - 7](/Assets/images/api/postman-tutorial/postman-tutorial-7.png)     ---     Modify the example data to suit your needs and send a request.  <br /><br />  ![postman - tutorial - 8](/Assets/images/api/postman-tutorial/postman-tutorial-8.png)  </div>    # Webhooks    Webhooks allow you to build or set up Envoice Apps which subscribe to invoice activities.   When one of those events is triggered, we'll send a HTTP POST payload to the webhook's configured URL.   Webhooks can be used to update an external invoice data storage.    In order to use webhooks visit [this link](/account/settings#api-tab) and add upto 10 webhook urls that will return status `200` in order to signal that the webhook is working.  All nonworking webhooks will be ignored after a certain period of time and several retry attempts.  If after several attempts the webhook starts to work, we will send you all activities, both past and present, in chronological order.    The payload of the webhook is in format:  ```  {      Signature: \"\"sha256 string\"\",      Timestamp: \"\"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"\",      Activity: {          Message: \"string\",          Link: \"share url\",          Type: int,                  InvoiceNumber: \"string\",          InvoiceId: int,                  OrderNumber: \"string\",          OrderId: int,          Id: int,          CreatedOn: \"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"      }  }  ```            
 *
 * The version of the OpenAPI document: v1
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
 * IErrorInfo
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:00.947845-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IErrorInfo {
  public static final String SERIALIZED_NAME_CODE = "Code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_FAULT_MESSAGE = "FaultMessage";
  @SerializedName(SERIALIZED_NAME_FAULT_MESSAGE)
  private String faultMessage;

  public static final String SERIALIZED_NAME_GROUP = "Group";
  @SerializedName(SERIALIZED_NAME_GROUP)
  private String group;

  public static final String SERIALIZED_NAME_USER_VISIBLE_MESSAGE = "UserVisibleMessage";
  @SerializedName(SERIALIZED_NAME_USER_VISIBLE_MESSAGE)
  private String userVisibleMessage;

  public IErrorInfo() {
  }

  public IErrorInfo(
     String code, 
     String faultMessage, 
     String group, 
     String userVisibleMessage
  ) {
    this();
    this.code = code;
    this.faultMessage = faultMessage;
    this.group = group;
    this.userVisibleMessage = userVisibleMessage;
  }

  /**
   * Get code
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }



  /**
   * Get faultMessage
   * @return faultMessage
   */
  @javax.annotation.Nullable
  public String getFaultMessage() {
    return faultMessage;
  }



  /**
   * Get group
   * @return group
   */
  @javax.annotation.Nullable
  public String getGroup() {
    return group;
  }



  /**
   * Get userVisibleMessage
   * @return userVisibleMessage
   */
  @javax.annotation.Nullable
  public String getUserVisibleMessage() {
    return userVisibleMessage;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IErrorInfo ierrorInfo = (IErrorInfo) o;
    return Objects.equals(this.code, ierrorInfo.code) &&
        Objects.equals(this.faultMessage, ierrorInfo.faultMessage) &&
        Objects.equals(this.group, ierrorInfo.group) &&
        Objects.equals(this.userVisibleMessage, ierrorInfo.userVisibleMessage);
  }

  @Override
  public int hashCode() {
    return Objects.hash(code, faultMessage, group, userVisibleMessage);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IErrorInfo {\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    faultMessage: ").append(toIndentedString(faultMessage)).append("\n");
    sb.append("    group: ").append(toIndentedString(group)).append("\n");
    sb.append("    userVisibleMessage: ").append(toIndentedString(userVisibleMessage)).append("\n");
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
    openapiFields.add("Code");
    openapiFields.add("FaultMessage");
    openapiFields.add("Group");
    openapiFields.add("UserVisibleMessage");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IErrorInfo
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IErrorInfo.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IErrorInfo is not found in the empty JSON string", IErrorInfo.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IErrorInfo.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IErrorInfo` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Code") != null && !jsonObj.get("Code").isJsonNull()) && !jsonObj.get("Code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Code").toString()));
      }
      if ((jsonObj.get("FaultMessage") != null && !jsonObj.get("FaultMessage").isJsonNull()) && !jsonObj.get("FaultMessage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `FaultMessage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("FaultMessage").toString()));
      }
      if ((jsonObj.get("Group") != null && !jsonObj.get("Group").isJsonNull()) && !jsonObj.get("Group").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Group` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Group").toString()));
      }
      if ((jsonObj.get("UserVisibleMessage") != null && !jsonObj.get("UserVisibleMessage").isJsonNull()) && !jsonObj.get("UserVisibleMessage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `UserVisibleMessage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("UserVisibleMessage").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IErrorInfo.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IErrorInfo' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IErrorInfo> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IErrorInfo.class));

       return (TypeAdapter<T>) new TypeAdapter<IErrorInfo>() {
           @Override
           public void write(JsonWriter out, IErrorInfo value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IErrorInfo read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IErrorInfo given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IErrorInfo
   * @throws IOException if the JSON string is invalid with respect to IErrorInfo
   */
  public static IErrorInfo fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IErrorInfo.class);
  }

  /**
   * Convert an instance of IErrorInfo to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

