/*
 * Google Home
 * # Google Home Local API This is an unofficial documentation of the local API used by the Home app to communicate with GH devices. [GitHub Repo](https://github.com/rithvikvibhu/GHLocalApi)  [![GitHub stars](https://img.shields.io/github/stars/rithvikvibhu/GHLocalApi)](https://github.com/rithvikvibhu/GHLocalApi/stargazers) [![GitHub license](https://img.shields.io/github/license/rithvikvibhu/GHLocalApi)](https://github.com/rithvikvibhu/GHLocalApi/blob/master/LICENSE.md)  ## Getting Started  Requests must be made over HTTPS, port 8443, so the base URL for these endpoints is: `https://<google-home-ip>:8443/setup/`  Get the IP of Google Home from the Google Home app (Device Settings -> End of the list) or from your router.  GET requests are simple, in the browser kind.   POST requests need to set the header (when there's a body): `content-type: application/json`  ## Authentication  Since June 2019, most requests (with exceptions like `/setup/eureka_info`) need a local authorization token.  There are 3 kinds of tokens involved here:  ### Local Authorization Token This token must be sent in all requests in the header `cast-local-authorization-token`. It is short-lived (~1 day) and may change unexpectedly (with a sync, change in homegraph, etc.) ##### Get this token - With access to an android device, [get this token directly by either method](https://gist.github.com/rithvikvibhu/1a0f4937af957ef6a78453e3be482c1f). - Without a device, or to integrate it with a script, use an access token to get the homegraph and extract the token. To get an access token, read the next section. Check the example section for more info.  ### Access Token This is a standard google oauth2 access token. It is in the form `ya29.***`. This gives access to the Google Home Foyer API. These expire in an hour. Use this to get the homegraph (and then the local authorization token above). ##### Get this token To get this access token, either a Google account username/password or a Google Master Token is needed. More info in the gist. Use the script [from this gist](https://gist.github.com/rithvikvibhu/952f83ea656c6782fbd0f1645059055d).  ### Master Token This is in the form `aas_et/_***` and can be used to request access tokens. ##### Get this token The same [script in the gist](https://gist.github.com/rithvikvibhu/952f83ea656c6782fbd0f1645059055d) that gets the access token can also get the master token. Needs Google account creds.  ## Example  Here's the whole flow from just a pair of username/password to using the local API.  Prerequisites: - [grpcurl](https://github.com/fullstorydev/grpcurl) - [Proto files](https://drive.google.com/drive/folders/1RvnN3y-G23pd2SWHmfV_7sef8QU5GNF4?usp=sharing) (preserve folder structure)  ### 1. Get an access token with the script - Download get_tokens.py - Fill in username and password ```sh python3 get_tokens.py # Note down the access token printed. ```  ### 2. Use the access token and get home graph - This prints the json and uses jq to parse and filter out the fields deviceName and localAuthToken - This will give a list of all devices and their local auth tokens ```sh ./grpcurl -H 'authorization: Bearer ya29.a0Af****' \\  -import-path /path/to/protos \\  -proto /path/to/protos/google/internal/home/foyer/v1.proto \\  googlehomefoyer-pa.googleapis.com:443 \\  google.internal.home.foyer.v1.StructuresService/GetHomeGraph | jq '.home.devices[] | {deviceName, localAuthToken}' # Note down the local auth token for the device you want. ```  ### 3. Make the call to the local device using the local auth token ```sh curl -H \"cast-local-authorization-token: LOCAL_AUTH_TOKEN\" --verbose --insecure https://192.168.0.18:8443/setup/bluetooth/status ```
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Example17;
import org.openapitools.client.model.NightModesettingsRequest;
import org.openapitools.client.model.RebootandFactoryResetRequest;
import org.openapitools.client.model.SetEurekaInfoRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DeviceSettingsApi
 */
@Disabled
public class DeviceSettingsApiTest {

    private final DeviceSettingsApi api = new DeviceSettingsApi();

    /**
     * Night Mode settings
     *
     * This sets night mode options.   To view currently set values, use /setup/eureka_info.   If &#x60;enabled&#x60; is set to false, night mode is disabled and the other values do not matter.   &#x60;led_brightness&#x60; and &#x60;volume&#x60; refer to the maximum LED Brightness and Volume that is set during night mode.   &#x60;demo_to_user&#x60; is always set to &#x60;true&#x60; so change in values will be visible in realtime (like brightness).   &#x60;windows&#x60;: A combination of &#x60;length_hours&#x60; and &#x60;start_hour&#x60; is used to define start and end times for night mode. In this example, night mode starts at 10 PM (22) and ends at 6 AM (8 hours later). &#x60;windows.days&#x60; is an array of days of week when night mode will be enabled. Example: 0-&gt;Sunday, 1-&gt; Monday, ..., 6-&gt;Saturday.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void nightModesettingsTest() throws ApiException {
        NightModesettingsRequest nightModesettingsRequest = null;
        Example17 response = api.nightModesettings(nightModesettingsRequest);
        // TODO: test validations
    }

    /**
     * Reboot and Factory Reset
     *
     * This can simply reboot the device (&#x60;params: \&quot;now\&quot;&#x60;) or factory reset the device (&#x60;params: \&quot;fdr\&quot;&#x60;).
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void rebootandFactoryResetTest() throws ApiException {
        RebootandFactoryResetRequest rebootandFactoryResetRequest = null;
        Object response = api.rebootandFactoryReset(rebootandFactoryResetRequest);
        // TODO: test validations
    }

    /**
     * Set Eureka Info
     *
     * This can set custom values to some options.  Only fields to be modified need to be sent, not all. The example has some modifiable fields.  TODO: List all modifiable fields.  Sending non-existant fields will still return a 200 OK, but they are not saved.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setEurekaInfoTest() throws ApiException {
        SetEurekaInfoRequest setEurekaInfoRequest = null;
        Object response = api.setEurekaInfo(setEurekaInfoRequest);
        // TODO: test validations
    }

}
