/*
 * ODN API
 * The Socrata OpenDataNetwork (ODN) REST API exposes public data, often continuosly updated and enhanced, from many thousands of public government and non profit agencies.  Much of this data originating from independent sources is fused together to create new, and often powerful, entity level data. The API, in addition to search and autosuggest capabilities for finding datasets, enables data based comparisons across geographical regions such as states, counties, metropolitan areas, cities and zip codes using highly vetted data providers such as US Census, BEA, HUD and others. Comparison data is preformatted for easy and efficient display on a chart, graph or interactive map.  The API also exposes data organized by narrative style questions a human might ask. The questions can be rapidly found using an autosuggest style index, and then used to directly access all data needed to thoroughly and authoritatively answer the question. Retrieved data includes time series (temporally aligned), tabular, map heavy (includes spatial boundaries), and auto generated unstructured descriptive text.  The ODN API does not duplicate API endpoints or services provided by public sector agencies, but rather, returns context relevant pre-populated REST URLs, when appropriate, so the caller can access data directly from the source.  The [open source](http://github.com/socrata/odn-backend) API powers [OpenDataNetwork.com](http://OpenDataNetwork.com), an [open source](http://github.com/socrata/opendatanetwork.com) site; the site highlights myriad uses and provides API badges with contextually relevant API example REST endpoints and documentation pointers.  Finally, we continuously add new dat sources which appear automatically in the API, so if your favorite data source is not available, check back soon. You can also join us [HERE](http://www.opendatanetwork.com/join-open-data-network) and receive updates or let us know which data sources you are most interested in.  ## App Tokens  Registering for and including a [Socrata application token](https://dev.socrata.com/docs/app-tokens.html) is _required_ for the ODN API. They can be passed either using the `app_token` parameter or the `X-App-Token` HTTP header.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.auth;

import org.openapitools.client.ApiException;
import org.openapitools.client.Pair;

import java.net.URI;
import java.util.Map;
import java.util.List;

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:27.782808-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ApiKeyAuth implements Authentication {
  private final String location;
  private final String paramName;

  private String apiKey;
  private String apiKeyPrefix;

  public ApiKeyAuth(String location, String paramName) {
    this.location = location;
    this.paramName = paramName;
  }

  public String getLocation() {
    return location;
  }

  public String getParamName() {
    return paramName;
  }

  public String getApiKey() {
    return apiKey;
  }

  public void setApiKey(String apiKey) {
    this.apiKey = apiKey;
  }

  public String getApiKeyPrefix() {
    return apiKeyPrefix;
  }

  public void setApiKeyPrefix(String apiKeyPrefix) {
    this.apiKeyPrefix = apiKeyPrefix;
  }

  @Override
  public void applyToParams(List<Pair> queryParams, Map<String, String> headerParams, Map<String, String> cookieParams,
                           String payload, String method, URI uri) throws ApiException {
    if (apiKey == null) {
      return;
    }
    String value;
    if (apiKeyPrefix != null) {
      value = apiKeyPrefix + " " + apiKey;
    } else {
      value = apiKey;
    }
    if ("query".equals(location)) {
      queryParams.add(new Pair(paramName, value));
    } else if ("header".equals(location)) {
      headerParams.put(paramName, value);
    } else if ("cookie".equals(location)) {
      cookieParams.put(paramName, value);
    }
  }
}
