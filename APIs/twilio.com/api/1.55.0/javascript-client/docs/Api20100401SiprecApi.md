# TwilioApi.Api20100401SiprecApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSiprec**](Api20100401SiprecApi.md#createSiprec) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Siprec.json | 
[**updateSiprec**](Api20100401SiprecApi.md#updateSiprec) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Siprec/{Sid}.json | 



## createSiprec

> ApiV2010AccountCallSiprec createSiprec(accountSid, callSid, opts)



Create a Siprec

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401SiprecApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Siprec resource.
let callSid = "callSid_example"; // String | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Siprec resource is associated with.
let opts = {
  'connectorName': "connectorName_example", // String | Unique name used when configuring the connector via Marketplace Add-on.
  'name': "name_example", // String | The user-specified name of this Siprec, if one was given when the Siprec was created. This may be used to stop the Siprec.
  'parameter1Name': "parameter1Name_example", // String | Parameter name
  'parameter1Value': "parameter1Value_example", // String | Parameter value
  'parameter10Name': "parameter10Name_example", // String | Parameter name
  'parameter10Value': "parameter10Value_example", // String | Parameter value
  'parameter11Name': "parameter11Name_example", // String | Parameter name
  'parameter11Value': "parameter11Value_example", // String | Parameter value
  'parameter12Name': "parameter12Name_example", // String | Parameter name
  'parameter12Value': "parameter12Value_example", // String | Parameter value
  'parameter13Name': "parameter13Name_example", // String | Parameter name
  'parameter13Value': "parameter13Value_example", // String | Parameter value
  'parameter14Name': "parameter14Name_example", // String | Parameter name
  'parameter14Value': "parameter14Value_example", // String | Parameter value
  'parameter15Name': "parameter15Name_example", // String | Parameter name
  'parameter15Value': "parameter15Value_example", // String | Parameter value
  'parameter16Name': "parameter16Name_example", // String | Parameter name
  'parameter16Value': "parameter16Value_example", // String | Parameter value
  'parameter17Name': "parameter17Name_example", // String | Parameter name
  'parameter17Value': "parameter17Value_example", // String | Parameter value
  'parameter18Name': "parameter18Name_example", // String | Parameter name
  'parameter18Value': "parameter18Value_example", // String | Parameter value
  'parameter19Name': "parameter19Name_example", // String | Parameter name
  'parameter19Value': "parameter19Value_example", // String | Parameter value
  'parameter2Name': "parameter2Name_example", // String | Parameter name
  'parameter2Value': "parameter2Value_example", // String | Parameter value
  'parameter20Name': "parameter20Name_example", // String | Parameter name
  'parameter20Value': "parameter20Value_example", // String | Parameter value
  'parameter21Name': "parameter21Name_example", // String | Parameter name
  'parameter21Value': "parameter21Value_example", // String | Parameter value
  'parameter22Name': "parameter22Name_example", // String | Parameter name
  'parameter22Value': "parameter22Value_example", // String | Parameter value
  'parameter23Name': "parameter23Name_example", // String | Parameter name
  'parameter23Value': "parameter23Value_example", // String | Parameter value
  'parameter24Name': "parameter24Name_example", // String | Parameter name
  'parameter24Value': "parameter24Value_example", // String | Parameter value
  'parameter25Name': "parameter25Name_example", // String | Parameter name
  'parameter25Value': "parameter25Value_example", // String | Parameter value
  'parameter26Name': "parameter26Name_example", // String | Parameter name
  'parameter26Value': "parameter26Value_example", // String | Parameter value
  'parameter27Name': "parameter27Name_example", // String | Parameter name
  'parameter27Value': "parameter27Value_example", // String | Parameter value
  'parameter28Name': "parameter28Name_example", // String | Parameter name
  'parameter28Value': "parameter28Value_example", // String | Parameter value
  'parameter29Name': "parameter29Name_example", // String | Parameter name
  'parameter29Value': "parameter29Value_example", // String | Parameter value
  'parameter3Name': "parameter3Name_example", // String | Parameter name
  'parameter3Value': "parameter3Value_example", // String | Parameter value
  'parameter30Name': "parameter30Name_example", // String | Parameter name
  'parameter30Value': "parameter30Value_example", // String | Parameter value
  'parameter31Name': "parameter31Name_example", // String | Parameter name
  'parameter31Value': "parameter31Value_example", // String | Parameter value
  'parameter32Name': "parameter32Name_example", // String | Parameter name
  'parameter32Value': "parameter32Value_example", // String | Parameter value
  'parameter33Name': "parameter33Name_example", // String | Parameter name
  'parameter33Value': "parameter33Value_example", // String | Parameter value
  'parameter34Name': "parameter34Name_example", // String | Parameter name
  'parameter34Value': "parameter34Value_example", // String | Parameter value
  'parameter35Name': "parameter35Name_example", // String | Parameter name
  'parameter35Value': "parameter35Value_example", // String | Parameter value
  'parameter36Name': "parameter36Name_example", // String | Parameter name
  'parameter36Value': "parameter36Value_example", // String | Parameter value
  'parameter37Name': "parameter37Name_example", // String | Parameter name
  'parameter37Value': "parameter37Value_example", // String | Parameter value
  'parameter38Name': "parameter38Name_example", // String | Parameter name
  'parameter38Value': "parameter38Value_example", // String | Parameter value
  'parameter39Name': "parameter39Name_example", // String | Parameter name
  'parameter39Value': "parameter39Value_example", // String | Parameter value
  'parameter4Name': "parameter4Name_example", // String | Parameter name
  'parameter4Value': "parameter4Value_example", // String | Parameter value
  'parameter40Name': "parameter40Name_example", // String | Parameter name
  'parameter40Value': "parameter40Value_example", // String | Parameter value
  'parameter41Name': "parameter41Name_example", // String | Parameter name
  'parameter41Value': "parameter41Value_example", // String | Parameter value
  'parameter42Name': "parameter42Name_example", // String | Parameter name
  'parameter42Value': "parameter42Value_example", // String | Parameter value
  'parameter43Name': "parameter43Name_example", // String | Parameter name
  'parameter43Value': "parameter43Value_example", // String | Parameter value
  'parameter44Name': "parameter44Name_example", // String | Parameter name
  'parameter44Value': "parameter44Value_example", // String | Parameter value
  'parameter45Name': "parameter45Name_example", // String | Parameter name
  'parameter45Value': "parameter45Value_example", // String | Parameter value
  'parameter46Name': "parameter46Name_example", // String | Parameter name
  'parameter46Value': "parameter46Value_example", // String | Parameter value
  'parameter47Name': "parameter47Name_example", // String | Parameter name
  'parameter47Value': "parameter47Value_example", // String | Parameter value
  'parameter48Name': "parameter48Name_example", // String | Parameter name
  'parameter48Value': "parameter48Value_example", // String | Parameter value
  'parameter49Name': "parameter49Name_example", // String | Parameter name
  'parameter49Value': "parameter49Value_example", // String | Parameter value
  'parameter5Name': "parameter5Name_example", // String | Parameter name
  'parameter5Value': "parameter5Value_example", // String | Parameter value
  'parameter50Name': "parameter50Name_example", // String | Parameter name
  'parameter50Value': "parameter50Value_example", // String | Parameter value
  'parameter51Name': "parameter51Name_example", // String | Parameter name
  'parameter51Value': "parameter51Value_example", // String | Parameter value
  'parameter52Name': "parameter52Name_example", // String | Parameter name
  'parameter52Value': "parameter52Value_example", // String | Parameter value
  'parameter53Name': "parameter53Name_example", // String | Parameter name
  'parameter53Value': "parameter53Value_example", // String | Parameter value
  'parameter54Name': "parameter54Name_example", // String | Parameter name
  'parameter54Value': "parameter54Value_example", // String | Parameter value
  'parameter55Name': "parameter55Name_example", // String | Parameter name
  'parameter55Value': "parameter55Value_example", // String | Parameter value
  'parameter56Name': "parameter56Name_example", // String | Parameter name
  'parameter56Value': "parameter56Value_example", // String | Parameter value
  'parameter57Name': "parameter57Name_example", // String | Parameter name
  'parameter57Value': "parameter57Value_example", // String | Parameter value
  'parameter58Name': "parameter58Name_example", // String | Parameter name
  'parameter58Value': "parameter58Value_example", // String | Parameter value
  'parameter59Name': "parameter59Name_example", // String | Parameter name
  'parameter59Value': "parameter59Value_example", // String | Parameter value
  'parameter6Name': "parameter6Name_example", // String | Parameter name
  'parameter6Value': "parameter6Value_example", // String | Parameter value
  'parameter60Name': "parameter60Name_example", // String | Parameter name
  'parameter60Value': "parameter60Value_example", // String | Parameter value
  'parameter61Name': "parameter61Name_example", // String | Parameter name
  'parameter61Value': "parameter61Value_example", // String | Parameter value
  'parameter62Name': "parameter62Name_example", // String | Parameter name
  'parameter62Value': "parameter62Value_example", // String | Parameter value
  'parameter63Name': "parameter63Name_example", // String | Parameter name
  'parameter63Value': "parameter63Value_example", // String | Parameter value
  'parameter64Name': "parameter64Name_example", // String | Parameter name
  'parameter64Value': "parameter64Value_example", // String | Parameter value
  'parameter65Name': "parameter65Name_example", // String | Parameter name
  'parameter65Value': "parameter65Value_example", // String | Parameter value
  'parameter66Name': "parameter66Name_example", // String | Parameter name
  'parameter66Value': "parameter66Value_example", // String | Parameter value
  'parameter67Name': "parameter67Name_example", // String | Parameter name
  'parameter67Value': "parameter67Value_example", // String | Parameter value
  'parameter68Name': "parameter68Name_example", // String | Parameter name
  'parameter68Value': "parameter68Value_example", // String | Parameter value
  'parameter69Name': "parameter69Name_example", // String | Parameter name
  'parameter69Value': "parameter69Value_example", // String | Parameter value
  'parameter7Name': "parameter7Name_example", // String | Parameter name
  'parameter7Value': "parameter7Value_example", // String | Parameter value
  'parameter70Name': "parameter70Name_example", // String | Parameter name
  'parameter70Value': "parameter70Value_example", // String | Parameter value
  'parameter71Name': "parameter71Name_example", // String | Parameter name
  'parameter71Value': "parameter71Value_example", // String | Parameter value
  'parameter72Name': "parameter72Name_example", // String | Parameter name
  'parameter72Value': "parameter72Value_example", // String | Parameter value
  'parameter73Name': "parameter73Name_example", // String | Parameter name
  'parameter73Value': "parameter73Value_example", // String | Parameter value
  'parameter74Name': "parameter74Name_example", // String | Parameter name
  'parameter74Value': "parameter74Value_example", // String | Parameter value
  'parameter75Name': "parameter75Name_example", // String | Parameter name
  'parameter75Value': "parameter75Value_example", // String | Parameter value
  'parameter76Name': "parameter76Name_example", // String | Parameter name
  'parameter76Value': "parameter76Value_example", // String | Parameter value
  'parameter77Name': "parameter77Name_example", // String | Parameter name
  'parameter77Value': "parameter77Value_example", // String | Parameter value
  'parameter78Name': "parameter78Name_example", // String | Parameter name
  'parameter78Value': "parameter78Value_example", // String | Parameter value
  'parameter79Name': "parameter79Name_example", // String | Parameter name
  'parameter79Value': "parameter79Value_example", // String | Parameter value
  'parameter8Name': "parameter8Name_example", // String | Parameter name
  'parameter8Value': "parameter8Value_example", // String | Parameter value
  'parameter80Name': "parameter80Name_example", // String | Parameter name
  'parameter80Value': "parameter80Value_example", // String | Parameter value
  'parameter81Name': "parameter81Name_example", // String | Parameter name
  'parameter81Value': "parameter81Value_example", // String | Parameter value
  'parameter82Name': "parameter82Name_example", // String | Parameter name
  'parameter82Value': "parameter82Value_example", // String | Parameter value
  'parameter83Name': "parameter83Name_example", // String | Parameter name
  'parameter83Value': "parameter83Value_example", // String | Parameter value
  'parameter84Name': "parameter84Name_example", // String | Parameter name
  'parameter84Value': "parameter84Value_example", // String | Parameter value
  'parameter85Name': "parameter85Name_example", // String | Parameter name
  'parameter85Value': "parameter85Value_example", // String | Parameter value
  'parameter86Name': "parameter86Name_example", // String | Parameter name
  'parameter86Value': "parameter86Value_example", // String | Parameter value
  'parameter87Name': "parameter87Name_example", // String | Parameter name
  'parameter87Value': "parameter87Value_example", // String | Parameter value
  'parameter88Name': "parameter88Name_example", // String | Parameter name
  'parameter88Value': "parameter88Value_example", // String | Parameter value
  'parameter89Name': "parameter89Name_example", // String | Parameter name
  'parameter89Value': "parameter89Value_example", // String | Parameter value
  'parameter9Name': "parameter9Name_example", // String | Parameter name
  'parameter9Value': "parameter9Value_example", // String | Parameter value
  'parameter90Name': "parameter90Name_example", // String | Parameter name
  'parameter90Value': "parameter90Value_example", // String | Parameter value
  'parameter91Name': "parameter91Name_example", // String | Parameter name
  'parameter91Value': "parameter91Value_example", // String | Parameter value
  'parameter92Name': "parameter92Name_example", // String | Parameter name
  'parameter92Value': "parameter92Value_example", // String | Parameter value
  'parameter93Name': "parameter93Name_example", // String | Parameter name
  'parameter93Value': "parameter93Value_example", // String | Parameter value
  'parameter94Name': "parameter94Name_example", // String | Parameter name
  'parameter94Value': "parameter94Value_example", // String | Parameter value
  'parameter95Name': "parameter95Name_example", // String | Parameter name
  'parameter95Value': "parameter95Value_example", // String | Parameter value
  'parameter96Name': "parameter96Name_example", // String | Parameter name
  'parameter96Value': "parameter96Value_example", // String | Parameter value
  'parameter97Name': "parameter97Name_example", // String | Parameter name
  'parameter97Value': "parameter97Value_example", // String | Parameter value
  'parameter98Name': "parameter98Name_example", // String | Parameter name
  'parameter98Value': "parameter98Value_example", // String | Parameter value
  'parameter99Name': "parameter99Name_example", // String | Parameter name
  'parameter99Value': "parameter99Value_example", // String | Parameter value
  'statusCallback': "statusCallback_example", // String | Absolute URL of the status callback.
  'statusCallbackMethod': "statusCallbackMethod_example", // String | The http method for the status_callback (one of GET, POST).
  'track': "track_example" // SiprecEnumTrack | 
};
apiInstance.createSiprec(accountSid, callSid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Siprec resource. | 
 **callSid** | **String**| The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Siprec resource is associated with. | 
 **connectorName** | **String**| Unique name used when configuring the connector via Marketplace Add-on. | [optional] 
 **name** | **String**| The user-specified name of this Siprec, if one was given when the Siprec was created. This may be used to stop the Siprec. | [optional] 
 **parameter1Name** | **String**| Parameter name | [optional] 
 **parameter1Value** | **String**| Parameter value | [optional] 
 **parameter10Name** | **String**| Parameter name | [optional] 
 **parameter10Value** | **String**| Parameter value | [optional] 
 **parameter11Name** | **String**| Parameter name | [optional] 
 **parameter11Value** | **String**| Parameter value | [optional] 
 **parameter12Name** | **String**| Parameter name | [optional] 
 **parameter12Value** | **String**| Parameter value | [optional] 
 **parameter13Name** | **String**| Parameter name | [optional] 
 **parameter13Value** | **String**| Parameter value | [optional] 
 **parameter14Name** | **String**| Parameter name | [optional] 
 **parameter14Value** | **String**| Parameter value | [optional] 
 **parameter15Name** | **String**| Parameter name | [optional] 
 **parameter15Value** | **String**| Parameter value | [optional] 
 **parameter16Name** | **String**| Parameter name | [optional] 
 **parameter16Value** | **String**| Parameter value | [optional] 
 **parameter17Name** | **String**| Parameter name | [optional] 
 **parameter17Value** | **String**| Parameter value | [optional] 
 **parameter18Name** | **String**| Parameter name | [optional] 
 **parameter18Value** | **String**| Parameter value | [optional] 
 **parameter19Name** | **String**| Parameter name | [optional] 
 **parameter19Value** | **String**| Parameter value | [optional] 
 **parameter2Name** | **String**| Parameter name | [optional] 
 **parameter2Value** | **String**| Parameter value | [optional] 
 **parameter20Name** | **String**| Parameter name | [optional] 
 **parameter20Value** | **String**| Parameter value | [optional] 
 **parameter21Name** | **String**| Parameter name | [optional] 
 **parameter21Value** | **String**| Parameter value | [optional] 
 **parameter22Name** | **String**| Parameter name | [optional] 
 **parameter22Value** | **String**| Parameter value | [optional] 
 **parameter23Name** | **String**| Parameter name | [optional] 
 **parameter23Value** | **String**| Parameter value | [optional] 
 **parameter24Name** | **String**| Parameter name | [optional] 
 **parameter24Value** | **String**| Parameter value | [optional] 
 **parameter25Name** | **String**| Parameter name | [optional] 
 **parameter25Value** | **String**| Parameter value | [optional] 
 **parameter26Name** | **String**| Parameter name | [optional] 
 **parameter26Value** | **String**| Parameter value | [optional] 
 **parameter27Name** | **String**| Parameter name | [optional] 
 **parameter27Value** | **String**| Parameter value | [optional] 
 **parameter28Name** | **String**| Parameter name | [optional] 
 **parameter28Value** | **String**| Parameter value | [optional] 
 **parameter29Name** | **String**| Parameter name | [optional] 
 **parameter29Value** | **String**| Parameter value | [optional] 
 **parameter3Name** | **String**| Parameter name | [optional] 
 **parameter3Value** | **String**| Parameter value | [optional] 
 **parameter30Name** | **String**| Parameter name | [optional] 
 **parameter30Value** | **String**| Parameter value | [optional] 
 **parameter31Name** | **String**| Parameter name | [optional] 
 **parameter31Value** | **String**| Parameter value | [optional] 
 **parameter32Name** | **String**| Parameter name | [optional] 
 **parameter32Value** | **String**| Parameter value | [optional] 
 **parameter33Name** | **String**| Parameter name | [optional] 
 **parameter33Value** | **String**| Parameter value | [optional] 
 **parameter34Name** | **String**| Parameter name | [optional] 
 **parameter34Value** | **String**| Parameter value | [optional] 
 **parameter35Name** | **String**| Parameter name | [optional] 
 **parameter35Value** | **String**| Parameter value | [optional] 
 **parameter36Name** | **String**| Parameter name | [optional] 
 **parameter36Value** | **String**| Parameter value | [optional] 
 **parameter37Name** | **String**| Parameter name | [optional] 
 **parameter37Value** | **String**| Parameter value | [optional] 
 **parameter38Name** | **String**| Parameter name | [optional] 
 **parameter38Value** | **String**| Parameter value | [optional] 
 **parameter39Name** | **String**| Parameter name | [optional] 
 **parameter39Value** | **String**| Parameter value | [optional] 
 **parameter4Name** | **String**| Parameter name | [optional] 
 **parameter4Value** | **String**| Parameter value | [optional] 
 **parameter40Name** | **String**| Parameter name | [optional] 
 **parameter40Value** | **String**| Parameter value | [optional] 
 **parameter41Name** | **String**| Parameter name | [optional] 
 **parameter41Value** | **String**| Parameter value | [optional] 
 **parameter42Name** | **String**| Parameter name | [optional] 
 **parameter42Value** | **String**| Parameter value | [optional] 
 **parameter43Name** | **String**| Parameter name | [optional] 
 **parameter43Value** | **String**| Parameter value | [optional] 
 **parameter44Name** | **String**| Parameter name | [optional] 
 **parameter44Value** | **String**| Parameter value | [optional] 
 **parameter45Name** | **String**| Parameter name | [optional] 
 **parameter45Value** | **String**| Parameter value | [optional] 
 **parameter46Name** | **String**| Parameter name | [optional] 
 **parameter46Value** | **String**| Parameter value | [optional] 
 **parameter47Name** | **String**| Parameter name | [optional] 
 **parameter47Value** | **String**| Parameter value | [optional] 
 **parameter48Name** | **String**| Parameter name | [optional] 
 **parameter48Value** | **String**| Parameter value | [optional] 
 **parameter49Name** | **String**| Parameter name | [optional] 
 **parameter49Value** | **String**| Parameter value | [optional] 
 **parameter5Name** | **String**| Parameter name | [optional] 
 **parameter5Value** | **String**| Parameter value | [optional] 
 **parameter50Name** | **String**| Parameter name | [optional] 
 **parameter50Value** | **String**| Parameter value | [optional] 
 **parameter51Name** | **String**| Parameter name | [optional] 
 **parameter51Value** | **String**| Parameter value | [optional] 
 **parameter52Name** | **String**| Parameter name | [optional] 
 **parameter52Value** | **String**| Parameter value | [optional] 
 **parameter53Name** | **String**| Parameter name | [optional] 
 **parameter53Value** | **String**| Parameter value | [optional] 
 **parameter54Name** | **String**| Parameter name | [optional] 
 **parameter54Value** | **String**| Parameter value | [optional] 
 **parameter55Name** | **String**| Parameter name | [optional] 
 **parameter55Value** | **String**| Parameter value | [optional] 
 **parameter56Name** | **String**| Parameter name | [optional] 
 **parameter56Value** | **String**| Parameter value | [optional] 
 **parameter57Name** | **String**| Parameter name | [optional] 
 **parameter57Value** | **String**| Parameter value | [optional] 
 **parameter58Name** | **String**| Parameter name | [optional] 
 **parameter58Value** | **String**| Parameter value | [optional] 
 **parameter59Name** | **String**| Parameter name | [optional] 
 **parameter59Value** | **String**| Parameter value | [optional] 
 **parameter6Name** | **String**| Parameter name | [optional] 
 **parameter6Value** | **String**| Parameter value | [optional] 
 **parameter60Name** | **String**| Parameter name | [optional] 
 **parameter60Value** | **String**| Parameter value | [optional] 
 **parameter61Name** | **String**| Parameter name | [optional] 
 **parameter61Value** | **String**| Parameter value | [optional] 
 **parameter62Name** | **String**| Parameter name | [optional] 
 **parameter62Value** | **String**| Parameter value | [optional] 
 **parameter63Name** | **String**| Parameter name | [optional] 
 **parameter63Value** | **String**| Parameter value | [optional] 
 **parameter64Name** | **String**| Parameter name | [optional] 
 **parameter64Value** | **String**| Parameter value | [optional] 
 **parameter65Name** | **String**| Parameter name | [optional] 
 **parameter65Value** | **String**| Parameter value | [optional] 
 **parameter66Name** | **String**| Parameter name | [optional] 
 **parameter66Value** | **String**| Parameter value | [optional] 
 **parameter67Name** | **String**| Parameter name | [optional] 
 **parameter67Value** | **String**| Parameter value | [optional] 
 **parameter68Name** | **String**| Parameter name | [optional] 
 **parameter68Value** | **String**| Parameter value | [optional] 
 **parameter69Name** | **String**| Parameter name | [optional] 
 **parameter69Value** | **String**| Parameter value | [optional] 
 **parameter7Name** | **String**| Parameter name | [optional] 
 **parameter7Value** | **String**| Parameter value | [optional] 
 **parameter70Name** | **String**| Parameter name | [optional] 
 **parameter70Value** | **String**| Parameter value | [optional] 
 **parameter71Name** | **String**| Parameter name | [optional] 
 **parameter71Value** | **String**| Parameter value | [optional] 
 **parameter72Name** | **String**| Parameter name | [optional] 
 **parameter72Value** | **String**| Parameter value | [optional] 
 **parameter73Name** | **String**| Parameter name | [optional] 
 **parameter73Value** | **String**| Parameter value | [optional] 
 **parameter74Name** | **String**| Parameter name | [optional] 
 **parameter74Value** | **String**| Parameter value | [optional] 
 **parameter75Name** | **String**| Parameter name | [optional] 
 **parameter75Value** | **String**| Parameter value | [optional] 
 **parameter76Name** | **String**| Parameter name | [optional] 
 **parameter76Value** | **String**| Parameter value | [optional] 
 **parameter77Name** | **String**| Parameter name | [optional] 
 **parameter77Value** | **String**| Parameter value | [optional] 
 **parameter78Name** | **String**| Parameter name | [optional] 
 **parameter78Value** | **String**| Parameter value | [optional] 
 **parameter79Name** | **String**| Parameter name | [optional] 
 **parameter79Value** | **String**| Parameter value | [optional] 
 **parameter8Name** | **String**| Parameter name | [optional] 
 **parameter8Value** | **String**| Parameter value | [optional] 
 **parameter80Name** | **String**| Parameter name | [optional] 
 **parameter80Value** | **String**| Parameter value | [optional] 
 **parameter81Name** | **String**| Parameter name | [optional] 
 **parameter81Value** | **String**| Parameter value | [optional] 
 **parameter82Name** | **String**| Parameter name | [optional] 
 **parameter82Value** | **String**| Parameter value | [optional] 
 **parameter83Name** | **String**| Parameter name | [optional] 
 **parameter83Value** | **String**| Parameter value | [optional] 
 **parameter84Name** | **String**| Parameter name | [optional] 
 **parameter84Value** | **String**| Parameter value | [optional] 
 **parameter85Name** | **String**| Parameter name | [optional] 
 **parameter85Value** | **String**| Parameter value | [optional] 
 **parameter86Name** | **String**| Parameter name | [optional] 
 **parameter86Value** | **String**| Parameter value | [optional] 
 **parameter87Name** | **String**| Parameter name | [optional] 
 **parameter87Value** | **String**| Parameter value | [optional] 
 **parameter88Name** | **String**| Parameter name | [optional] 
 **parameter88Value** | **String**| Parameter value | [optional] 
 **parameter89Name** | **String**| Parameter name | [optional] 
 **parameter89Value** | **String**| Parameter value | [optional] 
 **parameter9Name** | **String**| Parameter name | [optional] 
 **parameter9Value** | **String**| Parameter value | [optional] 
 **parameter90Name** | **String**| Parameter name | [optional] 
 **parameter90Value** | **String**| Parameter value | [optional] 
 **parameter91Name** | **String**| Parameter name | [optional] 
 **parameter91Value** | **String**| Parameter value | [optional] 
 **parameter92Name** | **String**| Parameter name | [optional] 
 **parameter92Value** | **String**| Parameter value | [optional] 
 **parameter93Name** | **String**| Parameter name | [optional] 
 **parameter93Value** | **String**| Parameter value | [optional] 
 **parameter94Name** | **String**| Parameter name | [optional] 
 **parameter94Value** | **String**| Parameter value | [optional] 
 **parameter95Name** | **String**| Parameter name | [optional] 
 **parameter95Value** | **String**| Parameter value | [optional] 
 **parameter96Name** | **String**| Parameter name | [optional] 
 **parameter96Value** | **String**| Parameter value | [optional] 
 **parameter97Name** | **String**| Parameter name | [optional] 
 **parameter97Value** | **String**| Parameter value | [optional] 
 **parameter98Name** | **String**| Parameter name | [optional] 
 **parameter98Value** | **String**| Parameter value | [optional] 
 **parameter99Name** | **String**| Parameter name | [optional] 
 **parameter99Value** | **String**| Parameter value | [optional] 
 **statusCallback** | **String**| Absolute URL of the status callback. | [optional] 
 **statusCallbackMethod** | **String**| The http method for the status_callback (one of GET, POST). | [optional] 
 **track** | **SiprecEnumTrack**|  | [optional] 

### Return type

[**ApiV2010AccountCallSiprec**](ApiV2010AccountCallSiprec.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## updateSiprec

> ApiV2010AccountCallSiprec updateSiprec(accountSid, callSid, sid, status)



Stop a Siprec using either the SID of the Siprec resource or the &#x60;name&#x60; used when creating the resource

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401SiprecApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Siprec resource.
let callSid = "callSid_example"; // String | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Siprec resource is associated with.
let sid = "sid_example"; // String | The SID of the Siprec resource, or the `name` used when creating the resource
let status = "status_example"; // SiprecEnumUpdateStatus | 
apiInstance.updateSiprec(accountSid, callSid, sid, status, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Siprec resource. | 
 **callSid** | **String**| The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Siprec resource is associated with. | 
 **sid** | **String**| The SID of the Siprec resource, or the &#x60;name&#x60; used when creating the resource | 
 **status** | **SiprecEnumUpdateStatus**|  | 

### Return type

[**ApiV2010AccountCallSiprec**](ApiV2010AccountCallSiprec.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

