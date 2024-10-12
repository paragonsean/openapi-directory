QT += network

HEADERS += \
# Models
    $${PWD}/OAIServiceEndpointPolicies_Update_request.h \
    $${PWD}/OAIServiceEndpointPolicy.h \
    $${PWD}/OAIServiceEndpointPolicyDefinition.h \
    $${PWD}/OAIServiceEndpointPolicyDefinitionListResult.h \
    $${PWD}/OAIServiceEndpointPolicyDefinitionPropertiesFormat.h \
    $${PWD}/OAIServiceEndpointPolicyListResult.h \
    $${PWD}/OAIServiceEndpointPolicyPropertiesFormat.h \
# APIs
    $${PWD}/OAIServiceEndpointPoliciesApi.h \
    $${PWD}/OAIServiceEndpointPolicyDefinitionsApi.h \
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
    $${PWD}/OAIServiceEndpointPolicies_Update_request.cpp \
    $${PWD}/OAIServiceEndpointPolicy.cpp \
    $${PWD}/OAIServiceEndpointPolicyDefinition.cpp \
    $${PWD}/OAIServiceEndpointPolicyDefinitionListResult.cpp \
    $${PWD}/OAIServiceEndpointPolicyDefinitionPropertiesFormat.cpp \
    $${PWD}/OAIServiceEndpointPolicyListResult.cpp \
    $${PWD}/OAIServiceEndpointPolicyPropertiesFormat.cpp \
# APIs
    $${PWD}/OAIServiceEndpointPoliciesApi.cpp \
    $${PWD}/OAIServiceEndpointPolicyDefinitionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
