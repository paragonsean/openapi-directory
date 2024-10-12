QT += network

HEADERS += \
# Models
    $${PWD}/OAIInformationProtectionKeyword.h \
    $${PWD}/OAIInformationProtectionPolicies_List_default_response.h \
    $${PWD}/OAIInformationProtectionPolicies_List_default_response_error.h \
    $${PWD}/OAIInformationProtectionPolicy.h \
    $${PWD}/OAIInformationProtectionPolicyList.h \
    $${PWD}/OAIInformationProtectionPolicyProperties.h \
    $${PWD}/OAIInformationType.h \
    $${PWD}/OAISensitivityLabel.h \
# APIs
    $${PWD}/OAIInformationProtectionPoliciesApi.h \
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
    $${PWD}/OAIInformationProtectionKeyword.cpp \
    $${PWD}/OAIInformationProtectionPolicies_List_default_response.cpp \
    $${PWD}/OAIInformationProtectionPolicies_List_default_response_error.cpp \
    $${PWD}/OAIInformationProtectionPolicy.cpp \
    $${PWD}/OAIInformationProtectionPolicyList.cpp \
    $${PWD}/OAIInformationProtectionPolicyProperties.cpp \
    $${PWD}/OAIInformationType.cpp \
    $${PWD}/OAISensitivityLabel.cpp \
# APIs
    $${PWD}/OAIInformationProtectionPoliciesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
