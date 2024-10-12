/*
 * GraphHopper Directions API
 *  With the [GraphHopper Directions API](https://www.graphhopper.com/products/) you can integrate A-to-B route planning, turn-by-turn navigation, route optimization, isochrone calculations and other tools in your application.  The GraphHopper Directions API consists of the following RESTful web services:   * [Routing API](#tag/Routing-API),  * [Route Optimization API](#tag/Route-Optimization-API),  * [Isochrone API](#tag/Isochrone-API),  * [Map Matching API](#tag/Map-Matching-API),  * [Matrix API](#tag/Matrix-API),  * [Geocoding API](#tag/Geocoding-API) and  * [Cluster API](#tag/Cluster-API).  # Explore our APIs  ## Get started  1. [Sign up for GraphHopper](https://support.graphhopper.com/a/solutions/articles/44001976025) 2. [Create an API key](https://support.graphhopper.com/a/solutions/articles/44001976027)  Each API part has its own documentation. Jump to the desired API part and learn about the API through the given examples and tutorials.  In addition, for each API there are specific sample requests that you can send via Insomnia or Postman to see what the requests and responses look like.  ## Insomnia  To explore our APIs with [Insomnia](https://insomnia.rest/), follow these steps:  1. Open Insomnia and Import [our workspace](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/GraphHopper-Direction-API-Insomnia.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your workspace: Manage Environments -> Base Environment -> `\"api_key\": your API key` 3. Start exploring  ![Insomnia](./img/insomnia.png)  ## Postman  To explore our APIs with [Postman](https://www.getpostman.com/), follow these steps:  1. Import our [request collections](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_collection.json) as well as our [environment file](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_environment.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your environment: `\"api_key\": your API key` 3. Start exploring  ![Postman](./img/postman.png)  ## API Client Libraries  To speed up development and make coding easier, we offer the following client libraries:   * [JavaScript client](https://github.com/graphhopper/directions-api-js-client) - try the [live examples](https://graphhopper.com/api/1/examples/)  * [Others](https://github.com/graphhopper/directions-api-clients) like C#, Ruby, PHP, Python, ... automatically created for the Route Optimization API  ### Bandwidth reduction  If you create your own client, make sure it supports http/2 and gzipped responses for best speed.  If you use the Matrix, the Route Optimization API or the Cluster API and want to solve large problems, we recommend you to reduce bandwidth by [compressing your POST request](https://gist.github.com/karussell/82851e303ea7b3459b2dea01f18949f4) and specifying the header as follows: `Content-Encoding: gzip`. This will also avoid the HTTP 413 error \"Request Entity Too Large\".  ## Contact Us  If you have problems or questions, please read the following information:  - [FAQ](https://graphhopper.com/api/1/docs/FAQ/) - [Public forum](https://discuss.graphhopper.com/c/directions-api) - [Contact us](https://www.graphhopper.com/contact-form/) - [GraphHopper Status Page](https://status.graphhopper.com/)  To stay informed about the latest developments, you can  - follow us on [twitter](https://twitter.com/graphhopper/), - read [our blog](https://graphhopper.com/blog/), - watch [our documentation repository](https://github.com/graphhopper/directions-api-doc), - sign up for our newsletter or - [our forum](https://discuss.graphhopper.com/c/directions-api).  Select the channel you like the most.   # Map Data and Routing Profiles  Currently, our main data source is [OpenStreetMap](https://www.openstreetmap.org). We also integrated other network data providers. This chapter gives an overview about the options you have.  ## OpenStreetMap  #### Geographical Coverage  [OpenStreetMap](https://www.openstreetmap.org) covers the whole world. If you want to see for yourself if we can provide data suitable for your region, please visit [GraphHopper Maps](https://graphhopper.com/maps/). You can edit and modify OpenStreetMap data if you find that important information is missing, e.g. a weight limit for a bridge. [Here](https://wiki.openstreetmap.org/wiki/Beginners%27_guide) is a beginner's guide that shows how to add data. If you have edited data, we usually consider your data after 1 week at the latest.  #### Supported Vehicle Profiles  The Routing, Matrix and Route Optimization APIs support the following vehicle profiles:  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) truck      | Truck like a MAN or Mercedes-Benz Actros | height=3.7m, width=2.6+0.5m, length=12m, weight=13000 + 13000 kg, hgv=yes, 3 Axes | ![truck image](https://graphhopper.com/maps/img/truck.png) scooter    | Moped mode | Fast inner city, often used for food delivery, is able to ignore certain bollards, maximum speed of roughly 50km/h | ![scooter image](https://graphhopper.com/maps/img/scooter.png) foot       | Pedestrian or walking without dangerous [SAC-scales](https://wiki.openstreetmap.org/wiki/Key:sac_scale) | foot access         | ![foot image](https://graphhopper.com/maps/img/foot.png) hike       | Pedestrian or walking with priority for more beautiful hiking tours and potentially a bit longer than `foot`. Walking duration is influenced by elevation differences.  | foot access         | ![hike image](https://graphhopper.com/maps/img/hike.png) bike       | Trekking bike avoiding hills | bike access  | ![bike image](https://graphhopper.com/maps/img/bike.png) mtb        | Mountainbike          | bike access         | ![Mountainbike image](https://graphhopper.com/maps/img/mtb.png) racingbike| Bike preferring roads | bike access         | ![racingbike image](https://graphhopper.com/maps/img/racingbike.png)  Please note:   * all motor vehicles (`car`, `small_truck`, `truck` and `scooter`) support turn restrictions via `turn_costs=true`  * the free package supports only the vehicle profiles `car`, `bike` or `foot`  * up to 2 different vehicle profiles can be used in a single optimization request. The number of vehicles is unaffected and depends on your subscription.  * we offer custom vehicle profiles with different properties, different speed profiles or different access options. To find out more about custom profiles, please [contact us](https://www.graphhopper.com/contact-form/).  * a sophisticated `motorcycle` profile is available up on request. It is powered by the [Kurviger](https://kurviger.de/en) Routing API and favors curves and slopes while avoiding cities and highways.   ## TomTom  If you want to include traffic, you can purchase the TomTom Add-on. This Add-on only uses TomTom's road network and historical traffic information. Live traffic is not yet considered. If you are interested to learn how we consider traffic information, we recommend that you read [this article](https://www.graphhopper.com/blog/2017/11/06/time-dependent-optimization/).  Please note the following:   * Currently we only offer this for our [Route Optimization API](#tag/Route-Optimization-API).  * In addition to our terms, you need to accept TomTom's [End User License Aggreement](https://www.graphhopper.com/tomtom-end-user-license-agreement/).  * We do *not* use TomTom's web services. We only use their data with our software.   [Contact us](https://www.graphhopper.com/contact-form/) for more details.  #### Geographical Coverage  We offer  - Europe including Russia - North, Central and South America - Saudi Arabia - United Arab Emirates - South Africa - Australia  #### Supported Vehicle Profiles  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@graphhopper.com
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
 * Objective
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:20.208084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Objective {
  /**
   * Type of objective function, i.e. &#x60;min&#x60; or &#x60;min-max&#x60;.   * &#x60;min&#x60;: Minimizes the objective value.  * &#x60;min-max&#x60;: Minimizes the maximum objective value.  For instance, &#x60;min&#x60; -&gt; &#x60;vehicles&#x60; minimizes the number of employed vehicles. &#x60;min&#x60; -&gt; &#x60;completion_time&#x60; minimizes the sum of your vehicle routes&#39; completion time.  If you use, for example, &#x60;min-max&#x60; -&gt; &#x60;completion_time&#x60;, it minimizes the maximum of your vehicle routes&#39; completion time, i.e. it minimizes the overall makespan. This only makes sense if you have more than one vehicle. In case of one vehicle, switching from &#x60;min&#x60; to &#x60;min-max&#x60; should not have any impact. If you have more than one vehicle, then the algorithm tries to constantly move stops from one vehicle to another such that the completion time of longest vehicle route can be further reduced. For example, if you have one vehicle that takes 8 hours to serve all customers, adding another vehicle (and using &#x60;min-max&#x60;) might halve the time to serve all customers to 4 hours. However, this usually comes with higher transport costs.  If you want to minimize &#x60;vehicles&#x60; first and, second, &#x60;completion_time&#x60;, you can also combine different objectives like this:  &#x60;&#x60;&#x60;json \&quot;objectives\&quot; : [    {       \&quot;type\&quot;: \&quot;min\&quot;,       \&quot;value\&quot;: \&quot;vehicles\&quot;    },    {       \&quot;type\&quot;: \&quot;min\&quot;,       \&quot;value\&quot;: \&quot;completion_time\&quot;    } ] &#x60;&#x60;&#x60;  If you want to balance activities or the number of stops among all employed drivers, you need to specify it as follows:  &#x60;&#x60;&#x60;json \&quot;objectives\&quot; : [    {       \&quot;type\&quot;: \&quot;min-max\&quot;,       \&quot;value\&quot;: \&quot;completion_time\&quot;    },    {       \&quot;type\&quot;: \&quot;min-max\&quot;,       \&quot;value\&quot;: \&quot;activities\&quot;    } ] &#x60;&#x60;&#x60; 
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    MIN("min"),
    
    MIN_MAX("min-max");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type = TypeEnum.MIN;

  /**
   * The value of the objective function. The objective value &#x60;transport_time&#x60; solely considers the time your drivers spend on the road, i.e. transport time. In contrary to &#x60;transport_time&#x60;, &#x60;completion_time&#x60; also takes waiting times at customer sites into account. The &#x60;completion_time&#x60; of a route is defined as the time from starting to ending the route, i.e. the route&#39;s transport time, the sum of waiting times plus the sum of activity durations. Note that choosing &#x60;transport_time&#x60; or &#x60;completion_time&#x60; only makes a difference if you specified time windows for your services/shipments since only in scenarios with time windows waiting times can occur. The objective value &#x60;vehicles&#x60; can only be used along with &#x60;min&#x60; and minimizes vehicles. 
   */
  @JsonAdapter(ValueEnum.Adapter.class)
  public enum ValueEnum {
    COMPLETION_TIME("completion_time"),
    
    TRANSPORT_TIME("transport_time"),
    
    VEHICLES("vehicles"),
    
    ACTIVITIES("activities");

    private String value;

    ValueEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ValueEnum fromValue(String value) {
      for (ValueEnum b : ValueEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ValueEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ValueEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ValueEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ValueEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ValueEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private ValueEnum value = ValueEnum.TRANSPORT_TIME;

  public Objective() {
  }

  public Objective type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Type of objective function, i.e. &#x60;min&#x60; or &#x60;min-max&#x60;.   * &#x60;min&#x60;: Minimizes the objective value.  * &#x60;min-max&#x60;: Minimizes the maximum objective value.  For instance, &#x60;min&#x60; -&gt; &#x60;vehicles&#x60; minimizes the number of employed vehicles. &#x60;min&#x60; -&gt; &#x60;completion_time&#x60; minimizes the sum of your vehicle routes&#39; completion time.  If you use, for example, &#x60;min-max&#x60; -&gt; &#x60;completion_time&#x60;, it minimizes the maximum of your vehicle routes&#39; completion time, i.e. it minimizes the overall makespan. This only makes sense if you have more than one vehicle. In case of one vehicle, switching from &#x60;min&#x60; to &#x60;min-max&#x60; should not have any impact. If you have more than one vehicle, then the algorithm tries to constantly move stops from one vehicle to another such that the completion time of longest vehicle route can be further reduced. For example, if you have one vehicle that takes 8 hours to serve all customers, adding another vehicle (and using &#x60;min-max&#x60;) might halve the time to serve all customers to 4 hours. However, this usually comes with higher transport costs.  If you want to minimize &#x60;vehicles&#x60; first and, second, &#x60;completion_time&#x60;, you can also combine different objectives like this:  &#x60;&#x60;&#x60;json \&quot;objectives\&quot; : [    {       \&quot;type\&quot;: \&quot;min\&quot;,       \&quot;value\&quot;: \&quot;vehicles\&quot;    },    {       \&quot;type\&quot;: \&quot;min\&quot;,       \&quot;value\&quot;: \&quot;completion_time\&quot;    } ] &#x60;&#x60;&#x60;  If you want to balance activities or the number of stops among all employed drivers, you need to specify it as follows:  &#x60;&#x60;&#x60;json \&quot;objectives\&quot; : [    {       \&quot;type\&quot;: \&quot;min-max\&quot;,       \&quot;value\&quot;: \&quot;completion_time\&quot;    },    {       \&quot;type\&quot;: \&quot;min-max\&quot;,       \&quot;value\&quot;: \&quot;activities\&quot;    } ] &#x60;&#x60;&#x60; 
   * @return type
   */
  @javax.annotation.Nonnull
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }


  public Objective value(ValueEnum value) {
    this.value = value;
    return this;
  }

  /**
   * The value of the objective function. The objective value &#x60;transport_time&#x60; solely considers the time your drivers spend on the road, i.e. transport time. In contrary to &#x60;transport_time&#x60;, &#x60;completion_time&#x60; also takes waiting times at customer sites into account. The &#x60;completion_time&#x60; of a route is defined as the time from starting to ending the route, i.e. the route&#39;s transport time, the sum of waiting times plus the sum of activity durations. Note that choosing &#x60;transport_time&#x60; or &#x60;completion_time&#x60; only makes a difference if you specified time windows for your services/shipments since only in scenarios with time windows waiting times can occur. The objective value &#x60;vehicles&#x60; can only be used along with &#x60;min&#x60; and minimizes vehicles. 
   * @return value
   */
  @javax.annotation.Nonnull
  public ValueEnum getValue() {
    return value;
  }

  public void setValue(ValueEnum value) {
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
    Objective objective = (Objective) o;
    return Objects.equals(this.type, objective.type) &&
        Objects.equals(this.value, objective.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(type, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Objective {\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("type");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("type");
    openapiRequiredFields.add("value");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Objective
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Objective.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Objective is not found in the empty JSON string", Objective.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Objective.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Objective` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Objective.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the required field `type`
      TypeEnum.validateJsonElement(jsonObj.get("type"));
      if (!jsonObj.get("value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("value").toString()));
      }
      // validate the required field `value`
      ValueEnum.validateJsonElement(jsonObj.get("value"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Objective.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Objective' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Objective> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Objective.class));

       return (TypeAdapter<T>) new TypeAdapter<Objective>() {
           @Override
           public void write(JsonWriter out, Objective value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Objective read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Objective given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Objective
   * @throws IOException if the JSON string is invalid with respect to Objective
   */
  public static Objective fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Objective.class);
  }

  /**
   * Convert an instance of Objective to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

