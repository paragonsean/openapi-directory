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
import org.openapitools.client.model.Route;
import org.openapitools.client.model.SolutionUnassigned;

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
 * Only available if status field indicates &#x60;finished&#x60;.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:20.208084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Solution {
  public static final String SERIALIZED_NAME_COMPLETION_TIME = "completion_time";
  @SerializedName(SERIALIZED_NAME_COMPLETION_TIME)
  private Long completionTime;

  public static final String SERIALIZED_NAME_COSTS = "costs";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_COSTS)
  private Integer costs;

  public static final String SERIALIZED_NAME_DISTANCE = "distance";
  @SerializedName(SERIALIZED_NAME_DISTANCE)
  private Integer distance;

  public static final String SERIALIZED_NAME_MAX_OPERATION_TIME = "max_operation_time";
  @SerializedName(SERIALIZED_NAME_MAX_OPERATION_TIME)
  private Long maxOperationTime;

  public static final String SERIALIZED_NAME_NO_UNASSIGNED = "no_unassigned";
  @SerializedName(SERIALIZED_NAME_NO_UNASSIGNED)
  private Integer noUnassigned;

  public static final String SERIALIZED_NAME_NO_VEHICLES = "no_vehicles";
  @SerializedName(SERIALIZED_NAME_NO_VEHICLES)
  private Integer noVehicles;

  public static final String SERIALIZED_NAME_PREPARATION_TIME = "preparation_time";
  @SerializedName(SERIALIZED_NAME_PREPARATION_TIME)
  private Long preparationTime;

  public static final String SERIALIZED_NAME_ROUTES = "routes";
  @SerializedName(SERIALIZED_NAME_ROUTES)
  private List<Route> routes = new ArrayList<>();

  public static final String SERIALIZED_NAME_SERVICE_DURATION = "service_duration";
  @SerializedName(SERIALIZED_NAME_SERVICE_DURATION)
  private Long serviceDuration;

  public static final String SERIALIZED_NAME_TIME = "time";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_TIME)
  private Long time;

  public static final String SERIALIZED_NAME_TRANSPORT_TIME = "transport_time";
  @SerializedName(SERIALIZED_NAME_TRANSPORT_TIME)
  private Long transportTime;

  public static final String SERIALIZED_NAME_UNASSIGNED = "unassigned";
  @SerializedName(SERIALIZED_NAME_UNASSIGNED)
  private SolutionUnassigned unassigned;

  public static final String SERIALIZED_NAME_WAITING_TIME = "waiting_time";
  @SerializedName(SERIALIZED_NAME_WAITING_TIME)
  private Long waitingTime;

  public Solution() {
  }

  public Solution completionTime(Long completionTime) {
    this.completionTime = completionTime;
    return this;
  }

  /**
   * Overall completion time in seconds, i.e. the sum of each routes/drivers operation time.
   * @return completionTime
   */
  @javax.annotation.Nullable
  public Long getCompletionTime() {
    return completionTime;
  }

  public void setCompletionTime(Long completionTime) {
    this.completionTime = completionTime;
  }


  @Deprecated
  public Solution costs(Integer costs) {
    this.costs = costs;
    return this;
  }

  /**
   * Get costs
   * @return costs
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Integer getCosts() {
    return costs;
  }

  @Deprecated
  public void setCosts(Integer costs) {
    this.costs = costs;
  }


  public Solution distance(Integer distance) {
    this.distance = distance;
    return this;
  }

  /**
   * Overall distance travelled in meter, i.e. the sum of each route&#39;s transport distance
   * @return distance
   */
  @javax.annotation.Nullable
  public Integer getDistance() {
    return distance;
  }

  public void setDistance(Integer distance) {
    this.distance = distance;
  }


  public Solution maxOperationTime(Long maxOperationTime) {
    this.maxOperationTime = maxOperationTime;
    return this;
  }

  /**
   * Operation time of longest route in seconds.
   * @return maxOperationTime
   */
  @javax.annotation.Nullable
  public Long getMaxOperationTime() {
    return maxOperationTime;
  }

  public void setMaxOperationTime(Long maxOperationTime) {
    this.maxOperationTime = maxOperationTime;
  }


  public Solution noUnassigned(Integer noUnassigned) {
    this.noUnassigned = noUnassigned;
    return this;
  }

  /**
   * Number of jobs that could not be assigned to final solution.
   * @return noUnassigned
   */
  @javax.annotation.Nullable
  public Integer getNoUnassigned() {
    return noUnassigned;
  }

  public void setNoUnassigned(Integer noUnassigned) {
    this.noUnassigned = noUnassigned;
  }


  public Solution noVehicles(Integer noVehicles) {
    this.noVehicles = noVehicles;
    return this;
  }

  /**
   * Number of employed vehicles.
   * @return noVehicles
   */
  @javax.annotation.Nullable
  public Integer getNoVehicles() {
    return noVehicles;
  }

  public void setNoVehicles(Integer noVehicles) {
    this.noVehicles = noVehicles;
  }


  public Solution preparationTime(Long preparationTime) {
    this.preparationTime = preparationTime;
    return this;
  }

  /**
   * Overall preparation time in seconds.
   * @return preparationTime
   */
  @javax.annotation.Nullable
  public Long getPreparationTime() {
    return preparationTime;
  }

  public void setPreparationTime(Long preparationTime) {
    this.preparationTime = preparationTime;
  }


  public Solution routes(List<Route> routes) {
    this.routes = routes;
    return this;
  }

  public Solution addRoutesItem(Route routesItem) {
    if (this.routes == null) {
      this.routes = new ArrayList<>();
    }
    this.routes.add(routesItem);
    return this;
  }

  /**
   * An array of routes
   * @return routes
   */
  @javax.annotation.Nullable
  public List<Route> getRoutes() {
    return routes;
  }

  public void setRoutes(List<Route> routes) {
    this.routes = routes;
  }


  public Solution serviceDuration(Long serviceDuration) {
    this.serviceDuration = serviceDuration;
    return this;
  }

  /**
   * Overall service time in seconds.
   * @return serviceDuration
   */
  @javax.annotation.Nullable
  public Long getServiceDuration() {
    return serviceDuration;
  }

  public void setServiceDuration(Long serviceDuration) {
    this.serviceDuration = serviceDuration;
  }


  @Deprecated
  public Solution time(Long time) {
    this.time = time;
    return this;
  }

  /**
   * Use &#x60;transport_time&#x60; instead.
   * @return time
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Long getTime() {
    return time;
  }

  @Deprecated
  public void setTime(Long time) {
    this.time = time;
  }


  public Solution transportTime(Long transportTime) {
    this.transportTime = transportTime;
    return this;
  }

  /**
   * Overall time travelled in seconds, i.e. the sum of each route&#39;s transport time.
   * @return transportTime
   */
  @javax.annotation.Nullable
  public Long getTransportTime() {
    return transportTime;
  }

  public void setTransportTime(Long transportTime) {
    this.transportTime = transportTime;
  }


  public Solution unassigned(SolutionUnassigned unassigned) {
    this.unassigned = unassigned;
    return this;
  }

  /**
   * Get unassigned
   * @return unassigned
   */
  @javax.annotation.Nullable
  public SolutionUnassigned getUnassigned() {
    return unassigned;
  }

  public void setUnassigned(SolutionUnassigned unassigned) {
    this.unassigned = unassigned;
  }


  public Solution waitingTime(Long waitingTime) {
    this.waitingTime = waitingTime;
    return this;
  }

  /**
   * Overall waiting time in seconds.
   * @return waitingTime
   */
  @javax.annotation.Nullable
  public Long getWaitingTime() {
    return waitingTime;
  }

  public void setWaitingTime(Long waitingTime) {
    this.waitingTime = waitingTime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Solution solution = (Solution) o;
    return Objects.equals(this.completionTime, solution.completionTime) &&
        Objects.equals(this.costs, solution.costs) &&
        Objects.equals(this.distance, solution.distance) &&
        Objects.equals(this.maxOperationTime, solution.maxOperationTime) &&
        Objects.equals(this.noUnassigned, solution.noUnassigned) &&
        Objects.equals(this.noVehicles, solution.noVehicles) &&
        Objects.equals(this.preparationTime, solution.preparationTime) &&
        Objects.equals(this.routes, solution.routes) &&
        Objects.equals(this.serviceDuration, solution.serviceDuration) &&
        Objects.equals(this.time, solution.time) &&
        Objects.equals(this.transportTime, solution.transportTime) &&
        Objects.equals(this.unassigned, solution.unassigned) &&
        Objects.equals(this.waitingTime, solution.waitingTime);
  }

  @Override
  public int hashCode() {
    return Objects.hash(completionTime, costs, distance, maxOperationTime, noUnassigned, noVehicles, preparationTime, routes, serviceDuration, time, transportTime, unassigned, waitingTime);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Solution {\n");
    sb.append("    completionTime: ").append(toIndentedString(completionTime)).append("\n");
    sb.append("    costs: ").append(toIndentedString(costs)).append("\n");
    sb.append("    distance: ").append(toIndentedString(distance)).append("\n");
    sb.append("    maxOperationTime: ").append(toIndentedString(maxOperationTime)).append("\n");
    sb.append("    noUnassigned: ").append(toIndentedString(noUnassigned)).append("\n");
    sb.append("    noVehicles: ").append(toIndentedString(noVehicles)).append("\n");
    sb.append("    preparationTime: ").append(toIndentedString(preparationTime)).append("\n");
    sb.append("    routes: ").append(toIndentedString(routes)).append("\n");
    sb.append("    serviceDuration: ").append(toIndentedString(serviceDuration)).append("\n");
    sb.append("    time: ").append(toIndentedString(time)).append("\n");
    sb.append("    transportTime: ").append(toIndentedString(transportTime)).append("\n");
    sb.append("    unassigned: ").append(toIndentedString(unassigned)).append("\n");
    sb.append("    waitingTime: ").append(toIndentedString(waitingTime)).append("\n");
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
    openapiFields.add("completion_time");
    openapiFields.add("costs");
    openapiFields.add("distance");
    openapiFields.add("max_operation_time");
    openapiFields.add("no_unassigned");
    openapiFields.add("no_vehicles");
    openapiFields.add("preparation_time");
    openapiFields.add("routes");
    openapiFields.add("service_duration");
    openapiFields.add("time");
    openapiFields.add("transport_time");
    openapiFields.add("unassigned");
    openapiFields.add("waiting_time");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Solution
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Solution.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Solution is not found in the empty JSON string", Solution.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Solution.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Solution` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("routes") != null && !jsonObj.get("routes").isJsonNull()) {
        JsonArray jsonArrayroutes = jsonObj.getAsJsonArray("routes");
        if (jsonArrayroutes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("routes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `routes` to be an array in the JSON string but got `%s`", jsonObj.get("routes").toString()));
          }

          // validate the optional field `routes` (array)
          for (int i = 0; i < jsonArrayroutes.size(); i++) {
            Route.validateJsonElement(jsonArrayroutes.get(i));
          };
        }
      }
      // validate the optional field `unassigned`
      if (jsonObj.get("unassigned") != null && !jsonObj.get("unassigned").isJsonNull()) {
        SolutionUnassigned.validateJsonElement(jsonObj.get("unassigned"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Solution.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Solution' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Solution> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Solution.class));

       return (TypeAdapter<T>) new TypeAdapter<Solution>() {
           @Override
           public void write(JsonWriter out, Solution value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Solution read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Solution given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Solution
   * @throws IOException if the JSON string is invalid with respect to Solution
   */
  public static Solution fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Solution.class);
  }

  /**
   * Convert an instance of Solution to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

