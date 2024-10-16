/*
 * Carbone API
 * Carbone Cloud/On-premise Open API reference.  For requesting: - Carbone Cloud API: find your API key on your [Carbone account](https://account.carbone.io). Home page > Copy the `production` or `testing` API key. - Carbone On-premise: Update the `Server URL` on the Open API specification.  Useful links: - [API Flow](https://carbone.io/api-reference.html#quickstart-api-flow) - [Integration / SDKs](https://carbone.io/api-reference.html#api-integration) - [Generated document storage](https://carbone.io/api-reference.html#report-storage) - [Request timeout](https://carbone.io/api-reference.html#api-timeout)
 *
 * The version of the OpenAPI document: 1.2.0
 * Contact: support@carbone.io
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
