# DweetIo.LocksApi

All URIs are relative to *https://dweet.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lockThing**](LocksApi.md#lockThing) | **GET** /lock/{thing} | Reserve and lock a thing.
[**removeLock**](LocksApi.md#removeLock) | **GET** /remove/lock/{lock} | Remove a lock from thing.
[**unlockThing**](LocksApi.md#unlockThing) | **GET** /unlock/{thing} | Unlock a thing.



## lockThing

> lockThing(thing, lock, key)

Reserve and lock a thing.

### Example

```javascript
import DweetIo from 'dweet_io';

let apiInstance = new DweetIo.LocksApi();
let thing = "thing_example"; // String | A unique name of a thing.
let lock = "lock_example"; // String | A valid dweet.io lock.
let key = "key_example"; // String | A valid dweet.io master key.
apiInstance.lockThing(thing, lock, key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing** | **String**| A unique name of a thing. | 
 **lock** | **String**| A valid dweet.io lock. | 
 **key** | **String**| A valid dweet.io master key. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeLock

> removeLock(lock, key)

Remove a lock from thing.

### Example

```javascript
import DweetIo from 'dweet_io';

let apiInstance = new DweetIo.LocksApi();
let lock = "lock_example"; // String | A valid dweet.io lock.
let key = "key_example"; // String | A valid dweet.io master key.
apiInstance.removeLock(lock, key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lock** | **String**| A valid dweet.io lock. | 
 **key** | **String**| A valid dweet.io master key. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## unlockThing

> unlockThing(thing, key)

Unlock a thing.

### Example

```javascript
import DweetIo from 'dweet_io';

let apiInstance = new DweetIo.LocksApi();
let thing = "thing_example"; // String | A unique name of a thing.
let key = "key_example"; // String | A valid dweet.io master key.
apiInstance.unlockThing(thing, key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing** | **String**| A unique name of a thing. | 
 **key** | **String**| A valid dweet.io master key. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

