

# EncryptionContractConfiguration

Use encryptionContractConfiguration to configure one or more content encryption keys for your endpoints that use SPEKE 2.0.  The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream.  To configure the encryption contract, specify which audio and video encryption presets to use. Note the following considerations when using encryptionContractConfiguration: encryptionContractConfiguration can be used for DASH endpoints that use SPEKE 2.0. SPEKE 2.0 relies on the CPIX 2.3 specification. You must disable key rotation for this endpoint by setting keyRotationIntervalSeconds to 0. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**presetSpeke20Audio** | [**PresetSpeke20Audio**](PresetSpeke20Audio.md) |  |  |
|**presetSpeke20Video** | [**PresetSpeke20Video**](PresetSpeke20Video.md) |  |  |



