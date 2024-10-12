/*
 * Zapier Natural Language Actions (NLA) API - Beta
 * <img src=\"https://cdn.zappy.app/945f9bf9e44126873952ec5113949c3f.png\" width=\"100\" />  ## Hi, there! Welcome to the **Zapier Natural Language Actions API docs**. You are currently viewing the **root** API.  The endpoints of this **root** API are static and useful for reference. To see the live playground with dynamic API endpoints that match up to your own **actions**, [log in first](/login/zapier/), then go here:  **[NLA Dynamic API](/api/v1/dynamic/docs).**   ## Overview <a name=\"overview\"></a>  Zapier is an integration platform with over 5,000+ apps and 50,000+ actions. You can view the [full list here](https://zapier.com/apps). Zapier is used by millions of users, most of whom are non-technical builders -- but often savvy with software. Zapier offers several no code products to connect together the various apps on our platform. NLA exposes the same integrations Zapier uses to build our products, to you, to plug-in the capabilties of Zapier's platform into your own products.   For example, you can use the NLA API to: * Send messages in [Slack](https://zapier.com/apps/slack/integrations) * Add a row to a [Google Sheet](https://zapier.com/apps/google-sheets/integrations) * Draft a new email in [Gmail](https://zapier.com/apps/gmail/integrations) * ... and thousands more, with one universal natural language API  The typical use-case for NLA is to expose our ecosystem of thousands of apps/actions within your own product. NLA is optimized for products that receive user input in natural language (eg. chat, assistant, or other large language model based experience) -- that said, it can also be used to power _any_ product that needs integrations. In this case, think of NLA as a more friendly, human API.  NLA contains a decade of experience with API shenanigans, so you don't have to. Common API complexity, automatically handled: * **Every type of auth** (Basic, Session, API Key, OAuth v1, Oauth v2, Digest, ...), Zapier securely handles and signs requests for you * **Support for create, update, and search actions**, endpoints optimized for natural language usage * **Support for custom fields**, Spreadsheet, CRM, and Mailing List friendly! * **Reference by name, not ID**, humans use natural language names, not IDs, to reference things in their apps, so NLA does too * **Smart, human defaults**, APIs sometimes have 100 options. Zapier's platform data helps us make NLA simpler for users out of the box  #### Two Usage Modes <a name=\"usage-modes\"></a>  NLA handles all the underlying API auth and translation from natural language --> underlying API call --> return simplified output. The key idea is you (the developer), or your users, expose a set of actions via an oauth-like setup window, which you can then query and execute via a REST API. NLA offers both API Key and OAuth for signing NLA API requests.  1. **Server-side only** (API Key): for quickly getting started, testing, and production scenarios where your app will only use actions exposed in the developer's Zapier account (and will use the developer's connected accounts on Zapier.com)  2. **User-facing** (Oauth): for production scenarios where you are deploying an end-user facing application and your app needs access to end-user's exposed actions and connected accounts on Zapier.com  #### Why Natural Language?   Simply, it makes the API easier to use for both developers and users (and also for [large language models](https://en.wikipedia.org/wiki/Wikipedia:Large_language_models)!)  We designed NLA to expose the power of Zapier's platform without passing along the complexity. A few design choices: * There is a [user-facing component](https://cdn.zappy.app/83728f684b91c0afe7d435445fe4ac90.png) to NLA, exposed via a popup window, users set up and enable basic actions which \"expose\" them to you, the `provider`. * The default action setup for users is minimal and fast. [All required fields are guessed](https://cdn.zappy.app/20afede9be56bf4e30d31986bc5325f8.png). This guessing is accomplished using an lanuage model on the NLA side. * Users can [choose to override any guessed field](https://cdn.zappy.app/e07f6eabfe7512e9decf01cba0c9e847.png) with a fixed value or choice, increasing trust to use the natural language interface. * Custom fields (ex. spreadsheet columns) can also be [dynamically guessed at action run time](https://cdn.zappy.app/9061499b4b973200fc345f695b33e3c7.png), or fixed by the user.  Using the API is then simple:  ``` curl -v \\     -d '{\"instructions\": \"Add Bryan Helmig at Zapier to my NLA test sheet, oh and he loves guitars!\"}' \\     -H \"Authorization: Bearer <ACCESS_TOKEN>\" \\     -H \"Content-Type: application/json\" \\     'https://nla.zapier.com/api/v1/dynamic/exposed/<ACTION_ID>/execute/' ```  Or mix in some fixed values:  ``` curl -v \\     -d '{\"instructions\": \"Send a short poem about automation to slack\", \"channel\": \"#fun-zapier\"}' \\     -H \"Authorization: Bearer <ACCESS_TOKEN>\" \\     -H \"Content-Type: application/json\" \\     'https://nla.zapier.com/api/v1/dynamic/exposed/<ACTION_ID>/execute/' ```  ## Auth <a name=\"auth\"></a>  #### For Quickly Exploring <a name=\"exploring\"></a>  It's best to take advantage of session auth built into the OpenAPI docs.  1. [Log in](/login/zapier/) 2. [Create and enable an action](/demo/) using our `demo` provider  then all your enabled (\"exposed\") actions will be available at the bottom of the the **[dynamic API](/api/v1/dynamic/docs)**.  #### For Testing or Production (Server-side only mode) <a name=\"server-side\"></a>  For development purposes, or using NLA in a server-side only use case, you can get started quickly using the provider `dev`. You can generate an `API key` using this provider and make authenticated requests.  Please follow these steps:  1. Go to the [Dev App provider](/dev/provider/debug/) debug page. 2. Look for \"User\" -> \"Information\" -> \"API Key\". If a key does not exist, follow the instructions to generate one. 3. Use this key in the header `x-api-key` to make authenticated requests.  Test that the API key is working:  ``` curl -v \\     -H \"Content-Type: application/json\" \\     -H \"x-api-key: <API_KEY>\" \\     'https://nla.zapier.com/api/v1/check/' ```  #### For Production (User-facing mode) <a name=\"production\"></a>  The API is authenticated via [standard OAuth v2](https://oauth.net/2/). Submit [this form](https://share.hsforms.com/1DWkLQ7SpSZCuZbTxcBB98gck10t) to get access and receive a `cliend_id`, `client_secret`, and your `provider` name (ex. 'acme'). You'll also need to share with us a `redirect_uri` to receive each `code`. This API uses both `access_token` and `refresh_token`.  Each of your users will get a per-user access token which you'll use to sign requests. The access token both authenticates and authorizes a request to access or run (execute) a given user's actions.  The basic auth flow is:  1. **Send user to our OAuth start URL, ideally in a popup window**  ```javascript var url = https://nla.zapier.com/oauth/authorize/?     response_type=code&     client_id=<YOUR_CLIENT_ID>&     redirect_uri=<YOUR_REDIRECT_URI>&     scope=nla%3Aexposed_actions%3Aexecute var nla = window.open(url, 'nla', 'width=650,height=700'); ```  2. **User approves request for access**  3. **NLA will redirect user via `GET` to the `redirect_uri` you provided us with a `?code=` in the query string**  4. **Snag the `code` and `POST` it to the NLA token endpoint `https://nla.zapier.com/oauth/token/`**  ``` curl -v \\     -d '{ \\         \"code\": \"<CODE>\", \\         \"grant_type\": \"authorization_code\", \\         \"client_id\": \"<YOUR_CLIENT_ID>\", \\         \"client_secret\": \"<YOUR_CLIENT_SECRET>\" \\         }' \\     -H \"Content-Type: application/json\" \\     -X POST 'https://nla.zapier.com/oauth/token/' ```  5. **Finally, receive `refresh_token` and `access_token` in response**  Save the refresh token, you'll need to use it to request a new access tokehn when it expires.  Now you can use the `access_token` to make authenticated requests:  ``` curl -v -H \"Authorization: Bearer <ACCESS_TOKEN>\" https://nla.zapier.com/api/v1/dynamic/openapi.json ```  6. **When the `access_token` expires, refresh it**  ``` curl -v \\     -d '{ \\         \"refresh_token\": \"<REFRESH_TOKEN>\", \\         \"grant_type\": \"refresh_token\", \\         \"client_id\": \"<YOUR_CLIENT_ID>\", \\         \"client_secret\": \"<YOUR_CLIENT_SECRET>\" \\         }' \\     -H \"Content-Type: application/json\" \\     -X POST 'https://nla.zapier.com/oauth/token/' ```  ## Action Setup Window <a name=\"action-setup-window\"></a>  Users set up their actions inside a window popup, that looks and feels similar to an OAuth window. The setup URL is the same for all your users: `https://nla.zapier.com/<PROVIDER>/start/`  You can check the validity of an access/refresh token by checking against the `api/v1/check/` endpoint to determine if you should present the `oauth/authorize/` or `<PROVIDER>/start/` url.  You'd typically include a button or link somewhere inside your product to open the setup window.  ```javascript var nla = window.open('https://nla.zapier.com/<PROVIDER>/start', 'nla', 'width=650,height=700'); ```  _Note: the setup window is optimized for 650px width, 700px height_  ## Using the API <a name=\"using-the-api\"></a>  #### Understanding the AI guessing flow <a name=\"ai-guessing\"></a>  NLA is optimized for a chat/assistant style usage paradigm where you want to offload as much work to a large language model, as possible. For end users, the action setup flow that takes ~seconds (compared to minutes/hours with traditional, complex integration setup).  An action is then run (executed) via an API call with one single natural language parameter `instructions`. In the chat/assistant use case, these instructions are likely being generated by your own large language model. However NLA works just as well even in more traditional software paradigm where `instructions` are perhaps hard-coded into your codebase or supplied by the user directly.  Consider the case where you've built a chat product and your end user wants to expose a \"Send Slack Message\" action to your product. Their action setup [might look like this](https://cdn.zappy.app/d19215e5a2fb3896f6cddf435dfcbe27.png).  The user only has to pick Slack and authorize their Slack account. By default, all required fields are set to \"Have AI guess\". In this example there are two required fields: Channel and Message Text.  If a field uses \"Have AI guess\", two things happen: 1. When the action is run via the API, NLA will interpret passed `instructions` (using a language model) to fill in the values for Channel and Message Text. NLA is smart about fields like Channel -- Slack's API requires a Channel ID, not a plain text Channel name. NLA handles all such cases automatically. 2. The field will be listed as an optional hint parameter in the OpenAPI spec (see \"hint parameters\" below) which allows you (the developer) to override any `instructions` guessing.  Sometimes language models hallucinate or guess wrong. And if this were a particuarly sensitive Slack message, the user may not want to leave the selection of \"Channel\" up to chance. NLA allows the user [to use a specific, fixed value like this](https://cdn.zappy.app/dc4976635259b4889f8412d231fb3be4.png).  Now when the action executes, the Message Text will still be automatically guessed but Channel will be fixed to \"#testing\". This significantly increases user trust and unlocks use cases where the user may have partial but not full trust in an AI guessing.  We call the set of fields the user denoted \"Have AI guess\" as \"hint parameters\" -- Message Text above in the above example is one. They are *always* optional. When running actions via the API, you (the developer) can choose to supply none/any/all hint parameters. Any hint parameters provided are treated exactly like \"Use a specific value\" at the user layer -- as an override.   One aside: custom fields. Zapier supports custom fields throughout the platform. The degenerate case is a spreadsheet, where _every_ column is a custom field. This introduces complexity because sheet columns are unknowable at action setup time if the user picks \"Have AI guess\" for which spreadsheet. NLA handles such custom fields using the same pattern as above with one distinction: they are not listed as hint parameters because they are literally unknowable until run time. Also as you may expect, if the user picks a specific spreadsheet during action setup, custom fields act like regular fields and flow through normally.  In the typical chat/assistant product use case, you'll want to expose these hint parameters alongside the exposed action list to your own language model. Your language model is likely to have broader context about the user vs the narrowly constrained `instructions` string passed to the API and will result in a better guess.  In summary:  ``` [user supplied \"Use specific value\"] --overrides--> [API call supplied hint parameters] --overrides--> [API call supplied \"instructions\"] ```   #### Common API use cases <a name=\"common-api-uses\"></a>  There are three common usages: 1. Get a list of the current user's exposed actions 2. Get a list of an action's optional hint parameters 3. Execute an action  Let's go through each, assuming you have a valid access token already.  ### 1. Get a list of the current user's exposed actions <a name=\"list-exposed-actions\"></a>  ``` # via the RESTful list endpoint: curl -v -H \"Authorization: Bearer <ACCESS_TOKEN>\" https://nla.zapier.com/api/v1/dynamic/exposed/  # via the dynamic openapi.json schema: curl -v -H \"Authorization: Bearer <ACCESS_TOKEN>\" https://nla.zapier.com/api/v1/dynamic/openapi.json ```  Example of [full list endpoint response here](https://nla.zapier.com/api/v1/dynamic/exposed/), snipped below:  ``` {     \"results\": [         {             \"id\": \"01GTB1KMX72QTJEXXXXXXXXXX\",             \"description\": \"Slack: Send Channel Message\",             ... ```  Example of [full openapi.json response here](https://nla.zapier.com/api/v1/dynamic/openapi.json), snipped below:  ``` {     ...     \"paths\": {         ...         \"/api/v1/dynamic/exposed/01GTB1KMX72QTJEXXXXXXXXXX/execute/\": {             \"post\": {                 \"operationId\": \"exposed_01GTB1KMX72QTJEXXXXXXXXXX_execute\",                 \"summary\": \"Slack: Send Channel Message (execute)\",                 ...  ```  ### 2. Get a list of an action's optional hint parameters <a name=\"get-hints\"></a>  As a reminder, hint parameters are _always_ optional. By default, all parameters are filled in via guessing based on a provided `instructions` parameter. If a hint parameter is supplied in an API request along with instructions, the hint parameter will _override_ the guess.  ``` # via the RESTful list endpoint: curl -v -H \"Authorization: Bearer <ACCESS_TOKEN>\" https://nla.zapier.com/api/v1/dynamic/exposed/  # via the dynamic openapi.json schema: curl -v -H \"Authorization: Bearer <ACCESS_TOKEN>\" https://nla.zapier.com/api/v1/dynamic/openapi.json ```  Example of [full list endpoint response here](https://nla.zapier.com/api/v1/dynamic/exposed/), snipped below:  ``` {     \"results\": [         {             \"id\": \"01GTB1KMX72QTJEXXXXXXXXXX\",             \"description\": \"Slack: Send Channel Message\",             \"input_params\": {                 \"instructions\": \"str\",                 \"Message_Text\": \"str\",                 \"Channel\": \"str\",                 ... ```  Example of [full openapi.json response here](https://nla.zapier.com/api/v1/dynamic/openapi.json), snipped below:  ``` {     ...     \"components\": {         \"schemas\": {             ...             \"PreviewExecuteRequest_01GTB1KMX72QTJEXXXXXXXXXX\": {                 \"title\": \"PreviewExecuteRequest_01GTB1KMX72QTJEXXXXXXXXXX\",                 \"type\": \"object\",                 \"properties\": {                     \"instructions\": {                         ...                     },                     \"Message_Text\": {                         ...                     },                     \"Channel_Name\": {                         ...                     }  ```  _Note: Every list of input_params will contain `instructions`, the only required parameter for execution._   ### 3. Execute (or preview) an action <a name=\"execute-action\"></a>  Finally, with an action ID and any desired, optional, hint parameters in hand, we can run (execute) an action. The parameter `instructions` is the only required parameter run an action.  ``` curl -v \\     -d '{\"instructions\": \"send a short poem about automation and robots to slack\", \"Channel_Name\": \"#fun-zapier\"}' \\     -H \"Content-Type: application/json\" \\     -X POST 'https://nla.zapier.com/api/v1/dynamic/exposed/01GTB1KMX72QTJEXXXXXXXXXX/execute/' ```  Another example, this time an action to retrieve data:  ``` curl -v \\     -d '{\"instructions\": \"grab the latest email from bryan helmig\"}' \\     -H \"Content-Type: application/json\" \\     -X POST 'https://nla.zapier.com/api/v1/dynamic/exposed/01GTA3G1WD49GN1XXXXXXXXX/execute/' ```  One more example, this time requesting a preview of the action:  ``` curl -v \\     -d '{\"instructions\": \"say Hello World to #fun-zapier\", \"preview_only\": true}' \\     -H \"Content-Type: application/json\" \\     -X POST 'https://nla.zapier.com/api/v1/dynamic/exposed/01GTB1KMX72QTJEXXXXXXXXXX/execute/' ```   #### Execution Return Data <a name=\"return-data\"></a>  ##### The Status Key <a name=\"status-key\"></a>  All actions will contain a `status`. The status can be one of four values:  `success`  The action executed successfully and found results.  `error`  The action failed to execute. An `error` key will have its value populated.  Example:  ```     {         ...         \"action_used\": \"Gmail: Send Email\",         \"result\": null,         \"status\": \"error\",         \"error\": \"Error from app: Required field \"subject\" (subject) is missing. Required field \"Body\" (body) is missing.\"     } ```  `empty`  The action executed successfully, but no results were found. This status exists to be explicit that having an empty `result` is correct.  `preview`  The action is a preview and not a real execution. A `review_url` key will contain a URL to optionally execute the action from a browser, or just rerun without the `preview_only` input parameter.  Example:  ```     {         ...         \"action_used\": \"Slack: Send Channel Message\",         \"input_params\": {             \"Channel\": \"fun-zapier\",             \"Message_Text\": \"Hello World\"         },         \"review_url\": \"https://nla.zapier.com/execution/01GW2E2ZNE5W07D32E41HFT5GJ/?needs_confirmation=true\",         \"status\": \"preview\",     } ```  ##### The Result Key <a name=\"result-key\"></a>  All actions will return trimmed `result` data. `result` is ideal for humans and language models alike! By default, `full_results` is not included but can be useful for machines (contact us if you'd like access to full results). The trimmed version is created using some AI and heuristics:  * selects for data that is plain text and human readable * discards machine data like IDs, headers, etc. * prioritizes data that is very popular on Zapier * reduces final result into about ~500 words  Trimmed results are ideal for inserting directly back into the prompt context of a large language models without blowing up context token window limits.  Example of a trimmed results payload from \"Gmail: Find Email\":  ```     {         \"result\": {             \"from__email\": \"mike@zapier.com\",             \"from__name\": \"Mike Knoop\",             \"subject\": \"Re: Getting setup\",             \"body_plain\": \"Hi Karla, thanks for following up. I can confirm I got access to everything! ... Thanks! Mike\",             \"cc__emails\": \"bryan@zapier.com, wade@zapier.com\"             \"to__email\": \"Mike Knoop\",         }     } ``` ## Changelog <a name=\"changelog\"></a>  **Mar 20, 2023** Shipped two minor but breaking changes, and one other minor change to the API's response data:  * Route: `/api/v1/configuration-link/`   * Key `url` is now `configuration_link` **(breaking change)** * Route: `/api/v1/exposed/{exposed_app_action_id}/execute/`   * Key `rating_url` is now `review_url` **(breaking change)** * Route: `/api/v1/exposed/`   * Added `configuration_link` key
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client;

import okhttp3.*;
import okhttp3.internal.http.HttpMethod;
import okhttp3.internal.tls.OkHostnameVerifier;
import okhttp3.logging.HttpLoggingInterceptor;
import okhttp3.logging.HttpLoggingInterceptor.Level;
import okio.Buffer;
import okio.BufferedSink;
import okio.Okio;
import org.apache.oltu.oauth2.client.request.OAuthClientRequest.TokenRequestBuilder;
import org.apache.oltu.oauth2.common.message.types.GrantType;

import javax.net.ssl.*;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.lang.reflect.Type;
import java.net.URI;
import java.net.URLConnection;
import java.net.URLEncoder;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.GeneralSecurityException;
import java.security.KeyStore;
import java.security.SecureRandom;
import java.security.cert.Certificate;
import java.security.cert.CertificateException;
import java.security.cert.CertificateFactory;
import java.security.cert.X509Certificate;
import java.text.DateFormat;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.util.Map.Entry;
import java.util.concurrent.TimeUnit;
import java.util.function.Supplier;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.openapitools.client.auth.Authentication;
import org.openapitools.client.auth.HttpBasicAuth;
import org.openapitools.client.auth.HttpBearerAuth;
import org.openapitools.client.auth.ApiKeyAuth;
import org.openapitools.client.auth.OAuth;
import org.openapitools.client.auth.RetryingOAuth;
import org.openapitools.client.auth.OAuthFlow;

/**
 * <p>ApiClient class.</p>
 */
public class ApiClient {

    private String basePath = "https://nla.zapier.com";
    protected List<ServerConfiguration> servers = new ArrayList<ServerConfiguration>(Arrays.asList(
    new ServerConfiguration(
      "https://nla.zapier.com",
      "No description provided",
      new HashMap<String, ServerVariable>()
    )
  ));
    protected Integer serverIndex = 0;
    protected Map<String, String> serverVariables = null;
    private boolean debugging = false;
    private Map<String, String> defaultHeaderMap = new HashMap<String, String>();
    private Map<String, String> defaultCookieMap = new HashMap<String, String>();
    private String tempFolderPath = null;

    private Map<String, Authentication> authentications;

    private DateFormat dateFormat;
    private DateFormat datetimeFormat;
    private boolean lenientDatetimeFormat;
    private int dateLength;

    private InputStream sslCaCert;
    private boolean verifyingSsl;
    private KeyManager[] keyManagers;

    private OkHttpClient httpClient;
    private JSON json;

    private HttpLoggingInterceptor loggingInterceptor;

    /**
     * Basic constructor for ApiClient
     */
    public ApiClient() {
        init();
        initHttpClient();

        // Setup authentications (key: authentication name, value: authentication).
        authentications.put("AccessPointApiKeyHeader", new ApiKeyAuth("header", "X-API-Key"));
        authentications.put("AccessPointApiKeyQuery", new ApiKeyAuth("query", "api_key"));
        authentications.put("AccessPointOAuth", new OAuth());
        authentications.put("SessionAuth", new ApiKeyAuth("cookie", "sessionid"));
        // Prevent the authentications from being modified.
        authentications = Collections.unmodifiableMap(authentications);
    }

    /**
     * Basic constructor with custom OkHttpClient
     *
     * @param client a {@link okhttp3.OkHttpClient} object
     */
    public ApiClient(OkHttpClient client) {
        init();

        httpClient = client;

        // Setup authentications (key: authentication name, value: authentication).
        authentications.put("AccessPointApiKeyHeader", new ApiKeyAuth("header", "X-API-Key"));
        authentications.put("AccessPointApiKeyQuery", new ApiKeyAuth("query", "api_key"));
        authentications.put("AccessPointOAuth", new OAuth());
        authentications.put("SessionAuth", new ApiKeyAuth("cookie", "sessionid"));
        // Prevent the authentications from being modified.
        authentications = Collections.unmodifiableMap(authentications);
    }

    /**
     * Constructor for ApiClient to support access token retry on 401/403 configured with client ID
     *
     * @param clientId client ID
     */
    public ApiClient(String clientId) {
        this(clientId, null, null);
    }

    /**
     * Constructor for ApiClient to support access token retry on 401/403 configured with client ID and additional parameters
     *
     * @param clientId client ID
     * @param parameters a {@link java.util.Map} of parameters
     */
    public ApiClient(String clientId, Map<String, String> parameters) {
        this(clientId, null, parameters);
    }

    /**
     * Constructor for ApiClient to support access token retry on 401/403 configured with client ID, secret, and additional parameters
     *
     * @param clientId client ID
     * @param clientSecret client secret
     * @param parameters a {@link java.util.Map} of parameters
     */
    public ApiClient(String clientId, String clientSecret, Map<String, String> parameters) {
        this(null, clientId, clientSecret, parameters);
    }

    /**
     * Constructor for ApiClient to support access token retry on 401/403 configured with base path, client ID, secret, and additional parameters
     *
     * @param basePath base path
     * @param clientId client ID
     * @param clientSecret client secret
     * @param parameters a {@link java.util.Map} of parameters
     */
    public ApiClient(String basePath, String clientId, String clientSecret, Map<String, String> parameters) {
        init();
        if (basePath != null) {
            this.basePath = basePath;
        }

        String tokenUrl = "/oauth/token/";
        if (!"".equals(tokenUrl) && !URI.create(tokenUrl).isAbsolute()) {
            URI uri = URI.create(getBasePath());
            tokenUrl = uri.getScheme() + ":" +
                (uri.getAuthority() != null ? "//" + uri.getAuthority() : "") +
                tokenUrl;
            if (!URI.create(tokenUrl).isAbsolute()) {
                throw new IllegalArgumentException("OAuth2 token URL must be an absolute URL");
            }
        }
        RetryingOAuth retryingOAuth = new RetryingOAuth(tokenUrl, clientId, OAuthFlow.ACCESS_CODE, clientSecret, parameters);
        authentications.put(
                "AccessPointOAuth",
                retryingOAuth
        );
        initHttpClient(Collections.<Interceptor>singletonList(retryingOAuth));
        // Setup authentications (key: authentication name, value: authentication).
        authentications.put("AccessPointApiKeyHeader", new ApiKeyAuth("header", "X-API-Key"));
        authentications.put("AccessPointApiKeyQuery", new ApiKeyAuth("query", "api_key"));
        authentications.put("SessionAuth", new ApiKeyAuth("cookie", "sessionid"));

        // Prevent the authentications from being modified.
        authentications = Collections.unmodifiableMap(authentications);
    }

    private void initHttpClient() {
        initHttpClient(Collections.<Interceptor>emptyList());
    }

    private void initHttpClient(List<Interceptor> interceptors) {
        OkHttpClient.Builder builder = new OkHttpClient.Builder();
        builder.addNetworkInterceptor(getProgressInterceptor());
        for (Interceptor interceptor: interceptors) {
            builder.addInterceptor(interceptor);
        }

        httpClient = builder.build();
    }

    private void init() {
        verifyingSsl = true;

        json = new JSON();

        // Set default User-Agent.
        setUserAgent("OpenAPI-Generator/1.0.0/java");

        authentications = new HashMap<String, Authentication>();
    }

    /**
     * Get base path
     *
     * @return Base path
     */
    public String getBasePath() {
        return basePath;
    }

    /**
     * Set base path
     *
     * @param basePath Base path of the URL (e.g https://nla.zapier.com
     * @return An instance of OkHttpClient
     */
    public ApiClient setBasePath(String basePath) {
        this.basePath = basePath;
        this.serverIndex = null;
        return this;
    }

    public List<ServerConfiguration> getServers() {
        return servers;
    }

    public ApiClient setServers(List<ServerConfiguration> servers) {
        this.servers = servers;
        return this;
    }

    public Integer getServerIndex() {
        return serverIndex;
    }

    public ApiClient setServerIndex(Integer serverIndex) {
        this.serverIndex = serverIndex;
        return this;
    }

    public Map<String, String> getServerVariables() {
        return serverVariables;
    }

    public ApiClient setServerVariables(Map<String, String> serverVariables) {
        this.serverVariables = serverVariables;
        return this;
    }

    /**
     * Get HTTP client
     *
     * @return An instance of OkHttpClient
     */
    public OkHttpClient getHttpClient() {
        return httpClient;
    }

    /**
     * Set HTTP client, which must never be null.
     *
     * @param newHttpClient An instance of OkHttpClient
     * @return Api Client
     * @throws java.lang.NullPointerException when newHttpClient is null
     */
    public ApiClient setHttpClient(OkHttpClient newHttpClient) {
        this.httpClient = Objects.requireNonNull(newHttpClient, "HttpClient must not be null!");
        return this;
    }

    /**
     * Get JSON
     *
     * @return JSON object
     */
    public JSON getJSON() {
        return json;
    }

    /**
     * Set JSON
     *
     * @param json JSON object
     * @return Api client
     */
    public ApiClient setJSON(JSON json) {
        this.json = json;
        return this;
    }

    /**
     * True if isVerifyingSsl flag is on
     *
     * @return True if isVerifySsl flag is on
     */
    public boolean isVerifyingSsl() {
        return verifyingSsl;
    }

    /**
     * Configure whether to verify certificate and hostname when making https requests.
     * Default to true.
     * NOTE: Do NOT set to false in production code, otherwise you would face multiple types of cryptographic attacks.
     *
     * @param verifyingSsl True to verify TLS/SSL connection
     * @return ApiClient
     */
    public ApiClient setVerifyingSsl(boolean verifyingSsl) {
        this.verifyingSsl = verifyingSsl;
        applySslSettings();
        return this;
    }

    /**
     * Get SSL CA cert.
     *
     * @return Input stream to the SSL CA cert
     */
    public InputStream getSslCaCert() {
        return sslCaCert;
    }

    /**
     * Configure the CA certificate to be trusted when making https requests.
     * Use null to reset to default.
     *
     * @param sslCaCert input stream for SSL CA cert
     * @return ApiClient
     */
    public ApiClient setSslCaCert(InputStream sslCaCert) {
        this.sslCaCert = sslCaCert;
        applySslSettings();
        return this;
    }

    /**
     * <p>Getter for the field <code>keyManagers</code>.</p>
     *
     * @return an array of {@link javax.net.ssl.KeyManager} objects
     */
    public KeyManager[] getKeyManagers() {
        return keyManagers;
    }

    /**
     * Configure client keys to use for authorization in an SSL session.
     * Use null to reset to default.
     *
     * @param managers The KeyManagers to use
     * @return ApiClient
     */
    public ApiClient setKeyManagers(KeyManager[] managers) {
        this.keyManagers = managers;
        applySslSettings();
        return this;
    }

    /**
     * <p>Getter for the field <code>dateFormat</code>.</p>
     *
     * @return a {@link java.text.DateFormat} object
     */
    public DateFormat getDateFormat() {
        return dateFormat;
    }

    /**
     * <p>Setter for the field <code>dateFormat</code>.</p>
     *
     * @param dateFormat a {@link java.text.DateFormat} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setDateFormat(DateFormat dateFormat) {
        JSON.setDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set SqlDateFormat.</p>
     *
     * @param dateFormat a {@link java.text.DateFormat} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setSqlDateFormat(DateFormat dateFormat) {
        JSON.setSqlDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set OffsetDateTimeFormat.</p>
     *
     * @param dateFormat a {@link java.time.format.DateTimeFormatter} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setOffsetDateTimeFormat(DateTimeFormatter dateFormat) {
        JSON.setOffsetDateTimeFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set LocalDateFormat.</p>
     *
     * @param dateFormat a {@link java.time.format.DateTimeFormatter} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setLocalDateFormat(DateTimeFormatter dateFormat) {
        JSON.setLocalDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set LenientOnJson.</p>
     *
     * @param lenientOnJson a boolean
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setLenientOnJson(boolean lenientOnJson) {
        JSON.setLenientOnJson(lenientOnJson);
        return this;
    }

    /**
     * Get authentications (key: authentication name, value: authentication).
     *
     * @return Map of authentication objects
     */
    public Map<String, Authentication> getAuthentications() {
        return authentications;
    }

    /**
     * Get authentication for the given name.
     *
     * @param authName The authentication name
     * @return The authentication, null if not found
     */
    public Authentication getAuthentication(String authName) {
        return authentications.get(authName);
    }


    /**
     * Helper method to set username for the first HTTP basic authentication.
     *
     * @param username Username
     */
    public void setUsername(String username) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof HttpBasicAuth) {
                ((HttpBasicAuth) auth).setUsername(username);
                return;
            }
        }
        throw new RuntimeException("No HTTP basic authentication configured!");
    }

    /**
     * Helper method to set password for the first HTTP basic authentication.
     *
     * @param password Password
     */
    public void setPassword(String password) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof HttpBasicAuth) {
                ((HttpBasicAuth) auth).setPassword(password);
                return;
            }
        }
        throw new RuntimeException("No HTTP basic authentication configured!");
    }

    /**
     * Helper method to set API key value for the first API key authentication.
     *
     * @param apiKey API key
     */
    public void setApiKey(String apiKey) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof ApiKeyAuth) {
                ((ApiKeyAuth) auth).setApiKey(apiKey);
                return;
            }
        }
        throw new RuntimeException("No API key authentication configured!");
    }

    /**
     * Helper method to set API key prefix for the first API key authentication.
     *
     * @param apiKeyPrefix API key prefix
     */
    public void setApiKeyPrefix(String apiKeyPrefix) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof ApiKeyAuth) {
                ((ApiKeyAuth) auth).setApiKeyPrefix(apiKeyPrefix);
                return;
            }
        }
        throw new RuntimeException("No API key authentication configured!");
    }

    /**
     * Helper method to set access token for the first OAuth2 authentication.
     *
     * @param accessToken Access token
     */
    public void setAccessToken(String accessToken) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof OAuth) {
                ((OAuth) auth).setAccessToken(accessToken);
                return;
            }
        }
        throw new RuntimeException("No OAuth2 authentication configured!");
    }

    /**
     * Helper method to set credentials for AWSV4 Signature
     *
     * @param accessKey Access Key
     * @param secretKey Secret Key
     * @param region Region
     * @param service Service to access to
     */
    public void setAWS4Configuration(String accessKey, String secretKey, String region, String service) {
        throw new RuntimeException("No AWS4 authentication configured!");
    }

    /**
     * Helper method to set credentials for AWSV4 Signature
     *
     * @param accessKey Access Key
     * @param secretKey Secret Key
     * @param sessionToken Session Token
     * @param region Region
     * @param service Service to access to
     */
    public void setAWS4Configuration(String accessKey, String secretKey, String sessionToken, String region, String service) {
        throw new RuntimeException("No AWS4 authentication configured!");
    }

    /**
     * Set the User-Agent header's value (by adding to the default header map).
     *
     * @param userAgent HTTP request's user agent
     * @return ApiClient
     */
    public ApiClient setUserAgent(String userAgent) {
        addDefaultHeader("User-Agent", userAgent);
        return this;
    }

    /**
     * Add a default header.
     *
     * @param key The header's key
     * @param value The header's value
     * @return ApiClient
     */
    public ApiClient addDefaultHeader(String key, String value) {
        defaultHeaderMap.put(key, value);
        return this;
    }

    /**
     * Add a default cookie.
     *
     * @param key The cookie's key
     * @param value The cookie's value
     * @return ApiClient
     */
    public ApiClient addDefaultCookie(String key, String value) {
        defaultCookieMap.put(key, value);
        return this;
    }

    /**
     * Check that whether debugging is enabled for this API client.
     *
     * @return True if debugging is enabled, false otherwise.
     */
    public boolean isDebugging() {
        return debugging;
    }

    /**
     * Enable/disable debugging for this API client.
     *
     * @param debugging To enable (true) or disable (false) debugging
     * @return ApiClient
     */
    public ApiClient setDebugging(boolean debugging) {
        if (debugging != this.debugging) {
            if (debugging) {
                loggingInterceptor = new HttpLoggingInterceptor();
                loggingInterceptor.setLevel(Level.BODY);
                httpClient = httpClient.newBuilder().addInterceptor(loggingInterceptor).build();
            } else {
                final OkHttpClient.Builder builder = httpClient.newBuilder();
                builder.interceptors().remove(loggingInterceptor);
                httpClient = builder.build();
                loggingInterceptor = null;
            }
        }
        this.debugging = debugging;
        return this;
    }

    /**
     * The path of temporary folder used to store downloaded files from endpoints
     * with file response. The default value is <code>null</code>, i.e. using
     * the system's default temporary folder.
     *
     * @see <a href="https://docs.oracle.com/javase/7/docs/api/java/nio/file/Files.html#createTempFile(java.lang.String,%20java.lang.String,%20java.nio.file.attribute.FileAttribute...)">createTempFile</a>
     * @return Temporary folder path
     */
    public String getTempFolderPath() {
        return tempFolderPath;
    }

    /**
     * Set the temporary folder path (for downloading files)
     *
     * @param tempFolderPath Temporary folder path
     * @return ApiClient
     */
    public ApiClient setTempFolderPath(String tempFolderPath) {
        this.tempFolderPath = tempFolderPath;
        return this;
    }

    /**
     * Get connection timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getConnectTimeout() {
        return httpClient.connectTimeoutMillis();
    }

    /**
     * Sets the connect timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param connectionTimeout connection timeout in milliseconds
     * @return Api client
     */
    public ApiClient setConnectTimeout(int connectionTimeout) {
        httpClient = httpClient.newBuilder().connectTimeout(connectionTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }

    /**
     * Get read timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getReadTimeout() {
        return httpClient.readTimeoutMillis();
    }

    /**
     * Sets the read timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param readTimeout read timeout in milliseconds
     * @return Api client
     */
    public ApiClient setReadTimeout(int readTimeout) {
        httpClient = httpClient.newBuilder().readTimeout(readTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }

    /**
     * Get write timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getWriteTimeout() {
        return httpClient.writeTimeoutMillis();
    }

    /**
     * Sets the write timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param writeTimeout connection timeout in milliseconds
     * @return Api client
     */
    public ApiClient setWriteTimeout(int writeTimeout) {
        httpClient = httpClient.newBuilder().writeTimeout(writeTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }

    /**
     * Helper method to configure the token endpoint of the first oauth found in the apiAuthorizations (there should be only one)
     *
     * @return Token request builder
     */
    public TokenRequestBuilder getTokenEndPoint() {
        for (Authentication apiAuth : authentications.values()) {
            if (apiAuth instanceof RetryingOAuth) {
                RetryingOAuth retryingOAuth = (RetryingOAuth) apiAuth;
                return retryingOAuth.getTokenRequestBuilder();
            }
        }
        return null;
    }

    /**
     * Format the given parameter object into string.
     *
     * @param param Parameter
     * @return String representation of the parameter
     */
    public String parameterToString(Object param) {
        if (param == null) {
            return "";
        } else if (param instanceof Date || param instanceof OffsetDateTime || param instanceof LocalDate) {
            //Serialize to json string and remove the " enclosing characters
            String jsonStr = JSON.serialize(param);
            return jsonStr.substring(1, jsonStr.length() - 1);
        } else if (param instanceof Collection) {
            StringBuilder b = new StringBuilder();
            for (Object o : (Collection) param) {
                if (b.length() > 0) {
                    b.append(",");
                }
                b.append(o);
            }
            return b.toString();
        } else {
            return String.valueOf(param);
        }
    }

    /**
     * Formats the specified query parameter to a list containing a single {@code Pair} object.
     *
     * Note that {@code value} must not be a collection.
     *
     * @param name The name of the parameter.
     * @param value The value of the parameter.
     * @return A list containing a single {@code Pair} object.
     */
    public List<Pair> parameterToPair(String name, Object value) {
        List<Pair> params = new ArrayList<Pair>();

        // preconditions
        if (name == null || name.isEmpty() || value == null || value instanceof Collection) {
            return params;
        }

        params.add(new Pair(name, parameterToString(value)));
        return params;
    }

    /**
     * Formats the specified collection query parameters to a list of {@code Pair} objects.
     *
     * Note that the values of each of the returned Pair objects are percent-encoded.
     *
     * @param collectionFormat The collection format of the parameter.
     * @param name The name of the parameter.
     * @param value The value of the parameter.
     * @return A list of {@code Pair} objects.
     */
    public List<Pair> parameterToPairs(String collectionFormat, String name, Collection value) {
        List<Pair> params = new ArrayList<Pair>();

        // preconditions
        if (name == null || name.isEmpty() || value == null || value.isEmpty()) {
            return params;
        }

        // create the params based on the collection format
        if ("multi".equals(collectionFormat)) {
            for (Object item : value) {
                params.add(new Pair(name, escapeString(parameterToString(item))));
            }
            return params;
        }

        // collectionFormat is assumed to be "csv" by default
        String delimiter = ",";

        // escape all delimiters except commas, which are URI reserved
        // characters
        if ("ssv".equals(collectionFormat)) {
            delimiter = escapeString(" ");
        } else if ("tsv".equals(collectionFormat)) {
            delimiter = escapeString("\t");
        } else if ("pipes".equals(collectionFormat)) {
            delimiter = escapeString("|");
        }

        StringBuilder sb = new StringBuilder();
        for (Object item : value) {
            sb.append(delimiter);
            sb.append(escapeString(parameterToString(item)));
        }

        params.add(new Pair(name, sb.substring(delimiter.length())));

        return params;
    }

    /**
    * Formats the specified free-form query parameters to a list of {@code Pair} objects.
    *
    * @param value The free-form query parameters.
    * @return A list of {@code Pair} objects.
    */
    public List<Pair> freeFormParameterToPairs(Object value) {
        List<Pair> params = new ArrayList<>();

        // preconditions
        if (value == null || !(value instanceof Map )) {
            return params;
        }

        final Map<String, Object> valuesMap = (Map<String, Object>) value;

        for (Map.Entry<String, Object> entry : valuesMap.entrySet()) {
            params.add(new Pair(entry.getKey(), parameterToString(entry.getValue())));
        }

        return params;
    }


    /**
     * Formats the specified collection path parameter to a string value.
     *
     * @param collectionFormat The collection format of the parameter.
     * @param value The value of the parameter.
     * @return String representation of the parameter
     */
    public String collectionPathParameterToString(String collectionFormat, Collection value) {
        // create the value based on the collection format
        if ("multi".equals(collectionFormat)) {
            // not valid for path params
            return parameterToString(value);
        }

        // collectionFormat is assumed to be "csv" by default
        String delimiter = ",";

        if ("ssv".equals(collectionFormat)) {
            delimiter = " ";
        } else if ("tsv".equals(collectionFormat)) {
            delimiter = "\t";
        } else if ("pipes".equals(collectionFormat)) {
            delimiter = "|";
        }

        StringBuilder sb = new StringBuilder() ;
        for (Object item : value) {
            sb.append(delimiter);
            sb.append(parameterToString(item));
        }

        return sb.substring(delimiter.length());
    }

    /**
     * Sanitize filename by removing path.
     * e.g. ../../sun.gif becomes sun.gif
     *
     * @param filename The filename to be sanitized
     * @return The sanitized filename
     */
    public String sanitizeFilename(String filename) {
        return filename.replaceAll(".*[/\\\\]", "");
    }

    /**
     * Check if the given MIME is a JSON MIME.
     * JSON MIME examples:
     *   application/json
     *   application/json; charset=UTF8
     *   APPLICATION/JSON
     *   application/vnd.company+json
     * "* / *" is also default to JSON
     * @param mime MIME (Multipurpose Internet Mail Extensions)
     * @return True if the given MIME is JSON, false otherwise.
     */
    public boolean isJsonMime(String mime) {
        String jsonMime = "(?i)^(application/json|[^;/ \t]+/[^;/ \t]+[+]json)[ \t]*(;.*)?$";
        return mime != null && (mime.matches(jsonMime) || mime.equals("*/*"));
    }

    /**
     * Select the Accept header's value from the given accepts array:
     *   if JSON exists in the given array, use it;
     *   otherwise use all of them (joining into a string)
     *
     * @param accepts The accepts array to select from
     * @return The Accept header to use. If the given array is empty,
     *   null will be returned (not to set the Accept header explicitly).
     */
    public String selectHeaderAccept(String[] accepts) {
        if (accepts.length == 0) {
            return null;
        }
        for (String accept : accepts) {
            if (isJsonMime(accept)) {
                return accept;
            }
        }
        return StringUtil.join(accepts, ",");
    }

    /**
     * Select the Content-Type header's value from the given array:
     *   if JSON exists in the given array, use it;
     *   otherwise use the first one of the array.
     *
     * @param contentTypes The Content-Type array to select from
     * @return The Content-Type header to use. If the given array is empty,
     *   returns null. If it matches "any", JSON will be used.
     */
    public String selectHeaderContentType(String[] contentTypes) {
        if (contentTypes.length == 0) {
            return null;
        }

        if (contentTypes[0].equals("*/*")) {
            return "application/json";
        }

        for (String contentType : contentTypes) {
            if (isJsonMime(contentType)) {
                return contentType;
            }
        }

        return contentTypes[0];
    }

    /**
     * Escape the given string to be used as URL query value.
     *
     * @param str String to be escaped
     * @return Escaped string
     */
    public String escapeString(String str) {
        try {
            return URLEncoder.encode(str, "utf8").replaceAll("\\+", "%20");
        } catch (UnsupportedEncodingException e) {
            return str;
        }
    }

    /**
     * Deserialize response body to Java object, according to the return type and
     * the Content-Type response header.
     *
     * @param <T> Type
     * @param response HTTP response
     * @param returnType The type of the Java object
     * @return The deserialized Java object
     * @throws org.openapitools.client.ApiException If fail to deserialize response body, i.e. cannot read response body
     *   or the Content-Type of the response is not supported.
     */
    @SuppressWarnings("unchecked")
    public <T> T deserialize(Response response, Type returnType) throws ApiException {
        if (response == null || returnType == null) {
            return null;
        }

        if ("byte[]".equals(returnType.toString())) {
            // Handle binary response (byte array).
            try {
                return (T) response.body().bytes();
            } catch (IOException e) {
                throw new ApiException(e);
            }
        } else if (returnType.equals(File.class)) {
            // Handle file downloading.
            return (T) downloadFileFromResponse(response);
        }

        String respBody;
        try {
            if (response.body() != null)
                respBody = response.body().string();
            else
                respBody = null;
        } catch (IOException e) {
            throw new ApiException(e);
        }

        if (respBody == null || "".equals(respBody)) {
            return null;
        }

        String contentType = response.headers().get("Content-Type");
        if (contentType == null) {
            // ensuring a default content type
            contentType = "application/json";
        }
        if (isJsonMime(contentType)) {
            return JSON.deserialize(respBody, returnType);
        } else if (returnType.equals(String.class)) {
            // Expecting string, return the raw response body.
            return (T) respBody;
        } else {
            throw new ApiException(
                    "Content type \"" + contentType + "\" is not supported for type: " + returnType,
                    response.code(),
                    response.headers().toMultimap(),
                    respBody);
        }
    }

    /**
     * Serialize the given Java object into request body according to the object's
     * class and the request Content-Type.
     *
     * @param obj The Java object
     * @param contentType The request Content-Type
     * @return The serialized request body
     * @throws org.openapitools.client.ApiException If fail to serialize the given object
     */
    public RequestBody serialize(Object obj, String contentType) throws ApiException {
        if (obj instanceof byte[]) {
            // Binary (byte array) body parameter support.
            return RequestBody.create((byte[]) obj, MediaType.parse(contentType));
        } else if (obj instanceof File) {
            // File body parameter support.
            return RequestBody.create((File) obj, MediaType.parse(contentType));
        } else if ("text/plain".equals(contentType) && obj instanceof String) {
            return RequestBody.create((String) obj, MediaType.parse(contentType));
        } else if (isJsonMime(contentType)) {
            String content;
            if (obj != null) {
                content = JSON.serialize(obj);
            } else {
                content = null;
            }
            return RequestBody.create(content, MediaType.parse(contentType));
        } else if (obj instanceof String) {
            return RequestBody.create((String) obj, MediaType.parse(contentType));
        } else {
            throw new ApiException("Content type \"" + contentType + "\" is not supported");
        }
    }

    /**
     * Download file from the given response.
     *
     * @param response An instance of the Response object
     * @throws org.openapitools.client.ApiException If fail to read file content from response and write to disk
     * @return Downloaded file
     */
    public File downloadFileFromResponse(Response response) throws ApiException {
        try {
            File file = prepareDownloadFile(response);
            BufferedSink sink = Okio.buffer(Okio.sink(file));
            sink.writeAll(response.body().source());
            sink.close();
            return file;
        } catch (IOException e) {
            throw new ApiException(e);
        }
    }

    /**
     * Prepare file for download
     *
     * @param response An instance of the Response object
     * @return Prepared file for the download
     * @throws java.io.IOException If fail to prepare file for download
     */
    public File prepareDownloadFile(Response response) throws IOException {
        String filename = null;
        String contentDisposition = response.header("Content-Disposition");
        if (contentDisposition != null && !"".equals(contentDisposition)) {
            // Get filename from the Content-Disposition header.
            Pattern pattern = Pattern.compile("filename=['\"]?([^'\"\\s]+)['\"]?");
            Matcher matcher = pattern.matcher(contentDisposition);
            if (matcher.find()) {
                filename = sanitizeFilename(matcher.group(1));
            }
        }

        String prefix = null;
        String suffix = null;
        if (filename == null) {
            prefix = "download-";
            suffix = "";
        } else {
            int pos = filename.lastIndexOf(".");
            if (pos == -1) {
                prefix = filename + "-";
            } else {
                prefix = filename.substring(0, pos) + "-";
                suffix = filename.substring(pos);
            }
            // Files.createTempFile requires the prefix to be at least three characters long
            if (prefix.length() < 3)
                prefix = "download-";
        }

        if (tempFolderPath == null)
            return Files.createTempFile(prefix, suffix).toFile();
        else
            return Files.createTempFile(Paths.get(tempFolderPath), prefix, suffix).toFile();
    }

    /**
     * {@link #execute(Call, Type)}
     *
     * @param <T> Type
     * @param call An instance of the Call object
     * @return ApiResponse&lt;T&gt;
     * @throws org.openapitools.client.ApiException If fail to execute the call
     */
    public <T> ApiResponse<T> execute(Call call) throws ApiException {
        return execute(call, null);
    }

    /**
     * Execute HTTP call and deserialize the HTTP response body into the given return type.
     *
     * @param returnType The return type used to deserialize HTTP response body
     * @param <T> The return type corresponding to (same with) returnType
     * @param call Call
     * @return ApiResponse object containing response status, headers and
     *   data, which is a Java object deserialized from response body and would be null
     *   when returnType is null.
     * @throws org.openapitools.client.ApiException If fail to execute the call
     */
    public <T> ApiResponse<T> execute(Call call, Type returnType) throws ApiException {
        try {
            Response response = call.execute();
            T data = handleResponse(response, returnType);
            return new ApiResponse<T>(response.code(), response.headers().toMultimap(), data);
        } catch (IOException e) {
            throw new ApiException(e);
        }
    }

    /**
     * {@link #executeAsync(Call, Type, ApiCallback)}
     *
     * @param <T> Type
     * @param call An instance of the Call object
     * @param callback ApiCallback&lt;T&gt;
     */
    public <T> void executeAsync(Call call, ApiCallback<T> callback) {
        executeAsync(call, null, callback);
    }

    /**
     * Execute HTTP call asynchronously.
     *
     * @param <T> Type
     * @param call The callback to be executed when the API call finishes
     * @param returnType Return type
     * @param callback ApiCallback
     * @see #execute(Call, Type)
     */
    @SuppressWarnings("unchecked")
    public <T> void executeAsync(Call call, final Type returnType, final ApiCallback<T> callback) {
        call.enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                callback.onFailure(new ApiException(e), 0, null);
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                T result;
                try {
                    result = (T) handleResponse(response, returnType);
                } catch (ApiException e) {
                    callback.onFailure(e, response.code(), response.headers().toMultimap());
                    return;
                } catch (Exception e) {
                    callback.onFailure(new ApiException(e), response.code(), response.headers().toMultimap());
                    return;
                }
                callback.onSuccess(result, response.code(), response.headers().toMultimap());
            }
        });
    }

    /**
     * Handle the given response, return the deserialized object when the response is successful.
     *
     * @param <T> Type
     * @param response Response
     * @param returnType Return type
     * @return Type
     * @throws org.openapitools.client.ApiException If the response has an unsuccessful status code or
     *                      fail to deserialize the response body
     */
    public <T> T handleResponse(Response response, Type returnType) throws ApiException {
        if (response.isSuccessful()) {
            if (returnType == null || response.code() == 204) {
                // returning null if the returnType is not defined,
                // or the status code is 204 (No Content)
                if (response.body() != null) {
                    try {
                        response.body().close();
                    } catch (Exception e) {
                        throw new ApiException(response.message(), e, response.code(), response.headers().toMultimap());
                    }
                }
                return null;
            } else {
                return deserialize(response, returnType);
            }
        } else {
            String respBody = null;
            if (response.body() != null) {
                try {
                    respBody = response.body().string();
                } catch (IOException e) {
                    throw new ApiException(response.message(), e, response.code(), response.headers().toMultimap());
                }
            }
            throw new ApiException(response.message(), response.code(), response.headers().toMultimap(), respBody);
        }
    }

    /**
     * Build HTTP call with the given options.
     *
     * @param baseUrl The base URL
     * @param path The sub-path of the HTTP URL
     * @param method The request method, one of "GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH" and "DELETE"
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @param body The request body object
     * @param headerParams The header parameters
     * @param cookieParams The cookie parameters
     * @param formParams The form parameters
     * @param authNames The authentications to apply
     * @param callback Callback for upload/download progress
     * @return The HTTP call
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object
     */
    public Call buildCall(String baseUrl, String path, String method, List<Pair> queryParams, List<Pair> collectionQueryParams, Object body, Map<String, String> headerParams, Map<String, String> cookieParams, Map<String, Object> formParams, String[] authNames, ApiCallback callback) throws ApiException {
        Request request = buildRequest(baseUrl, path, method, queryParams, collectionQueryParams, body, headerParams, cookieParams, formParams, authNames, callback);

        return httpClient.newCall(request);
    }

    /**
     * Build an HTTP request with the given options.
     *
     * @param baseUrl The base URL
     * @param path The sub-path of the HTTP URL
     * @param method The request method, one of "GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH" and "DELETE"
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @param body The request body object
     * @param headerParams The header parameters
     * @param cookieParams The cookie parameters
     * @param formParams The form parameters
     * @param authNames The authentications to apply
     * @param callback Callback for upload/download progress
     * @return The HTTP request
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object
     */
    public Request buildRequest(String baseUrl, String path, String method, List<Pair> queryParams, List<Pair> collectionQueryParams, Object body, Map<String, String> headerParams, Map<String, String> cookieParams, Map<String, Object> formParams, String[] authNames, ApiCallback callback) throws ApiException {
        final String url = buildUrl(baseUrl, path, queryParams, collectionQueryParams);

        // prepare HTTP request body
        RequestBody reqBody;
        String contentType = headerParams.get("Content-Type");
        String contentTypePure = contentType;
        if (contentTypePure != null && contentTypePure.contains(";")) {
            contentTypePure = contentType.substring(0, contentType.indexOf(";"));
        }
        if (!HttpMethod.permitsRequestBody(method)) {
            reqBody = null;
        } else if ("application/x-www-form-urlencoded".equals(contentTypePure)) {
            reqBody = buildRequestBodyFormEncoding(formParams);
        } else if ("multipart/form-data".equals(contentTypePure)) {
            reqBody = buildRequestBodyMultipart(formParams);
        } else if (body == null) {
            if ("DELETE".equals(method)) {
                // allow calling DELETE without sending a request body
                reqBody = null;
            } else {
                // use an empty request body (for POST, PUT and PATCH)
                reqBody = RequestBody.create("", contentType == null ? null : MediaType.parse(contentType));
            }
        } else {
            reqBody = serialize(body, contentType);
        }

        List<Pair> updatedQueryParams = new ArrayList<>(queryParams);

        // update parameters with authentication settings
        updateParamsForAuth(authNames, updatedQueryParams, headerParams, cookieParams, requestBodyToString(reqBody), method, URI.create(url));

        final Request.Builder reqBuilder = new Request.Builder().url(buildUrl(baseUrl, path, updatedQueryParams, collectionQueryParams));
        processHeaderParams(headerParams, reqBuilder);
        processCookieParams(cookieParams, reqBuilder);

        // Associate callback with request (if not null) so interceptor can
        // access it when creating ProgressResponseBody
        reqBuilder.tag(callback);

        Request request = null;

        if (callback != null && reqBody != null) {
            ProgressRequestBody progressRequestBody = new ProgressRequestBody(reqBody, callback);
            request = reqBuilder.method(method, progressRequestBody).build();
        } else {
            request = reqBuilder.method(method, reqBody).build();
        }

        return request;
    }

    /**
     * Build full URL by concatenating base path, the given sub path and query parameters.
     *
     * @param baseUrl The base URL
     * @param path The sub path
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @return The full URL
     */
    public String buildUrl(String baseUrl, String path, List<Pair> queryParams, List<Pair> collectionQueryParams) {
        final StringBuilder url = new StringBuilder();
        if (baseUrl != null) {
            url.append(baseUrl).append(path);
        } else {
            String baseURL;
            if (serverIndex != null) {
                if (serverIndex < 0 || serverIndex >= servers.size()) {
                    throw new ArrayIndexOutOfBoundsException(String.format(
                    "Invalid index %d when selecting the host settings. Must be less than %d", serverIndex, servers.size()
                    ));
                }
                baseURL = servers.get(serverIndex).URL(serverVariables);
            } else {
                baseURL = basePath;
            }
            url.append(baseURL).append(path);
        }

        if (queryParams != null && !queryParams.isEmpty()) {
            // support (constant) query string in `path`, e.g. "/posts?draft=1"
            String prefix = path.contains("?") ? "&" : "?";
            for (Pair param : queryParams) {
                if (param.getValue() != null) {
                    if (prefix != null) {
                        url.append(prefix);
                        prefix = null;
                    } else {
                        url.append("&");
                    }
                    String value = parameterToString(param.getValue());
                    url.append(escapeString(param.getName())).append("=").append(escapeString(value));
                }
            }
        }

        if (collectionQueryParams != null && !collectionQueryParams.isEmpty()) {
            String prefix = url.toString().contains("?") ? "&" : "?";
            for (Pair param : collectionQueryParams) {
                if (param.getValue() != null) {
                    if (prefix != null) {
                        url.append(prefix);
                        prefix = null;
                    } else {
                        url.append("&");
                    }
                    String value = parameterToString(param.getValue());
                    // collection query parameter value already escaped as part of parameterToPairs
                    url.append(escapeString(param.getName())).append("=").append(value);
                }
            }
        }

        return url.toString();
    }

    /**
     * Set header parameters to the request builder, including default headers.
     *
     * @param headerParams Header parameters in the form of Map
     * @param reqBuilder Request.Builder
     */
    public void processHeaderParams(Map<String, String> headerParams, Request.Builder reqBuilder) {
        for (Entry<String, String> param : headerParams.entrySet()) {
            reqBuilder.header(param.getKey(), parameterToString(param.getValue()));
        }
        for (Entry<String, String> header : defaultHeaderMap.entrySet()) {
            if (!headerParams.containsKey(header.getKey())) {
                reqBuilder.header(header.getKey(), parameterToString(header.getValue()));
            }
        }
    }

    /**
     * Set cookie parameters to the request builder, including default cookies.
     *
     * @param cookieParams Cookie parameters in the form of Map
     * @param reqBuilder Request.Builder
     */
    public void processCookieParams(Map<String, String> cookieParams, Request.Builder reqBuilder) {
        for (Entry<String, String> param : cookieParams.entrySet()) {
            reqBuilder.addHeader("Cookie", String.format("%s=%s", param.getKey(), param.getValue()));
        }
        for (Entry<String, String> param : defaultCookieMap.entrySet()) {
            if (!cookieParams.containsKey(param.getKey())) {
                reqBuilder.addHeader("Cookie", String.format("%s=%s", param.getKey(), param.getValue()));
            }
        }
    }

    /**
     * Update query and header parameters based on authentication settings.
     *
     * @param authNames The authentications to apply
     * @param queryParams List of query parameters
     * @param headerParams Map of header parameters
     * @param cookieParams Map of cookie parameters
     * @param payload HTTP request body
     * @param method HTTP method
     * @param uri URI
     * @throws org.openapitools.client.ApiException If fails to update the parameters
     */
    public void updateParamsForAuth(String[] authNames, List<Pair> queryParams, Map<String, String> headerParams,
                                    Map<String, String> cookieParams, String payload, String method, URI uri) throws ApiException {
        for (String authName : authNames) {
            Authentication auth = authentications.get(authName);
            if (auth == null) {
                throw new RuntimeException("Authentication undefined: " + authName);
            }
            auth.applyToParams(queryParams, headerParams, cookieParams, payload, method, uri);
        }
    }

    /**
     * Build a form-encoding request body with the given form parameters.
     *
     * @param formParams Form parameters in the form of Map
     * @return RequestBody
     */
    public RequestBody buildRequestBodyFormEncoding(Map<String, Object> formParams) {
        okhttp3.FormBody.Builder formBuilder = new okhttp3.FormBody.Builder();
        for (Entry<String, Object> param : formParams.entrySet()) {
            formBuilder.add(param.getKey(), parameterToString(param.getValue()));
        }
        return formBuilder.build();
    }

    /**
     * Build a multipart (file uploading) request body with the given form parameters,
     * which could contain text fields and file fields.
     *
     * @param formParams Form parameters in the form of Map
     * @return RequestBody
     */
    public RequestBody buildRequestBodyMultipart(Map<String, Object> formParams) {
        MultipartBody.Builder mpBuilder = new MultipartBody.Builder().setType(MultipartBody.FORM);
        for (Entry<String, Object> param : formParams.entrySet()) {
            if (param.getValue() instanceof File) {
                File file = (File) param.getValue();
                addPartToMultiPartBuilder(mpBuilder, param.getKey(), file);
            } else if (param.getValue() instanceof List) {
                List list = (List) param.getValue();
                for (Object item: list) {
                    if (item instanceof File) {
                        addPartToMultiPartBuilder(mpBuilder, param.getKey(), (File) item);
                    } else {
                        addPartToMultiPartBuilder(mpBuilder, param.getKey(), param.getValue());
                    }
                }
            } else {
                addPartToMultiPartBuilder(mpBuilder, param.getKey(), param.getValue());
            }
        }
        return mpBuilder.build();
    }

    /**
     * Guess Content-Type header from the given file (defaults to "application/octet-stream").
     *
     * @param file The given file
     * @return The guessed Content-Type
     */
    public String guessContentTypeFromFile(File file) {
        String contentType = URLConnection.guessContentTypeFromName(file.getName());
        if (contentType == null) {
            return "application/octet-stream";
        } else {
            return contentType;
        }
    }

    /**
     * Add a Content-Disposition Header for the given key and file to the MultipartBody Builder.
     *
     * @param mpBuilder MultipartBody.Builder 
     * @param key The key of the Header element
     * @param file The file to add to the Header
     */ 
    private void addPartToMultiPartBuilder(MultipartBody.Builder mpBuilder, String key, File file) {
        Headers partHeaders = Headers.of("Content-Disposition", "form-data; name=\"" + key + "\"; filename=\"" + file.getName() + "\"");
        MediaType mediaType = MediaType.parse(guessContentTypeFromFile(file));
        mpBuilder.addPart(partHeaders, RequestBody.create(file, mediaType));
    }

    /**
     * Add a Content-Disposition Header for the given key and complex object to the MultipartBody Builder.
     *
     * @param mpBuilder MultipartBody.Builder
     * @param key The key of the Header element
     * @param obj The complex object to add to the Header
     */
    private void addPartToMultiPartBuilder(MultipartBody.Builder mpBuilder, String key, Object obj) {
        RequestBody requestBody;
        if (obj instanceof String) {
            requestBody = RequestBody.create((String) obj, MediaType.parse("text/plain"));
        } else {
            String content;
            if (obj != null) {
                content = JSON.serialize(obj);
            } else {
                content = null;
            }
            requestBody = RequestBody.create(content, MediaType.parse("application/json"));
        }

        Headers partHeaders = Headers.of("Content-Disposition", "form-data; name=\"" + key + "\"");
        mpBuilder.addPart(partHeaders, requestBody);
    }

    /**
     * Get network interceptor to add it to the httpClient to track download progress for
     * async requests.
     */
    private Interceptor getProgressInterceptor() {
        return new Interceptor() {
            @Override
            public Response intercept(Interceptor.Chain chain) throws IOException {
                final Request request = chain.request();
                final Response originalResponse = chain.proceed(request);
                if (request.tag() instanceof ApiCallback) {
                    final ApiCallback callback = (ApiCallback) request.tag();
                    return originalResponse.newBuilder()
                        .body(new ProgressResponseBody(originalResponse.body(), callback))
                        .build();
                }
                return originalResponse;
            }
        };
    }

    /**
     * Apply SSL related settings to httpClient according to the current values of
     * verifyingSsl and sslCaCert.
     */
    private void applySslSettings() {
        try {
            TrustManager[] trustManagers;
            HostnameVerifier hostnameVerifier;
            if (!verifyingSsl) {
                trustManagers = new TrustManager[]{
                        new X509TrustManager() {
                            @Override
                            public void checkClientTrusted(java.security.cert.X509Certificate[] chain, String authType) throws CertificateException {
                            }

                            @Override
                            public void checkServerTrusted(java.security.cert.X509Certificate[] chain, String authType) throws CertificateException {
                            }

                            @Override
                            public java.security.cert.X509Certificate[] getAcceptedIssuers() {
                                return new java.security.cert.X509Certificate[]{};
                            }
                        }
                };
                hostnameVerifier = new HostnameVerifier() {
                    @Override
                    public boolean verify(String hostname, SSLSession session) {
                        return true;
                    }
                };
            } else {
                TrustManagerFactory trustManagerFactory = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());

                if (sslCaCert == null) {
                    trustManagerFactory.init((KeyStore) null);
                } else {
                    char[] password = null; // Any password will work.
                    CertificateFactory certificateFactory = CertificateFactory.getInstance("X.509");
                    Collection<? extends Certificate> certificates = certificateFactory.generateCertificates(sslCaCert);
                    if (certificates.isEmpty()) {
                        throw new IllegalArgumentException("expected non-empty set of trusted certificates");
                    }
                    KeyStore caKeyStore = newEmptyKeyStore(password);
                    int index = 0;
                    for (Certificate certificate : certificates) {
                        String certificateAlias = "ca" + (index++);
                        caKeyStore.setCertificateEntry(certificateAlias, certificate);
                    }
                    trustManagerFactory.init(caKeyStore);
                }
                trustManagers = trustManagerFactory.getTrustManagers();
                hostnameVerifier = OkHostnameVerifier.INSTANCE;
            }

            SSLContext sslContext = SSLContext.getInstance("TLS");
            sslContext.init(keyManagers, trustManagers, new SecureRandom());
            httpClient = httpClient.newBuilder()
                            .sslSocketFactory(sslContext.getSocketFactory(), (X509TrustManager) trustManagers[0])
                            .hostnameVerifier(hostnameVerifier)
                            .build();
        } catch (GeneralSecurityException e) {
            throw new RuntimeException(e);
        }
    }

    private KeyStore newEmptyKeyStore(char[] password) throws GeneralSecurityException {
        try {
            KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
            keyStore.load(null, password);
            return keyStore;
        } catch (IOException e) {
            throw new AssertionError(e);
        }
    }

    /**
     * Convert the HTTP request body to a string.
     *
     * @param requestBody The HTTP request object
     * @return The string representation of the HTTP request body
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object into a string
     */
    private String requestBodyToString(RequestBody requestBody) throws ApiException {
        if (requestBody != null) {
            try {
                final Buffer buffer = new Buffer();
                requestBody.writeTo(buffer);
                return buffer.readUtf8();
            } catch (final IOException e) {
                throw new ApiException(e);
            }
        }

        // empty http request body
        return "";
    }
}
