QT += network

HEADERS += \
# Models
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudErrorBody.h \
    $${PWD}/OAIDdosCustomPolicies_UpdateTags_request.h \
    $${PWD}/OAIDdosCustomPolicy.h \
    $${PWD}/OAIDdosCustomPolicyPropertiesFormat.h \
    $${PWD}/OAIDdosCustomPolicyPropertiesFormat_publicIPAddresses_inner.h \
    $${PWD}/OAIProtocolCustomSettingsFormat.h \
# APIs
    $${PWD}/OAIDdosCustomPoliciesApi.h \
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
    $${PWD}/OAICloudError.cpp \
    $${PWD}/OAICloudErrorBody.cpp \
    $${PWD}/OAIDdosCustomPolicies_UpdateTags_request.cpp \
    $${PWD}/OAIDdosCustomPolicy.cpp \
    $${PWD}/OAIDdosCustomPolicyPropertiesFormat.cpp \
    $${PWD}/OAIDdosCustomPolicyPropertiesFormat_publicIPAddresses_inner.cpp \
    $${PWD}/OAIProtocolCustomSettingsFormat.cpp \
# APIs
    $${PWD}/OAIDdosCustomPoliciesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
