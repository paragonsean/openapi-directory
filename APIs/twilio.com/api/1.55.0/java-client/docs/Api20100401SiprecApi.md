# Api20100401SiprecApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSiprec**](Api20100401SiprecApi.md#createSiprec) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Siprec.json |  |
| [**updateSiprec**](Api20100401SiprecApi.md#updateSiprec) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Siprec/{Sid}.json |  |


<a id="createSiprec"></a>
# **createSiprec**
> ApiV2010AccountCallSiprec createSiprec(accountSid, callSid, connectorName, name, parameter1Name, parameter1Value, parameter10Name, parameter10Value, parameter11Name, parameter11Value, parameter12Name, parameter12Value, parameter13Name, parameter13Value, parameter14Name, parameter14Value, parameter15Name, parameter15Value, parameter16Name, parameter16Value, parameter17Name, parameter17Value, parameter18Name, parameter18Value, parameter19Name, parameter19Value, parameter2Name, parameter2Value, parameter20Name, parameter20Value, parameter21Name, parameter21Value, parameter22Name, parameter22Value, parameter23Name, parameter23Value, parameter24Name, parameter24Value, parameter25Name, parameter25Value, parameter26Name, parameter26Value, parameter27Name, parameter27Value, parameter28Name, parameter28Value, parameter29Name, parameter29Value, parameter3Name, parameter3Value, parameter30Name, parameter30Value, parameter31Name, parameter31Value, parameter32Name, parameter32Value, parameter33Name, parameter33Value, parameter34Name, parameter34Value, parameter35Name, parameter35Value, parameter36Name, parameter36Value, parameter37Name, parameter37Value, parameter38Name, parameter38Value, parameter39Name, parameter39Value, parameter4Name, parameter4Value, parameter40Name, parameter40Value, parameter41Name, parameter41Value, parameter42Name, parameter42Value, parameter43Name, parameter43Value, parameter44Name, parameter44Value, parameter45Name, parameter45Value, parameter46Name, parameter46Value, parameter47Name, parameter47Value, parameter48Name, parameter48Value, parameter49Name, parameter49Value, parameter5Name, parameter5Value, parameter50Name, parameter50Value, parameter51Name, parameter51Value, parameter52Name, parameter52Value, parameter53Name, parameter53Value, parameter54Name, parameter54Value, parameter55Name, parameter55Value, parameter56Name, parameter56Value, parameter57Name, parameter57Value, parameter58Name, parameter58Value, parameter59Name, parameter59Value, parameter6Name, parameter6Value, parameter60Name, parameter60Value, parameter61Name, parameter61Value, parameter62Name, parameter62Value, parameter63Name, parameter63Value, parameter64Name, parameter64Value, parameter65Name, parameter65Value, parameter66Name, parameter66Value, parameter67Name, parameter67Value, parameter68Name, parameter68Value, parameter69Name, parameter69Value, parameter7Name, parameter7Value, parameter70Name, parameter70Value, parameter71Name, parameter71Value, parameter72Name, parameter72Value, parameter73Name, parameter73Value, parameter74Name, parameter74Value, parameter75Name, parameter75Value, parameter76Name, parameter76Value, parameter77Name, parameter77Value, parameter78Name, parameter78Value, parameter79Name, parameter79Value, parameter8Name, parameter8Value, parameter80Name, parameter80Value, parameter81Name, parameter81Value, parameter82Name, parameter82Value, parameter83Name, parameter83Value, parameter84Name, parameter84Value, parameter85Name, parameter85Value, parameter86Name, parameter86Value, parameter87Name, parameter87Value, parameter88Name, parameter88Value, parameter89Name, parameter89Value, parameter9Name, parameter9Value, parameter90Name, parameter90Value, parameter91Name, parameter91Value, parameter92Name, parameter92Value, parameter93Name, parameter93Value, parameter94Name, parameter94Value, parameter95Name, parameter95Value, parameter96Name, parameter96Value, parameter97Name, parameter97Value, parameter98Name, parameter98Value, parameter99Name, parameter99Value, statusCallback, statusCallbackMethod, track)



Create a Siprec

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401SiprecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401SiprecApi apiInstance = new Api20100401SiprecApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Siprec resource.
    String callSid = "callSid_example"; // String | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Siprec resource is associated with.
    String connectorName = "connectorName_example"; // String | Unique name used when configuring the connector via Marketplace Add-on.
    String name = "name_example"; // String | The user-specified name of this Siprec, if one was given when the Siprec was created. This may be used to stop the Siprec.
    String parameter1Name = "parameter1Name_example"; // String | Parameter name
    String parameter1Value = "parameter1Value_example"; // String | Parameter value
    String parameter10Name = "parameter10Name_example"; // String | Parameter name
    String parameter10Value = "parameter10Value_example"; // String | Parameter value
    String parameter11Name = "parameter11Name_example"; // String | Parameter name
    String parameter11Value = "parameter11Value_example"; // String | Parameter value
    String parameter12Name = "parameter12Name_example"; // String | Parameter name
    String parameter12Value = "parameter12Value_example"; // String | Parameter value
    String parameter13Name = "parameter13Name_example"; // String | Parameter name
    String parameter13Value = "parameter13Value_example"; // String | Parameter value
    String parameter14Name = "parameter14Name_example"; // String | Parameter name
    String parameter14Value = "parameter14Value_example"; // String | Parameter value
    String parameter15Name = "parameter15Name_example"; // String | Parameter name
    String parameter15Value = "parameter15Value_example"; // String | Parameter value
    String parameter16Name = "parameter16Name_example"; // String | Parameter name
    String parameter16Value = "parameter16Value_example"; // String | Parameter value
    String parameter17Name = "parameter17Name_example"; // String | Parameter name
    String parameter17Value = "parameter17Value_example"; // String | Parameter value
    String parameter18Name = "parameter18Name_example"; // String | Parameter name
    String parameter18Value = "parameter18Value_example"; // String | Parameter value
    String parameter19Name = "parameter19Name_example"; // String | Parameter name
    String parameter19Value = "parameter19Value_example"; // String | Parameter value
    String parameter2Name = "parameter2Name_example"; // String | Parameter name
    String parameter2Value = "parameter2Value_example"; // String | Parameter value
    String parameter20Name = "parameter20Name_example"; // String | Parameter name
    String parameter20Value = "parameter20Value_example"; // String | Parameter value
    String parameter21Name = "parameter21Name_example"; // String | Parameter name
    String parameter21Value = "parameter21Value_example"; // String | Parameter value
    String parameter22Name = "parameter22Name_example"; // String | Parameter name
    String parameter22Value = "parameter22Value_example"; // String | Parameter value
    String parameter23Name = "parameter23Name_example"; // String | Parameter name
    String parameter23Value = "parameter23Value_example"; // String | Parameter value
    String parameter24Name = "parameter24Name_example"; // String | Parameter name
    String parameter24Value = "parameter24Value_example"; // String | Parameter value
    String parameter25Name = "parameter25Name_example"; // String | Parameter name
    String parameter25Value = "parameter25Value_example"; // String | Parameter value
    String parameter26Name = "parameter26Name_example"; // String | Parameter name
    String parameter26Value = "parameter26Value_example"; // String | Parameter value
    String parameter27Name = "parameter27Name_example"; // String | Parameter name
    String parameter27Value = "parameter27Value_example"; // String | Parameter value
    String parameter28Name = "parameter28Name_example"; // String | Parameter name
    String parameter28Value = "parameter28Value_example"; // String | Parameter value
    String parameter29Name = "parameter29Name_example"; // String | Parameter name
    String parameter29Value = "parameter29Value_example"; // String | Parameter value
    String parameter3Name = "parameter3Name_example"; // String | Parameter name
    String parameter3Value = "parameter3Value_example"; // String | Parameter value
    String parameter30Name = "parameter30Name_example"; // String | Parameter name
    String parameter30Value = "parameter30Value_example"; // String | Parameter value
    String parameter31Name = "parameter31Name_example"; // String | Parameter name
    String parameter31Value = "parameter31Value_example"; // String | Parameter value
    String parameter32Name = "parameter32Name_example"; // String | Parameter name
    String parameter32Value = "parameter32Value_example"; // String | Parameter value
    String parameter33Name = "parameter33Name_example"; // String | Parameter name
    String parameter33Value = "parameter33Value_example"; // String | Parameter value
    String parameter34Name = "parameter34Name_example"; // String | Parameter name
    String parameter34Value = "parameter34Value_example"; // String | Parameter value
    String parameter35Name = "parameter35Name_example"; // String | Parameter name
    String parameter35Value = "parameter35Value_example"; // String | Parameter value
    String parameter36Name = "parameter36Name_example"; // String | Parameter name
    String parameter36Value = "parameter36Value_example"; // String | Parameter value
    String parameter37Name = "parameter37Name_example"; // String | Parameter name
    String parameter37Value = "parameter37Value_example"; // String | Parameter value
    String parameter38Name = "parameter38Name_example"; // String | Parameter name
    String parameter38Value = "parameter38Value_example"; // String | Parameter value
    String parameter39Name = "parameter39Name_example"; // String | Parameter name
    String parameter39Value = "parameter39Value_example"; // String | Parameter value
    String parameter4Name = "parameter4Name_example"; // String | Parameter name
    String parameter4Value = "parameter4Value_example"; // String | Parameter value
    String parameter40Name = "parameter40Name_example"; // String | Parameter name
    String parameter40Value = "parameter40Value_example"; // String | Parameter value
    String parameter41Name = "parameter41Name_example"; // String | Parameter name
    String parameter41Value = "parameter41Value_example"; // String | Parameter value
    String parameter42Name = "parameter42Name_example"; // String | Parameter name
    String parameter42Value = "parameter42Value_example"; // String | Parameter value
    String parameter43Name = "parameter43Name_example"; // String | Parameter name
    String parameter43Value = "parameter43Value_example"; // String | Parameter value
    String parameter44Name = "parameter44Name_example"; // String | Parameter name
    String parameter44Value = "parameter44Value_example"; // String | Parameter value
    String parameter45Name = "parameter45Name_example"; // String | Parameter name
    String parameter45Value = "parameter45Value_example"; // String | Parameter value
    String parameter46Name = "parameter46Name_example"; // String | Parameter name
    String parameter46Value = "parameter46Value_example"; // String | Parameter value
    String parameter47Name = "parameter47Name_example"; // String | Parameter name
    String parameter47Value = "parameter47Value_example"; // String | Parameter value
    String parameter48Name = "parameter48Name_example"; // String | Parameter name
    String parameter48Value = "parameter48Value_example"; // String | Parameter value
    String parameter49Name = "parameter49Name_example"; // String | Parameter name
    String parameter49Value = "parameter49Value_example"; // String | Parameter value
    String parameter5Name = "parameter5Name_example"; // String | Parameter name
    String parameter5Value = "parameter5Value_example"; // String | Parameter value
    String parameter50Name = "parameter50Name_example"; // String | Parameter name
    String parameter50Value = "parameter50Value_example"; // String | Parameter value
    String parameter51Name = "parameter51Name_example"; // String | Parameter name
    String parameter51Value = "parameter51Value_example"; // String | Parameter value
    String parameter52Name = "parameter52Name_example"; // String | Parameter name
    String parameter52Value = "parameter52Value_example"; // String | Parameter value
    String parameter53Name = "parameter53Name_example"; // String | Parameter name
    String parameter53Value = "parameter53Value_example"; // String | Parameter value
    String parameter54Name = "parameter54Name_example"; // String | Parameter name
    String parameter54Value = "parameter54Value_example"; // String | Parameter value
    String parameter55Name = "parameter55Name_example"; // String | Parameter name
    String parameter55Value = "parameter55Value_example"; // String | Parameter value
    String parameter56Name = "parameter56Name_example"; // String | Parameter name
    String parameter56Value = "parameter56Value_example"; // String | Parameter value
    String parameter57Name = "parameter57Name_example"; // String | Parameter name
    String parameter57Value = "parameter57Value_example"; // String | Parameter value
    String parameter58Name = "parameter58Name_example"; // String | Parameter name
    String parameter58Value = "parameter58Value_example"; // String | Parameter value
    String parameter59Name = "parameter59Name_example"; // String | Parameter name
    String parameter59Value = "parameter59Value_example"; // String | Parameter value
    String parameter6Name = "parameter6Name_example"; // String | Parameter name
    String parameter6Value = "parameter6Value_example"; // String | Parameter value
    String parameter60Name = "parameter60Name_example"; // String | Parameter name
    String parameter60Value = "parameter60Value_example"; // String | Parameter value
    String parameter61Name = "parameter61Name_example"; // String | Parameter name
    String parameter61Value = "parameter61Value_example"; // String | Parameter value
    String parameter62Name = "parameter62Name_example"; // String | Parameter name
    String parameter62Value = "parameter62Value_example"; // String | Parameter value
    String parameter63Name = "parameter63Name_example"; // String | Parameter name
    String parameter63Value = "parameter63Value_example"; // String | Parameter value
    String parameter64Name = "parameter64Name_example"; // String | Parameter name
    String parameter64Value = "parameter64Value_example"; // String | Parameter value
    String parameter65Name = "parameter65Name_example"; // String | Parameter name
    String parameter65Value = "parameter65Value_example"; // String | Parameter value
    String parameter66Name = "parameter66Name_example"; // String | Parameter name
    String parameter66Value = "parameter66Value_example"; // String | Parameter value
    String parameter67Name = "parameter67Name_example"; // String | Parameter name
    String parameter67Value = "parameter67Value_example"; // String | Parameter value
    String parameter68Name = "parameter68Name_example"; // String | Parameter name
    String parameter68Value = "parameter68Value_example"; // String | Parameter value
    String parameter69Name = "parameter69Name_example"; // String | Parameter name
    String parameter69Value = "parameter69Value_example"; // String | Parameter value
    String parameter7Name = "parameter7Name_example"; // String | Parameter name
    String parameter7Value = "parameter7Value_example"; // String | Parameter value
    String parameter70Name = "parameter70Name_example"; // String | Parameter name
    String parameter70Value = "parameter70Value_example"; // String | Parameter value
    String parameter71Name = "parameter71Name_example"; // String | Parameter name
    String parameter71Value = "parameter71Value_example"; // String | Parameter value
    String parameter72Name = "parameter72Name_example"; // String | Parameter name
    String parameter72Value = "parameter72Value_example"; // String | Parameter value
    String parameter73Name = "parameter73Name_example"; // String | Parameter name
    String parameter73Value = "parameter73Value_example"; // String | Parameter value
    String parameter74Name = "parameter74Name_example"; // String | Parameter name
    String parameter74Value = "parameter74Value_example"; // String | Parameter value
    String parameter75Name = "parameter75Name_example"; // String | Parameter name
    String parameter75Value = "parameter75Value_example"; // String | Parameter value
    String parameter76Name = "parameter76Name_example"; // String | Parameter name
    String parameter76Value = "parameter76Value_example"; // String | Parameter value
    String parameter77Name = "parameter77Name_example"; // String | Parameter name
    String parameter77Value = "parameter77Value_example"; // String | Parameter value
    String parameter78Name = "parameter78Name_example"; // String | Parameter name
    String parameter78Value = "parameter78Value_example"; // String | Parameter value
    String parameter79Name = "parameter79Name_example"; // String | Parameter name
    String parameter79Value = "parameter79Value_example"; // String | Parameter value
    String parameter8Name = "parameter8Name_example"; // String | Parameter name
    String parameter8Value = "parameter8Value_example"; // String | Parameter value
    String parameter80Name = "parameter80Name_example"; // String | Parameter name
    String parameter80Value = "parameter80Value_example"; // String | Parameter value
    String parameter81Name = "parameter81Name_example"; // String | Parameter name
    String parameter81Value = "parameter81Value_example"; // String | Parameter value
    String parameter82Name = "parameter82Name_example"; // String | Parameter name
    String parameter82Value = "parameter82Value_example"; // String | Parameter value
    String parameter83Name = "parameter83Name_example"; // String | Parameter name
    String parameter83Value = "parameter83Value_example"; // String | Parameter value
    String parameter84Name = "parameter84Name_example"; // String | Parameter name
    String parameter84Value = "parameter84Value_example"; // String | Parameter value
    String parameter85Name = "parameter85Name_example"; // String | Parameter name
    String parameter85Value = "parameter85Value_example"; // String | Parameter value
    String parameter86Name = "parameter86Name_example"; // String | Parameter name
    String parameter86Value = "parameter86Value_example"; // String | Parameter value
    String parameter87Name = "parameter87Name_example"; // String | Parameter name
    String parameter87Value = "parameter87Value_example"; // String | Parameter value
    String parameter88Name = "parameter88Name_example"; // String | Parameter name
    String parameter88Value = "parameter88Value_example"; // String | Parameter value
    String parameter89Name = "parameter89Name_example"; // String | Parameter name
    String parameter89Value = "parameter89Value_example"; // String | Parameter value
    String parameter9Name = "parameter9Name_example"; // String | Parameter name
    String parameter9Value = "parameter9Value_example"; // String | Parameter value
    String parameter90Name = "parameter90Name_example"; // String | Parameter name
    String parameter90Value = "parameter90Value_example"; // String | Parameter value
    String parameter91Name = "parameter91Name_example"; // String | Parameter name
    String parameter91Value = "parameter91Value_example"; // String | Parameter value
    String parameter92Name = "parameter92Name_example"; // String | Parameter name
    String parameter92Value = "parameter92Value_example"; // String | Parameter value
    String parameter93Name = "parameter93Name_example"; // String | Parameter name
    String parameter93Value = "parameter93Value_example"; // String | Parameter value
    String parameter94Name = "parameter94Name_example"; // String | Parameter name
    String parameter94Value = "parameter94Value_example"; // String | Parameter value
    String parameter95Name = "parameter95Name_example"; // String | Parameter name
    String parameter95Value = "parameter95Value_example"; // String | Parameter value
    String parameter96Name = "parameter96Name_example"; // String | Parameter name
    String parameter96Value = "parameter96Value_example"; // String | Parameter value
    String parameter97Name = "parameter97Name_example"; // String | Parameter name
    String parameter97Value = "parameter97Value_example"; // String | Parameter value
    String parameter98Name = "parameter98Name_example"; // String | Parameter name
    String parameter98Value = "parameter98Value_example"; // String | Parameter value
    String parameter99Name = "parameter99Name_example"; // String | Parameter name
    String parameter99Value = "parameter99Value_example"; // String | Parameter value
    URI statusCallback = new URI(); // URI | Absolute URL of the status callback.
    String statusCallbackMethod = "HEAD"; // String | The http method for the status_callback (one of GET, POST).
    SiprecEnumTrack track = SiprecEnumTrack.fromValue("inbound_track"); // SiprecEnumTrack | 
    try {
      ApiV2010AccountCallSiprec result = apiInstance.createSiprec(accountSid, callSid, connectorName, name, parameter1Name, parameter1Value, parameter10Name, parameter10Value, parameter11Name, parameter11Value, parameter12Name, parameter12Value, parameter13Name, parameter13Value, parameter14Name, parameter14Value, parameter15Name, parameter15Value, parameter16Name, parameter16Value, parameter17Name, parameter17Value, parameter18Name, parameter18Value, parameter19Name, parameter19Value, parameter2Name, parameter2Value, parameter20Name, parameter20Value, parameter21Name, parameter21Value, parameter22Name, parameter22Value, parameter23Name, parameter23Value, parameter24Name, parameter24Value, parameter25Name, parameter25Value, parameter26Name, parameter26Value, parameter27Name, parameter27Value, parameter28Name, parameter28Value, parameter29Name, parameter29Value, parameter3Name, parameter3Value, parameter30Name, parameter30Value, parameter31Name, parameter31Value, parameter32Name, parameter32Value, parameter33Name, parameter33Value, parameter34Name, parameter34Value, parameter35Name, parameter35Value, parameter36Name, parameter36Value, parameter37Name, parameter37Value, parameter38Name, parameter38Value, parameter39Name, parameter39Value, parameter4Name, parameter4Value, parameter40Name, parameter40Value, parameter41Name, parameter41Value, parameter42Name, parameter42Value, parameter43Name, parameter43Value, parameter44Name, parameter44Value, parameter45Name, parameter45Value, parameter46Name, parameter46Value, parameter47Name, parameter47Value, parameter48Name, parameter48Value, parameter49Name, parameter49Value, parameter5Name, parameter5Value, parameter50Name, parameter50Value, parameter51Name, parameter51Value, parameter52Name, parameter52Value, parameter53Name, parameter53Value, parameter54Name, parameter54Value, parameter55Name, parameter55Value, parameter56Name, parameter56Value, parameter57Name, parameter57Value, parameter58Name, parameter58Value, parameter59Name, parameter59Value, parameter6Name, parameter6Value, parameter60Name, parameter60Value, parameter61Name, parameter61Value, parameter62Name, parameter62Value, parameter63Name, parameter63Value, parameter64Name, parameter64Value, parameter65Name, parameter65Value, parameter66Name, parameter66Value, parameter67Name, parameter67Value, parameter68Name, parameter68Value, parameter69Name, parameter69Value, parameter7Name, parameter7Value, parameter70Name, parameter70Value, parameter71Name, parameter71Value, parameter72Name, parameter72Value, parameter73Name, parameter73Value, parameter74Name, parameter74Value, parameter75Name, parameter75Value, parameter76Name, parameter76Value, parameter77Name, parameter77Value, parameter78Name, parameter78Value, parameter79Name, parameter79Value, parameter8Name, parameter8Value, parameter80Name, parameter80Value, parameter81Name, parameter81Value, parameter82Name, parameter82Value, parameter83Name, parameter83Value, parameter84Name, parameter84Value, parameter85Name, parameter85Value, parameter86Name, parameter86Value, parameter87Name, parameter87Value, parameter88Name, parameter88Value, parameter89Name, parameter89Value, parameter9Name, parameter9Value, parameter90Name, parameter90Value, parameter91Name, parameter91Value, parameter92Name, parameter92Value, parameter93Name, parameter93Value, parameter94Name, parameter94Value, parameter95Name, parameter95Value, parameter96Name, parameter96Value, parameter97Name, parameter97Value, parameter98Name, parameter98Value, parameter99Name, parameter99Value, statusCallback, statusCallbackMethod, track);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401SiprecApi#createSiprec");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Siprec resource. | |
| **callSid** | **String**| The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Siprec resource is associated with. | |
| **connectorName** | **String**| Unique name used when configuring the connector via Marketplace Add-on. | [optional] |
| **name** | **String**| The user-specified name of this Siprec, if one was given when the Siprec was created. This may be used to stop the Siprec. | [optional] |
| **parameter1Name** | **String**| Parameter name | [optional] |
| **parameter1Value** | **String**| Parameter value | [optional] |
| **parameter10Name** | **String**| Parameter name | [optional] |
| **parameter10Value** | **String**| Parameter value | [optional] |
| **parameter11Name** | **String**| Parameter name | [optional] |
| **parameter11Value** | **String**| Parameter value | [optional] |
| **parameter12Name** | **String**| Parameter name | [optional] |
| **parameter12Value** | **String**| Parameter value | [optional] |
| **parameter13Name** | **String**| Parameter name | [optional] |
| **parameter13Value** | **String**| Parameter value | [optional] |
| **parameter14Name** | **String**| Parameter name | [optional] |
| **parameter14Value** | **String**| Parameter value | [optional] |
| **parameter15Name** | **String**| Parameter name | [optional] |
| **parameter15Value** | **String**| Parameter value | [optional] |
| **parameter16Name** | **String**| Parameter name | [optional] |
| **parameter16Value** | **String**| Parameter value | [optional] |
| **parameter17Name** | **String**| Parameter name | [optional] |
| **parameter17Value** | **String**| Parameter value | [optional] |
| **parameter18Name** | **String**| Parameter name | [optional] |
| **parameter18Value** | **String**| Parameter value | [optional] |
| **parameter19Name** | **String**| Parameter name | [optional] |
| **parameter19Value** | **String**| Parameter value | [optional] |
| **parameter2Name** | **String**| Parameter name | [optional] |
| **parameter2Value** | **String**| Parameter value | [optional] |
| **parameter20Name** | **String**| Parameter name | [optional] |
| **parameter20Value** | **String**| Parameter value | [optional] |
| **parameter21Name** | **String**| Parameter name | [optional] |
| **parameter21Value** | **String**| Parameter value | [optional] |
| **parameter22Name** | **String**| Parameter name | [optional] |
| **parameter22Value** | **String**| Parameter value | [optional] |
| **parameter23Name** | **String**| Parameter name | [optional] |
| **parameter23Value** | **String**| Parameter value | [optional] |
| **parameter24Name** | **String**| Parameter name | [optional] |
| **parameter24Value** | **String**| Parameter value | [optional] |
| **parameter25Name** | **String**| Parameter name | [optional] |
| **parameter25Value** | **String**| Parameter value | [optional] |
| **parameter26Name** | **String**| Parameter name | [optional] |
| **parameter26Value** | **String**| Parameter value | [optional] |
| **parameter27Name** | **String**| Parameter name | [optional] |
| **parameter27Value** | **String**| Parameter value | [optional] |
| **parameter28Name** | **String**| Parameter name | [optional] |
| **parameter28Value** | **String**| Parameter value | [optional] |
| **parameter29Name** | **String**| Parameter name | [optional] |
| **parameter29Value** | **String**| Parameter value | [optional] |
| **parameter3Name** | **String**| Parameter name | [optional] |
| **parameter3Value** | **String**| Parameter value | [optional] |
| **parameter30Name** | **String**| Parameter name | [optional] |
| **parameter30Value** | **String**| Parameter value | [optional] |
| **parameter31Name** | **String**| Parameter name | [optional] |
| **parameter31Value** | **String**| Parameter value | [optional] |
| **parameter32Name** | **String**| Parameter name | [optional] |
| **parameter32Value** | **String**| Parameter value | [optional] |
| **parameter33Name** | **String**| Parameter name | [optional] |
| **parameter33Value** | **String**| Parameter value | [optional] |
| **parameter34Name** | **String**| Parameter name | [optional] |
| **parameter34Value** | **String**| Parameter value | [optional] |
| **parameter35Name** | **String**| Parameter name | [optional] |
| **parameter35Value** | **String**| Parameter value | [optional] |
| **parameter36Name** | **String**| Parameter name | [optional] |
| **parameter36Value** | **String**| Parameter value | [optional] |
| **parameter37Name** | **String**| Parameter name | [optional] |
| **parameter37Value** | **String**| Parameter value | [optional] |
| **parameter38Name** | **String**| Parameter name | [optional] |
| **parameter38Value** | **String**| Parameter value | [optional] |
| **parameter39Name** | **String**| Parameter name | [optional] |
| **parameter39Value** | **String**| Parameter value | [optional] |
| **parameter4Name** | **String**| Parameter name | [optional] |
| **parameter4Value** | **String**| Parameter value | [optional] |
| **parameter40Name** | **String**| Parameter name | [optional] |
| **parameter40Value** | **String**| Parameter value | [optional] |
| **parameter41Name** | **String**| Parameter name | [optional] |
| **parameter41Value** | **String**| Parameter value | [optional] |
| **parameter42Name** | **String**| Parameter name | [optional] |
| **parameter42Value** | **String**| Parameter value | [optional] |
| **parameter43Name** | **String**| Parameter name | [optional] |
| **parameter43Value** | **String**| Parameter value | [optional] |
| **parameter44Name** | **String**| Parameter name | [optional] |
| **parameter44Value** | **String**| Parameter value | [optional] |
| **parameter45Name** | **String**| Parameter name | [optional] |
| **parameter45Value** | **String**| Parameter value | [optional] |
| **parameter46Name** | **String**| Parameter name | [optional] |
| **parameter46Value** | **String**| Parameter value | [optional] |
| **parameter47Name** | **String**| Parameter name | [optional] |
| **parameter47Value** | **String**| Parameter value | [optional] |
| **parameter48Name** | **String**| Parameter name | [optional] |
| **parameter48Value** | **String**| Parameter value | [optional] |
| **parameter49Name** | **String**| Parameter name | [optional] |
| **parameter49Value** | **String**| Parameter value | [optional] |
| **parameter5Name** | **String**| Parameter name | [optional] |
| **parameter5Value** | **String**| Parameter value | [optional] |
| **parameter50Name** | **String**| Parameter name | [optional] |
| **parameter50Value** | **String**| Parameter value | [optional] |
| **parameter51Name** | **String**| Parameter name | [optional] |
| **parameter51Value** | **String**| Parameter value | [optional] |
| **parameter52Name** | **String**| Parameter name | [optional] |
| **parameter52Value** | **String**| Parameter value | [optional] |
| **parameter53Name** | **String**| Parameter name | [optional] |
| **parameter53Value** | **String**| Parameter value | [optional] |
| **parameter54Name** | **String**| Parameter name | [optional] |
| **parameter54Value** | **String**| Parameter value | [optional] |
| **parameter55Name** | **String**| Parameter name | [optional] |
| **parameter55Value** | **String**| Parameter value | [optional] |
| **parameter56Name** | **String**| Parameter name | [optional] |
| **parameter56Value** | **String**| Parameter value | [optional] |
| **parameter57Name** | **String**| Parameter name | [optional] |
| **parameter57Value** | **String**| Parameter value | [optional] |
| **parameter58Name** | **String**| Parameter name | [optional] |
| **parameter58Value** | **String**| Parameter value | [optional] |
| **parameter59Name** | **String**| Parameter name | [optional] |
| **parameter59Value** | **String**| Parameter value | [optional] |
| **parameter6Name** | **String**| Parameter name | [optional] |
| **parameter6Value** | **String**| Parameter value | [optional] |
| **parameter60Name** | **String**| Parameter name | [optional] |
| **parameter60Value** | **String**| Parameter value | [optional] |
| **parameter61Name** | **String**| Parameter name | [optional] |
| **parameter61Value** | **String**| Parameter value | [optional] |
| **parameter62Name** | **String**| Parameter name | [optional] |
| **parameter62Value** | **String**| Parameter value | [optional] |
| **parameter63Name** | **String**| Parameter name | [optional] |
| **parameter63Value** | **String**| Parameter value | [optional] |
| **parameter64Name** | **String**| Parameter name | [optional] |
| **parameter64Value** | **String**| Parameter value | [optional] |
| **parameter65Name** | **String**| Parameter name | [optional] |
| **parameter65Value** | **String**| Parameter value | [optional] |
| **parameter66Name** | **String**| Parameter name | [optional] |
| **parameter66Value** | **String**| Parameter value | [optional] |
| **parameter67Name** | **String**| Parameter name | [optional] |
| **parameter67Value** | **String**| Parameter value | [optional] |
| **parameter68Name** | **String**| Parameter name | [optional] |
| **parameter68Value** | **String**| Parameter value | [optional] |
| **parameter69Name** | **String**| Parameter name | [optional] |
| **parameter69Value** | **String**| Parameter value | [optional] |
| **parameter7Name** | **String**| Parameter name | [optional] |
| **parameter7Value** | **String**| Parameter value | [optional] |
| **parameter70Name** | **String**| Parameter name | [optional] |
| **parameter70Value** | **String**| Parameter value | [optional] |
| **parameter71Name** | **String**| Parameter name | [optional] |
| **parameter71Value** | **String**| Parameter value | [optional] |
| **parameter72Name** | **String**| Parameter name | [optional] |
| **parameter72Value** | **String**| Parameter value | [optional] |
| **parameter73Name** | **String**| Parameter name | [optional] |
| **parameter73Value** | **String**| Parameter value | [optional] |
| **parameter74Name** | **String**| Parameter name | [optional] |
| **parameter74Value** | **String**| Parameter value | [optional] |
| **parameter75Name** | **String**| Parameter name | [optional] |
| **parameter75Value** | **String**| Parameter value | [optional] |
| **parameter76Name** | **String**| Parameter name | [optional] |
| **parameter76Value** | **String**| Parameter value | [optional] |
| **parameter77Name** | **String**| Parameter name | [optional] |
| **parameter77Value** | **String**| Parameter value | [optional] |
| **parameter78Name** | **String**| Parameter name | [optional] |
| **parameter78Value** | **String**| Parameter value | [optional] |
| **parameter79Name** | **String**| Parameter name | [optional] |
| **parameter79Value** | **String**| Parameter value | [optional] |
| **parameter8Name** | **String**| Parameter name | [optional] |
| **parameter8Value** | **String**| Parameter value | [optional] |
| **parameter80Name** | **String**| Parameter name | [optional] |
| **parameter80Value** | **String**| Parameter value | [optional] |
| **parameter81Name** | **String**| Parameter name | [optional] |
| **parameter81Value** | **String**| Parameter value | [optional] |
| **parameter82Name** | **String**| Parameter name | [optional] |
| **parameter82Value** | **String**| Parameter value | [optional] |
| **parameter83Name** | **String**| Parameter name | [optional] |
| **parameter83Value** | **String**| Parameter value | [optional] |
| **parameter84Name** | **String**| Parameter name | [optional] |
| **parameter84Value** | **String**| Parameter value | [optional] |
| **parameter85Name** | **String**| Parameter name | [optional] |
| **parameter85Value** | **String**| Parameter value | [optional] |
| **parameter86Name** | **String**| Parameter name | [optional] |
| **parameter86Value** | **String**| Parameter value | [optional] |
| **parameter87Name** | **String**| Parameter name | [optional] |
| **parameter87Value** | **String**| Parameter value | [optional] |
| **parameter88Name** | **String**| Parameter name | [optional] |
| **parameter88Value** | **String**| Parameter value | [optional] |
| **parameter89Name** | **String**| Parameter name | [optional] |
| **parameter89Value** | **String**| Parameter value | [optional] |
| **parameter9Name** | **String**| Parameter name | [optional] |
| **parameter9Value** | **String**| Parameter value | [optional] |
| **parameter90Name** | **String**| Parameter name | [optional] |
| **parameter90Value** | **String**| Parameter value | [optional] |
| **parameter91Name** | **String**| Parameter name | [optional] |
| **parameter91Value** | **String**| Parameter value | [optional] |
| **parameter92Name** | **String**| Parameter name | [optional] |
| **parameter92Value** | **String**| Parameter value | [optional] |
| **parameter93Name** | **String**| Parameter name | [optional] |
| **parameter93Value** | **String**| Parameter value | [optional] |
| **parameter94Name** | **String**| Parameter name | [optional] |
| **parameter94Value** | **String**| Parameter value | [optional] |
| **parameter95Name** | **String**| Parameter name | [optional] |
| **parameter95Value** | **String**| Parameter value | [optional] |
| **parameter96Name** | **String**| Parameter name | [optional] |
| **parameter96Value** | **String**| Parameter value | [optional] |
| **parameter97Name** | **String**| Parameter name | [optional] |
| **parameter97Value** | **String**| Parameter value | [optional] |
| **parameter98Name** | **String**| Parameter name | [optional] |
| **parameter98Value** | **String**| Parameter value | [optional] |
| **parameter99Name** | **String**| Parameter name | [optional] |
| **parameter99Value** | **String**| Parameter value | [optional] |
| **statusCallback** | **URI**| Absolute URL of the status callback. | [optional] |
| **statusCallbackMethod** | **String**| The http method for the status_callback (one of GET, POST). | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **track** | **SiprecEnumTrack**|  | [optional] [enum: inbound_track, outbound_track, both_tracks] |

### Return type

[**ApiV2010AccountCallSiprec**](ApiV2010AccountCallSiprec.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="updateSiprec"></a>
# **updateSiprec**
> ApiV2010AccountCallSiprec updateSiprec(accountSid, callSid, sid, status)



Stop a Siprec using either the SID of the Siprec resource or the &#x60;name&#x60; used when creating the resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401SiprecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401SiprecApi apiInstance = new Api20100401SiprecApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Siprec resource.
    String callSid = "callSid_example"; // String | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Siprec resource is associated with.
    String sid = "sid_example"; // String | The SID of the Siprec resource, or the `name` used when creating the resource
    SiprecEnumUpdateStatus status = SiprecEnumUpdateStatus.fromValue("stopped"); // SiprecEnumUpdateStatus | 
    try {
      ApiV2010AccountCallSiprec result = apiInstance.updateSiprec(accountSid, callSid, sid, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401SiprecApi#updateSiprec");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Siprec resource. | |
| **callSid** | **String**| The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Siprec resource is associated with. | |
| **sid** | **String**| The SID of the Siprec resource, or the &#x60;name&#x60; used when creating the resource | |
| **status** | **SiprecEnumUpdateStatus**|  | [enum: stopped] |

### Return type

[**ApiV2010AccountCallSiprec**](ApiV2010AccountCallSiprec.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

