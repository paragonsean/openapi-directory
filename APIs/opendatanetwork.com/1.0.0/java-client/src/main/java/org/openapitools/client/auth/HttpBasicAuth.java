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

import org.openapitools.client.Pair;
import org.openapitools.client.ApiException;

import okhttp3.Credentials;

import java.net.URI;
import java.util.Map;
import java.util.List;

public class HttpBasicAuth implements Authentication {
    private String username;
    private String password;

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    @Override
    public void applyToParams(List<Pair> queryParams, Map<String, String> headerParams, Map<String, String> cookieParams,
                              String payload, String method, URI uri) throws ApiException {
        if (username == null && password == null) {
            return;
        }
        headerParams.put("Authorization", Credentials.basic(
            username == null ? "" : username,
            password == null ? "" : password));
    }
}
