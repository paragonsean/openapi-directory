# FilesComApi.LockEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowAccessByAnyUser** | **Boolean** | Can lock be modified by users other than its creator? | [optional] 
**depth** | **String** | DEPRECATED: Lock depth | [optional] 
**exclusive** | **Boolean** | Is lock exclusive? | [optional] 
**owner** | **String** | Owner of the lock.  This can be any arbitrary string. | [optional] 
**path** | **String** | Path | [optional] 
**recursive** | **Boolean** | Does lock apply to subfolders? | [optional] 
**scope** | **String** | DEPRECATED: Lock scope | [optional] 
**timeout** | **Number** | Lock timeout in seconds | [optional] 
**token** | **String** | Lock token.  Use to release lock. | [optional] 
**type** | **String** | DEPRECATED: Lock type | [optional] 
**userId** | **Number** | Lock creator user ID | [optional] 
**username** | **String** | Lock creator username | [optional] 


