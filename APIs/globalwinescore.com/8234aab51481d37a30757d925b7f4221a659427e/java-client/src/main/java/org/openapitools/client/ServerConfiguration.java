/*
 * GlobalWineScore API Documentation
 *   The GlobalWineScore API is designed as a RESTful API, providing several resources and methods depending on your usage plan.  For further information please refer to <a href=\"https://www.globalwinescore.com/plans\" target=\"_blank\">our plans</a>.  # Authentication The API uses token-based authentication. In order to authenticate your requests, you need to include a specific header in each of your requests:  ``` Authorization: Token {YOUR-API-TOKEN} ``` The word <b>Token</b> must be written. Your requests must also use the <b>HTTPS</b> protocol.  If you don't have a token yet, you need to apply for one [here](https://www.globalwinescore.com/api/).  Your personal token can be found under the <a href=\"https://www.globalwinescore.com/account/api/\" target=\"_blank\">My account > API</a> section of the GlobalWineScore website  # Format The API provides several rendering formats which you can control using the `Accept` header or `format` query parameter.  - JSON (default): no header or `Accept: application/json` - XML: `Accept: application/xml` # Rate limiting For API requests, the rate limit allows for up to 10 requests per minute.  # Error handling  Whether a request succeeded is indicated by the HTTP status code. A 2xx status code indicates success, whereas a 4xx status code indicates failure.  When a request fails, the response body is still JSON, but always contains a `detail` field with a description of the error, which you can inspect for debugging.  For example, trying to access the API without proper authentication will return code 403 along with the message:  `{\"detail\": \"Authentication credentials were not provided.\"}`  Found a bug ? send us an email at <a href=\"mailto:api@globalwinescore.com\">api@globalwinescore.com</a>  # Ordering  At the moment, GlobalWineScores may be sorted by `date` and `score`. Use \"-\" to sort in descending order.  # Continuous synchronization  If you need to synchronize your database with our API, you can query our API using `?ordering=-date` to get the newest scores first, which means you won't have to crawl the whole catalog every time :-)  # Quick search interface If you need to search our catalog (e.g. to align it with yours), we're providing you with a handy interface accessible here: <a href=\"https://api.globalwinescore.com/search/\" target=\"_blank\">https://api.globalwinescore.com/search/</a>  You need to be logged in (email/password) to access this page, but other than that you can share it with anyone in your team and start searching right away !  # Resources  The details about available endpoints can be found below. You can click on each endpoint to find information about their parameters. 
 *
 * The version of the OpenAPI document: 8234aab51481d37a30757d925b7f4221a659427e
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client;

import java.util.Map;

/**
 * Representing a Server configuration.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:42.926406-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ServerConfiguration {
    public String URL;
    public String description;
    public Map<String, ServerVariable> variables;

    /**
     * @param URL A URL to the target host.
     * @param description A description of the host designated by the URL.
     * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
     */
    public ServerConfiguration(String URL, String description, Map<String, ServerVariable> variables) {
        this.URL = URL;
        this.description = description;
        this.variables = variables;
    }

    /**
     * Format URL template using given variables.
     *
     * @param variables A map between a variable name and its value.
     * @return Formatted URL.
     */
    public String URL(Map<String, String> variables) {
        String url = this.URL;

        // go through variables and replace placeholders
        for (Map.Entry<String, ServerVariable> variable: this.variables.entrySet()) {
            String name = variable.getKey();
            ServerVariable serverVariable = variable.getValue();
            String value = serverVariable.defaultValue;

            if (variables != null && variables.containsKey(name)) {
                value = variables.get(name);
                if (serverVariable.enumValues.size() > 0 && !serverVariable.enumValues.contains(value)) {
                    throw new IllegalArgumentException("The variable " + name + " in the server URL has invalid value " + value + ".");
                }
            }
            url = url.replace("{" + name + "}", value);
        }
        return url;
    }

    /**
     * Format URL template using default server variables.
     *
     * @return Formatted URL.
     */
    public String URL() {
        return URL(null);
    }
}
