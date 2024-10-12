# InstanceFailoverGroupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**instanceFailoverGroupsCreateOrUpdate**](InstanceFailoverGroupsApi.md#instanceFailoverGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/instanceFailoverGroups/{failoverGroupName} |  |
| [**instanceFailoverGroupsDelete**](InstanceFailoverGroupsApi.md#instanceFailoverGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/instanceFailoverGroups/{failoverGroupName} |  |
| [**instanceFailoverGroupsFailover**](InstanceFailoverGroupsApi.md#instanceFailoverGroupsFailover) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/instanceFailoverGroups/{failoverGroupName}/failover |  |
| [**instanceFailoverGroupsForceFailoverAllowDataLoss**](InstanceFailoverGroupsApi.md#instanceFailoverGroupsForceFailoverAllowDataLoss) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/instanceFailoverGroups/{failoverGroupName}/forceFailoverAllowDataLoss |  |
| [**instanceFailoverGroupsGet**](InstanceFailoverGroupsApi.md#instanceFailoverGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/instanceFailoverGroups/{failoverGroupName} |  |
| [**instanceFailoverGroupsListByLocation**](InstanceFailoverGroupsApi.md#instanceFailoverGroupsListByLocation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/instanceFailoverGroups |  |


<a id="instanceFailoverGroupsCreateOrUpdate"></a>
# **instanceFailoverGroupsCreateOrUpdate**
> InstanceFailoverGroup instanceFailoverGroupsCreateOrUpdate(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion, parameters)



Creates or updates a failover group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceFailoverGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    InstanceFailoverGroupsApi apiInstance = new InstanceFailoverGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String locationName = "locationName_example"; // String | The name of the region where the resource is located.
    String failoverGroupName = "failoverGroupName_example"; // String | The name of the failover group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    InstanceFailoverGroup parameters = new InstanceFailoverGroup(); // InstanceFailoverGroup | The failover group parameters.
    try {
      InstanceFailoverGroup result = apiInstance.instanceFailoverGroupsCreateOrUpdate(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceFailoverGroupsApi#instanceFailoverGroupsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **locationName** | **String**| The name of the region where the resource is located. | |
| **failoverGroupName** | **String**| The name of the failover group. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**InstanceFailoverGroup**](InstanceFailoverGroup.md)| The failover group parameters. | |

### Return type

[**InstanceFailoverGroup**](InstanceFailoverGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the failover group. |  -  |
| **201** | Successfully created the failover group. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidPartner - The given partners field in create or update instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupCreateOrUpdateRequestDuplicatePartner - One or more of the provided partner servers are already part of the instance failover group. Please make sure the primary server and all of the given partner servers are unique.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidManagedInstanceRegion - The provided partner managed instance region in the instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupCreateOrUpdateRequestUnsupportedPartnerCount - Only one partner region is supported.   * 400 InstanceFailoverGroupCreateOrUpdateRequestUnsupportedPairCount - Only one managed instance pair is supported.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpoint - The readWriteEndpoint field is required for create or update requests.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalid - The create or update instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupUpdateOrDeleteRequestOnSecondary - Modifications to the instance failover group are not allowed on a secondary server. Execute the request on the primary server.   * 400 InstanceFailoverGroupCreateOrUpdateRequestNegativeGracePeriodValues - Grace period value for the read-write endpoint must be non-negative.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpointFields - The property failoverWithDataLossGracePeriodMinutes must be provided when failover policy Automatic is selected for the read-write endpoint.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteFailoverPolicy - The failoverPolicy field for the read-write endpoint is required for create or update requests.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpointFieldsForManualPolicy - Grace period value should not be provided when failover policy Manual is selected for the read-write endpoint.   * 400 InstanceFailoverGroupCreateOrUpdateRequestReadOnlyPropertyModified - The create or update instance failover group request body should not modify the read-only property &#39;{0}&#39;.   * 400 InstanceFailoverGroupFailoverRequestOnPrimary - The failover request should be initiated on the secondary server of instance failover group.   * 400 InstanceFailoverGroupPartnerManagedInstanceFromDifferentSubscription - Primary server and the partner server of failover group are from different subscriptions. Cross subscription for servers of failover group is not allowed.   * 400 InvalidAddSecondaryPermission - User does not have sufficient permission to add secondary on the specified server.   * 400 InvalidSku - The user specified an invalid sku.   * 400 ServerNotFound - The requested server was not found.   * 400 FeatureDisabledOnSelectedEdition - User attempted to use a feature which is disabled on current database edition.   * 400 TokenTooLong - The provided token is too long.   * 400 InvalidTargetSubregion - The target server of a non-readable secondary is not in a DR paired Azure region.   * 400 IncorrectReplicationLinkState - The operation expects the database to be in an expected state on the replication link.   * 400 PlannedFailoverTimedOutForDatabase - User invoked planned failover, it timed out, and a specific database appears to be to blame.   * 400 PlannedFailoverTimedOut - User invoked planned failover, and it timed out while trying to contact the partner management service.   * 400 CannotUseReservedDatabaseName - Cannot use reserved database name in this operation.   * 400 InvalidFailoverGroupRegion - Servers specified in an Instance Failover Group need to reside in different regions to provide isolation.   * 400 InstanceFailoverGroupDoesNotExist - Failover group does not exist on a server.   * 400 InstanceFailoverGroupNotSecondary - Failover cannot be initiated from the primary server in a instance failover group.   * 400 InvalidServerName - Invalid server name specified.   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 400 GeoReplicationDatabaseNotSecondary - The operation expects the database to be a replication target.   * 400 UnableToResolveRemoteServer - The remote partner server name could not be resolved due to an invalid server name or DNS connectivity issues.   * 400 RemoteDatabaseCopyPermission - User does not have sufficient permission to create a database copy on the specified server.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ResourceNotFound - The requested resource was not found.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 ServerNotInSubscription - Specified server does not exist on the specified subscription.   * 404 SourceDatabaseNotFound - The source database does not exist.   * 405 UnsupportedReplicationOperation - An unsupported replication operation was initiated on the database.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 409 ConflictingServerOperation - An operation is currently in progress for the server.   * 409 SubscriptionDisabled - Subscription is disabled.   * 409 ConflictingSystemOperationInProgress - A system maintenance operation is in progress on the database and further operations need to wait until it is completed.   * 409 GeoReplicationCannotBecomePrimaryDuringUndo - User attempted to failover or force-terminate a geo-link while the secondary is in a state where it may not be physically consistent and so cannot enter the primary role.   * 409 UpdateSloInProgress - User tried to initiate an incompatible operation while a SLO update was in progress.   * 409 InstanceFailoverGroupAlreadyExists - Failover group already exists on a given server.   * 409 InstanceFailoverGroupBusy - Instance failover group is busy with another operation.   * 409 InstanceFailoverGroupDnsRecordInUse - A duplicate DNS record exists for the requested endpoint.   * 409 InvalidFailoverGroupName - Invalid Instance Failover Group name was supplied.   * 409 InvalidOperationForDatabaseNotInReplicationRelationship - A replication seeding operation was performed on a database that is already in a replication relationship.   * 409 InvalidDatabaseStateForOperation - The operation is not allowed on the database in its current replication state.   * 409 DuplicateGeoDrRelation - The databases are already in a replication relation. This is a duplicate request.   * 409 RemoteDatabaseExists - The destination database name already exists on the destination server.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="instanceFailoverGroupsDelete"></a>
# **instanceFailoverGroupsDelete**
> instanceFailoverGroupsDelete(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion)



Deletes a failover group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceFailoverGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    InstanceFailoverGroupsApi apiInstance = new InstanceFailoverGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String locationName = "locationName_example"; // String | The name of the region where the resource is located.
    String failoverGroupName = "failoverGroupName_example"; // String | The name of the failover group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.instanceFailoverGroupsDelete(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceFailoverGroupsApi#instanceFailoverGroupsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **locationName** | **String**| The name of the region where the resource is located. | |
| **failoverGroupName** | **String**| The name of the failover group. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted the failover group. |  -  |
| **202** | Accepted |  -  |
| **204** | The specified failover group does not exist. |  -  |
| **0** | *** Error Responses: ***   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidPartner - The given partners field in create or update instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupCreateOrUpdateRequestDuplicatePartner - One or more of the provided partner servers are already part of the instance failover group. Please make sure the primary server and all of the given partner servers are unique.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidManagedInstanceRegion - The provided partner managed instance region in the instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupCreateOrUpdateRequestUnsupportedPartnerCount - Only one partner region is supported.   * 400 InstanceFailoverGroupCreateOrUpdateRequestUnsupportedPairCount - Only one managed instance pair is supported.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpoint - The readWriteEndpoint field is required for create or update requests.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalid - The create or update instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupUpdateOrDeleteRequestOnSecondary - Modifications to the instance failover group are not allowed on a secondary server. Execute the request on the primary server.   * 400 InstanceFailoverGroupCreateOrUpdateRequestNegativeGracePeriodValues - Grace period value for the read-write endpoint must be non-negative.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpointFields - The property failoverWithDataLossGracePeriodMinutes must be provided when failover policy Automatic is selected for the read-write endpoint.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteFailoverPolicy - The failoverPolicy field for the read-write endpoint is required for create or update requests.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpointFieldsForManualPolicy - Grace period value should not be provided when failover policy Manual is selected for the read-write endpoint.   * 400 InstanceFailoverGroupCreateOrUpdateRequestReadOnlyPropertyModified - The create or update instance failover group request body should not modify the read-only property &#39;{0}&#39;.   * 400 InstanceFailoverGroupFailoverRequestOnPrimary - The failover request should be initiated on the secondary server of instance failover group.   * 400 InstanceFailoverGroupPartnerManagedInstanceFromDifferentSubscription - Primary server and the partner server of failover group are from different subscriptions. Cross subscription for servers of failover group is not allowed.   * 400 InvalidAddSecondaryPermission - User does not have sufficient permission to add secondary on the specified server.   * 400 InvalidSku - The user specified an invalid sku.   * 400 ServerNotFound - The requested server was not found.   * 400 FeatureDisabledOnSelectedEdition - User attempted to use a feature which is disabled on current database edition.   * 400 TokenTooLong - The provided token is too long.   * 400 InvalidTargetSubregion - The target server of a non-readable secondary is not in a DR paired Azure region.   * 400 IncorrectReplicationLinkState - The operation expects the database to be in an expected state on the replication link.   * 400 PlannedFailoverTimedOutForDatabase - User invoked planned failover, it timed out, and a specific database appears to be to blame.   * 400 PlannedFailoverTimedOut - User invoked planned failover, and it timed out while trying to contact the partner management service.   * 400 CannotUseReservedDatabaseName - Cannot use reserved database name in this operation.   * 400 InvalidFailoverGroupRegion - Servers specified in an Instance Failover Group need to reside in different regions to provide isolation.   * 400 InstanceFailoverGroupDoesNotExist - Failover group does not exist on a server.   * 400 InstanceFailoverGroupNotSecondary - Failover cannot be initiated from the primary server in a instance failover group.   * 400 InvalidServerName - Invalid server name specified.   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 400 GeoReplicationDatabaseNotSecondary - The operation expects the database to be a replication target.   * 400 UnableToResolveRemoteServer - The remote partner server name could not be resolved due to an invalid server name or DNS connectivity issues.   * 400 RemoteDatabaseCopyPermission - User does not have sufficient permission to create a database copy on the specified server.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ResourceNotFound - The requested resource was not found.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 ServerNotInSubscription - Specified server does not exist on the specified subscription.   * 404 SourceDatabaseNotFound - The source database does not exist.   * 405 UnsupportedReplicationOperation - An unsupported replication operation was initiated on the database.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 409 ConflictingServerOperation - An operation is currently in progress for the server.   * 409 SubscriptionDisabled - Subscription is disabled.   * 409 ConflictingSystemOperationInProgress - A system maintenance operation is in progress on the database and further operations need to wait until it is completed.   * 409 GeoReplicationCannotBecomePrimaryDuringUndo - User attempted to failover or force-terminate a geo-link while the secondary is in a state where it may not be physically consistent and so cannot enter the primary role.   * 409 UpdateSloInProgress - User tried to initiate an incompatible operation while a SLO update was in progress.   * 409 InstanceFailoverGroupAlreadyExists - Failover group already exists on a given server.   * 409 InstanceFailoverGroupBusy - Instance failover group is busy with another operation.   * 409 InstanceFailoverGroupDnsRecordInUse - A duplicate DNS record exists for the requested endpoint.   * 409 InvalidFailoverGroupName - Invalid Instance Failover Group name was supplied.   * 409 InvalidOperationForDatabaseNotInReplicationRelationship - A replication seeding operation was performed on a database that is already in a replication relationship.   * 409 InvalidDatabaseStateForOperation - The operation is not allowed on the database in its current replication state.   * 409 DuplicateGeoDrRelation - The databases are already in a replication relation. This is a duplicate request.   * 409 RemoteDatabaseExists - The destination database name already exists on the destination server.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="instanceFailoverGroupsFailover"></a>
# **instanceFailoverGroupsFailover**
> InstanceFailoverGroup instanceFailoverGroupsFailover(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion)



Fails over from the current primary managed instance to this managed instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceFailoverGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    InstanceFailoverGroupsApi apiInstance = new InstanceFailoverGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String locationName = "locationName_example"; // String | The name of the region where the resource is located.
    String failoverGroupName = "failoverGroupName_example"; // String | The name of the failover group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      InstanceFailoverGroup result = apiInstance.instanceFailoverGroupsFailover(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceFailoverGroupsApi#instanceFailoverGroupsFailover");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **locationName** | **String**| The name of the region where the resource is located. | |
| **failoverGroupName** | **String**| The name of the failover group. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**InstanceFailoverGroup**](InstanceFailoverGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully failed over. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidPartner - The given partners field in create or update instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupCreateOrUpdateRequestDuplicatePartner - One or more of the provided partner servers are already part of the instance failover group. Please make sure the primary server and all of the given partner servers are unique.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidManagedInstanceRegion - The provided partner managed instance region in the instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupCreateOrUpdateRequestUnsupportedPartnerCount - Only one partner region is supported.   * 400 InstanceFailoverGroupCreateOrUpdateRequestUnsupportedPairCount - Only one managed instance pair is supported.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpoint - The readWriteEndpoint field is required for create or update requests.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalid - The create or update instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupUpdateOrDeleteRequestOnSecondary - Modifications to the instance failover group are not allowed on a secondary server. Execute the request on the primary server.   * 400 InstanceFailoverGroupCreateOrUpdateRequestNegativeGracePeriodValues - Grace period value for the read-write endpoint must be non-negative.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpointFields - The property failoverWithDataLossGracePeriodMinutes must be provided when failover policy Automatic is selected for the read-write endpoint.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteFailoverPolicy - The failoverPolicy field for the read-write endpoint is required for create or update requests.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpointFieldsForManualPolicy - Grace period value should not be provided when failover policy Manual is selected for the read-write endpoint.   * 400 InstanceFailoverGroupCreateOrUpdateRequestReadOnlyPropertyModified - The create or update instance failover group request body should not modify the read-only property &#39;{0}&#39;.   * 400 InstanceFailoverGroupFailoverRequestOnPrimary - The failover request should be initiated on the secondary server of instance failover group.   * 400 InstanceFailoverGroupPartnerManagedInstanceFromDifferentSubscription - Primary server and the partner server of failover group are from different subscriptions. Cross subscription for servers of failover group is not allowed.   * 400 InvalidAddSecondaryPermission - User does not have sufficient permission to add secondary on the specified server.   * 400 InvalidSku - The user specified an invalid sku.   * 400 ServerNotFound - The requested server was not found.   * 400 FeatureDisabledOnSelectedEdition - User attempted to use a feature which is disabled on current database edition.   * 400 TokenTooLong - The provided token is too long.   * 400 InvalidTargetSubregion - The target server of a non-readable secondary is not in a DR paired Azure region.   * 400 IncorrectReplicationLinkState - The operation expects the database to be in an expected state on the replication link.   * 400 PlannedFailoverTimedOutForDatabase - User invoked planned failover, it timed out, and a specific database appears to be to blame.   * 400 PlannedFailoverTimedOut - User invoked planned failover, and it timed out while trying to contact the partner management service.   * 400 CannotUseReservedDatabaseName - Cannot use reserved database name in this operation.   * 400 InvalidFailoverGroupRegion - Servers specified in an Instance Failover Group need to reside in different regions to provide isolation.   * 400 InstanceFailoverGroupDoesNotExist - Failover group does not exist on a server.   * 400 InstanceFailoverGroupNotSecondary - Failover cannot be initiated from the primary server in a instance failover group.   * 400 InvalidServerName - Invalid server name specified.   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 400 GeoReplicationDatabaseNotSecondary - The operation expects the database to be a replication target.   * 400 UnableToResolveRemoteServer - The remote partner server name could not be resolved due to an invalid server name or DNS connectivity issues.   * 400 RemoteDatabaseCopyPermission - User does not have sufficient permission to create a database copy on the specified server.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ResourceNotFound - The requested resource was not found.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 ServerNotInSubscription - Specified server does not exist on the specified subscription.   * 404 SourceDatabaseNotFound - The source database does not exist.   * 405 UnsupportedReplicationOperation - An unsupported replication operation was initiated on the database.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 409 ConflictingServerOperation - An operation is currently in progress for the server.   * 409 SubscriptionDisabled - Subscription is disabled.   * 409 ConflictingSystemOperationInProgress - A system maintenance operation is in progress on the database and further operations need to wait until it is completed.   * 409 GeoReplicationCannotBecomePrimaryDuringUndo - User attempted to failover or force-terminate a geo-link while the secondary is in a state where it may not be physically consistent and so cannot enter the primary role.   * 409 UpdateSloInProgress - User tried to initiate an incompatible operation while a SLO update was in progress.   * 409 InstanceFailoverGroupAlreadyExists - Failover group already exists on a given server.   * 409 InstanceFailoverGroupBusy - Instance failover group is busy with another operation.   * 409 InstanceFailoverGroupDnsRecordInUse - A duplicate DNS record exists for the requested endpoint.   * 409 InvalidFailoverGroupName - Invalid Instance Failover Group name was supplied.   * 409 InvalidOperationForDatabaseNotInReplicationRelationship - A replication seeding operation was performed on a database that is already in a replication relationship.   * 409 InvalidDatabaseStateForOperation - The operation is not allowed on the database in its current replication state.   * 409 DuplicateGeoDrRelation - The databases are already in a replication relation. This is a duplicate request.   * 409 RemoteDatabaseExists - The destination database name already exists on the destination server.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="instanceFailoverGroupsForceFailoverAllowDataLoss"></a>
# **instanceFailoverGroupsForceFailoverAllowDataLoss**
> InstanceFailoverGroup instanceFailoverGroupsForceFailoverAllowDataLoss(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion)



Fails over from the current primary managed instance to this managed instance. This operation might result in data loss.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceFailoverGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    InstanceFailoverGroupsApi apiInstance = new InstanceFailoverGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String locationName = "locationName_example"; // String | The name of the region where the resource is located.
    String failoverGroupName = "failoverGroupName_example"; // String | The name of the failover group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      InstanceFailoverGroup result = apiInstance.instanceFailoverGroupsForceFailoverAllowDataLoss(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceFailoverGroupsApi#instanceFailoverGroupsForceFailoverAllowDataLoss");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **locationName** | **String**| The name of the region where the resource is located. | |
| **failoverGroupName** | **String**| The name of the failover group. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**InstanceFailoverGroup**](InstanceFailoverGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully failed over. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidPartner - The given partners field in create or update instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupCreateOrUpdateRequestDuplicatePartner - One or more of the provided partner servers are already part of the instance failover group. Please make sure the primary server and all of the given partner servers are unique.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidManagedInstanceRegion - The provided partner managed instance region in the instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupCreateOrUpdateRequestUnsupportedPartnerCount - Only one partner region is supported.   * 400 InstanceFailoverGroupCreateOrUpdateRequestUnsupportedPairCount - Only one managed instance pair is supported.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpoint - The readWriteEndpoint field is required for create or update requests.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalid - The create or update instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupUpdateOrDeleteRequestOnSecondary - Modifications to the instance failover group are not allowed on a secondary server. Execute the request on the primary server.   * 400 InstanceFailoverGroupCreateOrUpdateRequestNegativeGracePeriodValues - Grace period value for the read-write endpoint must be non-negative.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpointFields - The property failoverWithDataLossGracePeriodMinutes must be provided when failover policy Automatic is selected for the read-write endpoint.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteFailoverPolicy - The failoverPolicy field for the read-write endpoint is required for create or update requests.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpointFieldsForManualPolicy - Grace period value should not be provided when failover policy Manual is selected for the read-write endpoint.   * 400 InstanceFailoverGroupCreateOrUpdateRequestReadOnlyPropertyModified - The create or update instance failover group request body should not modify the read-only property &#39;{0}&#39;.   * 400 InstanceFailoverGroupFailoverRequestOnPrimary - The failover request should be initiated on the secondary server of instance failover group.   * 400 InstanceFailoverGroupPartnerManagedInstanceFromDifferentSubscription - Primary server and the partner server of failover group are from different subscriptions. Cross subscription for servers of failover group is not allowed.   * 400 InvalidAddSecondaryPermission - User does not have sufficient permission to add secondary on the specified server.   * 400 InvalidSku - The user specified an invalid sku.   * 400 ServerNotFound - The requested server was not found.   * 400 FeatureDisabledOnSelectedEdition - User attempted to use a feature which is disabled on current database edition.   * 400 TokenTooLong - The provided token is too long.   * 400 InvalidTargetSubregion - The target server of a non-readable secondary is not in a DR paired Azure region.   * 400 IncorrectReplicationLinkState - The operation expects the database to be in an expected state on the replication link.   * 400 PlannedFailoverTimedOutForDatabase - User invoked planned failover, it timed out, and a specific database appears to be to blame.   * 400 PlannedFailoverTimedOut - User invoked planned failover, and it timed out while trying to contact the partner management service.   * 400 CannotUseReservedDatabaseName - Cannot use reserved database name in this operation.   * 400 InvalidFailoverGroupRegion - Servers specified in an Instance Failover Group need to reside in different regions to provide isolation.   * 400 InstanceFailoverGroupDoesNotExist - Failover group does not exist on a server.   * 400 InstanceFailoverGroupNotSecondary - Failover cannot be initiated from the primary server in a instance failover group.   * 400 InvalidServerName - Invalid server name specified.   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 400 GeoReplicationDatabaseNotSecondary - The operation expects the database to be a replication target.   * 400 UnableToResolveRemoteServer - The remote partner server name could not be resolved due to an invalid server name or DNS connectivity issues.   * 400 RemoteDatabaseCopyPermission - User does not have sufficient permission to create a database copy on the specified server.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ResourceNotFound - The requested resource was not found.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 ServerNotInSubscription - Specified server does not exist on the specified subscription.   * 404 SourceDatabaseNotFound - The source database does not exist.   * 405 UnsupportedReplicationOperation - An unsupported replication operation was initiated on the database.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 409 ConflictingServerOperation - An operation is currently in progress for the server.   * 409 SubscriptionDisabled - Subscription is disabled.   * 409 ConflictingSystemOperationInProgress - A system maintenance operation is in progress on the database and further operations need to wait until it is completed.   * 409 GeoReplicationCannotBecomePrimaryDuringUndo - User attempted to failover or force-terminate a geo-link while the secondary is in a state where it may not be physically consistent and so cannot enter the primary role.   * 409 UpdateSloInProgress - User tried to initiate an incompatible operation while a SLO update was in progress.   * 409 InstanceFailoverGroupAlreadyExists - Failover group already exists on a given server.   * 409 InstanceFailoverGroupBusy - Instance failover group is busy with another operation.   * 409 InstanceFailoverGroupDnsRecordInUse - A duplicate DNS record exists for the requested endpoint.   * 409 InvalidFailoverGroupName - Invalid Instance Failover Group name was supplied.   * 409 InvalidOperationForDatabaseNotInReplicationRelationship - A replication seeding operation was performed on a database that is already in a replication relationship.   * 409 InvalidDatabaseStateForOperation - The operation is not allowed on the database in its current replication state.   * 409 DuplicateGeoDrRelation - The databases are already in a replication relation. This is a duplicate request.   * 409 RemoteDatabaseExists - The destination database name already exists on the destination server.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="instanceFailoverGroupsGet"></a>
# **instanceFailoverGroupsGet**
> InstanceFailoverGroup instanceFailoverGroupsGet(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion)



Gets a failover group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceFailoverGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    InstanceFailoverGroupsApi apiInstance = new InstanceFailoverGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String locationName = "locationName_example"; // String | The name of the region where the resource is located.
    String failoverGroupName = "failoverGroupName_example"; // String | The name of the failover group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      InstanceFailoverGroup result = apiInstance.instanceFailoverGroupsGet(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceFailoverGroupsApi#instanceFailoverGroupsGet");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **locationName** | **String**| The name of the region where the resource is located. | |
| **failoverGroupName** | **String**| The name of the failover group. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**InstanceFailoverGroup**](InstanceFailoverGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified failover group. |  -  |
| **0** | *** Error Responses: ***   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidPartner - The given partners field in create or update instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupCreateOrUpdateRequestDuplicatePartner - One or more of the provided partner servers are already part of the instance failover group. Please make sure the primary server and all of the given partner servers are unique.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidManagedInstanceRegion - The provided partner managed instance region in the instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupCreateOrUpdateRequestUnsupportedPartnerCount - Only one partner region is supported.   * 400 InstanceFailoverGroupCreateOrUpdateRequestUnsupportedPairCount - Only one managed instance pair is supported.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpoint - The readWriteEndpoint field is required for create or update requests.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalid - The create or update instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupUpdateOrDeleteRequestOnSecondary - Modifications to the instance failover group are not allowed on a secondary server. Execute the request on the primary server.   * 400 InstanceFailoverGroupCreateOrUpdateRequestNegativeGracePeriodValues - Grace period value for the read-write endpoint must be non-negative.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpointFields - The property failoverWithDataLossGracePeriodMinutes must be provided when failover policy Automatic is selected for the read-write endpoint.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteFailoverPolicy - The failoverPolicy field for the read-write endpoint is required for create or update requests.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpointFieldsForManualPolicy - Grace period value should not be provided when failover policy Manual is selected for the read-write endpoint.   * 400 InstanceFailoverGroupCreateOrUpdateRequestReadOnlyPropertyModified - The create or update instance failover group request body should not modify the read-only property &#39;{0}&#39;.   * 400 InstanceFailoverGroupFailoverRequestOnPrimary - The failover request should be initiated on the secondary server of instance failover group.   * 400 InstanceFailoverGroupPartnerManagedInstanceFromDifferentSubscription - Primary server and the partner server of failover group are from different subscriptions. Cross subscription for servers of failover group is not allowed.   * 400 InvalidAddSecondaryPermission - User does not have sufficient permission to add secondary on the specified server.   * 400 InvalidSku - The user specified an invalid sku.   * 400 ServerNotFound - The requested server was not found.   * 400 FeatureDisabledOnSelectedEdition - User attempted to use a feature which is disabled on current database edition.   * 400 TokenTooLong - The provided token is too long.   * 400 InvalidTargetSubregion - The target server of a non-readable secondary is not in a DR paired Azure region.   * 400 IncorrectReplicationLinkState - The operation expects the database to be in an expected state on the replication link.   * 400 PlannedFailoverTimedOutForDatabase - User invoked planned failover, it timed out, and a specific database appears to be to blame.   * 400 PlannedFailoverTimedOut - User invoked planned failover, and it timed out while trying to contact the partner management service.   * 400 CannotUseReservedDatabaseName - Cannot use reserved database name in this operation.   * 400 InvalidFailoverGroupRegion - Servers specified in an Instance Failover Group need to reside in different regions to provide isolation.   * 400 InstanceFailoverGroupDoesNotExist - Failover group does not exist on a server.   * 400 InstanceFailoverGroupNotSecondary - Failover cannot be initiated from the primary server in a instance failover group.   * 400 InvalidServerName - Invalid server name specified.   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 400 GeoReplicationDatabaseNotSecondary - The operation expects the database to be a replication target.   * 400 UnableToResolveRemoteServer - The remote partner server name could not be resolved due to an invalid server name or DNS connectivity issues.   * 400 RemoteDatabaseCopyPermission - User does not have sufficient permission to create a database copy on the specified server.   * 404 ResourceNotFound - The requested resource was not found.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 ServerNotInSubscription - Specified server does not exist on the specified subscription.   * 404 SourceDatabaseNotFound - The source database does not exist.   * 405 UnsupportedReplicationOperation - An unsupported replication operation was initiated on the database.   * 409 ConflictingServerOperation - An operation is currently in progress for the server.   * 409 SubscriptionDisabled - Subscription is disabled.   * 409 ConflictingSystemOperationInProgress - A system maintenance operation is in progress on the database and further operations need to wait until it is completed.   * 409 GeoReplicationCannotBecomePrimaryDuringUndo - User attempted to failover or force-terminate a geo-link while the secondary is in a state where it may not be physically consistent and so cannot enter the primary role.   * 409 UpdateSloInProgress - User tried to initiate an incompatible operation while a SLO update was in progress.   * 409 InstanceFailoverGroupAlreadyExists - Failover group already exists on a given server.   * 409 InstanceFailoverGroupBusy - Instance failover group is busy with another operation.   * 409 InstanceFailoverGroupDnsRecordInUse - A duplicate DNS record exists for the requested endpoint.   * 409 InvalidFailoverGroupName - Invalid Instance Failover Group name was supplied.   * 409 InvalidOperationForDatabaseNotInReplicationRelationship - A replication seeding operation was performed on a database that is already in a replication relationship.   * 409 InvalidDatabaseStateForOperation - The operation is not allowed on the database in its current replication state.   * 409 DuplicateGeoDrRelation - The databases are already in a replication relation. This is a duplicate request.   * 409 RemoteDatabaseExists - The destination database name already exists on the destination server.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="instanceFailoverGroupsListByLocation"></a>
# **instanceFailoverGroupsListByLocation**
> InstanceFailoverGroupListResult instanceFailoverGroupsListByLocation(resourceGroupName, locationName, subscriptionId, apiVersion)



Lists the failover groups in a location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceFailoverGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    InstanceFailoverGroupsApi apiInstance = new InstanceFailoverGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String locationName = "locationName_example"; // String | The name of the region where the resource is located.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      InstanceFailoverGroupListResult result = apiInstance.instanceFailoverGroupsListByLocation(resourceGroupName, locationName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceFailoverGroupsApi#instanceFailoverGroupsListByLocation");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **locationName** | **String**| The name of the region where the resource is located. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**InstanceFailoverGroupListResult**](InstanceFailoverGroupListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the failover groups. |  -  |
| **0** | *** Error Responses: ***   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidPartner - The given partners field in create or update instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupCreateOrUpdateRequestDuplicatePartner - One or more of the provided partner servers are already part of the instance failover group. Please make sure the primary server and all of the given partner servers are unique.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidManagedInstanceRegion - The provided partner managed instance region in the instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupCreateOrUpdateRequestUnsupportedPartnerCount - Only one partner region is supported.   * 400 InstanceFailoverGroupCreateOrUpdateRequestUnsupportedPairCount - Only one managed instance pair is supported.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpoint - The readWriteEndpoint field is required for create or update requests.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalid - The create or update instance failover group request body is empty or invalid.   * 400 InstanceFailoverGroupUpdateOrDeleteRequestOnSecondary - Modifications to the instance failover group are not allowed on a secondary server. Execute the request on the primary server.   * 400 InstanceFailoverGroupCreateOrUpdateRequestNegativeGracePeriodValues - Grace period value for the read-write endpoint must be non-negative.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpointFields - The property failoverWithDataLossGracePeriodMinutes must be provided when failover policy Automatic is selected for the read-write endpoint.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteFailoverPolicy - The failoverPolicy field for the read-write endpoint is required for create or update requests.   * 400 InstanceFailoverGroupCreateOrUpdateRequestInvalidReadWriteEndpointFieldsForManualPolicy - Grace period value should not be provided when failover policy Manual is selected for the read-write endpoint.   * 400 InstanceFailoverGroupCreateOrUpdateRequestReadOnlyPropertyModified - The create or update instance failover group request body should not modify the read-only property &#39;{0}&#39;.   * 400 InstanceFailoverGroupFailoverRequestOnPrimary - The failover request should be initiated on the secondary server of instance failover group.   * 400 InstanceFailoverGroupPartnerManagedInstanceFromDifferentSubscription - Primary server and the partner server of failover group are from different subscriptions. Cross subscription for servers of failover group is not allowed.   * 400 InvalidAddSecondaryPermission - User does not have sufficient permission to add secondary on the specified server.   * 400 InvalidSku - The user specified an invalid sku.   * 400 ServerNotFound - The requested server was not found.   * 400 FeatureDisabledOnSelectedEdition - User attempted to use a feature which is disabled on current database edition.   * 400 TokenTooLong - The provided token is too long.   * 400 InvalidTargetSubregion - The target server of a non-readable secondary is not in a DR paired Azure region.   * 400 IncorrectReplicationLinkState - The operation expects the database to be in an expected state on the replication link.   * 400 PlannedFailoverTimedOutForDatabase - User invoked planned failover, it timed out, and a specific database appears to be to blame.   * 400 PlannedFailoverTimedOut - User invoked planned failover, and it timed out while trying to contact the partner management service.   * 400 CannotUseReservedDatabaseName - Cannot use reserved database name in this operation.   * 400 InvalidFailoverGroupRegion - Servers specified in an Instance Failover Group need to reside in different regions to provide isolation.   * 400 InstanceFailoverGroupDoesNotExist - Failover group does not exist on a server.   * 400 InstanceFailoverGroupNotSecondary - Failover cannot be initiated from the primary server in a instance failover group.   * 400 InvalidServerName - Invalid server name specified.   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 400 GeoReplicationDatabaseNotSecondary - The operation expects the database to be a replication target.   * 400 UnableToResolveRemoteServer - The remote partner server name could not be resolved due to an invalid server name or DNS connectivity issues.   * 400 RemoteDatabaseCopyPermission - User does not have sufficient permission to create a database copy on the specified server.   * 404 ResourceNotFound - The requested resource was not found.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 ServerNotInSubscription - Specified server does not exist on the specified subscription.   * 404 SourceDatabaseNotFound - The source database does not exist.   * 405 UnsupportedReplicationOperation - An unsupported replication operation was initiated on the database.   * 409 ConflictingServerOperation - An operation is currently in progress for the server.   * 409 SubscriptionDisabled - Subscription is disabled.   * 409 ConflictingSystemOperationInProgress - A system maintenance operation is in progress on the database and further operations need to wait until it is completed.   * 409 GeoReplicationCannotBecomePrimaryDuringUndo - User attempted to failover or force-terminate a geo-link while the secondary is in a state where it may not be physically consistent and so cannot enter the primary role.   * 409 UpdateSloInProgress - User tried to initiate an incompatible operation while a SLO update was in progress.   * 409 InstanceFailoverGroupAlreadyExists - Failover group already exists on a given server.   * 409 InstanceFailoverGroupBusy - Instance failover group is busy with another operation.   * 409 InstanceFailoverGroupDnsRecordInUse - A duplicate DNS record exists for the requested endpoint.   * 409 InvalidFailoverGroupName - Invalid Instance Failover Group name was supplied.   * 409 InvalidOperationForDatabaseNotInReplicationRelationship - A replication seeding operation was performed on a database that is already in a replication relationship.   * 409 InvalidDatabaseStateForOperation - The operation is not allowed on the database in its current replication state.   * 409 DuplicateGeoDrRelation - The databases are already in a replication relation. This is a duplicate request.   * 409 RemoteDatabaseExists - The destination database name already exists on the destination server.   * 429 SubscriptionTooManyCreateUpdateRequests - Requests beyond max requests that can be processed by available resources.   * 429 SubscriptionTooManyRequests - Requests beyond max requests that can be processed by available resources.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

