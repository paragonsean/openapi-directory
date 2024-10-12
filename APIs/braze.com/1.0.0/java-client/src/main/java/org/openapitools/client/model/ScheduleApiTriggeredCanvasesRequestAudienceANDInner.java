/*
 * Braze Endpoints
 * # Braze API Overview  Braze provides a high performance REST API to allow you to track users, send messages, export data, and more.  A REST API is a way to programmatically transfer information over the web using a predefined schema. Braze has created many different endpoints with specific requirements that will perform various actions and/or return various data. API access is done using HTTPS web requests to your company's REST API endpoint (this will correspond to your Dashboard URL as shown in the table below).  Customers using Braze's EU database should use `https://rest.fra-01.braze.eu/`. For more information on REST API endpoints for customers using Braze's EU database see our [EU/US Implementation Differences documentation](https://www.braze.com/docs/developer_guide/eu01_us3_sdk_implementation_differences/overview/).  ## Braze Instances  Instance    | Dashboard URL   | REST Endpoint ----------- |---------------- | -------------------- US-01 | `https://dashboard.braze.com` or<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` US-02 | `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` US-03 | `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` US-04 | `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` US-06 | `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` EU-01 | `https://dashboard.braze.eu` or<br> `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu`   # Using Braze's Postman Collection   If you have a Postman account (MacOS, Windows, and Linux versions can be downloaded from their website located [here](https://www.getpostman.com)), you can go to our Postman documentation and click the orange `Run in Postman` button in the top, right corner. This will allow you to [create an environment](#setting-up-your-postman-environment), as well as edit the available `POST` and `GET` requests to suit your own needs.  ## Setting Up Your Postman Environment  The Braze Postman Collection uses a templating variable, `{{instance_url}}`, to substitute the REST API URL of your Braze instance into the pre-built requests. Rather than having to manually edit all requests in the Collection, you can set up this variable in your Postman environment. To do so, please follow the steps below:  1. Click on the gear icon in the top right corner of the Postman app.  2. Select \"Manage Environments\" to open a modal window which displays your active environments. 3. In the bottom right corner of the modal window, click \"Add\" to create a new environment. 4. Give this environment a name (e.g. \"Braze API Requests\") and add keys for `instance_url` and `api_key` with values corresponding to [your Braze instance](https://www.braze.com/docs/api/basics/#endpoints) and [Braze REST API Key](https://www.braze.com/docs/api/basics/#app-group-rest-api-keys), as pictured below.   As of April, 2020 Braze has changed how we read App Group API keys. Instead of passing them in the request body or through url parameters, we now read the App Group Rest`api_key` through the HTTP Authorization header. API keys not passed through the HTTP Authorization Header will coninue to work until they have been sunset.   ## Using the Pre-Built Requests from the Collection  Once you have configured your environment. You can use any of the pre-built requests in the collection as a template for building new API requests. To start using one of the pre-built requests, simply click on it within the 'Collections' menu on the left side of Postman. This will open the request as a new tab in the main window of the Postman app.  In general, there are two types of requests that Braze's API endpoints accept - `GET` and `POST`. Depending on which `HTTP` method the endpoint uses, you'll need to edit the pre-built request differently.  ### Edit a POST Request  When editing a `POST` request, you'll need to open the request and navigate to the `Body` section in the request editor. For readability, select the `raw` radio button to format the `JSON` request body.  ### Edit a GET Request  When editing a `GET` request, you will need to edit the parameters passed in the request URL. To edit these easily, select the `Params` button next to the URL bar and edit the key-value pairs in the fields that will appear below the URL bar.  ## Send Your Request  Once your API request is ready to send, click on the 'Send' button next to the URL bar. The request will be sent and the response data will be populated in a section underneath the request editor. From here, you can view the raw data returned from Braze's API, see the HTTP response code, see how long the request took to process, and view header information.
 *
 * The version of the OpenAPI document: 1.0.0
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
import org.openapitools.client.model.ScheduleApiTriggeredCanvasesRequestAudienceANDInnerCustomAttribute;

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
 * ScheduleApiTriggeredCanvasesRequestAudienceANDInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:50.247868-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ScheduleApiTriggeredCanvasesRequestAudienceANDInner {
  public static final String SERIALIZED_NAME_CUSTOM_ATTRIBUTE = "custom_attribute";
  @SerializedName(SERIALIZED_NAME_CUSTOM_ATTRIBUTE)
  private ScheduleApiTriggeredCanvasesRequestAudienceANDInnerCustomAttribute customAttribute;

  public ScheduleApiTriggeredCanvasesRequestAudienceANDInner() {
  }

  public ScheduleApiTriggeredCanvasesRequestAudienceANDInner customAttribute(ScheduleApiTriggeredCanvasesRequestAudienceANDInnerCustomAttribute customAttribute) {
    this.customAttribute = customAttribute;
    return this;
  }

  /**
   * Get customAttribute
   * @return customAttribute
   */
  @javax.annotation.Nullable
  public ScheduleApiTriggeredCanvasesRequestAudienceANDInnerCustomAttribute getCustomAttribute() {
    return customAttribute;
  }

  public void setCustomAttribute(ScheduleApiTriggeredCanvasesRequestAudienceANDInnerCustomAttribute customAttribute) {
    this.customAttribute = customAttribute;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ScheduleApiTriggeredCanvasesRequestAudienceANDInner scheduleApiTriggeredCanvasesRequestAudienceANDInner = (ScheduleApiTriggeredCanvasesRequestAudienceANDInner) o;
    return Objects.equals(this.customAttribute, scheduleApiTriggeredCanvasesRequestAudienceANDInner.customAttribute);
  }

  @Override
  public int hashCode() {
    return Objects.hash(customAttribute);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ScheduleApiTriggeredCanvasesRequestAudienceANDInner {\n");
    sb.append("    customAttribute: ").append(toIndentedString(customAttribute)).append("\n");
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
    openapiFields.add("custom_attribute");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ScheduleApiTriggeredCanvasesRequestAudienceANDInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ScheduleApiTriggeredCanvasesRequestAudienceANDInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ScheduleApiTriggeredCanvasesRequestAudienceANDInner is not found in the empty JSON string", ScheduleApiTriggeredCanvasesRequestAudienceANDInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ScheduleApiTriggeredCanvasesRequestAudienceANDInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ScheduleApiTriggeredCanvasesRequestAudienceANDInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `custom_attribute`
      if (jsonObj.get("custom_attribute") != null && !jsonObj.get("custom_attribute").isJsonNull()) {
        ScheduleApiTriggeredCanvasesRequestAudienceANDInnerCustomAttribute.validateJsonElement(jsonObj.get("custom_attribute"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ScheduleApiTriggeredCanvasesRequestAudienceANDInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ScheduleApiTriggeredCanvasesRequestAudienceANDInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ScheduleApiTriggeredCanvasesRequestAudienceANDInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ScheduleApiTriggeredCanvasesRequestAudienceANDInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ScheduleApiTriggeredCanvasesRequestAudienceANDInner>() {
           @Override
           public void write(JsonWriter out, ScheduleApiTriggeredCanvasesRequestAudienceANDInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ScheduleApiTriggeredCanvasesRequestAudienceANDInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ScheduleApiTriggeredCanvasesRequestAudienceANDInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ScheduleApiTriggeredCanvasesRequestAudienceANDInner
   * @throws IOException if the JSON string is invalid with respect to ScheduleApiTriggeredCanvasesRequestAudienceANDInner
   */
  public static ScheduleApiTriggeredCanvasesRequestAudienceANDInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ScheduleApiTriggeredCanvasesRequestAudienceANDInner.class);
  }

  /**
   * Convert an instance of ScheduleApiTriggeredCanvasesRequestAudienceANDInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

