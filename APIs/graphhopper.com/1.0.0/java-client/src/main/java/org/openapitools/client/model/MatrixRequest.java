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
import org.openapitools.client.model.VehicleProfileId;

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
 * MatrixRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:20.208084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class MatrixRequest {
  public static final String SERIALIZED_NAME_FAIL_FAST = "fail_fast";
  @SerializedName(SERIALIZED_NAME_FAIL_FAST)
  private Boolean failFast = true;

  public static final String SERIALIZED_NAME_FROM_CURBSIDES = "from_curbsides";
  @SerializedName(SERIALIZED_NAME_FROM_CURBSIDES)
  private List<String> fromCurbsides = new ArrayList<>();

  public static final String SERIALIZED_NAME_FROM_POINT_HINTS = "from_point_hints";
  @SerializedName(SERIALIZED_NAME_FROM_POINT_HINTS)
  private List<String> fromPointHints = new ArrayList<>();

  public static final String SERIALIZED_NAME_FROM_POINTS = "from_points";
  @SerializedName(SERIALIZED_NAME_FROM_POINTS)
  private List<List<Double>> fromPoints = new ArrayList<>();

  public static final String SERIALIZED_NAME_OUT_ARRAYS = "out_arrays";
  @SerializedName(SERIALIZED_NAME_OUT_ARRAYS)
  private List<String> outArrays = new ArrayList<>();

  public static final String SERIALIZED_NAME_SNAP_PREVENTIONS = "snap_preventions";
  @SerializedName(SERIALIZED_NAME_SNAP_PREVENTIONS)
  private List<String> snapPreventions = new ArrayList<>();

  public static final String SERIALIZED_NAME_TO_CURBSIDES = "to_curbsides";
  @SerializedName(SERIALIZED_NAME_TO_CURBSIDES)
  private List<String> toCurbsides = new ArrayList<>();

  public static final String SERIALIZED_NAME_TO_POINT_HINTS = "to_point_hints";
  @SerializedName(SERIALIZED_NAME_TO_POINT_HINTS)
  private List<String> toPointHints = new ArrayList<>();

  public static final String SERIALIZED_NAME_TO_POINTS = "to_points";
  @SerializedName(SERIALIZED_NAME_TO_POINTS)
  private List<List<Double>> toPoints = new ArrayList<>();

  public static final String SERIALIZED_NAME_TURN_COSTS = "turn_costs";
  @SerializedName(SERIALIZED_NAME_TURN_COSTS)
  private Boolean turnCosts = false;

  public static final String SERIALIZED_NAME_VEHICLE = "vehicle";
  @SerializedName(SERIALIZED_NAME_VEHICLE)
  private VehicleProfileId vehicle;

  public MatrixRequest() {
  }

  public MatrixRequest failFast(Boolean failFast) {
    this.failFast = failFast;
    return this;
  }

  /**
   * Specifies whether or not the matrix calculation should return with an error as soon as possible in case some points cannot be found or some points are not connected. If set to &#x60;false&#x60; the time/weight/distance matrix will be calculated for all valid points and contain the &#x60;null&#x60; value for all entries that could not be calculated. The &#x60;hint&#x60; field of the response will also contain additional information about what went wrong (see its documentation).
   * @return failFast
   */
  @javax.annotation.Nullable
  public Boolean getFailFast() {
    return failFast;
  }

  public void setFailFast(Boolean failFast) {
    this.failFast = failFast;
  }


  public MatrixRequest fromCurbsides(List<String> fromCurbsides) {
    this.fromCurbsides = fromCurbsides;
    return this;
  }

  public MatrixRequest addFromCurbsidesItem(String fromCurbsidesItem) {
    if (this.fromCurbsides == null) {
      this.fromCurbsides = new ArrayList<>();
    }
    this.fromCurbsides.add(fromCurbsidesItem);
    return this;
  }

  /**
   * See &#x60;curbsides&#x60;of symmetrical matrix
   * @return fromCurbsides
   */
  @javax.annotation.Nullable
  public List<String> getFromCurbsides() {
    return fromCurbsides;
  }

  public void setFromCurbsides(List<String> fromCurbsides) {
    this.fromCurbsides = fromCurbsides;
  }


  public MatrixRequest fromPointHints(List<String> fromPointHints) {
    this.fromPointHints = fromPointHints;
    return this;
  }

  public MatrixRequest addFromPointHintsItem(String fromPointHintsItem) {
    if (this.fromPointHints == null) {
      this.fromPointHints = new ArrayList<>();
    }
    this.fromPointHints.add(fromPointHintsItem);
    return this;
  }

  /**
   * See &#x60;point_hints&#x60;of symmetrical matrix
   * @return fromPointHints
   */
  @javax.annotation.Nullable
  public List<String> getFromPointHints() {
    return fromPointHints;
  }

  public void setFromPointHints(List<String> fromPointHints) {
    this.fromPointHints = fromPointHints;
  }


  public MatrixRequest fromPoints(List<List<Double>> fromPoints) {
    this.fromPoints = fromPoints;
    return this;
  }

  public MatrixRequest addFromPointsItem(List<Double> fromPointsItem) {
    if (this.fromPoints == null) {
      this.fromPoints = new ArrayList<>();
    }
    this.fromPoints.add(fromPointsItem);
    return this;
  }

  /**
   * The starting points for the routes in an array of &#x60;[longitude,latitude]&#x60;. For instance, if you want to calculate three routes from point A such as A-&gt;1, A-&gt;2, A-&gt;3 then you have one &#x60;from_point&#x60; parameter and three &#x60;to_point&#x60; parameters.
   * @return fromPoints
   */
  @javax.annotation.Nullable
  public List<List<Double>> getFromPoints() {
    return fromPoints;
  }

  public void setFromPoints(List<List<Double>> fromPoints) {
    this.fromPoints = fromPoints;
  }


  public MatrixRequest outArrays(List<String> outArrays) {
    this.outArrays = outArrays;
    return this;
  }

  public MatrixRequest addOutArraysItem(String outArraysItem) {
    if (this.outArrays == null) {
      this.outArrays = new ArrayList<>();
    }
    this.outArrays.add(outArraysItem);
    return this;
  }

  /**
   * Specifies which matrices should be included in the response. Specify one or more of the following options &#x60;weights&#x60;, &#x60;times&#x60;, &#x60;distances&#x60;. The units of the entries of &#x60;distances&#x60; are meters, of &#x60;times&#x60; are seconds and of &#x60;weights&#x60; is arbitrary and it can differ for different vehicles or versions of this API.
   * @return outArrays
   */
  @javax.annotation.Nullable
  public List<String> getOutArrays() {
    return outArrays;
  }

  public void setOutArrays(List<String> outArrays) {
    this.outArrays = outArrays;
  }


  public MatrixRequest snapPreventions(List<String> snapPreventions) {
    this.snapPreventions = snapPreventions;
    return this;
  }

  public MatrixRequest addSnapPreventionsItem(String snapPreventionsItem) {
    if (this.snapPreventions == null) {
      this.snapPreventions = new ArrayList<>();
    }
    this.snapPreventions.add(snapPreventionsItem);
    return this;
  }

  /**
   * See &#x60;snap_preventions&#x60; of symmetrical matrix
   * @return snapPreventions
   */
  @javax.annotation.Nullable
  public List<String> getSnapPreventions() {
    return snapPreventions;
  }

  public void setSnapPreventions(List<String> snapPreventions) {
    this.snapPreventions = snapPreventions;
  }


  public MatrixRequest toCurbsides(List<String> toCurbsides) {
    this.toCurbsides = toCurbsides;
    return this;
  }

  public MatrixRequest addToCurbsidesItem(String toCurbsidesItem) {
    if (this.toCurbsides == null) {
      this.toCurbsides = new ArrayList<>();
    }
    this.toCurbsides.add(toCurbsidesItem);
    return this;
  }

  /**
   * See &#x60;curbsides&#x60;of symmetrical matrix
   * @return toCurbsides
   */
  @javax.annotation.Nullable
  public List<String> getToCurbsides() {
    return toCurbsides;
  }

  public void setToCurbsides(List<String> toCurbsides) {
    this.toCurbsides = toCurbsides;
  }


  public MatrixRequest toPointHints(List<String> toPointHints) {
    this.toPointHints = toPointHints;
    return this;
  }

  public MatrixRequest addToPointHintsItem(String toPointHintsItem) {
    if (this.toPointHints == null) {
      this.toPointHints = new ArrayList<>();
    }
    this.toPointHints.add(toPointHintsItem);
    return this;
  }

  /**
   * See &#x60;point_hints&#x60;of symmetrical matrix
   * @return toPointHints
   */
  @javax.annotation.Nullable
  public List<String> getToPointHints() {
    return toPointHints;
  }

  public void setToPointHints(List<String> toPointHints) {
    this.toPointHints = toPointHints;
  }


  public MatrixRequest toPoints(List<List<Double>> toPoints) {
    this.toPoints = toPoints;
    return this;
  }

  public MatrixRequest addToPointsItem(List<Double> toPointsItem) {
    if (this.toPoints == null) {
      this.toPoints = new ArrayList<>();
    }
    this.toPoints.add(toPointsItem);
    return this;
  }

  /**
   * The destination points for the routes in an array of &#x60;[longitude,latitude]&#x60;.
   * @return toPoints
   */
  @javax.annotation.Nullable
  public List<List<Double>> getToPoints() {
    return toPoints;
  }

  public void setToPoints(List<List<Double>> toPoints) {
    this.toPoints = toPoints;
  }


  public MatrixRequest turnCosts(Boolean turnCosts) {
    this.turnCosts = turnCosts;
    return this;
  }

  /**
   * Specifies if turn restrictions should be considered. Enabling this option increases the matrix computation time. Only supported for motor vehicles and OpenStreetMap.
   * @return turnCosts
   */
  @javax.annotation.Nullable
  public Boolean getTurnCosts() {
    return turnCosts;
  }

  public void setTurnCosts(Boolean turnCosts) {
    this.turnCosts = turnCosts;
  }


  public MatrixRequest vehicle(VehicleProfileId vehicle) {
    this.vehicle = vehicle;
    return this;
  }

  /**
   * Get vehicle
   * @return vehicle
   */
  @javax.annotation.Nullable
  public VehicleProfileId getVehicle() {
    return vehicle;
  }

  public void setVehicle(VehicleProfileId vehicle) {
    this.vehicle = vehicle;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MatrixRequest matrixRequest = (MatrixRequest) o;
    return Objects.equals(this.failFast, matrixRequest.failFast) &&
        Objects.equals(this.fromCurbsides, matrixRequest.fromCurbsides) &&
        Objects.equals(this.fromPointHints, matrixRequest.fromPointHints) &&
        Objects.equals(this.fromPoints, matrixRequest.fromPoints) &&
        Objects.equals(this.outArrays, matrixRequest.outArrays) &&
        Objects.equals(this.snapPreventions, matrixRequest.snapPreventions) &&
        Objects.equals(this.toCurbsides, matrixRequest.toCurbsides) &&
        Objects.equals(this.toPointHints, matrixRequest.toPointHints) &&
        Objects.equals(this.toPoints, matrixRequest.toPoints) &&
        Objects.equals(this.turnCosts, matrixRequest.turnCosts) &&
        Objects.equals(this.vehicle, matrixRequest.vehicle);
  }

  @Override
  public int hashCode() {
    return Objects.hash(failFast, fromCurbsides, fromPointHints, fromPoints, outArrays, snapPreventions, toCurbsides, toPointHints, toPoints, turnCosts, vehicle);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MatrixRequest {\n");
    sb.append("    failFast: ").append(toIndentedString(failFast)).append("\n");
    sb.append("    fromCurbsides: ").append(toIndentedString(fromCurbsides)).append("\n");
    sb.append("    fromPointHints: ").append(toIndentedString(fromPointHints)).append("\n");
    sb.append("    fromPoints: ").append(toIndentedString(fromPoints)).append("\n");
    sb.append("    outArrays: ").append(toIndentedString(outArrays)).append("\n");
    sb.append("    snapPreventions: ").append(toIndentedString(snapPreventions)).append("\n");
    sb.append("    toCurbsides: ").append(toIndentedString(toCurbsides)).append("\n");
    sb.append("    toPointHints: ").append(toIndentedString(toPointHints)).append("\n");
    sb.append("    toPoints: ").append(toIndentedString(toPoints)).append("\n");
    sb.append("    turnCosts: ").append(toIndentedString(turnCosts)).append("\n");
    sb.append("    vehicle: ").append(toIndentedString(vehicle)).append("\n");
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
    openapiFields.add("fail_fast");
    openapiFields.add("from_curbsides");
    openapiFields.add("from_point_hints");
    openapiFields.add("from_points");
    openapiFields.add("out_arrays");
    openapiFields.add("snap_preventions");
    openapiFields.add("to_curbsides");
    openapiFields.add("to_point_hints");
    openapiFields.add("to_points");
    openapiFields.add("turn_costs");
    openapiFields.add("vehicle");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to MatrixRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!MatrixRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in MatrixRequest is not found in the empty JSON string", MatrixRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!MatrixRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `MatrixRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("from_curbsides") != null && !jsonObj.get("from_curbsides").isJsonNull() && !jsonObj.get("from_curbsides").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `from_curbsides` to be an array in the JSON string but got `%s`", jsonObj.get("from_curbsides").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("from_point_hints") != null && !jsonObj.get("from_point_hints").isJsonNull() && !jsonObj.get("from_point_hints").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `from_point_hints` to be an array in the JSON string but got `%s`", jsonObj.get("from_point_hints").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("from_points") != null && !jsonObj.get("from_points").isJsonNull() && !jsonObj.get("from_points").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `from_points` to be an array in the JSON string but got `%s`", jsonObj.get("from_points").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("out_arrays") != null && !jsonObj.get("out_arrays").isJsonNull() && !jsonObj.get("out_arrays").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `out_arrays` to be an array in the JSON string but got `%s`", jsonObj.get("out_arrays").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("snap_preventions") != null && !jsonObj.get("snap_preventions").isJsonNull() && !jsonObj.get("snap_preventions").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `snap_preventions` to be an array in the JSON string but got `%s`", jsonObj.get("snap_preventions").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("to_curbsides") != null && !jsonObj.get("to_curbsides").isJsonNull() && !jsonObj.get("to_curbsides").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `to_curbsides` to be an array in the JSON string but got `%s`", jsonObj.get("to_curbsides").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("to_point_hints") != null && !jsonObj.get("to_point_hints").isJsonNull() && !jsonObj.get("to_point_hints").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `to_point_hints` to be an array in the JSON string but got `%s`", jsonObj.get("to_point_hints").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("to_points") != null && !jsonObj.get("to_points").isJsonNull() && !jsonObj.get("to_points").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `to_points` to be an array in the JSON string but got `%s`", jsonObj.get("to_points").toString()));
      }
      // validate the optional field `vehicle`
      if (jsonObj.get("vehicle") != null && !jsonObj.get("vehicle").isJsonNull()) {
        VehicleProfileId.validateJsonElement(jsonObj.get("vehicle"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!MatrixRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'MatrixRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<MatrixRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(MatrixRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<MatrixRequest>() {
           @Override
           public void write(JsonWriter out, MatrixRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public MatrixRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of MatrixRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of MatrixRequest
   * @throws IOException if the JSON string is invalid with respect to MatrixRequest
   */
  public static MatrixRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, MatrixRequest.class);
  }

  /**
   * Convert an instance of MatrixRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

