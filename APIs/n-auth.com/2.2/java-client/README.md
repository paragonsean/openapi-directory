# openapi-java-client

nextAuth API
- API version: 2.2
  - Build date: 2024-10-12T09:57:02.089808-04:00[America/New_York]
  - Generator version: 7.9.0

API for the nextAuth server


*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>2.2</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:2.2"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-2.2.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    Integer accountid = 56; // Integer | Account id
    try {
      apiInstance.deleteAccount(serverid, accountid);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#deleteAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://api.nextauth.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**deleteAccount**](docs/AccountsApi.md#deleteAccount) | **DELETE** /servers/{serverid}/accounts/{accountid}/ | Delete specific account
*AccountsApi* | [**deleteUserAccounts_0**](docs/AccountsApi.md#deleteUserAccounts_0) | **DELETE** /servers/{serverid}/users/{userid}/accounts | Delete all accounts of a specific user
*AccountsApi* | [**getAccount**](docs/AccountsApi.md#getAccount) | **GET** /servers/{serverid}/accounts/{accountid}/ | Get specific account
*AccountsApi* | [**getAllAccounts**](docs/AccountsApi.md#getAllAccounts) | **GET** /servers/{serverid}/accounts/ | Get all accounts
*AccountsApi* | [**getUser_0**](docs/AccountsApi.md#getUser_0) | **GET** /servers/{serverid}/users/{userid}/accounts | Get all accounts of a specific user
*AccountsApi* | [**updateAccount**](docs/AccountsApi.md#updateAccount) | **PUT** /servers/{serverid}/accounts/{accountid}/ | Update specific account
*AccountsApi* | [**updateAccountUser**](docs/AccountsApi.md#updateAccountUser) | **PUT** /servers/{serverid}/accounts/{accountid}/user | Update user of the given account.
*GlobalApi* | [**deleteGlobalAttribute**](docs/GlobalApi.md#deleteGlobalAttribute) | **DELETE** /attributes/{attributekey} | Delete specific global attribute
*GlobalApi* | [**deleteGlobalAttributes**](docs/GlobalApi.md#deleteGlobalAttributes) | **DELETE** /attributes/ | Delete all global attributes
*GlobalApi* | [**deleteServerPrivilegedAttribute**](docs/GlobalApi.md#deleteServerPrivilegedAttribute) | **DELETE** /servers/{serverid}/privilegedattributes/{attributekey} | Delete specific privileged attribute of a specific server
*GlobalApi* | [**deleteServerPrivilegedAttributes**](docs/GlobalApi.md#deleteServerPrivilegedAttributes) | **DELETE** /servers/{serverid}/privilegedattributes/ | Delete all privileged attributes of a specific server
*GlobalApi* | [**getGlobalAttributes**](docs/GlobalApi.md#getGlobalAttributes) | **GET** /attributes/ | Get all global attributes
*GlobalApi* | [**getServerPrivilegedAttributes**](docs/GlobalApi.md#getServerPrivilegedAttributes) | **GET** /servers/{serverid}/privilegedattributes/ | Get all privileged attributes of a specific server
*GlobalApi* | [**setGlobalAttributes**](docs/GlobalApi.md#setGlobalAttributes) | **POST** /attributes/ | Set all global attributes
*GlobalApi* | [**setServerPrivilegedAttributes**](docs/GlobalApi.md#setServerPrivilegedAttributes) | **POST** /servers/{serverid}/privilegedattributes/ | Set all privileged attributes of a specific server
*GlobalApi* | [**updateGlobalAttributes**](docs/GlobalApi.md#updateGlobalAttributes) | **PUT** /attributes/ | Update specified global attributes
*GlobalApi* | [**updateServerPrivilegedAttributes**](docs/GlobalApi.md#updateServerPrivilegedAttributes) | **PUT** /servers/{serverid}/privilegedattributes/ | Update privileged specified attributes of a specific server
*HtmlApi* | [**getHtmlEnrol**](docs/HtmlApi.md#getHtmlEnrol) | **GET** /servers/{serverid}/sessions/html/enrol | Generate HTML to enrol a new user
*HtmlApi* | [**getHtmlFooter**](docs/HtmlApi.md#getHtmlFooter) | **GET** /servers/{serverid}/sessions/html/footer | Generic HTML to add to footer. Required for login/logout/enrol functionality.
*HtmlApi* | [**getHtmlLogin**](docs/HtmlApi.md#getHtmlLogin) | **GET** /servers/{serverid}/sessions/html/login | Generate HTML for the login block
*HtmlApi* | [**getSession_0**](docs/HtmlApi.md#getSession_0) | **GET** /servers/{serverid}/sessions/ | Check if the user is logged in
*HtmlApi* | [**logout_0**](docs/HtmlApi.md#logout_0) | **POST** /servers/{serverid}/sessions/logout | Force a logout on the given session
*ManagementApi* | [**createApiKey**](docs/ManagementApi.md#createApiKey) | **POST** /apikeys/ | Create a new API key.
*ManagementApi* | [**getAllPermissions**](docs/ManagementApi.md#getAllPermissions) | **GET** /servers/{serverid}/permissions/ | Get all permissions for the specified server.
*ManagementApi* | [**getApiKeys**](docs/ManagementApi.md#getApiKeys) | **GET** /apikeys/ | Get all API keys.
*ManagementApi* | [**getOrCreateUserRole**](docs/ManagementApi.md#getOrCreateUserRole) | **POST** /servers/{serverid}/users/{userid}/role/ | Get or create a role for a specific user.
*ManagementApi* | [**getPermissions**](docs/ManagementApi.md#getPermissions) | **GET** /servers/{serverid}/permissions/{roleid} | Get all permissions for the specified server and role.
*ManagementApi* | [**getUserRole**](docs/ManagementApi.md#getUserRole) | **GET** /servers/{serverid}/users/{userid}/role/ | Get role for a specific user.
*ManagementApi* | [**grantPermissions**](docs/ManagementApi.md#grantPermissions) | **POST** /servers/{serverid}/permissions/{roleid} | Set new permissions for the specified role on a server
*ManagementApi* | [**revokePermissions**](docs/ManagementApi.md#revokePermissions) | **DELETE** /servers/{serverid}/permissions/{roleid} | Revoke all permissions for the specified server and role.
*RegistrationApi* | [**getQrEnrol**](docs/RegistrationApi.md#getQrEnrol) | **GET** /servers/{serverid}/sessions/qr/enrol | Generate data for an enrol qr code
*RegistrationApi* | [**getServerVash**](docs/RegistrationApi.md#getServerVash) | **GET** /servers/{serverid}/vash | Visual hash of this server
*RegistrationApi* | [**registerUser_0**](docs/RegistrationApi.md#registerUser_0) | **POST** /servers/{serverid}/sessions/registeruser | Register a userid for the currently logged in account.
*RegistrationApi* | [**updateAccountUser_0**](docs/RegistrationApi.md#updateAccountUser_0) | **PUT** /servers/{serverid}/accounts/{accountid}/user | Update user of the given account.
*ServersApi* | [**createServer**](docs/ServersApi.md#createServer) | **POST** /servers/ | Create a new server
*ServersApi* | [**deleteServerAttribute**](docs/ServersApi.md#deleteServerAttribute) | **DELETE** /servers/{serverid}/attributes/{attributekey} | Delete specific attribute of a specific server
*ServersApi* | [**deleteServerAttributes**](docs/ServersApi.md#deleteServerAttributes) | **DELETE** /servers/{serverid}/attributes/ | Delete all attributes of a specific server
*ServersApi* | [**getServer**](docs/ServersApi.md#getServer) | **GET** /servers/{serverid}/ | Configuration of a specific server
*ServersApi* | [**getServerAttributes**](docs/ServersApi.md#getServerAttributes) | **GET** /servers/{serverid}/attributes/ | Get all attributes of a specific server
*ServersApi* | [**getServers**](docs/ServersApi.md#getServers) | **GET** /servers/ | List all your servers
*ServersApi* | [**setServerAttributes**](docs/ServersApi.md#setServerAttributes) | **POST** /servers/{serverid}/attributes/ | Set all attributes of a specific server
*ServersApi* | [**updateServer**](docs/ServersApi.md#updateServer) | **PUT** /servers/{serverid}/ | Update configuration of a specific server
*ServersApi* | [**updateServerAttributes**](docs/ServersApi.md#updateServerAttributes) | **PUT** /servers/{serverid}/attributes/ | Update specified attributes of a specific server
*SessionsApi* | [**getQrLogin**](docs/SessionsApi.md#getQrLogin) | **GET** /servers/{serverid}/sessions/qr/login | Generate data for a login qr code
*SessionsApi* | [**getSession**](docs/SessionsApi.md#getSession) | **GET** /servers/{serverid}/sessions/ | Check if the user is logged in
*SessionsApi* | [**logout**](docs/SessionsApi.md#logout) | **POST** /servers/{serverid}/sessions/logout | Force a logout on the given session
*SessionsApi* | [**provokeLogin**](docs/SessionsApi.md#provokeLogin) | **POST** /servers/{serverid}/sessions/provokelogin | Push a login confirmation to the user&#39;s app
*SessionsApi* | [**provokeLoginOnAccount**](docs/SessionsApi.md#provokeLoginOnAccount) | **POST** /servers/{serverid}/accounts/{accountid}/provokelogin | Push a login confirmation to the user&#39;s app
*SessionsApi* | [**provokeLoginOnUser**](docs/SessionsApi.md#provokeLoginOnUser) | **POST** /servers/{serverid}/users/{userid}/provokelogin | Push a login confirmation to the user&#39;s app
*TransactionsApi* | [**createTransaction**](docs/TransactionsApi.md#createTransaction) | **POST** /servers/{serverid}/sessions/transactions | Create a transaction to be approved within the current session.
*TransactionsApi* | [**getTransactionResult**](docs/TransactionsApi.md#getTransactionResult) | **GET** /servers/{serverid}/transactions/{transactionid} | Get transaction result for a given transaction.
*UsersApi* | [**deleteUser**](docs/UsersApi.md#deleteUser) | **DELETE** /servers/{serverid}/users/{userid}/ | Delete a specific user
*UsersApi* | [**deleteUserAccounts**](docs/UsersApi.md#deleteUserAccounts) | **DELETE** /servers/{serverid}/users/{userid}/accounts | Delete all accounts of a specific user
*UsersApi* | [**deleteUserAttribute**](docs/UsersApi.md#deleteUserAttribute) | **DELETE** /servers/{serverid}/users/{userid}/attributes/{attributekey} | Delete specific attribute of a specific user
*UsersApi* | [**deleteUserAttributes**](docs/UsersApi.md#deleteUserAttributes) | **DELETE** /servers/{serverid}/users/{userid}/attributes/ | Delete all attributes of a specific user
*UsersApi* | [**getUser**](docs/UsersApi.md#getUser) | **GET** /servers/{serverid}/users/{userid}/accounts | Get all accounts of a specific user
*UsersApi* | [**getUserAttributes**](docs/UsersApi.md#getUserAttributes) | **GET** /servers/{serverid}/users/{userid}/attributes/ | Get all attributes of a specific user
*UsersApi* | [**getUsers**](docs/UsersApi.md#getUsers) | **GET** /servers/{serverid}/users/ | Get all users
*UsersApi* | [**registerUser**](docs/UsersApi.md#registerUser) | **POST** /servers/{serverid}/sessions/registeruser | Register a userid for the currently logged in account.
*UsersApi* | [**setUserAttributes**](docs/UsersApi.md#setUserAttributes) | **POST** /servers/{serverid}/users/{userid}/attributes/ | Set all attributes of a specific user
*UsersApi* | [**updateUserAttributes**](docs/UsersApi.md#updateUserAttributes) | **PUT** /servers/{serverid}/users/{userid}/attributes/ | Update specified attributes of a specific user


## Documentation for Models

 - [Account](docs/Account.md)
 - [Accounts](docs/Accounts.md)
 - [ApiKey](docs/ApiKey.md)
 - [ApiKeys](docs/ApiKeys.md)
 - [GetOrCreateUserRole200Response](docs/GetOrCreateUserRole200Response.md)
 - [HtmlFooterBody](docs/HtmlFooterBody.md)
 - [LoginStatus](docs/LoginStatus.md)
 - [Permission](docs/Permission.md)
 - [Permissions](docs/Permissions.md)
 - [Role](docs/Role.md)
 - [Server](docs/Server.md)
 - [ServerSession](docs/ServerSession.md)
 - [Servers](docs/Servers.md)
 - [SessionInfo](docs/SessionInfo.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionId](docs/TransactionId.md)
 - [TransactionResult](docs/TransactionResult.md)
 - [User](docs/User.md)
 - [UserContext](docs/UserContext.md)
 - [Users](docs/Users.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="api_key"></a>
### api_key

- **Type**: API key
- **API key parameter name**: X-apikey
- **Location**: HTTP header

<a id="role_id"></a>
### role_id

- **Type**: API key
- **API key parameter name**: X-su
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



