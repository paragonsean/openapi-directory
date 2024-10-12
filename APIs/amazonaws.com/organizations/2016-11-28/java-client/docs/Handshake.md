

# Handshake

<p>Contains information that must be exchanged to securely establish a relationship between two accounts (an <i>originator</i> and a <i>recipient</i>). For example, when a management account (the originator) invites another account (the recipient) to join its organization, the two accounts exchange information as a series of handshake requests and responses.</p> <p> <b>Note:</b> Handshakes that are <code>CANCELED</code>, <code>ACCEPTED</code>, <code>DECLINED</code>, or <code>EXPIRED</code> show up in lists for only 30 days after entering that state After that they are deleted.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  [optional] |
|**arn** | [**String**](String.md) |  |  [optional] |
|**parties** | [**List**](List.md) |  |  [optional] |
|**state** | [**HandshakeState**](HandshakeState.md) |  |  [optional] |
|**requestedTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**expirationTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**action** | [**ActionType**](ActionType.md) |  |  [optional] |
|**resources** | [**List**](List.md) |  |  [optional] |



