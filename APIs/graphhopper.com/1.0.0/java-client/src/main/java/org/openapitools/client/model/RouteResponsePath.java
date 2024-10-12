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
import org.openapitools.client.model.RouteResponsePathInstructionsInner;
import org.openapitools.client.model.RouteResponsePathPoints;
import org.openapitools.client.model.RouteResponsePathSnappedWaypoints;

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
 * RouteResponsePath
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:20.208084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RouteResponsePath {
  public static final String SERIALIZED_NAME_ASCEND = "ascend";
  @SerializedName(SERIALIZED_NAME_ASCEND)
  private Double ascend;

  public static final String SERIALIZED_NAME_BBOX = "bbox";
  @SerializedName(SERIALIZED_NAME_BBOX)
  private List<Double> bbox = new ArrayList<>();

  public static final String SERIALIZED_NAME_DESCEND = "descend";
  @SerializedName(SERIALIZED_NAME_DESCEND)
  private Double descend;

  public static final String SERIALIZED_NAME_DETAILS = "details";
  @SerializedName(SERIALIZED_NAME_DETAILS)
  private Object details;

  public static final String SERIALIZED_NAME_DISTANCE = "distance";
  @SerializedName(SERIALIZED_NAME_DISTANCE)
  private Double distance;

  public static final String SERIALIZED_NAME_INSTRUCTIONS = "instructions";
  @SerializedName(SERIALIZED_NAME_INSTRUCTIONS)
  private List<RouteResponsePathInstructionsInner> instructions = new ArrayList<>();

  public static final String SERIALIZED_NAME_POINTS = "points";
  @SerializedName(SERIALIZED_NAME_POINTS)
  private RouteResponsePathPoints points;

  public static final String SERIALIZED_NAME_POINTS_ENCODED = "points_encoded";
  @SerializedName(SERIALIZED_NAME_POINTS_ENCODED)
  private Boolean pointsEncoded;

  public static final String SERIALIZED_NAME_POINTS_ORDER = "points_order";
  @SerializedName(SERIALIZED_NAME_POINTS_ORDER)
  private List<Integer> pointsOrder = new ArrayList<>();

  public static final String SERIALIZED_NAME_SNAPPED_WAYPOINTS = "snapped_waypoints";
  @SerializedName(SERIALIZED_NAME_SNAPPED_WAYPOINTS)
  private RouteResponsePathSnappedWaypoints snappedWaypoints;

  public static final String SERIALIZED_NAME_TIME = "time";
  @SerializedName(SERIALIZED_NAME_TIME)
  private Long time;

  public RouteResponsePath() {
  }

  public RouteResponsePath ascend(Double ascend) {
    this.ascend = ascend;
    return this;
  }

  /**
   * The total ascent, in meters. 
   * @return ascend
   */
  @javax.annotation.Nullable
  public Double getAscend() {
    return ascend;
  }

  public void setAscend(Double ascend) {
    this.ascend = ascend;
  }


  public RouteResponsePath bbox(List<Double> bbox) {
    this.bbox = bbox;
    return this;
  }

  public RouteResponsePath addBboxItem(Double bboxItem) {
    if (this.bbox == null) {
      this.bbox = new ArrayList<>();
    }
    this.bbox.add(bboxItem);
    return this;
  }

  /**
   * The bounding box of the route geometry. Format: &#x60;[minLon, minLat, maxLon, maxLat]&#x60;. 
   * @return bbox
   */
  @javax.annotation.Nullable
  public List<Double> getBbox() {
    return bbox;
  }

  public void setBbox(List<Double> bbox) {
    this.bbox = bbox;
  }


  public RouteResponsePath descend(Double descend) {
    this.descend = descend;
    return this;
  }

  /**
   * The total descent, in meters. 
   * @return descend
   */
  @javax.annotation.Nullable
  public Double getDescend() {
    return descend;
  }

  public void setDescend(Double descend) {
    this.descend = descend;
  }


  public RouteResponsePath details(Object details) {
    this.details = details;
    return this;
  }

  /**
   * Details, as requested with the &#x60;details&#x60; parameter. Consider the value &#x60;{\&quot;street_name\&quot;: [[0,2,\&quot;Frankfurter Straße\&quot;],[2,6,\&quot;Zollweg\&quot;]]}&#x60;. In this example, the route uses two streets: The first, Frankfurter Straße, is used between &#x60;points[0]&#x60; and &#x60;points[2]&#x60;, and the second, Zollweg, between &#x60;points[2]&#x60; and &#x60;points[6]&#x60;. See [here](https://discuss.graphhopper.com/t/2539) for discussion. 
   * @return details
   */
  @javax.annotation.Nullable
  public Object getDetails() {
    return details;
  }

  public void setDetails(Object details) {
    this.details = details;
  }


  public RouteResponsePath distance(Double distance) {
    this.distance = distance;
    return this;
  }

  /**
   * The total distance, in meters. To get this information for one &#39;leg&#39; please read [this blog post](https://www.graphhopper.com/blog/2019/11/28/routing-api-using-path-details/). 
   * @return distance
   */
  @javax.annotation.Nullable
  public Double getDistance() {
    return distance;
  }

  public void setDistance(Double distance) {
    this.distance = distance;
  }


  public RouteResponsePath instructions(List<RouteResponsePathInstructionsInner> instructions) {
    this.instructions = instructions;
    return this;
  }

  public RouteResponsePath addInstructionsItem(RouteResponsePathInstructionsInner instructionsItem) {
    if (this.instructions == null) {
      this.instructions = new ArrayList<>();
    }
    this.instructions.add(instructionsItem);
    return this;
  }

  /**
   * The instructions for this route. This feature is under active development, and our instructions can sometimes be misleading, so be mindful when using them for navigation. 
   * @return instructions
   */
  @javax.annotation.Nullable
  public List<RouteResponsePathInstructionsInner> getInstructions() {
    return instructions;
  }

  public void setInstructions(List<RouteResponsePathInstructionsInner> instructions) {
    this.instructions = instructions;
  }


  public RouteResponsePath points(RouteResponsePathPoints points) {
    this.points = points;
    return this;
  }

  /**
   * Get points
   * @return points
   */
  @javax.annotation.Nullable
  public RouteResponsePathPoints getPoints() {
    return points;
  }

  public void setPoints(RouteResponsePathPoints points) {
    this.points = points;
  }


  public RouteResponsePath pointsEncoded(Boolean pointsEncoded) {
    this.pointsEncoded = pointsEncoded;
    return this;
  }

  /**
   * Whether the &#x60;points&#x60; and &#x60;snapped_waypoints&#x60; fields are polyline-encoded strings rather than JSON arrays of coordinates. See the field description for more information on the two formats. 
   * @return pointsEncoded
   */
  @javax.annotation.Nullable
  public Boolean getPointsEncoded() {
    return pointsEncoded;
  }

  public void setPointsEncoded(Boolean pointsEncoded) {
    this.pointsEncoded = pointsEncoded;
  }


  public RouteResponsePath pointsOrder(List<Integer> pointsOrder) {
    this.pointsOrder = pointsOrder;
    return this;
  }

  public RouteResponsePath addPointsOrderItem(Integer pointsOrderItem) {
    if (this.pointsOrder == null) {
      this.pointsOrder = new ArrayList<>();
    }
    this.pointsOrder.add(pointsOrderItem);
    return this;
  }

  /**
   * An array of indices (zero-based), specifiying the order in which the input points are visited. Only present if the &#x60;optimize&#x60; parameter was used. 
   * @return pointsOrder
   */
  @javax.annotation.Nullable
  public List<Integer> getPointsOrder() {
    return pointsOrder;
  }

  public void setPointsOrder(List<Integer> pointsOrder) {
    this.pointsOrder = pointsOrder;
  }


  public RouteResponsePath snappedWaypoints(RouteResponsePathSnappedWaypoints snappedWaypoints) {
    this.snappedWaypoints = snappedWaypoints;
    return this;
  }

  /**
   * Get snappedWaypoints
   * @return snappedWaypoints
   */
  @javax.annotation.Nullable
  public RouteResponsePathSnappedWaypoints getSnappedWaypoints() {
    return snappedWaypoints;
  }

  public void setSnappedWaypoints(RouteResponsePathSnappedWaypoints snappedWaypoints) {
    this.snappedWaypoints = snappedWaypoints;
  }


  public RouteResponsePath time(Long time) {
    this.time = time;
    return this;
  }

  /**
   * The total travel time, in milliseconds. To get this information for one &#39;leg&#39; please read [this blog post](https://www.graphhopper.com/blog/2019/11/28/routing-api-using-path-details/). 
   * @return time
   */
  @javax.annotation.Nullable
  public Long getTime() {
    return time;
  }

  public void setTime(Long time) {
    this.time = time;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RouteResponsePath routeResponsePath = (RouteResponsePath) o;
    return Objects.equals(this.ascend, routeResponsePath.ascend) &&
        Objects.equals(this.bbox, routeResponsePath.bbox) &&
        Objects.equals(this.descend, routeResponsePath.descend) &&
        Objects.equals(this.details, routeResponsePath.details) &&
        Objects.equals(this.distance, routeResponsePath.distance) &&
        Objects.equals(this.instructions, routeResponsePath.instructions) &&
        Objects.equals(this.points, routeResponsePath.points) &&
        Objects.equals(this.pointsEncoded, routeResponsePath.pointsEncoded) &&
        Objects.equals(this.pointsOrder, routeResponsePath.pointsOrder) &&
        Objects.equals(this.snappedWaypoints, routeResponsePath.snappedWaypoints) &&
        Objects.equals(this.time, routeResponsePath.time);
  }

  @Override
  public int hashCode() {
    return Objects.hash(ascend, bbox, descend, details, distance, instructions, points, pointsEncoded, pointsOrder, snappedWaypoints, time);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RouteResponsePath {\n");
    sb.append("    ascend: ").append(toIndentedString(ascend)).append("\n");
    sb.append("    bbox: ").append(toIndentedString(bbox)).append("\n");
    sb.append("    descend: ").append(toIndentedString(descend)).append("\n");
    sb.append("    details: ").append(toIndentedString(details)).append("\n");
    sb.append("    distance: ").append(toIndentedString(distance)).append("\n");
    sb.append("    instructions: ").append(toIndentedString(instructions)).append("\n");
    sb.append("    points: ").append(toIndentedString(points)).append("\n");
    sb.append("    pointsEncoded: ").append(toIndentedString(pointsEncoded)).append("\n");
    sb.append("    pointsOrder: ").append(toIndentedString(pointsOrder)).append("\n");
    sb.append("    snappedWaypoints: ").append(toIndentedString(snappedWaypoints)).append("\n");
    sb.append("    time: ").append(toIndentedString(time)).append("\n");
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
    openapiFields.add("ascend");
    openapiFields.add("bbox");
    openapiFields.add("descend");
    openapiFields.add("details");
    openapiFields.add("distance");
    openapiFields.add("instructions");
    openapiFields.add("points");
    openapiFields.add("points_encoded");
    openapiFields.add("points_order");
    openapiFields.add("snapped_waypoints");
    openapiFields.add("time");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RouteResponsePath
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RouteResponsePath.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RouteResponsePath is not found in the empty JSON string", RouteResponsePath.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RouteResponsePath.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RouteResponsePath` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("bbox") != null && !jsonObj.get("bbox").isJsonNull() && !jsonObj.get("bbox").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `bbox` to be an array in the JSON string but got `%s`", jsonObj.get("bbox").toString()));
      }
      if (jsonObj.get("instructions") != null && !jsonObj.get("instructions").isJsonNull()) {
        JsonArray jsonArrayinstructions = jsonObj.getAsJsonArray("instructions");
        if (jsonArrayinstructions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("instructions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `instructions` to be an array in the JSON string but got `%s`", jsonObj.get("instructions").toString()));
          }

          // validate the optional field `instructions` (array)
          for (int i = 0; i < jsonArrayinstructions.size(); i++) {
            RouteResponsePathInstructionsInner.validateJsonElement(jsonArrayinstructions.get(i));
          };
        }
      }
      // validate the optional field `points`
      if (jsonObj.get("points") != null && !jsonObj.get("points").isJsonNull()) {
        RouteResponsePathPoints.validateJsonElement(jsonObj.get("points"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("points_order") != null && !jsonObj.get("points_order").isJsonNull() && !jsonObj.get("points_order").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `points_order` to be an array in the JSON string but got `%s`", jsonObj.get("points_order").toString()));
      }
      // validate the optional field `snapped_waypoints`
      if (jsonObj.get("snapped_waypoints") != null && !jsonObj.get("snapped_waypoints").isJsonNull()) {
        RouteResponsePathSnappedWaypoints.validateJsonElement(jsonObj.get("snapped_waypoints"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RouteResponsePath.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RouteResponsePath' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RouteResponsePath> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RouteResponsePath.class));

       return (TypeAdapter<T>) new TypeAdapter<RouteResponsePath>() {
           @Override
           public void write(JsonWriter out, RouteResponsePath value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RouteResponsePath read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RouteResponsePath given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RouteResponsePath
   * @throws IOException if the JSON string is invalid with respect to RouteResponsePath
   */
  public static RouteResponsePath fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RouteResponsePath.class);
  }

  /**
   * Convert an instance of RouteResponsePath to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

