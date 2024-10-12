QT += network

HEADERS += \
# Models
    $${PWD}/OAIListCredentialListResponse.h \
    $${PWD}/OAIListIpAccessControlListResponse.h \
    $${PWD}/OAIListOriginationUrlResponse.h \
    $${PWD}/OAIListPhoneNumberResponse.h \
    $${PWD}/OAIListTrunkResponse.h \
    $${PWD}/OAIListTrunkResponse_meta.h \
    $${PWD}/OAIPhone_number_enum_address_requirement.h \
    $${PWD}/OAIRecording_enum_recording_mode.h \
    $${PWD}/OAIRecording_enum_recording_trim.h \
    $${PWD}/OAITrunk_enum_transfer_caller_id.h \
    $${PWD}/OAITrunk_enum_transfer_setting.h \
    $${PWD}/OAITrunking_v1_trunk.h \
    $${PWD}/OAITrunking_v1_trunk_credential_list.h \
    $${PWD}/OAITrunking_v1_trunk_ip_access_control_list.h \
    $${PWD}/OAITrunking_v1_trunk_origination_url.h \
    $${PWD}/OAITrunking_v1_trunk_phone_number.h \
    $${PWD}/OAITrunking_v1_trunk_recording.h \
# APIs
    $${PWD}/OAITrunkingV1CredentialListApi.h \
    $${PWD}/OAITrunkingV1IpAccessControlListApi.h \
    $${PWD}/OAITrunkingV1OriginationUrlApi.h \
    $${PWD}/OAITrunkingV1PhoneNumberApi.h \
    $${PWD}/OAITrunkingV1RecordingApi.h \
    $${PWD}/OAITrunkingV1TrunkApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIListCredentialListResponse.cpp \
    $${PWD}/OAIListIpAccessControlListResponse.cpp \
    $${PWD}/OAIListOriginationUrlResponse.cpp \
    $${PWD}/OAIListPhoneNumberResponse.cpp \
    $${PWD}/OAIListTrunkResponse.cpp \
    $${PWD}/OAIListTrunkResponse_meta.cpp \
    $${PWD}/OAIPhone_number_enum_address_requirement.cpp \
    $${PWD}/OAIRecording_enum_recording_mode.cpp \
    $${PWD}/OAIRecording_enum_recording_trim.cpp \
    $${PWD}/OAITrunk_enum_transfer_caller_id.cpp \
    $${PWD}/OAITrunk_enum_transfer_setting.cpp \
    $${PWD}/OAITrunking_v1_trunk.cpp \
    $${PWD}/OAITrunking_v1_trunk_credential_list.cpp \
    $${PWD}/OAITrunking_v1_trunk_ip_access_control_list.cpp \
    $${PWD}/OAITrunking_v1_trunk_origination_url.cpp \
    $${PWD}/OAITrunking_v1_trunk_phone_number.cpp \
    $${PWD}/OAITrunking_v1_trunk_recording.cpp \
# APIs
    $${PWD}/OAITrunkingV1CredentialListApi.cpp \
    $${PWD}/OAITrunkingV1IpAccessControlListApi.cpp \
    $${PWD}/OAITrunkingV1OriginationUrlApi.cpp \
    $${PWD}/OAITrunkingV1PhoneNumberApi.cpp \
    $${PWD}/OAITrunkingV1RecordingApi.cpp \
    $${PWD}/OAITrunkingV1TrunkApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
