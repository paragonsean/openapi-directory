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
 * RouteResponsePathInstructionsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:20.208084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RouteResponsePathInstructionsInner {
  public static final String SERIALIZED_NAME_DISTANCE = "distance";
  @SerializedName(SERIALIZED_NAME_DISTANCE)
  private Double distance;

  public static final String SERIALIZED_NAME_EXIT_NUMBER = "exit_number";
  @SerializedName(SERIALIZED_NAME_EXIT_NUMBER)
  private Integer exitNumber;

  public static final String SERIALIZED_NAME_INTERVAL = "interval";
  @SerializedName(SERIALIZED_NAME_INTERVAL)
  private List<Integer> interval = new ArrayList<>();

  public static final String SERIALIZED_NAME_SIGN = "sign";
  @SerializedName(SERIALIZED_NAME_SIGN)
  private Integer sign;

  public static final String SERIALIZED_NAME_STREET_NAME = "street_name";
  @SerializedName(SERIALIZED_NAME_STREET_NAME)
  private String streetName;

  public static final String SERIALIZED_NAME_TEXT = "text";
  @SerializedName(SERIALIZED_NAME_TEXT)
  private String text;

  public static final String SERIALIZED_NAME_TIME = "time";
  @SerializedName(SERIALIZED_NAME_TIME)
  private Integer time;

  public static final String SERIALIZED_NAME_TURN_ANGLE = "turn_angle";
  @SerializedName(SERIALIZED_NAME_TURN_ANGLE)
  private Double turnAngle;

  public RouteResponsePathInstructionsInner() {
  }

  public RouteResponsePathInstructionsInner distance(Double distance) {
    this.distance = distance;
    return this;
  }

  /**
   * The distance for this instruction, in meters. 
   * @return distance
   */
  @javax.annotation.Nullable
  public Double getDistance() {
    return distance;
  }

  public void setDistance(Double distance) {
    this.distance = distance;
  }


  public RouteResponsePathInstructionsInner exitNumber(Integer exitNumber) {
    this.exitNumber = exitNumber;
    return this;
  }

  /**
   * Only available for roundabout instructions (sign is 6). The count of exits at which the route leaves the roundabout. 
   * @return exitNumber
   */
  @javax.annotation.Nullable
  public Integer getExitNumber() {
    return exitNumber;
  }

  public void setExitNumber(Integer exitNumber) {
    this.exitNumber = exitNumber;
  }


  public RouteResponsePathInstructionsInner interval(List<Integer> interval) {
    this.interval = interval;
    return this;
  }

  public RouteResponsePathInstructionsInner addIntervalItem(Integer intervalItem) {
    if (this.interval == null) {
      this.interval = new ArrayList<>();
    }
    this.interval.add(intervalItem);
    return this;
  }

  /**
   * Two indices into &#x60;points&#x60;, referring to the beginning and the end of the segment of the route this instruction refers to. 
   * @return interval
   */
  @javax.annotation.Nullable
  public List<Integer> getInterval() {
    return interval;
  }

  public void setInterval(List<Integer> interval) {
    this.interval = interval;
  }


  public RouteResponsePathInstructionsInner sign(Integer sign) {
    this.sign = sign;
    return this;
  }

  /**
   * A number which specifies the sign to show:  | sign | description  | |---|---| |-98| an U-turn without the knowledge if it is a right or left U-turn | | -8| a left U-turn | | -7| keep left | | -6| **not yet used**: leave roundabout | | -3| turn sharp left | | -2| turn left | | -1| turn slight left | |  0| continue on street | |  1| turn slight right | |  2| turn right | |  3| turn sharp right | |  4| the finish instruction before the last point | |  5| the instruction before a via point | |  6| the instruction before entering a roundabout | |  7| keep right | |  8| a right U-turn | |  *| **For future compatibility** it is important that all clients are able to handle also unknown instruction sign numbers 
   * @return sign
   */
  @javax.annotation.Nullable
  public Integer getSign() {
    return sign;
  }

  public void setSign(Integer sign) {
    this.sign = sign;
  }


  public RouteResponsePathInstructionsInner streetName(String streetName) {
    this.streetName = streetName;
    return this;
  }

  /**
   * The name of the street to turn onto in order to follow the route. 
   * @return streetName
   */
  @javax.annotation.Nullable
  public String getStreetName() {
    return streetName;
  }

  public void setStreetName(String streetName) {
    this.streetName = streetName;
  }


  public RouteResponsePathInstructionsInner text(String text) {
    this.text = text;
    return this;
  }

  /**
   * A description what the user has to do in order to follow the route. The language depends on the locale parameter. 
   * @return text
   */
  @javax.annotation.Nullable
  public String getText() {
    return text;
  }

  public void setText(String text) {
    this.text = text;
  }


  public RouteResponsePathInstructionsInner time(Integer time) {
    this.time = time;
    return this;
  }

  /**
   * The duration for this instruction, in milliseconds. 
   * @return time
   */
  @javax.annotation.Nullable
  public Integer getTime() {
    return time;
  }

  public void setTime(Integer time) {
    this.time = time;
  }


  public RouteResponsePathInstructionsInner turnAngle(Double turnAngle) {
    this.turnAngle = turnAngle;
    return this;
  }

  /**
   * Only available for roundabout instructions (sign is 6). The radian of the route within the roundabout &#x60;0 &lt; r &lt; 2*PI&#x60; for clockwise and &#x60;-2*PI &lt; r &lt; 0&#x60; for counterclockwise turns. 
   * @return turnAngle
   */
  @javax.annotation.Nullable
  public Double getTurnAngle() {
    return turnAngle;
  }

  public void setTurnAngle(Double turnAngle) {
    this.turnAngle = turnAngle;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RouteResponsePathInstructionsInner routeResponsePathInstructionsInner = (RouteResponsePathInstructionsInner) o;
    return Objects.equals(this.distance, routeResponsePathInstructionsInner.distance) &&
        Objects.equals(this.exitNumber, routeResponsePathInstructionsInner.exitNumber) &&
        Objects.equals(this.interval, routeResponsePathInstructionsInner.interval) &&
        Objects.equals(this.sign, routeResponsePathInstructionsInner.sign) &&
        Objects.equals(this.streetName, routeResponsePathInstructionsInner.streetName) &&
        Objects.equals(this.text, routeResponsePathInstructionsInner.text) &&
        Objects.equals(this.time, routeResponsePathInstructionsInner.time) &&
        Objects.equals(this.turnAngle, routeResponsePathInstructionsInner.turnAngle);
  }

  @Override
  public int hashCode() {
    return Objects.hash(distance, exitNumber, interval, sign, streetName, text, time, turnAngle);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RouteResponsePathInstructionsInner {\n");
    sb.append("    distance: ").append(toIndentedString(distance)).append("\n");
    sb.append("    exitNumber: ").append(toIndentedString(exitNumber)).append("\n");
    sb.append("    interval: ").append(toIndentedString(interval)).append("\n");
    sb.append("    sign: ").append(toIndentedString(sign)).append("\n");
    sb.append("    streetName: ").append(toIndentedString(streetName)).append("\n");
    sb.append("    text: ").append(toIndentedString(text)).append("\n");
    sb.append("    time: ").append(toIndentedString(time)).append("\n");
    sb.append("    turnAngle: ").append(toIndentedString(turnAngle)).append("\n");
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
    openapiFields.add("distance");
    openapiFields.add("exit_number");
    openapiFields.add("interval");
    openapiFields.add("sign");
    openapiFields.add("street_name");
    openapiFields.add("text");
    openapiFields.add("time");
    openapiFields.add("turn_angle");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RouteResponsePathInstructionsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RouteResponsePathInstructionsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RouteResponsePathInstructionsInner is not found in the empty JSON string", RouteResponsePathInstructionsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RouteResponsePathInstructionsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RouteResponsePathInstructionsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("interval") != null && !jsonObj.get("interval").isJsonNull() && !jsonObj.get("interval").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `interval` to be an array in the JSON string but got `%s`", jsonObj.get("interval").toString()));
      }
      if ((jsonObj.get("street_name") != null && !jsonObj.get("street_name").isJsonNull()) && !jsonObj.get("street_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `street_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("street_name").toString()));
      }
      if ((jsonObj.get("text") != null && !jsonObj.get("text").isJsonNull()) && !jsonObj.get("text").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `text` to be a primitive type in the JSON string but got `%s`", jsonObj.get("text").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RouteResponsePathInstructionsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RouteResponsePathInstructionsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RouteResponsePathInstructionsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RouteResponsePathInstructionsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<RouteResponsePathInstructionsInner>() {
           @Override
           public void write(JsonWriter out, RouteResponsePathInstructionsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RouteResponsePathInstructionsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RouteResponsePathInstructionsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RouteResponsePathInstructionsInner
   * @throws IOException if the JSON string is invalid with respect to RouteResponsePathInstructionsInner
   */
  public static RouteResponsePathInstructionsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RouteResponsePathInstructionsInner.class);
  }

  /**
   * Convert an instance of RouteResponsePathInstructionsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

