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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.IErrorInfo;
import org.openapitools.client.model.PaymentLink;

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
 * ListResultPaymentLink
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:00.947845-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ListResultPaymentLink {
  public static final String SERIALIZED_NAME_COUNT = "Count";
  @SerializedName(SERIALIZED_NAME_COUNT)
  private Integer count;

  public static final String SERIALIZED_NAME_ERROR_MESSAGES = "ErrorMessages";
  @SerializedName(SERIALIZED_NAME_ERROR_MESSAGES)
  private List<IErrorInfo> errorMessages = new ArrayList<>();

  public static final String SERIALIZED_NAME_IS_FAULTED = "IsFaulted";
  @SerializedName(SERIALIZED_NAME_IS_FAULTED)
  private Boolean isFaulted;

  public static final String SERIALIZED_NAME_RESULT = "Result";
  @SerializedName(SERIALIZED_NAME_RESULT)
  private List<PaymentLink> result = new ArrayList<>();

  public static final String SERIALIZED_NAME_TOTAL_COUNT = "TotalCount";
  @SerializedName(SERIALIZED_NAME_TOTAL_COUNT)
  private Integer totalCount;

  public ListResultPaymentLink() {
  }

  public ListResultPaymentLink(
     Integer count
  ) {
    this();
    this.count = count;
  }

  /**
   * Get count
   * @return count
   */
  @javax.annotation.Nullable
  public Integer getCount() {
    return count;
  }



  public ListResultPaymentLink errorMessages(List<IErrorInfo> errorMessages) {
    this.errorMessages = errorMessages;
    return this;
  }

  public ListResultPaymentLink addErrorMessagesItem(IErrorInfo errorMessagesItem) {
    if (this.errorMessages == null) {
      this.errorMessages = new ArrayList<>();
    }
    this.errorMessages.add(errorMessagesItem);
    return this;
  }

  /**
   * Get errorMessages
   * @return errorMessages
   */
  @javax.annotation.Nullable
  public List<IErrorInfo> getErrorMessages() {
    return errorMessages;
  }

  public void setErrorMessages(List<IErrorInfo> errorMessages) {
    this.errorMessages = errorMessages;
  }


  public ListResultPaymentLink isFaulted(Boolean isFaulted) {
    this.isFaulted = isFaulted;
    return this;
  }

  /**
   * Get isFaulted
   * @return isFaulted
   */
  @javax.annotation.Nullable
  public Boolean getIsFaulted() {
    return isFaulted;
  }

  public void setIsFaulted(Boolean isFaulted) {
    this.isFaulted = isFaulted;
  }


  public ListResultPaymentLink result(List<PaymentLink> result) {
    this.result = result;
    return this;
  }

  public ListResultPaymentLink addResultItem(PaymentLink resultItem) {
    if (this.result == null) {
      this.result = new ArrayList<>();
    }
    this.result.add(resultItem);
    return this;
  }

  /**
   * Get result
   * @return result
   */
  @javax.annotation.Nullable
  public List<PaymentLink> getResult() {
    return result;
  }

  public void setResult(List<PaymentLink> result) {
    this.result = result;
  }


  public ListResultPaymentLink totalCount(Integer totalCount) {
    this.totalCount = totalCount;
    return this;
  }

  /**
   * Get totalCount
   * @return totalCount
   */
  @javax.annotation.Nullable
  public Integer getTotalCount() {
    return totalCount;
  }

  public void setTotalCount(Integer totalCount) {
    this.totalCount = totalCount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ListResultPaymentLink listResultPaymentLink = (ListResultPaymentLink) o;
    return Objects.equals(this.count, listResultPaymentLink.count) &&
        Objects.equals(this.errorMessages, listResultPaymentLink.errorMessages) &&
        Objects.equals(this.isFaulted, listResultPaymentLink.isFaulted) &&
        Objects.equals(this.result, listResultPaymentLink.result) &&
        Objects.equals(this.totalCount, listResultPaymentLink.totalCount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(count, errorMessages, isFaulted, result, totalCount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ListResultPaymentLink {\n");
    sb.append("    count: ").append(toIndentedString(count)).append("\n");
    sb.append("    errorMessages: ").append(toIndentedString(errorMessages)).append("\n");
    sb.append("    isFaulted: ").append(toIndentedString(isFaulted)).append("\n");
    sb.append("    result: ").append(toIndentedString(result)).append("\n");
    sb.append("    totalCount: ").append(toIndentedString(totalCount)).append("\n");
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
    openapiFields.add("Count");
    openapiFields.add("ErrorMessages");
    openapiFields.add("IsFaulted");
    openapiFields.add("Result");
    openapiFields.add("TotalCount");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ListResultPaymentLink
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ListResultPaymentLink.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ListResultPaymentLink is not found in the empty JSON string", ListResultPaymentLink.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ListResultPaymentLink.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ListResultPaymentLink` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("ErrorMessages") != null && !jsonObj.get("ErrorMessages").isJsonNull()) {
        JsonArray jsonArrayerrorMessages = jsonObj.getAsJsonArray("ErrorMessages");
        if (jsonArrayerrorMessages != null) {
          // ensure the json data is an array
          if (!jsonObj.get("ErrorMessages").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `ErrorMessages` to be an array in the JSON string but got `%s`", jsonObj.get("ErrorMessages").toString()));
          }

          // validate the optional field `ErrorMessages` (array)
          for (int i = 0; i < jsonArrayerrorMessages.size(); i++) {
            IErrorInfo.validateJsonElement(jsonArrayerrorMessages.get(i));
          };
        }
      }
      if (jsonObj.get("Result") != null && !jsonObj.get("Result").isJsonNull()) {
        JsonArray jsonArrayresult = jsonObj.getAsJsonArray("Result");
        if (jsonArrayresult != null) {
          // ensure the json data is an array
          if (!jsonObj.get("Result").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `Result` to be an array in the JSON string but got `%s`", jsonObj.get("Result").toString()));
          }

          // validate the optional field `Result` (array)
          for (int i = 0; i < jsonArrayresult.size(); i++) {
            PaymentLink.validateJsonElement(jsonArrayresult.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ListResultPaymentLink.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ListResultPaymentLink' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ListResultPaymentLink> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ListResultPaymentLink.class));

       return (TypeAdapter<T>) new TypeAdapter<ListResultPaymentLink>() {
           @Override
           public void write(JsonWriter out, ListResultPaymentLink value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ListResultPaymentLink read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ListResultPaymentLink given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ListResultPaymentLink
   * @throws IOException if the JSON string is invalid with respect to ListResultPaymentLink
   */
  public static ListResultPaymentLink fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ListResultPaymentLink.class);
  }

  /**
   * Convert an instance of ListResultPaymentLink to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

